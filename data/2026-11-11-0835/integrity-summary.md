# ACI tenant logical-integrity report: 2026-11-11

## BROKEN RELATIONS FOUND - 24 broken, 99 warnings (11 of 37 tenants broken: Cursor_tenant1, LAB-TENANT, Production, RB-Tenant, Tenant_RG, Test100, Test_9112026, VY-TN, tenant_mylab, tn_example_tenant, zzzps4021_BGP)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-11 08:35:58 AEDT)
- Generated: 2026-11-11 08:36:13 AEDT
- Scope: 37 tenants on the APIC (4 in baseline, new: billing-test-DPYD6hPFFmE9, Cursor_tenant1, Cursor_Tenant2, Cursor_Tenant3, Cursor_tenant5, EM-LAB, iTenant, LAB-TENANT, MAD, MGMT_LAN, mjay_dev, Mouse, Prod, Production, RB-Tenant, Tenant-Ahmed, Tenant2, Tenant_RG, Test, Test100, Test_9112026, TN-CONSUMER, TN-CONSUMER-BGS, TN-LAB-ANS01, TN-LAB-K01, TN-LAB-K02, TN-PROVIDER, TN-PROVIDER-BGS, tn_example_tenant, VY-TN, Zangief, zzzps4021, zzzps4021_BGP); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 253 tests, 236 passed, 17 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| billing-test-DPYD6hPFFmE9 | NEW | 1 | 1 | 1 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| common | yes | 2 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 1 | 2 | 2 | 1 | 1 | 1 | 0 | 1 | 3 | 0 | 81 | BROKEN |
| Cursor_Tenant2 | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Cursor_Tenant3 | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Cursor_tenant5 | NEW | 1 | 7 | 7 | 1 | 3 | 0 | 0 | 0 | 7 | 0 | 79 | WARN |
| EM-LAB | NEW | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| iTenant | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| LAB-TENANT | NEW | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 3 | 4 | 2 | 58 | BROKEN |
| MAD | NEW | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| MGMT_LAN | NEW | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| mjay_dev | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Mouse | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| oneaciapp | yes | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Prod | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Production | NEW | 1 | 2 | 2 | 3 | 0 | 2 | 0 | 2 | 7 | 0 | 59 | BROKEN |
| RB-Tenant | NEW | 1 | 1 | 1 | 2 | 2 | 2 | 0 | 3 | 4 | 1 | 58 | BROKEN |
| Tenant-Ahmed | NEW | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| Tenant2 | NEW | 1 | 1 | 0 | 2 | 2 | 0 | 0 | 0 | 6 | 0 | 82 | WARN |
| Tenant_RG | NEW | 2 | 2 | 0 | 1 | 1 | 0 | 1 | 2 | 4 | 3 | 68 | BROKEN |
| Test | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Test100 | NEW | 2 | 4 | 4 | 2 | 4 | 3 | 1 | 1 | 8 | 1 | 66 | BROKEN |
| Test_9112026 | NEW | 2 | 0 | 0 | 0 | 0 | 2 | 3 | 5 | 3 | 3 | 41 | BROKEN |
| TN-CONSUMER | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| TN-CONSUMER-BGS | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| TN-LAB-ANS01 | NEW | 1 | 3 | 3 | 1 | 3 | 2 | 0 | 0 | 3 | 0 | 91 | WARN |
| TN-LAB-K01 | NEW | 1 | 3 | 3 | 1 | 3 | 3 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| TN-LAB-K02 | NEW | 1 | 3 | 3 | 1 | 3 | 3 | 0 | 0 | 2 | 0 | 94 | WARN |
| TN-PROVIDER | NEW | 1 | 2 | 2 | 1 | 2 | 3 | 0 | 0 | 2 | 0 | 94 | WARN |
| TN-PROVIDER-BGS | NEW | 1 | 2 | 2 | 1 | 2 | 3 | 0 | 0 | 2 | 0 | 94 | WARN |
| tn_example_tenant | NEW | 1 | 4 | 3 | 2 | 3 | 2 | 1 | 2 | 8 | 4 | 56 | BROKEN |
| VY-TN | NEW | 3 | 3 | 1 | 1 | 4 | 2 | 1 | 3 | 5 | 3 | 55 | BROKEN |
| Zangief | NEW | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| zzzps4021 | NEW | 2 | 4 | 4 | 2 | 4 | 3 | 1 | 0 | 8 | 0 | 76 | WARN |
| zzzps4021_BGP | NEW | 3 | 3 | 1 | 1 | 4 | 2 | 1 | 1 | 5 | 1 | 75 | BROKEN |

## Broken relations (24)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Cursor_tenant1 | BD VRF missing-target | `uni/tn-Cursor_tenant1/BD-p2bd` | BD points to VRF 'p2v' which does not exist in tenant Cursor_tenant1 or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'p2v' in Cursor_tenant1 (or common), or point the BD to an existing VRF. |
| LAB-TENANT | Contract without subjects | `uni/tn-LAB-TENANT/brc-teste123` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| LAB-TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-LAB-TENANT/out-L3OUT_TESTE` | Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Production | Contract without subjects | `uni/tn-Production/brc-BD-APP` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| Production | Contract without subjects | `uni/tn-Production/brc-BD-DB` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-FTP` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| RB-Tenant | Contract without subjects | `uni/tn-RB-Tenant/brc-HTTPS` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| RB-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for node 102 due to Interface Configured as L3, debug message: port-configured-as-l3: Interface is already configured under other VRF named LAB-TENANT:LAB-VRF; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Tenant_RG | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test100 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test100/out-L3out` | Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-inter-VRF_contract` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| Test_9112026 | Contract without subjects | `uni/tn-Test_9112026/brc-intra-VRF_contract` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Test_9112026 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out node 101 eth1/11 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG` | Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| VY-TN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| VY-TN | Major fault F0565 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | Deployment of EPG uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02 failed on domain test-vmm due to EPG encapsulation value is not part of any static encapsulation block for the VMM domain | See the APIC fault description and resolve the referenced object. |
| tenant_mylab | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tenant_mylab/out-ok` | Configuration failed for uni/tn-tenant_mylab/out-ok node 101 eth1/40 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-333 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned t | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| tn_example_tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_20 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-111 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| zzzps4021_BGP | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-zzzps4021_BGP/out-test-L3OUT` | Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (99)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Cursor_Tenant2 | EPG isolated (no contracts) | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_Tenant3 | EPG isolated (no contracts) | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_tenant1 | BD unused | `uni/tn-Cursor_tenant1/BD-p2bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Cursor_tenant1 | Contract unused | `uni/tn-Cursor_tenant1/brc-p2ctr` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Cursor_tenant1 | EPG isolated (no contracts) | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_tenant5 | BD unused | `uni/tn-Cursor_tenant5/BD-cursor5_fw_app_bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Cursor_tenant5 | BD unused | `uni/tn-Cursor_tenant5/BD-cursor5_fw_db_bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Cursor_tenant5 | BD unused | `uni/tn-Cursor_tenant5/BD-cursor5_fw_dmz_bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Cursor_tenant5 | BD unused | `uni/tn-Cursor_tenant5/BD-cursor5_fw_web_bd` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Cursor_tenant5 | EPG isolated (no contracts) | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-app` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_tenant5 | EPG isolated (no contracts) | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_tenant5 | EPG isolated (no contracts) | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| EM-LAB | BD VRF fallback to common | `uni/tn-EM-LAB/BD-AABD` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. | Set the VRF explicitly on the BD. |
| EM-LAB | EPG isolated (no contracts) | `uni/tn-EM-LAB/ap-AAAP/epg-AAEPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| LAB-TENANT | BD VRF fallback to common | `uni/tn-LAB-TENANT/BD-LAB-BD` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. | Set the VRF explicitly on the BD. |
| LAB-TENANT | Config fault F1298 | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | For tenant LAB-TENANT, application profile LAB-APP, deployment of application EPG WEB-EPG failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| LAB-TENANT | Contract consumed, never provided | `uni/tn-LAB-TENANT/brc-teste123` | Consumed by 2 object(s) (e.g. tn-LAB-TENANT/out-L3OUT_TESTE/instP-EEPG_L3OUT) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| LAB-TENANT | L3 BD without subnet | `uni/tn-LAB-TENANT/BD-LAB-BD` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| MAD | EPG isolated (no contracts) | `uni/tn-MAD/ap-MAD_test_AP/epg-MAD_test_test_2101_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| MAD | L2 BD settings | `uni/tn-MAD/BD-MAD_test_test_BD` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| MGMT_LAN | AP without EPGs | `uni/tn-MGMT_LAN/ap-AP-MGMT` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| Mouse | EPG isolated (no contracts) | `uni/tn-Mouse/ap-network-segment/epg-EPG-10` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Prod | Tenant empty | `uni/tn-Prod` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Production | AP without EPGs | `uni/tn-Production/ap-EPG-APP` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| Production | AP without EPGs | `uni/tn-Production/ap-EPG-DATABASE` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| Production | AP without EPGs | `uni/tn-Production/ap-EPG-WEB` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| Production | BD unused | `uni/tn-Production/BD-BD-APP` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Production | BD unused | `uni/tn-Production/BD-BD-WEB` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Production | Contract unused | `uni/tn-Production/brc-BD-APP` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Production | Contract unused | `uni/tn-Production/brc-BD-DB` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| RB-Tenant | BD unused | `uni/tn-RB-Tenant/BD-RB-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| RB-Tenant | Config fault F1298 | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | For tenant RB-Tenant, application profile FTP, deployment of application EPG FTP-EPG failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| RB-Tenant | L2 BD settings | `uni/tn-RB-Tenant/BD-RB-BD` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| RB-Tenant | Subnet on L2 BD | `uni/tn-RB-Tenant/BD-RB-BD` | 1 subnet(s) configured but unicast routing is disabled, so the gateway is not active. | Enable unicast routing or remove the subnets. |
| TN-LAB-ANS01 | Contract provided, never consumed | `uni/tn-TN-LAB-ANS01/brc-CT-WEB-APP` | Provided by 2 object(s) (e.g. tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-APP) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TN-LAB-ANS01 | Contract unused | `uni/tn-TN-LAB-ANS01/brc-CT-APP-DB` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| TN-LAB-ANS01 | EPG isolated (no contracts) | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TN-LAB-K02 | Contract provided, never consumed | `uni/tn-TN-LAB-K02/brc-CT-APP-DB` | Provided by 1 object(s) (e.g. tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-DB) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TN-LAB-K02 | Contract unused | `uni/tn-TN-LAB-K02/brc-CT-WEB-DB` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| TN-PROVIDER | Contract consumed, never provided | `uni/tn-TN-PROVIDER/brc-CTR-WEB-DB` | Consumed by 1 object(s) (e.g. tn-TN-CONSUMER/ap-AP-WEB/epg-EPG-WEB) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| TN-PROVIDER | Contract provided, never consumed | `uni/tn-TN-PROVIDER/brc-CTR-APP-DB` | Provided by 1 object(s) (e.g. tn-TN-PROVIDER/ap-AP-APP/epg-EPG-DB) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| TN-PROVIDER-BGS | BD VRF fallback to common | `uni/tn-TN-PROVIDER-BGS/BD-BD-DB` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. | Set the VRF explicitly on the BD. |
| TN-PROVIDER-BGS | Contract provided, never consumed | `uni/tn-TN-PROVIDER-BGS/brc-CTR-BD-APP` | Provided by 2 object(s) (e.g. tn-TN-PROVIDER-BGS/ap-AP-APP/epg-EPG-APP) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| Tenant-Ahmed | AP without EPGs | `uni/tn-Tenant-Ahmed/ap-App-X` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| Tenant-Ahmed | VRF unused | `uni/tn-Tenant-Ahmed/ctx-VRF-1` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| Tenant2 | BD unused | `uni/tn-Tenant2/BD-BD2` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Tenant2 | EPG BD fallback to common | `uni/tn-Tenant2/ap-App-XYZ/epg-EPG-B` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Tenant2 | EPG BD fallback to common | `uni/tn-Tenant2/ap-App-Y/epg-EPG-B` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| Tenant2 | EPG isolated (no contracts) | `uni/tn-Tenant2/ap-App-XYZ/epg-EPG-B` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tenant2 | EPG isolated (no contracts) | `uni/tn-Tenant2/ap-App-Y/epg-EPG-B` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tenant2 | L3 BD without subnet | `uni/tn-Tenant2/BD-BD2` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| Tenant_RG | BD unused | `uni/tn-Tenant_RG/BD-L2_BD_RG` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Tenant_RG | EPG isolated (no contracts) | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Tenant_RG | External EPG without contracts | `uni/tn-Tenant_RG/out-rg_l3_out_ext/instP-epg_RG_EXT_ROUTED` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| Tenant_RG | L2 BD settings | `uni/tn-Tenant_RG/BD-RG_BD_EXT_L2` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| Test | Tenant empty | `uni/tn-Test` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| Test100 | Config fault F1298 | `uni/tn-Test100/out-L3out/instP-EXT-EPG` | For tenant Test100, outside L3out, deployment of external EPG EXT-EPG failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Test100 | Contract provided, never consumed | `uni/tn-Test100/brc-L3out` | Provided by 1 object(s) (e.g. tn-Test100/out-L3out/instP-EXT-EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| Test100 | Contract unused | `uni/tn-Test100/brc-APP-to-DB` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Test100 | Contract unused | `uni/tn-Test100/brc-ESG` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Test100 | EPG isolated (no contracts) | `uni/tn-Test100/ap-DEV/epg-D-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Test100 | EPG isolated (no contracts) | `uni/tn-Test100/ap-DEV/epg-D-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Test100 | EPG isolated (no contracts) | `uni/tn-Test100/ap-PROD/epg-P-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Test100 | EPG isolated (no contracts) | `uni/tn-Test100/ap-PROD/epg-P-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Test_9112026 | Config fault F1298 | `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out/instP-IAAS-STRE-SHRP01-PSN-COLL-IPv6_Ext` | For tenant Test_9112026, outside IAAS-STRE-SHRP01-PSN-COLL_L3Out, deployment of external EPG IAAS-STRE-SHRP01-PSN-COLL-IPv6_Ext failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Test_9112026 | Config fault F1298 | `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out/instP-IaaS_Ipv6_extEPG` | For tenant Test_9112026, outside IAAS1-PSNXXXX_L3Out, deployment of external EPG IaaS_Ipv6_extEPG failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| Test_9112026 | Config fault F2069 | `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out/lnodep-CSP-PSNXXXX_L3Out_nodeProfile` | Configuration failed for Tenant Test_9112026, Name CSP-PSNXXXX_L3Out, Logical Node Profile CSP-PSNXXXX_L3Out_nodeProfile due to RsNodeL3OutAtt VirtualLIfP Misconfiguration | See the APIC fault description and resolve the referenced object. |
| VY-TN | EPG isolated (no contracts) | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| VY-TN | EPG isolated (no contracts) | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG03` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| VY-TN | L3 BD without subnet | `uni/tn-VY-TN/BD-VY-BD02` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| VY-TN | L3 BD without subnet | `uni/tn-VY-TN/BD-VY-BD03` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| VY-TN | vzAny contract | `uni/tn-VY-TN/ctx-VY-VRF` | vzAny provides 0 / consumes 1 contract(s) (Contract2); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| Zangief | AP without EPGs | `uni/tn-Zangief/ap-LEGACY-DIAG-APP` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| iTenant | Tenant empty | `uni/tn-iTenant` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| mjay_dev | Tenant empty | `uni/tn-mjay_dev` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| oneaciapp | Tenant empty | `uni/tn-oneaciapp` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| tn_example_tenant | BD unused | `uni/tn-tn_example_tenant/BD-BIGIP_222_BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| tn_example_tenant | Config fault F1298 | `uni/tn-tn_example_tenant/out-my_first_l3out/instP-my_first_epg_for_bgp` | For tenant tn_example_tenant, outside my_first_l3out, deployment of external EPG my_first_epg_for_bgp failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| tn_example_tenant | Contract consumed, never provided | `uni/tn-tn_example_tenant/brc-in-contract` | Consumed by 1 object(s) (e.g. tn-tn_example_tenant/out-my_first_l3out/instP-my_first_epg_for_bgp) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| tn_example_tenant | Contract provided, never consumed | `uni/tn-tn_example_tenant/brc-out-contract` | Provided by 1 object(s) (e.g. tn-tn_example_tenant/out-my_first_l3out/instP-my_first_epg_for_bgp) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| tn_example_tenant | EPG isolated (no contracts) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| tn_example_tenant | EPG isolated (no contracts) | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| tn_example_tenant | EPG isolated (no contracts) | `uni/tn-tn_example_tenant/ap-app-profile/epg-201_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| tn_example_tenant | Permit-any filter | `uni/tn-tn_example_tenant/brc-out-contract` | Contract permits ALL traffic via tn-tn_example_tenant/flt-ip-any entry any (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| zzzps4021 | Config fault F1298 | `uni/tn-zzzps4021/out-L3out/instP-EXT-EPG` | For tenant zzzps4021, outside L3out, deployment of external EPG EXT-EPG failed on node 101. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| zzzps4021 | Contract provided, never consumed | `uni/tn-zzzps4021/brc-L3out` | Provided by 1 object(s) (e.g. tn-zzzps4021/out-L3out/instP-EXT-EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| zzzps4021 | Contract unused | `uni/tn-zzzps4021/brc-APP-to-DB` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| zzzps4021 | Contract unused | `uni/tn-zzzps4021/brc-ESG` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| zzzps4021 | EPG isolated (no contracts) | `uni/tn-zzzps4021/ap-DEV/epg-D-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021 | EPG isolated (no contracts) | `uni/tn-zzzps4021/ap-DEV/epg-D-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021 | EPG isolated (no contracts) | `uni/tn-zzzps4021/ap-PROD/epg-P-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021 | EPG isolated (no contracts) | `uni/tn-zzzps4021/ap-PROD/epg-P-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021_BGP | Contract provided, never consumed | `uni/tn-zzzps4021_BGP/brc-Contract2` | Provided by 1 object(s) (e.g. tn-zzzps4021_BGP/out-test-L3OUT/instP-test-L3EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| zzzps4021_BGP | EPG isolated (no contracts) | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG02` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021_BGP | EPG isolated (no contracts) | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG03` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| zzzps4021_BGP | L3 BD without subnet | `uni/tn-zzzps4021_BGP/BD-VY-BD02` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| zzzps4021_BGP | L3 BD without subnet | `uni/tn-zzzps4021_BGP/BD-VY-BD03` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 24 broken relation(s) in 11 tenant(s): Critical fault F0467 (EPG deployment on path failed) (15); Contract without subjects (7); BD VRF missing-target (1); Major fault F0565 (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 2 (e.g. tn-tn_example_tenant/brc-out-contract, tn-common/brc-default); vzAny contract: 1 (e.g. tn-VY-TN/ctx-VY-VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 8 (e.g. tn-TN-LAB-ANS01/brc-CT-WEB-APP, tn-TN-LAB-K02/brc-CT-APP-DB); Contract consumed, never provided: 3 (e.g. tn-LAB-TENANT/brc-teste123, tn-TN-PROVIDER/brc-CTR-WEB-DB); Contract unused: 10 (e.g. tn-Cursor_tenant1/brc-p2ctr, tn-Production/brc-BD-APP); EPG isolated (no contracts): 28 (e.g. tn-Cursor_Tenant2/ap-cursor2_ap/epg-web, tn-Cursor_Tenant3/ap-cursor3_ap/epg-web); External EPG without contracts: 1 (e.g. tn-Tenant_RG/out-rg_l3_out_ext/instP-epg_RG_EXT_ROUTED)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Match contract scope to real usage** - found: scope mismatch: 0, wider than needed: 1  
   Do: Use 'context' by default, 'tenant'/'global' only for inter-VRF/tenant flows (with shared subnets).
5. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 8 (e.g. tn-LAB-TENANT/BD-LAB-BD, tn-Tenant2/BD-BD2); Subnet on L2 BD: 1 (e.g. tn-RB-Tenant/BD-RB-BD); L2 BD settings: 3 (e.g. tn-MAD/BD-MAD_test_test_BD, tn-RB-Tenant/BD-RB-BD); L3 BD flooding: 42 (e.g. tn-Cursor_Tenant2/BD-cursor2_bd, tn-Cursor_Tenant3/BD-cursor3_bd)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
6. **Clean up unused objects** - found: Tenant empty: 5; VRF unused: 3; BD unused: 12; AP without EPGs: 7; Filter unused: 4; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
7. **Add descriptions** - found: 213 of 254 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
8. **Tag ownership (annotations) for NaC** - found: 169 of 254 objects have no annotation; in use: 'orchestrator:ansible' x75, 'orchestrator:terraform' x10.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
9. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 172, lower 55, Mixed 27; 3 generic/VLAN/IP-style names (e.g. tn-LAB-TENANT/brc-teste123, tn-MAD/ctx-test, tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-testers).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
10. **Bind EPGs to a domain** - found: no domain: 38, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (143)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| Cursor_Tenant2 | EPG without domain | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_Tenant2 | EPG without static path | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` | No static path bindings (fvRsPathAtt). |
| Cursor_Tenant2 | L3 BD flooding | `uni/tn-Cursor_Tenant2/BD-cursor2_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_Tenant3 | EPG without domain | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_Tenant3 | EPG without static path | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` | No static path bindings (fvRsPathAtt). |
| Cursor_Tenant3 | L3 BD flooding | `uni/tn-Cursor_Tenant3/BD-cursor3_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant1 | EPG without domain | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_tenant1 | EPG without static path | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` | No static path bindings (fvRsPathAtt). |
| Cursor_tenant1 | L3 BD flooding | `uni/tn-Cursor_tenant1/BD-cursor_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant1 | L3 BD flooding | `uni/tn-Cursor_tenant1/BD-p2bd` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Cursor_tenant5 | EPG without domain | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-app` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_tenant5 | EPG without domain | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_tenant5 | EPG without domain | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Cursor_tenant5 | EPG without static path | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-app` | No static path bindings (fvRsPathAtt). |
| Cursor_tenant5 | EPG without static path | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-db` | No static path bindings (fvRsPathAtt). |
| Cursor_tenant5 | EPG without static path | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-web` | No static path bindings (fvRsPathAtt). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_app_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_db_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_fw_app_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_fw_db_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_fw_dmz_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_fw_web_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Cursor_tenant5 | L3 BD flooding | `uni/tn-Cursor_tenant5/BD-cursor5_web_bd` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| EM-LAB | EPG without static path | `uni/tn-EM-LAB/ap-AAAP/epg-AAEPG` | No static path bindings (fvRsPathAtt). |
| EM-LAB | L3 BD flooding | `uni/tn-EM-LAB/BD-AABD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MAD | EPG without domain | `uni/tn-MAD/ap-MAD_test_AP/epg-MAD_test_test_2101_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| MAD | EPG without static path | `uni/tn-MAD/ap-MAD_test_AP/epg-MAD_test_test_2101_EPG` | No static path bindings (fvRsPathAtt). |
| Mouse | EPG without domain | `uni/tn-Mouse/ap-network-segment/epg-EPG-10` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Mouse | EPG without static path | `uni/tn-Mouse/ap-network-segment/epg-EPG-10` | No static path bindings (fvRsPathAtt). |
| Mouse | L3 BD flooding | `uni/tn-Mouse/BD-BD-10` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Production | L3 BD flooding | `uni/tn-Production/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| RB-Tenant | EPG without domain | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| RB-Tenant | EPG without domain | `uni/tn-RB-Tenant/ap-WWW/epg-WWW` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| RB-Tenant | EPG without static path | `uni/tn-RB-Tenant/ap-WWW/epg-WWW` | No static path bindings (fvRsPathAtt). |
| RB-Tenant | Filter unused | `uni/tn-RB-Tenant/flt-FTP` | Filter is not referenced by any contract subject. |
| RB-Tenant | Filter unused | `uni/tn-RB-Tenant/flt-https` | Filter is not referenced by any contract subject. |
| TN-CONSUMER | EPG without domain | `uni/tn-TN-CONSUMER/ap-AP-WEB/epg-EPG-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-CONSUMER | EPG without static path | `uni/tn-TN-CONSUMER/ap-AP-WEB/epg-EPG-WEB` | No static path bindings (fvRsPathAtt). |
| TN-CONSUMER | L3 BD flooding | `uni/tn-TN-CONSUMER/BD-BD-WEB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-CONSUMER-BGS | EPG without domain | `uni/tn-TN-CONSUMER-BGS/ap-AP-WEB/epg-EPG-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-CONSUMER-BGS | EPG without static path | `uni/tn-TN-CONSUMER-BGS/ap-AP-WEB/epg-EPG-WEB` | No static path bindings (fvRsPathAtt). |
| TN-CONSUMER-BGS | L3 BD flooding | `uni/tn-TN-CONSUMER-BGS/BD-BD-CONSUMER` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-ANS01 | EPG without domain | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-ANS01 | EPG without domain | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-ANS01 | EPG without domain | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-ANS01 | EPG without static path | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-APP` | No static path bindings (fvRsPathAtt). |
| TN-LAB-ANS01 | EPG without static path | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-DB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-ANS01 | EPG without static path | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-WEB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-ANS01 | L3 BD flooding | `uni/tn-TN-LAB-ANS01/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-ANS01 | L3 BD flooding | `uni/tn-TN-LAB-ANS01/BD-BD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-ANS01 | L3 BD flooding | `uni/tn-TN-LAB-ANS01/BD-BD-WEB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K01 | EPG without domain | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K01 | EPG without domain | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K01 | EPG without domain | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K01 | EPG without static path | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-APP` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K01 | EPG without static path | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-DB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K01 | EPG without static path | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-WEB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K01 | L3 BD flooding | `uni/tn-TN-LAB-K01/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K01 | L3 BD flooding | `uni/tn-TN-LAB-K01/BD-BD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K01 | L3 BD flooding | `uni/tn-TN-LAB-K01/BD-BD-WEB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K02 | Contract scope wider than used | `uni/tn-TN-LAB-K02/brc-CT-WEB-APP` | Scope 'tenant' but all users are in one VRF (tn-TN-LAB-K02/ctx-VRF-LAB). |
| TN-LAB-K02 | EPG without domain | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K02 | EPG without domain | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K02 | EPG without domain | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-WEB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-LAB-K02 | EPG without static path | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-APP` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K02 | EPG without static path | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-DB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K02 | EPG without static path | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-WEB` | No static path bindings (fvRsPathAtt). |
| TN-LAB-K02 | L3 BD flooding | `uni/tn-TN-LAB-K02/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K02 | L3 BD flooding | `uni/tn-TN-LAB-K02/BD-BD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-LAB-K02 | L3 BD flooding | `uni/tn-TN-LAB-K02/BD-BD-WE` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-PROVIDER | EPG without domain | `uni/tn-TN-PROVIDER/ap-AP-APP/epg-EPG-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROVIDER | EPG without domain | `uni/tn-TN-PROVIDER/ap-AP-APP/epg-EPG-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROVIDER | EPG without static path | `uni/tn-TN-PROVIDER/ap-AP-APP/epg-EPG-APP` | No static path bindings (fvRsPathAtt). |
| TN-PROVIDER | EPG without static path | `uni/tn-TN-PROVIDER/ap-AP-APP/epg-EPG-DB` | No static path bindings (fvRsPathAtt). |
| TN-PROVIDER | L3 BD flooding | `uni/tn-TN-PROVIDER/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-PROVIDER | L3 BD flooding | `uni/tn-TN-PROVIDER/BD-BD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-PROVIDER-BGS | EPG without domain | `uni/tn-TN-PROVIDER-BGS/ap-AP-APP/epg-EPG-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROVIDER-BGS | EPG without domain | `uni/tn-TN-PROVIDER-BGS/ap-AP-APP/epg-EPG-BD` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TN-PROVIDER-BGS | EPG without static path | `uni/tn-TN-PROVIDER-BGS/ap-AP-APP/epg-EPG-APP` | No static path bindings (fvRsPathAtt). |
| TN-PROVIDER-BGS | EPG without static path | `uni/tn-TN-PROVIDER-BGS/ap-AP-APP/epg-EPG-BD` | No static path bindings (fvRsPathAtt). |
| TN-PROVIDER-BGS | L3 BD flooding | `uni/tn-TN-PROVIDER-BGS/BD-BD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| TN-PROVIDER-BGS | L3 BD flooding | `uni/tn-TN-PROVIDER-BGS/BD-BD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Tenant2 | EPG without domain | `uni/tn-Tenant2/ap-App-XYZ/epg-EPG-B` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tenant2 | EPG without domain | `uni/tn-Tenant2/ap-App-Y/epg-EPG-B` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Tenant2 | EPG without static path | `uni/tn-Tenant2/ap-App-XYZ/epg-EPG-B` | No static path bindings (fvRsPathAtt). |
| Tenant2 | EPG without static path | `uni/tn-Tenant2/ap-App-Y/epg-EPG-B` | No static path bindings (fvRsPathAtt). |
| Test100 | EPG without domain | `uni/tn-Test100/ap-DEV/epg-D-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Test100 | EPG without domain | `uni/tn-Test100/ap-PROD/epg-P-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Test100 | EPG without domain | `uni/tn-Test100/ap-PROD/epg-P-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| Test100 | EPG without static path | `uni/tn-Test100/ap-DEV/epg-D-APP` | No static path bindings (fvRsPathAtt). |
| Test100 | EPG without static path | `uni/tn-Test100/ap-DEV/epg-D-DB` | No static path bindings (fvRsPathAtt). |
| Test100 | EPG without static path | `uni/tn-Test100/ap-PROD/epg-P-APP` | No static path bindings (fvRsPathAtt). |
| Test100 | EPG without static path | `uni/tn-Test100/ap-PROD/epg-P-DB` | No static path bindings (fvRsPathAtt). |
| Test100 | L3 BD flooding | `uni/tn-Test100/BD-DEV-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test100 | L3 BD flooding | `uni/tn-Test100/BD-DEV-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test100 | L3 BD flooding | `uni/tn-Test100/BD-PROD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Test100 | L3 BD flooding | `uni/tn-Test100/BD-PROD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| VY-TN | EPG without domain | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG03` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| VY-TN | EPG without static path | `uni/tn-VY-TN/ap-VY-AP/epg-EPG2` | No static path bindings (fvRsPathAtt). |
| VY-TN | EPG without static path | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | No static path bindings (fvRsPathAtt). |
| VY-TN | EPG without static path | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG03` | No static path bindings (fvRsPathAtt). |
| VY-TN | L3 BD flooding | `uni/tn-VY-TN/BD-VY-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| billing-test-DPYD6hPFFmE9 | EPG without domain | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-app` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| billing-test-DPYD6hPFFmE9 | EPG without domain | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| billing-test-DPYD6hPFFmE9 | EPG without domain | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-testers` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| billing-test-DPYD6hPFFmE9 | EPG without static path | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-app` | No static path bindings (fvRsPathAtt). |
| billing-test-DPYD6hPFFmE9 | EPG without static path | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-db` | No static path bindings (fvRsPathAtt). |
| billing-test-DPYD6hPFFmE9 | EPG without static path | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-testers` | No static path bindings (fvRsPathAtt). |
| billing-test-DPYD6hPFFmE9 | L3 BD flooding | `uni/tn-billing-test-DPYD6hPFFmE9/BD-bd-vlan102` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| tn_example_tenant | BD uses common VRF | `uni/tn-tn_example_tenant/BD-BIGIP_111_BD` | VRF 'default' is not in tn_example_tenant; it resolved to tn-common/ctx-default (shared-services design). |
| tn_example_tenant | BD uses common VRF | `uni/tn-tn_example_tenant/BD-BIGIP_222_BD` | VRF 'default' is not in tn_example_tenant; it resolved to tn-common/ctx-default (shared-services design). |
| tn_example_tenant | BD uses common VRF | `uni/tn-tn_example_tenant/BD-BIGIP_333_BD` | VRF 'default' is not in tn_example_tenant; it resolved to tn-common/ctx-default (shared-services design). |
| tn_example_tenant | EPG without static path | `uni/tn-tn_example_tenant/ap-app-profile/epg-201_EPG` | No static path bindings (fvRsPathAtt). |
| tn_example_tenant | L3 BD flooding | `uni/tn-tn_example_tenant/BD-BIGIP_111_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| tn_example_tenant | L3 BD flooding | `uni/tn-tn_example_tenant/BD-BIGIP_222_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| zzzps4021 | EPG without domain | `uni/tn-zzzps4021/ap-DEV/epg-D-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| zzzps4021 | EPG without domain | `uni/tn-zzzps4021/ap-PROD/epg-P-APP` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| zzzps4021 | EPG without domain | `uni/tn-zzzps4021/ap-PROD/epg-P-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| zzzps4021 | EPG without static path | `uni/tn-zzzps4021/ap-DEV/epg-D-APP` | No static path bindings (fvRsPathAtt). |
| zzzps4021 | EPG without static path | `uni/tn-zzzps4021/ap-DEV/epg-D-DB` | No static path bindings (fvRsPathAtt). |
| zzzps4021 | EPG without static path | `uni/tn-zzzps4021/ap-PROD/epg-P-APP` | No static path bindings (fvRsPathAtt). |
| zzzps4021 | EPG without static path | `uni/tn-zzzps4021/ap-PROD/epg-P-DB` | No static path bindings (fvRsPathAtt). |
| zzzps4021 | L3 BD flooding | `uni/tn-zzzps4021/BD-DEV-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| zzzps4021 | L3 BD flooding | `uni/tn-zzzps4021/BD-DEV-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| zzzps4021 | L3 BD flooding | `uni/tn-zzzps4021/BD-PROD-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| zzzps4021 | L3 BD flooding | `uni/tn-zzzps4021/BD-PROD-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| zzzps4021_BGP | EPG without domain | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG03` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| zzzps4021_BGP | EPG without static path | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-EPG2` | No static path bindings (fvRsPathAtt). |
| zzzps4021_BGP | EPG without static path | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG` | No static path bindings (fvRsPathAtt). |
| zzzps4021_BGP | EPG without static path | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG02` | No static path bindings (fvRsPathAtt). |
| zzzps4021_BGP | EPG without static path | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG03` | No static path bindings (fvRsPathAtt). |
| zzzps4021_BGP | L3 BD flooding | `uni/tn-zzzps4021_BGP/BD-VY-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| Cursor tenant1 | Integrity Cursor_tenant1: all named relations resolve | Unresolved relations: ['uni/tn-Cursor_tenant1/BD-p2bd/rsctx (state=missing-target, stateQual=none, tDn=-)'] |
| Cursor tenant1 | Integrity BD Cursor_tenant1/p2bd: VRF resolves | uni/tn-Cursor_tenant1/BD-p2bd/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| LAB-TENANT | Integrity LAB-TENANT: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message: ', 'F0467 critical: Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out '] |
| LAB-TENANT | Integrity contract LAB-TENANT/teste123: subjects and filters | Contract uni/tn-LAB-TENANT/brc-teste123 has no subjects (permits nothing) |
| Production | Integrity contract Production/BD-APP: subjects and filters | Contract uni/tn-Production/brc-BD-APP has no subjects (permits nothing) |
| Production | Integrity contract Production/BD-DB: subjects and filters | Contract uni/tn-Production/brc-BD-DB has no subjects (permits nothing) |
| RB-Tenant | Integrity RB-Tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message: '] |
| RB-Tenant | Integrity contract RB-Tenant/HTTPS: subjects and filters | Contract uni/tn-RB-Tenant/brc-HTTPS has no subjects (permits nothing) |
| RB-Tenant | Integrity contract RB-Tenant/FTP: subjects and filters | Contract uni/tn-RB-Tenant/brc-FTP has no subjects (permits nothing) |
| Tenant RG | Integrity Tenant_RG: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for node 102 due to Interface Configured as L3, debug message: port-configured-as-l3: Interface is already configured under other VRF named', 'F0467 critical: Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: vlan-1410', 'F0467 critical: |
| Test 9112026 | Integrity Test_9112026: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the Ep', 'F0467 critical: Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path', 'F0467 critical: |
| Test 9112026 | Integrity contract Test_9112026/inter-VRF_contract: subjects and filters | Contract uni/tn-Test_9112026/brc-inter-VRF_contract has no subjects (permits nothing) |
| Test 9112026 | Integrity contract Test_9112026/intra-VRF_contract: subjects and filters | Contract uni/tn-Test_9112026/brc-intra-VRF_contract has no subjects (permits nothing) |
| Test100 | Integrity Test100: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not a'] |
| Tn Example Tenant | Integrity tn_example_tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configura', 'F0467 critical: Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/6 due to Invalid Path Configuration,Invalid VLAN Configura', 'F0467 critical: |
| VY-TN | Integrity VY-TN: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not ', 'F0467 critical: Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is no', 'F0565 major: De |
| zzzps4021 BGP | Integrity zzzps4021_BGP: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does '] |

## Tenant faults (faultInst)

By severity: minor 11, major 1, warning 4, critical 18; TCA/threshold faults (context only): 3

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| VY-TN | major | F0565 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` | Deployment of EPG uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02 failed on domain test-vmm due to EPG encapsulation value is not part of any static encapsulation block for the VMM domain |
| zzzps4021_BGP | critical | F0467 | `uni/tn-zzzps4021_BGP/out-test-L3OUT` | Configuration failed for uni/tn-zzzps4021_BGP/out-test-L3OUT node 102 INT_VPC_RG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| VY-TN | critical | F0467 | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG` | Configuration failed for uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG node 102 PG-VPC-20 due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| VY-TN | critical | F0467 | `uni/tn-VY-TN/out-test-L3OUT` | Configuration failed for uni/tn-VY-TN/out-test-L3OUT node 102 eth1/30 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain |
| LAB-TENANT | critical | F0467 | `uni/tn-LAB-TENANT/out-L3OUT_TESTE` | Configuration failed for uni/tn-LAB-TENANT/out-L3OUT_TESTE node 102 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the d |
| Tenant_RG | critical | F0467 | `uni/tn-Tenant_RG/out-rg_l3_out_ext` | Configuration failed for uni/tn-Tenant_RG/out-rg_l3_out_ext node 102 eth1/38 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the |
| Test_9112026 | critical | F0467 | `uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-CSP-PSNXXXX_L3Out node 102 eth1/3 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain  |
| Tenant_RG | critical | F0467 | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for node 102 due to Interface Configured as L3, debug message: port-configured-as-l3: Interface is already configured under other VRF named LAB-TENANT:LAB-VRF; |
| tn_example_tenant | critical | F0467 | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_20 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-111 :Either the EpG is not  |
| tn_example_tenant | critical | F0467 | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-HON_BIGIP_111_EPG node 102 vPC_19 due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-222 :Either the EpG is not  |
| tn_example_tenant | critical | F0467 | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan- |
| tn_example_tenant | critical | F0467 | `uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG` | Configuration failed for uni/tn-tn_example_tenant/ap-HON_BIGIP_AP/epg-DEV_BIGIP_333_EPG node 102 eth1/6 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan- |
| Test_9112026 | critical | F0467 | `uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS-STRE-SHRP01-PSN-COLL_L3Out node 101 eth1/15 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated |
| RB-Tenant | critical | F0467 | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` | Configuration failed for uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG due to VRF Not Present, debug message:  |
| LAB-TENANT | critical | F0467 | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` | Configuration failed for uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG due to VRF Not Present, debug message:  |
| Tenant_RG | critical | F0467 | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` | Configuration failed for uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2 node 101 eth1/4 due to Invalid Path Configuration, debug message: invalid-path: vlan-1410 :There is no domain, associated with bo |
| Test100 | critical | F0467 | `uni/tn-Test100/out-L3out` | Configuration failed for uni/tn-Test100/out-L3out node 101 eth1/12 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain do |
| tenant_mylab | critical | F0467 | `uni/tn-tenant_mylab/out-ok` | Configuration failed for uni/tn-tenant_mylab/out-ok node 101 eth1/40 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain  |
| Test_9112026 | critical | F0467 | `uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out` | Configuration failed for uni/tn-Test_9112026/out-IAAS1-PSNXXXX_L3Out node 101 eth1/11 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a doma |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
