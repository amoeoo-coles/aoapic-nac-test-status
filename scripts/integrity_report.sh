#!/usr/bin/env bash
# Daily ACI tenant logical-integrity report. READ-ONLY against the APIC (aaaLogin POST + GETs only).
#   1. scripts/integrity_check.py collect  -> results/integrity-YYYY-MM-DD/live-objects.json + nac-data/integrity.nac.yaml
#   2. nac-test (templates/tests/integrity, tag 'integrity', one suite per tenant) -> results/integrity-YYYY-MM-DD/robot/
#   3. scripts/integrity_check.py report   -> integrity-summary.{md,html,json} (headline, scorecard, broken relations,
#      warnings, recommendations), then zips the folder and prunes integrity results older than 30 days.
# Always exits 0; the outcome is in integrity-summary.json ("status": broken | warnings | healthy | error).
# Usage: scripts/integrity_report.sh
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD
export TZ=Australia/Melbourne
case "${1:-}" in -h|--help) sed -n '2,9p' "$0"; exit 0 ;; esac
[[ -f .env ]] && { set -a; source .env; set +a; }
PY=.venv/bin/python
DAY=$(date +%F)
OUT=results/integrity-$DAY
log() { echo "[$(date '+%F %T %Z')] $*"; }

rm -rf "$OUT" "$OUT.zip"; mkdir -p "$OUT"
log "integrity: pulling APIC object graph -> $OUT"
$PY scripts/integrity_check.py collect --out "$OUT" --date "$DAY" || true
rc=-1
if [[ -f "$OUT/nac-data/integrity.nac.yaml" ]]; then
  log "integrity: running nac-test (tag integrity) -> $OUT/robot"
  rc=0; .venv/bin/nac-test -d "$OUT/nac-data/" -d defaults/ -t templates/ -o "$OUT/robot/" -i integrity --processes 4 \
        > "$OUT/nac-test-console.log" 2>&1 || rc=$?
  log "integrity: nac-test exit code $rc"
else
  log "integrity: no snapshot (APIC pull failed), skipping nac-test"
fi
$PY scripts/integrity_check.py report --out "$OUT" --date "$DAY" --baseline baseline/data \
    --robot-xml "$OUT/robot/output.xml" --robot-rc "$rc" || true

$PY - "$OUT" <<'PY' || log "WARN zip failed"
import shutil, sys, pathlib
p = pathlib.Path(sys.argv[1]); shutil.make_archive(str(p), "zip", p.parent, p.name)
PY
CUT=$(date -d '30 days ago' +%F)
for d in results/integrity-????-??-?? results/integrity-????-??-??.zip; do
  [[ -e "$d" ]] || continue
  ds=${d#results/integrity-}; ds=${ds%.zip}
  [[ "$ds" < "$CUT" ]] && { log "pruning $d"; rm -rf "$d"; }
done
log "integrity summary: $ROOT/$OUT/integrity-summary.{md,html,json}  zip: $ROOT/$OUT.zip"
exit 0
