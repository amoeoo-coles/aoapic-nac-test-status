# Daily ACI report: 2026-11-09

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-09 08:25:34 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 85 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 8 broken, 40 warnings (4 of 14 tenants broken: LAB-TENANT, RB-Tenant, Tenant_RG, VY-TN)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| CORP_PROD | NEW | 0 | 10 | 70 | WARN |
| Cursor_tenant1 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant2 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant3 | NEW | 0 | 1 | 97 | WARN |
| Cursor_tenant5 | NEW | 0 | 7 | 79 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| LAB-TENANT | NEW | 1 | 4 | 78 | BROKEN |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| RB-Tenant | NEW | 3 | 3 | 61 | BROKEN |
| tenant_mylab | NEW | 0 | 1 | 97 | WARN |
| Tenant_RG | NEW | 2 | 4 | 68 | BROKEN |
| VY-TN | NEW | 2 | 5 | 65 | BROKEN |

Details: `integrity/integrity-summary.md`
