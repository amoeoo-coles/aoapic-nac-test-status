# Daily ACI report: 2026-11-10

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-10 08:19:14 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 190 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 17 broken, 77 warnings (7 of 30 tenants broken: LAB-TENANT, RB-Tenant, Tenant_RG, Test100, Test_9112026, VY-TN, tenant_mylab)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| billing-test-DPYD6hPFFmE9 | NEW | 0 | 0 | 100 | HEALTHY |
| common | yes | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant2 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant3 | NEW | 0 | 1 | 97 | WARN |
| Cursor_tenant5 | NEW | 0 | 7 | 79 | WARN |
| EM-LAB | NEW | 0 | 1 | 97 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| iTenant | NEW | 0 | 1 | 97 | WARN |
| LAB-TENANT | NEW | 3 | 4 | 58 | BROKEN |
| mgmt | yes | 0 | 2 | 94 | WARN |
| MGMT_LAN | NEW | 0 | 1 | 97 | WARN |
| mjay_dev | NEW | 0 | 1 | 97 | WARN |
| NZ-ACI-LAB | NEW | 0 | 3 | 91 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| RB-Tenant | NEW | 3 | 4 | 58 | BROKEN |
| Tenant-Ahmed | NEW | 0 | 2 | 94 | WARN |
| tenant_mylab | NEW | 1 | 1 | 87 | BROKEN |
| Tenant_RG | NEW | 2 | 4 | 68 | BROKEN |
| Test100 | NEW | 1 | 8 | 66 | BROKEN |
| Test_9112026 | NEW | 5 | 3 | 41 | BROKEN |
| TESTING123 | NEW | 0 | 1 | 97 | WARN |
| TN-LAB-ANS01 | NEW | 0 | 3 | 91 | WARN |
| TN-LAB-K01 | NEW | 0 | 0 | 100 | HEALTHY |
| TN-LAB-K02 | NEW | 0 | 2 | 94 | WARN |
| tn_example_tenant | NEW | 0 | 6 | 82 | WARN |
| VY-TN | NEW | 2 | 5 | 65 | BROKEN |
| Zangief | NEW | 0 | 1 | 97 | WARN |
| zzzps4021 | NEW | 0 | 8 | 76 | WARN |
| zzzps4021_BGP | NEW | 0 | 5 | 85 | WARN |

Details: `integrity/integrity-summary.md`
