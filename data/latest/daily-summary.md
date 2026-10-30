# Daily ACI report: 2026-10-31

## DRIFT DETECTED | HEALTHY

- Generated: 2026-10-31 08:22:19 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 31/129 passed, 98 failed; 50 added, 98 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**HEALTHY - 0 broken relations, 29 warnings across 14 tenants**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| aaaaa | NEW | 0 | 1 | 97 | WARN |
| Atul_tenant | NEW | 0 | 1 | 97 | WARN |
| BCC-222 | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 2 | 94 | WARN |
| DEMO1 | NEW | 0 | 5 | 85 | WARN |
| iacdemo-contractors | NEW | 0 | 2 | 94 | WARN |
| iacdemo-prod | NEW | 0 | 4 | 88 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| MS-T | NEW | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| PY-TN | NEW | 0 | 2 | 94 | WARN |
| ROR | yes | 0 | 3 | 91 | WARN |
| Tenant_Test | NEW | 0 | 3 | 91 | WARN |

Details: `integrity/integrity-summary.md`
