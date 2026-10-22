#!/usr/bin/env python3
"""Read-only: aaaLogin + class GETs on APIC, build NaC YAML for selected tenants."""
import os, json, re, sys, pathlib, requests, urllib3, yaml
ROOT=pathlib.Path(__file__).resolve().parent.parent
urllib3.disable_warnings()
for k in ("ACI_URL","ACI_USERNAME","ACI_PASSWORD"):
    if not os.environ.get(k): sys.exit(f"missing env var {k} (see .env.example)")
URL=os.environ["ACI_URL"].rstrip("/")
TENANTS=[l.split(",")[0] for l in open(ROOT/"scripts"/"tenants.csv").read().splitlines()[1:] if l.strip()]
s=requests.Session(); s.verify=False
r=s.post(f"{URL}/api/aaaLogin.json",json={"aaaUser":{"attributes":{"name":os.environ["ACI_USERNAME"],"pwd":os.environ["ACI_PASSWORD"]}}},timeout=30); r.raise_for_status()
(ROOT/"raw").mkdir(exist_ok=True); (ROOT/"data").mkdir(exist_ok=True)
raw={}
for c in ["fvTenant","fvCtx","fvBD","fvSubnet","fvAp","fvAEPg","fvRsBd","fvRsCtx"]:
    d=s.get(f"{URL}/api/class/{c}.json",timeout=60).json(); raw[c]=[x[c]["attributes"] for x in d["imdata"]]
    json.dump(d,open(ROOT/"raw"/f"{c}.json","w"),indent=1)
def tn(dn): return re.match(r"uni/tn-([^/]+)",dn).group(1)
rsctx={a["dn"].rsplit("/rsctx",1)[0]:a.get("tnFvCtxName","") for a in raw["fvRsCtx"]}
rsbd={a["dn"].rsplit("/rsbd",1)[0]:a.get("tnFvBDName","") for a in raw["fvRsBd"]}
out=[]
live={a["name"] for a in raw["fvTenant"]}
for t in TENANTS:
    if t not in live: print("WARN tenant missing on APIC:",t,file=sys.stderr); continue
    ta=next(a for a in raw["fvTenant"] if a["name"]==t)
    T={"name":t}
    if ta["descr"]: T["description"]=ta["descr"]
    vrfs=[{"name":a["name"],"enforcement_direction":a["pcEnfDir"],"enforcement_preference":a["pcEnfPref"]} for a in raw["fvCtx"] if tn(a["dn"])==t]
    if vrfs: T["vrfs"]=vrfs
    bds=[]
    for a in raw["fvBD"]:
        if tn(a["dn"])!=t: continue
        b={"name":a["name"],"unicast_routing":a["unicastRoute"]=="yes","arp_flooding":a["arpFlood"]=="yes"}
        if rsctx.get(a["dn"]): b["vrf"]=rsctx[a["dn"]]
        subs=[{"ip":x["ip"],"scope":x["scope"]} for x in raw["fvSubnet"] if x["dn"].startswith(a["dn"]+"/subnet-")]
        if subs: b["subnets"]=subs
        bds.append(b)
    if bds: T["bridge_domains"]=bds
    aps=[]
    for ap in raw["fvAp"]:
        if tn(ap["dn"])!=t: continue
        epgs=[]
        for e in raw["fvAEPg"]:
            if e["dn"].startswith(ap["dn"]+"/epg-"):
                g={"name":e["name"]}
                if rsbd.get(e["dn"]): g["bridge_domain"]=rsbd[e["dn"]]
                epgs.append(g)
        A={"name":ap["name"]}
        if epgs: A["endpoint_groups"]=epgs
        aps.append(A)
    if aps: T["application_profiles"]=aps
    out.append(T)
    yaml.safe_dump({"apic":{"tenants":[T]}},open(ROOT/"data"/f"tenant_{t}.nac.yaml","w"),sort_keys=False)
print("tenants written:",len(out),"| live tenants on APIC:",len(live),sorted(live-set(TENANTS)))
