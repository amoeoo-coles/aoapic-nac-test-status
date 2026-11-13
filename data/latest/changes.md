# Changes since previous morning (2026-11-11-0835 -> 2026-11-14-0835)

Previous snapshot 2026-11-11 08:35:58 AEDT; current snapshot 2026-11-14 08:35:26 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 253 | 57 | -196 |
| integrity passed | 236 | 55 | -181 |
| integrity failed | 17 | 2 | -15 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 56 | +36 |
| drift failed | 109 | 73 | -36 |

Tenants: 37 -> 7; broken 10 -> 2
- added: Heroes, ROR, SnV
- removed: billing-test-DPYD6hPFFmE9, Cursor_tenant1, Cursor_Tenant2, Cursor_Tenant3, Cursor_tenant5, EM-LAB, iTenant, LAB-TENANT, MAD, MGMT_LAN, mjay_dev, Mouse, Prod, Production, RB-Tenant, Tenant-Ahmed, Tenant2, Tenant_RG, Test, Test100, Test_9112026, TN-CONSUMER, TN-CONSUMER-BGS, TN-LAB-ANS01, TN-LAB-K01, TN-LAB-K02, TN-PROVIDER, TN-PROVIDER-BGS, tn_example_tenant, VY-TN, Zangief, zzzps4021, zzzps4021_BGP
- newly broken: Heroes (new), SnV (new)
- fixed: none

Broken relations: 24 -> 12
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 101 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- ADDED SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED Cursor_tenant1 | BD VRF missing-target | `uni/tn-Cursor_tenant1/BD-p2bd` | BD points to VRF 'p2v' which does not exist in tenant Cursor_tenant1 or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- RESOLVED LAB-TENANT | Contract without subjects | `uni/tn-LAB-TENANT/brc-teste123` | Contract has no subject, so it permits nothing.
- RESOLVED LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message: 
- RESOLVED LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/out-L3OUT_TESTE` | Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Production | Contract without subjects | `uni/tn-Production/brc-BD-APP` | Contract has no subject, so it permits nothing.
- RESOLVED Production | Contract without subjects | `uni/tn-Production/brc-BD-DB` | Contract has no subject, so it permits nothing.
- RESOLVED RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-FTP` | Contract has no subject, so it permits nothing.
- RESOLVED RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-HTTPS` | Contract has no subject, so it permits nothing.
- RESOLVED RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message: 
- RESOLVED Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for node 102 due to Interface Configured as L3, debug message: port-configured-as-l3: Interface is already configured under other VRF named LAB-TENANT:LAB-VRF;
- RESOLVED Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Test100 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test100/out-L3out` | Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-inter-VRF_contract` | Contract has no subject, so it permits nothing.
- RESOLVED Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-intra-VRF_contract` | Contract has no subject, so it permits nothing.
- RESOLVED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out node 101 eth1/11 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG` | Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED VY-TN | Major fault F0565 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | Deployment of EPG uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02 failed on domain test-vmm due to EPG encapsulation value is not part of any static encapsulation block for the VMM domain
- RESOLVED tenant_mylab | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tenant_mylab/out-ok` | Configuration failed for uni/tn-tenant_mylab/out-ok node 101 eth1/40 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-333 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned t
- RESOLVED tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_20 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-111 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- RESOLVED zzzps4021_BGP | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-zzzps4021_BGP/out-test-L3OUT` | Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;

New critical faults:
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-app`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-db`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-web`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 Heroes `uni/tn-Heroes/out-Heroes_external_corporate`: Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 102 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 SnV `uni/tn-SnV/ap-Chaos/epg-Database`: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Chaos/epg-Web`: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Evolution_X/epg-Database`: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Evolution_X/epg-Web`: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Power_Up/epg-Database`: Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Power_Up/epg-Web`: Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Rescue/epg-Database`: Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- F0467 SnV `uni/tn-SnV/ap-Rescue/epg-Web`: Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 37 | 7 | -30 | 0 | 9 |
| VRF | 18 | 40 | 9 | -31 | 0 | 9 |
| BD | 23 | 59 | 8 | -51 | 0 | 15 |
| Subnet (BD) | 23 | 46 | 8 | -38 | 0 | 15 |
| AP | 16 | 38 | 9 | -29 | 0 | 7 |
| EPG | 33 | 54 | 15 | -39 | 0 | 18 |
