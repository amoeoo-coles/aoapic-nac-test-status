# ACI tenant logical-integrity report: 2026-10-30

## BROKEN RELATIONS FOUND - 31 broken, 44 warnings (8 of 17 tenants broken: ASN-02, MUHC, T1_FIRST, TN-AUTO, TN-DEDUP-LAB, TN_PROD, Test101, mgmt)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-30 08:16:31 AEDT)
- Generated: 2026-10-30 08:16:55 AEDT
- Scope: 17 tenants on the APIC (6 in baseline, new: ASN-02, ASN_01, Automation-Test, ddso, gtest, Irelia-TEST, T1_FIRST, Test101, TestTenant, TN-AUTO, TN_PROD); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 127 tests, 116 passed, 11 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| ASN-02 | NEW | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 3 | 1 | 81 | BROKEN |
| ASN_01 | NEW | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| Automation-Test | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 7 | 1 | 0 | 6 | 0 | 82 | WARN |
| ddso | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| gtest | NEW | 1 | 1 | 0 | 1 | 10 | 0 | 0 | 0 | 11 | 0 | 67 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| Irelia-TEST | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 3 | 1 | 81 | BROKEN |
| MUHC | yes | 0 | 2 | 2 | 1 | 2 | 0 | 0 | 8 | 0 | 0 | 20 | BROKEN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| T1_FIRST | NEW | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 90 | BROKEN |
| Test101 | NEW | 2 | 4 | 4 | 2 | 4 | 1 | 0 | 8 | 2 | 12 | 14 | BROKEN |
| TestTenant | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 97 | WARN |
| TN-AUTO | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 4 | 2 | 68 | BROKEN |
| TN-DEDUP-LAB | yes | 1 | 1 | 1 | 1 | 9 | 21 | 2 | 9 | 5 | 0 | 0 | BROKEN |
| TN_PROD | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 87 | BROKEN |

## Broken relations (31)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| ASN-02 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-ASN-02/out-VRF_PRUEBA` | Configuration failed for uni/tn-ASN-02/out-VRF_PRUEBA node 101 eth1/25 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2341_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended. | Create L3Out 'LEGACY_L3OUT' or remove the BD-to-L3Out association. |
| MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2342_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended. | Create L3Out 'LEGACY_L3OUT' or remove the BD-to-L3Out association. |
| MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2341_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'LEGACY_VRF' in MUHC (or common), or point the BD to an existing VRF. |
| MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2342_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'LEGACY_VRF' in MUHC (or common), or point the BD to an existing VRF. |
| MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` | EPG -> tn-MUHC/BD-VLAN_2341_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present'). | Fix the VRF of tn-MUHC/BD-VLAN_2341_BD first; the EPG recovers automatically. |
| MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` | EPG -> tn-MUHC/BD-VLAN_2342_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present'). | Fix the VRF of tn-MUHC/BD-VLAN_2342_BD first; the EPG recovers automatically. |
| MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target). | Create domain uni/phys-LEGACY_SRVF_PHY (with VLAN pool/AAEP) or associate an existing one. |
| MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target). | Create domain uni/phys-LEGACY_SRVF_PHY (with VLAN pool/AAEP) or associate an existing one. |
| T1_FIRST | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG` | Configuration failed for uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG node 101 eth1/26 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TN-AUTO | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TN-AUTO | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-BACKUP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-MGMT-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-WEB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-LDAP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-SMTP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-WEB-APP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN_PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a` | Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 102 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-833 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-40 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test101 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test101 | Major fault F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-APP) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-APP) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompE | See the APIC fault description and resolve the referenced object. |
| Test101 | Major fault F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-DB) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-DB) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompEpP | See the APIC fault description and resolve the referenced object. |
| Test101 | Major fault F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-APP) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-APP) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:C | See the APIC fault description and resolve the referenced object. |
| Test101 | Major fault F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-DB) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-DB) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: vcenter-SI VM Domain: DVS VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:Com | See the APIC fault description and resolve the referenced object. |
| mgmt | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-mgmt/out-l3out_mgmt_inb` | Configuration failed for uni/tn-mgmt/out-l3out_mgmt_inb node 101 eth1/5 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (44)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| ASN-02 | AP without EPGs | `uni/tn-ASN-02/ap-AP` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| ASN-02 | External EPG without contracts | `uni/tn-ASN-02/out-VRF_PRUEBA/instP-EXTEPG` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| ASN-02 | VRF unused | `uni/tn-ASN-02/ctx-VRF_ASN-02A` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| ASN_01 | BD unused | `uni/tn-ASN_01/BD-BD01` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| ASN_01 | VRF unused | `uni/tn-ASN_01/ctx-VRF_A2` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| ASN_01 | VRF unused | `uni/tn-ASN_01/ctx-VRF_A3` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| Automation-Test | Tenant empty | `uni/tn-Automation-Test` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Irelia-TEST | Tenant empty | `uni/tn-Irelia-TEST` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| TN-AUTO | BD unused | `uni/tn-TN-AUTO/BD-BD_AUTO` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TN-AUTO | External EPG without contracts | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP/instP-EXT_EPG` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| TN-AUTO | External EPG without contracts | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC/instP-EXT_EPG` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| TN-AUTO | L3 BD without subnet | `uni/tn-TN-AUTO/BD-BD_AUTO` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| TN-DEDUP-LAB | Contract provided, never consumed | `uni/tn-TN-DEDUP-LAB/brc-C-APP-DB-FW` | Provided by 2 object(s) (e.g. tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-App) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-DNS: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-DNS-FW (keep tn-TN-DEDUP-LAB/brc-C-DNS). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-MONITORING: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD (keep tn-TN-DEDUP-LAB/brc-C-MONITORING). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-NTP-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-NTP: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-NTP-FW (keep tn-TN-DEDUP-LAB/brc-C-NTP). |
| TN-DEDUP-LAB | vzAny contract | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` | vzAny provides 0 / consumes 2 contract(s) (C-SMTP, C-SMTP-FW); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| TN_PROD | External EPG without contracts | `uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a/instP-L3EPG_SW_DISTR_2a_PROD` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| Test101 | EPG isolated (no contracts) | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Test101 | EPG isolated (no contracts) | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TestTenant | L3Out without external EPG | `uni/tn-TestTenant/out-TestL3Out` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. | Add an external EPG with the external subnets and contracts. |
| common | Contract unused | `uni/tn-common/brc-ct-DNS-SHARED` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-ct-MONITORING-SHARED` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-ct-NTP-SHARED` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-power_up` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-sql` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| ddso | BD unused | `uni/tn-ddso/BD-BD11` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| ddso | L3 BD without subnet | `uni/tn-ddso/BD-BD11` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Arizona` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-California` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Florida` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Idaho` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Nebraska` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Nevada` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Oklahoma` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Texas` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Utah` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | EPG isolated (no contracts) | `uni/tn-gtest/ap-gtest-apps/epg-Washington` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| gtest | L3 BD without subnet | `uni/tn-gtest/BD-gtest-bridge` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | Contract consumed, never provided | `uni/tn-mgmt/brc-contract-mgmt-inb` | Consumed by 1 object(s) (e.g. tn-mgmt/out-l3out_mgmt_inb/instP-eepg_mgmt_inb) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 31 broken relation(s) in 8 tenant(s): Critical fault F0467 (EPG deployment on path failed) (10); Contract service graph not instantiated (9); Major fault F606347 (4); BD L3Out missing-target (2); BD VRF missing-target (2); EPG chain broken (BD has no VRF) (2)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default); vzAny contract: 1 (e.g. tn-TN-DEDUP-LAB/ctx-VRF-LAB)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 1 (e.g. tn-TN-DEDUP-LAB/brc-C-APP-DB-FW); Contract consumed, never provided: 1 (e.g. tn-mgmt/brc-contract-mgmt-inb); Contract unused: 7 (e.g. tn-common/brc-ct-DNS-SHARED, tn-common/brc-ct-MONITORING-SHARED); EPG isolated (no contracts): 12 (e.g. tn-Test101/ap-DEV/epg-DEV-APP, tn-Test101/ap-DEV/epg-DEV-DB); External EPG without contracts: 4 (e.g. tn-ASN-02/out-VRF_PRUEBA/instP-EXTEPG, tn-TN-AUTO/out-L3OUT_ROUTER_BGP/instP-EXT_EPG); Duplicate contract: 3 (e.g. tn-TN-DEDUP-LAB/brc-C-DNS-FW, tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 5 (e.g. tn-TN-AUTO/BD-BD_AUTO, tn-ddso/BD-BD11); L3 BD flooding: 8 (e.g. tn-ASN_01/BD-BD01, tn-MUHC/BD-VLAN_2341_BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 3; VRF unused: 5; BD unused: 5; AP without EPGs: 2; Filter unused: 2; L3Out without external EPG: 2  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 98 of 119 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 53 of 119 objects have no annotation; in use: 'orchestrator:ansible' x58, 'orchestrator:terraform' x6, 'orchestrator:RobotFramework' x2.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 72, Mixed 31, lower 16; 2 generic/VLAN/IP-style names (e.g. tn-TestTenant/ctx-TestVRF, tn-TestTenant/out-TestL3Out).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 20, missing domain: 2  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (61)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| ASN_01 | L3 BD flooding | `uni/tn-ASN_01/BD-BD01` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MUHC | EPG without static path | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` | No static path bindings (fvRsPathAtt). |
| MUHC | EPG without static path | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` | No static path bindings (fvRsPathAtt). |
| MUHC | L3 BD flooding | `uni/tn-MUHC/BD-VLAN_2341_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MUHC | L3 BD flooding | `uni/tn-MUHC/BD-VLAN_2342_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| T1_FIRST | EPG without domain | `uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| T1_FIRST | L3 BD flooding | `uni/tn-T1_FIRST/BD-BD_FIRST` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Backup` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Dir` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Infra` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mail` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mgmt` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mon` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without domain | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-App` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Backup` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-DB` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Dir` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Infra` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mail` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mgmt` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mon` | No static path bindings (fvRsPathAtt). |
| TN-DEDUP-LAB | EPG without static path | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Web` | No static path bindings (fvRsPathAtt). |
| Test101 | L3 BD flooding | `uni/tn-Test101/BD-BD10` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test101 | L3 BD flooding | `uni/tn-Test101/BD-BD100` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test101 | L3 BD flooding | `uni/tn-Test101/BD-BD20` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test101 | L3 BD flooding | `uni/tn-Test101/BD-BD200` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | BD unused | `uni/tn-common/BD-default` | No EPG is attached to this bridge domain. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | L3Out without external EPG | `uni/tn-common/out-default` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Arizona` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-California` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Florida` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Idaho` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Nebraska` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Nevada` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Oklahoma` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Texas` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Utah` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without domain | `uni/tn-gtest/ap-gtest-apps/epg-Washington` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Arizona` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-California` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Florida` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Idaho` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Nebraska` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Nevada` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Oklahoma` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Texas` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Utah` | No static path bindings (fvRsPathAtt). |
| gtest | EPG without static path | `uni/tn-gtest/ap-gtest-apps/epg-Washington` | No static path bindings (fvRsPathAtt). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| ASN-02 | Integrity ASN-02: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-ASN-02/out-VRF_PRUEBA node 101 eth1/25 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is n'] |
| MUHC | Integrity MUHC: all named relations resolve | Unresolved relations: ['uni/tn-MUHC/BD-VLAN_2341_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2342_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2341_BD/rsBDToOut-LEGACY_L3OUT (state=formed, stateQual=mismatch-target, tDn=uni/tn-common/out-default)', 'uni/tn-MUHC/BD-VLAN_2342_BD/rsBDToOut-LEGACY_L3OUT (state=formed, stateQual=mismatc |
| MUHC | Integrity BD MUHC/VLAN_2341_BD: VRF resolves | uni/tn-MUHC/BD-VLAN_2341_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity BD MUHC/VLAN_2342_BD: VRF resolves | uni/tn-MUHC/BD-VLAN_2342_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity EPG MUHC/LEGACY_APR/VLAN_2341_EPG: BD and VRF chain resolves | uni/tn-MUHC/BD-VLAN_2341_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity EPG MUHC/LEGACY_APR/VLAN_2342_EPG: BD and VRF chain resolves | uni/tn-MUHC/BD-VLAN_2342_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| Mgmt | Integrity mgmt: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-mgmt/out-l3out_mgmt_inb node 101 eth1/5 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is '] |
| T1 FIRST | Integrity T1_FIRST: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG node 101 eth1/26 due to Invalid Path Configuration,Invalid VLAN Configuration, debug'] |
| TN PROD | Integrity TN_PROD: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 101 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: inval', 'F0467 critical: Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 102 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: inval'] |
| TN-AUTO | Integrity TN-AUTO: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does n', 'F0467 critical: Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface doe'] |
| Test101 | Integrity Test101: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 101 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the E', 'F0467 critical: Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the E', 'F0467 critical: |

## Tenant faults (faultInst)

By severity: warning 4, minor 40, major 4, critical 15; TCA/threshold faults (context only): 0

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| Test101 | major | F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-APP) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-APP) or Services:(LDevInst:   EPpInfo:   ) on VM  |
| Test101 | major | F606347 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-DEV/epg-DEV-DB) Tenant: Test101 associated with either EPG:(Ap: DEV Epg: DEV-DB) or Services:(LDevInst:   EPpInfo:   ) on VM Co |
| Test101 | major | F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-APP) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-APP) or Services:(LDevInst:   EPpInfo:   ) on |
| Test101 | major | F606347 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-Test101/ap-PROD/epg-PROD-DB) Tenant: Test101 associated with either EPG:(Ap: PROD Epg: PROD-DB) or Services:(LDevInst:   EPpInfo:   ) on V |
| TN_PROD | critical | F0467 | `uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a` | Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 102 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-833 :Either the EpG is not |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the EpG is not associated with a domain or th |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-40 :Either the EpG is not associated with a domain or the |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-APP node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :Either the EpG is not associated with a domain or  |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-DB node 102 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :Either the EpG is not associated with a domain or t |
| TN-AUTO | critical | F0467 | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_BGP node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| TN-AUTO | critical | F0467 | `uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC` | Configuration failed for uni/tn-TN-AUTO/out-L3OUT_ROUTER_STATIC node 101 PC_ROUTER due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| T1_FIRST | critical | F0467 | `uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG` | Configuration failed for uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG node 101 eth1/26 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :STP Seg |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-DB node 101 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-20 :Either the EpG is not associated with a domain or t |
| ASN-02 | critical | F0467 | `uni/tn-ASN-02/out-VRF_PRUEBA` | Configuration failed for uni/tn-ASN-02/out-VRF_PRUEBA node 101 eth1/25 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domai |
| TN_PROD | critical | F0467 | `uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a` | Configuration failed for uni/tn-TN_PROD/out-L3OUT_SW_DISTR_2a node 101 SRVR01 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-833 :Either the EpG is not |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-APP node 101 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-30 :Either the EpG is not associated with a domain or th |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` | Configuration failed for uni/tn-Test101/ap-DEV/epg-DEV-DB node 101 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-40 :Either the EpG is not associated with a domain or the |
| Test101 | critical | F0467 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` | Configuration failed for uni/tn-Test101/ap-PROD/epg-PROD-APP node 101 SRVR01 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :Either the EpG is not associated with a domain or  |
| mgmt | critical | F0467 | `uni/tn-mgmt/out-l3out_mgmt_inb` | Configuration failed for uni/tn-mgmt/out-l3out_mgmt_inb node 101 eth1/5 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the doma |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
