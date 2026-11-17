# Changes since previous morning (2026-11-14-0835 -> 2026-11-18-0725)

Previous snapshot 2026-11-14 08:35:26 AEDT; current snapshot 2026-11-18 07:26:22 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 57 | 173 | +116 |
| integrity passed | 55 | 164 | +109 |
| integrity failed | 2 | 9 | +7 |
| drift total | 129 | 129 | +0 |
| drift passed | 56 | 42 | -14 |
| drift failed | 73 | 87 | +14 |

Tenants: 7 -> 35; broken 2 -> 7
- added: aci_p03_tenant, aci_p03_vrf, charlie_terraform, Charlie_Test_Dev, DEV, DevNetAcademy, Jacob, Koushik, KoushikM, l3out-bfd, Lab1-TN, LAB_KK, Lab_Tenant_SAMBI_MTL, PRD, PROD, Pruebas, Pune-Tenants, RB-Tenant, SCADA, Sistemas, Suresh_Tenant, Tenant_DEVOPS, TENANT_PROD, TenantPython, TenantPython2, test, test-tenant, User-Applications, XYZ
- removed: Heroes
- newly broken: PROD (new), Pune-Tenants (new), RB-Tenant (new), test-tenant (new), User-Applications (new), XYZ (new)
- fixed: none

Broken relations: 12 -> 18
- ADDED PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: vlan-801 :There is no domain, associated with both EPG and Port, that has required VLAN;
- ADDED PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: vlan-800 :There is no domain, associated with both EPG and Port, that has required VLAN;
- ADDED Pune-Tenants | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG` | Configuration failed for uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG node 101 eth1/26 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/out-RB-L3-Out` | Configuration failed for uni/tn-RB-Tenant/out-RB-L3-Out node 102 eth1/48 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED User-Applications | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox` | Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 102 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED User-Applications | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier` | Configuration failed for uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier node 102 eth1/8 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED XYZ | EPG domain missing-target | `uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ` | Domain uni/vmmp-VMware/dom-CCIE-XYZ does not exist (state missing-target).
- ADDED test-tenant | Contract without subjects | `uni/tn-test-tenant/brc-consumer` | Contract has no subject, so it permits nothing.
- ADDED test-tenant | Contract without subjects | `uni/tn-test-tenant/brc-provider` | Contract has no subject, so it permits nothing.
- ADDED test-tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-test-tenant/out-l3out1` | Configuration failed for uni/tn-test-tenant/out-l3out1 node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 101 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database`
- STILL BROKEN, reason changed: SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web`

New critical faults:
- F0467 PROD `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG`: Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 PROD `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG`: Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG node 101 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Pune-Tenants `uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG`: Configuration failed for uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG node 101 eth1/26 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 RB-Tenant `uni/tn-RB-Tenant/out-RB-L3-Out`: Configuration failed for uni/tn-RB-Tenant/out-RB-L3-Out node 102 eth1/48 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 User-Applications `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox`: Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 101 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 User-Applications `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier`: Configuration failed for uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier node 101 eth1/8 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 test-tenant `uni/tn-test-tenant/out-l3out1`: Configuration failed for uni/tn-test-tenant/out-l3out1 node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 7 | 35 | +28 | 29 | 10 |
| VRF | 18 | 9 | 30 | +21 | 22 | 10 |
| BD | 23 | 8 | 35 | +27 | 28 | 16 |
| Subnet (BD) | 23 | 8 | 30 | +22 | 24 | 17 |
| AP | 16 | 9 | 23 | +14 | 15 | 8 |
| EPG | 33 | 15 | 41 | +26 | 29 | 21 |
