# Changes since previous morning (2026-11-08-0817 -> 2026-11-09-0824)

Previous snapshot 2026-11-08 08:18:00 AEDT; current snapshot 2026-11-09 08:25:12 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 43 | 82 | +39 |
| integrity passed | 38 | 76 | +38 |
| integrity failed | 5 | 6 | +1 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 20 | +0 |
| drift failed | 109 | 109 | +0 |

Tenants: 9 -> 14; broken 3 -> 4
- added: CORP_PROD, Cursor_tenant1, Cursor_Tenant2, Cursor_Tenant3, Cursor_tenant5
- removed: none
- newly broken: LAB-TENANT
- fixed: none

Broken relations: 6 -> 8
- ADDED LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message: 
- ADDED VY-TN | Major fault F0565 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | Deployment of EPG uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02 failed on domain test-vmm due to No valid encapsulation identifier allocated for the epg
- STILL BROKEN, reason changed: Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2`

New critical faults:
- F0467 LAB-TENANT `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG`: Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message: 

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 9 | 14 | +5 | 10 | 12 |
| VRF | 18 | 11 | 18 | +7 | 12 | 12 |
| BD | 23 | 9 | 22 | +13 | 18 | 19 |
| Subnet (BD) | 23 | 3 | 13 | +10 | 12 | 22 |
| AP | 16 | 8 | 14 | +6 | 11 | 13 |
| EPG | 33 | 8 | 24 | +16 | 22 | 31 |
