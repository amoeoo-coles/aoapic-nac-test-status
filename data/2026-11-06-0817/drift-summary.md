# ACI drift report: 2026-11-06

## DRIFT DETECTED - tests 20/129 passed, 109 failed; 167 added, 109 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-11-06 08:18:03 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

## nac-test

- Tests: **129** total, **20** passed, **109** failed, 0 skipped (nac-test exit code 109)

| Suite | Test | Kind | Reason |
|---|---|---|---|
| Heroes | Verify Tenant Heroes | missing | Object uni/tn-Heroes not found on APIC |
| Heroes | Verify VRF Heroes/Heroes_Only | missing | Object uni/tn-Heroes/ctx-Heroes_Only not found on APIC |
| Heroes | Verify BD Heroes/Hero_Land | missing | Object uni/tn-Heroes/BD-Hero_Land not found on APIC |
| Heroes | Verify Subnet Heroes/Hero_Land/10.1.120.1/22 | missing | Object uni/tn-Heroes/BD-Hero_Land/subnet-[10.1.120.1/22] not found on APIC |
| Heroes | Verify Subnet Heroes/Hero_Land/192.168.120.1/22 | missing | Object uni/tn-Heroes/BD-Hero_Land/subnet-[192.168.120.1/22] not found on APIC |
| Heroes | Verify AP Heroes/Save_The_Planet | missing | Object uni/tn-Heroes/ap-Save_The_Planet not found on APIC |
| Heroes | Verify EPG Heroes/Save_The_Planet/web | missing | Object uni/tn-Heroes/ap-Save_The_Planet/epg-web not found on APIC |
| Heroes | Verify EPG Heroes/Save_The_Planet/app | missing | Object uni/tn-Heroes/ap-Save_The_Planet/epg-app not found on APIC |
| Heroes | Verify EPG Heroes/Save_The_Planet/db | missing | Object uni/tn-Heroes/ap-Save_The_Planet/epg-db not found on APIC |
| MUHC | Verify Tenant MUHC | missing | Object uni/tn-MUHC not found on APIC |
| MUHC | Verify BD MUHC/VLAN_2780_BD | missing | Object uni/tn-MUHC/BD-VLAN_2780_BD not found on APIC |
| MUHC | Verify BD MUHC/VLAN_2701_BD | missing | Object uni/tn-MUHC/BD-VLAN_2701_BD not found on APIC |
| MUHC | Verify Subnet MUHC/VLAN_2701_BD/172.26.200.1/24 | missing | Object uni/tn-MUHC/BD-VLAN_2701_BD/subnet-[172.26.200.1/24] not found on APIC |
| MUHC | Verify AP MUHC/LEGACY_APR | missing | Object uni/tn-MUHC/ap-LEGACY_APR not found on APIC |
| MUHC | Verify EPG MUHC/LEGACY_APR/VLAN_2780_EPG | missing | Object uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG not found on APIC |
| MUHC | Verify EPG MUHC/LEGACY_APR/VLAN_2701_EPG | missing | Object uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG not found on APIC |
| OS1 | Verify Tenant OS1 | missing | Object uni/tn-OS1 not found on APIC |
| OS1 | Verify VRF OS1/OS1 | missing | Object uni/tn-OS1/ctx-OS1 not found on APIC |
| OS1 | Verify BD OS1/VLAN1 | missing | Object uni/tn-OS1/BD-VLAN1 not found on APIC |
| OS1 | Verify BD OS1/vlan | missing | Object uni/tn-OS1/BD-vlan not found on APIC |
| OS1 | Verify Subnet OS1/vlan/10.10.10.1/24 | missing | Object uni/tn-OS1/BD-vlan/subnet-[10.10.10.1/24] not found on APIC |
| OS1 | Verify AP OS1/APP-Prod | missing | Object uni/tn-OS1/ap-APP-Prod not found on APIC |
| OS1 | Verify EPG OS1/APP-Prod/APP-WEB | missing | Object uni/tn-OS1/ap-APP-Prod/epg-APP-WEB not found on APIC |
| Prod | Verify Tenant prod | missing | Object uni/tn-prod not found on APIC |
| Prod | Verify VRF prod/prod.prod-vrf | missing | Object uni/tn-prod/ctx-prod.prod-vrf not found on APIC |
| Prod | Verify BD prod/10.1.103.0_24 | missing | Object uni/tn-prod/BD-10.1.103.0_24 not found on APIC |
| Prod | Verify Subnet prod/10.1.103.0_24/10.1.103.1/24 | missing | Object uni/tn-prod/BD-10.1.103.0_24/subnet-[10.1.103.1/24] not found on APIC |
| Prod | Verify BD prod/10.1.102.0_24 | missing | Object uni/tn-prod/BD-10.1.102.0_24 not found on APIC |
| Prod | Verify Subnet prod/10.1.102.0_24/10.1.102.1/24 | missing | Object uni/tn-prod/BD-10.1.102.0_24/subnet-[10.1.102.1/24] not found on APIC |
| Prod | Verify BD prod/10.1.101.0_24 | missing | Object uni/tn-prod/BD-10.1.101.0_24 not found on APIC |
| Prod | Verify Subnet prod/10.1.101.0_24/10.1.101.1/24 | missing | Object uni/tn-prod/BD-10.1.101.0_24/subnet-[10.1.101.1/24] not found on APIC |
| Prod | Verify BD prod/10.1.100.0_24 | missing | Object uni/tn-prod/BD-10.1.100.0_24 not found on APIC |
| Prod | Verify Subnet prod/10.1.100.0_24/10.1.100.1/24 | missing | Object uni/tn-prod/BD-10.1.100.0_24/subnet-[10.1.100.1/24] not found on APIC |
| Prod | Verify AP prod/vlans | missing | Object uni/tn-prod/ap-vlans not found on APIC |
| Prod | Verify EPG prod/vlans/vlan102 | missing | Object uni/tn-prod/ap-vlans/epg-vlan102 not found on APIC |
| Prod | Verify EPG prod/vlans/vlan100 | missing | Object uni/tn-prod/ap-vlans/epg-vlan100 not found on APIC |
| Prod | Verify EPG prod/vlans/vlan101 | missing | Object uni/tn-prod/ap-vlans/epg-vlan101 not found on APIC |
| ROR | Verify Tenant ROR | missing | Object uni/tn-ROR not found on APIC |
| ROR | Verify VRF ROR/ROR_VRF | missing | Object uni/tn-ROR/ctx-ROR_VRF not found on APIC |
| ROR | Verify BD ROR/ROR_WEB_BD | missing | Object uni/tn-ROR/BD-ROR_WEB_BD not found on APIC |
| ROR | Verify Subnet ROR/ROR_WEB_BD/203.0.113.1/24 | missing | Object uni/tn-ROR/BD-ROR_WEB_BD/subnet-[203.0.113.1/24] not found on APIC |
| ROR | Verify Subnet ROR/ROR_WEB_BD/3fff:cb:0:71::1/64 | missing | Object uni/tn-ROR/BD-ROR_WEB_BD/subnet-[3fff:cb:0:71::1/64] not found on APIC |
| ROR | Verify BD ROR/ROR_DB_BD | missing | Object uni/tn-ROR/BD-ROR_DB_BD not found on APIC |
| ROR | Verify Subnet ROR/ROR_DB_BD/10.33.6.1/24 | missing | Object uni/tn-ROR/BD-ROR_DB_BD/subnet-[10.33.6.1/24] not found on APIC |
| ROR | Verify Subnet ROR/ROR_DB_BD/fd00:a:17:6::1/64 | missing | Object uni/tn-ROR/BD-ROR_DB_BD/subnet-[fd00:a:17:6::1/64] not found on APIC |
| ROR | Verify AP ROR/ROR_WEB_AP | missing | Object uni/tn-ROR/ap-ROR_WEB_AP not found on APIC |
| ROR | Verify EPG ROR/ROR_WEB_AP/ROR_WEB_EPG | missing | Object uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG not found on APIC |
| ROR | Verify EPG ROR/ROR_WEB_AP/ROR_DB_EPG | missing | Object uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG not found on APIC |
| SnV | Verify Tenant SnV | missing | Object uni/tn-SnV not found on APIC |
| SnV | Verify VRF SnV/Superverse | missing | Object uni/tn-SnV/ctx-Superverse not found on APIC |
| SnV | Verify BD SnV/antigravity | missing | Object uni/tn-SnV/BD-antigravity not found on APIC |
| SnV | Verify Subnet SnV/antigravity/10.2.10.1/23 | missing | Object uni/tn-SnV/BD-antigravity/subnet-[10.2.10.1/23] not found on APIC |
| SnV | Verify AP SnV/Rescue | missing | Object uni/tn-SnV/ap-Rescue not found on APIC |
| SnV | Verify EPG SnV/Rescue/Web | missing | Object uni/tn-SnV/ap-Rescue/epg-Web not found on APIC |
| SnV | Verify EPG SnV/Rescue/Database | missing | Object uni/tn-SnV/ap-Rescue/epg-Database not found on APIC |
| SnV | Verify AP SnV/Evolution_X | missing | Object uni/tn-SnV/ap-Evolution_X not found on APIC |
| SnV | Verify EPG SnV/Evolution_X/Database | missing | Object uni/tn-SnV/ap-Evolution_X/epg-Database not found on APIC |
| SnV | Verify EPG SnV/Evolution_X/Web | missing | Object uni/tn-SnV/ap-Evolution_X/epg-Web not found on APIC |
| SnV | Verify AP SnV/Chaos | missing | Object uni/tn-SnV/ap-Chaos not found on APIC |
| SnV | Verify EPG SnV/Chaos/Web | missing | Object uni/tn-SnV/ap-Chaos/epg-Web not found on APIC |
| SnV | Verify EPG SnV/Chaos/Database | missing | Object uni/tn-SnV/ap-Chaos/epg-Database not found on APIC |
| SnV | Verify AP SnV/Power_Up | missing | Object uni/tn-SnV/ap-Power_Up not found on APIC |
| SnV | Verify EPG SnV/Power_Up/Web | missing | Object uni/tn-SnV/ap-Power_Up/epg-Web not found on APIC |
| SnV | Verify EPG SnV/Power_Up/Database | missing | Object uni/tn-SnV/ap-Power_Up/epg-Database not found on APIC |
| TEST | Verify Tenant TEST | missing | Object uni/tn-TEST not found on APIC |
| TEST | Verify VRF TEST/TEST | missing | Object uni/tn-TEST/ctx-TEST not found on APIC |
| TEST | Verify BD TEST/TESTBD | missing | Object uni/tn-TEST/BD-TESTBD not found on APIC |
| TEST | Verify Subnet TEST/TESTBD/1.1.1.1/24 | missing | Object uni/tn-TEST/BD-TESTBD/subnet-[1.1.1.1/24] not found on APIC |
| TEST | Verify AP TEST/TEST_AAEP | missing | Object uni/tn-TEST/ap-TEST_AAEP not found on APIC |
| TEST | Verify EPG TEST/TEST_AAEP/TESTEPG | missing | Object uni/tn-TEST/ap-TEST_AAEP/epg-TESTEPG not found on APIC |
| TEST-ABC1 | Verify Tenant TEST-ABC1 | missing | Object uni/tn-TEST-ABC1 not found on APIC |
| TEST-ABC1 | Verify VRF TEST-ABC1/VRF-INT-TESTABC1 | missing | Object uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1 not found on APIC |
| TEST-ABC1 | Verify BD TEST-ABC1/BD-INT-TESTABC1 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1 not found on APIC |
| TEST-ABC1 | Verify Subnet TEST-ABC1/BD-INT-TESTABC1/10.10.10.1/24 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.10.1/24] not found on APIC |
| TEST-ABC1 | Verify Subnet TEST-ABC1/BD-INT-TESTABC1/10.10.20.1/24 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.20.1/24] not found on APIC |
| TEST-ABC1 | Verify BD TEST-ABC1/BD-L2-TESTABC1 | missing | Object uni/tn-TEST-ABC1/BD-BD-L2-TESTABC1 not found on APIC |
| TN-DEDUP-LAB | Verify Tenant TN-DEDUP-LAB | missing | Object uni/tn-TN-DEDUP-LAB not found on APIC |
| TN-DEDUP-LAB | Verify VRF TN-DEDUP-LAB/VRF-LAB | missing | Object uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB not found on APIC |
| TN-DEDUP-LAB | Verify BD TN-DEDUP-LAB/BD-LAB | missing | Object uni/tn-TN-DEDUP-LAB/BD-BD-LAB not found on APIC |
| TN-DEDUP-LAB | Verify Subnet TN-DEDUP-LAB/BD-LAB/10.99.1.1/24 | missing | Object uni/tn-TN-DEDUP-LAB/BD-BD-LAB/subnet-[10.99.1.1/24] not found on APIC |
| TN-DEDUP-LAB | Verify AP TN-DEDUP-LAB/AP-LAB | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Mon | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mon not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Infra | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Infra not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Mail | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mail not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Dir | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Dir not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Web | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Web not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-App | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-App not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-DB | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-DB not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Mgmt | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mgmt not found on APIC |
| TN-DEDUP-LAB | Verify EPG TN-DEDUP-LAB/AP-LAB/EPG-Backup | missing | Object uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Backup not found on APIC |
| Test-Tenant | Verify Tenant Test-Tenant | missing | Object uni/tn-Test-Tenant not found on APIC |
| Test-Tenant | Verify VRF Test-Tenant/Test-VRF | missing | Object uni/tn-Test-Tenant/ctx-Test-VRF not found on APIC |
| Test-Tenant | Verify BD Test-Tenant/test-BD-01 | missing | Object uni/tn-Test-Tenant/BD-test-BD-01 not found on APIC |
| Test-Tenant | Verify Subnet Test-Tenant/test-BD-01/10.10.14.254/24 | missing | Object uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.14.254/24] not found on APIC |
| Test-Tenant | Verify Subnet Test-Tenant/test-BD-01/10.10.11.254/24 | missing | Object uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.11.254/24] not found on APIC |
| Test-Tenant | Verify Subnet Test-Tenant/test-BD-01/10.10.10.254/24 | missing | Object uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.10.254/24] not found on APIC |
| Test-Tenant | Verify Subnet Test-Tenant/test-BD-01/10.10.12.254/24 | missing | Object uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.12.254/24] not found on APIC |
| Test-Tenant | Verify AP Test-Tenant/Test-APP-Profile-01 | missing | Object uni/tn-Test-Tenant/ap-Test-APP-Profile-01 not found on APIC |
| Test-Tenant | Verify EPG Test-Tenant/Test-APP-Profile-01/test-epg-01 | missing | Object uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01 not found on APIC |
| UT | Verify Tenant UT | missing | Object uni/tn-UT not found on APIC |
| UT | Verify VRF UT/UVRF | missing | Object uni/tn-UT/ctx-UVRF not found on APIC |
| UT | Verify VRF UT/FWVRF | missing | Object uni/tn-UT/ctx-FWVRF not found on APIC |
| UT | Verify BD UT/UBD | missing | Object uni/tn-UT/BD-UBD not found on APIC |
| UT | Verify Subnet UT/UBD/192.168.10.254/24 | missing | Object uni/tn-UT/BD-UBD/subnet-[192.168.10.254/24] not found on APIC |
| UT | Verify BD UT/FBD | missing | Object uni/tn-UT/BD-FBD not found on APIC |
| UT | Verify AP UT/UAP | missing | Object uni/tn-UT/ap-UAP not found on APIC |
| UT | Verify EPG UT/UAP/USER_EPG | missing | Object uni/tn-UT/ap-UAP/epg-USER_EPG not found on APIC |
| tn-MGK | Verify Tenant tn-MGK | missing | Object uni/tn-tn-MGK not found on APIC |
| tn-MGK | Verify VRF tn-MGK/ctx-MGK | missing | Object uni/tn-tn-MGK/ctx-ctx-MGK not found on APIC |

## Object counts (REST pull vs baseline)

| Type | Baseline | Current (APIC, all tenants) | Added | Removed |
|---|---:|---:|---:|---:|
| Tenant | 16 | 27 | 23 | 12 |
| VRF | 18 | 28 | 22 | 12 |
| BD | 23 | 36 | 32 | 19 |
| Subnet (BD) | 23 | 34 | 33 | 22 |
| AP | 16 | 25 | 22 | 13 |
| EPG | 33 | 37 | 35 | 31 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (167)

| Type | Tenant | DN |
|---|---|---|
| Tenant | AAL001 | `uni/tn-AAL001` |
| Tenant | ASN_550 | `uni/tn-ASN_550` |
| Tenant | CiscoU-Tenant-03 | `uni/tn-CiscoU-Tenant-03` |
| Tenant | CiscoU-Tenant-04 | `uni/tn-CiscoU-Tenant-04` |
| Tenant | Demo1 | `uni/tn-Demo1` |
| Tenant | L3TenantL | `uni/tn-L3TenantL` |
| Tenant | MOJ_TENANAT | `uni/tn-MOJ_TENANAT` |
| Tenant | My-Tenant | `uni/tn-My-Tenant` |
| Tenant | NP-DEMO | `uni/tn-NP-DEMO` |
| Tenant | SCADAAA | `uni/tn-SCADAAA` |
| Tenant | T1_VMM | `uni/tn-T1_VMM` |
| Tenant | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01` |
| Tenant | TECCRT-3778-02 | `uni/tn-TECCRT-3778-02` |
| Tenant | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN` |
| Tenant | TeamTest-Bakker | `uni/tn-TeamTest-Bakker` |
| Tenant | dev-demo | `uni/tn-dev-demo` |
| Tenant | global-NBK-Tenant | `uni/tn-global-NBK-Tenant` |
| Tenant | iTenant | `uni/tn-iTenant` |
| Tenant | iacdemo-contractors | `uni/tn-iacdemo-contractors` |
| Tenant | iacdemo-prod | `uni/tn-iacdemo-prod` |
| Tenant | juan | `uni/tn-juan` |
| Tenant | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th` |
| Tenant | test | `uni/tn-test` |
| VRF | AAL001 | `uni/tn-AAL001/ctx-VRF1` |
| VRF | AAL001 | `uni/tn-AAL001/ctx-VRF2` |
| VRF | ASN_550 | `uni/tn-ASN_550/ctx-VRF_01` |
| VRF | CiscoU-Tenant-03 | `uni/tn-CiscoU-Tenant-03/ctx-CiscoU-Tenant-03-VRF` |
| VRF | CiscoU-Tenant-04 | `uni/tn-CiscoU-Tenant-04/ctx-CiscoU-Tenant-04-VRF` |
| VRF | Demo1 | `uni/tn-Demo1/ctx-vrf-demo1` |
| VRF | L3TenantL | `uni/tn-L3TenantL/ctx-L3-Vrf` |
| VRF | MOJ_TENANAT | `uni/tn-MOJ_TENANAT/ctx-MOJ_VRF` |
| VRF | My-Tenant | `uni/tn-My-Tenant/ctx-My-VRF` |
| VRF | NP-DEMO | `uni/tn-NP-DEMO/ctx-VRF-NP` |
| VRF | SCADAAA | `uni/tn-SCADAAA/ctx-SCADA_VRF` |
| VRF | T1_VMM | `uni/tn-T1_VMM/ctx-VRF_VMM` |
| VRF | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN/ctx-VRF_PROD` |
| VRF | dev-demo | `uni/tn-dev-demo/ctx-VRF-DEV-POC` |
| VRF | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/ctx-nbk` |
| VRF | iTenant | `uni/tn-iTenant/ctx-VRF_iTenant` |
| VRF | iacdemo-contractors | `uni/tn-iacdemo-contractors/ctx-VRF-Contractors` |
| VRF | iacdemo-prod | `uni/tn-iacdemo-prod/ctx-VRF-Prod` |
| VRF | oneaciapp | `uni/tn-oneaciapp/ctx-dev` |
| VRF | oneaciapp | `uni/tn-oneaciapp/ctx-prod` |
| VRF | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/ctx-VRF_RED` |
| VRF | test | `uni/tn-test/ctx-test` |
| BD | ASN_550 | `uni/tn-ASN_550/BD-BD01` |
| BD | CiscoU-Tenant-03 | `uni/tn-CiscoU-Tenant-03/BD-CiscoU-Tenant-03-BD` |
| BD | CiscoU-Tenant-04 | `uni/tn-CiscoU-Tenant-04/BD-CiscoU-Tenant-04-BD` |
| BD | Demo1 | `uni/tn-Demo1/BD-bd-dab-demo1` |
| BD | Demo1 | `uni/tn-Demo1/BD-bd-web-demo1` |
| BD | MOJ_TENANAT | `uni/tn-MOJ_TENANAT/BD-MOJ_BD_IS` |
| BD | My-Tenant | `uni/tn-My-Tenant/BD-My-app` |
| BD | My-Tenant | `uni/tn-My-Tenant/BD-My-db` |
| BD | My-Tenant | `uni/tn-My-Tenant/BD-My-web` |
| BD | SCADAAA | `uni/tn-SCADAAA/BD-SCADA_BD` |
| BD | T1_VMM | `uni/tn-T1_VMM/BD-BD_VMM` |
| BD | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN/BD-BD_10` |
| BD | common | `uni/tn-common/BD-BD-PAN-NS` |
| BD | dev-demo | `uni/tn-dev-demo/BD-BD-INTERNAL` |
| BD | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/BD-Vlan1216_BD` |
| BD | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/BD-Vlan1217_BD` |
| BD | iTenant | `uni/tn-iTenant/BD-BD_iTenant` |
| BD | iacdemo-contractors | `uni/tn-iacdemo-contractors/BD-Contractors-BD` |
| BD | iacdemo-prod | `uni/tn-iacdemo-prod/BD-App-BD` |
| BD | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Booking-BD` |
| BD | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Db-BD` |
| BD | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Web-BD` |
| BD | mgmt | `uni/tn-mgmt/BD-MOJ_BD_INBM` |
| BD | mgmt | `uni/tn-mgmt/BD-MOJ_BD_VH_MGMT` |
| BD | mgmt | `uni/tn-mgmt/BD-default` |
| BD | oneaciapp | `uni/tn-oneaciapp/BD-D-APP` |
| BD | oneaciapp | `uni/tn-oneaciapp/BD-D-DB` |
| BD | oneaciapp | `uni/tn-oneaciapp/BD-P-APP` |
| BD | oneaciapp | `uni/tn-oneaciapp/BD-P-DB` |
| BD | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/BD-BD_PROD` |
| BD | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/BD-BD_TEST` |
| BD | test | `uni/tn-test/BD-tes` |
| Subnet (BD) | ASN_550 | `uni/tn-ASN_550/BD-BD01/subnet-[110.1.1.1/24]` |
| Subnet (BD) | ASN_550 | `uni/tn-ASN_550/BD-BD01/subnet-[111.1.1.1/24]` |
| Subnet (BD) | ASN_550 | `uni/tn-ASN_550/BD-BD01/subnet-[112.2.2.1/24]` |
| Subnet (BD) | CiscoU-Tenant-03 | `uni/tn-CiscoU-Tenant-03/BD-CiscoU-Tenant-03-BD/subnet-[10.10.100.1/24]` |
| Subnet (BD) | CiscoU-Tenant-04 | `uni/tn-CiscoU-Tenant-04/BD-CiscoU-Tenant-04-BD/subnet-[10.100.100.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-web-demo1/subnet-[10.10.10.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-web-demo1/subnet-[20.20.20.1/24]` |
| Subnet (BD) | MOJ_TENANAT | `uni/tn-MOJ_TENANAT/BD-MOJ_BD_IS/subnet-[10.50.100.1/29]` |
| Subnet (BD) | My-Tenant | `uni/tn-My-Tenant/BD-My-db/subnet-[10.0.20.1/24]` |
| Subnet (BD) | My-Tenant | `uni/tn-My-Tenant/BD-My-web/subnet-[10.0.30.1/24]` |
| Subnet (BD) | SCADAAA | `uni/tn-SCADAAA/BD-SCADA_BD/subnet-[10.0.0.1/24]` |
| Subnet (BD) | common | `uni/tn-common/BD-BD-PAN-NS/subnet-[10.255.100.1/29]` |
| Subnet (BD) | dev-demo | `uni/tn-dev-demo/BD-BD-INTERNAL/subnet-[10.60.10.1/24]` |
| Subnet (BD) | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/BD-Vlan1216_BD/subnet-[10.160.216.1/24]` |
| Subnet (BD) | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/BD-Vlan1217_BD/subnet-[10.160.217.1/24]` |
| Subnet (BD) | iTenant | `uni/tn-iTenant/BD-BD_iTenant/subnet-[192.168.0.254/24]` |
| Subnet (BD) | iacdemo-contractors | `uni/tn-iacdemo-contractors/BD-Contractors-BD/subnet-[10.10.0.1/24]` |
| Subnet (BD) | iacdemo-prod | `uni/tn-iacdemo-prod/BD-App-BD/subnet-[10.20.20.1/24]` |
| Subnet (BD) | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Booking-BD/subnet-[10.20.0.1/24]` |
| Subnet (BD) | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Db-BD/subnet-[10.20.30.1/24]` |
| Subnet (BD) | iacdemo-prod | `uni/tn-iacdemo-prod/BD-Web-BD/subnet-[10.20.10.1/24]` |
| Subnet (BD) | mgmt | `uni/tn-mgmt/BD-MOJ_BD_INBM/subnet-[10.150.100.1/24]` |
| Subnet (BD) | mgmt | `uni/tn-mgmt/BD-MOJ_BD_VH_MGMT/subnet-[10.100.100.1/29]` |
| Subnet (BD) | mgmt | `uni/tn-mgmt/BD-default/subnet-[10.60.100.1/29]` |
| Subnet (BD) | mgmt | `uni/tn-mgmt/BD-inb/subnet-[192.168.1.1/24]` |
| Subnet (BD) | oneaciapp | `uni/tn-oneaciapp/BD-D-APP/subnet-[192.168.3.1/24]` |
| Subnet (BD) | oneaciapp | `uni/tn-oneaciapp/BD-D-DB/subnet-[192.168.4.1/24]` |
| Subnet (BD) | oneaciapp | `uni/tn-oneaciapp/BD-P-APP/subnet-[192.168.2.1/24]` |
| Subnet (BD) | oneaciapp | `uni/tn-oneaciapp/BD-P-DB/subnet-[192.168.1.1/24]` |
| Subnet (BD) | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/BD-BD_PROD/subnet-[192.168.1.1/24]` |
| Subnet (BD) | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/BD-BD_PROD/subnet-[192.168.2.1/24]` |
| Subnet (BD) | task_ansible_aci_6th | `uni/tn-task_ansible_aci_6th/BD-BD_TEST/subnet-[10.0.1.1/24]` |
| Subnet (BD) | test | `uni/tn-test/BD-tes/subnet-[10.10.10.1/24]` |
| AP | ASN_550 | `uni/tn-ASN_550/ap-ASN_APP_PROF` |
| AP | Demo1 | `uni/tn-Demo1/ap-app-demo1` |
| AP | MOJ_TENANAT | `uni/tn-MOJ_TENANAT/ap-MOJ_APP_IS` |
| AP | My-Tenant | `uni/tn-My-Tenant/ap-My-APP-Profile` |
| AP | NP-DEMO | `uni/tn-NP-DEMO/ap-APP-NP` |
| AP | SCADAAA | `uni/tn-SCADAAA/ap-SCADA_AP` |
| AP | T1_VMM | `uni/tn-T1_VMM/ap-APP_PROFILE` |
| AP | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App01` |
| AP | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App02` |
| AP | TECCRT-3778-02 | `uni/tn-TECCRT-3778-02/ap-App03` |
| AP | TeamTest-Bakker | `uni/tn-TeamTest-Bakker/ap-tt-shop` |
| AP | dev-demo | `uni/tn-dev-demo/ap-AP-PBR` |
| AP | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS` |
| AP | iTenant | `uni/tn-iTenant/ap-AP_iTenant` |
| AP | iTenant | `uni/tn-iTenant/ap-AP_iTenant-2` |
| AP | iacdemo-contractors | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP` |
| AP | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Booking-AP` |
| AP | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Shop-AP` |
| AP | mgmt | `uni/tn-mgmt/ap-MOJ_APP_VH_MGMT` |
| AP | oneaciapp | `uni/tn-oneaciapp/ap-DEV` |
| AP | oneaciapp | `uni/tn-oneaciapp/ap-PROD` |
| AP | test | `uni/tn-test/ap-test` |
| EPG | ASN_550 | `uni/tn-ASN_550/ap-ASN_APP_PROF/epg-ASN_EPG` |
| EPG | Demo1 | `uni/tn-Demo1/ap-app-demo1/epg-epg-vlan300-web-demo1` |
| EPG | MOJ_TENANAT | `uni/tn-MOJ_TENANAT/ap-MOJ_APP_IS/epg-MOJ_EPG_IS` |
| EPG | My-Tenant | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-APP-EPG` |
| EPG | My-Tenant | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-DB-EPG` |
| EPG | My-Tenant | `uni/tn-My-Tenant/ap-My-APP-Profile/epg-My-WEB-EPG` |
| EPG | SCADAAA | `uni/tn-SCADAAA/ap-SCADA_AP/epg-SCADA_EPG` |
| EPG | T1_VMM | `uni/tn-T1_VMM/ap-APP_PROFILE/epg-EPG1_USERS` |
| EPG | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG01` |
| EPG | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App01/epg-EPG02` |
| EPG | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG03` |
| EPG | TECCRT-3778-01 | `uni/tn-TECCRT-3778-01/ap-App02/epg-EPG04` |
| EPG | TECCRT-3778-02 | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG05` |
| EPG | TECCRT-3778-02 | `uni/tn-TECCRT-3778-02/ap-App03/epg-EPG06` |
| EPG | TeamTest-Bakker | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-app` |
| EPG | TeamTest-Bakker | `uni/tn-TeamTest-Bakker/ap-tt-shop/epg-web` |
| EPG | dev-demo | `uni/tn-dev-demo/ap-AP-PBR/epg-EPG-INTERNAL-POC` |
| EPG | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1216_EPG` |
| EPG | global-NBK-Tenant | `uni/tn-global-NBK-Tenant/ap-STRETCHED_ROUTED_VLANS/epg-Vlan1217_EPG` |
| EPG | iTenant | `uni/tn-iTenant/ap-AP_iTenant-2/epg-application` |
| EPG | iTenant | `uni/tn-iTenant/ap-AP_iTenant/epg-database_iTenant` |
| EPG | iTenant | `uni/tn-iTenant/ap-AP_iTenant/epg-webserver_iTenant` |
| EPG | iacdemo-contractors | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Jump-Hosts` |
| EPG | iacdemo-contractors | `uni/tn-iacdemo-contractors/ap-Remote-Access-AP/epg-Vendors` |
| EPG | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Db` |
| EPG | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Booking-AP/epg-Web` |
| EPG | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-App` |
| EPG | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Db` |
| EPG | iacdemo-prod | `uni/tn-iacdemo-prod/ap-Shop-AP/epg-Web` |
| EPG | mgmt | `uni/tn-mgmt/ap-MOJ_APP_VH_MGMT/epg-MOJ_EPG_VH_MGMT` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-DEV/epg-D-APP` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-DEV/epg-D-DB` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-PROD/epg-P-APP` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-PROD/epg-P-DB` |
| EPG | test | `uni/tn-test/ap-test/epg-test` |

## Removed since baseline (109)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Heroes | `uni/tn-Heroes` |
| Tenant | MUHC | `uni/tn-MUHC` |
| Tenant | OS1 | `uni/tn-OS1` |
| Tenant | ROR | `uni/tn-ROR` |
| Tenant | SnV | `uni/tn-SnV` |
| Tenant | TEST | `uni/tn-TEST` |
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
| Tenant | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB` |
| Tenant | Test-Tenant | `uni/tn-Test-Tenant` |
| Tenant | UT | `uni/tn-UT` |
| Tenant | prod | `uni/tn-prod` |
| Tenant | tn-MGK | `uni/tn-tn-MGK` |
| VRF | Heroes | `uni/tn-Heroes/ctx-Heroes_Only` |
| VRF | OS1 | `uni/tn-OS1/ctx-OS1` |
| VRF | ROR | `uni/tn-ROR/ctx-ROR_VRF` |
| VRF | SnV | `uni/tn-SnV/ctx-Superverse` |
| VRF | TEST-ABC1 | `uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1` |
| VRF | TEST | `uni/tn-TEST/ctx-TEST` |
| VRF | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` |
| VRF | Test-Tenant | `uni/tn-Test-Tenant/ctx-Test-VRF` |
| VRF | UT | `uni/tn-UT/ctx-FWVRF` |
| VRF | UT | `uni/tn-UT/ctx-UVRF` |
| VRF | prod | `uni/tn-prod/ctx-prod.prod-vrf` |
| VRF | tn-MGK | `uni/tn-tn-MGK/ctx-ctx-MGK` |
| BD | Heroes | `uni/tn-Heroes/BD-Hero_Land` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2780_BD` |
| BD | OS1 | `uni/tn-OS1/BD-VLAN1` |
| BD | OS1 | `uni/tn-OS1/BD-vlan` |
| BD | ROR | `uni/tn-ROR/BD-ROR_DB_BD` |
| BD | ROR | `uni/tn-ROR/BD-ROR_WEB_BD` |
| BD | SnV | `uni/tn-SnV/BD-antigravity` |
| BD | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1` |
| BD | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-L2-TESTABC1` |
| BD | TEST | `uni/tn-TEST/BD-TESTBD` |
| BD | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/BD-BD-LAB` |
| BD | Test-Tenant | `uni/tn-Test-Tenant/BD-test-BD-01` |
| BD | UT | `uni/tn-UT/BD-FBD` |
| BD | UT | `uni/tn-UT/BD-UBD` |
| BD | prod | `uni/tn-prod/BD-10.1.100.0_24` |
| BD | prod | `uni/tn-prod/BD-10.1.101.0_24` |
| BD | prod | `uni/tn-prod/BD-10.1.102.0_24` |
| BD | prod | `uni/tn-prod/BD-10.1.103.0_24` |
| Subnet (BD) | Heroes | `uni/tn-Heroes/BD-Hero_Land/subnet-[10.1.120.1/22]` |
| Subnet (BD) | Heroes | `uni/tn-Heroes/BD-Hero_Land/subnet-[192.168.120.1/22]` |
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD/subnet-[172.26.200.1/24]` |
| Subnet (BD) | OS1 | `uni/tn-OS1/BD-vlan/subnet-[10.10.10.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_DB_BD/subnet-[10.33.6.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_DB_BD/subnet-[fd00:a:17:6::1/64]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_WEB_BD/subnet-[203.0.113.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_WEB_BD/subnet-[3fff:cb:0:71::1/64]` |
| Subnet (BD) | SnV | `uni/tn-SnV/BD-antigravity/subnet-[10.2.10.1/23]` |
| Subnet (BD) | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.10.1/24]` |
| Subnet (BD) | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.20.1/24]` |
| Subnet (BD) | TEST | `uni/tn-TEST/BD-TESTBD/subnet-[1.1.1.1/24]` |
| Subnet (BD) | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/BD-BD-LAB/subnet-[10.99.1.1/24]` |
| Subnet (BD) | Test-Tenant | `uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.10.254/24]` |
| Subnet (BD) | Test-Tenant | `uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.11.254/24]` |
| Subnet (BD) | Test-Tenant | `uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.12.254/24]` |
| Subnet (BD) | Test-Tenant | `uni/tn-Test-Tenant/BD-test-BD-01/subnet-[10.10.14.254/24]` |
| Subnet (BD) | UT | `uni/tn-UT/BD-UBD/subnet-[192.168.10.254/24]` |
| Subnet (BD) | prod | `uni/tn-prod/BD-10.1.100.0_24/subnet-[10.1.100.1/24]` |
| Subnet (BD) | prod | `uni/tn-prod/BD-10.1.101.0_24/subnet-[10.1.101.1/24]` |
| Subnet (BD) | prod | `uni/tn-prod/BD-10.1.102.0_24/subnet-[10.1.102.1/24]` |
| Subnet (BD) | prod | `uni/tn-prod/BD-10.1.103.0_24/subnet-[10.1.103.1/24]` |
| AP | Heroes | `uni/tn-Heroes/ap-Save_The_Planet` |
| AP | MUHC | `uni/tn-MUHC/ap-LEGACY_APR` |
| AP | OS1 | `uni/tn-OS1/ap-APP-Prod` |
| AP | ROR | `uni/tn-ROR/ap-ROR_WEB_AP` |
| AP | SnV | `uni/tn-SnV/ap-Chaos` |
| AP | SnV | `uni/tn-SnV/ap-Evolution_X` |
| AP | SnV | `uni/tn-SnV/ap-Power_Up` |
| AP | SnV | `uni/tn-SnV/ap-Rescue` |
| AP | TEST | `uni/tn-TEST/ap-TEST_AAEP` |
| AP | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB` |
| AP | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01` |
| AP | UT | `uni/tn-UT/ap-UAP` |
| AP | prod | `uni/tn-prod/ap-vlans` |
| EPG | Heroes | `uni/tn-Heroes/ap-Save_The_Planet/epg-app` |
| EPG | Heroes | `uni/tn-Heroes/ap-Save_The_Planet/epg-db` |
| EPG | Heroes | `uni/tn-Heroes/ap-Save_The_Planet/epg-web` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` |
| EPG | OS1 | `uni/tn-OS1/ap-APP-Prod/epg-APP-WEB` |
| EPG | ROR | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` |
| EPG | ROR | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` |
| EPG | SnV | `uni/tn-SnV/ap-Chaos/epg-Database` |
| EPG | SnV | `uni/tn-SnV/ap-Chaos/epg-Web` |
| EPG | SnV | `uni/tn-SnV/ap-Evolution_X/epg-Database` |
| EPG | SnV | `uni/tn-SnV/ap-Evolution_X/epg-Web` |
| EPG | SnV | `uni/tn-SnV/ap-Power_Up/epg-Database` |
| EPG | SnV | `uni/tn-SnV/ap-Power_Up/epg-Web` |
| EPG | SnV | `uni/tn-SnV/ap-Rescue/epg-Database` |
| EPG | SnV | `uni/tn-SnV/ap-Rescue/epg-Web` |
| EPG | TEST | `uni/tn-TEST/ap-TEST_AAEP/epg-TESTEPG` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-App` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Backup` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-DB` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Dir` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Infra` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mail` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mgmt` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Mon` |
| EPG | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB/epg-EPG-Web` |
| EPG | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01` |
| EPG | UT | `uni/tn-UT/ap-UAP/epg-USER_EPG` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan100` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan101` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan102` |

## APIC faults (faultInst, context only)

| critical | major | minor | warning | info | cleared | total |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | 9 | 54 | 503 | 0 | 15 | 588 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
