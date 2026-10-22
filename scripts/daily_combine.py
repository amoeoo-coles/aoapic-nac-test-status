#!/usr/bin/env python3
"""Combine results/drift-DATE and results/integrity-DATE into results/daily-DATE/ (daily-summary.{html,md,json} + zip).
No APIC access. Always exits 0."""
import argparse, datetime as dt, html, json, pathlib, re, shutil, sys, traceback
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent.parent
TZ = ZoneInfo("Australia/Melbourne")


def load(p):
    try:
        return json.loads(p.read_text())
    except Exception:
        return None


def body(p):
    try:
        t = p.read_text()
        m = re.search(r"<body[^>]*>(.*)</body>", t, re.S)
        return m.group(1) if m else t
    except Exception:
        return '<p style="font-size:13px;color:#c0392b;">Summary not available.</p>'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    a = ap.parse_args()
    res = ROOT / "results"
    dr, ir = res / f"drift-{a.date}", res / f"integrity-{a.date}"
    out = res / f"daily-{a.date}"
    shutil.rmtree(out, ignore_errors=True)
    out.mkdir(parents=True)
    D, I = load(dr / "drift-summary.json"), load(ir / "integrity-summary.json")
    dstat = (D or {}).get("status", "error")
    istat = (I or {}).get("status", "error")
    if "error" in (dstat, istat):
        status = "error"
    elif dstat == "drift" or istat in ("broken", "warnings"):
        status = "attention"
    else:
        status = "ok"
    dhead = (D or {}).get("headline", "DRIFT CHECK FAILED - no summary")
    ihead = (I or {}).get("headline", "INTEGRITY CHECK FAILED - no summary")
    short_d = dhead.split(" - ")[0]
    short_i = ihead.split(" - ")[0]
    headline = f"{short_d} | {short_i}"
    gen = dt.datetime.now(TZ)
    S = {"schema": 1, "date": a.date, "status": status, "headline": headline,
         "generated_at": gen.isoformat(timespec="seconds"), "generated_at_local": gen.strftime("%Y-%m-%d %H:%M:%S %Z"),
         "drift": {"status": dstat, "headline": dhead, "tests": (D or {}).get("tests", {}).get("total"),
                   "failed": (D or {}).get("tests", {}).get("failed"), "added": len((D or {}).get("added", []) or []),
                   "removed": len((D or {}).get("removed", []) or []), "folder": "drift/"},
         "integrity": {"status": istat, "headline": ihead, "broken": (I or {}).get("broken"),
                       "warnings": (I or {}).get("warnings"),
                       "robot": {k: (I or {}).get("robot", {}).get(k) for k in ("total", "passed", "failed")},
                       "scorecard": [{k: t[k] for k in ("tenant", "in_baseline", "broken", "warnings", "score", "status")}
                                     for t in (I or {}).get("scorecard", [])], "folder": "integrity/"}}
    for src, name in ((dr, "drift"), (ir, "integrity")):
        if src.is_dir():
            shutil.copytree(src, out / name)
    (out / "daily-summary.json").write_text(json.dumps(S, indent=2))
    md = [f"# Daily ACI report: {a.date}", "", f"## {headline}", "", f"- Generated: {S['generated_at_local']}",
          f"- Overall status: `{status}`", "", "## 1. Drift (baseline vs live)", "", f"**{dhead}**", "",
          "Details: `drift/drift-summary.md`", "", "## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)",
          "", f"**{ihead}**", ""]
    if I and I.get("scorecard"):
        md += ["| Tenant | Baseline | Broken | Warn | Score | Status |", "|---|---|---:|---:|---:|---|"]
        md += [f"| {t['tenant']} | {'yes' if t['in_baseline'] else 'NEW'} | {t['broken']} | {t['warnings']} | "
               f"{t['score']} | {t['status']} |" for t in I["scorecard"]]
    md += ["", "Details: `integrity/integrity-summary.md`", ""]
    (out / "daily-summary.md").write_text("\n".join(md))
    col = {"ok": "#1e8449", "attention": "#c0392b", "error": "#7f8c8d"}[status]
    e = html.escape
    h = ['<!DOCTYPE html><html><head><meta charset="utf-8"><title>Daily ACI report ' + e(a.date) + '</title></head>'
         '<body style="margin:12px;"><div style="font-family:Arial,Helvetica,sans-serif;color:#222;max-width:1100px;">',
         f'<h2 style="margin:0 0 6px 0;">Daily ACI report: {e(a.date)}</h2>',
         f'<div style="background:{col};color:#fff;padding:10px 14px;font-size:18px;font-weight:bold;">{e(headline)}</div>',
         f'<p style="font-size:12px;">Generated {e(S["generated_at_local"])}. Part 1 = drift vs frozen baseline; '
         'part 2 = logical integrity of every tenant\'s object graph. Full Robot reports are in the attached zip '
         '(drift/ and integrity/robot/).</p>',
         '<h2 style="border-bottom:2px solid #333;margin-top:18px;">1. Drift (baseline vs live)</h2>', body(dr / "drift-summary.html"),
         '<h2 style="border-bottom:2px solid #333;margin-top:18px;">2. Tenant logical integrity</h2>',
         body(ir / "integrity-summary.html"), "</div></body></html>\n"]
    (out / "daily-summary.html").write_text("\n".join(h))
    zp = res / f"daily-{a.date}.zip"
    zp.unlink(missing_ok=True)
    shutil.make_archive(str(res / f"daily-{a.date}"), "zip", res, out.name)
    print(headline)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
    sys.exit(0)
