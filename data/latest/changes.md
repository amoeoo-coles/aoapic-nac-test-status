# Changes since previous morning (2026-10-31-0821 -> 2026-11-01-0821)

Previous snapshot 2026-10-31 08:22:07 AEDT; current snapshot 2026-11-01 08:21:24 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 66 | 61 | -5 |
| integrity passed | 66 | 60 | -6 |
| integrity failed | 0 | 1 | +1 |
| drift total | 129 | 129 | +0 |
| drift passed | 31 | 45 | +14 |
| drift failed | 98 | 84 | -14 |

Tenants: 14 -> 10; broken 0 -> 1
- added: Ansible-PROD, Ansible-QA, daa, Heroes, SnV, TENANT_MYTEST
- removed: aaaaa, Atul_tenant, BCC-222, DEMO1, iacdemo-contractors, iacdemo-prod, MS-T, PY-TN, ROR, Tenant_Test
- newly broken: SnV (new)
- fixed: none

Broken relations: 0 -> 4
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;

New critical faults:
- F0467 SnV `uni/tn-SnV/ap-Chaos/epg-Web`: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Evolution_X/epg-Web`: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Power_Up/epg-Web`: Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Rescue/epg-Web`: Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 14 | 10 | -4 | 4 | 10 |
| VRF | 18 | 13 | 8 | -5 | 0 | 10 |
| BD | 23 | 15 | 6 | -9 | 0 | 17 |
| Subnet (BD) | 23 | 11 | 4 | -7 | 0 | 19 |
| AP | 16 | 11 | 12 | +1 | 4 | 8 |
| EPG | 33 | 17 | 20 | +3 | 7 | 20 |
