# ACI tenant logical-integrity report: 2026-10-27

## BROKEN RELATIONS FOUND - 10 broken, 35 warnings (2 of 11 tenants broken: Pune-Lab, TN-DEDUP-LAB)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-27 08:16:45 AEDT)
- Generated: 2026-10-27 08:16:53 AEDT
- Scope: 11 tenants on the APIC (6 in baseline, new: DEMO, Pune-Lab, TF_LAB_SAMAN, TN-POC-LN, TN-PROD); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 122 tests, 121 passed, 1 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 7 | 1 | 0 | 6 | 0 | 82 | WARN |
| DEMO | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| oneaciapp | yes | 2 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 3 | 0 | 91 | WARN |
| Pune-Lab | NEW | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 2 | 0 | 84 | BROKEN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| TF_LAB_SAMAN | NEW | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TN-DEDUP-LAB | yes | 1 | 1 | 1 | 1 | 9 | 21 | 2 | 9 | 5 | 0 | 0 | BROKEN |
| TN-POC-LN | NEW | 1 | 5 | 4 | 1 | 4 | 5 | 1 | 0 | 10 | 0 | 70 | WARN |
| TN-PROD | NEW | 1 | 3 | 3 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 100 | HEALTHY |

## Broken relations (10)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Pune-Lab | Subject without filters | `uni/tn-Pune-Lab/brc-Pune-Ping-allow/subj-HTTPS-SERVICE` | Contract subject has no filter, so it permits nothing. | Attach specific filters to the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-BACKUP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F0758: Service graph  for tenant TN-DEDUP-LAB could not be instantiated. Info: Unable to find LDevCtx for node:); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-MGMT-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-WEB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-LDAP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-SMTP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-WEB-APP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |

## Warnings (35)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| DEMO | EPG isolated (no contracts) | `uni/tn-DEMO/ap-DEMO_prod_AP/epg-DEMO_prod_web1_201_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEMO | L2 BD settings | `uni/tn-DEMO/BD-DEMO_prod_web1_BD` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| Pune-Lab | Contract unused | `uni/tn-Pune-Lab/brc-Pune-Ping-allow` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Pune-Lab | EPG isolated (no contracts) | `uni/tn-Pune-Lab/ap-APP-BD/epg-EPG-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| TF_LAB_SAMAN | BD unused | `uni/tn-TF_LAB_SAMAN/BD-BD_10` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-APP-DB-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-APP-DB: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-APP-DB-FW (keep tn-TN-DEDUP-LAB/brc-C-APP-DB). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-DNS: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-DNS-FW (keep tn-TN-DEDUP-LAB/brc-C-DNS). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-MONITORING: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD (keep tn-TN-DEDUP-LAB/brc-C-MONITORING). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-NTP-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-NTP: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-NTP-FW (keep tn-TN-DEDUP-LAB/brc-C-NTP). |
| TN-DEDUP-LAB | vzAny contract | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` | vzAny provides 0 / consumes 2 contract(s) (C-SMTP, C-SMTP-FW); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| TN-POC-LN | BD unused | `uni/tn-TN-POC-LN/BD-BD-FW-POC` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/LDevInst-[uni/tn-TN-POC-LN/lDevVip-DEV-POC-FW` | For tenant TN-POC-LN, application profile , deployment of application EPG  failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP` | For tenant TN-POC-LN, application profile AP-POC-SHOP, deployment of application EPG EPG-POC-APP failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB` | For tenant TN-POC-LN, application profile AP-POC-SHOP, deployment of application EPG EPG-POC-DB failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY` | For tenant TN-POC-LN, application profile AP-POC-SHOP, deployment of application EPG EPG-POC-LEGACY failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB` | For tenant TN-POC-LN, application profile AP-POC-SHOP, deployment of application EPG EPG-POC-WEB failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/l2out-L2O-POC-LEGACY/instP-EXT-POC-LEGACY` | For tenant TN-POC-LN, outside L2O-POC-LEGACY, deployment of external EPG EXT-POC-LEGACY failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Config fault F1298 | `uni/tn-TN-POC-LN/out-L3O-POC-WAN/instP-EXT-POC-WAN` | For tenant TN-POC-LN, outside L3O-POC-WAN, deployment of external EPG EXT-POC-WAN failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| TN-POC-LN | Permit-any filter | `uni/tn-TN-POC-LN/brc-CON-POC-LEGACY` | Contract permits ALL traffic via tn-TN-POC-LN/flt-FLT-POC-ANY entry any (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| TN-POC-LN | vzAny contract | `uni/tn-TN-POC-LN/ctx-VRF-POC-PROD` | vzAny provides 1 / consumes 1 contract(s) (CON-POC-ICMP); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| common | Contract consumed, never provided | `uni/tn-common/brc-ct-DNS-SHARED` | Consumed by 3 object(s) (e.g. tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| common | Contract consumed, never provided | `uni/tn-common/brc-ct-MONITORING-SHARED` | Consumed by 3 object(s) (e.g. tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| common | Contract consumed, never provided | `uni/tn-common/brc-ct-NTP-SHARED` | Consumed by 3 object(s) (e.g. tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| common | Contract unused | `uni/tn-common/brc-power_up` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-sql` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | Config fault F1298 | `uni/tn-mgmt/mgmtp-default/oob-default` | For tenant mgmt, management profile default, deployment of out-band EPG default failed on node 102. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Contract unused | `uni/tn-oneaciapp/brc-OneAci_Web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-OneAciApp_AP/epg-EPG1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| oneaciapp | VRF unused | `uni/tn-oneaciapp/ctx-VRF1` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 10 broken relation(s) in 2 tenant(s): Contract service graph not instantiated (9); Subject without filters (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 2 (e.g. tn-TN-POC-LN/brc-CON-POC-LEGACY, tn-common/brc-default); vzAny contract: 3 (e.g. tn-ROR/ctx-ROR_VRF, tn-TN-DEDUP-LAB/ctx-VRF-LAB)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 2 (e.g. tn-ROR/brc-ALLOW_ICMP_Ct, tn-ROR/brc-WEB_TO_OUTSIDE); Contract consumed, never provided: 3 (e.g. tn-common/brc-ct-DNS-SHARED, tn-common/brc-ct-MONITORING-SHARED); Contract unused: 6 (e.g. tn-Pune-Lab/brc-Pune-Ping-allow, tn-common/brc-power_up); EPG isolated (no contracts): 3 (e.g. tn-DEMO/ap-DEMO_prod_AP/epg-DEMO_prod_web1_201_EPG, tn-Pune-Lab/ap-APP-BD/epg-EPG-Web); Duplicate contract: 4 (e.g. tn-TN-DEDUP-LAB/brc-C-APP-DB-FW, tn-TN-DEDUP-LAB/brc-C-DNS-FW)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 2 (e.g. tn-mgmt/BD-inb, tn-common/BD-default); L2 BD settings: 1 (e.g. tn-DEMO/BD-DEMO_prod_web1_BD); L3 BD flooding: 7 (e.g. tn-Pune-Lab/BD-Pune-BD, tn-ROR/BD-ROR_DB_BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: VRF unused: 3; BD unused: 4; AP without EPGs: 1; Filter unused: 4; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 87 of 126 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 40 of 126 objects have no annotation; in use: 'orchestrator:ansible' x66, 'orchestrator:terraform' x20.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 86, Mixed 30, lower 10; 0 generic/VLAN/IP-style names (e.g. ).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 16, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (62)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| DEMO | EPG without domain | `uni/tn-DEMO/ap-DEMO_prod_AP/epg-DEMO_prod_web1_201_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DEMO | EPG without static path | `uni/tn-DEMO/ap-DEMO_prod_AP/epg-DEMO_prod_web1_201_EPG` | No static path bindings (fvRsPathAtt). |
| Pune-Lab | EPG without domain | `uni/tn-Pune-Lab/ap-APP-BD/epg-EPG-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Pune-Lab | EPG without static path | `uni/tn-Pune-Lab/ap-APP-BD/epg-EPG-Web` | No static path bindings (fvRsPathAtt). |
| Pune-Lab | Filter unused | `uni/tn-Pune-Lab/flt-ICMP` | Filter is not referenced by any contract subject. |
| Pune-Lab | L3 BD flooding | `uni/tn-Pune-Lab/BD-Pune-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP` | EPG consumes 'ct-MONITORING-SHARED' resolved to tn-common/brc-ct-MONITORING-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP` | EPG consumes 'ct-NTP-SHARED' resolved to tn-common/brc-ct-NTP-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP` | EPG consumes 'ct-DNS-SHARED' resolved to tn-common/brc-ct-DNS-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-DB` | EPG consumes 'ct-MONITORING-SHARED' resolved to tn-common/brc-ct-MONITORING-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-DB` | EPG consumes 'ct-DNS-SHARED' resolved to tn-common/brc-ct-DNS-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-DB` | EPG consumes 'ct-NTP-SHARED' resolved to tn-common/brc-ct-NTP-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-WEB` | EPG consumes 'ct-DNS-SHARED' resolved to tn-common/brc-ct-DNS-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-WEB` | EPG consumes 'ct-MONITORING-SHARED' resolved to tn-common/brc-ct-MONITORING-SHARED. |
| TN-PROD | EPG uses common contract | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-WEB` | EPG consumes 'ct-NTP-SHARED' resolved to tn-common/brc-ct-NTP-SHARED. |
| TN-PROD | EPG without domain | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROD | EPG without domain | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROD | EPG without domain | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROD | EPG without static path | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-APP` | No static path bindings (fvRsPathAtt). |
| TN-PROD | EPG without static path | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-DB` | No static path bindings (fvRsPathAtt). |
| TN-PROD | EPG without static path | `uni/tn-TN-PROD/ap-AP-DEMO-CRM/epg-EPG-DEMO-CRM-WEB` | No static path bindings (fvRsPathAtt). |
| TN-PROD | L3 BD flooding | `uni/tn-TN-PROD/BD-BD-DEMO-CRM-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| TN-PROD | L3 BD flooding | `uni/tn-TN-PROD/BD-BD-DEMO-CRM-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| TN-PROD | L3 BD flooding | `uni/tn-TN-PROD/BD-BD-DEMO-CRM-WEB` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | BD unused | `uni/tn-common/BD-default` | No EPG is attached to this bridge domain. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-icmp` | Filter is not referenced by any contract subject. |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | L3Out without external EPG | `uni/tn-common/out-default` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-OneAciApp_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| Pune-Lab | Integrity contract Pune-Lab/Pune-Ping-allow: subjects and filters | Subjects without filters: ['uni/tn-Pune-Lab/brc-Pune-Ping-allow/subj-HTTPS-SERVICE'] |

## Tenant faults (faultInst)

By severity: minor 49; TCA/threshold faults (context only): 0


Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
