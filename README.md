# AOAPIC nac-test status

Static status page for the read-only [nac-test](https://github.com/netascode/nac-test) drift and logical-integrity checks run against the public **Cisco DevNet Always-On APIC sandbox** (`https://sandboxapicdc.cisco.com`).

**Live page:** https://amoeoo-coles.github.io/aoapic-nac-test-status/

- `index.html` is a single self-contained page (no external assets) with KPIs, a tenant scorecard, broken relations, failed tests, warnings, drift vs. baseline and charts.
- `data/<YYYY-MM-DD-HHMM>/` holds each run's summary JSON/MD plus `changes.{json,md}` (diff vs. the previous morning run). `data/latest/` is the newest run, and `data/runs.json` is the run manifest.
- Daily routine, data layout and "previous morning" logic: see [RUNBOOK.md](RUNBOOK.md) (`scripts/morning_routine.sh`, `publish_run.py`, `compare_runs.py`, `build_site.py`, `build_email.py`, `security_scan.py`).
- `scripts/` holds the generator scripts. They are read-only against the APIC: `aaaLogin`/`aaaLogout` plus GETs. Credentials come from environment variables or a local, git-ignored `.env`, and none are stored here.

The sandbox is shared by every DevNet user and changes all the time, so this page is a point-in-time snapshot.
