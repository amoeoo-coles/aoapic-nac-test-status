#!/usr/bin/env python3
"""Render index.html from data/latest (or --run STAMP) + its changes.json + data/runs.json.

  build_site.py                 # newest run
  build_site.py --run 2026-10-23-0800
The page is scripts/site_template.html with a single JSON blob injected at /*__DATA__*/null; all rendering is
client-side, self-contained, no external assets. Reads only the published summary JSON in data/.
"""
import argparse, datetime as dt, json, pathlib, re

SITE = pathlib.Path(__file__).resolve().parent.parent
DATA = SITE / "data"
STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}$")


def load(p, default=None):
    try:
        return json.load(open(p))
    except Exception:
        return {} if default is None else default


def build(stamp):
    d = DATA / stamp
    daily, drift, integ = (load(d / f) for f in ("daily-summary.json", "drift-summary.json", "integrity-summary.json"))
    sc = integ.get("scorecard", [])
    r = integ.get("robot") or {}
    D = {
        "stamp": stamp,
        "generated_page": dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z"),
        "apic": integ.get("apic_url") or drift.get("apic_url"),
        "snapshot": integ.get("pulled_at_local"),
        "integrity_generated": integ.get("generated_at_local"),
        "drift_generated": drift.get("generated_at_local"),
        "daily_generated": daily.get("generated_at_local"),
        "status": daily.get("status"), "headline": daily.get("headline"),
        "integrity_headline": integ.get("headline"), "drift_headline": drift.get("headline"),
        "robot": {k: r.get(k, 0) for k in ("total", "passed", "failed")},
        "drift_tests": drift.get("tests") or {},
        "broken": integ.get("broken", 0), "warnings": integ.get("warnings", 0), "info": integ.get("info", 0),
        "tenants": {"total": len(sc), "healthy": sum(t["status"] == "HEALTHY" for t in sc),
                    "warn": sum(t["status"] == "WARN" for t in sc), "broken": sum(t["status"] == "BROKEN" for t in sc)},
        "new_tenants": integ.get("new_tenants", []), "missing_baseline": integ.get("missing_baseline_tenants", []),
        "baseline_count": integ.get("baseline_count"), "baseline_info": (drift.get("baseline") or {}).get("info", ""),
        "scorecard": sc,
        "findings": [f for f in integ.get("findings", []) if f.get("severity") in ("fail", "warn")],
        "failures": r.get("failures", []),
        "drift_failures": (drift.get("tests") or {}).get("failures", []),
        "counts": drift.get("counts", []), "added": drift.get("added", []), "removed": drift.get("removed", []),
        "faults": drift.get("faults", {}), "recs": integ.get("recommendations", []),
        "changes": load(d / "changes.json") or None,
        "runs": load(DATA / "runs.json").get("runs", []),
    }
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run")
    ap.add_argument("--out", default=str(SITE / "index.html"))
    a = ap.parse_args()
    stamp = a.run or sorted(p.name for p in DATA.iterdir() if p.is_dir() and STAMP_RE.match(p.name))[-1]
    D = build(stamp)
    js = json.dumps(D, ensure_ascii=False).replace("</", "<\\/")
    tpl = (SITE / "scripts" / "site_template.html").read_text()
    assert tpl.count("/*__DATA__*/null") == 1
    pathlib.Path(a.out).write_text(tpl.replace("/*__DATA__*/null", js))
    print(f"index.html built for run {stamp} (snapshot {D['snapshot']})")


if __name__ == "__main__":
    main()
