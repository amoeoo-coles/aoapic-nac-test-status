# Daily ACI report: 2026-10-27

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-10-27 08:16:53 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 44/129 passed, 85 failed; 50 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 10 broken, 35 warnings (2 of 11 tenants broken: Pune-Lab, TN-DEDUP-LAB)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 6 | 82 | WARN |
| DEMO | NEW | 0 | 2 | 94 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 3 | 91 | WARN |
| oneaciapp | yes | 0 | 3 | 91 | WARN |
| Pune-Lab | NEW | 1 | 2 | 84 | BROKEN |
| ROR | yes | 0 | 3 | 91 | WARN |
| TF_LAB_SAMAN | NEW | 0 | 1 | 97 | WARN |
| TN-DEDUP-LAB | yes | 9 | 5 | 0 | BROKEN |
| TN-POC-LN | NEW | 0 | 10 | 70 | WARN |
| TN-PROD | NEW | 0 | 0 | 100 | HEALTHY |

Details: `integrity/integrity-summary.md`
