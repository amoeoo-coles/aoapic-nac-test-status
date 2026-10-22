#!/usr/bin/env python3
"""Logical-integrity (relationship) check of every ACI tenant's object graph.
READ-ONLY against the APIC: aaaLogin POST + class GETs only. Credentials come from the environment
(ACI_URL / ACI_USERNAME / ACI_PASSWORD) and, like the APIC session cookie, are never written anywhere.

Graph checked per tenant:  tenant -> VRF -> BD (+subnets, L3Out link) -> AP -> EPG (+domain, static paths)
                           -> contracts (provider/consumer, vzAny, L3Out external EPGs) -> subjects -> filters -> entries
It uses the APIC's own resolution state (Rs objects: state / stateQual / tDn) and faults (faultInst).

Modes
  collect  pull the APIC -> <out>/live-objects.json and <out>/nac-data/integrity.nac.yaml (input for the
           Robot/nac-test suite templates/tests/integrity/)
  report   analyse <out>/live-objects.json (+ optional Robot output.xml) -> integrity-summary.{md,html,json}
  all      collect + report (default)
Usage: integrity_check.py [collect|report|all] --out results/integrity-YYYY-MM-DD [--date D] [--baseline baseline/data]
                          [--robot-xml <out>/robot/output.xml] [--robot-rc N]
Always exits 0 (status is in integrity-summary.json: broken | warnings | healthy | error).
"""
import argparse, collections, datetime as dt, html, ipaddress, json, os, pathlib, re, sys, traceback
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Australia/Melbourne")
CLASSES = [
    "fvTenant", "fvCtx", "vzAny", "vzRsAnyToProv", "vzRsAnyToCons", "vzRsAnyToConsIf",
    "fvBD", "fvRsCtx", "fvSubnet", "fvRsBDToOut",
    "fvAp", "fvAEPg", "fvRsBd", "fvRsProv", "fvRsCons", "fvRsConsIf", "fvRsDomAtt", "fvRsPathAtt",
    "vzBrCP", "vzSubj", "vzRsSubjFiltAtt", "vzInTerm", "vzOutTerm", "vzRsFiltAtt", "vzRsSubjGraphAtt",
    "vzCPIf", "vzRsIf", "vzFilter", "vzEntry",
    "l3extOut", "l3extRsEctx", "l3extInstP", "l3extSubnet", "mgmtInB", "mgmtRsMgmtBD",
]
SYSTEM = {  # objects the APIC creates itself; findings on them are downgraded to info
    "uni/tn-common/ctx-default", "uni/tn-common/ctx-copy", "uni/tn-common/BD-default", "uni/tn-common/ap-default",
    "uni/tn-common/brc-default", "uni/tn-common/out-default", "uni/tn-common/flt-default", "uni/tn-common/flt-arp",
    "uni/tn-common/flt-est", "uni/tn-common/flt-icmp", "uni/tn-mgmt/ctx-oob", "uni/tn-mgmt/ctx-inb",
}
RELATIONS_ONLY = {"infra"}  # fabric-internal tenant: only broken relations + critical/major faults
REL_FAULTS_FAIL = {"F0952", "F0956"}      # failed to form relation to MO
REL_FAULTS_FALLBACK = {"F0756"}           # named relation unresolved, using default target (tn-common)
GRAPH_FAULTS = {"F0758", "F0759", "F1690", "F0764", "F0772"}
FAULT_NAMES = {"F0467": "EPG deployment on path failed", "F0523": "EPG config failed", "F0952": "relation not formed",
               "F0956": "domain relation not formed", "F0756": "named relation fell back to default", "F3891": "leaked subnet invalid",
               "F1298": "EPG deployment on node failed"}
PEN = {"fail": 10, "warn": 3, "info": 0}


def now_mel():
    return dt.datetime.now(TZ)


# ------------------------------------------------------------------ helpers
def tenant_of(dn):
    m = re.search(r"uni/tn-([^/\]]+)", dn or "")
    return m.group(1) if m else None


def parent(dn):
    """Parent DN; '/' inside [...] (e.g. rsdomAtt-[uni/phys-x]) is not a separator."""
    depth, cut = 0, -1
    for i, ch in enumerate(dn):
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
        elif ch == "/" and depth == 0:
            cut = i
    return dn[:cut] if cut > 0 else ""


def short(dn):
    return dn.replace("uni/", "", 1)


# ------------------------------------------------------------------ collect
def collect(out: pathlib.Path):
    import requests, urllib3
    urllib3.disable_warnings()
    url = os.environ["ACI_URL"].rstrip("/")
    s = requests.Session()
    s.verify = False
    r = s.post(f"{url}/api/aaaLogin.json", json={"aaaUser": {"attributes": {
        "name": os.environ["ACI_USERNAME"], "pwd": os.environ["ACI_PASSWORD"]}}}, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"aaaLogin failed: HTTP {r.status_code}")  # never echo the body
    data = {}
    try:
        for c in CLASSES:
            r = s.get(f"{url}/api/class/{c}.json", timeout=120)
            r.raise_for_status()
            data[c] = [list(x.values())[0]["attributes"] for x in r.json()["imdata"]]
        r = s.get(f"{url}/api/class/faultInst.json",
                  params={"query-target-filter": 'wcard(faultInst.dn,"tn-")'}, timeout=120)
        r.raise_for_status()
        data["faultInst"] = [x["faultInst"]["attributes"] for x in r.json()["imdata"]]
    finally:
        try:
            s.post(f"{url}/api/aaaLogout.json", json={"aaaUser": {"attributes": {"name": os.environ["ACI_USERNAME"]}}},
                   timeout=15)
        except Exception:
            pass
    snap = {"schema": 1, "apic_url": url, "pulled_at": now_mel().isoformat(timespec="seconds"),
            "classes": data}
    out.mkdir(parents=True, exist_ok=True)
    (out / "live-objects.json").write_text(json.dumps(snap, indent=1))
    write_nac_data(snap, out / "nac-data")
    return snap


def write_nac_data(snap, d: pathlib.Path):
    """Integrity data model for the Robot templates (key 'integrity', so the config templates ignore it)."""
    import yaml
    C = snap["classes"]
    ten = []
    for t in sorted(C["fvTenant"], key=lambda a: a["name"].lower()):
        tn = t["name"]
        tdn = f"uni/tn-{tn}"
        own = lambda cls: [a for a in C[cls] if tenant_of(a["dn"]) == tn and a["dn"].startswith(tdn + "/")]
        T = {"name": tn, "relations_only": tn in RELATIONS_ONLY}
        T["bridge_domains"] = [{"name": a["name"]} for a in own("fvBD")]
        epgs = []
        for e in own("fvAEPg"):
            m = re.match(rf"^{re.escape(tdn)}/ap-([^/]+)/epg-(.+)$", e["dn"])
            if not m:
                continue
            rels = [{"rn": a["dn"].rsplit("/", 1)[1], "contract": a.get("tnVzBrCPName", "")}
                    for cls in ("fvRsProv", "fvRsCons") for a in C[cls] if parent(a["dn"]) == e["dn"]]
            epgs.append({"ap": m.group(1), "name": m.group(2), "contract_relations": rels})
        T["endpoint_groups"] = epgs
        T["contracts"] = [{"name": a["name"]} for a in own("vzBrCP")]
        T["l3outs"] = [{"name": a["name"]} for a in own("l3extOut")]
        if T["relations_only"]:
            T["bridge_domains"], T["endpoint_groups"], T["contracts"], T["l3outs"] = [], [], [], []
        ten.append(T)
    d.mkdir(parents=True, exist_ok=True)
    (d / "integrity.nac.yaml").write_text(yaml.safe_dump({"integrity": {"tenants": ten}}, sort_keys=False))


# ------------------------------------------------------------------ model + checks
class Analyser:
    def __init__(self, snap, baseline_tenants):
        self.C = snap["classes"]
        self.base = baseline_tenants
        self.F = []
        self._idx()

    def add(self, sev, check, dn, reason, fix, tenant=None, cat="relation"):
        tenant = tenant or tenant_of(dn)
        system = dn in SYSTEM
        if system and sev != "info":
            reason += " (APIC system default object - informational)"
            sev = "info"
        if tenant in RELATIONS_ONLY and sev != "fail" and cat != "fault":
            return
        self.F.append({"severity": sev, "check": check, "tenant": tenant, "dn": dn, "reason": reason,
                       "fix": fix, "category": cat, "system": system})

    def _idx(self):
        C = self.C
        by = lambda cls: {a["dn"]: a for a in C.get(cls, [])}
        kids = lambda cls: _group(C.get(cls, []))
        self.tenants = {a["name"]: a for a in C["fvTenant"]}
        self.vrfs, self.bds, self.aps, self.epgs = by("fvCtx"), by("fvBD"), by("fvAp"), by("fvAEPg")
        self.brc, self.subj, self.flt, self.l3o = by("vzBrCP"), by("vzSubj"), by("vzFilter"), by("l3extOut")
        self.instp, self.inb, self.cif = by("l3extInstP"), by("mgmtInB"), by("vzCPIf")
        self.any = {parent(a["dn"]): a for a in C.get("vzAny", [])}
        self.rsctx = {parent(a["dn"]): a for a in C.get("fvRsCtx", [])}
        self.rsbd = {parent(a["dn"]): a for a in C.get("fvRsBd", [])}
        self.rsectx = {parent(a["dn"]): a for a in C.get("l3extRsEctx", [])}
        self.rsmgmtbd = {parent(a["dn"]): a for a in C.get("mgmtRsMgmtBD", [])}
        self.rsif = {parent(a["dn"]): a for a in C.get("vzRsIf", [])}
        self.subnets, self.bdout = kids("fvSubnet"), kids("fvRsBDToOut")
        self.dom, self.paths = kids("fvRsDomAtt"), kids("fvRsPathAtt")
        self.prov, self.cons, self.consif = kids("fvRsProv"), kids("fvRsCons"), kids("fvRsConsIf")
        self.anyprov, self.anycons, self.anyconsif = kids("vzRsAnyToProv"), kids("vzRsAnyToCons"), kids("vzRsAnyToConsIf")
        self.subjs = _group(C.get("vzSubj", []))
        self.sfilt = kids("vzRsSubjFiltAtt")
        self.graph = kids("vzRsSubjGraphAtt")
        terms = {a["dn"]: parent(a["dn"]) for a in C.get("vzInTerm", []) + C.get("vzOutTerm", [])}
        self.termfilt = collections.defaultdict(list)
        for a in C.get("vzRsFiltAtt", []):
            subj = terms.get(parent(a["dn"]))
            if subj:
                self.termfilt[subj].append(a)
        self.entries = kids("vzEntry")
        self.instps = _group(C.get("l3extInstP", []))
        self.extsub = kids("l3extSubnet")
        self.bd_users = collections.defaultdict(list)
        for e, rs in self.rsbd.items():
            if rs.get("tDn"):
                self.bd_users[rs["tDn"]].append(e)
        for e, rs in self.rsmgmtbd.items():
            if rs.get("tDn"):
                self.bd_users[rs["tDn"]].append(e)
        self.faults = [f for f in self.C.get("faultInst", []) if tenant_of(f["dn"])]

    # -- graph resolution
    def bd_vrf(self, bd):
        rs = self.rsctx.get(bd)
        return rs["tDn"] if rs and rs.get("state") == "formed" and rs.get("tDn") in self.vrfs else None

    def src_info(self, src):
        """(kind, vrf_dn, ap_dn) for a contract provider/consumer parent DN."""
        if src in self.epgs:
            rs = self.rsbd.get(src)
            bd = rs.get("tDn") if rs and rs.get("state") == "formed" else None
            return "EPG", (self.bd_vrf(bd) if bd else None), parent(src)
        if src in self.instp:
            rs = self.rsectx.get(parent(src))
            return "ExtEPG", (rs["tDn"] if rs and rs.get("state") == "formed" else None), None
        if src.endswith("/any"):
            return "vzAny", parent(src), None
        if src in self.inb:
            rs = self.rsmgmtbd.get(src)
            return "InbMgmtEPG", (self.bd_vrf(rs["tDn"]) if rs and rs.get("tDn") else None), None
        return "other", None, None

    def contract_usage(self):
        use = collections.defaultdict(lambda: {"prov": [], "cons": []})
        for coll, role in ((self.prov, "prov"), (self.cons, "cons"), (self.anyprov, "prov"), (self.anycons, "cons")):
            for src, rels in coll.items():
                for rs in rels:
                    if rs.get("state") == "formed" and rs.get("tDn"):
                        use[rs["tDn"]][role].append(src)
        for coll in (self.consif, self.anyconsif):
            for src, rels in coll.items():
                for rs in rels:
                    rif = self.rsif.get(rs.get("tDn", ""))
                    if rs.get("state") == "formed" and rif and rif.get("tDn"):
                        use[rif["tDn"]]["cons"].append(src)
        return use

    # -- checks
    def run(self):
        self.check_tenants()
        self.check_vrfs()
        self.check_bds()
        self.check_aps_epgs()
        self.check_contracts()
        self.check_l3outs()
        self.check_faults()
        return self.F

    def check_tenants(self):
        for tn, t in self.tenants.items():
            tdn = t["dn"]
            has = any(d.startswith(tdn + "/") for coll in (self.vrfs, self.bds, self.aps, self.brc, self.l3o) for d in coll)
            if not has:
                self.add("warn", "Tenant empty", tdn, "Tenant has no VRF, BD, application profile, contract or L3Out.",
                         "Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects.",
                         cat="hygiene")

    def check_vrfs(self):
        for v, a in self.vrfs.items():
            tn = tenant_of(v)
            if a.get("pcEnfPref") == "unenforced":
                self.add("warn", "VRF unenforced", v, "Policy enforcement is 'unenforced': every EPG in the VRF talks to "
                         "every other EPG without contracts.", "Set pcEnfPref=enforced (NaC: enforcement_preference: "
                         "enforced) and model the required contracts.", cat="security")
            users = [b for b in self.bds if self.bd_vrf(b) == v]
            l3 = [o for o, rs in self.rsectx.items() if rs.get("tDn") == v]
            if not users and not l3:
                self.add("warn", "VRF unused", v, "No bridge domain or L3Out is attached to this VRF.",
                         "Remove the VRF or attach the BDs that should live in it.", cat="hygiene")
            anyo = self.any.get(v)
            members = [e for e, ea in self.epgs.items() if ea.get("prefGrMemb") == "include"
                       and self.src_info(e)[1] == v]
            if anyo and anyo.get("prefGrMemb") == "enabled":
                self.add("warn", "Preferred group enabled", v, f"Preferred group is enabled on vzAny; {len(members)} "
                         "member EPG(s) talk to each other without contracts.", "Use preferred groups only for "
                         "migration; replace with explicit contracts and keep the member list small.", cat="security")
            elif members:
                self.add("warn", "Preferred group member without group", v, f"{len(members)} EPG(s) are preferred-group "
                         "members but the VRF's preferred group is disabled, so the setting has no effect.",
                         "Set prefGrMemb=exclude on the EPGs, or enable the group deliberately.", cat="design")
            p, c = self.anyprov.get(v + "/any", []), self.anycons.get(v + "/any", [])
            if p or c:
                names = ", ".join(sorted({r.get("tnVzBrCPName", "") for r in p + c}))
                self.add("warn", "vzAny contract", v, f"vzAny provides {len(p)} / consumes {len(c)} contract(s) "
                         f"({names}); this applies to EVERY EPG and external EPG in the VRF.",
                         "Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); "
                         "keep its filters specific.", cat="security")
            for rs in p + c:
                if rs.get("state") != "formed":
                    self.add("fail", "vzAny contract missing", v, f"vzAny refers to contract "
                             f"'{rs.get('tnVzBrCPName')}' which does not exist (state {rs.get('state')}).",
                             "Create the contract or remove the vzAny relation.")

    def check_bds(self):
        by_vrf = collections.defaultdict(list)
        for b, a in self.bds.items():
            tn = tenant_of(b)
            rs = self.rsctx.get(b)
            subs = self.subnets.get(b, [])
            if not rs:
                self.add("fail", "BD has no VRF", b, "Bridge domain has no fvRsCtx relation.",
                         "Attach the BD to a VRF (NaC: bridge_domains[].vrf).")
            elif rs.get("state") != "formed" or not rs.get("tDn"):
                self.add("fail", "BD VRF missing-target", b, f"BD points to VRF '{rs.get('tnFvCtxName')}' which does "
                         f"not exist in tenant {tn} or in tenant common (state {rs.get('state')}). The BD and every EPG "
                         "in it cannot be deployed.", f"Create VRF '{rs.get('tnFvCtxName')}' in {tn} (or common), or "
                         "point the BD to an existing VRF.")
            elif rs.get("stateQual") == "mismatch-target":
                self.add("fail", "BD VRF missing-target", b, f"BD points to VRF '{rs.get('tnFvCtxName')}' which does "
                         f"not exist; APIC fell back to {short(rs['tDn'])} (stateQual mismatch-target).",
                         f"Create VRF '{rs.get('tnFvCtxName')}' or point the BD to an existing VRF.")
            elif rs.get("stateQual") == "default-target":
                self.add("warn", "BD VRF fallback to common", b, "BD has no VRF name (tnFvCtxName empty) and silently "
                         f"falls back to {short(rs['tDn'])}.", "Set the VRF explicitly on the BD.")
            elif tenant_of(rs["tDn"]) != tn:
                self.add("info", "BD uses common VRF", b, f"VRF '{rs.get('tnFvCtxName')}' is not in {tn}; it "
                         f"resolved to {short(rs['tDn'])} (shared-services design).",
                         "OK if intended; if not, create the VRF in the tenant (a same-named VRF in the tenant takes "
                         "precedence).", cat="design")
            l3 = a.get("unicastRoute") == "yes"
            if l3 and not subs:
                self.add("warn", "L3 BD without subnet", b, "Unicast routing is enabled but the BD has no subnet "
                         "(no gateway; IP learning without a subnet).", "Add the gateway subnet, or disable unicast "
                         "routing if the BD is meant to be Layer-2 only.", cat="design")
            if not l3 and subs:
                self.add("warn", "Subnet on L2 BD", b, f"{len(subs)} subnet(s) configured but unicast routing is "
                         "disabled, so the gateway is not active.", "Enable unicast routing or remove the subnets.",
                         cat="design")
            if not l3 and (a.get("arpFlood") != "yes" or a.get("unkMacUcastAct") != "flood"):
                self.add("warn", "L2 BD settings", b, f"Layer-2 BD with arpFlood={a.get('arpFlood')}, "
                         f"unkMacUcastAct={a.get('unkMacUcastAct')}; silent hosts may be unreachable.",
                         "For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood.", cat="design")
            if l3 and subs and (a.get("arpFlood") == "yes" or a.get("unkMacUcastAct") == "flood"):
                self.add("info", "L3 BD flooding", b, f"Routed BD with arpFlood={a.get('arpFlood')}, "
                         f"unkMacUcastAct={a.get('unkMacUcastAct')} (legacy/migration style).",
                         "For a pure L3 BD consider hardware proxy and ARP flooding off.", cat="design")
            if not self.bd_users.get(b):
                self.add("warn", "BD unused", b, "No EPG is attached to this bridge domain.",
                         "Remove the BD or attach the intended EPGs.", cat="hygiene")
            for o in self.bdout.get(b, []):
                if o.get("stateQual") in ("default-target", "mismatch-target") or o.get("state") != "formed" or (
                        o.get("tnL3extOutName") and o.get("tDn", "").endswith("/out-default")
                        and o.get("tnL3extOutName") != "default"):
                    self.add("fail", "BD L3Out missing-target", b, f"BD is associated to L3Out "
                             f"'{o.get('tnL3extOutName')}' which does not exist; APIC fell back to "
                             f"{short(o.get('tDn') or '?')}, so the BD subnets are not advertised as intended.",
                             f"Create L3Out '{o.get('tnL3extOutName')}' or remove the BD-to-L3Out association.")
            vrf = self.bd_vrf(b)
            if vrf:
                for s in subs:
                    try:
                        by_vrf[vrf].append((ipaddress.ip_interface(s["ip"]).network, b, s["ip"]))
                    except ValueError:
                        pass
        for vrf, nets in by_vrf.items():
            seen = set()
            for i, (n1, b1, ip1) in enumerate(nets):
                for n2, b2, ip2 in nets[i + 1:]:
                    if n1.version == n2.version and n1.overlaps(n2) and (b1, ip1, b2, ip2) not in seen:
                        seen.add((b1, ip1, b2, ip2))
                        self.add("fail", "Overlapping subnets in VRF", b1, f"Subnet {ip1} overlaps {ip2} on "
                                 f"{short(b2)} in VRF {short(vrf)}.", "Re-address one of the subnets; subnets must be "
                                 "unique within a VRF.")

    def check_aps_epgs(self):
        for ap in self.aps:
            if not any(parent(e) == ap for e in self.epgs):
                self.add("warn", "AP without EPGs", ap, "Application profile contains no EPG.",
                         "Remove the empty application profile or add its EPGs.", cat="hygiene")
        for e, a in self.epgs.items():
            tn = tenant_of(e)
            if tn in RELATIONS_ONLY:
                continue
            rs = self.rsbd.get(e)
            if not rs:
                self.add("fail", "EPG has no BD", e, "EPG has no fvRsBd relation.", "Attach the EPG to a BD.")
            elif rs.get("state") != "formed" or not rs.get("tDn"):
                self.add("fail", "EPG BD missing-target", e, f"EPG points to BD '{rs.get('tnFvBDName')}' which does "
                         f"not exist (state {rs.get('state')}).", f"Create BD '{rs.get('tnFvBDName')}' or fix the "
                         "EPG's bridge_domain.")
            else:
                bd = rs["tDn"]
                if rs.get("stateQual") == "mismatch-target":
                    self.add("fail", "EPG BD missing-target", e, f"EPG points to BD '{rs.get('tnFvBDName')}' which "
                             f"does not exist; APIC fell back to {short(bd)}.", f"Create BD '{rs.get('tnFvBDName')}' "
                             "or fix the EPG's bridge_domain.")
                elif rs.get("stateQual") == "default-target":
                    self.add("warn", "EPG BD fallback to common", e, f"EPG has no BD name and falls back to "
                             f"{short(bd)}.", "Set the BD explicitly on the EPG.")
                if not self.bd_vrf(bd):
                    vr = self.rsctx.get(bd, {}).get("tnFvCtxName", "")
                    self.add("fail", "EPG chain broken (BD has no VRF)", e, f"EPG -> {short(bd)} resolves, but that "
                             f"BD's VRF '{vr}' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context "
                             "Not present').", f"Fix the VRF of {short(bd)} first; the EPG recovers automatically.")
            doms = self.dom.get(e, [])
            if not doms:
                self.add("info", "EPG without domain", e, "No domain (fvRsDomAtt): the EPG cannot be deployed on any "
                         "leaf port or VMM.", "Associate a physical/VMM domain if the EPG should carry endpoints.",
                         cat="design")
            for d in doms:
                if d.get("state") != "formed":
                    self.add("fail", "EPG domain missing-target", e, f"Domain {d.get('tDn')} does not exist "
                             f"(state {d.get('state')}).", f"Create domain {d.get('tDn')} (with VLAN pool/AAEP) or "
                             "associate an existing one.")
            if not self.paths.get(e):
                self.add("info", "EPG without static path", e, "No static path bindings (fvRsPathAtt).",
                         "Expected for VMM/AAEP-bound EPGs; otherwise add static ports.", cat="design")
            rels = self.prov.get(e, []) + self.cons.get(e, []) + self.consif.get(e, [])
            for r in rels:
                kind = "provides" if "/rsprov-" in r["dn"] else "consumes"
                name = r.get("tnVzBrCPName") or r.get("tnVzCPIfName", "")
                if r.get("state") != "formed" or not r.get("tDn"):
                    self.add("fail", "EPG contract missing-target", e, f"EPG {kind} contract '{name}' which does not "
                             f"exist in {tn} or common (state {r.get('state')}).", f"Create contract '{name}' or remove "
                             "the relation.")
                elif tenant_of(r["tDn"]) != tn:
                    self.add("info", "EPG uses common contract", e, f"EPG {kind} '{name}' resolved to "
                             f"{short(r['tDn'])}.", "OK for shared contracts; a same-named contract in the tenant "
                             "would silently take precedence.", cat="design")
            if not rels and a.get("prefGrMemb") != "include":
                vrf = self.src_info(e)[1]
                via_any = vrf and (self.anyprov.get(vrf + "/any") or self.anycons.get(vrf + "/any"))
                if via_any:
                    self.add("info", "EPG only via vzAny", e, "EPG has no own contracts; it only inherits the VRF's "
                             "vzAny contracts.", "OK if intended.", cat="design")
                else:
                    self.add("warn", "EPG isolated (no contracts)", e, "EPG neither provides nor consumes any contract, "
                             "so in an enforced VRF it can only talk inside itself.", "Add provider/consumer contracts "
                             "for the flows it needs, or remove the EPG if unused.", cat="design")

    def check_contracts(self):
        use = self.contract_usage()
        filt_used = collections.defaultdict(list)
        sigs = collections.defaultdict(list)
        for c, a in self.brc.items():
            tn = tenant_of(c)
            subs = [s for s in self.subjs.get(c, [])]
            if not subs:
                self.add("fail", "Contract without subjects", c, "Contract has no subject, so it permits nothing.",
                         "Add a subject with specific filters, or delete the contract.")
            fsig, any_hits = set(), []
            for s in subs:
                rels = self.sfilt.get(s["dn"], []) + self.termfilt.get(s["dn"], [])
                if not rels:
                    self.add("fail", "Subject without filters", s["dn"], "Contract subject has no filter, so it "
                             "permits nothing.", "Attach specific filters to the subject.")
                for r in rels:
                    if r.get("state") != "formed" or not r.get("tDn"):
                        self.add("fail", "Subject filter missing-target", s["dn"], f"Subject refers to filter "
                                 f"'{r.get('tnVzFilterName')}' which does not exist (state {r.get('state')}).",
                                 f"Create filter '{r.get('tnVzFilterName')}' or remove the relation.")
                        continue
                    f = r["tDn"]
                    filt_used[f].append(c)
                    fsig.add(f)
                    for en in self.entries.get(f, []):
                        if en.get("etherT") in ("unspecified", "") or (
                                en.get("etherT") in ("ip", "ipv4", "ipv6") and en.get("prot") in ("unspecified", "")):
                            any_hits.append(f"{short(f)} entry {en.get('name')}")
                for g in self.graph.get(s["dn"], []):
                    fsig.add("graph:" + g.get("tDn", ""))
            if any_hits:
                self.add("warn", "Permit-any filter", c, "Contract permits ALL traffic via " + ", ".join(any_hits[:3]) +
                         " (etherType/protocol unspecified).", "Replace with specific filters (protocol + destination "
                         "port), e.g. tcp/443; keep 'common/default' for lab use only.", cat="security")
            u = use.get(c, {"prov": [], "cons": []})
            p, q = u["prov"], u["cons"]
            if not p and not q:
                self.add("warn", "Contract unused", c, "Contract is neither provided nor consumed.",
                         "Delete it or attach it to the intended provider and consumer EPGs.", cat="hygiene")
            elif not q:
                self.add("warn", "Contract provided, never consumed", c, f"Provided by {len(p)} object(s) (e.g. "
                         f"{short(p[0])}) but no consumer, so it permits no flow.",
                         "Add the consumer EPG(s) or remove the provider relation.", cat="relation")
            elif not p:
                self.add("warn", "Contract consumed, never provided", c, f"Consumed by {len(q)} object(s) (e.g. "
                         f"{short(q[0])}) but no provider, so it permits no flow.",
                         "Add the provider EPG(s) or remove the consumer relation.", cat="relation")
            scope = a.get("scope", "context")
            pairs, vrfset = [], set()
            for pv in p:
                pk, pvrf, pap = self.src_info(pv)
                for cv in q:
                    ck, cvrf, cap = self.src_info(cv)
                    if not pvrf or not cvrf:
                        continue
                    vrfset |= {pvrf, cvrf}
                    ok = {"context": pvrf == cvrf,
                          "application-profile": pvrf == cvrf and (pap is None or cap is None or pap == cap),
                          "tenant": tenant_of(pv) == tenant_of(cv), "global": True}.get(scope, True)
                    pairs.append((pv, cv, ok, pvrf, cvrf))
            # an endpoint is orphaned when none of its pairs is inside the contract scope
            orphan = [x for x in set(p) | set(q) if any(x in (a_, b_) for a_, b_, _, _, _ in pairs)
                      and not any(ok and x in (a_, b_) for a_, b_, ok, _, _ in pairs)]
            blocked = [x for x in pairs if not x[2]]
            if orphan:
                ex_ = next(x for x in blocked if x[0] in orphan or x[1] in orphan)
                self.add("fail", "Contract scope mismatch", c, f"Scope is '{scope}' but {len(orphan)} provider/consumer "
                         f"object(s) have no partner inside that scope, so their flows are NOT permitted, e.g. "
                         f"{short(ex_[0])} ({short(ex_[3])}) -> {short(ex_[1])} ({short(ex_[4])}).",
                         "Widen the scope (tenant for inter-VRF in one tenant, global across tenants) and leak the "
                         "subnets (shared), or move the EPGs into the same VRF/AP.")
            elif blocked:
                self.add("info", "Contract scope limits pairs", c, f"Scope '{scope}' blocks {len(blocked)} of "
                         f"{len(pairs)} provider/consumer combinations (e.g. {short(blocked[0][0])} -> "
                         f"{short(blocked[0][1])}); every user still has an in-scope partner.",
                         "OK if intended (per-AP isolation); otherwise widen the scope.", cat="design")
            elif scope in ("tenant", "global") and len(vrfset) == 1 and p and q:
                self.add("info", "Contract scope wider than used", c, f"Scope '{scope}' but all users are in one VRF "
                         f"({short(next(iter(vrfset)))}).", "Narrow the scope to 'context' unless inter-VRF use is "
                         "planned.", cat="design")
            if subs and (p or q):
                sigs[(tn, frozenset(fsig), frozenset(p), frozenset(q))].append(c)
        for (tn, fs, p, q), cs in sigs.items():
            if len(cs) > 1 and fs:
                for c in cs[1:]:
                    self.add("warn", "Duplicate contract", c, f"Same filters, providers and consumers as "
                             f"{short(cs[0])}: the contract is redundant.", f"Delete {short(c)} (keep "
                             f"{short(cs[0])}).", cat="hygiene")
        for f in self.flt:
            if not self.entries.get(f):
                sev = "fail" if filt_used.get(f) else "warn"
                self.add(sev, "Filter without entries", f, "Filter has no entries" + (
                    f" but is used by {short(filt_used[f][0])}, so that subject matches nothing." if filt_used.get(f)
                    else "."), "Add the intended entries (ether type, protocol, ports) or delete the filter.")
            elif not filt_used.get(f) and not any(r.get("tDn") == f for r in
                                                   [x for v in self.sfilt.values() for x in v]):
                self.add("info", "Filter unused", f, "Filter is not referenced by any contract subject.",
                         "Delete it if not needed.", cat="hygiene")

    def check_l3outs(self):
        for o, a in self.l3o.items():
            rs = self.rsectx.get(o)
            if not rs:
                self.add("fail", "L3Out has no VRF", o, "L3Out has no l3extRsEctx relation.", "Set the L3Out VRF.")
            elif rs.get("state") != "formed" or not rs.get("tDn"):
                self.add("fail", "L3Out VRF missing-target", o, f"L3Out points to VRF '{rs.get('tnFvCtxName')}' which "
                         f"does not exist (state {rs.get('state')}).", "Create the VRF or fix the L3Out VRF.")
            elif rs.get("stateQual") == "mismatch-target":
                self.add("fail", "L3Out VRF missing-target", o, f"L3Out points to VRF '{rs.get('tnFvCtxName')}' which "
                         f"does not exist; APIC fell back to {short(rs['tDn'])}.", "Create the VRF or fix the L3Out VRF.")
            elif rs.get("stateQual") == "default-target":
                self.add("warn", "L3Out VRF fallback to common", o, f"L3Out has no VRF name and falls back to "
                         f"{short(rs['tDn'])}.", "Set the VRF explicitly.")
            ext = self.instps.get(o, [])
            if not ext:
                self.add("warn", "L3Out without external EPG", o, "L3Out has no external EPG (l3extInstP), so no "
                         "external prefix is classified and no contract can apply.", "Add an external EPG with the "
                         "external subnets and contracts.", cat="design")
            for x in ext:
                if not self.prov.get(x["dn"]) and not self.cons.get(x["dn"]) and not self.consif.get(x["dn"]):
                    self.add("warn", "External EPG without contracts", x["dn"], "External EPG has no contracts, so "
                             "no traffic is permitted between the outside and internal EPGs.",
                             "Provide/consume the contracts for the external flows.", cat="design")
                for r in self.prov.get(x["dn"], []) + self.cons.get(x["dn"], []):
                    if r.get("state") != "formed" or not r.get("tDn"):
                        self.add("fail", "External EPG contract missing-target", x["dn"], f"External EPG uses contract "
                                 f"'{r.get('tnVzBrCPName')}' which does not exist.", "Create the contract or remove "
                                 "the relation.")

    def check_faults(self):
        self.fault_rows = []
        graph = collections.defaultdict(list)
        for f in self.faults:
            if f.get("severity") == "cleared":
                continue
            m = re.search(r"\[(uni/tn-[^\]]+)\]", f["dn"])
            aff = m.group(1) if m else f["dn"].split("/fault-")[0]
            row = {"tenant": tenant_of(aff), "severity": f["severity"], "code": f["code"], "dn": f["dn"],
                   "affected": aff, "descr": f.get("descr", ""), "tca": f.get("descr", "").startswith("TCA:")
                   or f.get("type") == "operational" and f["code"].startswith("F11")}
            self.fault_rows.append(row)
            if f["code"] in GRAPH_FAULTS and "GraphInst_C-[" in f["dn"]:
                graph[aff].append(row)
        for c, rows in graph.items():
            msg = rows[0]["descr"]
            for r in rows:
                if "device context" in r["descr"].lower() or "LDevCtx" in r["descr"]:
                    msg = r["descr"]
                    break
            g = re.search(r"G-\[([^\]]+)\]", rows[0]["dn"])
            self.add("fail", "Contract service graph not instantiated", c, f"Contract redirects through service graph "
                     f"{short(g.group(1)) if g else '?'} which cannot be deployed ({len(rows)} faults, e.g. "
                     f"{rows[0]['code']}: {msg.strip()[:140]}); traffic on this contract is dropped.",
                     "Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the "
                     "graph from the subject.")
        covered = lambda row: any(x["severity"] in ("fail", "warn") and x["tenant"] == row["tenant"] and (
            row["affected"].startswith(x["dn"]) or x["dn"].startswith(row["affected"])) for x in self.F)
        seen = set()
        for row in self.fault_rows:
            row["covered"] = covered(row)
            key = (row["code"], row["affected"])
            if row["tca"] or key in seen:
                continue
            seen.add(key)
            sev = row["severity"]
            if sev in ("critical", "major"):
                self.add("fail", f"{sev.capitalize()} fault {row['code']}" + (f" ({FAULT_NAMES[row['code']]})" if row["code"] in FAULT_NAMES else ""), row["affected"], row["descr"][:300],
                         fault_fix(row), tenant=row["tenant"], cat="fault")
            elif row["covered"]:
                continue
            elif row["code"] in REL_FAULTS_FAIL:
                self.add("fail", f"Relation fault {row['code']}", row["affected"], row["descr"][:300], fault_fix(row),
                         tenant=row["tenant"], cat="fault")
            elif row["code"] in REL_FAULTS_FALLBACK:
                self.add("warn", f"Relation fallback {row['code']}", row["affected"], row["descr"][:300],
                         fault_fix(row), tenant=row["tenant"], cat="fault")
            elif sev in ("minor", "warning") and row["tenant"] not in RELATIONS_ONLY:
                self.add("warn", f"Config fault {row['code']}", row["affected"], row["descr"][:300], fault_fix(row),
                         tenant=row["tenant"], cat="fault")


def fault_fix(row):
    c, d = row["code"], row["descr"]
    if c == "F0467":
        return "Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port."
    if c == "F0756":
        return "Create the named target policy (or correct its name); the object is silently using a tn-common default."
    if c in ("F0952", "F0956"):
        return "Create the referenced object or fix the relation name."
    if c == "F3891":
        return "The leaked subnet must match an existing BD/EPG subnet in the VRF; correct the prefix or remove the leak."
    if c == "F0523":
        return "Fix the EPG's dependency named in the fault (BD/VRF, management zone, etc.)."
    if c == "F1298":
        return "Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config)."
    return "See the APIC fault description and resolve the referenced object."


def _group(rows):
    g = collections.defaultdict(list)
    for a in rows:
        g[parent(a["dn"])].append(a)
    return g


# ------------------------------------------------------------------ scorecard + recommendations
def scorecard(A: Analyser, F):
    rows = []
    for tn in sorted(A.tenants, key=str.lower):
        tdn = f"uni/tn-{tn}/"
        cnt = lambda coll: sum(1 for d in coll if d.startswith(tdn))
        mine = [f for f in F if f["tenant"] == tn]
        nf = sum(f["severity"] == "fail" for f in mine)
        nw = sum(f["severity"] == "warn" for f in mine)
        ni = sum(f["severity"] == "info" for f in mine)
        flt = [r for r in A.fault_rows if r["tenant"] == tn]
        score = max(0, 100 - PEN["fail"] * nf - PEN["warn"] * nw)
        rows.append({"tenant": tn, "in_baseline": tn in A.base,
                     "scope": "relations+faults only (fabric-internal)" if tn in RELATIONS_ONLY else "full",
                     "vrf": cnt(A.vrfs), "bd": cnt(A.bds), "subnet": sum(len(v) for k, v in A.subnets.items()
                                                                         if k.startswith(tdn)),
                     "ap": cnt(A.aps), "epg": cnt(A.epgs), "contract": cnt(A.brc), "filter": cnt(A.flt),
                     "l3out": cnt(A.l3o), "broken": nf, "warnings": nw, "info": ni,
                     "faults_crit_major": sum(r["severity"] in ("critical", "major") for r in flt),
                     "faults_total": len(flt), "score": score,
                     "status": "BROKEN" if nf else ("WARN" if nw else "HEALTHY")})
    return rows


NAME_BAD = re.compile(r"^(vlan\d*|test\w*|\d+\.\d+\.\d+\.\d+.*|new\w*|temp\w*)$", re.I)


def recommendations(A: Analyser, F, sc):
    R = []
    by = collections.defaultdict(list)
    for f in F:
        by[f["check"]].append(f)
    ex = lambda chk, n=3: ", ".join(short(f["dn"]) for f in by[chk][:n])

    def rec(title, why, how, checks=()):
        n = sum(len(by[c]) for c in checks) if checks else None
        R.append({"title": title, "found": why, "action": how, "count": n})

    broken = [c for c in by if any(f["severity"] == "fail" for f in by[c])]
    if broken:
        rec("Fix the broken relations first", f"{sum(1 for f in F if f['severity'] == 'fail')} broken relation(s) "
            f"in {len({f['tenant'] for f in F if f['severity'] == 'fail'})} tenant(s): " +
            "; ".join(f"{c} ({len(by[c])})" for c in sorted(broken, key=lambda c: -len(by[c]))[:6]),
            "Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; "
            "missing-target objects never deploy and APIC may silently fall back to tn-common defaults.", broken)
    sec = ["Permit-any filter", "vzAny contract", "VRF unenforced", "Preferred group enabled"]
    if any(by[c] for c in sec):
        rec("Contract design: no permit-any, keep vzAny/preferred groups deliberate",
            "; ".join(f"{c}: {len(by[c])} (e.g. {ex(c, 2)})" for c in sec if by[c]),
            "Use specific filters (protocol + destination port, stateful where possible) instead of "
            "common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; "
            "keep every VRF enforced; avoid preferred groups except for migrations.", sec)
    pc = ["Contract provided, never consumed", "Contract consumed, never provided", "Contract unused",
          "EPG isolated (no contracts)", "External EPG without contracts", "Duplicate contract"]
    if any(by[c] for c in pc):
        rec("Every contract needs both a provider and a consumer; remove dead/duplicate contracts",
            "; ".join(f"{c}: {len(by[c])} (e.g. {ex(c, 2)})" for c in pc if by[c]),
            "Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and "
            "duplicate contracts (e.g. *-OLD) so the policy matches the intent.", pc)
    if by["Contract scope mismatch"] or by["Contract scope wider than used"]:
        rec("Match contract scope to real usage", f"scope mismatch: {len(by['Contract scope mismatch'])}, wider than "
            f"needed: {len(by['Contract scope wider than used'])}",
            "Use 'context' by default, 'tenant'/'global' only for inter-VRF/tenant flows (with shared subnets).",
            ["Contract scope mismatch", "Contract scope wider than used"])
    bd = ["L3 BD without subnet", "Subnet on L2 BD", "L2 BD settings", "L3 BD flooding"]
    if any(by[c] for c in bd):
        rec("Make BD settings match their role (L2 vs L3)", "; ".join(f"{c}: {len(by[c])} (e.g. {ex(c, 2)})"
                                                                      for c in bd if by[c]),
            "L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to "
            "subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.", bd)
    hy = ["Tenant empty", "VRF unused", "BD unused", "AP without EPGs", "Filter unused",
          "L3Out without external EPG"]
    if any(by[c] for c in hy):
        rec("Clean up unused objects", "; ".join(f"{c}: {len(by[c])}" for c in hy if by[c]),
            "Delete leftovers or bring them under NaC; unused objects hide real intent and drift.", hy)
    # descriptions / annotations / naming over user objects
    user = [(d, a) for coll in (A.vrfs, A.bds, A.aps, A.epgs, A.brc, A.flt, A.l3o) for d, a in coll.items()
            if d not in SYSTEM and tenant_of(d) not in RELATIONS_ONLY]
    nodesc = [d for d, a in user if not a.get("descr")]
    noann = [d for d, a in user if not a.get("annotation")]
    anns = collections.Counter(a.get("annotation") for d, a in user if a.get("annotation"))
    rec("Add descriptions", f"{len(nodesc)} of {len(user)} VRF/BD/AP/EPG/contract/filter/L3Out objects have no "
        "description.", "Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.")
    rec("Tag ownership (annotations) for NaC", f"{len(noann)} of {len(user)} objects have no annotation; in use: " +
        (", ".join(f"'{k}' x{v}" for k, v in anns.most_common()) or "none") + ".",
        "Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as "
        "nac:owner=<team>); objects without it are hand-made and drift-prone.")
    bad = sorted({short(d) for d, a in user if NAME_BAD.match(a.get("name", ""))})
    styles = collections.Counter()
    for d, a in user:
        n = a.get("name", "")
        styles["UPPER_SNAKE" if re.fullmatch(r"[A-Z0-9_\-]+", n) else "lower" if re.fullmatch(r"[a-z0-9_\-.]+", n)
               else "Mixed"] += 1
    rec("Adopt one naming convention", f"name styles in use: " + ", ".join(f"{k} {v}" for k, v in styles.items()) +
        f"; {len(bad)} generic/VLAN/IP-style names (e.g. {', '.join(bad[:5])}).",
        "e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; "
        "enforce it in the NaC schema/linting.")
    if by["EPG without domain"] or by["EPG domain missing-target"]:
        rec("Bind EPGs to a domain", f"no domain: {len(by['EPG without domain'])}, missing domain: "
            f"{len(by['EPG domain missing-target'])}", "Every EPG that should carry endpoints needs a physical/VMM "
            "domain whose VLAN pool covers the encap.", ["EPG without domain", "EPG domain missing-target"])
    return R


# ------------------------------------------------------------------ robot results
def parse_robot(xml: pathlib.Path):
    if not xml or not xml.exists():
        return {"available": False}
    from robot.api import ExecutionResult, ResultVisitor
    res = ExecutionResult(str(xml))
    fails = []

    class V(ResultVisitor):
        def visit_test(self, t):
            if t.status == "FAIL":
                msg = (t.message or "").strip()
                fails.append({"suite": t.parent.name, "test": t.name, "reason": msg[:400],
                              "kind": "run-error" if "setup failed" in msg.lower() or "aaaLogin" in msg else "integrity"})

    res.visit(V())
    st = res.statistics.total
    return {"available": True, "total": st.passed + st.failed + st.skipped, "passed": st.passed,
            "failed": st.failed, "skipped": st.skipped, "failures": fails,
            "run_errors": sum(f["kind"] == "run-error" for f in fails)}


# ------------------------------------------------------------------ render
SEVC = {"fail": "#c0392b", "warn": "#b9770e", "info": "#5d6d7e"}


def render_md(S):
    L = [f"# ACI tenant logical-integrity report: {S['date']}", "", f"## {S['headline']}", "",
         f"- APIC: {S['apic_url']} (snapshot {S['pulled_at_local']})",
         f"- Generated: {S['generated_at_local']}",
         f"- Scope: {len(S['scorecard'])} tenants on the APIC ({S['baseline_count']} in baseline, new: "
         f"{', '.join(S['new_tenants']) or 'none'}); infra checked for broken relations + critical/major faults only",
         f"- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, "
         "L3Out/external EPG, domains, service graphs, faults", ""]
    r = S["robot"]
    if r.get("available"):
        L += [f"- nac-test integrity suite (templates/tests/integrity): {r['total']} tests, {r['passed']} passed, "
              f"{r['failed']} failed" + (f" ({r['run_errors']} of them run errors, e.g. APIC login throttling)"
                                         if r.get("run_errors") else ""), ""]
    L += ["## Per-tenant scorecard", "", "| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | "
          "Broken | Warn | Crit/Major faults | Score | Status |", "|---|---|" + "---:|" * 11 + "---|"]
    for t in S["scorecard"]:
        L.append(f"| {t['tenant']} | {'yes' if t['in_baseline'] else 'NEW'} | {t['vrf']} | {t['bd']} | {t['subnet']} | "
                 f"{t['ap']} | {t['epg']} | {t['contract']} | {t['l3out']} | {t['broken']} | {t['warnings']} | "
                 f"{t['faults_crit_major']} | {t['score']} | {t['status']} |")
    for sev, title in (("fail", "Broken relations"), ("warn", "Warnings")):
        rows = [f for f in S["findings"] if f["severity"] == sev]
        L += ["", f"## {title} ({len(rows)})", ""]
        if rows:
            L += ["| Tenant | Check | Object DN | Why | Fix |", "|---|---|---|---|---|"]
            L += [f"| {f['tenant']} | {f['check']} | `{f['dn']}` | {_md(f['reason'])} | {_md(f['fix'])} |" for f in rows]
        else:
            L.append("None.")
    L += ["", "## Recommendations to look good", ""]
    for i, x in enumerate(S["recommendations"], 1):
        L += [f"{i}. **{x['title']}** - found: {x['found']}  ", f"   Do: {x['action']}"]
    info = [f for f in S["findings"] if f["severity"] == "info"]
    L += ["", f"## Informational ({len(info)})", ""]
    if info:
        L += ["| Tenant | Check | Object DN | Note |", "|---|---|---|---|"]
        L += [f"| {f['tenant']} | {f['check']} | `{f['dn']}` | {_md(f['reason'])} |" for f in info]
    if r.get("available") and r["failures"]:
        L += ["", "## nac-test integrity failures", "", "| Suite | Test | Reason |", "|---|---|---|"]
        L += [f"| {x['suite']} | {x['test']} | {_md(x['reason'])} |" for x in r["failures"]]
    fs = S["faults"]
    L += ["", "## Tenant faults (faultInst)", "", f"By severity: " + ", ".join(f"{k} {v}" for k, v in fs["by_severity"].items())
          + f"; TCA/threshold faults (context only): {fs['tca']}", ""]
    if fs["critical_major"]:
        L += ["| Tenant | Sev | Code | Affected | Description |", "|---|---|---|---|---|"]
        L += [f"| {x['tenant']} | {x['severity']} | {x['code']} | `{x['affected']}` | {_md(x['descr'][:200])} |"
              for x in fs["critical_major"]]
    if S["errors"]:
        L += ["", "## Errors", ""] + [f"- {e}" for e in S["errors"]]
    L += ["", "Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).", ""]
    return "\n".join(L)


def _md(s):
    return str(s).replace("|", "/").replace("\n", " ")


def render_html(S, embed=False):
    e = html.escape
    td = "padding:4px 6px;border:1px solid #ccc;font-size:12px;vertical-align:top;"
    th = td + "background:#f0f0f0;text-align:left;"
    tbl = "border-collapse:collapse;margin:6px 0 14px 0;width:100%;"
    col = {"broken": "#c0392b", "warnings": "#b9770e", "healthy": "#1e8449", "error": "#7f8c8d"}[S["status"]]
    stc = {"BROKEN": "#c0392b", "WARN": "#b9770e", "HEALTHY": "#1e8449"}

    def table(head, rows, right=(), raw=()):
        h = "".join(f'<th style="{th}">{e(x)}</th>' for x in head)
        b = ""
        for r in rows:
            b += "<tr>" + "".join(f'<td style="{td}{"text-align:right;" if i in right else ""}">'
                                  f'{c if i in raw else e(str(c))}</td>' for i, c in enumerate(r)) + "</tr>"
        return f'<table style="{tbl}"><tr>{h}</tr>{b}</table>'

    badge = lambda txt, c: (f'<span style="background:{c};color:#fff;padding:1px 6px;border-radius:3px;'
                            f'font-size:11px;font-weight:bold;">{e(txt)}</span>')
    p = ['<div style="font-family:Arial,Helvetica,sans-serif;color:#222;max-width:1100px;">']
    if not embed:
        p.append(f'<h2 style="margin:0 0 6px 0;">ACI tenant logical-integrity report: {e(S["date"])}</h2>')
    p.append(f'<div style="background:{col};color:#fff;padding:10px 14px;font-size:17px;font-weight:bold;">'
             f'{e(S["headline"])}</div>')
    r = S["robot"]
    p.append(f'<p style="font-size:12px;">APIC: {e(S["apic_url"])} (snapshot {e(S["pulled_at_local"])})<br>'
             f'Scope: {len(S["scorecard"])} tenants ({S["baseline_count"]} in baseline; new: '
             f'{e(", ".join(S["new_tenants"]) or "none")}); infra = broken relations + critical/major faults only<br>'
             'Graph: tenant &rarr; VRF &rarr; BD &rarr; subnet &rarr; AP &rarr; EPG &rarr; contract &rarr; subject '
             '&rarr; filter &rarr; entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults'
             + (f'<br>nac-test integrity suite (templates/tests/integrity): {r["total"]} tests, {r["passed"]} passed, '
               f'{r["failed"]} failed' + (f' ({r["run_errors"]} run errors)' if r.get("run_errors") else "")
                if r.get("available") else "") + "</p>")
    p.append('<h3 style="margin-bottom:2px;">Per-tenant scorecard</h3>')
    p.append(table(["Tenant", "Baseline", "VRF", "BD", "Subnet", "AP", "EPG", "Contract", "L3Out", "Broken", "Warn",
                    "Crit/Maj faults", "Score", "Status"],
                   [[t["tenant"], "yes" if t["in_baseline"] else "NEW", t["vrf"], t["bd"], t["subnet"], t["ap"],
                     t["epg"], t["contract"], t["l3out"], t["broken"], t["warnings"], t["faults_crit_major"],
                     t["score"], badge(t["status"], stc[t["status"]])] for t in S["scorecard"]],
                   right=tuple(range(2, 13)), raw=(13,)))
    for sev, title in (("fail", "Broken relations"), ("warn", "Warnings")):
        rows = [f for f in S["findings"] if f["severity"] == sev]
        p.append(f'<h3 style="margin-bottom:2px;color:{SEVC[sev]};">{title} ({len(rows)})</h3>')
        p.append(table(["Tenant", "Check", "Object DN", "Why", "Fix"],
                       [[f["tenant"], f["check"], f'<code style="font-size:11px;">{e(f["dn"])}</code>', f["reason"],
                         f["fix"]] for f in rows], raw=(2,)) if rows else '<p style="font-size:12px;">None.</p>')
    p.append('<h3 style="margin-bottom:2px;">Recommendations to look good</h3><ol style="font-size:12px;">')
    for x in S["recommendations"]:
        p.append(f'<li style="margin-bottom:6px;"><b>{e(x["title"])}</b><br><span style="color:#555;">Found: '
                 f'{e(x["found"])}</span><br>Do: {e(x["action"])}</li>')
    p.append("</ol>")
    if r.get("available") and r["failures"]:
        p.append('<h3 style="margin-bottom:2px;">nac-test integrity failures</h3>')
        p.append(table(["Suite", "Test", "Reason"], [[x["suite"], x["test"], x["reason"]] for x in r["failures"]]))
    fs = S["faults"]
    p.append('<h3 style="margin-bottom:2px;">Tenant faults (faultInst)</h3>')
    p.append(f'<p style="font-size:12px;">By severity: {e(", ".join(f"{k} {v}" for k, v in fs["by_severity"].items()))};'
             f' TCA/threshold faults (context only): {fs["tca"]}</p>')
    if fs["critical_major"]:
        p.append(table(["Tenant", "Severity", "Code", "Affected", "Description"],
                       [[x["tenant"], x["severity"], x["code"], x["affected"], x["descr"][:200]]
                        for x in fs["critical_major"]]))
    info = [f for f in S["findings"] if f["severity"] == "info"]
    p.append(f'<h3 style="margin-bottom:2px;">Informational ({len(info)})</h3>')
    if info:
        p.append(table(["Tenant", "Check", "Object DN", "Note"], [[f["tenant"], f["check"], f["dn"], f["reason"]]
                                                                 for f in info]))
    if S["errors"]:
        p.append('<p style="font-size:12px;color:#c0392b;">Errors: ' + e("; ".join(S["errors"])) + "</p>")
    p.append('<p style="font-size:11px;color:#777;">Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - '
             '3 x warnings (min 0). Generated ' + e(S["generated_at_local"]) + ".</p></div>")
    body = "\n".join(p)
    if embed:
        return body
    return ('<!DOCTYPE html><html><head><meta charset="utf-8"><title>ACI integrity ' + e(S["date"]) +
            '</title></head><body style="margin:12px;">' + body + "</body></html>\n")


# ------------------------------------------------------------------ main
def report(out: pathlib.Path, date, baseline: pathlib.Path, robot_xml, robot_rc, errors):
    snap = json.loads((out / "live-objects.json").read_text())
    base = {f.name[len("tenant_"):-len(".nac.yaml")] for f in baseline.glob("tenant_*.nac.yaml")} if baseline else set()
    A = Analyser(snap, base)
    F = A.run()
    order = {"fail": 0, "warn": 1, "info": 2}
    F.sort(key=lambda f: (order[f["severity"]], f["tenant"] or "", f["check"], f["dn"]))
    sc = scorecard(A, F)
    rec = recommendations(A, F, sc)
    rb = parse_robot(pathlib.Path(robot_xml)) if robot_xml else {"available": False}
    nf = sum(f["severity"] == "fail" for f in F)
    nw = sum(f["severity"] == "warn" for f in F)
    bt = sorted({f["tenant"] for f in F if f["severity"] == "fail"})
    status = "broken" if nf else ("warnings" if nw else "healthy")
    headline = (f"BROKEN RELATIONS FOUND - {nf} broken, {nw} warnings ({len(bt)} of {len(sc)} tenants broken: "
                f"{', '.join(bt)})" if nf else f"HEALTHY - 0 broken relations, {nw} warnings across {len(sc)} tenants")
    if errors:
        status = "error" if not F else status
    sevc = collections.Counter(r["severity"] for r in A.fault_rows)
    gen = now_mel()
    pulled = dt.datetime.fromisoformat(snap["pulled_at"]).astimezone(TZ)
    S = {"schema": 1, "date": date, "status": status, "broken": nf, "warnings": nw,
         "info": sum(f["severity"] == "info" for f in F), "headline": headline,
         "generated_at": gen.isoformat(timespec="seconds"), "generated_at_local": gen.strftime("%Y-%m-%d %H:%M:%S %Z"),
         "pulled_at_local": pulled.strftime("%Y-%m-%d %H:%M:%S %Z"), "apic_url": snap.get("apic_url", ""),
         "baseline_count": len(base & set(A.tenants)), "new_tenants": sorted(set(A.tenants) - base, key=str.lower),
         "missing_baseline_tenants": sorted(base - set(A.tenants)),
         "scorecard": sc, "findings": F, "recommendations": rec, "robot": rb, "robot_rc": robot_rc,
         "faults": {"by_severity": dict(sevc), "tca": sum(r["tca"] for r in A.fault_rows),
                    "critical_major": [r for r in A.fault_rows if r["severity"] in ("critical", "major")]},
         "errors": errors}
    (out / "integrity-summary.json").write_text(json.dumps(S, indent=2))
    (out / "integrity-summary.md").write_text(render_md(S))
    (out / "integrity-summary.html").write_text(render_html(S))
    print(headline)
    return S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", nargs="?", default="all", choices=["collect", "report", "all"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--date", default=now_mel().strftime("%F"))
    ap.add_argument("--baseline", default="baseline/data")
    ap.add_argument("--robot-xml")
    ap.add_argument("--robot-rc", type=int)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    errors = []
    if a.mode in ("collect", "all"):
        try:
            for k in ("ACI_URL", "ACI_USERNAME", "ACI_PASSWORD"):
                if not os.environ.get(k):
                    raise RuntimeError(f"missing env var {k}")
            collect(out)
        except Exception as ex:
            errors.append(f"APIC pull failed: {type(ex).__name__}: {str(ex)[:200]}")
            (out / "collect-error.txt").write_text(errors[-1] + "\n")
    if a.mode in ("report", "all"):
        ce = out / "collect-error.txt"
        if ce.exists():
            errors.append(ce.read_text().strip())
            errors = list(dict.fromkeys(errors))
        if not (out / "live-objects.json").exists():
            S = {"schema": 1, "date": a.date, "status": "error", "broken": None, "warnings": None,
                 "headline": "INTEGRITY CHECK FAILED - no APIC snapshot", "errors": errors or ["no snapshot"]}
            (out / "integrity-summary.json").write_text(json.dumps(S, indent=2))
            (out / "integrity-summary.md").write_text(f"# ACI integrity {a.date}\n\n## {S['headline']}\n\n" +
                                                       "\n".join(f"- {x}" for x in S["errors"]) + "\n")
            (out / "integrity-summary.html").write_text(f"<html><body style=\"font-family:Arial\"><h2>{S['headline']}"
                                                        f"</h2><p>{html.escape('; '.join(S['errors']))}</p></body></html>")
            print(S["headline"])
            return
        report(out, a.date, pathlib.Path(a.baseline), a.robot_xml, a.robot_rc, errors)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
    sys.exit(0)
