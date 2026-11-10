# Changes since previous morning (2026-11-10-0818 -> 2026-11-11-0835)

Previous snapshot 2026-11-10 08:19:02 AEDT; current snapshot 2026-11-11 08:35:58 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 200 | 253 | +53 |
| integrity passed | 188 | 236 | +48 |
| integrity failed | 12 | 17 | +5 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 20 | +0 |
| drift failed | 109 | 109 | +0 |

Tenants: 30 -> 37; broken 7 -> 10
- added: MAD, Mouse, Prod, Production, Tenant2, Test, TN-CONSUMER, TN-CONSUMER-BGS, TN-PROVIDER, TN-PROVIDER-BGS
- removed: NZ-ACI-LAB, tenant_mylab, TESTING123
- newly broken: Cursor_tenant1, tn_example_tenant, zzzps4021_BGP, Production (new)
- fixed: none

Broken relations: 17 -> 24
- ADDED Cursor_tenant1 | BD VRF missing-target | `uni/tn-Cursor_tenant1/BD-p2bd` | BD points to VRF 'p2v' which does not exist in tenant Cursor_tenant1 or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- ADDED Production | Contract without subjects | `uni/tn-Production/brc-BD-APP` | Contract has no subject, so it permits nothing.
- ADDED Production | Contract without subjects | `uni/tn-Production/brc-BD-DB` | Contract has no subject, so it permits nothing.
- ADDED VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG` | Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-333 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned t
- ADDED tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_20 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-111 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- ADDED zzzps4021_BGP | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-zzzps4021_BGP/out-test-L3OUT` | Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- STILL BROKEN, reason changed: Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2`

New critical faults:
- F0467 VY-TN `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG`: Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 tn_example_tenant `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG`: Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/6 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-333 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 tn_example_tenant `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG`: Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_19 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-222 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- F0467 zzzps4021_BGP `uni/tn-zzzps4021_BGP/out-test-L3OUT`: Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 30 | 37 | +7 | 33 | 12 |
| VRF | 18 | 33 | 40 | +7 | 34 | 12 |
| BD | 23 | 46 | 59 | +13 | 55 | 19 |
| Subnet (BD) | 23 | 36 | 46 | +10 | 45 | 22 |
| AP | 16 | 25 | 38 | +13 | 35 | 13 |
| EPG | 33 | 40 | 54 | +14 | 52 | 31 |
