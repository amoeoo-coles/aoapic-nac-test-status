# ACI tenant logical-integrity report: 2026-10-26

## HEALTHY - 0 broken relations, 8 warnings across 5 tenants

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-26 08:07:40 AEDT)
- Generated: 2026-10-26 08:07:43 AEDT
- Scope: 5 tenants on the APIC (4 in baseline, new: TF_LAB_SAMAN); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 18 tests, 18 passed, 0 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 3 | 0 | 91 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TF_LAB_SAMAN | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |

## Broken relations (0)

None.

## Warnings (8)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| TF_LAB_SAMAN | BD unused | `uni/tn-TF_LAB_SAMAN/BD-BD_10` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TF_LAB_SAMAN | L3 BD without subnet | `uni/tn-TF_LAB_SAMAN/BD-BD_10` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| common | Contract unused | `uni/tn-common/brc-power_up` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-sql` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
2. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract unused: 4 (e.g. tn-common/brc-power_up, tn-common/brc-sql)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
3. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 3 (e.g. tn-TF_LAB_SAMAN/BD-BD_10, tn-mgmt/BD-inb)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
4. **Clean up unused objects** - found: Tenant empty: 1; VRF unused: 2; BD unused: 3; AP without EPGs: 1; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
5. **Add descriptions** - found: 11 of 11 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
6. **Tag ownership (annotations) for NaC** - found: 9 of 11 objects have no annotation; in use: 'orchestrator:terraform' x2.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
7. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 2, lower 9; 0 generic/VLAN/IP-style names (e.g. ).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.

## Informational (13)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
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

## Tenant faults (faultInst)

By severity: ; TCA/threshold faults (context only): 0


Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
