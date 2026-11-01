# Daily ACI report: 2026-11-02

## DRIFT DETECTED | BROKEN RELATIONS FOUND

- Generated: 2026-11-02 08:17:11 AEDT
- Overall status: `attention`

## 1. Drift (baseline vs live)

**DRIFT DETECTED - tests 45/129 passed, 84 failed; 68 added, 84 removed**

Details: `drift/drift-summary.md`

## 2. Tenant logical integrity (tenant -> VRF -> BD -> EPG -> contract)

**BROKEN RELATIONS FOUND - 8 broken, 43 warnings (5 of 16 tenants broken: Graph, Heroes, SnV, daa, oneaciapp)**

| Tenant | Baseline | Broken | Warn | Score | Status |
|---|---|---:|---:|---:|---|
| Ansible-PROD | NEW | 0 | 4 | 88 | WARN |
| Ansible-QA | NEW | 0 | 10 | 70 | WARN |
| BCC-222 | NEW | 0 | 1 | 97 | WARN |
| common | yes | 0 | 0 | 100 | HEALTHY |
| daa | NEW | 1 | 1 | 87 | BROKEN |
| DEMO1 | NEW | 0 | 8 | 76 | WARN |
| Graph | NEW | 1 | 4 | 78 | BROKEN |
| Heroes | yes | 1 | 0 | 90 | BROKEN |
| iacdemo-contractors | NEW | 0 | 2 | 94 | WARN |
| iacdemo-prod | NEW | 0 | 3 | 91 | WARN |
| infra | yes | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 0 | 2 | 94 | WARN |
| oneaciapp | yes | 1 | 0 | 90 | BROKEN |
| SnV | yes | 4 | 1 | 57 | BROKEN |
| TENANT_MYTEST | NEW | 0 | 6 | 82 | WARN |
| TEST-POM | NEW | 0 | 1 | 97 | WARN |

Details: `integrity/integrity-summary.md`
