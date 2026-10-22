# Daily ACI report: 2026-10-23

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-23 08:11:45 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 71/129 passed, 58 failed; 122 added, 57 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 38 broken, 48 warnings (9 of 22 tenants broken: DEV, Heroes, MUHC, POC-LN, SnV, T1, TN-DEDUP-LAB, hacki-tn-a, lab-t01)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant2 | NEW | 0 | 1 | 97 | WARN |
| Cursor_Tenant3 | NEW | 0 | 1 | 97 | WARN |
| Demo1 | NEW | 0 | 2 | 94 | WARN |
| DEV | NEW | 3 | 1 | 67 | BROKEN |
| hacki-tn-a | NEW | 1 | 12 | 54 | BROKEN |
| Heroes | yes | 3 | 0 | 70 | BROKEN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| LAB-InterVRF | NEW | 0 | 3 | 91 | WARN |
| LAB-MEIRLAN | NEW | 0 | 1 | 97 | WARN |
| lab-t01 | NEW | 1 | 4 | 78 | BROKEN |
| LAB_ASN_01 | NEW | 0 | 3 | 91 | WARN |
| LAB_ASN_02 | NEW | 0 | 1 | 97 | WARN |
| mgmt | yes | 0 | 2 | 94 | WARN |
| MUHC | yes | 4 | 1 | 57 | BROKEN |
| oneaciapp | yes | 0 | 3 | 91 | WARN |
| POC-LN | NEW | 10 | 2 | 0 | BROKEN |
| ROR | yes | 0 | 3 | 91 | WARN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| T1 | NEW | 2 | 2 | 74 | BROKEN |
| TN-DEDUP-LAB | yes | 10 | 4 | 0 | BROKEN |

Details: `integrity/integrity-summary.md`
