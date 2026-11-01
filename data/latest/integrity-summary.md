# ACI tenant logical-integrity report: 2026-11-02

## BROKEN RELATIONS FOUND - 8 broken, 43 warnings (5 of 16 tenants broken: Graph, Heroes, SnV, daa, oneaciapp)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-02 08:16:42 AEDT)
- Generated: 2026-11-02 08:17:11 AEDT
- Scope: 16 tenants on the APIC (6 in baseline, new: Ansible-PROD, Ansible-QA, BCC-222, daa, DEMO1, Graph, iacdemo-contractors, iacdemo-prod, TENANT_MYTEST, TEST-POM); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 103 tests, 99 passed, 4 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Ansible-PROD | NEW | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| Ansible-QA | NEW | 0 | 0 | 0 | 2 | 5 | 0 | 0 | 0 | 10 | 0 | 70 | WARN |
| BCC-222 | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| daa | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 87 | BROKEN |
| DEMO1 | NEW | 2 | 4 | 2 | 1 | 3 | 0 | 0 | 0 | 8 | 0 | 76 | WARN |
| Graph | NEW | 1 | 2 | 0 | 1 | 2 | 1 | 0 | 1 | 4 | 0 | 78 | BROKEN |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 1 | 0 | 4 | 90 | BROKEN |
| iacdemo-contractors | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-prod | NEW | 1 | 3 | 3 | 1 | 3 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 | 90 | BROKEN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 1 | 4 | 57 | BROKEN |
| TENANT_MYTEST | NEW | 1 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 6 | 0 | 82 | WARN |
| TEST-POM | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |

## Broken relations (8)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Graph | Contract service graph not instantiated | `uni/tn-Graph/brc-Grapn-contract` | Contract redirects through service graph tn-Graph/AbsGraph-Firewall which cannot be deployed (4 faults, e.g. F0758: Service graph  for tenant Graph could not be instantiated. Info: Selected LDev has faults:  Tenant Graph, L4-L7 Devices Firewall); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-209 :There is no domain, associated with both EPG and Port, that has required VLAN; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| daa | Major fault F606347 | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-daa/ap-ap1/epg-TEST_EPG) Tenant: daa associated with either EPG:(Ap: ap1 Epg: TEST_EPG) or Services:(LDevInst:   EPpInfo:   ) on VM Controller: Vcenter VM Domain: VMM-Domain VM Provider: VMware, failed with error: (TASK:ifc:vmmmgr:CompEpP | See the APIC fault description and resolve the referenced object. |
| oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/out-OSPf` | Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (43)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Ansible-PROD | EPG BD fallback to common | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-PROD | EPG BD fallback to common | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-PROD | EPG isolated (no contracts) | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-PROD | EPG isolated (no contracts) | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-QA | EPG BD fallback to common | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-13-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-QA | EPG BD fallback to common | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-14-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-QA | EPG BD fallback to common | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-15-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-QA | EPG BD fallback to common | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-11-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-QA | EPG BD fallback to common | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-12-0` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Ansible-QA | EPG isolated (no contracts) | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-13-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-QA | EPG isolated (no contracts) | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-14-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-QA | EPG isolated (no contracts) | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-15-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-QA | EPG isolated (no contracts) | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-11-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Ansible-QA | EPG isolated (no contracts) | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-12-0` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| BCC-222 | VRF unused | `uni/tn-BCC-222/ctx-VRF-BCC-222` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| DEMO1 | BD unused | `uni/tn-DEMO1/BD-Test` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| DEMO1 | Config fault F4307 | `uni/tn-DEMO1/ctx-Test-01/ctxrtsummpol-aa/rtsummsubnet-[192.168.10.0/24]` | Route Summarization policy is missing from rtsumSubnet | See the APIC fault description and resolve the referenced object. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan300-web-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan301-dab-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan302-web2-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | L3 BD without subnet | `uni/tn-DEMO1/BD-Test` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| DEMO1 | L3 BD without subnet | `uni/tn-DEMO1/BD-bd-vlan301-dab-demo1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| DEMO1 | L3 BD without subnet | `uni/tn-DEMO1/BD-bd-vlan302-web2-demo1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Graph | Config fault F1690 | `uni/tn-Graph/lDevVip-Firewall/lIf-Cluster/vnsConfIssue-lif-has-invalid-encap` | Configuration is invalid due to invalid encapsulation on LIf | See the APIC fault description and resolve the referenced object. |
| Graph | Config fault F1690 | `uni/tn-Graph/lDevVip-Firewall/vnsConfIssue-lif-has-invalid-encap` | Configuration is invalid due to invalid encapsulation on LIf | See the APIC fault description and resolve the referenced object. |
| Graph | Permit-any filter | `uni/tn-Graph/brc-Grapn-contract` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| Graph | Preferred group enabled | `uni/tn-Graph/ctx-Graph` | Preferred group is enabled on vzAny; 2 member EPG(s) talk to each other without contracts. | Use preferred groups only for migration; replace with explicit contracts and keep the member list small. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TENANT_MYTEST | BD unused | `uni/tn-TENANT_MYTEST/BD-BD-MyTest1-192.168.1.0` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TENANT_MYTEST | BD unused | `uni/tn-TENANT_MYTEST/BD-BD1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TENANT_MYTEST | BD unused | `uni/tn-TENANT_MYTEST/BD-BD2` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TENANT_MYTEST | Config fault F0764 | `uni/tn-TENANT_MYTEST/lDevVip-Firewall` | L4-L7 Devices configuration Firewall for tenant TENANT_MYTEST is invalid. | See the APIC fault description and resolve the referenced object. |
| TENANT_MYTEST | Contract unused | `uni/tn-TENANT_MYTEST/brc-Contract` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| TENANT_MYTEST | L3 BD without subnet | `uni/tn-TENANT_MYTEST/BD-BD-MyTest1-192.168.1.0` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| TEST-POM | VRF unused | `uni/tn-TEST-POM/ctx-TEST-PRD` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| daa | EPG isolated (no contracts) | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 8 broken relation(s) in 5 tenant(s): Critical fault F0467 (EPG deployment on path failed) (6); Contract service graph not instantiated (1); Major fault F606347 (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 2 (e.g. tn-Graph/brc-Grapn-contract, tn-common/brc-default); Preferred group enabled: 1 (e.g. tn-Graph/ctx-Graph)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 1 (e.g. tn-SnV/brc-web); Contract unused: 1 (e.g. tn-TENANT_MYTEST/brc-Contract); EPG isolated (no contracts): 16 (e.g. tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0, tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Match contract scope to real usage** - found: scope mismatch: 0, wider than needed: 1  
   Do: Use 'context' by default, 'tenant'/'global' only for inter-VRF/tenant flows (with shared subnets).
5. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 6 (e.g. tn-DEMO1/BD-Test, tn-DEMO1/BD-bd-vlan301-dab-demo1); L3 BD flooding: 5 (e.g. tn-DEMO1/BD-bd-vlan300-web-demo1, tn-TENANT_MYTEST/BD-BD1)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
6. **Clean up unused objects** - found: VRF unused: 4; BD unused: 5; AP without EPGs: 1; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
7. **Add descriptions** - found: 69 of 87 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
8. **Tag ownership (annotations) for NaC** - found: 64 of 87 objects have no annotation; in use: 'orchestrator:terraform' x13, 'orchestrator:ansible' x10.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
9. **Adopt one naming convention** - found: name styles in use: Mixed 50, UPPER_SNAKE 11, lower 26; 3 generic/VLAN/IP-style names (e.g. tn-DEMO1/BD-Test, tn-daa/BD-TEST_BD, tn-daa/ap-ap1/epg-TEST_EPG).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
10. **Bind EPGs to a domain** - found: no domain: 15, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (56)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Ansible-PROD | EPG without domain | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-PROD | EPG without domain | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-PROD | EPG without static path | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0` | No static path bindings (fvRsPathAtt). |
| Ansible-PROD | EPG without static path | `uni/tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0` | No static path bindings (fvRsPathAtt). |
| Ansible-QA | EPG without domain | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-13-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-QA | EPG without domain | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-14-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-QA | EPG without domain | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-15-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-QA | EPG without domain | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-11-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-QA | EPG without domain | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-12-0` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Ansible-QA | EPG without static path | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-13-0` | No static path bindings (fvRsPathAtt). |
| Ansible-QA | EPG without static path | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-14-0` | No static path bindings (fvRsPathAtt). |
| Ansible-QA | EPG without static path | `uni/tn-Ansible-QA/ap-Bare-Metals/epg-Subnet-192-168-15-0` | No static path bindings (fvRsPathAtt). |
| Ansible-QA | EPG without static path | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-11-0` | No static path bindings (fvRsPathAtt). |
| Ansible-QA | EPG without static path | `uni/tn-Ansible-QA/ap-Hypervisors/epg-Subnet-192-168-12-0` | No static path bindings (fvRsPathAtt). |
| DEMO1 | EPG without domain | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan300-web-demo1` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DEMO1 | EPG without static path | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan300-web-demo1` | No static path bindings (fvRsPathAtt). |
| DEMO1 | EPG without static path | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan301-dab-demo1` | No static path bindings (fvRsPathAtt). |
| DEMO1 | EPG without static path | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan302-web2-demo1` | No static path bindings (fvRsPathAtt). |
| DEMO1 | L3 BD flooding | `uni/tn-DEMO1/BD-bd-vlan300-web-demo1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Graph | Contract scope wider than used | `uni/tn-Graph/brc-Grapn-contract` | Scope 'tenant' but all users are in one VRF (tn-Graph/ctx-Graph). |
| Graph | EPG without domain | `uni/tn-Graph/ap-APP/epg-EGP1` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Graph | EPG without domain | `uni/tn-Graph/ap-APP/epg-EPG2` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Graph | EPG without static path | `uni/tn-Graph/ap-APP/epg-EGP1` | No static path bindings (fvRsPathAtt). |
| Graph | EPG without static path | `uni/tn-Graph/ap-APP/epg-EPG2` | No static path bindings (fvRsPathAtt). |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| TENANT_MYTEST | L3 BD flooding | `uni/tn-TENANT_MYTEST/BD-BD1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TENANT_MYTEST | L3 BD flooding | `uni/tn-TENANT_MYTEST/BD-BD2` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-icmp` | Filter is not referenced by any contract subject. |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | L3Out without external EPG | `uni/tn-common/out-default` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| daa | EPG without static path | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | No static path bindings (fvRsPathAtt). |
| daa | L3 BD flooding | `uni/tn-daa/BD-TEST_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | L3 BD flooding | `uni/tn-iacdemo-contractors/BD-Contractors-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| Daa | Integrity daa: no critical or major faults | Critical/major faults: ['F606347 major: [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-daa/ap-ap1/epg-TEST_EPG) Tenant: daa associated with either EPG:(Ap: ap1 Epg: TEST_EPG) or Service'] |
| Heroes | Integrity Heroes: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/37 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug me', 'F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: vlan-200 :The', 'F0467 critical: |
| Oneaciapp | Integrity oneaciapp: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not ', 'F0467 critical: Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/47 due to Invalid Path Configuration,Multiple VRF configuration provided for an encap or path, '] |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |

## Tenant faults (faultInst)

By severity: warning 29, minor 10, major 1, critical 10; TCA/threshold faults (context only): 28

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| daa | major | F606347 | `uni/tn-daa/ap-ap1/epg-TEST_EPG` | [FSM:FAILED]: Addition or Deletion of Port Group for: (uni/tn-daa/ap-ap1/epg-TEST_EPG) Tenant: daa associated with either EPG:(Ap: ap1 Epg: TEST_EPG) or Services:(LDevInst:   EPpInfo:   ) on VM Contro |
| oneaciapp | critical | F0467 | `uni/tn-oneaciapp/out-OSPf` | Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain d |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-209 :There is no domain, associated with both EP |
| oneaciapp | critical | F0467 | `uni/tn-oneaciapp/out-OSPf` | Configuration failed for uni/tn-oneaciapp/out-OSPf node 102 eth1/47 due to Invalid Path Configuration,Multiple VRF configuration provided for an encap or path, debug message: multiple-ctx-configuratio |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: vlan-200 :There is no domain, associated with both EP |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/37 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 eth1/39 due to Invalid Path Configuration, debug message: invalid-path: vlan-210 :There is no domain, associated with both EP |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
