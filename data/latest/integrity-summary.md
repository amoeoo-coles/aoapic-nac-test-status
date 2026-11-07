# ACI tenant logical-integrity report: 2026-11-08

## BROKEN RELATIONS FOUND - 6 broken, 16 warnings (3 of 9 tenants broken: RB-Tenant, Tenant_RG, VY-TN)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-08 08:18:00 AEDT)
- Generated: 2026-11-08 08:18:05 AEDT
- Scope: 9 tenants on the APIC (4 in baseline, new: LAB-TENANT, RB-Tenant, tenant_mylab, Tenant_RG, VY-TN); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 43 tests, 38 passed, 5 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| LAB-TENANT | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| RB-Tenant | NEW | 1 | 1 | 1 | 2 | 2 | 2 | 0 | 3 | 3 | 1 | 61 | BROKEN |
| tenant_mylab | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Tenant_RG | NEW | 2 | 2 | 0 | 1 | 1 | 0 | 1 | 2 | 4 | 2 | 68 | BROKEN |
| VY-TN | NEW | 1 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 87 | BROKEN |

## Broken relations (6)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-FTP` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-HTTPS` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-1410 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-pat | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (16)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| LAB-TENANT | BD VRF fallback to common | `uni/tn-LAB-TENANT/BD-LAB-BD` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. | Set the VRF explicitly on the BD. |
| LAB-TENANT | EPG isolated (no contracts) | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| LAB-TENANT | L3 BD without subnet | `uni/tn-LAB-TENANT/BD-LAB-BD` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| LAB-TENANT | VRF unused | `uni/tn-LAB-TENANT/ctx-LAB-VRF` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| RB-Tenant | BD unused | `uni/tn-RB-Tenant/BD-RB-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| RB-Tenant | L2 BD settings | `uni/tn-RB-Tenant/BD-RB-BD` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| RB-Tenant | Subnet on L2 BD | `uni/tn-RB-Tenant/BD-RB-BD` | 1 subnet(s) configured but unicast routing is disabled, so the gateway is not active. | Enable unicast routing or remove the subnets. |
| Tenant_RG | BD unused | `uni/tn-Tenant_RG/BD-L2_BD_RG` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Tenant_RG | EPG isolated (no contracts) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tenant_RG | External EPG without contracts | `uni/tn-Tenant_RG/out-rg_l3_out_ext/instP-epg_RG_EXT_ROUTED` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| Tenant_RG | L2 BD settings | `uni/tn-Tenant_RG/BD-RG_BD_EXT_L2` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| VY-TN | vzAny contract | `uni/tn-VY-TN/ctx-VY-VRF` | vzAny provides 0 / consumes 1 contract(s) (Contract2); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| tenant_mylab | Tenant empty | `uni/tn-tenant_mylab` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 6 broken relation(s) in 3 tenant(s): Critical fault F0467 (EPG deployment on path failed) (4); Contract without subjects (2)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default); vzAny contract: 1 (e.g. tn-VY-TN/ctx-VY-VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract unused: 1 (e.g. tn-common/brc-default); EPG isolated (no contracts): 2 (e.g. tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG, tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2); External EPG without contracts: 1 (e.g. tn-Tenant_RG/out-rg_l3_out_ext/instP-epg_RG_EXT_ROUTED)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 3 (e.g. tn-LAB-TENANT/BD-LAB-BD, tn-mgmt/BD-inb); Subnet on L2 BD: 1 (e.g. tn-RB-Tenant/BD-RB-BD); L2 BD settings: 2 (e.g. tn-RB-Tenant/BD-RB-BD, tn-Tenant_RG/BD-RG_BD_EXT_L2); L3 BD flooding: 1 (e.g. tn-VY-TN/BD-VY-BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 2; VRF unused: 3; BD unused: 3; AP without EPGs: 1; Filter unused: 4; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 31 of 31 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 31 of 31 objects have no annotation; in use: none.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 24, lower 3, Mixed 4; 0 generic/VLAN/IP-style names (e.g. ).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 3, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (20)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| LAB-TENANT | EPG without domain | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| LAB-TENANT | EPG without static path | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | No static path bindings (fvRsPathAtt). |
| RB-Tenant | EPG without domain | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| RB-Tenant | EPG without domain | `uni/tn-RB-Tenant/ap-WWW/epg-WWW` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| RB-Tenant | EPG without static path | `uni/tn-RB-Tenant/ap-WWW/epg-WWW` | No static path bindings (fvRsPathAtt). |
| RB-Tenant | Filter unused | `uni/tn-RB-Tenant/flt-FTP` | Filter is not referenced by any contract subject. |
| RB-Tenant | Filter unused | `uni/tn-RB-Tenant/flt-https` | Filter is not referenced by any contract subject. |
| VY-TN | EPG without static path | `uni/tn-VY-TN/ap-VY-AP/epg-EPG2` | No static path bindings (fvRsPathAtt). |
| VY-TN | L3 BD flooding | `uni/tn-VY-TN/BD-VY-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | L3Out without external EPG | `uni/tn-common/out-default` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| RB-Tenant | Integrity RB-Tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message: '] |
| RB-Tenant | Integrity contract RB-Tenant/HTTPS: subjects and filters | Contract uni/tn-RB-Tenant/brc-HTTPS has no subjects (permits nothing) |
| RB-Tenant | Integrity contract RB-Tenant/FTP: subjects and filters | Contract uni/tn-RB-Tenant/brc-FTP has no subjects (permits nothing) |
| Tenant RG | Integrity Tenant_RG: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration,Invalid VLAN Configuration, debug messa', 'F0467 critical: Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Ou'] |
| VY-TN | Integrity VY-TN: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is no'] |

## Tenant faults (faultInst)

By severity: critical 4, warning 2; TCA/threshold faults (context only): 2

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| Tenant_RG | critical | F0467 | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the |
| VY-TN | critical | F0467 | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain |
| Tenant_RG | critical | F0467 | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-1410 :Either the  |
| RB-Tenant | critical | F0467 | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message:  |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
