#!/usr/bin/env bash
# Run nac-test against an APIC (default: DevNet Always-On ACI sandbox). Read-only: aaaLogin POST + GETs.
# Usage: ./run.sh [--refresh-data]     (reads .env if present)
set -euo pipefail
cd "$(dirname "$0")"
[[ -f .env ]] && { set -a; source .env; set +a; }
: "${ACI_URL:?set ACI_URL (see .env.example)}"
: "${ACI_USERNAME:?set ACI_USERNAME}"
: "${ACI_PASSWORD:?set ACI_PASSWORD}"
PY=.venv/bin/python
[[ "${1:-}" == "--refresh-data" ]] && $PY scripts/build_data.py
rm -rf results
rc=0; .venv/bin/nac-test -d data/ -d defaults/ -t templates/ -o results/ -e integrity || rc=$?
rm -f nac-test-results.zip
$PY -c "import shutil; shutil.make_archive('nac-test-results','zip','.','results')"
exit $rc
