# Changes since previous morning (2026-10-22-1105 -> 2026-10-22-1949)

Previous snapshot 2026-10-22 11:05:56 AEDT; current snapshot 2026-10-22 19:50:23 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 168 | 196 | +28 |
| integrity passed | 160 | 186 | +26 |
| integrity failed | 8 | 10 | +2 |
| drift total | 129 | 129 | +0 |
| drift passed | 129 | 123 | -6 |
| drift failed | 0 | 6 | +6 |

Tenants: 22 -> 28; broken 5 -> 7
- added: Cursor_tenant1, Cursor_Tenant2, DEMO1, KoolKid_Tenant, lab-t01, NE-LAB-1021, Shaver_API, WebServer-Demo, Yellow_Tenant
- removed: js_10018, js_10118, TEST-ABC1
- newly broken: Heroes, lab-t01 (new)
- fixed: none

Broken relations: 25 -> 28
- ADDED Heroes | External EPG contract missing-target | `uni/tn-Heroes/out-Heroes_external_corporate/instP-Heroes_default` | External EPG uses contract 'web' which does not exist.
- ADDED Heroes | External EPG contract missing-target | `uni/tn-Heroes/out-Heroes_external_corporate/instP-Heroes_default` | External EPG uses contract 'power_up' which does not exist.
- ADDED lab-t01 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-lab-t01/out-out-fw` | Configuration failed for uni/tn-lab-t01/out-out-fw node 101 eth1/33 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- STILL BROKEN, reason changed: UT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-UT/ap-UAP/epg-USER_EPG`

New critical faults:
- F0467 lab-t01 `uni/tn-lab-t01/out-out-fw`: Configuration failed for uni/tn-lab-t01/out-out-fw node 101 eth1/33 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 22 | 28 | +6 | 13 | 1 |
| VRF | 18 | 22 | 28 | +6 | 11 | 1 |
| BD | 23 | 27 | 34 | +7 | 13 | 2 |
| Subnet (BD) | 23 | 23 | 29 | +6 | 8 | 2 |
| AP | 16 | 19 | 27 | +8 | 11 | 0 |
| EPG | 33 | 37 | 47 | +10 | 14 | 0 |
