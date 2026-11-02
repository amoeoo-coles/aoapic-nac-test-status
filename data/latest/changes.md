# Changes since previous morning (2026-11-02-0816 -> 2026-11-03-0822)

Previous snapshot 2026-11-02 08:16:42 AEDT; current snapshot 2026-11-03 08:23:32 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 103 | 87 | -16 |
| integrity passed | 99 | 85 | -14 |
| integrity failed | 4 | 2 | -2 |
| drift total | 129 | 129 | +0 |
| drift passed | 45 | 45 | +0 |
| drift failed | 84 | 84 | +0 |

Tenants: 16 -> 11; broken 5 -> 2
- added: Bank-Demo, SIS_PROD, TenantAPPC3750
- removed: Ansible-PROD, Ansible-QA, BCC-222, daa, DEMO1, Graph, TENANT_MYTEST, TEST-POM
- newly broken: TenantAPPC3750 (new)
- fixed: Heroes, oneaciapp

Broken relations: 8 -> 5
- ADDED TenantAPPC3750 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not have
- RESOLVED Graph | Contract service graph not instantiated | `uni/tn-Graph/brc-Grapn-contract` | Contract redirects through service graph tn-Graph/AbsGraph-Firewall which cannot be deployed (4 faults, e.g. F0758: Service graph  for tenant Graph could not be instantiated. Info: Selected LDev has faults:  Tenant Graph, L4-L7 Devices Firewall); traffic on this contract is dropped.
- RESOLVED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-209 :There is no domain, associated with both EPG and Port, that has required VLAN;
- RESOLVED daa | Major fault F606347 | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-daa/ap-ap1/epg-TEST_EPG) Tenant: daa associated with either EPG:(Ap: ap1 Epg: TEST_EPG) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: Vcenter VM Domain: VMM-Domain VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompEpP
- RESOLVED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/out-OSPf` | Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

New critical faults:
- F0467 TenantAPPC3750 `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN`: Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: vlan-10 :There is no domain, associated with both EPG and Port, that has required VLAN;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 16 | 11 | -5 | 5 | 10 |
| VRF | 18 | 17 | 13 | -4 | 5 | 10 |
| BD | 23 | 20 | 16 | -4 | 10 | 17 |
| Subnet (BD) | 23 | 13 | 12 | -1 | 8 | 19 |
| AP | 16 | 16 | 13 | -3 | 5 | 8 |
| EPG | 33 | 31 | 26 | -5 | 13 | 20 |
