#!/usr/bin/env python3
"""Copy ONE nac-test daily run's summaries into the status site's data/ folder (keeps every previous run).

Only the summary files are copied (an allow-list): daily-summary.{json,md}, drift-summary.{json,md},
integrity-summary.{json,md}. Raw Robot output (log.html, output.xml, xunit.xml, report.html), console logs,
live-objects.json / live-snapshot.json and nac-data are NEVER copied.

Layout written:
  data/<YYYY-MM-DD-HHMM>/{daily,drift,integrity}-summary.{json,md} + run-meta.json
  data/latest/            copy of the newest run (stable URL)
  data/runs.json          manifest of all runs, newest first (stamp, snapshot, morning flag, headline numbers)

Usage:
  publish_run.py --daily-dir /tmp/nac-fresh-XXXX/results/daily-2026-10-23 [--stamp 2026-10-23-0800] [--site DIR]
  publish_run.py --reindex           # only rebuild data/runs.json from existing run folders
A run is a "morning" run when its local start time is before MORNING_CUTOFF_HOUR (default 12, env override).
"""
import argparse, datetime as dt, json, os, pathlib, re, shutil, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
ALLOW = ["daily-summary.json", "daily-summary.md", "drift-summary.json", "drift-summary.md",
         "integrity-summary.json", "integrity-summary.md"]
STAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}$")
CUTOFF = int(os.environ.get("MORNING_CUTOFF_HOUR", "12"))


def load(p):
    try:
        return json.load(open(p))
    except Exception:
        return {}


def run_info(d: pathlib.Path):
    daily, drift, integ = (load(d / f) for f in ("daily-summary.json", "drift-summary.json", "integrity-summary.json"))
    meta = load(d / "run-meta.json")
    stamp = d.name
    hh = int(stamp[11:13])
    sc = integ.get("scorecard", [])
    return {
        "stamp": stamp,
        "date": stamp[:10],
        "time_local": f"{stamp[11:13]}:{stamp[13:15]} AEDT",
        "morning": meta.get("morning", hh < CUTOFF),
        "kind": meta.get("kind", "scheduled" if hh < CUTOFF else "ad-hoc"),
        "snapshot": integ.get("pulled_at_local") or daily.get("generated_at_local"),
        "status": daily.get("status"),
        "headline": daily.get("headline"),
        "integrity_tests": (integ.get("robot") or {}).get("total"),
        "integrity_failed": (integ.get("robot") or {}).get("failed"),
        "drift_tests": (drift.get("tests") or {}).get("total"),
        "drift_failed": (drift.get("tests") or {}).get("failed"),
        "broken": integ.get("broken"), "warnings": integ.get("warnings"),
        "tenants": len(sc), "tenants_broken": sum(1 for t in sc if t.get("status") == "BROKEN"),
        "path": f"data/{stamp}/",
    }


def reindex():
    runs = sorted((p for p in (SITE / "data").iterdir() if p.is_dir() and STAMP_RE.match(p.name)), key=lambda p: p.name)
    idx = [run_info(p) for p in reversed(runs)]
    json.dump({"schema": 1, "generated_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
               "morning_cutoff_hour": CUTOFF, "runs": idx}, open(SITE / "data" / "runs.json", "w"), indent=1)
    if runs:
        lat = SITE / "data" / "latest"
        shutil.rmtree(lat, ignore_errors=True); lat.mkdir()
        for f in runs[-1].iterdir():
            if f.is_file():
                shutil.copy2(f, lat / f.name)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--daily-dir", help="results/daily-YYYY-MM-DD folder of the scratch nac-test copy")
    ap.add_argument("--stamp", help="YYYY-MM-DD-HHMM (local). Default: drift run start from drift-summary.json")
    ap.add_argument("--kind", default=None, help="scheduled | ad-hoc | sample (label only)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing run folder")
    ap.add_argument("--reindex", action="store_true")
    a = ap.parse_args()
    if a.reindex and not a.daily_dir:
        print(json.dumps(reindex()[:3], indent=1)); return
    src = pathlib.Path(a.daily_dir)
    srcs = {"daily-summary": src, "drift-summary": src / "drift", "integrity-summary": src / "integrity"}
    if not (src / "daily-summary.json").exists():
        sys.exit(f"no daily-summary.json in {src}")
    stamp = a.stamp
    if not stamp:
        g = load(src / "drift" / "drift-summary.json").get("generated_at") or load(src / "daily-summary.json")["generated_at"]
        stamp = dt.datetime.fromisoformat(g).strftime("%Y-%m-%d-%H%M")
    if not STAMP_RE.match(stamp):
        sys.exit(f"bad stamp {stamp}")
    dst = SITE / "data" / stamp
    if dst.exists() and not a.force:
        sys.exit(f"{dst} exists (use --force)")
    dst.mkdir(parents=True, exist_ok=True)
    for name in ALLOW:
        base = name.rsplit(".", 1)[0]
        f = srcs[base] / name
        if f.exists():
            shutil.copy2(f, dst / name)
        else:
            print("WARN missing", f, file=sys.stderr)
    hh = int(stamp[11:13])
    json.dump({"stamp": stamp, "kind": a.kind or ("scheduled" if hh < CUTOFF else "ad-hoc"), "morning": hh < CUTOFF,
               "published_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
               "files": [n for n in ALLOW if (dst / n).exists()]}, open(dst / "run-meta.json", "w"), indent=1)
    reindex()
    print(stamp)


if __name__ == "__main__":
    main()
