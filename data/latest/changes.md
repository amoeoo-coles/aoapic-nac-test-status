# Changes since previous morning (2026-11-04-0819 -> 2026-11-06-0817)

Previous snapshot 2026-11-04 08:19:50 AEDT; current snapshot 2026-11-06 08:18:14 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 55 | 146 | +91 |
| integrity passed | 53 | 134 | +81 |
| integrity failed | 2 | 12 | +10 |
| drift total | 129 | 129 | +0 |
| drift passed | 45 | 20 | -25 |
| drift failed | 84 | 109 | +25 |

Tenants: 8 -> 27; broken 2 -> 7
- added: AAL001, ASN_550, CiscoU-Tenant-03, CiscoU-Tenant-04, Demo1, global-NBK-Tenant, iacdemo-contractors, iacdemo-prod, iTenant, juan, L3TenantL, MOJ_TENANAT, My-Tenant, NP-DEMO, SCADAAA, T1_VMM, task_ansible_aci_6th, TeamTest-Bakker, TECCRT-3778-01, TECCRT-3778-02, test, TF_LAB_SAMAN
- removed: Heroes, SnV, TENANT-LAB
- newly broken: mgmt, oneaciapp, ASN_550 (new), iTenant (new), My-Tenant (new), task_ansible_aci_6th (new), test (new)
- fixed: none

Broken relations: 12 -> 12
- ADDED ASN_550 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-211 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: E
- ADDED My-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-10 :There is no domain, associated with both EPG and Port, that has required VLAN;
- ADDED TEST_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1` | Configuration failed for uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1 due to VRF Not Present, debug message: 
- ADDED iTenant | Contract without subjects | `uni/tn-iTenant/brc-contract_webserver-to-database` | Contract has no subject, so it permits nothing.
- ADDED mgmt | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-mgmt/out-inb_L3Out` | Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED mgmt | Subject without filters | `uni/tn-mgmt/brc-MOJ_CT_AP_vC/subj-MOJ_SUBJ_AP_vC` | Contract subject has no filter, so it permits nothing.
- ADDED oneaciapp | Contract without subjects | `uni/tn-oneaciapp/brc-ESG` | Contract has no subject, so it permits nothing.
- ADDED oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-APP` | EPG consumes contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target).
- ADDED oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` | EPG provides contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target).
- ADDED oneaciapp | External EPG contract missing-target | `uni/tn-oneaciapp/out-L3out/instP-externalepg-3` | External EPG uses contract 'APP-To-DB' which does not exist.
- ADDED task_ansible_aci_6th | BD VRF missing-target | `uni/tn-task_ansible_aci_6th/BD-BD_TEST` | BD points to VRF 'VRF_BLUE' which does not exist in tenant task_ansible_aci_6th or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- ADDED test | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-test/ap-test/epg-test` | Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan-10) is already in use by My-Tenant:My-APP-Profile:My-DB-EPG;invalid-path: Either the EpG/L3Out is not associated
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 102 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;

New critical faults:
- F0467 ASN_550 `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG`: Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 My-Tenant `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG`: Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-10 :There is no domain, associated with both EPG and Port, that has required VLAN;
- F0467 TEST_TENANT `uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1`: Configuration failed for uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1 due to VRF Not Present, debug message: 
- F0467 mgmt `uni/tn-mgmt/out-inb_L3Out`: Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 test `uni/tn-test/ap-test/epg-test`: Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan-10) is already in use by My-Tenant:My-APP-Profile:My-DB-EPG;invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 8 | 27 | +19 | 23 | 12 |
| VRF | 18 | 10 | 28 | +18 | 22 | 12 |
| BD | 23 | 9 | 36 | +27 | 32 | 19 |
| Subnet (BD) | 23 | 7 | 34 | +27 | 33 | 22 |
| AP | 16 | 8 | 25 | +17 | 22 | 13 |
| EPG | 33 | 13 | 37 | +24 | 35 | 31 |
