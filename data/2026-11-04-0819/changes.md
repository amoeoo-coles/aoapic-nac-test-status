# Changes since previous morning (2026-11-03-0822 -> 2026-11-04-0819)

Previous snapshot 2026-11-03 08:23:32 AEDT; current snapshot 2026-11-04 08:19:50 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 87 | 55 | -32 |
| integrity passed | 85 | 53 | -32 |
| integrity failed | 2 | 2 | +0 |
| drift total | 129 | 129 | +0 |
| drift passed | 45 | 45 | +0 |
| drift failed | 84 | 84 | +0 |

Tenants: 11 -> 8; broken 2 -> 2
- added: dev-demo, TENANT-LAB
- removed: Bank-Demo, iacdemo-contractors, iacdemo-prod, SIS_PROD, TenantAPPC3750
- newly broken: Heroes
- fixed: none

Broken relations: 5 -> 12
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 102 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED TenantAPPC3750 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not have
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web`

New critical faults:
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-app`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-db`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-web`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/out-Heroes_external_corporate`: Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 101 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 SnV `uni/tn-SnV/ap-Chaos/epg-Database`: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Evolution_X/epg-Database`: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Power_Up/epg-Database`: Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Rescue/epg-Database`: Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 11 | 8 | -3 | 2 | 10 |
| VRF | 18 | 13 | 10 | -3 | 2 | 10 |
| BD | 23 | 16 | 9 | -7 | 3 | 17 |
| Subnet (BD) | 23 | 12 | 7 | -5 | 3 | 19 |
| AP | 16 | 13 | 8 | -5 | 0 | 8 |
| EPG | 33 | 26 | 13 | -13 | 0 | 20 |
