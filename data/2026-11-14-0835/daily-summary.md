# Daily ACI report: 2026-11-14

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-14 08:35:34 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 56/129 passed, 73 failed; 0 added, 73 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 12 broken, 7 warnings (2 of 7 tenants broken: Heroes, SnV)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 4 | 0 | 60 | BROKEN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| ROR | yes | 0 | 3 | 91 | WARN |
| SnV | yes | 8 | 1 | 17 | BROKEN |

Details: `integrity/integrity-summary.md`
