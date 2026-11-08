#!/usr/bin/env python3
"""Record the real versions involved in a run -> data/<stamp>/versions.json (and data/latest/ via publish_run --reindex).

  versions.py --stamp 2026-11-09-0817 [--venv /workspace/aci-nac/.venv] [--nac-src /workspace/nac-test] [--note TEXT]
APIC: READ-ONLY (aaaLogin, GET firmwareCtrlrRunning + topSystem, aaaLogout) through the Report 17 collector's Apic client;
credentials come from its environment and are never printed or written. Python packages are read from the test venv with
importlib.metadata. Anything that cannot be read is recorded as an error, never guessed. Always exits 0.
"""
import argparse, datetime as dt, json, os, pathlib, re, subprocess, sys
SITE = pathlib.Path(__file__).resolve().parent.parent
PKGS = ["nac-test", "nac-test-pyats-common", "nac-yaml", "robotframework", "robotframework-pabot", "robotframework-requests", "requests", "PyYAML"]


def apic():
    sys.path.insert(0, "/workspace/grafana-docker/scripts")
    from publish_aoapic_monitor import Apic
    a = Apic(); lg = a.login()
    if not lg.get("login_ok"): raise RuntimeError("APIC login failed (HTTP %s)" % lg.get("http_status"))
    out = {"controllers": [], "switches": []}
    try:
        ctl, st1, _ = a.get("/api/node/class/firmwareCtrlrRunning.json", "versions firmwareCtrlrRunning")
        sysd, st2, _ = a.get("/api/node/class/topSystem.json", "versions topSystem")
        if ctl is None or sysd is None: raise RuntimeError("version query failed (HTTP %s/%s)" % (st1, st2))
        names = {}
        for x in sysd:
            at = next(iter(x.values()))["attributes"]
            names[at.get("id")] = at
            if at.get("role") in ("leaf", "spine"):
                out["switches"].append({"name": at.get("name"), "node": at.get("id"), "role": at.get("role"), "version": at.get("version"), "source": "topSystem"})
        for x in ctl:
            at = next(iter(x.values()))["attributes"]
            nid = (re.search(r"/node-(\d+)/", at.get("dn", "")) or [None, None])[1]
            out["controllers"].append({"name": (names.get(nid) or {}).get("name"), "node": nid, "version": at.get("version"), "source": "firmwareCtrlrRunning"})
    finally:
        try: a.s.post(a.url + "/api/aaaLogout.json", json={"aaaUser": {"attributes": {"name": os.environ.get("ACI_USERNAME", "")}}}, timeout=30)
        except Exception: pass
    out["switches"].sort(key=lambda s: int(s["node"] or 0))
    return out


def venv(py):
    code = ("import importlib.metadata as m,json,sys;r={'python':sys.version.split()[0]}\n"
            "for p in %r:\n try: r[p]=m.version(p)\n except Exception: r[p]=None\nprint(json.dumps(r))" % PKGS)
    return json.loads(subprocess.run([py, "-c", code], capture_output=True, text=True, check=True).stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stamp", required=True)
    ap.add_argument("--venv", default=os.environ.get("NAC_VENV", "/workspace/aci-nac/.venv"))
    ap.add_argument("--nac-src", default=os.environ.get("NAC_SRC", "/workspace/nac-test"))
    ap.add_argument("--validate-venv", default="/workspace/nbtenants/.venv")
    ap.add_argument("--note", default="")
    a = ap.parse_args()
    v = {"schema": 1, "stamp": a.stamp, "read_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
         "read_at_local": dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z"), "note": a.note, "errors": []}
    try: v["apic"] = apic()
    except Exception as e: v["errors"].append("APIC versions not read: " + type(e).__name__ + (": " + str(e) if isinstance(e, RuntimeError) else ""))
    try:
        t = venv(str(pathlib.Path(a.venv) / "bin" / "python"))
        v["python"] = t.pop("python"); v["tools"] = {k: x for k, x in t.items() if x}
        v["tools_source"] = "test venv (" + a.venv + ")"
    except Exception as e: v["errors"].append("test venv not read: " + type(e).__name__)
    try:
        r = subprocess.run([str(pathlib.Path(a.validate_venv) / "bin" / "python"), "-c", "import importlib.metadata as m;print(m.version('nac-validate'))"], capture_output=True, text=True)
        if r.returncode == 0: v["nac_validate"] = {"version": r.stdout.strip(), "used_by_this_run": False,
                                                    "note": "installed for the NetBox YAML Model page validation; the nac-test run does not call nac-validate"}
    except Exception: pass
    try:
        import yaml
        d = yaml.safe_load(open(pathlib.Path(a.nac_src) / "defaults" / "defaults.yaml"))
        dv = ((d or {}).get("defaults") or {}).get("apic", {}).get("version")
        if dv: v["data_model"] = {"defaults_apic_version": str(dv), "source": "nac-test defaults/defaults.yaml (defaults.apic.version)",
                                  "data_files": len(list((pathlib.Path(a.nac_src) / "data").glob("*.nac.yaml")))}
    except Exception as e: v["errors"].append("data model defaults not read: " + type(e).__name__)
    d = SITE / "data" / a.stamp
    if d.is_dir():
        (d / "versions.json").write_text(json.dumps(v, indent=1) + "\n")
        print("versions.json written for", a.stamp, "errors:", len(v["errors"]))
    else: print("no run folder", a.stamp)


if __name__ == "__main__":
    main()
