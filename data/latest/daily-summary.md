# Daily ACI report: 2026-11-18

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-18 07:27:09 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 42/129 passed, 87 failed; 147 added, 82 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 18 broken, 75 warnings (7 of 35 tenants broken: PROD, Pune-Tenants, RB-Tenant, SnV, User-Applications, XYZ, test-tenant)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| aci_p03_tenant | NEW | 0 | 1 | 97 | WARN |
| aci_p03_vrf | NEW | 0 | 1 | 97 | WARN |
| charlie_terraform | NEW | 0 | 1 | 97 | WARN |
| Charlie_Test_Dev | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 3 | 91 | WARN |
| DEV | NEW | 0 | 4 | 88 | WARN |
| DevNetAcademy | NEW | 0 | 5 | 85 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| Jacob | NEW | 0 | 1 | 97 | WARN |
| Koushik | NEW | 0 | 1 | 97 | WARN |
| KoushikM | NEW | 0 | 1 | 97 | WARN |
| l3out-bfd | NEW | 0 | 1 | 97 | WARN |
| Lab1-TN | NEW | 0 | 2 | 94 | WARN |
| LAB_KK | NEW | 0 | 2 | 94 | WARN |
| Lab_Tenant_SAMBI_MTL | NEW | 0 | 1 | 97 | WARN |
| mgmt | yes | 0 | 3 | 91 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| PRD | NEW | 0 | 8 | 76 | WARN |
| PROD | NEW | 2 | 5 | 65 | BROKEN |
| Pruebas | NEW | 0 | 1 | 97 | WARN |
| Pune-Tenants | NEW | 1 | 1 | 87 | BROKEN |
| RB-Tenant | NEW | 1 | 2 | 84 | BROKEN |
| ROR | yes | 0 | 3 | 91 | WARN |
| SCADA | NEW | 0 | 3 | 91 | WARN |
| Sistemas | NEW | 0 | 1 | 97 | WARN |
| SnV | yes | 8 | 1 | 17 | BROKEN |
| Suresh_Tenant | NEW | 0 | 3 | 91 | WARN |
| Tenant_DEVOPS | NEW | 0 | 1 | 97 | WARN |
| TENANT_PROD | NEW | 0 | 3 | 91 | WARN |
| TenantPython | NEW | 0 | 1 | 97 | WARN |
| TenantPython2 | NEW | 0 | 1 | 97 | WARN |
| test | NEW | 0 | 3 | 91 | WARN |
| test-tenant | NEW | 3 | 4 | 58 | BROKEN |
| User-Applications | NEW | 2 | 1 | 77 | BROKEN |
| XYZ | NEW | 1 | 3 | 81 | BROKEN |

Details: `integrity/integrity-summary.md`
