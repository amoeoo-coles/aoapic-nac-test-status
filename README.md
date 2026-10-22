# AOAPIC nac-test status

Static status page for the read-only [nac-test](https://github.com/netascode/nac-test) drift and logical-integrity checks run against the public **Cisco DevNet Always-On APIC sandbox** (`https://sandboxapicdc.cisco.com`).

**Live page:** https://amoeoo-coles.github.io/aoapic-nac-test-status/

- `index.html` is a single self-contained page (no external assets) with KPIs, a tenant scorecard, broken relations, failed tests, warnings, drift vs. baseline and charts.
- `data/latest/` holds the summary JSON/MD of the latest run (APIC snapshot 2026-10-22 18:57 AEDT). `data/2026-10-22-1105/` holds the earlier 11:05 AEDT run.
- `scripts/` holds the generator scripts. They are read-only against the APIC: `aaaLogin`/`aaaLogout` plus GETs. Credentials come from environment variables or a local, git-ignored `.env`, and none are stored here.

The sandbox is shared by every DevNet user and changes all the time, so this page is a point-in-time snapshot.
