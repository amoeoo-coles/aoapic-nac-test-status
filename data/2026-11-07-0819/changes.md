# Changes since previous morning (2026-11-06-0817 -> 2026-11-07-0819)

Previous snapshot 2026-11-06 08:18:14 AEDT; current snapshot 2026-11-07 08:20:19 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 146 | 91 | -55 |
| integrity passed | 134 | 87 | -47 |
| integrity failed | 12 | 4 | -8 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 45 | +25 |
| drift failed | 109 | 84 | -25 |

Tenants: 27 -> 12; broken 7 -> 4
- added: Heroes, MOJ_TENANT, PSCF, SnV, Tai_API_Tenant, Tai_Tenant
- removed: AAL001, ASN_550, CiscoU-Tenant-03, CiscoU-Tenant-04, Demo1, dev-demo, global-NBK-Tenant, iTenant, juan, L3TenantL, MOJ_TENANAT, My-Tenant, NP-DEMO, SCADAAA, T1_VMM, task_ansible_aci_6th, TeamTest-Bakker, TECCRT-3778-01, TECCRT-3778-02, test, TF_LAB_SAMAN
- newly broken: MOJ_TENANT (new), PSCF (new), SnV (new)
- fixed: mgmt

Broken relations: 12 -> 8
- ADDED MOJ_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 102 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either 
- ADDED PSCF | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message: 
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- ADDED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message: 
- ADDED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message: 
- RESOLVED ASN_550 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-211 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: E
- RESOLVED My-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-10 :There is no domain, associated with both EPG and Port, that has required VLAN;
- RESOLVED TEST_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1` | Configuration failed for uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1 due to VRF Not Present, debug message: 
- RESOLVED iTenant | Contract without subjects | `uni/tn-iTenant/brc-contract_webserver-to-database` | Contract has no subject, so it permits nothing.
- RESOLVED mgmt | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-mgmt/out-inb_L3Out` | Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED mgmt | Subject without filters | `uni/tn-mgmt/brc-MOJ_CT_AP_vC/subj-MOJ_SUBJ_AP_vC` | Contract subject has no filter, so it permits nothing.
- RESOLVED oneaciapp | Contract without subjects | `uni/tn-oneaciapp/brc-ESG` | Contract has no subject, so it permits nothing.
- RESOLVED oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-APP` | EPG consumes contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target).
- RESOLVED oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` | EPG provides contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target).
- RESOLVED oneaciapp | External EPG contract missing-target | `uni/tn-oneaciapp/out-L3out/instP-externalepg-3` | External EPG uses contract 'APP-To-DB' which does not exist.
- RESOLVED task_ansible_aci_6th | BD VRF missing-target | `uni/tn-task_ansible_aci_6th/BD-BD_TEST` | BD points to VRF 'VRF_BLUE' which does not exist in tenant task_ansible_aci_6th or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- RESOLVED test | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-test/ap-test/epg-test` | Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan-10) is already in use by My-Tenant:My-APP-Profile:My-DB-EPG;invalid-path: Either the EpG/L3Out is not associated

New critical faults:
- F0467 MOJ_TENANT `uni/tn-MOJ_TENANT/out-MOJ_L3out`: Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 101 MOJ_VPC_FW2 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 PSCF `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING`: Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message: 
- F0467 SnV `uni/tn-SnV/ap-Chaos/epg-Web`: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Evolution_X/epg-Web`: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Power_Up/epg-Web`: Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 SnV `uni/tn-SnV/ap-Rescue/epg-Web`: Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B;
- F0467 oneaciapp `uni/tn-oneaciapp/ap-TEST/epg-TEST1`: Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message: 
- F0467 oneaciapp `uni/tn-oneaciapp/ap-TEST/epg-TEST2`: Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message: 

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 27 | 12 | -15 | 6 | 10 |
| VRF | 18 | 28 | 14 | -14 | 6 | 10 |
| BD | 23 | 36 | 15 | -21 | 9 | 17 |
| Subnet (BD) | 23 | 34 | 13 | -21 | 9 | 19 |
| AP | 16 | 25 | 16 | -9 | 8 | 8 |
| EPG | 33 | 37 | 30 | -7 | 17 | 20 |
