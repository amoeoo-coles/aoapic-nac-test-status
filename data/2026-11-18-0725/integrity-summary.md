# ACI tenant logical-integrity report: 2026-11-18

## BROKEN RELATIONS FOUND - 18 broken, 75 warnings (7 of 35 tenants broken: PROD, Pune-Tenants, RB-Tenant, SnV, User-Applications, XYZ, test-tenant)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-18 07:26:22 AEDT)
- Generated: 2026-11-18 07:27:09 AEDT
- Scope: 35 tenants on the APIC (6 in baseline, new: aci_p03_tenant, aci_p03_vrf, charlie_terraform, Charlie_Test_Dev, DEV, DevNetAcademy, Jacob, Koushik, KoushikM, l3out-bfd, Lab1-TN, LAB_KK, Lab_Tenant_SAMBI_MTL, PRD, PROD, Pruebas, Pune-Tenants, RB-Tenant, SCADA, Sistemas, Suresh_Tenant, Tenant_DEVOPS, TENANT_PROD, TenantPython, TenantPython2, test, test-tenant, User-Applications, XYZ); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 173 tests, 164 passed, 9 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| aci_p03_tenant | NEW | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| aci_p03_vrf | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| charlie_terraform | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Charlie_Test_Dev | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 3 | 0 | 91 | WARN |
| DEV | NEW | 1 | 3 | 2 | 1 | 2 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| DevNetAcademy | NEW | 2 | 3 | 3 | 2 | 4 | 0 | 0 | 0 | 5 | 0 | 85 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| Jacob | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Koushik | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| KoushikM | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| l3out-bfd | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 97 | WARN |
| Lab1-TN | NEW | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| LAB_KK | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| Lab_Tenant_SAMBI_MTL | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| PRD | NEW | 2 | 2 | 2 | 1 | 8 | 0 | 0 | 0 | 8 | 0 | 76 | WARN |
| PROD | NEW | 1 | 3 | 3 | 1 | 3 | 0 | 0 | 2 | 5 | 4 | 65 | BROKEN |
| Pruebas | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Pune-Tenants | NEW | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 87 | BROKEN |
| RB-Tenant | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 1 | 84 | BROKEN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| SCADA | NEW | 3 | 3 | 3 | 1 | 3 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| Sistemas | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 8 | 1 | 36 | 17 | BROKEN |
| Suresh_Tenant | NEW | 2 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| Tenant_DEVOPS | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TENANT_PROD | NEW | 1 | 3 | 3 | 1 | 3 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| TenantPython | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| TenantPython2 | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| test | NEW | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 3 | 0 | 91 | WARN |
| test-tenant | NEW | 1 | 1 | 0 | 1 | 1 | 2 | 1 | 3 | 4 | 2 | 58 | BROKEN |
| User-Applications | NEW | 1 | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 1 | 4 | 77 | BROKEN |
| XYZ | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 3 | 0 | 81 | BROKEN |

## Broken relations (18)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: vlan-801 :There is no domain, associated with both EPG and Port, that has required VLAN; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| PROD | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: vlan-800 :There is no domain, associated with both EPG and Port, that has required VLAN; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Pune-Tenants | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG` | Configuration failed for uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG node 101 eth1/26 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/out-RB-L3-Out` | Configuration failed for uni/tn-RB-Tenant/out-RB-L3-Out node 102 eth1/48 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| User-Applications | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox` | Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 102 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| User-Applications | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier` | Configuration failed for uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier node 102 eth1/8 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| XYZ | EPG domain missing-target | `uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ` | Domain uni/vmmp-VMware/dom-CCIE-XYZ does not exist (state missing-target). | Create domain uni/vmmp-VMware/dom-CCIE-XYZ (with VLAN pool/AAEP) or associate an existing one. |
| test-tenant | Contract without subjects | `uni/tn-test-tenant/brc-consumer` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| test-tenant | Contract without subjects | `uni/tn-test-tenant/brc-provider` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| test-tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-test-tenant/out-l3out1` | Configuration failed for uni/tn-test-tenant/out-l3out1 node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (75)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Charlie_Test_Dev | Tenant empty | `uni/tn-Charlie_Test_Dev` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| DEV | BD unused | `uni/tn-DEV/BD-10.1.255.0_24` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| DEV | EPG isolated (no contracts) | `uni/tn-DEV/ap-VLANS/epg-VLAN1200` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEV | EPG isolated (no contracts) | `uni/tn-DEV/ap-VLANS/epg-VLAN1201` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEV | L3 BD without subnet | `uni/tn-DEV/BD-10.1.200.0_24` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| DevNetAcademy | EPG isolated (no contracts) | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-CLIENTS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DevNetAcademy | EPG isolated (no contracts) | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-FINANCE` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DevNetAcademy | EPG isolated (no contracts) | `uni/tn-DevNetAcademy/ap-OFFICE/epg-CLIENTS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DevNetAcademy | EPG isolated (no contracts) | `uni/tn-DevNetAcademy/ap-OFFICE/epg-GUESTS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DevNetAcademy | L3 BD without subnet | `uni/tn-DevNetAcademy/BD-NET-113.211.23.0` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Jacob | Tenant empty | `uni/tn-Jacob` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Koushik | Tenant empty | `uni/tn-Koushik` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| KoushikM | Tenant empty | `uni/tn-KoushikM` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| LAB_KK | EPG isolated (no contracts) | `uni/tn-LAB_KK/ap-LAB_AP/epg-LAB_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| LAB_KK | L3 BD without subnet | `uni/tn-LAB_KK/BD-LAB_BD` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Lab1-TN | BD unused | `uni/tn-Lab1-TN/BD-Lab1-App-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Lab1-TN | BD unused | `uni/tn-Lab1-TN/BD-Lab1-Web-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Lab_Tenant_SAMBI_MTL | Tenant empty | `uni/tn-Lab_Tenant_SAMBI_MTL` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-WEB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2201` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PRD | EPG isolated (no contracts) | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-WEB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PROD | EPG isolated (no contracts) | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PROD | EPG isolated (no contracts) | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PROD | EPG isolated (no contracts) | `uni/tn-PROD/ap-APP-PROFILE/epg-WEB-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| PROD | L2 BD settings | `uni/tn-PROD/BD-BD-DB` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| PROD | Subnet on L2 BD | `uni/tn-PROD/BD-BD-DB` | 1 subnet(s) configured but unicast routing is disabled, so the gateway is not active. | Enable unicast routing or remove the subnets. |
| Pruebas | Tenant empty | `uni/tn-Pruebas` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Pune-Tenants | Permit-any filter | `uni/tn-Pune-Tenants/brc-PUNE-CONTRACT` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| RB-Tenant | BD unused | `uni/tn-RB-Tenant/BD-BD-PRod` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| RB-Tenant | L3 BD without subnet | `uni/tn-RB-Tenant/BD-BD-PRod` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| SCADA | EPG isolated (no contracts) | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_APP_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| SCADA | EPG isolated (no contracts) | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_DB_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| SCADA | EPG isolated (no contracts) | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_WEB_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Sistemas | Tenant empty | `uni/tn-Sistemas` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| Suresh_Tenant | BD unused | `uni/tn-Suresh_Tenant/BD-BD_1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Suresh_Tenant | BD unused | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Suresh_Tenant | L3 BD without subnet | `uni/tn-Suresh_Tenant/BD-BD_1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| TENANT_PROD | EPG isolated (no contracts) | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_CLOIENTS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TENANT_PROD | EPG isolated (no contracts) | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_DMZ` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TENANT_PROD | EPG isolated (no contracts) | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_SERVERS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TEST | Config fault F0887 | `uni/tn-TEST/ap-APP_1/epg-EPG1` | Failed to form relation to MO uni/tn-TEST/ap-APP_1/epg-EPG1 of class fvAEPg | See the APIC fault description and resolve the referenced object. |
| TenantPython | Tenant empty | `uni/tn-TenantPython` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| TenantPython2 | Tenant empty | `uni/tn-TenantPython2` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Tenant_DEVOPS | Tenant empty | `uni/tn-Tenant_DEVOPS` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| User-Applications | Permit-any filter | `uni/tn-User-Applications/brc-Open-Communitcation` | Contract permits ALL traffic via tn-User-Applications/flt-All-Traffic entry All-Traffic (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| XYZ | BD unused | `uni/tn-XYZ/BD-DEV` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| XYZ | EPG isolated (no contracts) | `uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| XYZ | L3 BD without subnet | `uni/tn-XYZ/BD-DEV` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| aci_p03_tenant | AP without EPGs | `uni/tn-aci_p03_tenant/ap-aci_p03` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| aci_p03_vrf | VRF unused | `uni/tn-aci_p03_vrf/ctx-aci_p03_tennt` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| charlie_terraform | Tenant empty | `uni/tn-charlie_terraform` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| common | Contract unused | `uni/tn-common/brc-power_up` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-sql` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| l3out-bfd | L3Out without external EPG | `uni/tn-l3out-bfd/out-l3out-test` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. | Add an external EPG with the external subnets and contracts. |
| mgmt | Config fault F0523 | `uni/tn-mgmt/mgmtp-default/inb-InBand-Mgt` | Configuration failed for EPG InBand-Mgt due to Not Associated With Management Zone | Fix the EPG's dependency named in the fault (BD/VRF, management zone, etc.). |
| mgmt | Config fault F0618 | `uni/tn-mgmt/mgmtp-default/oob-default` | Out-of-band management address is not allocated to node 101 | See the APIC fault description and resolve the referenced object. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| test | AP without EPGs | `uni/tn-test/ap-test_test_AP` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| test | Contract unused | `uni/tn-test/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| test | VRF unused | `uni/tn-test/ctx-test` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| test-tenant | Contract consumed, never provided | `uni/tn-test-tenant/brc-consumer` | Consumed by 1 object(s) (e.g. tn-test-tenant/out-l3out1/instP-Ext-EPG) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| test-tenant | Contract provided, never consumed | `uni/tn-test-tenant/brc-provider` | Provided by 1 object(s) (e.g. tn-test-tenant/out-l3out1/instP-Ext-EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| test-tenant | EPG isolated (no contracts) | `uni/tn-test-tenant/ap-ap1/epg-epg1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| test-tenant | L3 BD without subnet | `uni/tn-test-tenant/BD-bd1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 18 broken relation(s) in 7 tenant(s): Critical fault F0467 (EPG deployment on path failed) (15); Contract without subjects (2); EPG domain missing-target (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 3 (e.g. tn-Pune-Tenants/brc-PUNE-CONTRACT, tn-User-Applications/brc-Open-Communitcation); vzAny contract: 1 (e.g. tn-ROR/ctx-ROR_VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 4 (e.g. tn-ROR/brc-ALLOW_ICMP_Ct, tn-ROR/brc-WEB_TO_OUTSIDE); Contract consumed, never provided: 1 (e.g. tn-test-tenant/brc-consumer); Contract unused: 4 (e.g. tn-common/brc-power_up, tn-common/brc-sql); EPG isolated (no contracts): 26 (e.g. tn-DEV/ap-VLANS/epg-VLAN1200, tn-DEV/ap-VLANS/epg-VLAN1201)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 9 (e.g. tn-DEV/BD-10.1.200.0_24, tn-DevNetAcademy/BD-NET-113.211.23.0); Subnet on L2 BD: 1 (e.g. tn-PROD/BD-BD-DB); L2 BD settings: 1 (e.g. tn-PROD/BD-BD-DB); L3 BD flooding: 20 (e.g. tn-DEV/BD-10.1.201.0_24, tn-DEV/BD-10.1.255.0_24)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 12; VRF unused: 4; BD unused: 7; AP without EPGs: 3; Filter unused: 5; L3Out without external EPG: 2  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 141 of 146 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 115 of 146 objects have no annotation; in use: 'orchestrator:terraform' x31.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: Mixed 37, UPPER_SNAKE 74, lower 35; 10 generic/VLAN/IP-style names (e.g. tn-DEV/BD-10.1.200.0_24, tn-DEV/BD-10.1.201.0_24, tn-DEV/BD-10.1.255.0_24, tn-DEV/ap-VLANS/epg-VLAN1200, tn-DEV/ap-VLANS/epg-VLAN1201).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 25, missing domain: 1  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (85)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| DEV | EPG without domain | `uni/tn-DEV/ap-VLANS/epg-VLAN1200` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DEV | EPG without domain | `uni/tn-DEV/ap-VLANS/epg-VLAN1201` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DEV | EPG without static path | `uni/tn-DEV/ap-VLANS/epg-VLAN1200` | No static path bindings (fvRsPathAtt). |
| DEV | EPG without static path | `uni/tn-DEV/ap-VLANS/epg-VLAN1201` | No static path bindings (fvRsPathAtt). |
| DEV | L3 BD flooding | `uni/tn-DEV/BD-10.1.201.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| DEV | L3 BD flooding | `uni/tn-DEV/BD-10.1.255.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| DevNetAcademy | EPG without domain | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-CLIENTS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DevNetAcademy | EPG without domain | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-FINANCE` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DevNetAcademy | EPG without domain | `uni/tn-DevNetAcademy/ap-OFFICE/epg-CLIENTS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DevNetAcademy | EPG without domain | `uni/tn-DevNetAcademy/ap-OFFICE/epg-GUESTS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| DevNetAcademy | EPG without static path | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-CLIENTS` | No static path bindings (fvRsPathAtt). |
| DevNetAcademy | EPG without static path | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-FINANCE` | No static path bindings (fvRsPathAtt). |
| DevNetAcademy | EPG without static path | `uni/tn-DevNetAcademy/ap-OFFICE/epg-CLIENTS` | No static path bindings (fvRsPathAtt). |
| DevNetAcademy | EPG without static path | `uni/tn-DevNetAcademy/ap-OFFICE/epg-GUESTS` | No static path bindings (fvRsPathAtt). |
| LAB_KK | EPG without domain | `uni/tn-LAB_KK/ap-LAB_AP/epg-LAB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| LAB_KK | EPG without static path | `uni/tn-LAB_KK/ap-LAB_AP/epg-LAB_EPG` | No static path bindings (fvRsPathAtt). |
| Lab1-TN | L3 BD flooding | `uni/tn-Lab1-TN/BD-Lab1-App-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Lab1-TN | L3 BD flooding | `uni/tn-Lab1-TN/BD-Lab1-Web-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2201` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without domain | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-APP` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-DB` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-WEB` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2201` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-APP` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-DB` | No static path bindings (fvRsPathAtt). |
| PRD | EPG without static path | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-WEB` | No static path bindings (fvRsPathAtt). |
| PRD | L3 BD flooding | `uni/tn-PRD/BD-10.2.200.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| PRD | L3 BD flooding | `uni/tn-PRD/BD-10.2.201.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| PROD | EPG without domain | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PROD | EPG without domain | `uni/tn-PROD/ap-APP-PROFILE/epg-WEB-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| PROD | EPG without static path | `uni/tn-PROD/ap-APP-PROFILE/epg-WEB-EPG` | No static path bindings (fvRsPathAtt). |
| PROD | L3 BD flooding | `uni/tn-PROD/BD-BD-WEB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| PROD | L3 BD flooding | `uni/tn-PROD/BD-TEST-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Pune-Tenants | L3 BD flooding | `uni/tn-Pune-Tenants/BD-PUNE-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SCADA | EPG without domain | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_APP_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| SCADA | EPG without domain | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| SCADA | EPG without domain | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| SCADA | EPG without static path | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_APP_EPG` | No static path bindings (fvRsPathAtt). |
| SCADA | EPG without static path | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_DB_EPG` | No static path bindings (fvRsPathAtt). |
| SCADA | EPG without static path | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| SCADA | L3 BD flooding | `uni/tn-SCADA/BD-SCADA_APP_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SCADA | L3 BD flooding | `uni/tn-SCADA/BD-SCADA_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SCADA | L3 BD flooding | `uni/tn-SCADA/BD-SCADA_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| Suresh_Tenant | L3 BD flooding | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TENANT_PROD | EPG without domain | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_CLOIENTS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TENANT_PROD | EPG without domain | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_DMZ` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TENANT_PROD | EPG without domain | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_SERVERS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TENANT_PROD | EPG without static path | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_CLOIENTS` | No static path bindings (fvRsPathAtt). |
| TENANT_PROD | EPG without static path | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_DMZ` | No static path bindings (fvRsPathAtt). |
| TENANT_PROD | EPG without static path | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_SERVERS` | No static path bindings (fvRsPathAtt). |
| TENANT_PROD | L3 BD flooding | `uni/tn-TENANT_PROD/BD-BD-DMZ` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TENANT_PROD | L3 BD flooding | `uni/tn-TENANT_PROD/BD-BD_CLIENTS` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TENANT_PROD | L3 BD flooding | `uni/tn-TENANT_PROD/BD-BD_SERVERS` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| User-Applications | L3 BD flooding | `uni/tn-User-Applications/BD-Jumpbox` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| User-Applications | L3 BD flooding | `uni/tn-User-Applications/BD-Wordpress` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| XYZ | EPG without static path | `uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ` | No static path bindings (fvRsPathAtt). |
| XYZ | Filter unused | `uni/tn-XYZ/flt-YES` | Filter is not referenced by any contract subject. |
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
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| oneaciapp | Filter unused | `uni/tn-oneaciapp/flt-yres` | Filter is not referenced by any contract subject. |
| test-tenant | EPG without static path | `uni/tn-test-tenant/ap-ap1/epg-epg1` | No static path bindings (fvRsPathAtt). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| PROD | Integrity PROD: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the E', 'F0467 critical: Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: vlan-801 :Th', 'F0467 critical: |
| Pune-Tenants | Integrity Pune-Tenants: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG node 101 eth1/26 due to Invalid Path Configuration, debug message: invalid-path: Either the'] |
| RB-Tenant | Integrity RB-Tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-RB-Tenant/out-RB-L3-Out node 102 eth1/48 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is'] |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not ', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not ', 'F0467 critical: |
| Test-Tenant | Integrity test-tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-test-tenant/out-l3out1 node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out', 'F0467 critical: Configuration failed for uni/tn-test-tenant/out-l3out1 node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out'] |
| Test-Tenant | Integrity contract test-tenant/provider: subjects and filters | Contract uni/tn-test-tenant/brc-provider has no subjects (permits nothing) |
| Test-Tenant | Integrity contract test-tenant/consumer: subjects and filters | Contract uni/tn-test-tenant/brc-consumer has no subjects (permits nothing) |
| User-Applications | Integrity User-Applications: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 101 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either ', 'F0467 critical: Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 102 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either ', 'F0467 critical: |
| XYZ | Integrity XYZ: all named relations resolve | Unresolved relations: ['uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ/rsdomAtt-[uni/vmmp-VMware/dom-CCIE-XYZ] (state=missing-target, stateQual=none, tDn=uni/vmmp-VMware/dom-CCIE-XYZ)'] |

## Tenant faults (faultInst)

By severity: warning 5, minor 2, critical 48; TCA/threshold faults (context only): 3

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| User-Applications | critical | F0467 | `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier` | Configuration failed for uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier node 102 eth1/8 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associa |
| RB-Tenant | critical | F0467 | `uni/tn-RB-Tenant/out-RB-L3-Out` | Configuration failed for uni/tn-RB-Tenant/out-RB-L3-Out node 102 eth1/48 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the dom |
| PROD | critical | F0467 | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG node 102 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: vlan-800 :There is no domain, associated with both EPG |
| PROD | critical | F0467 | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: vlan-801 :There is no domain, associated with both E |
| User-Applications | critical | F0467 | `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox` | Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 102 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a d |
| test-tenant | critical | F0467 | `uni/tn-test-tenant/out-l3out1` | Configuration failed for uni/tn-test-tenant/out-l3out1 node 102 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the  |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 102 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| PROD | critical | F0467 | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG node 101 eth1/43 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain o |
| PROD | critical | F0467 | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` | Configuration failed for uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain |
| Pune-Tenants | critical | F0467 | `uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG` | Configuration failed for uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG node 101 eth1/26 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a doma |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Database` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Database` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Database` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Database node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 SnV_FI-1B due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Database` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Database node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-125 :Either the EpG is not associa |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-127 :Either the EpG is not asso |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-123 :Either the EpG is not associ |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-121 :Either the EpG is not a |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 SnV_FI-1A due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| User-Applications | critical | F0467 | `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier` | Configuration failed for uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier node 101 eth1/8 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associa |
| User-Applications | critical | F0467 | `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox` | Configuration failed for uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox node 101 eth1/7 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a d |
| test-tenant | critical | F0467 | `uni/tn-test-tenant/out-l3out1` | Configuration failed for uni/tn-test-tenant/out-l3out1 node 101 IPG-VPC-DEV due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the  |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
