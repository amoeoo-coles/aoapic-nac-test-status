#!/usr/bin/env python3
"""Compare two published runs in data/ and write data/<current>/changes.{json,md}.

Default: current = newest run in data/, previous = newest MORNING run (data/runs.json "morning": true)
whose stamp is older than the current one, i.e. "changes since the previous morning".
  compare_runs.py                                   # auto
  compare_runs.py --current 2026-10-22-1949 --prev 2026-10-22-1105
Covers: test pass/fail deltas (integrity + drift) incl. newly failing / fixed tests, tenants newly broken / fixed /
added / removed, broken relations added / resolved, new critical (and major) faults, drift-vs-baseline count table,
objects that appeared / disappeared since the previous run, and faultInst totals.
Only reads the summary JSON in data/; never talks to the APIC.
"""
import argparse, json, pathlib, re, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
DATA = SITE / "data"
STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}$")


def load(p):
    try:
        return json.load(open(p))
    except Exception:
        return {}


def runs():
    return sorted(p.name for p in DATA.iterdir() if p.is_dir() and STAMP_RE.match(p.name))


def is_morning(stamp):
    m = load(DATA / stamp / "run-meta.json")
    if "morning" in m:
        return bool(m["morning"])
    return int(stamp[11:13]) < 12


def pick_prev(cur):
    older = [r for r in runs() if r < cur and is_morning(r)]
    return older[-1] if older else None


def bundle(stamp):
    d = DATA / stamp
    return {"stamp": stamp, "daily": load(d / "daily-summary.json"), "drift": load(d / "drift-summary.json"),
            "integ": load(d / "integrity-summary.json")}


def tests(b):
    r = b["integ"].get("robot") or {}
    t = b["drift"].get("tests") or {}
    return {"integrity": {k: r.get(k, 0) for k in ("total", "passed", "failed")},
            "drift": {k: t.get(k, 0) for k in ("total", "passed", "failed")},
            "integrity_fail_names": sorted({f"{f['suite']} :: {f['test']}" for f in r.get("failures", [])}),
            "drift_fail_names": sorted({f"{f['suite']} :: {f['test']}" for f in t.get("failures", [])})}


def compare(cur, prev):
    C, P = bundle(cur), bundle(prev)
    tc, tp = tests(C), tests(P)
    out = {"schema": 1, "current": cur, "previous": prev,
           "current_snapshot": C["integ"].get("pulled_at_local"), "previous_snapshot": P["integ"].get("pulled_at_local"),
           "current_status": C["daily"].get("status"), "current_headline": C["daily"].get("headline")}
    # tests
    tv = {}
    for k in ("integrity", "drift"):
        tv[k] = {m: {"prev": tp[k][m], "now": tc[k][m], "delta": tc[k][m] - tp[k][m]} for m in ("total", "passed", "failed")}
    out["tests"] = tv
    out["tests_newly_failing"] = sorted(set(tc["integrity_fail_names"]) - set(tp["integrity_fail_names"])) + \
        sorted(set(tc["drift_fail_names"]) - set(tp["drift_fail_names"]))
    out["tests_fixed"] = sorted(set(tp["integrity_fail_names"]) - set(tc["integrity_fail_names"])) + \
        sorted(set(tp["drift_fail_names"]) - set(tc["drift_fail_names"]))
    # tenants
    sc = {t["tenant"]: t for t in C["integ"].get("scorecard", [])}
    sp = {t["tenant"]: t for t in P["integ"].get("scorecard", [])}
    out["tenants"] = {
        "prev_total": len(sp), "now_total": len(sc),
        "added": sorted(set(sc) - set(sp), key=str.lower),
        "removed": sorted(set(sp) - set(sc), key=str.lower),
        "newly_broken": sorted([t for t in sc if t in sp and sc[t]["status"] == "BROKEN" and sp[t]["status"] != "BROKEN"], key=str.lower),
        "added_broken": sorted([t for t in sc if t not in sp and sc[t]["status"] == "BROKEN"], key=str.lower),
        "fixed": sorted([t for t in sc if t in sp and sp[t]["status"] == "BROKEN" and sc[t]["status"] != "BROKEN"], key=str.lower),
        "status_changes": [{"tenant": t, "prev": sp[t]["status"], "now": sc[t]["status"], "prev_score": sp[t]["score"], "now_score": sc[t]["score"]}
                           for t in sorted(sc, key=str.lower) if t in sp and (sp[t]["status"] != sc[t]["status"] or sp[t]["score"] != sc[t]["score"])],
        "broken_prev": sum(1 for t in sp.values() if t["status"] == "BROKEN"),
        "broken_now": sum(1 for t in sc.values() if t["status"] == "BROKEN"),
    }
    # broken relations
    # match broken relations by (tenant, check, dn); within a group exact reasons match first, the rest are paired
    # as "reason changed" (same object, different APIC message) and only the leftovers count as added / resolved
    slim = lambda f: {k: f.get(k) for k in ("tenant", "check", "dn", "reason")}
    def groups(b):
        g = {}
        for f in b["integ"].get("findings", []):
            if f.get("severity") == "fail":
                g.setdefault((f.get("tenant"), f.get("check"), f.get("dn")), []).append(f)
        return g
    gc, gp = groups(C), groups(P)
    added, resolved, changed = [], [], []
    for k in sorted(set(gc) | set(gp), key=str):
        c, p_ = list(gc.get(k, [])), list(gp.get(k, []))
        for f in list(c):
            m = next((x for x in p_ if x.get("reason") == f.get("reason")), None)
            if m is not None:
                c.remove(f); p_.remove(m)
        while c and p_:
            f, m = c.pop(0), p_.pop(0)
            changed.append({**slim(f), "prev_reason": m.get("reason")})
        added += [slim(f) for f in c]; resolved += [slim(f) for f in p_]
    out["broken_relations"] = {"prev": sum(map(len, gp.values())), "now": sum(map(len, gc.values())),
                               "added": added, "resolved": resolved, "reason_changed": changed}
    wc = sum(1 for f in C["integ"].get("findings", []) if f.get("severity") == "warn")
    wp = sum(1 for f in P["integ"].get("findings", []) if f.get("severity") == "warn")
    out["warnings"] = {"prev": wp, "now": wc, "delta": wc - wp}
    # faults
    fk = lambda f: (f.get("code"), f.get("affected") or f.get("dn"))
    fc = {fk(f): f for f in (C["integ"].get("faults") or {}).get("critical_major", [])}
    fp = {fk(f): f for f in (P["integ"].get("faults") or {}).get("critical_major", [])}
    fs = lambda f: {k: f.get(k) for k in ("tenant", "severity", "code", "affected", "descr")}
    new = [fs(fc[k]) for k in sorted(set(fc) - set(fp), key=str)]
    out["faults"] = {
        "new_critical": [f for f in new if f["severity"] == "critical"],
        "new_major": [f for f in new if f["severity"] == "major"],
        "cleared_critical_major": [fs(fp[k]) for k in sorted(set(fp) - set(fc), key=str)],
        "fabric_totals": {s: {"prev": (P["drift"].get("faults") or {}).get(s, 0), "now": (C["drift"].get("faults") or {}).get(s, 0)}
                          for s in ("critical", "major", "minor", "warning", "total")},
    }
    # drift table
    pc = {c["type"]: c for c in P["drift"].get("counts", [])}
    out["drift_table"] = [{"type": c["type"], "baseline": c["baseline"], "prev": pc.get(c["type"], {}).get("current"),
                           "now": c["current"], "delta": c["current"] - pc.get(c["type"], {}).get("current", 0),
                           "added_vs_baseline": c["added"], "removed_vs_baseline": c["removed"]}
                          for c in C["drift"].get("counts", [])]
    da = lambda b, k: {x["dn"]: x for x in b["drift"].get(k, [])}
    out["drift_objects"] = {
        "appeared": [da(C, "added")[d] for d in sorted(set(da(C, "added")) - set(da(P, "added")))],
        "disappeared_again": [da(P, "added")[d] for d in sorted(set(da(P, "added")) - set(da(C, "added")))],
        "newly_removed_from_baseline": [da(C, "removed")[d] for d in sorted(set(da(C, "removed")) - set(da(P, "removed")))],
        "restored_to_baseline": [da(P, "removed")[d] for d in sorted(set(da(P, "removed")) - set(da(C, "removed")))],
    }
    return out


def md(o):
    L = [f"# Changes since previous morning ({o['previous']} -> {o['current']})", "",
         f"Previous snapshot {o['previous_snapshot']}; current snapshot {o['current_snapshot']}.", "",
         "| Tests | Prev | Now | Delta |", "|---|---:|---:|---:|"]
    for k in ("integrity", "drift"):
        for m in ("total", "passed", "failed"):
            v = o["tests"][k][m]; L.append(f"| {k} {m} | {v['prev']} | {v['now']} | {v['delta']:+d} |")
    t = o["tenants"]
    L += ["", f"Tenants: {t['prev_total']} -> {t['now_total']}; broken {t['broken_prev']} -> {t['broken_now']}",
          f"- added: {', '.join(t['added']) or 'none'}", f"- removed: {', '.join(t['removed']) or 'none'}",
          f"- newly broken: {', '.join(t['newly_broken'] + [x + ' (new)' for x in t['added_broken']]) or 'none'}",
          f"- fixed: {', '.join(t['fixed']) or 'none'}", "",
          f"Broken relations: {o['broken_relations']['prev']} -> {o['broken_relations']['now']}"]
    for x in o["broken_relations"]["added"]: L.append(f"- ADDED {x['tenant']} | {x['check']} | `{x['dn']}` | {x['reason']}")
    for x in o["broken_relations"]["resolved"]: L.append(f"- RESOLVED {x['tenant']} | {x['check']} | `{x['dn']}` | {x['reason']}")
    for x in o["broken_relations"].get("reason_changed", []): L.append(f"- STILL BROKEN, reason changed: {x['tenant']} | {x['check']} | `{x['dn']}`")
    L += ["", "New critical faults:"] + [f"- {f['code']} {f['tenant']} `{f['affected']}`: {f['descr']}" for f in o["faults"]["new_critical"]] + \
         (["- none"] if not o["faults"]["new_critical"] else [])
    L += ["", "| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |", "|---|---:|---:|---:|---:|---:|---:|"]
    for r in o["drift_table"]:
        L.append(f"| {r['type']} | {r['baseline']} | {r['prev']} | {r['now']} | {r['delta']:+d} | {r['added_vs_baseline']} | {r['removed_vs_baseline']} |")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--current"); ap.add_argument("--prev")
    a = ap.parse_args()
    cur = a.current or runs()[-1]
    prev = a.prev or pick_prev(cur)
    if not prev:
        print(f"no previous morning run before {cur}; nothing to compare", file=sys.stderr)
        json.dump({"schema": 1, "current": cur, "previous": None}, open(DATA / cur / "changes.json", "w"), indent=1)
        return
    o = compare(cur, prev)
    json.dump(o, open(DATA / cur / "changes.json", "w"), indent=1)
    open(DATA / cur / "changes.md", "w").write(md(o))
    print(f"changes {prev} -> {cur}: tenants +{len(o['tenants']['added'])}/-{len(o['tenants']['removed'])}, "
          f"newly broken {o['tenants']['newly_broken'] + o['tenants']['added_broken']}, fixed {o['tenants']['fixed']}, "
          f"broken rel +{len(o['broken_relations']['added'])}/-{len(o['broken_relations']['resolved'])}, "
          f"new critical faults {len(o['faults']['new_critical'])}")


if __name__ == "__main__":
    main()
