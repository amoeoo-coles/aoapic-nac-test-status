# Daily ACI report: 2026-11-04

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-04 08:20:12 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 45/129 passed, 84 failed; 10 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 12 broken, 9 warnings (2 of 8 tenants broken: Heroes, SnV)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| common | yes | 0 | 0 | 100 | HEALTHY |
| dev-demo | NEW | 0 | 2 | 94 | WARN |
| Heroes | yes | 4 | 0 | 60 | BROKEN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 3 | 91 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| SnV | yes | 8 | 1 | 17 | BROKEN |
| TENANT-LAB | NEW | 0 | 2 | 94 | WARN |

Details: `integrity/integrity-summary.md`
