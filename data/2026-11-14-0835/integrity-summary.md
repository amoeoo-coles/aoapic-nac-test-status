# ACI tenant logical-integrity report: 2026-11-14

## BROKEN RELATIONS FOUND - 12 broken, 7 warnings (2 of 7 tenants broken: Heroes, SnV)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-14 08:35:26 AEDT)
- Generated: 2026-11-14 08:35:34 AEDT
- Scope: 7 tenants on the APIC (7 in baseline, new: none); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 57 tests, 55 passed, 2 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 4 | 0 | 14 | 60 | BROKEN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 8 | 1 | 36 | 17 | BROKEN |

## Broken relations (12)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 101 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (7)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| mgmt | Config fault F0523 | `uni/tn-mgmt/mgmtp-default/inb-InBand-Mgt` | Configuration failed for EPG InBand-Mgt due to Not Associated With Management Zone | Fix the EPG's dependency named in the fault (BD/VRF, management zone, etc.). |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 12 broken relation(s) in 2 tenant(s): Critical fault F0467 (EPG deployment on path failed) (12)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default); vzAny contract: 1 (e.g. tn-ROR/ctx-ROR_VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 3 (e.g. tn-ROR/brc-ALLOW_ICMP_Ct, tn-ROR/brc-WEB_TO_OUTSIDE); Contract unused: 1 (e.g. tn-common/brc-default)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 2 (e.g. tn-mgmt/BD-inb, tn-common/BD-default); L3 BD flooding: 2 (e.g. tn-ROR/BD-ROR_DB_BD, tn-ROR/BD-ROR_WEB_BD)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 1; VRF unused: 2; BD unused: 1; AP without EPGs: 1; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 47 of 47 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 47 of 47 objects have no annotation; in use: none.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 22, UPPER_SNAKE 8, lower 17; 0 generic/VLAN/IP-style names (e.g. ).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 2, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (25)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
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

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| Heroes | Integrity Heroes: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interfac', 'F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interfac', 'F0467 critical: |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not ', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not ', 'F0467 critical: |

## Tenant faults (faultInst)

By severity: minor 1, critical 50; TCA/threshold faults (context only): 0

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 101 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a doma |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-125 :Either the EpG is not associa |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-127 :Either the EpG is not asso |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-123 :Either the EpG is not associ |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-121 :Either the EpG is not a |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/out-Heroes_external_corporate` | Configuration failed for uni/tn-Heroes/out-Heroes_external_corporate node 102 eth1/47 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a doma |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
