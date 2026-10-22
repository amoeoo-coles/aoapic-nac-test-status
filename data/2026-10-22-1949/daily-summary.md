# Daily ACI report: 2026-10-22

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-22 19:51:30 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 123/129 passed, 6 failed; 70 added, 6 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 28 broken, 50 warnings (7 of 28 tenants broken: Heroes, MUHC, SnV, TN-DEDUP-LAB, UT, lab-t01, prod)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant2 | NEW | 0 | 1 | 97 | WARN |
| DEMO1 | NEW | 0 | 1 | 97 | WARN |
| Heroes | yes | 2 | 2 | 74 | BROKEN |
| infra | yes | 0 | 1 | 97 | WARN |
| KoolKid_Tenant | NEW | 0 | 2 | 94 | WARN |
| lab-t01 | NEW | 1 | 3 | 81 | BROKEN |
| mgmt | yes | 0 | 4 | 88 | WARN |
| MUHC | yes | 7 | 0 | 30 | BROKEN |
| NE-LAB-1021 | NEW | 0 | 1 | 97 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| OS1 | yes | 0 | 2 | 94 | WARN |
| prod | yes | 3 | 3 | 61 | BROKEN |
| Production_Tenant | NEW | 0 | 2 | 94 | WARN |
| Production_Tenant2 | NEW | 0 | 2 | 94 | WARN |
| Production_Tenant22 | NEW | 0 | 3 | 91 | WARN |
| ROR | yes | 0 | 3 | 91 | WARN |
| Shaver_API | NEW | 0 | 1 | 97 | WARN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| TEST | yes | 0 | 1 | 97 | WARN |
| Test-Tenant | yes | 0 | 1 | 97 | WARN |
| TN-DEDUP-LAB | yes | 10 | 5 | 0 | BROKEN |
| tn-MGK | yes | 0 | 2 | 94 | WARN |
| tn_TEST1 | NEW | 0 | 1 | 97 | WARN |
| UT | yes | 1 | 3 | 81 | BROKEN |
| WebServer-Demo | NEW | 0 | 1 | 97 | WARN |
| Yellow_Tenant | NEW | 0 | 2 | 94 | WARN |

Details: `integrity/integrity-summary.md`
