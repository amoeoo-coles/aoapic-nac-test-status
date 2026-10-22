#!/usr/bin/env bash
# Daily ACI report = drift report + tenant logical-integrity report, combined. READ-ONLY (aaaLogin POST + GETs).
#   1. scripts/drift_report.sh [options]  -> results/drift-YYYY-MM-DD/      (baseline vs live, nac-test config suite)
#   2. scripts/integrity_report.sh        -> results/integrity-YYYY-MM-DD/  (relationship graph + nac-test integrity suite)
#   3. scripts/daily_combine.py           -> results/daily-YYYY-MM-DD/daily-summary.{html,md,json} (+ both runs copied
#      in as drift/ and integrity/) and results/daily-YYYY-MM-DD.zip; prunes daily results older than 30 days.
# Always exits 0; overall outcome in daily-summary.json ("status": ok | attention | error).
# Usage: scripts/daily_report.sh [--rebaseline] [--refresh-data]   (options are passed to drift_report.sh)
# cron (07:00 Melbourne): 0 7 * * *  cd /path/to/nac-test && scripts/daily_report.sh >> results/daily-cron.log 2>&1
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD
export TZ=Australia/Melbourne
case "${1:-}" in -h|--help) sed -n '2,10p' "$0"; exit 0 ;; esac
DAY=$(date +%F)
log() { echo "[$(date '+%F %T %Z')] $*"; }
log "daily: drift report"
scripts/drift_report.sh "$@" || true
log "daily: integrity report"
scripts/integrity_report.sh || true
log "daily: combining"
.venv/bin/python scripts/daily_combine.py --date "$DAY" || log "WARN combine failed"
CUT=$(date -d '30 days ago' +%F)
for d in results/daily-????-??-?? results/daily-????-??-??.zip; do
  [[ -e "$d" ]] || continue
  ds=${d#results/daily-}; ds=${ds%.zip}
  [[ "$ds" < "$CUT" ]] && { log "pruning $d"; rm -rf "$d"; }
done
log "daily summary: $ROOT/results/daily-$DAY/daily-summary.html  zip: $ROOT/results/daily-$DAY.zip"
exit 0
