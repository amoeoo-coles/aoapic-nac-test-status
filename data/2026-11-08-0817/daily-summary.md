# Daily ACI report: 2026-11-08

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-08 08:18:06 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 28 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 6 broken, 16 warnings (3 of 9 tenants broken: RB-Tenant, Tenant_RG, VY-TN)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| LAB-TENANT | NEW | 0 | 4 | 88 | WARN |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| RB-Tenant | NEW | 3 | 3 | 61 | BROKEN |
| tenant_mylab | NEW | 0 | 1 | 97 | WARN |
| Tenant_RG | NEW | 2 | 4 | 68 | BROKEN |
| VY-TN | NEW | 1 | 1 | 87 | BROKEN |

Details: `integrity/integrity-summary.md`
