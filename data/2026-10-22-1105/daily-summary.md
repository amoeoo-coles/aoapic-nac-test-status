# Daily ACI report: 2026-10-22

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-22 11:06:58 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 129/129 passed, 0 failed; 21 added, 0 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 25 broken, 39 warnings (5 of 22 tenants broken: MUHC, SnV, TN-DEDUP-LAB, UT, prod)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 0 | 0 | 100 | HEALTHY |
| infra | yes | 0 | 1 | 97 | WARN |
| js_10018 | NEW | 0 | 1 | 97 | WARN |
| js_10118 | NEW | 0 | 2 | 94 | WARN |
| mgmt | yes | 0 | 4 | 88 | WARN |
| MUHC | yes | 7 | 0 | 30 | BROKEN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| OS1 | yes | 0 | 2 | 94 | WARN |
| prod | yes | 3 | 3 | 61 | BROKEN |
| Production_Tenant | NEW | 0 | 2 | 94 | WARN |
| Production_Tenant2 | NEW | 0 | 2 | 94 | WARN |
| Production_Tenant22 | NEW | 0 | 3 | 91 | WARN |
| ROR | yes | 0 | 3 | 91 | WARN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| TEST | yes | 0 | 1 | 97 | WARN |
| TEST-ABC1 | yes | 0 | 2 | 94 | WARN |
| Test-Tenant | yes | 0 | 1 | 97 | WARN |
| TN-DEDUP-LAB | yes | 10 | 4 | 0 | BROKEN |
| tn-MGK | yes | 0 | 2 | 94 | WARN |
| tn_TEST1 | NEW | 0 | 1 | 97 | WARN |
| UT | yes | 1 | 3 | 81 | BROKEN |

Details: `integrity/integrity-summary.md`
