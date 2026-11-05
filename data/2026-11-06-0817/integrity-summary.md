# ACI tenant logical-integrity report: 2026-11-06

## BROKEN RELATIONS FOUND - 12 broken, 68 warnings (8 of 27 tenants broken: ASN_550, My-Tenant, TEST_TENANT, iTenant, mgmt, oneaciapp, task_ansible_aci_6th, test)

- APIC: https://sandboxapicdc.cisco.com (snapshot 2026-11-06 08:18:14 AEDT)
- Generated: 2026-11-06 08:18:35 AEDT
- Scope: 27 tenants on the APIC (4 in baseline, new: AAL001, ASN_550, CiscoU-Tenant-03, CiscoU-Tenant-04, Demo1, dev-demo, global-NBK-Tenant, iacdemo-contractors, iacdemo-prod, iTenant, juan, L3TenantL, MOJ_TENANAT, My-Tenant, NP-DEMO, SCADAAA, T1_VMM, task_ansible_aci_6th, TeamTest-Bakker, TECCRT-3778-01, TECCRT-3778-02, test, TF_LAB_SAMAN); infra checked for broken relations + critical/major faults only
- Graph: tenant -> VRF -> BD -> subnet -> AP -> EPG -> contract -> subject -> filter -> entry, plus vzAny, L3Out/external EPG, domains, service graphs, faults

- nac-test integrity suite (templates/tests/integrity): 146 tests, 134 passed, 12 failed

## Per-tenant scorecard

| Tenant | Baseline | VRF | BD | Subnet | AP | EPG | Contract | L3Out | Broken | Warn | Crit/Major faults | Score | Status |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AAL001 | NEW | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| ASN_550 | NEW | 1 | 1 | 4 | 1 | 1 | 0 | 0 | 1 | 1 | 2 | 87 | BROKEN |
| CiscoU-Tenant-03 | NEW | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| CiscoU-Tenant-04 | NEW | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| common | yes | 2 | 2 | 1 | 1 | 0 | 6 | 1 | 0 | 10 | 0 | 70 | WARN |
| Demo1 | NEW | 1 | 2 | 2 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 91 | WARN |
| dev-demo | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| global-NBK-Tenant | NEW | 1 | 2 | 2 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-contractors | NEW | 1 | 1 | 1 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| iacdemo-prod | NEW | 1 | 4 | 4 | 2 | 5 | 0 | 0 | 0 | 5 | 0 | 85 | WARN |
| infra | yes | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| iTenant | NEW | 1 | 1 | 1 | 2 | 3 | 1 | 0 | 1 | 4 | 0 | 78 | BROKEN |
| juan | NEW | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| L3TenantL | NEW | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 97 | WARN |
| mgmt | yes | 2 | 4 | 4 | 1 | 1 | 2 | 1 | 2 | 3 | 1 | 71 | BROKEN |
| MOJ_TENANAT | NEW | 1 | 1 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 100 | HEALTHY |
| My-Tenant | NEW | 1 | 3 | 3 | 1 | 3 | 0 | 0 | 1 | 4 | 1 | 78 | BROKEN |
| NP-DEMO | NEW | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| oneaciapp | yes | 2 | 4 | 4 | 2 | 4 | 1 | 1 | 4 | 4 | 0 | 48 | BROKEN |
| SCADAAA | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 97 | WARN |
| T1_VMM | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |
| task_ansible_aci_6th | NEW | 1 | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 84 | BROKEN |
| TeamTest-Bakker | NEW | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 0 | 2 | 0 | 94 | WARN |
| TECCRT-3778-01 | NEW | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 0 | 8 | 0 | 76 | WARN |
| TECCRT-3778-02 | NEW | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 4 | 0 | 88 | WARN |
| test | NEW | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 87 | BROKEN |
| TF_LAB_SAMAN | NEW | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 94 | WARN |

## Broken relations (12)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| ASN_550 | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-211 :Either the EpG is not associated with a domain or the domain does not have this vlan assigned to it;invalid-path: E | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| My-Tenant | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-10 :There is no domain, associated with both EPG and Port, that has required VLAN; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| TEST_TENANT | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1` | Configuration failed for uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1 due to VRF Not Present, debug message:  | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| iTenant | Contract without subjects | `uni/tn-iTenant/brc-contract_webserver-to-database` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| mgmt | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-mgmt/out-inb_L3Out` | Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |
| mgmt | Subject without filters | `uni/tn-mgmt/brc-MOJ_CT_AP_vC/subj-MOJ_SUBJ_AP_vC` | Contract subject has no filter, so it permits nothing. | Attach specific filters to the subject. |
| oneaciapp | Contract without subjects | `uni/tn-oneaciapp/brc-ESG` | Contract has no subject, so it permits nothing. | Add a subject with specific filters, or delete the contract. |
| oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-APP` | EPG consumes contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target). | Create contract 'APP-To-DB' or remove the relation. |
| oneaciapp | EPG contract missing-target | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` | EPG provides contract 'APP-To-DB' which does not exist in oneaciapp or common (state missing-target). | Create contract 'APP-To-DB' or remove the relation. |
| oneaciapp | External EPG contract missing-target | `uni/tn-oneaciapp/out-L3out/instP-externalepg-3` | External EPG uses contract 'APP-To-DB' which does not exist. | Create the contract or remove the relation. |
| task_ansible_aci_6th | BD VRF missing-target | `uni/tn-task_ansible_aci_6th/BD-BD_TEST` | BD points to VRF 'VRF_BLUE' which does not exist in tenant task_ansible_aci_6th or in tenant common (state missing-target). The BD and every EPG in it cannot be deployed. | Create VRF 'VRF_BLUE' in task_ansible_aci_6th (or common), or point the BD to an existing VRF. |
| test | Critical fault F0467 (EPG deployment on path failed) | `uni/tn-test/ap-test/epg-test` | Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan-10) is already in use by My-Tenant:My-APP-Profile:My-DB-EPG;invalid-path: Either the EpG/L3Out is not associated | Check the static path: interface policy group/AAEP, VLAN pool and domain must allow the EPG's encap on that port. |

## Warnings (68)

| Tenant | Check | Object DN | Why | Fix |
|---|---|---|---|---|
| AAL001 | VRF unused | `uni/tn-AAL001/ctx-VRF1` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| AAL001 | VRF unused | `uni/tn-AAL001/ctx-VRF2` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| ASN_550 | EPG isolated (no contracts) | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| CiscoU-Tenant-03 | BD unused | `uni/tn-CiscoU-Tenant-03/BD-CiscoU-Tenant-03-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| CiscoU-Tenant-04 | BD unused | `uni/tn-CiscoU-Tenant-04/BD-CiscoU-Tenant-04-BD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Demo1 | BD unused | `uni/tn-Demo1/BD-bd-dab-demo1` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| Demo1 | EPG isolated (no contracts) | `uni/tn-Demo1/ap-app-demo1/epg-epg-vlan300-web-demo1` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| Demo1 | L3 BD without subnet | `uni/tn-Demo1/BD-bd-dab-demo1` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| L3TenantL | L3Out without external EPG | `uni/tn-L3TenantL/out-L3out` | L3Out has no external EPG (l3extInstP), so no external prefix is classified and no contract can apply. | Add an external EPG with the external subnets and contracts. |
| My-Tenant | EPG isolated (no contracts) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-APP-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| My-Tenant | EPG isolated (no contracts) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| My-Tenant | EPG isolated (no contracts) | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-WEB-EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| My-Tenant | L3 BD without subnet | `uni/tn-My-Tenant/BD-My-app` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| NP-DEMO | AP without EPGs | `uni/tn-NP-DEMO/ap-APP-NP` | Application profile contains no EPG. | Remove the empty application profile or add its EPGs. |
| NP-DEMO | VRF unused | `uni/tn-NP-DEMO/ctx-VRF-NP` | No bridge domain or L3Out is attached to this VRF. | Remove the VRF or attach the BDs that should live in it. |
| SCADAAA | EPG isolated (no contracts) | `uni/tn-SCADAAA/ap-SCADA_AP/epg-SCADA_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| T1_VMM | EPG isolated (no contracts) | `uni/tn-T1_VMM/ap-APP_PROFILE/epg-EPG1_USERS` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| T1_VMM | L3 BD without subnet | `uni/tn-T1_VMM/BD-BD_VMM` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). | Add the gateway subnet, or disable unicast routing if the BD is meant to be Layer-2 only. |
| TECCRT-3778-01 | EPG BD fallback to common | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG01` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-01 | EPG BD fallback to common | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG02` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-01 | EPG BD fallback to common | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG03` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-01 | EPG BD fallback to common | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG04` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-01 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG01` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TECCRT-3778-01 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG02` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TECCRT-3778-01 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG03` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TECCRT-3778-01 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG04` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TECCRT-3778-02 | EPG BD fallback to common | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG05` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-02 | EPG BD fallback to common | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG06` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TECCRT-3778-02 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG05` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TECCRT-3778-02 | EPG isolated (no contracts) | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG06` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| TF_LAB_SAMAN | BD unused | `uni/tn-TF_LAB_SAMAN/BD-BD_10` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| TF_LAB_SAMAN | L2 BD settings | `uni/tn-TF_LAB_SAMAN/BD-BD_10` | Layer-2 BD with arpFlood=yes, unkMacUcastAct=proxy; silent hosts may be unreachable. | For L2-only BDs use ARP flooding = yes and L2 unknown unicast = flood. |
| TeamTest-Bakker | EPG BD fallback to common | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-app` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| TeamTest-Bakker | EPG BD fallback to common | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-web` | EPG has no BD name and falls back to tn-common/BD-default. | Set the BD explicitly on the EPG. |
| common | Config fault F1690 | `uni/tn-common/lDevVip-PAN_FW/vnsConfIssue-missing-cdev` | Configuration is invalid due to No device found in cluster. | See the APIC fault description and resolve the referenced object. |
| common | Config fault F1690 | `uni/tn-common/lDevVip-PAN_FW/vnsConfIssue-missing-lif` | Configuration is invalid due to no cluster interface found | See the APIC fault description and resolve the referenced object. |
| common | Config fault F1690 | `uni/tn-common/lDevVip-PAN_FW/vnsConfIssue-missing-namespace` | Configuration is invalid due to no vlan/vxlan namespace found | See the APIC fault description and resolve the referenced object. |
| common | Contract consumed, never provided | `uni/tn-common/brc-CT-PAN-NS` | Consumed by 1 object(s) (e.g. tn-dev-demo/ap-AP-PBR/epg-EPG-INTERNAL-POC) but no provider, so it permits no flow. | Add the provider EPG(s) or remove the consumer relation. |
| common | Contract unused | `uni/tn-common/brc-VRF1-SHARED-CT` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-power_up` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-sql` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | Contract unused | `uni/tn-common/brc-web` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| common | External EPG without contracts | `uni/tn-common/out-default/instP-EXT-EPG-LEGACY` | External EPG has no contracts, so no traffic is permitted between the outside and internal EPGs. | Provide/consume the contracts for the external flows. |
| common | Permit-any filter | `uni/tn-common/brc-CT-PAN-NS` | Contract permits ALL traffic via tn-common/flt-FLT-PBR-IPV4 entry IPV4 (etherType/protocol unspecified). | Replace with specific filters (protocol + destination port), e.g. tcp/443; keep 'common/default' for lab use only. |
| global-NBK-Tenant | EPG isolated (no contracts) | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1216_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| global-NBK-Tenant | EPG isolated (no contracts) | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1217_EPG` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iTenant | Contract unused | `uni/tn-iTenant/brc-contract_webserver-to-database` | Contract is neither provided nor consumed. | Delete it or attach it to the intended provider and consumer EPGs. |
| iTenant | EPG isolated (no contracts) | `uni/tn-iTenant/ap-AP_iTenant-2/epg-application` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iTenant | EPG isolated (no contracts) | `uni/tn-iTenant/ap-AP_iTenant/epg-database_iTenant` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iTenant | EPG isolated (no contracts) | `uni/tn-iTenant/ap-AP_iTenant/epg-webserver_iTenant` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-contractors | EPG isolated (no contracts) | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| iacdemo-prod | EPG isolated (no contracts) | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| juan | Tenant empty | `uni/tn-juan` | Tenant has no VRF, BD, application profile, contract or L3Out. | Delete the tenant if it is no longer needed, or bring it under NaC with its intended objects. |
| mgmt | BD unused | `uni/tn-mgmt/BD-MOJ_BD_INBM` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| mgmt | Config fault F0523 | `uni/tn-mgmt/mgmtp-default/inb-default` | Configuration failed for EPG default due to Not Associated With Management Zone | Fix the EPG's dependency named in the fault (BD/VRF, management zone, etc.). |
| mgmt | Config fault F1298 | `uni/tn-mgmt/out-inb_L3Out/instP-inbExt_EPG` | For tenant mgmt, outside inb_L3Out, deployment of external EPG inbExt_EPG failed on node 102. Reason Node Cannot Deploy EPG | Check that the target nodes can deploy the EPG (node role/pod, interface and VLAN config). |
| oneaciapp | Config fault F3891 | `uni/tn-oneaciapp/ctx-dev/leakroutes/leakintsubnet-[192.168.40.0/24]` | Configuration failed for Inter-VRF Leaked Subnet (EPG/BD in case of APIC, cloudSubnet/CloudCidr in case of CAPIC) 192.168.40.0/24 under VRF dev Tenant oneaciapp, due to Subnet does not match any EPG/BD Subnets in the VRF. An Inter-VRF Leaked Subnet must be equal to an EPG/BD Subnet or be a subset of | The leaked subnet must match an existing BD/EPG subnet in the VRF; correct the prefix or remove the leak. |
| oneaciapp | Config fault F3891 | `uni/tn-oneaciapp/ctx-prod/leakroutes/leakintsubnet-[192.168.8.0/24]` | Configuration failed for Inter-VRF Leaked Subnet (EPG/BD in case of APIC, cloudSubnet/CloudCidr in case of CAPIC) 192.168.8.0/24 under VRF prod Tenant oneaciapp, due to Subnet does not match any EPG/BD Subnets in the VRF. An Inter-VRF Leaked Subnet must be equal to an EPG/BD Subnet or be a subset of | The leaked subnet must match an existing BD/EPG subnet in the VRF; correct the prefix or remove the leak. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-DEV/epg-D-APP` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| oneaciapp | EPG isolated (no contracts) | `uni/tn-oneaciapp/ap-DEV/epg-D-DB` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |
| task_ansible_aci_6th | BD unused | `uni/tn-task_ansible_aci_6th/BD-BD_PROD` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| task_ansible_aci_6th | BD unused | `uni/tn-task_ansible_aci_6th/BD-BD_TEST` | No EPG is attached to this bridge domain. | Remove the BD or attach the intended EPGs. |
| test | EPG isolated (no contracts) | `uni/tn-test/ap-test/epg-test` | EPG neither provides nor consumes any contract, so in an enforced VRF it can only talk inside itself. | Add provider/consumer contracts for the flows it needs, or remove the EPG if unused. |

## Recommendations to look good

1. **Fix the broken relations first** - found: 12 broken relation(s) in 8 tenant(s): Critical fault F0467 (EPG deployment on path failed) (5); Contract without subjects (2); EPG contract missing-target (2); Subject without filters (1); External EPG contract missing-target (1); BD VRF missing-target (1)  
   Do: Create the missing targets (VRF, domain, L3Out, device context) or remove the stale relations; missing-target objects never deploy and APIC may silently fall back to tn-common defaults.
2. **Contract design: no permit-any, keep vzAny/preferred groups deliberate** - found: Permit-any filter: 2 (e.g. tn-common/brc-CT-PAN-NS, tn-common/brc-default)  
   Do: Use specific filters (protocol + destination port, stateful where possible) instead of common/default or 'ip any'; reserve vzAny for shared services (DNS/NTP/ICMP) with narrow filters; keep every VRF enforced; avoid preferred groups except for migrations.
3. **Every contract needs both a provider and a consumer; remove dead/duplicate contracts** - found: Contract consumed, never provided: 1 (e.g. tn-common/brc-CT-PAN-NS); Contract unused: 6 (e.g. tn-common/brc-VRF1-SHARED-CT, tn-common/brc-power_up); EPG isolated (no contracts): 28 (e.g. tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG, tn-Demo1/ap-app-demo1/epg-epg-vlan300-web-demo1); External EPG without contracts: 1 (e.g. tn-common/out-default/instP-EXT-EPG-LEGACY)  
   Do: Model each flow as provider (server side) + consumer (client side) in NaC; delete unused and duplicate contracts (e.g. *-OLD) so the policy matches the intent.
4. **Match contract scope to real usage** - found: scope mismatch: 0, wider than needed: 1  
   Do: Use 'context' by default, 'tenant'/'global' only for inter-VRF/tenant flows (with shared subnets).
5. **Make BD settings match their role (L2 vs L3)** - found: L3 BD without subnet: 4 (e.g. tn-Demo1/BD-bd-dab-demo1, tn-My-Tenant/BD-My-app); L2 BD settings: 1 (e.g. tn-TF_LAB_SAMAN/BD-BD_10); L3 BD flooding: 21 (e.g. tn-ASN_550/BD-BD01, tn-Demo1/BD-bd-web-demo1)  
   Do: L3 BD: unicast routing + gateway subnet, hardware proxy, ARP flooding off, limit IP learning to subnet. L2 BD: unicast routing off, ARP flooding on, unknown unicast flood, no subnets.
6. **Clean up unused objects** - found: Tenant empty: 1; VRF unused: 5; BD unused: 7; AP without EPGs: 2; Filter unused: 3; L3Out without external EPG: 1  
   Do: Delete leftovers or bring them under NaC; unused objects hide real intent and drift.
7. **Add descriptions** - found: 91 of 138 VRF/BD/AP/EPG/contract/filter/L3Out objects have no description.  
   Do: Set descr on every object (NaC: description:) - owner, purpose, ticket/change ID.
8. **Tag ownership (annotations) for NaC** - found: 108 of 138 objects have no annotation; in use: 'orchestrator:terraform' x25, 'orchestrator:ansible' x5.  
   Do: Push everything through NaC/Terraform so objects carry 'orchestrator:terraform' (or a tag such as nac:owner=<team>); objects without it are hand-made and drift-prone.
9. **Adopt one naming convention** - found: name styles in use: Mixed 50, UPPER_SNAKE 57, lower 31; 3 generic/VLAN/IP-style names (e.g. tn-test/ap-test, tn-test/ap-test/epg-test, tn-test/ctx-test).  
   Do: e.g. <app>_VRF, <app>_<tier>_BD, <app>_AP, <tier>_EPG, <consumer>-to-<provider>_CON, <proto>-<port>_FLT; enforce it in the NaC schema/linting.
10. **Bind EPGs to a domain** - found: no domain: 25, missing domain: 0  
   Do: Every EPG that should carry endpoints needs a physical/VMM domain whose VLAN pool covers the encap.

## Informational (91)

| Tenant | Check | Object DN | Note |
|---|---|---|---|
| ASN_550 | L3 BD flooding | `uni/tn-ASN_550/BD-BD01` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| Demo1 | EPG without static path | `uni/tn-Demo1/ap-app-demo1/epg-epg-vlan300-web-demo1` | No static path bindings (fvRsPathAtt). |
| Demo1 | L3 BD flooding | `uni/tn-Demo1/BD-bd-web-demo1` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| MOJ_TENANAT | EPG without static path | `uni/tn-MOJ_TENANAT/ap-MOJ_APP_IS/epg-MOJ_EPG_IS` | No static path bindings (fvRsPathAtt). |
| MOJ_TENANAT | L3 BD flooding | `uni/tn-MOJ_TENANAT/BD-MOJ_BD_IS` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| My-Tenant | EPG without domain | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-APP-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| My-Tenant | EPG without domain | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| My-Tenant | EPG without domain | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-WEB-EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| My-Tenant | EPG without static path | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-APP-EPG` | No static path bindings (fvRsPathAtt). |
| My-Tenant | EPG without static path | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-WEB-EPG` | No static path bindings (fvRsPathAtt). |
| My-Tenant | L3 BD flooding | `uni/tn-My-Tenant/BD-My-db` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| My-Tenant | L3 BD flooding | `uni/tn-My-Tenant/BD-My-web` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| SCADAAA | EPG without static path | `uni/tn-SCADAAA/ap-SCADA_AP/epg-SCADA_EPG` | No static path bindings (fvRsPathAtt). |
| SCADAAA | L3 BD flooding | `uni/tn-SCADAAA/BD-SCADA_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| T1_VMM | EPG without domain | `uni/tn-T1_VMM/ap-APP_PROFILE/epg-EPG1_USERS` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| T1_VMM | EPG without static path | `uni/tn-T1_VMM/ap-APP_PROFILE/epg-EPG1_USERS` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-01 | EPG without domain | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG01` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-01 | EPG without domain | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG02` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-01 | EPG without domain | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG03` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-01 | EPG without domain | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG04` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-01 | EPG without static path | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG01` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-01 | EPG without static path | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG02` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-01 | EPG without static path | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG03` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-01 | EPG without static path | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG04` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-02 | EPG without domain | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG05` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-02 | EPG without domain | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG06` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TECCRT-3778-02 | EPG without static path | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG05` | No static path bindings (fvRsPathAtt). |
| TECCRT-3778-02 | EPG without static path | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG06` | No static path bindings (fvRsPathAtt). |
| TeamTest-Bakker | EPG without domain | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-app` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TeamTest-Bakker | EPG without domain | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| TeamTest-Bakker | EPG without static path | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-app` | No static path bindings (fvRsPathAtt). |
| TeamTest-Bakker | EPG without static path | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-web` | No static path bindings (fvRsPathAtt). |
| common | AP without EPGs | `uni/tn-common/ap-default` | Application profile contains no EPG. (APIC system default object - informational) |
| common | BD VRF fallback to common | `uni/tn-common/BD-default` | BD has no VRF name (tnFvCtxName empty) and silently falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | Contract unused | `uni/tn-common/brc-default` | Contract is neither provided nor consumed. (APIC system default object - informational) |
| common | Filter unused | `uni/tn-common/flt-arp` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-est` | Filter is not referenced by any contract subject. |
| common | Filter unused | `uni/tn-common/flt-icmp` | Filter is not referenced by any contract subject. |
| common | L3 BD flooding | `uni/tn-common/BD-BD-PAN-NS` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| common | L3 BD without subnet | `uni/tn-common/BD-default` | Unicast routing is enabled but the BD has no subnet (no gateway; IP learning without a subnet). (APIC system default object - informational) |
| common | L3Out VRF fallback to common | `uni/tn-common/out-default` | L3Out has no VRF name and falls back to tn-common/ctx-default. (APIC system default object - informational) |
| common | Permit-any filter | `uni/tn-common/brc-default` | Contract permits ALL traffic via tn-common/flt-default entry default (etherType/protocol unspecified). (APIC system default object - informational) |
| common | VRF unused | `uni/tn-common/ctx-copy` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| dev-demo | EPG uses common contract | `uni/tn-dev-demo/ap-AP-PBR/epg-EPG-INTERNAL-POC` | EPG consumes 'CT-PAN-NS' resolved to tn-common/brc-CT-PAN-NS. |
| dev-demo | EPG without static path | `uni/tn-dev-demo/ap-AP-PBR/epg-EPG-INTERNAL-POC` | No static path bindings (fvRsPathAtt). |
| dev-demo | L3 BD flooding | `uni/tn-dev-demo/BD-BD-INTERNAL` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| global-NBK-Tenant | EPG without domain | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1216_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| global-NBK-Tenant | EPG without domain | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1217_EPG` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| global-NBK-Tenant | EPG without static path | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1216_EPG` | No static path bindings (fvRsPathAtt). |
| global-NBK-Tenant | EPG without static path | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1217_EPG` | No static path bindings (fvRsPathAtt). |
| global-NBK-Tenant | L3 BD flooding | `uni/tn-global-NBK-Tenant/BD-Vlan1216_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| global-NBK-Tenant | L3 BD flooding | `uni/tn-global-NBK-Tenant/BD-Vlan1217_BD` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| iTenant | EPG without domain | `uni/tn-iTenant/ap-AP_iTenant-2/epg-application` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iTenant | EPG without domain | `uni/tn-iTenant/ap-AP_iTenant/epg-database_iTenant` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iTenant | EPG without domain | `uni/tn-iTenant/ap-AP_iTenant/epg-webserver_iTenant` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iTenant | EPG without static path | `uni/tn-iTenant/ap-AP_iTenant-2/epg-application` | No static path bindings (fvRsPathAtt). |
| iTenant | EPG without static path | `uni/tn-iTenant/ap-AP_iTenant/epg-database_iTenant` | No static path bindings (fvRsPathAtt). |
| iTenant | EPG without static path | `uni/tn-iTenant/ap-AP_iTenant/epg-webserver_iTenant` | No static path bindings (fvRsPathAtt). |
| iTenant | L3 BD flooding | `uni/tn-iTenant/BD-BD_iTenant` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without domain | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | EPG without static path | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` | No static path bindings (fvRsPathAtt). |
| iacdemo-contractors | L3 BD flooding | `uni/tn-iacdemo-contractors/BD-Contractors-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without domain | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | EPG without static path | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` | No static path bindings (fvRsPathAtt). |
| iacdemo-prod | L3 BD flooding | `uni/tn-iacdemo-prod/BD-Booking-BD` | Routed BD with arpFlood=yes, unkMacUcastAct=flood (legacy/migration style). |
| mgmt | Contract scope wider than used | `uni/tn-mgmt/brc-ctr_inb_mgmt` | Scope 'global' but all users are in one VRF (tn-mgmt/ctx-inb). |
| mgmt | EPG without static path | `uni/tn-mgmt/ap-MOJ_APP_VH_MGMT/epg-MOJ_EPG_VH_MGMT` | No static path bindings (fvRsPathAtt). |
| mgmt | L3 BD flooding | `uni/tn-mgmt/BD-MOJ_BD_INBM` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| mgmt | L3 BD flooding | `uni/tn-mgmt/BD-MOJ_BD_VH_MGMT` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| mgmt | L3 BD flooding | `uni/tn-mgmt/BD-default` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| mgmt | VRF unused | `uni/tn-mgmt/ctx-oob` | No bridge domain or L3Out is attached to this VRF. (APIC system default object - informational) |
| oneaciapp | EPG without domain | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` | No domain (fvRsDomAtt): the EPG cannot be deployed on any leaf port or VMM. |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-DEV/epg-D-APP` | No static path bindings (fvRsPathAtt). |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-DEV/epg-D-DB` | No static path bindings (fvRsPathAtt). |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-PROD/epg-P-APP` | No static path bindings (fvRsPathAtt). |
| oneaciapp | EPG without static path | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` | No static path bindings (fvRsPathAtt). |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-D-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-D-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-P-APP` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| oneaciapp | L3 BD flooding | `uni/tn-oneaciapp/BD-P-DB` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |
| test | L3 BD flooding | `uni/tn-test/BD-tes` | Routed BD with arpFlood=yes, unkMacUcastAct=proxy (legacy/migration style). |

## nac-test integrity failures

| Suite | Test | Reason |
|---|---|---|
| ASN 550 | Integrity ASN_550: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message:', 'F0467 critical: Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-pa'] |
| Mgmt | Integrity mgmt: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface doe'] |
| Mgmt | Integrity contract mgmt/MOJ_CT_AP_vC: subjects and filters | Subjects without filters: ['uni/tn-mgmt/brc-MOJ_CT_AP_vC/subj-MOJ_SUBJ_AP_vC'] |
| My-Tenant | Integrity My-Tenant: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-1'] |
| Oneaciapp | Integrity oneaciapp: all named relations resolve | Unresolved relations: ['uni/tn-oneaciapp/ap-PROD/epg-P-DB/rsprov-APP-To-DB (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-oneaciapp/out-L3out/instP-externalepg-3/rsprov-APP-To-DB (state=missing-target, stateQual=none, tDn=-)', 'uni/tn-oneaciapp/ap-PROD/epg-P-APP/rscons-APP-To-DB (state=missing-target, stateQual=none, tDn=-)'] |
| Oneaciapp | Integrity EPG oneaciapp/PROD/P-APP: contract relations resolve | uni/tn-oneaciapp/ap-PROD/epg-P-APP/rscons-APP-To-DB is 'missing-target' (target vzBrCP not found): missing-target != formed |
| Oneaciapp | Integrity EPG oneaciapp/PROD/P-DB: contract relations resolve | uni/tn-oneaciapp/ap-PROD/epg-P-DB/rsprov-APP-To-DB is 'missing-target' (target vzBrCP not found): missing-target != formed |
| Oneaciapp | Integrity contract oneaciapp/ESG: subjects and filters | Contract uni/tn-oneaciapp/brc-ESG has no subjects (permits nothing) |
| Task Ansible Aci 6Th | Integrity task_ansible_aci_6th: all named relations resolve | Unresolved relations: ['uni/tn-task_ansible_aci_6th/BD-BD_TEST/rsctx (state=missing-target, stateQual=none, tDn=-)'] |
| Task Ansible Aci 6Th | Integrity BD task_ansible_aci_6th/BD_TEST: VRF resolves | uni/tn-task_ansible_aci_6th/BD-BD_TEST/rsctx is 'missing-target' (target fvCtx not found): missing-target != formed |
| Test | Integrity test: no critical or major faults | Critical/major faults: ['F0467 critical: Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-'] |
| iTenant | Integrity contract iTenant/contract_webserver-to-database: subjects and filters | Contract uni/tn-iTenant/brc-contract_webserver-to-database has no subjects (permits nothing) |

## Tenant faults (faultInst)

By severity: warning 6, minor 14, critical 6; TCA/threshold faults (context only): 1

| Tenant | Sev | Code | Affected | Description |
|---|---|---|---|---|
| TEST_TENANT | critical | F0467 | `uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1` | Configuration failed for uni/tn-TEST_TENANT/ap-App_P-1/epg-EPG_LAB-1 due to VRF Not Present, debug message:  |
| test | critical | F0467 | `uni/tn-test/ap-test/epg-test` | Configuration failed for uni/tn-test/ap-test/epg-test node 101 eth1/5 due to Encap Already Used in Another EPG,Invalid Path Configuration, debug message: encap-already-in-use: Encap (vlan-10) is alrea |
| My-Tenant | critical | F0467 | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` | Configuration failed for uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG node 101 eth1/1 due to Invalid Path Configuration, debug message: invalid-path: vlan-10 :There is no domain, associated with b |
| ASN_550 | critical | F0467 | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 eth1/1 due to Invalid Path Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-211 :Either the EpG  |
| ASN_550 | critical | F0467 | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` | Configuration failed for uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |
| mgmt | critical | F0467 | `uni/tn-mgmt/out-inb_L3Out` | Configuration failed for uni/tn-mgmt/out-inb_L3Out node 101 vpcInband_L3out_PolGrp due to Invalid Path Configuration, debug message: invalid-path: Interface does not exist; |

Read-only check (aaaLogin + GET). Score = 100 - 10 x broken - 3 x warnings (min 0).
