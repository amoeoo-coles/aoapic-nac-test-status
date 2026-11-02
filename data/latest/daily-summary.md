# Daily ACI report: 2026-11-03

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-03 08:23:57 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 45/129 passed, 84 failed; 46 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 5 broken, 33 warnings (2 of 11 tenants broken: SnV, TenantAPPC3750)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| Bank-Demo | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 1 | 97 | WARN |
| Heroes | yes | 0 | 4 | 88 | WARN |
| iacdemo-contractors | NEW | 0 | 2 | 94 | WARN |
| iacdemo-prod | NEW | 0 | 5 | 85 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| SIS_PROD | NEW | 0 | 6 | 82 | WARN |
| SnV | yes | 4 | 9 | 33 | BROKEN |
| TenantAPPC3750 | NEW | 1 | 2 | 84 | BROKEN |

Details: `integrity/integrity-summary.md`
