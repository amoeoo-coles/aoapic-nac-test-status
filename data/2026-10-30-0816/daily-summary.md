# Daily ACI report: 2026-10-30

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-30 08:16:55 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 35/129 passed, 94 failed; 67 added, 93 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 31 broken, 44 warnings (8 of 17 tenants broken: ASN-02, MUHC, T1_FIRST, TN-AUTO, TN-DEDUP-LAB, TN_PROD, Test101, mgmt)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| ASN-02 | NEW | 1 | 3 | 81 | BROKEN |
| ASN_01 | NEW | 0 | 3 | 91 | WARN |
| Automation-Test | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 6 | 82 | WARN |
| ddso | NEW | 0 | 2 | 94 | WARN |
| gtest | NEW | 0 | 11 | 67 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| Irelia-TEST | NEW | 0 | 1 | 97 | WARN |
| mgmt | yes | 1 | 3 | 81 | BROKEN |
| MUHC | yes | 8 | 0 | 20 | BROKEN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| T1_FIRST | NEW | 1 | 0 | 90 | BROKEN |
| Test101 | NEW | 8 | 2 | 14 | BROKEN |
| TestTenant | NEW | 0 | 1 | 97 | WARN |
| TN-AUTO | NEW | 2 | 4 | 68 | BROKEN |
| TN-DEDUP-LAB | yes | 9 | 5 | 0 | BROKEN |
| TN_PROD | NEW | 1 | 1 | 87 | BROKEN |

Details: `integrity/integrity-summary.md`
