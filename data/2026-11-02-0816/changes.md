# Changes since previous morning (2026-11-01-0821 -> 2026-11-02-0816)

Previous snapshot 2026-11-01 08:21:24 AEDT; current snapshot 2026-11-02 08:16:42 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 61 | 103 | +42 |
| integrity passed | 60 | 99 | +39 |
| integrity failed | 1 | 4 | +3 |
| drift total | 129 | 129 | +0 |
| drift passed | 45 | 45 | +0 |
| drift failed | 84 | 84 | +0 |

Tenants: 10 -> 16; broken 1 -> 5
- added: BCC-222, DEMO1, Graph, iacdemo-contractors, iacdemo-prod, TEST-POM
- removed: none
- newly broken: daa, Heroes, oneaciapp, Graph (new)
- fixed: none

Broken relations: 4 -> 8
- ADDED Graph | Contract service graph not instantiated | `uni/tn-Graph/brc-Grapn-contract` | Contract redirects through service graph tn-Graph/AbsGraph-Firewall which cannot be deployed (4 faults, e.g. F0758: Service graph  for tenant Graph could not be instantiated. Info: Selected LDev has faults:  Tenant Graph, L4-L7 Devices Firewall); traffic on this contract is dropped.
- ADDED Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-209 :There is no domain, associated with both EPG and Port, that has required VLAN;
- ADDED daa | Major fault F606347 | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-daa/ap-ap1/epg-TEST_EPG) Tenant: daa associated with either EPG:(Ap: ap1 Epg: TEST_EPG) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: Vcenter VM Domain: VMM-Domain VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompEpP
- ADDED oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/out-OSPf` | Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

New critical faults:
- F0467 Heroes `uni/tn-Heroes/ap-Save_The_Planet/epg-web`: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-210 :There is no domain, associated with both EPG and Port, that has required VLAN;
- F0467 oneaciapp `uni/tn-oneaciapp/out-OSPf`: Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/47 due to Invalid Path Configuration,Multiple VRF configuration provided for an encap or path, debug message: multiple-ctx-configuration: Interface is already configured under other VRF named Heroes:Heroes_Only;invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 10 | 16 | +6 | 10 | 10 |
| VRF | 18 | 8 | 17 | +9 | 9 | 10 |
| BD | 23 | 6 | 20 | +14 | 14 | 17 |
| Subnet (BD) | 23 | 4 | 13 | +9 | 9 | 19 |
| AP | 16 | 12 | 16 | +4 | 8 | 8 |
| EPG | 33 | 20 | 31 | +11 | 18 | 20 |
