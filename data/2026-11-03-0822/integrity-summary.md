# ACI tenant logical-integrity report: 2026-11-03

## BROKEN RELATIONS FOUND - 5 broken, 33 warnings (2 of 11 tenants broken: SnV, TenantAPPC3750)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-03 08:23:32 AEDT)
- Generated: 2026-11-03 08:23:57 AEDT
- Scope: 11 tenants on the APIC (6 in baseline, new: Bank-Demo, iacdemo-contractors, iacdemo-prod, SIS_PROD, TenantAPPC3750); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 87 tests, 85 passed, 2 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Bank-Demo | NEW | 1 | 1 | 1 | 1 | 3 | 3 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 5 | 1 | 0 | 1 | 0 | 97 | WARN |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 0 | 4 | 0 | 88 | WARN |
| iacdemo-contractors | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-prod | NEW | 1 | 5 | 5 | 1 | 4 | 0 | 0 | 0 | 5 | 0 | 85 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| SIS_PROD | NEW | 1 | 2 | 0 | 1 | 2 | 0 | 1 | 0 | 6 | 0 | 82 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 9 | 4 | 33 | BROKEN |
| TenantAPPC3750 | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 1 | 2 | 1 | 84 | BROKEN |

## Broken relations (5)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TenantAPPC3750 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not have | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (33)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Bank-Demo | Contract provided, never consumed | `uni/tn-Bank-Demo/brc-Client-to-Web` | Provided by 1 object(s) (e.g. tn-Bank-Demo/ap-Core-Banking/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| Heroes | Config fault F1298 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | For tenant Heroes, application profile Save_The_Planet, deployment of application EPG app failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Heroes | Config fault F1298 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | For tenant Heroes, application profile Save_The_Planet, deployment of application EPG db failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Heroes | Config fault F1298 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | For tenant Heroes, application profile Save_The_Planet, deployment of application EPG web failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Heroes | Config fault F1298 | `uni/tn-Heroes/out-Heroes_external_corporate/instP-Heroes_default` | For tenant Heroes, outside Heroes_external_corporate, deployment of external EPG Heroes_default failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SIS_PROD | EPG isolated (no contracts) | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-10` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| SIS_PROD | EPG isolated (no contracts) | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-16` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| SIS_PROD | L3 BD without subnet | `uni/tn-SIS_PROD/BD-vlan-10` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| SIS_PROD | L3 BD without subnet | `uni/tn-SIS_PROD/BD-vlan-16` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| SIS_PROD | L3Out VRF fallback to common | `uni/tn-SIS_PROD/out-SIS` | L3Out has no VRF name and falls back to tn-common/ctx-default. | Set the VRF explicitly. |
| SIS_PROD | L3Out without external EPG | `uni/tn-SIS_PROD/out-SIS` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. | Add an external EPG with the external subnets and contracts. |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Chaos/epg-Database` | For tenant SnV, application profile Chaos, deployment of application EPG Database failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Chaos/epg-Web` | For tenant SnV, application profile Chaos, deployment of application EPG Web failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | For tenant SnV, application profile Evolution_X, deployment of application EPG Database failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | For tenant SnV, application profile Evolution_X, deployment of application EPG Web failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Power_Up/epg-Database` | For tenant SnV, application profile Power_Up, deployment of application EPG Database failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Power_Up/epg-Web` | For tenant SnV, application profile Power_Up, deployment of application EPG Web failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Rescue/epg-Database` | For tenant SnV, application profile Rescue, deployment of application EPG Database failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Config fault F1298 | `uni/tn-SnV/ap-Rescue/epg-Web` | For tenant SnV, application profile Rescue, deployment of application EPG Web failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TenantAPPC3750 | EPG isolated (no contracts) | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TenantAPPC3750 | EPG isolated (no contracts) | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN2` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| common | Contract unused | `uni/tn-common/brc-testtt` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | BD unused | `uni/tn-iacdemo-prod/BD-jols-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Cache` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 5 broken relation(s) in 2 tenant(s): Critical fault F0467 (EPG deployment on path failed) (5)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 2 (e.g. tn-Bank-Demo/brc-Client-to-Web, tn-SnV/brc-web); Contract unused: 2 (e.g. tn-common/brc-testtt, tn-common/brc-default); EPG isolated (no contracts): 10 (e.g. tn-SIS_PROD/ap-SIS_AP/epg-EPG-10, tn-SIS_PROD/ap-SIS_AP/epg-EPG-16)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 4 (e.g. tn-SIS_PROD/BD-vlan-10, tn-SIS_PROD/BD-vlan-16); L3 BD flooding: 3 (e.g. tn-TenantAPPC3750/BD-BDN, tn-iacdemo-contractors/BD-Contractors-BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 1; VRF unused: 2; BD unused: 3; AP without EPGs: 1; Filter unused: 2; L3Out without external EPG: 2  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 58 of 75 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 59 of 75 objects have no annotation; in use: 'orchestrator:terraform' x16.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 42, UPPER_SNAKE 10, lower 23; 1 generic/VLAN/IP-style names (e.g. tn-common/brc-testtt).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 13, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (46)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Bank-Demo | EPG without domain | `uni/tn-Bank-Demo/ap-Core-Banking/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Bank-Demo | EPG without domain | `uni/tn-Bank-Demo/ap-Core-Banking/epg-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Bank-Demo | EPG without domain | `uni/tn-Bank-Demo/ap-Core-Banking/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Bank-Demo | EPG without static path | `uni/tn-Bank-Demo/ap-Core-Banking/epg-App` | No static path bindings (fvRsPathAtt). |
| Bank-Demo | EPG without static path | `uni/tn-Bank-Demo/ap-Core-Banking/epg-DB` | No static path bindings (fvRsPathAtt). |
| Bank-Demo | EPG without static path | `uni/tn-Bank-Demo/ap-Core-Banking/epg-Web` | No static path bindings (fvRsPathAtt). |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| SIS_PROD | EPG without domain | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-10` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| SIS_PROD | EPG without domain | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-16` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| SIS_PROD | EPG without static path | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-10` | No static path bindings (fvRsPathAtt). |
| SIS_PROD | EPG without static path | `uni/tn-SIS_PROD/ap-SIS_AP/epg-EPG-16` | No static path bindings (fvRsPathAtt). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| TenantAPPC3750 | EPG without domain | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TenantAPPC3750 | EPG without domain | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN2` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TenantAPPC3750 | EPG without static path | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN2` | No static path bindings (fvRsPathAtt). |
| TenantAPPC3750 | L3 BD flooding | `uni/tn-TenantAPPC3750/BD-BDN` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | L3 BD flooding | `uni/tn-iacdemo-contractors/BD-Contractors-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Cache` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Cache` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | L3 BD flooding | `uni/tn-iacdemo-prod/BD-jols-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |
| TenantAPPC3750 | Integrity TenantAPPC3750: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug mess'] |

## Tenant faults (faultInst)

By severity: minor 13, warning 28, critical 5; TCA/threshold faults (context only): 28

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| TenantAPPC3750 | critical | F0467 | `uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN` | Configuration failed for uni/tn-TenantAPPC3750/ap-AppN/epg-EPGN node 102 IPG_VPC_C3750N due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10 :STP Segment  |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
