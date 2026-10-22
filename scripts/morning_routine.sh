#!/usr/bin/env bash
# Weekday 8 AM AOAPIC routine (Melbourne time). READ-ONLY against the APIC; never modifies /workspace/nac-test.
#   1. scratch copy of $NAC_SRC (default /workspace/nac-test) -> /tmp/nac-fresh-YYYYMMDD-HHMMSS (results/ and zips excluded)
#   2. scripts/daily_report.sh in the scratch copy (drift + integrity, aaaLogin + GETs only)
#   3. publish_run.py   -> data/<YYYY-MM-DD-HHMM>/ summaries only, data/latest/, data/runs.json
#   4. compare_runs.py  -> data/<stamp>/changes.{json,md} vs the previous MORNING run (auto)
#   5. build_site.py    -> index.html ; build_email.py -> /tmp/aoapic-email-<stamp>.html (not published)
#   6. security_scan.py -> aborts before git if anything sensitive would be published
#   7. git commit + push to main (skip with --no-push); then poll the Pages URL for the new run stamp
# Email is sent separately by the agent with the Gmail connector (subject printed at the end).
# Usage: scripts/morning_routine.sh [--no-push] [--kind scheduled|sample|ad-hoc] [--prev STAMP]
set -euo pipefail
SITE=$(cd "$(dirname "$0")/.." && pwd)
NAC_SRC=${NAC_SRC:-/workspace/nac-test}
VENV=${NAC_VENV:-/workspace/aci-nac/.venv}      # any venv with requirements.txt of nac-test installed
PAGES=${PAGES_URL:-https://amoeoo-coles.github.io/aoapic-nac-test-status/}
export TZ=Australia/Melbourne
PUSH=1; KIND=""; PREV=""; SAMPLE=""
while [[ $# -gt 0 ]]; do case "$1" in
  --no-push) PUSH=0 ;; --kind) KIND=$2; shift ;; --prev) PREV=$2; shift ;;
  -h|--help) sed -n '2,13p' "$0"; exit 0 ;; *) echo "unknown option $1" >&2; exit 2 ;; esac; shift; done
[[ "$KIND" == sample ]] && SAMPLE=--sample
log() { echo "[$(date '+%F %T %Z')] $*"; }

TS=$(date +%Y%m%d-%H%M%S); STAMP=$(date +%Y-%m-%d-%H%M); DAY=$(date +%F)
S=/tmp/nac-fresh-$TS
log "scratch copy $NAC_SRC -> $S"
mkdir -p "$S"; (cd "$NAC_SRC" && tar --exclude=./results --exclude='./*.zip' --exclude=./.venv -cf - .) | tar -xf - -C "$S"
mkdir -p "$S/results"; ln -s "$VENV" "$S/.venv"
log "daily report (read-only)"; (cd "$S" && scripts/daily_report.sh) || true
cd "$SITE"
python3 scripts/publish_run.py --daily-dir "$S/results/daily-$DAY" --stamp "$STAMP" ${KIND:+--kind "$KIND"}
python3 scripts/compare_runs.py --current "$STAMP" ${PREV:+--prev "$PREV"}
python3 scripts/publish_run.py --reindex >/dev/null      # refresh data/latest with changes.*
python3 scripts/build_site.py --run "$STAMP"
python3 scripts/build_email.py --run "$STAMP" $SAMPLE
python3 scripts/security_scan.py || { log "SECURITY SCAN FAILED - not committing"; exit 1; }
if [[ $PUSH -eq 1 ]]; then
  git add -A && git commit -qm "AOAPIC run $STAMP (APIC snapshot $(python3 -c "import json;print(json.load(open('data/$STAMP/integrity-summary.json')).get('pulled_at_local'))"))" && git push -q origin main
  log "pushed $(git rev-parse --short HEAD); waiting for Pages"
  for i in $(seq 1 24); do
    code=$(curl -s -o /tmp/pages.html -w '%{http_code}' "$PAGES?nocache=$RANDOM")
    [[ "$code" == 200 ]] && grep -q "\"stamp\": \"$STAMP\"" /tmp/pages.html && { log "Pages 200 with run $STAMP"; break; }
    sleep 10
  done
fi
log "done: run $STAMP  scratch $S  email /tmp/aoapic-email-$STAMP.html"
