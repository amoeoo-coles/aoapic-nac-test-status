# ACI tenant logical-integrity report: 2026-10-22

## BROKEN RELATIONS FOUND - 25 broken, 39 warnings (5 of 22 tenants broken: MUHC, SnV, TN-DEDUP-LAB, UT, prod)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-22 11:05:56 AEDT)
- Generated: 2026-10-22 11:06:58 AEDT
- Scope: 22 tenants on the APIC (16 in baseline, new: js_10018, js_10118, Production_Tenant, Production_Tenant2, Production_Tenant22, tn_TEST1); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 168 tests, 160 passed, 8 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 1 | 0 | 1 | 0 | 97 | WARN |
| js_10018 | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| js_10118 | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 88 | WARN |
| MUHC | yes | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 7 | 0 | 0 | 30 | BROKEN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| OS1 | yes | 1 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| prod | yes | 1 | 4 | 4 | 1 | 3 | 1 | 1 | 3 | 3 | 3 | 61 | BROKEN |
| Production_Tenant | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| Production_Tenant2 | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| Production_Tenant22 | NEW | 1 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 1 | 4 | 57 | BROKEN |
| TEST | yes | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TEST-ABC1 | yes | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| Test-Tenant | yes | 1 | 1 | 4 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TN-DEDUP-LAB | yes | 1 | 1 | 1 | 1 | 9 | 20 | 2 | 10 | 4 | 0 | 0 | BROKEN |
| tn-MGK | yes | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 94 | WARN |
| tn_TEST1 | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| UT | yes | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 3 | 1 | 81 | BROKEN |

## Broken relations (25)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2701_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended. | Create L3Out 'LEGACY_L3OUT' or remove the BD-to-L3Out association. |
| MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2701_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'LEGACY_VRF' in MUHC (or common), or point the BD to an existing VRF. |
| MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2780_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'LEGACY_VRF' in MUHC (or common), or point the BD to an existing VRF. |
| MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` | EPG -> tn-MUHC/BD-VLAN_2701_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present'). | Fix the VRF of tn-MUHC/BD-VLAN_2701_BD first; the EPG recovers automatically. |
| MUHC | EPG chain broken (BD has no VRF) | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` | EPG -> tn-MUHC/BD-VLAN_2780_BD resolves, but that BD's VRF 'LEGACY_VRF' is missing, so the EPG cannot be deployed (APIC fault F0523 'Context Not present'). | Fix the VRF of tn-MUHC/BD-VLAN_2780_BD first; the EPG recovers automatically. |
| MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target). | Create domain uni/phys-LEGACY_SRVF_PHY (with VLAN pool/AAEP) or associate an existing one. |
| MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target). | Create domain uni/phys-LEGACY_SRVF_PHY (with VLAN pool/AAEP) or associate an existing one. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-APP-DB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-BACKUP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-MGMT-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-WEB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-LDAP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-SMTP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-WEB-APP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped. | Create the device selection policy (vnsLDevCtx) for this contract/graph/node, or detach the graph from the subject. |
| UT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-UT/ap-UAP/epg-USER_EPG` | Configuration failed for uni/tn-UT/ap-UAP/epg-USER_EPG node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: vlan-101 :There is no domain, associated with both EPG and Port, that has required VLAN; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| prod | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-prod/ap-vlans/epg-vlan100` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan100 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| prod | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-prod/ap-vlans/epg-vlan101` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan101 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| prod | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-prod/ap-vlans/epg-vlan102` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan102 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (39)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| OS1 | BD unused | `uni/tn-OS1/BD-VLAN1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| OS1 | EPG isolated (no contracts) | `uni/tn-OS1/ap-APP-Prod/epg-APP-WEB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Production_Tenant | EPG isolated (no contracts) | `uni/tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Production_Tenant | L3 BD without subnet | `uni/tn-Production_Tenant/BD-Prod_BD_100` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Production_Tenant2 | EPG isolated (no contracts) | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2/epg-Web_EPG2` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Production_Tenant2 | L3 BD without subnet | `uni/tn-Production_Tenant2/BD-Prod_BD_200` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Production_Tenant22 | EPG isolated (no contracts) | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG22` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Production_Tenant22 | EPG isolated (no contracts) | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG222` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Production_Tenant22 | L3 BD without subnet | `uni/tn-Production_Tenant22/BD-Prod_BD_300` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TEST | EPG isolated (no contracts) | `uni/tn-TEST/ap-TEST_AAEP/epg-TESTEPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TEST-ABC1 | BD unused | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TEST-ABC1 | BD unused | `uni/tn-TEST-ABC1/BD-BD-L2-TESTABC1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-DNS: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-DNS-FW (keep tn-TN-DEDUP-LAB/brc-C-DNS). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-MONITORING: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD (keep tn-TN-DEDUP-LAB/brc-C-MONITORING). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-NTP-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-NTP: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-NTP-FW (keep tn-TN-DEDUP-LAB/brc-C-NTP). |
| TN-DEDUP-LAB | vzAny contract | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` | vzAny provides 0 / consumes 2 contract(s) (C-SMTP, C-SMTP-FW); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| Test-Tenant | EPG isolated (no contracts) | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| UT | BD unused | `uni/tn-UT/BD-FBD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| UT | Config fault F3891 | `uni/tn-UT/ctx-FWVRF/leakroutes/leakintsubnet-[172.16.100.1/24]` | Configuration failed for Inter-VRF Leaked Subnet (EPG/BD in case of APIC, cloudSubnet/CloudCidr in case of CAPIC) 172.16.100.1/24 under VRF FWVRF Tenant UT, due to Subnet does not match any EPG/BD Subnets in the VRF. An Inter-VRF Leaked Subnet must be equal to an EPG/BD Subnet or be a subset of an E | The leaked subnet must match an existing BD/EPG subnet in the VRF; correct the prefix or remove the leak. |
| UT | L3 BD without subnet | `uni/tn-UT/BD-FBD` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| infra | Relation fallback F0756 | `uni/tn-infra/out-IPN/lnodep-IPN/lifp-IPN/ospfIfP/rsIfPol` | Could not resolve the target ospfIfPol-external-isn-switches to form a named relationship. Using a default target uni/tn-common/ospfIfPol-default instead | Create the named target policy (or correct its name); the object is silently using a tn-common default. |
| js_10018 | Tenant empty | `uni/tn-js_10018` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| js_10118 | BD unused | `uni/tn-js_10118/BD-prod_bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| js_10118 | L3 BD without subnet | `uni/tn-js_10118/BD-prod_bd` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| mgmt | Config fault F0523 | `uni/tn-mgmt/mgmtp-default/inb-inb` | Configuration failed for EPG inb due to Not Associated With Management Zone | Fix the EPG's dependency named in the fault (BD/VRF, management zone, etc.). |
| mgmt | Config fault F1298 | `uni/tn-mgmt/mgmtp-default/oob-oob` | For tenant mgmt, management profile default, deployment of out-band EPG oob failed on node 1102. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| mgmt | Contract provided, never consumed | `uni/tn-mgmt/brc-permit-to-inb` | Provided by 1 object(s) (e.g. tn-mgmt/mgmtp-default/inb-inb) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| prod | BD unused | `uni/tn-prod/BD-10.1.103.0_24` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| prod | EPG isolated (no contracts) | `uni/tn-prod/ap-vlans/epg-vlan102` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| prod | L3Out without external EPG | `uni/tn-prod/out-l3out-to-external-router-1` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. | Add an external EPG with the external subnets and contracts. |
| tn-MGK | Contract unused | `uni/tn-tn-MGK/brc-A2B` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| tn-MGK | VRF unused | `uni/tn-tn-MGK/ctx-ctx-MGK` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| tn_TEST1 | Tenant empty | `uni/tn-tn_TEST1` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 25 broken relation(s) in 5 tenant(s): Contract service graph not instantiated (10); Critical fault F0467 (EPG deployment on path failed) (8); BD VRF missing-target (2); EPG chain broken (BD has no VRF) (2); EPG domain missing-target (2); BD L3Out missing-target (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default); vzAny contract: 2 (e.g. tn-ROR/ctx-ROR_VRF, tn-TN-DEDUP-LAB/ctx-VRF-LAB)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 4 (e.g. tn-ROR/brc-ALLOW_ICMP_Ct, tn-ROR/brc-WEB_TO_OUTSIDE); Contract unused: 2 (e.g. tn-tn-MGK/brc-A2B, tn-common/brc-default); EPG isolated (no contracts): 8 (e.g. tn-OS1/ap-APP-Prod/epg-APP-WEB, tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG); Duplicate contract: 3 (e.g. tn-TN-DEDUP-LAB/brc-C-DNS-FW, tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 7 (e.g. tn-Production_Tenant/BD-Prod_BD_100, tn-Production_Tenant2/BD-Prod_BD_200); L3 BD flooding: 11 (e.g. tn-MUHC/BD-VLAN_2701_BD, tn-OS1/BD-vlan)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 3; VRF unused: 3; BD unused: 7; AP without EPGs: 1; Filter unused: 2; L3Out without external EPG: 2  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 147 of 163 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 114 of 163 objects have no annotation; in use: 'orchestrator:ansible' x49.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 58, UPPER_SNAKE 68, lower 37; 13 generic/VLAN/IP-style names (e.g. tn-OS1/BD-VLAN1, tn-OS1/BD-vlan, tn-TEST/BD-TESTBD, tn-TEST/ap-TEST_AAEP, tn-TEST/ap-TEST_AAEP/epg-TESTEPG).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 16, missing domain: 2  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (65)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| MUHC | EPG without static path | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` | No static path bindings (fvRsPathAtt). |
| MUHC | EPG without static path | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` | No static path bindings (fvRsPathAtt). |
| MUHC | L3 BD flooding | `uni/tn-MUHC/BD-VLAN_2701_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| OS1 | EPG without static path | `uni/tn-OS1/ap-APP-Prod/epg-APP-WEB` | No static path bindings (fvRsPathAtt). |
| OS1 | L3 BD flooding | `uni/tn-OS1/BD-vlan` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Production_Tenant | EPG without domain | `uni/tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Production_Tenant | EPG without static path | `uni/tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG` | No static path bindings (fvRsPathAtt). |
| Production_Tenant2 | EPG without domain | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2/epg-Web_EPG2` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Production_Tenant2 | EPG without static path | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2/epg-Web_EPG2` | No static path bindings (fvRsPathAtt). |
| Production_Tenant22 | EPG without domain | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG22` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Production_Tenant22 | EPG without domain | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG222` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Production_Tenant22 | EPG without static path | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG22` | No static path bindings (fvRsPathAtt). |
| Production_Tenant22 | EPG without static path | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG222` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| TEST | EPG without static path | `uni/tn-TEST/ap-TEST_AAEP/epg-TESTEPG` | No static path bindings (fvRsPathAtt). |
| TEST | L3 BD flooding | `uni/tn-TEST/BD-TESTBD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| Test-Tenant | EPG without static path | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01` | No static path bindings (fvRsPathAtt). |
| Test-Tenant | L3 BD flooding | `uni/tn-Test-Tenant/BD-test-BD-01` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| UT | EPG without domain | `uni/tn-UT/ap-UAP/epg-USER_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| UT | L3 BD flooding | `uni/tn-UT/BD-UBD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| prod | L3 BD flooding | `uni/tn-prod/BD-10.1.100.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| prod | L3 BD flooding | `uni/tn-prod/BD-10.1.101.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| prod | L3 BD flooding | `uni/tn-prod/BD-10.1.102.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| prod | L3 BD flooding | `uni/tn-prod/BD-10.1.103.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| MUHC | Integrity MUHC: all named relations resolve | Unresolved relations: ['uni/tn-MUHC/BD-VLAN_2780_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2701_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2701_BD/rsBDToOut-LEGACY_L3OUT (state=formed, stateQual=mismatch-target, tDn=uni/tn-common/out-default)', 'uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG/rsdomAtt-[uni/phys-LEGACY_SRVF_PHY] (st |
| MUHC | Integrity BD MUHC/VLAN_2780_BD: VRF resolves | uni/tn-MUHC/BD-VLAN_2780_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity BD MUHC/VLAN_2701_BD: VRF resolves | uni/tn-MUHC/BD-VLAN_2701_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity EPG MUHC/LEGACY_APR/VLAN_2780_EPG: BD and VRF chain resolves | uni/tn-MUHC/BD-VLAN_2780_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity EPG MUHC/LEGACY_APR/VLAN_2701_EPG: BD and VRF chain resolves | uni/tn-MUHC/BD-VLAN_2701_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| Prod | Integrity prod: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-prod/ap-vlans/epg-vlan100 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out i', 'F0467 critical: Configuration failed for uni/tn-prod/ap-vlans/epg-vlan101 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out i', 'F0467 critical: |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |
| UT | Integrity UT: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-UT/ap-UAP/epg-USER_EPG node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: vlan-101 :There is no do'] |

## Tenant faults (faultInst)

By severity: warning 33, minor 50, critical 8; TCA/threshold faults (context only): 29

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| prod | critical | F0467 | `uni/tn-prod/ap-vlans/epg-vlan100` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan100 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the do |
| prod | critical | F0467 | `uni/tn-prod/ap-vlans/epg-vlan102` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan102 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the do |
| prod | critical | F0467 | `uni/tn-prod/ap-vlans/epg-vlan101` | Configuration failed for uni/tn-prod/ap-vlans/epg-vlan101 node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the do |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| UT | critical | F0467 | `uni/tn-UT/ap-UAP/epg-USER_EPG` | Configuration failed for uni/tn-UT/ap-UAP/epg-USER_EPG node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: vlan-101 :There is no domain, associated with both EPG and Port, |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
