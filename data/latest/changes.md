# Changes since previous morning (2026-11-09-0824 -> 2026-11-10-0818)

Previous snapshot 2026-11-09 08:25:12 AEDT; current snapshot 2026-11-10 08:19:02 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 82 | 200 | +118 |
| integrity passed | 76 | 188 | +112 |
| integrity failed | 6 | 12 | +6 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 20 | +0 |
| drift failed | 109 | 109 | +0 |

Tenants: 14 -> 30; broken 4 -> 7
- added: billing-test-DPYD6hPFFmE9, EM-LAB, iTenant, MGMT_LAN, mjay_dev, NZ-ACI-LAB, Tenant-Ahmed, Test100, Test_9112026, TESTING123, TN-LAB-ANS01, TN-LAB-K01, TN-LAB-K02, tn_example_tenant, Zangief, zzzps4021, zzzps4021_BGP
- removed: CORP_PROD
- newly broken: tenant_mylab, Test100 (new), Test_9112026 (new)
- fixed: none

Broken relations: 8 -> 17
- ADDED LAB-TENANT | Contract without subjects | `uni/tn-LAB-TENANT/brc-teste123` | Contract has no subject, so it permits nothing.
- ADDED LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/out-L3OUT_TESTE` | Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED Test100 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test100/out-L3out` | Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-inter-VRF_contract` | Contract has no subject, so it permits nothing.
- ADDED Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-intra-VRF_contract` | Contract has no subject, so it permits nothing.
- ADDED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out node 101 eth1/11 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- ADDED tenant_mylab | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tenant_mylab/out-ok` | Configuration failed for uni/tn-tenant_mylab/out-ok node 101 eth1/40 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- STILL BROKEN, reason changed: VY-TN | Major fault F0565 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02`

New critical faults:
- F0467 LAB-TENANT `uni/tn-LAB-TENANT/out-L3OUT_TESTE`: Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Test100 `uni/tn-Test100/out-L3out`: Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Test_9112026 `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out`: Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Test_9112026 `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out`: Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 Test_9112026 `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out`: Configuration failed for uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out node 101 eth1/11 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- F0467 tenant_mylab `uni/tn-tenant_mylab/out-ok`: Configuration failed for uni/tn-tenant_mylab/out-ok node 101 eth1/40 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 14 | 30 | +16 | 26 | 12 |
| VRF | 18 | 18 | 33 | +15 | 27 | 12 |
| BD | 23 | 22 | 46 | +24 | 42 | 19 |
| Subnet (BD) | 23 | 13 | 36 | +23 | 35 | 22 |
| AP | 16 | 14 | 25 | +11 | 22 | 13 |
| EPG | 33 | 24 | 40 | +16 | 38 | 31 |
