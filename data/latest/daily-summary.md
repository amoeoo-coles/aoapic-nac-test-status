# Daily ACI report: 2026-11-01

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-01 08:21:37 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 45/129 passed, 84 failed; 15 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 4 broken, 20 warnings (1 of 10 tenants broken: SnV)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| Ansible-PROD | NEW | 0 | 4 | 88 | WARN |
| Ansible-QA | NEW | 0 | 10 | 70 | WARN |
| common | yes | 0 | 0 | 100 | HEALTHY |
| daa | NEW | 0 | 1 | 97 | WARN |
| Heroes | yes | 0 | 0 | 100 | HEALTHY |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 0 | 1 | 97 | WARN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| TENANT_MYTEST | NEW | 0 | 1 | 97 | WARN |

Details: `integrity/integrity-summary.md`
