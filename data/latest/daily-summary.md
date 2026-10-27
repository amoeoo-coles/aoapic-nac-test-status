# Daily ACI report: 2026-10-28

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-28 08:22:42 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 48/129 passed, 81 failed; 3289 added, 80 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 49 broken, 1104 warnings (9 of 22 tenants broken: ACME, Learning, MUHC, Pune-Lab, TN-DEDUP-LAB, TN-POC-LN, Test, mgmt, oneaciapp)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| ACME | NEW | 2 | 3 | 71 | BROKEN |
| common | yes | 0 | 3 | 91 | WARN |
| DC_Test | NEW | 0 | 1 | 97 | WARN |
| DEV | NEW | 0 | 1 | 97 | WARN |
| hacki-tenant-t | NEW | 0 | 0 | 100 | HEALTHY |
| hacki-tn-a | NEW | 0 | 7 | 79 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| LAB | NEW | 0 | 2 | 94 | WARN |
| Learning | NEW | 1 | 4 | 78 | BROKEN |
| mgmt | yes | 1 | 3 | 81 | BROKEN |
| MUHC | yes | 13 | 0 | 0 | BROKEN |
| oneaciapp | yes | 1 | 7 | 69 | BROKEN |
| PROVA1 | NEW | 0 | 2 | 94 | WARN |
| Pune-Lab | NEW | 2 | 1 | 77 | BROKEN |
| ROR | yes | 0 | 3 | 91 | WARN |
| T1 | NEW | 0 | 1050 | 0 | WARN |
| Test | NEW | 10 | 2 | 0 | BROKEN |
| TN-DEDUP-LAB | yes | 9 | 6 | 0 | BROKEN |
| tn-DEMO-CRM-DEV | NEW | 0 | 0 | 100 | HEALTHY |
| TN-POC-LN | NEW | 10 | 3 | 0 | BROKEN |
| tn-PORTAIL-DEV | NEW | 0 | 0 | 100 | HEALTHY |
| tn_BFT | NEW | 0 | 6 | 82 | WARN |

Details: `integrity/integrity-summary.md`
