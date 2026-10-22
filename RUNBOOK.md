# RUNBOOK: weekday 8 AM AOAPIC routine

Live page: https://amoeoo-coles.github.io/aoapic-nac-test-status/. Repo: `amoeoo-coles/aoapic-nac-test-status` (branch `main`, GitHub Pages from the root).
All times are Melbourne local (AEDT, UTC+11).

## Rules
- **Read-only.** Only `aaaLogin`/`aaaLogout` POSTs and GETs reach `https://sandboxapicdc.cisco.com`. Never push config to the APIC.
- **Never modify `/workspace/nac-test`.** Every run works on a scratch copy at `/tmp/nac-fresh-YYYYMMDD-HHMMSS`.
- **Publish summaries only.** Never publish Robot `log.html`/`report.html`/`output.xml`/`xunit.xml`, console logs, live object dumps, `.env` values or cookies. `scripts/security_scan.py` blocks the commit if any of these would go out.

## One command
```bash
cd /workspace/aoapic-status-site
scripts/morning_routine.sh                 # weekday 8 AM run: scratch copy, report, publish, compare, build, scan, push, check Pages
scripts/morning_routine.sh --no-push       # dry run (writes data/ + index.html locally, no git push)
scripts/morning_routine.sh --kind sample --prev 2026-10-22-1105   # how the 22 Oct sample run was compared
```
Then email the report with the Gmail connector (namespace `user-Gmail`, `send_email`). Send it to 179172@gmail.com only.
- Subject: `AOAPIC drift report – <Ddd D Mon YYYY>`. The routine prints it.
- HTML body: `/tmp/aoapic-email-<stamp>.html`, built by `scripts/build_email.py`. It uses inline CSS and tables, so it reads well in Gmail.

## Steps (if you run them by hand)
| # | Command | Output |
|---|---|---|
| 1 | `cp` of `/workspace/nac-test` to `/tmp/nac-fresh-…` (leave out `results/` and zips; symlink `.venv` to `/workspace/aci-nac/.venv`, which has nac-test 2.0.1) | scratch copy |
| 2 | `cd /tmp/nac-fresh-… && scripts/daily_report.sh` | `results/daily-YYYY-MM-DD/` (drift + integrity summaries) |
| 3 | `scripts/publish_run.py --daily-dir /tmp/nac-fresh-…/results/daily-YYYY-MM-DD [--stamp YYYY-MM-DD-HHMM] [--kind …]` | `data/<stamp>/{daily,drift,integrity}-summary.{json,md}` and `run-meta.json`, `data/latest/`, `data/runs.json` |
| 4 | `scripts/compare_runs.py [--current STAMP] [--prev STAMP]` | `data/<stamp>/changes.{json,md}` |
| 5 | `scripts/publish_run.py --reindex` | refreshes `data/latest/` (now includes `changes.*`) |
| 6 | `scripts/build_site.py [--run STAMP]` | `index.html` (template `scripts/site_template.html`) |
| 7 | `scripts/build_email.py [--run STAMP] [--sample]` | `/tmp/aoapic-email-<stamp>.html` and the subject line |
| 8 | `scripts/security_scan.py` | exits 1 if any file to publish is a raw artefact, matches a secret pattern, or contains a `.env` value |
| 9 | `git add -A && git commit -m "AOAPIC run <stamp>" && git push origin main` | then poll the Pages URL until it returns 200 and contains `"stamp": "<stamp>"` (takes 1 to 3 min) |

## Data layout
```
data/
  runs.json                 manifest, newest first: stamp, kind, morning flag, snapshot, headline numbers
  latest/                   copy of the newest run (stable links)
  YYYY-MM-DD-HHMM/          one folder per run, never overwritten (publish_run.py refuses unless --force)
    daily-summary.json|md  drift-summary.json|md  integrity-summary.json|md
    run-meta.json           kind (scheduled | ad-hoc | sample), morning true/false
    changes.json|md         diff against the previous morning run
```

## How "previous morning" is chosen
A run is a **morning** run when it starts before 12:00 local (set `MORNING_CUTOFF_HOUR` to change this, or set `"morning"` in `run-meta.json`).
`compare_runs.py` compares the current run with the **newest morning run whose stamp is older than the current one**.
Ad-hoc and sample runs later in the day (such as 2026-10-22-1857 and 2026-10-22-1949) are not morning runs, so tomorrow's 08:00 run is compared with 2026-10-22-1105 automatically.
After that, each weekday run is compared with the one before it. Monday is compared with Friday.
To force a comparison, pass `--prev STAMP`.

## What the diff covers
- Test totals and pass/fail deltas for the integrity suite and the drift suite, plus which tests started failing or were fixed.
- Tenants added or removed on the APIC, newly broken (including new tenants that are broken), and fixed, with any status or score changes.
- Broken relations added or resolved, matched on tenant + check + DN. A relation that stays broken with a different APIC message is listed as "reason changed".
- New critical and major faults on tenant objects (`faultInst`), and changes in the fabric fault totals.
- A drift table of object counts per type (baseline, previous morning, now) and baseline objects deleted since the previous morning.

## Scheduling
Example cron, weekdays at 08:00 Melbourne time: `0 8 * * 1-5  cd /workspace/aoapic-status-site && scripts/morning_routine.sh >> /tmp/aoapic-morning.log 2>&1`.
The email step needs the agent (Gmail connector), so in practice an agent schedule runs the script and then sends the mail.

## Housekeeping
- The scratch copies in `/tmp/nac-fresh-*` can be deleted after the run (`find /tmp -maxdepth 1 -name 'nac-fresh-*' -mtime +7 -exec rm -rf {} +`).
- Re-baselining is a deliberate act. Run it in a scratch copy (`scripts/drift_report.sh --refresh-data --rebaseline`) and only copy `baseline/` back into `/workspace/nac-test` if Aung asks for it.
