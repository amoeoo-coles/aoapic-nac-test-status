# Daily ACI report: 2026-10-26

## DRIFT DETECTED | HEALTHY

- Generated: 2026-10-26 08:07:44 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 20/129 passed, 109 failed; 3 added, 109 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**HEALTHY - 0 broken relations, 8 warnings across 5 tenants**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 3 | 91 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| TF_LAB_SAMAN | NEW | 0 | 2 | 94 | WARN |

Details: `integrity/integrity-summary.md`
