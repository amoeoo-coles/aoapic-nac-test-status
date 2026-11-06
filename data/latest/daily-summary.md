# Daily ACI report: 2026-11-07

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-07 08:20:31 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 45/129 passed, 84 failed; 55 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 8 broken, 19 warnings (4 of 12 tenants broken: MOJ_TENANT, PSCF, SnV, oneaciapp)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 0 | 0 | 100 | HEALTHY |
| iacdemo-contractors | NEW | 0 | 2 | 94 | WARN |
| iacdemo-prod | NEW | 0 | 5 | 85 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 3 | 91 | WARN |
| MOJ_TENANT | NEW | 1 | 1 | 87 | BROKEN |
| oneaciapp | yes | 2 | 3 | 71 | BROKEN |
| PSCF | NEW | 1 | 2 | 84 | BROKEN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| Tai_API_Tenant | NEW | 0 | 1 | 97 | WARN |
| Tai_Tenant | NEW | 0 | 1 | 97 | WARN |

Details: `integrity/integrity-summary.md`
