# ACI tenant logical-integrity report: 2026-10-23

## BROKEN RELATIONS FOUND - 38 broken, 48 warnings (9 of 22 tenants broken: DEV, Heroes, MUHC, POC-LN, SnV, T1, TN-DEDUP-LAB, hacki-tn-a, lab-t01)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-10-23 08:10:28 AEDT)
- Generated: 2026-10-23 08:11:44 AEDT
- Scope: 22 tenants on the APIC (9 in baseline, new: Cursor_tenant1, Cursor_Tenant2, Cursor_Tenant3, Demo1, DEV, hacki-tn-a, LAB-InterVRF, LAB-MEIRLAN, lab-t01, LAB_ASN_01, LAB_ASN_02, POC-LN, T1); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 211 tests, 201 passed, 10 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| common | yes | 2 | 1 | 0 | 1 | 0 | 4 | 1 | 0 | 0 | 0 | 100 | HEALTHY |
| Cursor_tenant1 | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Cursor_Tenant2 | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Cursor_Tenant3 | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| Demo1 | NEW | 2 | 2 | 4 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| DEV | NEW | 1 | 3 | 3 | 1 | 3 | 3 | 0 | 3 | 1 | 6 | 67 | BROKEN |
| hacki-tn-a | NEW | 5 | 2 | 2 | 1 | 3 | 4 | 3 | 1 | 12 | 1 | 54 | BROKEN |
| Heroes | yes | 1 | 1 | 2 | 1 | 3 | 0 | 1 | 3 | 0 | 12 | 70 | BROKEN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| LAB-InterVRF | NEW | 2 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| LAB-MEIRLAN | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| lab-t01 | NEW | 2 | 4 | 4 | 1 | 4 | 4 | 1 | 1 | 4 | 1 | 78 | BROKEN |
| LAB_ASN_01 | NEW | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| LAB_ASN_02 | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| mgmt | yes | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| MUHC | yes | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 4 | 1 | 0 | 57 | BROKEN |
| oneaciapp | yes | 1 | 1 | 0 | 1 | 3 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| POC-LN | NEW | 1 | 4 | 3 | 1 | 4 | 4 | 0 | 10 | 2 | 10 | 0 | BROKEN |
| ROR | yes | 1 | 2 | 4 | 1 | 2 | 3 | 0 | 0 | 3 | 0 | 91 | WARN |
| SnV | yes | 1 | 1 | 1 | 4 | 8 | 2 | 0 | 4 | 1 | 4 | 57 | BROKEN |
| T1 | NEW | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 2 | 74 | BROKEN |
| TN-DEDUP-LAB | yes | 1 | 1 | 1 | 1 | 9 | 21 | 2 | 10 | 4 | 0 | 0 | BROKEN |

## Broken relations (38)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| DEV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-DEV/ap-VLANS/epg-VLAN200` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN200 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| DEV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-DEV/ap-VLANS/epg-VLAN201` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN201 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| DEV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-DEV/ap-VLANS/epg-VLAN202` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN202 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-202 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| Heroes | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-200 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| MUHC | BD L3Out missing-target | `uni/tn-MUHC/BD-VLAN_2014_BD` | BD is associated to L3Out 'LEGACY_L3OUT' which does not exist; APIC fell back to tn-common/out-default, so the BD subnets are not advertised as intended. | Create L3Out 'LEGACY_L3OUT' or remove the BD-to-L3Out association. |
| MUHC | BD VRF missing-target | `uni/tn-MUHC/BD-VLAN_2014_BD` | BD points to VRF 'LEGACY_VRF' which does not exist in tenant MUHC or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'LEGACY_VRF' in MUHC (or common), or point the BD to an existing VRF. |
| MUHC | EPG BD missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG` | EPG points to BD 'VLAN_2781_BD' which does not exist (state missing-target). | Create BD 'VLAN_2781_BD' or fix the EPG's bridge_domain. |
| MUHC | EPG domain missing-target | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG` | Domain uni/phys-LEGACY_SRVF_PHY does not exist (state missing-target). | Create domain uni/phys-LEGACY_SRVF_PHY (with VLAN pool/AAEP) or associate an existing one. |
| POC-LN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP` | Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-apic: Port is connected to the APIC; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| POC-LN | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB` | Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-apic: Port is connected to the APIC; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-46:CD:BB:C0:00:00/ip-[10.193.101.5]` | In Tenant POC-LN, 10.193.101.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-46:CD:BB:C0:00:00/ip-[2222::65:5]` | In Tenant POC-LN, 2222::65:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP c | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-47:CD:BB:C0:00:00/ip-[10.193.102.5]` | In Tenant POC-LN, 10.193.102.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-47:CD:BB:C0:00:00/ip-[2222::66:5]` | In Tenant POC-LN, 2222::66:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP c | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00/ip-[10.193.101.5]` | In Tenant POC-LN, 10.193.101.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00/ip-[2222::65:5]` | In Tenant POC-LN, 2222::65:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP c | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00/ip-[10.193.102.5]` | In Tenant POC-LN, 10.193.102.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP | See the APIC fault description and resolve the referenced object. |
| POC-LN | Major fault F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00/ip-[2222::66:5]` | In Tenant POC-LN, 2222::66:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs                     are sourcing traffic with the same IP due to NIC teaming, duplicate external IP c | See the APIC fault description and resolve the referenced object. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| SnV | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1B; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| T1 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-T1/ap-User_App_Profile/epg-Users_EPG` | Configuration failed for uni/tn-T1/ap-User_App_Profile/epg-Users_EPG node 102 eth1/28 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-60 :STP Segment Id not present for Encap. Either the EpG is not associated with a domain or the domain does not have t | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| T1 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-T1/out-L3_OUT_FW` | Configuration failed for uni/tn-T1/out-L3_OUT_FW node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
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
| hacki-tn-a | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-hacki-tn-a/out-L3-OSPF-500` | Configuration failed for uni/tn-hacki-tn-a/out-L3-OSPF-500 node 101 eth1/21 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-500 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: Either th | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| lab-t01 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-lab-t01/out-out-fw` | Configuration failed for uni/tn-lab-t01/out-out-fw node 101 eth1/33 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain does not have this interface assigned to it; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (48)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| Cursor_Tenant2 | EPG isolated (no contracts) | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_Tenant3 | EPG isolated (no contracts) | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Cursor_tenant1 | EPG isolated (no contracts) | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| DEV | Contract unused | `uni/tn-DEV/brc-SSH-CONTRACT` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| Demo1 | EPG isolated (no contracts) | `uni/tn-Demo1/ap-ap-demo1/epg-epg-vlan300-web-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Demo1 | EPG isolated (no contracts) | `uni/tn-Demo1/ap-ap-demo1/epg-epg-vlan301-dab-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| LAB-InterVRF | AP without EPGs | `uni/tn-LAB-InterVRF/ap-apInterVRF` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| LAB-InterVRF | BD unused | `uni/tn-LAB-InterVRF/BD-bdAdministracion` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| LAB-InterVRF | BD unused | `uni/tn-LAB-InterVRF/BD-bdAplicacion` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| LAB-MEIRLAN | Tenant empty | `uni/tn-LAB-MEIRLAN` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| LAB_ASN_01 | BD unused | `uni/tn-LAB_ASN_01/BD-BD1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| LAB_ASN_01 | VRF unused | `uni/tn-LAB_ASN_01/ctx-ASN02` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| LAB_ASN_01 | VRF unused | `uni/tn-LAB_ASN_01/ctx-ASN03` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| LAB_ASN_02 | VRF unused | `uni/tn-LAB_ASN_02/ctx-NewASN` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| MUHC | BD unused | `uni/tn-MUHC/BD-VLAN_2014_BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| POC-LN | Contract provided, never consumed | `uni/tn-POC-LN/brc-CON-POC-WEB` | Provided by 1 object(s) (e.g. tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| POC-LN | vzAny contract | `uni/tn-POC-LN/ctx-VRF-POC-PROD` | vzAny provides 1 / consumes 1 contract(s) (CON-POC-ICMP); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-ALLOW_ICMP_Ct` | Provided by 1 object(s) (e.g. tn-ROR/ctx-ROR_VRF/any) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | Contract provided, never consumed | `uni/tn-ROR/brc-WEB_TO_OUTSIDE` | Provided by 1 object(s) (e.g. tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| ROR | vzAny contract | `uni/tn-ROR/ctx-ROR_VRF` | vzAny provides 1 / consumes 0 contract(s) (ALLOW_ICMP_Ct); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| SnV | Contract provided, never consumed | `uni/tn-SnV/brc-web` | Provided by 4 object(s) (e.g. tn-SnV/ap-Chaos/epg-Web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| T1 | BD unused | `uni/tn-T1/BD-Bd1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| T1 | L3 BD without subnet | `uni/tn-T1/BD-Bd1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-DNS: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-DNS-FW (keep tn-TN-DEDUP-LAB/brc-C-DNS). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-MONITORING: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD (keep tn-TN-DEDUP-LAB/brc-C-MONITORING). |
| TN-DEDUP-LAB | Duplicate contract | `uni/tn-TN-DEDUP-LAB/brc-C-NTP-FW` | Same filters, providers and consumers as tn-TN-DEDUP-LAB/brc-C-NTP: the contract is redundant. | Delete tn-TN-DEDUP-LAB/brc-C-NTP-FW (keep tn-TN-DEDUP-LAB/brc-C-NTP). |
| TN-DEDUP-LAB | vzAny contract | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` | vzAny provides 0 / consumes 2 contract(s) (C-SMTP, C-SMTP-FW); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| hacki-tn-a | Config fault F1386 | `uni/tn-hacki-tn-a/BD-hacki-bd2` | ARP flooding must be enabled when L2 unknown unicast is set to flood | See the APIC fault description and resolve the referenced object. |
| hacki-tn-a | Config fault F2069 | `uni/tn-hacki-tn-a/out-L3-OSPF-505/lnodep-L3-OSPF-505_nodeProfile` | Configuration failed for Tenant hacki-tn-a, Name L3-OSPF-505, Logical Node Profile L3-OSPF-505_nodeProfile due to RsNodeL3OutAtt RsPathL3OutAtt Misconfiguration | See the APIC fault description and resolve the referenced object. |
| hacki-tn-a | Config fault F2069 | `uni/tn-hacki-tn-a/out-L3-OSPF-509/lnodep-L3-OSPF-509_nodeProfile` | Configuration failed for Tenant hacki-tn-a, Name L3-OSPF-509, Logical Node Profile L3-OSPF-509_nodeProfile due to RsNodeL3OutAtt RsPathL3OutAtt Misconfiguration | See the APIC fault description and resolve the referenced object. |
| hacki-tn-a | Contract provided, never consumed | `uni/tn-hacki-tn-a/brc-web` | Provided by 1 object(s) (e.g. tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-web) but no consumer, so it permits no flow. | Add the consumer EPG(s) or remove the provider relation. |
| hacki-tn-a | Contract unused | `uni/tn-hacki-tn-a/brc-mgmt` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| hacki-tn-a | External EPG without contracts | `uni/tn-hacki-tn-a/out-L3-OSPF-500/instP-L3-OSPF-500-extEpg` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| hacki-tn-a | External EPG without contracts | `uni/tn-hacki-tn-a/out-L3-OSPF-505/instP-L3-OSPF-505-extEpg` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| hacki-tn-a | External EPG without contracts | `uni/tn-hacki-tn-a/out-L3-OSPF-509/instP-L3-OSPF-509-extEpg` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| hacki-tn-a | VRF unused | `uni/tn-hacki-tn-a/ctx-hacki-vrf2` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| hacki-tn-a | VRF unused | `uni/tn-hacki-tn-a/ctx-hacki-vrf3` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| hacki-tn-a | VRF unused | `uni/tn-hacki-tn-a/ctx-hacki-vrf5` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| hacki-tn-a | VRF unused | `uni/tn-hacki-tn-a/ctx-hacki-vrf6` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| lab-t01 | Config fault F1021 | `uni/tn-lab-t01/out-out-fw/rsl3DomAtt` | Failed to form relation to MO uni/l3dom-all-tenant-vrfs of class extnwDomP | See the APIC fault description and resolve the referenced object. |
| lab-t01 | EPG isolated (no contracts) | `uni/tn-lab-t01/ap-ap-01/epg-epg-b` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| lab-t01 | EPG isolated (no contracts) | `uni/tn-lab-t01/ap-ap-01/epg-epg-shared` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| lab-t01 | vzAny contract | `uni/tn-lab-t01/ctx-vrf-a` | vzAny provides 1 / consumes 1 contract(s) (c-icmp); this applies to EVERY EPG and external EPG in the VRF. | Confirm the vzAny relation is intended (common for shared services such as DNS/NTP/ICMP); keep its filters specific. |
| mgmt | BD unused | `uni/tn-mgmt/BD-inb` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | L3 BD without subnet | `uni/tn-mgmt/BD-inb` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-x/epg-2323323` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-x/epg-234` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-x/epg-x` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 38 broken relation(s) in 9 tenant(s): Critical fault F0467 (EPG deployment on path failed) (16); Contract service graph not instantiated (10); Major fault F3083 (8); BD L3Out missing-target (1); BD VRF missing-target (1); EPG BD missing-target (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 1 (e.g. tn-common/brc-default); vzAny contract: 4 (e.g. tn-POC-LN/ctx-VRF-POC-PROD, tn-ROR/ctx-ROR_VRF)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract provided, never consumed: 5 (e.g. tn-POC-LN/brc-CON-POC-WEB, tn-ROR/brc-ALLOW_ICMP_Ct); Contract unused: 3 (e.g. tn-DEV/brc-SSH-CONTRACT, tn-hacki-tn-a/brc-mgmt); EPG isolated (no contracts): 10 (e.g. tn-Cursor_Tenant2/ap-cursor2_ap/epg-web, tn-Cursor_Tenant3/ap-cursor3_ap/epg-web); External EPG without contracts: 3 (e.g. tn-hacki-tn-a/out-L3-OSPF-500/instP-L3-OSPF-500-extEpg, tn-hacki-tn-a/out-L3-OSPF-505/instP-L3-OSPF-505-extEpg); Duplicate contract: 3 (e.g. tn-TN-DEDUP-LAB/brc-C-DNS-FW, tn-TN-DEDUP-LAB/brc-C-MONITORING-OLD)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 3 (e.g. tn-T1/BD-Bd1, tn-mgmt/BD-inb); L3 BD flooding: 15 (e.g. tn-Cursor_Tenant2/BD-cursor2_bd, tn-Cursor_Tenant3/BD-cursor3_bd)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
5. **Clean up unused objects** - found: Tenant empty: 1; VRF unused: 9; BD unused: 7; AP without EPGs: 2; Filter unused: 2; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
6. **Add descriptions** - found: 178 of 213 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
7. **Tag ownership (annotations) for NaC** - found: 103 of 213 objects have no annotation; in use: 'orchestrator:ansible' x96, 'orchestrator:terraform' x14.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
8. **Adopt one naming convention** - found: name styles in use: UPPER_SNAKE 92, Mixed 42, lower 79; 7 generic/VLAN/IP-style names (e.g. tn-DEV/BD-10.1.200.0_24, tn-DEV/BD-10.1.201.0_24, tn-DEV/BD-10.1.202.0_24, tn-DEV/ap-VLANS/epg-VLAN200, tn-DEV/ap-VLANS/epg-VLAN201).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
9. **Bind EPGs to a domain** - found: no domain: 22, missing domain: 1  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (82)

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
| DEV | L3 BD flooding | `uni/tn-DEV/BD-10.1.200.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| DEV | L3 BD flooding | `uni/tn-DEV/BD-10.1.201.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| DEV | L3 BD flooding | `uni/tn-DEV/BD-10.1.202.0_24` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| Demo1 | L3 BD flooding | `uni/tn-Demo1/BD-bd-vlan300-web-demo1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Demo1 | L3 BD flooding | `uni/tn-Demo1/BD-bd-vlan301-dab-demo1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG provides 'power_up' resolved to tn-common/brc-power_up. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | EPG provides 'sql' resolved to tn-common/brc-sql. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG provides 'web' resolved to tn-common/brc-web. |
| Heroes | EPG uses common contract | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | EPG consumes 'sql' resolved to tn-common/brc-sql. |
| LAB-InterVRF | L3 BD flooding | `uni/tn-LAB-InterVRF/BD-bdAdministracion` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| LAB-InterVRF | L3 BD flooding | `uni/tn-LAB-InterVRF/BD-bdAplicacion` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| LAB_ASN_01 | L3 BD flooding | `uni/tn-LAB_ASN_01/BD-BD1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MUHC | EPG without static path | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG` | No static path bindings (fvRsPathAtt). |
| POC-LN | EPG only via vzAny | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY` | EPG has no own contracts; it only inherits the VRF's vzAny contracts. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without domain | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | EPG without static path | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` | No static path bindings (fvRsPathAtt). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_DB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| ROR | L3 BD flooding | `uni/tn-ROR/BD-ROR_WEB_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SnV | Contract scope limits pairs | `uni/tn-SnV/brc-database` | Scope 'application-profile' blocks 12 of 16 provider/consumer combinations (e.g. tn-SnV/ap-Power_Up/epg-Database -> tn-SnV/ap-Chaos/epg-Web); every user still has an in-scope partner. |
| T1 | EPG without domain | `uni/tn-T1/ap-User_App_Profile/epg-Users_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| T1 | L3 BD flooding | `uni/tn-T1/BD-BD2` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
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
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | BD unused | `uni/tn-common/BD-default` | No EPG is attached to this bridge domain. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | L3Out without external EPG | `uni/tn-common/out-default` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| hacki-tn-a | EPG without static path | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-DB` | No static path bindings (fvRsPathAtt). |
| hacki-tn-a | EPG without static path | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-back` | No static path bindings (fvRsPathAtt). |
| hacki-tn-a | EPG without static path | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-web` | No static path bindings (fvRsPathAtt). |
| hacki-tn-a | L3 BD flooding | `uni/tn-hacki-tn-a/BD-hacki-bd2` | Routed BD with arpFlood=no, unkMacUcastAct=flood (legacy/migration style). |
| lab-t01 | BD uses common VRF | `uni/tn-lab-t01/BD-bd-shared` | VRF 'default' is not in lab-t01; it resolved to tn-common/ctx-default (shared-services design). |
| lab-t01 | EPG without domain | `uni/tn-lab-t01/ap-ap-01/epg-epg-b` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| lab-t01 | EPG without domain | `uni/tn-lab-t01/ap-ap-01/epg-epg-db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| lab-t01 | EPG without domain | `uni/tn-lab-t01/ap-ap-01/epg-epg-shared` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| lab-t01 | EPG without domain | `uni/tn-lab-t01/ap-ap-01/epg-epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| lab-t01 | EPG without static path | `uni/tn-lab-t01/ap-ap-01/epg-epg-b` | No static path bindings (fvRsPathAtt). |
| lab-t01 | EPG without static path | `uni/tn-lab-t01/ap-ap-01/epg-epg-db` | No static path bindings (fvRsPathAtt). |
| lab-t01 | EPG without static path | `uni/tn-lab-t01/ap-ap-01/epg-epg-shared` | No static path bindings (fvRsPathAtt). |
| lab-t01 | EPG without static path | `uni/tn-lab-t01/ap-ap-01/epg-epg-web` | No static path bindings (fvRsPathAtt). |
| lab-t01 | Filter unused | `uni/tn-lab-t01/flt-flt-telnet` | Filter is not referenced by any contract subject. |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-x/epg-2323323` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-x/epg-234` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-x/epg-x` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-x/epg-2323323` | No static path bindings (fvRsPathAtt). |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-x/epg-234` | No static path bindings (fvRsPathAtt). |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-x/epg-x` | No static path bindings (fvRsPathAtt). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| DEV | Integrity DEV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN200 node 101 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface do', 'F0467 critical: Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN200 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface do', 'F0467 critical: |
| Hacki-Tn-A | Integrity hacki-tn-a: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-hacki-tn-a/out-L3-OSPF-500 node 101 eth1/21 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid'] |
| Heroes | Integrity Heroes: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201', 'F0467 critical: Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201', 'F0467 critical: |
| Lab-T01 | Integrity lab-t01: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-lab-t01/out-out-fw node 101 eth1/33 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not '] |
| MUHC | Integrity MUHC: all named relations resolve | Unresolved relations: ['uni/tn-MUHC/BD-VLAN_2014_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2780_BD/rsctx (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-MUHC/BD-VLAN_2014_BD/rsBDToOut-LEGACY_L3OUT (state=formed, stateQual=mismatch-target, tDn=uni/tn-common/out-default)', 'uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG/rsdomAtt-[uni/phys-LEGACY_SRVF_PHY] (st |
| MUHC | Integrity BD MUHC/VLAN_2014_BD: VRF resolves | uni/tn-MUHC/BD-VLAN_2014_BD/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| MUHC | Integrity EPG MUHC/LEGACY_APR/VLAN_2781_EPG: BD and VRF chain resolves | uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG/rsbd is 'missing-target' (target fvBD not found): missing-target != formed |
| POC-LN | Integrity POC-LN: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-a', 'F0467 critical: Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-ap', 'F3083 major: In |
| SnV | Integrity SnV: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is p', 'F0467 critical: Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Por', 'F0467 critical: |
| T1 | Integrity T1: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-T1/ap-User_App_Profile/epg-Users_EPG node 102 eth1/28 due to Invalid Path Configuration,Invalid VLAN Configuration, debug messag', 'F0467 critical: Configuration failed for uni/tn-T1/out-L3_OUT_FW node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not as'] |

## Tenant faults (faultInst)

By severity: warning 36, minor 44, major 8, critical 28; TCA/threshold faults (context only): 31

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-46:CD:BB:C0:00:00/ip-[2222::65:5]` | In Tenant POC-LN, 2222::65:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs   |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-46:CD:BB:C0:00:00/ip-[10.193.101.5]` | In Tenant POC-LN, 10.193.101.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00/ip-[2222::65:5]` | In Tenant POC-LN, 2222::65:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs   |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00/ip-[10.193.101.5]` | In Tenant POC-LN, 10.193.101.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-46:CD:BB:C0:00:00;). This can happen when different MACs |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00/ip-[2222::66:5]` | In Tenant POC-LN, 2222::66:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs   |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00/ip-[10.193.102.5]` | In Tenant POC-LN, 10.193.102.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-47:CD:BB:C0:00:00/ip-[2222::66:5]` | In Tenant POC-LN, 2222::66:5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs   |
| POC-LN | major | F3083 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY/cep-47:CD:BB:C0:00:00/ip-[10.193.102.5]` | In Tenant POC-LN, 10.193.102.5 is detected on multiple MACs (Context: 2424832. First 3 fvCEps: uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB/cep-47:CD:BB:C0:00:00;). This can happen when different MACs |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-200 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-202 :Either the EpG is not associated with a |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 102 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 102 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-200 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 102 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-202 :Either the EpG is not associated with a |
| T1 | critical | F0467 | `uni/tn-T1/ap-User_App_Profile/epg-Users_EPG` | Configuration failed for uni/tn-T1/ap-User_App_Profile/epg-Users_EPG node 102 eth1/28 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-60 :STP Segment Id |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN201` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN201 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN202` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN202 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN200` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN200 node 102 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Chaos/epg-Web` | Configuration failed for uni/tn-SnV/ap-Chaos/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI-1 |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Power_Up/epg-Web` | Configuration failed for uni/tn-SnV/ap-Power_Up/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_F |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Rescue/epg-Web` | Configuration failed for uni/tn-SnV/ap-Rescue/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name SnV_FI- |
| SnV | critical | F0467 | `uni/tn-SnV/ap-Evolution_X/epg-Web` | Configuration failed for uni/tn-SnV/ap-Evolution_X/epg-Web node 101 eth1/10 due to Port is Member of Port Channel, debug message: port-part-of-port-channel: Port is part of a port-channel with name Sn |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-202 :Either the EpG is not associated with a |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-200 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-app node 101 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-201 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-web node 101 Heroes_FI-2A due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-200 :Either the EpG is not associated with  |
| Heroes | critical | F0467 | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` | Configuration failed for uni/tn-Heroes/ap-Save_The_Planet/epg-db node 101 Heroes_FI-2B due to Invalid VLAN Configuration, debug message: invalid-vlan: vlan-202 :Either the EpG is not associated with a |
| T1 | critical | F0467 | `uni/tn-T1/out-L3_OUT_FW` | Configuration failed for uni/tn-T1/out-L3_OUT_FW node 101 eth1/27 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain doe |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN200` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN200 node 101 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| hacki-tn-a | critical | F0467 | `uni/tn-hacki-tn-a/out-L3-OSPF-500` | Configuration failed for uni/tn-hacki-tn-a/out-L3-OSPF-500 node 101 eth1/21 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-500 :Either the EpG is not a |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN201` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN201 node 101 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| DEV | critical | F0467 | `uni/tn-DEV/ap-VLANS/epg-VLAN202` | Configuration failed for uni/tn-DEV/ap-VLANS/epg-VLAN202 node 101 DEV-SERVER-VPC-PG due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| POC-LN | critical | F0467 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP` | Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-apic: Port is connected to the APIC; |
| POC-LN | critical | F0467 | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB` | Configuration failed for uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB node 101 eth1/41 due to Port Connected to Controller, debug message: port-configured-for-apic: Port is connected to the APIC; |
| lab-t01 | critical | F0467 | `uni/tn-lab-t01/out-out-fw` | Configuration failed for uni/tn-lab-t01/out-out-fw node 101 eth1/33 due to Invalid Path Configuration, debug message: invalid-path: Either the EpG/L3Out is not associated with a domain or the domain d |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
