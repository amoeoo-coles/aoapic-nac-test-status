# Daily ACI report: 2026-11-11

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-11 08:36:13 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 254 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 24 broken, 99 warnings (11 of 37 tenants broken: Cursor_tenant1, LAB-TENANT, Production, RB-Tenant, Tenant_RG, Test100, Test_9112026, VY-TN, tenant_mylab, tn_example_tenant, zzzps4021_BGP)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| billing-test-DPYD6hPFFmE9 | NEW | 0 | 0 | 100 | HEALTHY |
| common | yes | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 1 | 3 | 81 | BROKEN |
| Cursor_Tenant2 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant3 | NEW | 0 | 1 | 97 | WARN |
| Cursor_tenant5 | NEW | 0 | 7 | 79 | WARN |
| EM-LAB | NEW | 0 | 2 | 94 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| iTenant | NEW | 0 | 1 | 97 | WARN |
| LAB-TENANT | NEW | 3 | 4 | 58 | BROKEN |
| MAD | NEW | 0 | 2 | 94 | WARN |
| mgmt | yes | 0 | 2 | 94 | WARN |
| MGMT_LAN | NEW | 0 | 1 | 97 | WARN |
| mjay_dev | NEW | 0 | 1 | 97 | WARN |
| Mouse | NEW | 0 | 1 | 97 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| Prod | NEW | 0 | 1 | 97 | WARN |
| Production | NEW | 2 | 7 | 59 | BROKEN |
| RB-Tenant | NEW | 3 | 4 | 58 | BROKEN |
| Tenant-Ahmed | NEW | 0 | 2 | 94 | WARN |
| Tenant2 | NEW | 0 | 6 | 82 | WARN |
| Tenant_RG | NEW | 2 | 4 | 68 | BROKEN |
| Test | NEW | 0 | 1 | 97 | WARN |
| Test100 | NEW | 1 | 8 | 66 | BROKEN |
| Test_9112026 | NEW | 5 | 3 | 41 | BROKEN |
| TN-CONSUMER | NEW | 0 | 0 | 100 | HEALTHY |
| TN-CONSUMER-BGS | NEW | 0 | 0 | 100 | HEALTHY |
| TN-LAB-ANS01 | NEW | 0 | 3 | 91 | WARN |
| TN-LAB-K01 | NEW | 0 | 0 | 100 | HEALTHY |
| TN-LAB-K02 | NEW | 0 | 2 | 94 | WARN |
| TN-PROVIDER | NEW | 0 | 2 | 94 | WARN |
| TN-PROVIDER-BGS | NEW | 0 | 2 | 94 | WARN |
| tn_example_tenant | NEW | 2 | 8 | 56 | BROKEN |
| VY-TN | NEW | 3 | 5 | 55 | BROKEN |
| Zangief | NEW | 0 | 1 | 97 | WARN |
| zzzps4021 | NEW | 0 | 8 | 76 | WARN |
| zzzps4021_BGP | NEW | 1 | 5 | 75 | BROKEN |

Details: `integrity/integrity-summary.md`
