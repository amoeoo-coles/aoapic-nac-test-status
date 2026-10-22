#!/usr/bin/env python3
"""Drift comparison for the daily ACI drift report. READ-ONLY against the APIC (aaaLogin POST + class GETs).

Compares a fresh REST pull (fvTenant, fvCtx, fvBD, fvSubnet, fvAp, fvAEPg) with the frozen NaC baseline YAML,
collects APIC fault counts (faultInst by severity), parses the nac-test output.xml, and writes
drift-summary.md / drift-summary.html / drift-summary.json into the results folder.

Credentials come from the environment (ACI_URL / ACI_USERNAME / ACI_PASSWORD, loaded from .env by drift_report.sh).
They and the APIC session cookie are never written anywhere.
"""
import argparse, datetime as dt, html, json, os, pathlib, re, sys, traceback
from zoneinfo import ZoneInfo

import requests, urllib3, yaml

urllib3.disable_warnings()
TZ = ZoneInfo("Australia/Melbourne")
TYPES = [  # (key, label, APIC class)
    ("tenant", "Tenant", "fvTenant"),
    ("vrf", "VRF", "fvCtx"),
    ("bd", "BD", "fvBD"),
    ("subnet", "Subnet (BD)", "fvSubnet"),
    ("ap", "AP", "fvAp"),
    ("epg", "EPG", "fvAEPg"),
]
SEVERITIES = ["critical", "major", "minor", "warning", "info", "cleared"]
TN_RE = re.compile(r"^uni/tn-([^/]+)")


def now_mel():
    return dt.datetime.now(TZ)


# ---------------------------------------------------------------- baseline
def baseline_dns(base_dir: pathlib.Path):
    """Build the expected DN set per object type from the NaC YAML (same model build_data.py writes)."""
    out = {k: set() for k, _, _ in TYPES}
    for f in sorted(base_dir.glob("*.y*ml")):
        doc = yaml.safe_load(f.read_text()) or {}
        for t in (doc.get("apic") or {}).get("tenants") or []:
            tdn = f"uni/tn-{t['name']}"
            out["tenant"].add(tdn)
            for v in t.get("vrfs") or []:
                out["vrf"].add(f"{tdn}/ctx-{v['name']}")
            for b in t.get("bridge_domains") or []:
                bdn = f"{tdn}/BD-{b['name']}"
                out["bd"].add(bdn)
                for s in b.get("subnets") or []:
                    out["subnet"].add(f"{bdn}/subnet-[{s['ip']}]")
            for a in t.get("application_profiles") or []:
                adn = f"{tdn}/ap-{a['name']}"
                out["ap"].add(adn)
                for e in a.get("endpoint_groups") or []:
                    out["epg"].add(f"{adn}/epg-{e['name']}")
    return out


# ---------------------------------------------------------------- live APIC
def apic_session():
    url = os.environ["ACI_URL"].rstrip("/")
    s = requests.Session()
    s.verify = False
    r = s.post(f"{url}/api/aaaLogin.json",
               json={"aaaUser": {"attributes": {"name": os.environ["ACI_USERNAME"],
                                                "pwd": os.environ["ACI_PASSWORD"]}}}, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"aaaLogin failed: HTTP {r.status_code}")  # never echo body/creds
    return s, url


def live_dns(s, url):
    out = {}
    for key, _, cls in TYPES:
        r = s.get(f"{url}/api/class/{cls}.json", timeout=90)
        r.raise_for_status()
        dns = {x[cls]["attributes"]["dn"] for x in r.json()["imdata"]}
        if key == "subnet":  # baseline models BD subnets only; EPG-level subnets are out of scope
            dns = {d for d in dns if re.match(r"^uni/tn-[^/]+/BD-[^/]+/subnet-\[", d)}
        out[key] = dns
    return out


def fault_counts(s, url):
    counts = {}
    for sev in SEVERITIES:
        r = s.get(f"{url}/api/class/faultInst.json",
                  params={"query-target-filter": f'eq(faultInst.severity,"{sev}")', "rsp-subtree-include": "count"},
                  timeout=90)
        r.raise_for_status()
        counts[sev] = int(r.json()["imdata"][0]["moCount"]["attributes"]["count"])
    counts["total"] = sum(counts.values())
    return counts


# ---------------------------------------------------------------- nac-test results
def parse_tests(output_xml: pathlib.Path):
    if not output_xml.exists():
        return {"available": False, "total": 0, "passed": 0, "failed": 0, "skipped": 0, "failures": []}
    from robot.api import ExecutionResult, ResultVisitor

    res = ExecutionResult(str(output_xml))
    fails = []

    class V(ResultVisitor):
        def visit_test(self, t):
            if t.status == "FAIL":
                msg = (t.message or "").strip()
                kind = "missing" if "not found on APIC" in msg or "404" in msg else "changed"
                fails.append({"suite": t.parent.name, "test": t.name, "kind": kind, "reason": msg[:500]})

    res.visit(V())
    st = res.statistics.total
    return {"available": True, "total": st.passed + st.failed + st.skipped, "passed": st.passed,
            "failed": st.failed, "skipped": st.skipped, "failures": fails}


# ---------------------------------------------------------------- rendering
def tenant_of(dn):
    m = TN_RE.match(dn)
    return m.group(1) if m else "?"


def render_md(S):
    L = [f"# ACI drift report: {S['date']}", "",
         f"## {S['headline']}", "",
         f"- APIC: {S['apic_url']}",
         f"- Generated: {S['generated_at_local']} (Australia/Melbourne)",
         f"- Baseline: `baseline/data/` ({S['baseline']['info']})",
         f"- Status: `{S['status']}`" + (f"; errors: {'; '.join(S['errors'])}" if S["errors"] else ""), ""]
    if S.get("note"):
        L += [f"> {S['note']}", ""]
    t = S["tests"]
    L += ["## nac-test", "",
          f"- Tests: **{t['total']}** total, **{t['passed']}** passed, **{t['failed']}** failed, {t['skipped']} skipped"
          f" (nac-test exit code {S['nac_test_rc']})", ""]
    if t["failures"]:
        L += ["| Suite | Test | Kind | Reason |", "|---|---|---|---|"]
        for f in t["failures"]:
            L.append(f"| {f['suite']} | {f['test']} | {f['kind']} | {f['reason'].replace('|', '/').replace(chr(10), ' ')} |")
        L.append("")
    else:
        L += ["No failed tests.", ""]
    L += ["## Object counts (REST pull vs baseline)", "",
          "| Type | Baseline | Current (APIC, all tenants) | Added | Removed |", "|---|---:|---:|---:|---:|"]
    for c in S["counts"]:
        L.append(f"| {c['type']} | {c['baseline']} | {c['current']} | {c['added']} | {c['removed']} |")
    L += ["", "Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).", ""]
    for title, key in (("Added since baseline", "added"), ("Removed since baseline", "removed")):
        objs = S[key]
        L += [f"## {title} ({len(objs)})", ""]
        if objs:
            L += ["| Type | Tenant | DN |", "|---|---|---|"]
            L += [f"| {o['type']} | {o['tenant']} | `{o['dn']}` |" for o in objs]
        else:
            L.append("None.")
        L.append("")
    fc = S["faults"]
    L += ["## APIC faults (faultInst, context only)", ""]
    if fc:
        L += ["| " + " | ".join(k for k in SEVERITIES + ["total"]) + " |",
              "|" + "---:|" * (len(SEVERITIES) + 1),
              "| " + " | ".join(str(fc[k]) for k in SEVERITIES + ["total"]) + " |", ""]
    else:
        L += ["Not available.", ""]
    L += ["## Artifacts", "", "`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, "
          "`live-snapshot.json`", ""]
    return "\n".join(L)


def render_html(S):
    e = html.escape
    td = "padding:4px 8px;border:1px solid #ccc;font-size:13px;"
    th = td + "background:#f0f0f0;text-align:left;"
    tbl = "border-collapse:collapse;margin:6px 0 14px 0;"
    colour = {"drift": "#c0392b", "no_drift": "#1e8449", "error": "#b9770e"}[S["status"]]

    def table(head, rows, right=()):
        h = "".join(f'<th style="{th}">{e(x)}</th>' for x in head)
        b = "".join("<tr>" + "".join(
            f'<td style="{td}{"text-align:right;" if i in right else ""}">{e(str(c))}</td>' for i, c in enumerate(r))
                    + "</tr>" for r in rows)
        return f'<table style="{tbl}"><tr>{h}</tr>{b}</table>'

    t = S["tests"]
    p = [f'<div style="font-family:Arial,Helvetica,sans-serif;color:#222;max-width:900px;">',
         f'<h2 style="margin:0 0 6px 0;">ACI drift report: {e(S["date"])}</h2>',
         f'<div style="background:{colour};color:#fff;padding:10px 14px;font-size:18px;font-weight:bold;">{e(S["headline"])}</div>',
         f'<p style="font-size:13px;">APIC: {e(S["apic_url"])}<br>Generated: {e(S["generated_at_local"])} (Australia/Melbourne)<br>'
         f'Baseline: baseline/data/ ({e(S["baseline"]["info"])})<br>Status: {e(S["status"])}'
         + (f'<br>Errors: {e("; ".join(S["errors"]))}' if S["errors"] else "") + "</p>"]
    if S.get("note"):
        p.append(f'<p style="font-size:13px;background:#fdf6e3;padding:6px 10px;">{e(S["note"])}</p>')
    p.append('<h3 style="margin-bottom:2px;">nac-test</h3>')
    p.append(table(["Total", "Passed", "Failed", "Skipped"], [[t["total"], t["passed"], t["failed"], t["skipped"]]],
                   right=(0, 1, 2, 3)))
    if t["failures"]:
        p.append(table(["Suite", "Test", "Kind", "Reason"],
                       [[f["suite"], f["test"], f["kind"], f["reason"]] for f in t["failures"]]))
    else:
        p.append('<p style="font-size:13px;">No failed tests.</p>')
    p.append('<h3 style="margin-bottom:2px;">Object counts (REST pull vs baseline)</h3>')
    p.append(table(["Type", "Baseline", "Current (APIC, all tenants)", "Added", "Removed"],
                   [[c["type"], c["baseline"], c["current"], c["added"], c["removed"]] for c in S["counts"]],
                   right=(1, 2, 3, 4)))
    for title, key in (("Added since baseline", "added"), ("Removed since baseline", "removed")):
        objs = S[key]
        p.append(f'<h3 style="margin-bottom:2px;">{e(title)} ({len(objs)})</h3>')
        p.append(table(["Type", "Tenant", "DN"], [[o["type"], o["tenant"], o["dn"]] for o in objs])
                 if objs else '<p style="font-size:13px;">None.</p>')
    p.append('<h3 style="margin-bottom:2px;">APIC faults (faultInst, context only)</h3>')
    fc = S["faults"]
    p.append(table(SEVERITIES + ["total"], [[fc[k] for k in SEVERITIES + ["total"]]], right=tuple(range(7)))
             if fc else '<p style="font-size:13px;">Not available.</p>')
    p.append('<p style="font-size:11px;color:#777;">Read-only check: aaaLogin + GET only. Subnets are BD subnets only. '
             'Full Robot reports: report.html / log.html in the attached zip.</p></div>')
    return "<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>ACI drift report " + e(S["date"]) + \
           "</title></head><body style=\"margin:12px;\">" + "\n".join(p) + "</body></html>\n"


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--nac-rc", type=int, default=0)
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    res = pathlib.Path(a.results)
    base_root = pathlib.Path(a.baseline)
    errors = []

    info_line = ""
    bi = base_root / "BASELINE_INFO.md"
    if bi.exists():
        m = re.search(r"^- Frozen: (.+)$", bi.read_text(), re.M)
        info_line = f"frozen {m.group(1)}" if m else "see BASELINE_INFO.md"

    base = baseline_dns(base_root / "data")
    live, faults = None, None
    try:
        s, url = apic_session()
        live = live_dns(s, url)
        try:
            faults = fault_counts(s, url)
        except Exception as ex:
            errors.append(f"fault count query failed: {type(ex).__name__}")
        try:
            s.post(f"{url}/api/aaaLogout.json", json={"aaaUser": {"attributes": {"name": os.environ["ACI_USERNAME"]}}},
                   timeout=15)
        except Exception:
            pass
    except Exception as ex:
        errors.append(f"REST pull failed: {type(ex).__name__}: {str(ex)[:200]}")

    try:
        tests = parse_tests(res / "output.xml")
        if not tests["available"]:
            errors.append("nac-test output.xml missing")
    except Exception as ex:
        tests = {"available": False, "total": 0, "passed": 0, "failed": 0, "skipped": 0, "failures": []}
        errors.append(f"output.xml parse failed: {type(ex).__name__}")

    added, removed, counts = [], [], []
    for key, label, cls in TYPES:
        cur = live[key] if live else set()
        ad = sorted(cur - base[key]) if live else []
        rm = sorted(base[key] - cur) if live else []
        added += [{"type": label, "class": cls, "tenant": tenant_of(d), "dn": d} for d in ad]
        removed += [{"type": label, "class": cls, "tenant": tenant_of(d), "dn": d} for d in rm]
        counts.append({"type": label, "class": cls, "baseline": len(base[key]),
                       "current": len(cur) if live else None, "added": len(ad) if live else None,
                       "removed": len(rm) if live else None})

    drift = bool(added or removed or tests["failed"])
    if live is None or not tests["available"]:
        status = "error"
        headline = "DRIFT CHECK INCOMPLETE" + (" - DRIFT DETECTED" if drift else "")
    else:
        status = "drift" if drift else "no_drift"
        headline = "DRIFT DETECTED" if drift else "NO DRIFT"
    if live is not None or tests["available"]:
        headline += (f" - tests {tests['passed']}/{tests['total']} passed, {tests['failed']} failed; "
                     f"{len(added)} added, {len(removed)} removed")

    note = None
    known = {"Production_Tenant", "Production_Tenant2", "Production_Tenant22", "tn_TEST1"}
    new_tn = {o["tenant"] for o in added if o["type"] == "Tenant"}
    if new_tn & known:
        note = ("Tenants " + ", ".join(sorted(new_tn & known)) + " already existed on the shared sandbox when the "
                "baseline data was pulled (22 Oct 2026 ~10:15 AEDT) but were deliberately left out of scope; they "
                "are reported as added since baseline.")

    gen = now_mel()
    S = {"schema": 1, "date": a.date, "status": status, "drift": drift, "headline": headline,
         "generated_at": gen.isoformat(timespec="seconds"),
         "generated_at_local": gen.strftime("%Y-%m-%d %H:%M:%S %Z"),
         "apic_url": os.environ.get("ACI_URL", ""), "nac_test_rc": a.nac_rc,
         "baseline": {"path": "baseline/data", "info": info_line or "n/a"},
         "tests": tests, "counts": counts, "added": added, "removed": removed, "faults": faults,
         "errors": errors, "note": note}
    if live:
        (res / "live-snapshot.json").write_text(json.dumps({k: sorted(v) for k, v in live.items()}, indent=1))
    (res / "drift-summary.json").write_text(json.dumps(S, indent=2))
    (res / "drift-summary.md").write_text(render_md(S))
    (res / "drift-summary.html").write_text(render_html(S))
    print(headline)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(0)  # caller decides; drift_report.sh always exits 0
