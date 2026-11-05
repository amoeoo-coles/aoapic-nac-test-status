# Daily ACI report: 2026-11-06

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-06 08:18:35 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 167 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 12 broken, 68 warnings (8 of 27 tenants broken: ASN_550, My-Tenant, TEST_TENANT, iTenant, mgmt, oneaciapp, task_ansible_aci_6th, test)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| AAL001 | NEW | 0 | 2 | 94 | WARN |
| ASN_550 | NEW | 1 | 1 | 87 | BROKEN |
| CiscoU-Tenant-03 | NEW | 0 | 1 | 97 | WARN |
| CiscoU-Tenant-04 | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 10 | 70 | WARN |
| Demo1 | NEW | 0 | 3 | 91 | WARN |
| dev-demo | NEW | 0 | 0 | 100 | HEALTHY |
| global-NBK-Tenant | NEW | 0 | 2 | 94 | WARN |
| iacdemo-contractors | NEW | 0 | 2 | 94 | WARN |
| iacdemo-prod | NEW | 0 | 5 | 85 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| iTenant | NEW | 1 | 4 | 78 | BROKEN |
| juan | NEW | 0 | 1 | 97 | WARN |
| L3TenantL | NEW | 0 | 1 | 97 | WARN |
| mgmt | yes | 2 | 3 | 71 | BROKEN |
| MOJ_TENANAT | NEW | 0 | 0 | 100 | HEALTHY |
| My-Tenant | NEW | 1 | 4 | 78 | BROKEN |
| NP-DEMO | NEW | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 4 | 4 | 48 | BROKEN |
| SCADAAA | NEW | 0 | 1 | 97 | WARN |
| T1_VMM | NEW | 0 | 2 | 94 | WARN |
| task_ansible_aci_6th | NEW | 1 | 2 | 84 | BROKEN |
| TeamTest-Bakker | NEW | 0 | 2 | 94 | WARN |
| TECCRT-3778-01 | NEW | 0 | 8 | 76 | WARN |
| TECCRT-3778-02 | NEW | 0 | 4 | 88 | WARN |
| test | NEW | 1 | 1 | 87 | BROKEN |
| TF_LAB_SAMAN | NEW | 0 | 2 | 94 | WARN |

Details: `integrity/integrity-summary.md`
