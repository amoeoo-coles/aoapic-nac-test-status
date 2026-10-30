# Changes since previous morning (2026-10-30-0816 -> 2026-10-31-0821)

Previous snapshot 2026-10-30 08:16:31 AEDT; current snapshot 2026-10-31 08:22:07 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 127 | 66 | -61 |
| integrity passed | 116 | 66 | -50 |
| integrity failed | 11 | 0 | -11 |
| drift total | 129 | 129 | +0 |
| drift passed | 35 | 31 | -4 |
| drift failed | 94 | 98 | +4 |

Tenants: 17 -> 14; broken 8 -> 0
- added: aaaaa, Atul_tenant, BCC-222, DEMO1, iacdemo-contractors, iacdemo-prod, MS-T, PY-TN, ROR, Tenant_Test
- removed: ASN-02, ASN_01, Automation-Test, ddso, gtest, Irelia-TEST, MUHC, T1_FIRST, Test101, TestTenant, TN-AUTO, TN-DEDUP-LAB, TN_PROD
- newly broken: none
- fixed: mgmt

Broken relations: 31 -> 0
- RESOLVED ASN-02 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-ASN-02/out-VRF_PRUEBA` | Configuration failed for uni/tn-ASN-02/out-VRF_PRUEBA node 101 eth1/25 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;
- RESOLVED MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2341_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended.
- RESOLVED MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2342_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended.
- RESOLVED MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2341_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- RESOLVED MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2342_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed.
- RESOLVED MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` | EPG -> tn-MUHC/BD-VLAN_2341_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present').
- RESOLVED MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` | EPG -> tn-MUHC/BD-VLAN_2342_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present').
- RESOLVED MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target).
- RESOLVED MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target).
- RESOLVED T1_FIRST | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG` | Configuration failed for uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG node 101 eth1/26 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not
- RESOLVED TN-AUTO | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED TN-AUTO | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist;
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-BACKUP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-MGMT-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-WEB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-LDAP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-SMTP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-WEB-APP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- RESOLVED TN_PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a` | Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 102 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-833 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either 
- RESOLVED Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- RESOLVED Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-40 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- RESOLVED Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- RESOLVED Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;
- RESOLVED Test101 | Major fault F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-APP) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-APP) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompE
- RESOLVED Test101 | Major fault F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-DB) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-DB) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompEpP
- RESOLVED Test101 | Major fault F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-APP) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-APP) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:C
- RESOLVED Test101 | Major fault F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-DB) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-DB) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:Com
- RESOLVED mgmt | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-mgmt/out-l3out_mgmt_inb` | Configuration failed for uni/tn-mgmt/out-l3out_mgmt_inb node 101 eth1/5 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it;

New critical faults:
- none

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 17 | 14 | -3 | 9 | 11 |
| VRF | 18 | 20 | 13 | -7 | 6 | 11 |
| BD | 23 | 16 | 15 | -1 | 9 | 17 |
| Subnet (BD) | 23 | 12 | 11 | -1 | 6 | 18 |
| AP | 16 | 10 | 11 | +1 | 7 | 12 |
| EPG | 33 | 28 | 17 | -11 | 13 | 29 |
