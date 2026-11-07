# Changes since previous morning (2026-11-07-0819 -> 2026-11-08-0817)

Previous snapshot 2026-11-07 08:20:19 AEDT; current snapshot 2026-11-08 08:18:00 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 91 | 43 | -48 |
| integrity passed | 87 | 38 | -49 |
| integrity failed | 4 | 5 | +1 |
| drift total | 129 | 129 | +0 |
| drift passed | 45 | 20 | -25 |
| drift failed | 84 | 109 | +25 |

Tenants: 12 -> 9; broken 4 -> 3
- added: LAB-TENANT, RB-Tenant, tenant_mylab, Tenant_RG, VY-TN
- removed: Heroes, iacdemo-contractors, iacdemo-prod, MOJ_TENANT, PSCF, SnV, Tai_API_Tenant, Tai_Tenant
- newly broken: RB-Tenant (new), Tenant_RG (new), VY-TN (new)
- fixed: oneaciapp

Broken relations: 8 -> 6
- ADDED RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-FTP` | Contract has no subject, so it permits nothing.
- ADDED RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-HTTPS` | Contract has no subject, so it permits nothing.
- ADDED RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message: 
- ADDED Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-1410 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-pat
- ADDED Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED MOJ_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 102 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either 
- RESOLVED PSCF | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message: 
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- RESOLVED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message: 
- RESOLVED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message: 

New critical faults:
- F0467 RB-Tenant `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG`: Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message: 
- F0467 Tenant_RG `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2`: Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-1410 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Tenant_RG `uni/tn-Tenant_RG/out-rg_l3_out_ext`: Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 VY-TN `uni/tn-VY-TN/out-test-L3OUT`: Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 12 | 9 | -3 | 5 | 12 |
| VRF | 18 | 14 | 11 | -3 | 5 | 12 |
| BD | 23 | 15 | 9 | -6 | 5 | 19 |
| Subnet (BD) | 23 | 13 | 3 | -10 | 2 | 22 |
| AP | 16 | 16 | 8 | -8 | 5 | 13 |
| EPG | 33 | 30 | 8 | -22 | 6 | 31 |
