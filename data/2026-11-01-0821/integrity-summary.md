# ACI tenant logical-integrity report: 2026-11-01

## BROKEN RELATIONS FOUND - 4 broken, 20 warnings (1 of 10 tenants broken: SnV)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-01 08:21:24 AEDT)
- Generated: 2026-11-01 08:21:37 AEDT
- Scope: 10 tenants on the APIC (6 in baseline, new: Ansible-PROD, Ansible-QA, daa, TENANT_MYTEST); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 61 tests, 60 passed, 1 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Ansible-PROD | NEW | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| Ansible-QA | NEW | 0 | 0 | 0 | 2 | 5 | 0 | 0 | 0 | 10 | 0 | 70 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| daa | NEW | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 1 | 4 | 57 | BROKEN |
| TENANT_MYTEST | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |

## Broken relations (4)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (20)

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
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TENANT_MYTEST | Tenant empty | `uni/tn-TENANT_MYTEST` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| daa | AP without EPGs | `uni/tn-daa/ap-ap1` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 4 broken relation(s) in 1 tenant(s): Critical fault F0467 (EPG deployment on path failed) (4)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 1 (e.g. tn-SnV/brc-web); Contract unused: 1 (e.g. tn-common/brc-default); EPG isolated (no contracts): 7 (e.g. tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-1-0, tn-Ansible-PROD/ap-Hypervisors/epg-Subnet-192-168-2-0)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 2 (e.g. tn-mgmt/BD-inb, tn-common/BD-default)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 2; VRF unused: 2; BD unused: 1; AP without EPGs: 2; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 45 of 45 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 35 of 45 objects have no annotation; in use: 'orchestrator:ansible' x10.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 27, lower 18; 0 generic/VLAN/IP-style names (e.g. ).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 7, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (32)

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
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
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
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |

## Tenant faults (faultInst)

By severity: warning 28, critical 4; TCA/threshold faults (context only): 28

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
