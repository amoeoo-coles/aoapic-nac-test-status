# ACI tenant logical-integrity report: 2026-10-31

## HEALTHY - 0 broken relations, 29 warnings across 14 tenants

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-31 08:22:07 AEDT)
- Generated: 2026-10-31 08:22:19 AEDT
- Scope: 14 tenants on the APIC (5 in baseline, new: aaaaa, Atul_tenant, BCC-222, DEMO1, iacdemo-contractors, iacdemo-prod, MS-T, PY-TN, Tenant_Test); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 66 tests, 66 passed, 0 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| aaaaa | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Atul_tenant | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| BCC-222 | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 2 | 1 | 0 | 2 | 0 | 94 | WARN |
| DEMO1 | NEW | 1 | 3 | 2 | 1 | 3 | 0 | 0 | 0 | 5 | 0 | 85 | WARN |
| iacdemo-contractors | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-prod | NEW | 1 | 3 | 3 | 1 | 4 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| MS-T | NEW | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| PY-TN | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| Tenant_Test | NEW | 1 | 1 | 0 | 1 | 2 | 1 | 0 | 0 | 3 | 0 | 91 | WARN |

## Broken relations (0)

None.

## Warnings (29)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Atul_tenant | Tenant empty | `uni/tn-Atul_tenant` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| BCC-222 | VRF unused | `uni/tn-BCC-222/ctx-VRF-BCC-222` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan300-web-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan301-dab-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | EPG isolated (no contracts) | `uni/tn-DEMO1/ap-app-demo1/epg-epg-vlan302-web2-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO1 | L3 BD without subnet | `uni/tn-DEMO1/BD-bd-vlan301-dab-demo1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| DEMO1 | L3 BD without subnet | `uni/tn-DEMO1/BD-bd-vlan302-web2-demo1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| MS-T | AP without EPGs | `uni/tn-MS-T/ap-MS-AP02` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| MS-T | EPG isolated (no contracts) | `uni/tn-MS-T/ap-MS-AP01/epg-MS-EPG01` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PY-TN | EPG isolated (no contracts) | `uni/tn-PY-TN/ap-PY-AP/epg-PY-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PY-TN | L3 BD without subnet | `uni/tn-PY-TN/BD-PY-BD` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| Tenant_Test | Contract consumed, never provided | `uni/tn-Tenant_Test/brc-CT_EPG` | Consumed by 1 object(s) (e.g. tn-Tenant_Test/ap-App_P_1/epg-EPG_Web) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| Tenant_Test | EPG isolated (no contracts) | `uni/tn-Tenant_Test/ap-App_P_1/epg-EPG_App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tenant_Test | L3 BD without subnet | `uni/tn-Tenant_Test/BD-BD_1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| aaaaa | Tenant empty | `uni/tn-aaaaa` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| common | Contract unused | `uni/tn-common/brc-CT-PAN-NS` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Permit-any filter | `uni/tn-common/brc-CT-PAN-NS` | Contract permits ALL traffic via tn-common/flt-FLT-PBR-IPV4 entry Any-IPV4 (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | Preferred group member without group | `uni/tn-iacdemo-prod/ctx-VRF-Prod` | 1 EPG(s) are preferred-group members but the VRF's preferred group is disabled, so the setting has no effect. | Set prefGrMemb=exclude on the EPGs, or enable the group deliberately. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 2 (e.g. tn-common/brc-CT-PAN-NS, tn-common/brc-default); vzAny contract: 1 (e.g. tn-ROR/ctx-ROR_VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
2. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 2 (e.g. tn-ROR/brc-ALLOW_ICMP_Ct, tn-ROR/brc-WEB_TO_OUTSIDE); Contract consumed, never provided: 1 (e.g. tn-Tenant_Test/brc-CT_EPG); Contract unused: 2 (e.g. tn-common/brc-CT-PAN-NS, tn-common/brc-default); EPG isolated (no contracts): 11 (e.g. tn-DEMO1/ap-app-demo1/epg-epg-vlan300-web-demo1, tn-DEMO1/ap-app-demo1/epg-epg-vlan301-dab-demo1)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
3. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 6 (e.g. tn-DEMO1/BD-bd-vlan301-dab-demo1, tn-DEMO1/BD-bd-vlan302-web2-demo1); L3 BD flooding: 4 (e.g. tn-DEMO1/BD-bd-vlan300-web-demo1, tn-ROR/BD-ROR_DB_BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
4. **Clean up unused objects** - found: Tenant empty: 3; VRF unused: 3; BD unused: 1; AP without EPGs: 2; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
5. **Add descriptions** - found: 32 of 53 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
6. **Tag ownership (annotations) for NaC** - found: 40 of 53 objects have no annotation; in use: 'orchestrator:terraform' x13.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
7. **Adopt one naming convention** - found: name styles in use: Mixed 21, lower 10, UPPER_SNAKE 22; 1 generic/VLAN/IP-style names (e.g. tn-iacdemo-prod/ap-Shop-AP/epg-test).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
8. **Bind EPGs to a domain** - found: no domain: 11, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (38)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| DEMO1 | L3 BD flooding | `uni/tn-DEMO1/BD-bd-vlan300-web-demo1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MS-T | EPG without domain | `uni/tn-MS-T/ap-MS-AP01/epg-MS-EPG01` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| MS-T | EPG without static path | `uni/tn-MS-T/ap-MS-AP01/epg-MS-EPG01` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Tenant_Test | EPG without domain | `uni/tn-Tenant_Test/ap-App_P_1/epg-EPG_App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tenant_Test | EPG without domain | `uni/tn-Tenant_Test/ap-App_P_1/epg-EPG_Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tenant_Test | EPG without static path | `uni/tn-Tenant_Test/ap-App_P_1/epg-EPG_App` | No static path bindings (fvRsPathAtt). |
| Tenant_Test | EPG without static path | `uni/tn-Tenant_Test/ap-App_P_1/epg-EPG_Web` | No static path bindings (fvRsPathAtt). |
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
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-test` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-test` | No static path bindings (fvRsPathAtt). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## Tenant faults (faultInst)

By severity: warning 4; TCA/threshold faults (context only): 4


Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
