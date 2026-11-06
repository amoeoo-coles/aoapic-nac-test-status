# ACI tenant logical-integrity report: 2026-11-07

## BROKEN RELATIONS FOUND - 8 broken, 19 warnings (4 of 12 tenants broken: MOJ_TENANT, PSCF, SnV, oneaciapp)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-07 08:20:19 AEDT)
- Generated: 2026-11-07 08:20:31 AEDT
- Scope: 12 tenants on the APIC (6 in baseline, new: iacdemo-contractors, iacdemo-prod, MOJ_TENANT, PSCF, Tai_API_Tenant, Tai_Tenant); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 91 tests, 87 passed, 4 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| iacdemo-contractors | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-prod | NEW | 1 | 4 | 4 | 2 | 5 | 0 | 0 | 0 | 5 | 0 | 85 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| MOJ_TENANT | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 4 | 87 | BROKEN |
| oneaciapp | yes | 0 | 1 | 1 | 1 | 2 | 0 | 0 | 2 | 3 | 3 | 71 | BROKEN |
| PSCF | NEW | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 2 | 1 | 84 | BROKEN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 1 | 4 | 57 | BROKEN |
| Tai_API_Tenant | NEW | 1 | 1 | 1 | 1 | 3 | 1 | 0 | 0 | 1 | 0 | 97 | WARN |
| Tai_Tenant | NEW | 1 | 1 | 1 | 1 | 3 | 1 | 0 | 0 | 1 | 0 | 97 | WARN |

## Broken relations (8)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| MOJ_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 102 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| PSCF | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| oneaciapp | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (19)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| MOJ_TENANT | External EPG without contracts | `uni/tn-MOJ_TENANT/out-MOJ_L3out/instP-EEPG_LRout` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| PSCF | EPG isolated (no contracts) | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PSCF | VRF unused | `uni/tn-PSCF/ctx-VRF_PSCF` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| Tai_API_Tenant | EPG isolated (no contracts) | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tai_Tenant | EPG isolated (no contracts) | `uni/tn-Tai_Tenant/ap-Tai_App/epg-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | EPG isolated (no contracts) | `uni/tn-mgmt/ap-MOJ_APP_ESXiMGMT/epg-MOJ_EPG_ESXi_MGMT` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | BD VRF fallback to common | `uni/tn-oneaciapp/BD-TEST` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. | Set the VRF explicitly on the BD. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 8 broken relation(s) in 4 tenant(s): Critical fault F0467 (EPG deployment on path failed) (8)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 1 (e.g. tn-SnV/brc-web); Contract unused: 1 (e.g. tn-common/brc-default); EPG isolated (no contracts): 13 (e.g. tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING, tn-Tai_API_Tenant/ap-Tai_App/epg-DB); External EPG without contracts: 1 (e.g. tn-MOJ_TENANT/out-MOJ_L3out/instP-EEPG_LRout)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 2 (e.g. tn-mgmt/BD-inb, tn-common/BD-default); L3 BD flooding: 5 (e.g. tn-Tai_Tenant/BD-Tai_BD, tn-iacdemo-contractors/BD-Contractors-BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: VRF unused: 3; BD unused: 1; AP without EPGs: 1; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 64 of 79 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 62 of 79 objects have no annotation; in use: 'orchestrator:terraform' x17.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 49, UPPER_SNAKE 10, lower 20; 4 generic/VLAN/IP-style names (e.g. tn-oneaciapp/BD-TEST, tn-oneaciapp/ap-TEST, tn-oneaciapp/ap-TEST/epg-TEST1, tn-oneaciapp/ap-TEST/epg-TEST2).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 17, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (55)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| PSCF | EPG without domain | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PSCF | EPG without static path | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | No static path bindings (fvRsPathAtt). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| Tai_API_Tenant | EPG without domain | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_API_Tenant | EPG without domain | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_API_Tenant | EPG without domain | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_API_Tenant | EPG without static path | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-App` | No static path bindings (fvRsPathAtt). |
| Tai_API_Tenant | EPG without static path | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-DB` | No static path bindings (fvRsPathAtt). |
| Tai_API_Tenant | EPG without static path | `uni/tn-Tai_API_Tenant/ap-Tai_App/epg-Web` | No static path bindings (fvRsPathAtt). |
| Tai_Tenant | EPG without domain | `uni/tn-Tai_Tenant/ap-Tai_App/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_Tenant | EPG without domain | `uni/tn-Tai_Tenant/ap-Tai_App/epg-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_Tenant | EPG without domain | `uni/tn-Tai_Tenant/ap-Tai_App/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tai_Tenant | EPG without static path | `uni/tn-Tai_Tenant/ap-Tai_App/epg-App` | No static path bindings (fvRsPathAtt). |
| Tai_Tenant | EPG without static path | `uni/tn-Tai_Tenant/ap-Tai_App/epg-DB` | No static path bindings (fvRsPathAtt). |
| Tai_Tenant | EPG without static path | `uni/tn-Tai_Tenant/ap-Tai_App/epg-Web` | No static path bindings (fvRsPathAtt). |
| Tai_Tenant | L3 BD flooding | `uni/tn-Tai_Tenant/BD-Tai_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-icmp` | Filter is not referenced by any contract subject. |
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
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | L3 BD flooding | `uni/tn-iacdemo-prod/BD-Booking-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| mgmt | EPG without domain | `uni/tn-mgmt/ap-MOJ_APP_ESXiMGMT/epg-MOJ_EPG_ESXi_MGMT` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| mgmt | EPG without static path | `uni/tn-mgmt/ap-MOJ_APP_ESXiMGMT/epg-MOJ_EPG_ESXi_MGMT` | No static path bindings (fvRsPathAtt). |
| mgmt | L3 BD flooding | `uni/tn-mgmt/BD-EsxiMGMT` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-TEST` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| MOJ TENANT | Integrity MOJ_TENANT: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 101 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: inval', 'F0467 critical: Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 101 MOJ_VPC_FW2 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: inval', 'F0467 critical: |
| Oneaciapp | Integrity oneaciapp: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message: ', 'F0467 critical: Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message: '] |
| PSCF | Integrity PSCF: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message: '] |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |

## Tenant faults (faultInst)

By severity: warning 28, critical 12; TCA/threshold faults (context only): 28

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| oneaciapp | critical | F0467 | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message:  |
| MOJ_TENANT | critical | F0467 | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 102 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not |
| MOJ_TENANT | critical | F0467 | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 102 MOJ_VPC_FW2 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |
| oneaciapp | critical | F0467 | `uni/tn-oneaciapp/ap-TEST/epg-TEST2` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST2 due to VRF Not Present, debug message:  |
| oneaciapp | critical | F0467 | `uni/tn-oneaciapp/ap-TEST/epg-TEST1` | Configuration failed for uni/tn-oneaciapp/ap-TEST/epg-TEST1 due to VRF Not Present, debug message:  |
| PSCF | critical | F0467 | `uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING` | Configuration failed for uni/tn-PSCF/ap-ANP_TESTING/epg-USEG_TESTING due to VRF Not Present, debug message:  |
| MOJ_TENANT | critical | F0467 | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 101 MOJ_VPC_FW1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not |
| MOJ_TENANT | critical | F0467 | `uni/tn-MOJ_TENANT/out-MOJ_L3out` | Configuration failed for uni/tn-MOJ_TENANT/out-MOJ_L3out node 101 MOJ_VPC_FW2 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-255 :Either the EpG is not |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
