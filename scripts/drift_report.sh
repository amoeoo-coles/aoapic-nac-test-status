#!/usr/bin/env bash
# Daily ACI drift report. READ-ONLY against the APIC (aaaLogin POST + GETs only).
#   1. freezes data/ into baseline/ on first run (or with --rebaseline)
#   2. runs nac-test with baseline/data against the live APIC -> results/drift-YYYY-MM-DD/ (-e integrity: the
#      logical-integrity suite runs separately, see scripts/integrity_report.sh / scripts/daily_report.sh)
#   3. REST pull (fvTenant, fvCtx, fvBD, fvSubnet, fvAp, fvAEPg) vs baseline + faultInst counts
#   4. writes drift-summary.{md,html,json}, zips the folder, prunes drift results older than 30 days
# Always exits 0; the outcome is in drift-summary.json ("status": drift | no_drift | error).
# Usage: scripts/drift_report.sh [--rebaseline] [--refresh-data]
#   --rebaseline    copy the current data/ over baseline/ before running (new expected state)
#   --refresh-data  regenerate data/ from the live APIC first (scripts/build_data.py); use with --rebaseline
set -uo pipefail
cd "$(dirname "$0")/.."
ROOT=$PWD
export TZ=Australia/Melbourne
REBASE=0; REFRESH=0
for a in "$@"; do
  case "$a" in
    --rebaseline) REBASE=1 ;;
    --refresh-data) REFRESH=1 ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "unknown option: $a" >&2; exit 0 ;;
  esac
done
[[ -f .env ]] && { set -a; source .env; set +a; }
PY=.venv/bin/python
DAY=$(date +%F)
OUT=results/drift-$DAY
log() { echo "[$(date '+%F %T %Z')] $*"; }

if [[ -z "${ACI_URL:-}" || -z "${ACI_USERNAME:-}" || -z "${ACI_PASSWORD:-}" ]]; then
  mkdir -p "$OUT"
  printf '{"schema":1,"date":"%s","status":"error","drift":null,"headline":"DRIFT CHECK FAILED - ACI_URL/ACI_USERNAME/ACI_PASSWORD not set","errors":["missing credentials in .env"]}\n' "$DAY" > "$OUT/drift-summary.json"
  log "missing ACI_* env vars (see .env.example)"; exit 0
fi

# 1. baseline
if [[ $REFRESH -eq 1 ]]; then log "refreshing data/ from APIC"; $PY scripts/build_data.py || log "WARN build_data.py failed"; fi
if [[ ! -d baseline/data || $REBASE -eq 1 ]]; then
  log "freezing data/ -> baseline/data/"
  rm -rf baseline/data && mkdir -p baseline/data && cp data/*.nac.yaml baseline/data/
  {
    echo "# Baseline (expected state) for the daily drift report"
    echo
    echo "- Frozen: $(date '+%Y-%m-%d %H:%M %Z') (Australia/Melbourne) by \`scripts/drift_report.sh$([[ $REBASE -eq 1 ]] && echo ' --rebaseline')\`"
    echo "- Source: copy of \`data/\`$([[ $REFRESH -eq 1 ]] && echo ", refreshed from the APIC just before freezing" || echo ", last pulled from the APIC at $(date -r data '+%Y-%m-%d %H:%M %Z')")"
    echo "- APIC: ${ACI_URL}"
    echo "- Files: $(ls baseline/data | wc -l) tenant files ($(ls baseline/data | sed 's/^tenant_//;s/\.nac\.yaml$//' | paste -sd, - | sed 's/,/, /g'))"
    echo "- Out of scope (exist on the APIC but not in this baseline, so they show up as \"added\"): Production_Tenant, Production_Tenant2, Production_Tenant22, tn_TEST1"
    echo
    echo "The drift report treats \`baseline/data/\` as the expected state and never overwrites it unless run with"
    echo "\`--rebaseline\` (optionally \`--refresh-data --rebaseline\` to pull the live APIC first)."
    echo
    echo "## SHA-256"
    echo '```'
    (cd baseline/data && sha256sum *.nac.yaml)
    echo '```'
  } > baseline/BASELINE_INFO.md
else
  log "using existing baseline/data/ ($(ls baseline/data | wc -l) files)"
fi

# 2. nac-test (login/request logging is suppressed in templates/resources/apic.resource)
rm -rf "$OUT" "$OUT.zip"; mkdir -p "$OUT"
log "running nac-test -> $OUT"
rc=0; .venv/bin/nac-test -d baseline/data/ -d defaults/ -t templates/ -o "$OUT/" -e integrity > "$OUT/nac-test-console.log" 2>&1 || rc=$?
log "nac-test exit code $rc"

# 3+4. REST pull, compare, summaries
$PY scripts/drift_compare.py --results "$OUT" --baseline baseline --nac-rc "$rc" --date "$DAY" || true
if [[ ! -f "$OUT/drift-summary.json" ]]; then
  printf '{"schema":1,"date":"%s","status":"error","drift":null,"headline":"DRIFT CHECK FAILED - summary not generated","nac_test_rc":%s,"errors":["drift_compare.py failed"]}\n' "$DAY" "$rc" > "$OUT/drift-summary.json"
fi

# 5. zip + prune (>30 days)
$PY - "$OUT" <<'EOF' || log "WARN zip failed"
import shutil, sys, pathlib
p = pathlib.Path(sys.argv[1]); shutil.make_archive(str(p), "zip", p.parent, p.name)
EOF
CUT=$(date -d '30 days ago' +%F)
for d in results/drift-????-??-??; do
  [[ -e "$d" ]] || continue
  ds=${d#results/drift-}
  [[ "$ds" < "$CUT" ]] && { log "pruning $d"; rm -rf "$d" "$d.zip"; }
done
for z in results/drift-????-??-??.zip; do
  [[ -e "$z" ]] || continue
  ds=${z#results/drift-}; ds=${ds%.zip}
  [[ "$ds" < "$CUT" ]] && { log "pruning $z"; rm -f "$z"; }
done

log "summary: $ROOT/$OUT/drift-summary.{md,html,json}  zip: $ROOT/$OUT.zip"
exit 0
