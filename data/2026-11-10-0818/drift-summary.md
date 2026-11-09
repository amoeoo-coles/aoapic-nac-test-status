# ACI drift report: 2026-11-10

## DRIFT DETECTED - tests 20/129 passed, 109 failed; 190 added, 109 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-11-10 08:18:59 AEDT (Australia/Melbourne)
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
| Tenant | 16 | 30 | 26 | 12 |
| VRF | 18 | 33 | 27 | 12 |
| BD | 23 | 46 | 42 | 19 |
| Subnet (BD) | 23 | 36 | 35 | 22 |
| AP | 16 | 25 | 22 | 13 |
| EPG | 33 | 40 | 38 | 31 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (190)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2` |
| Tenant | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3` |
| Tenant | Cursor_tenant1 | `uni/tn-Cursor_tenant1` |
| Tenant | Cursor_tenant5 | `uni/tn-Cursor_tenant5` |
| Tenant | EM-LAB | `uni/tn-EM-LAB` |
| Tenant | LAB-TENANT | `uni/tn-LAB-TENANT` |
| Tenant | MGMT_LAN | `uni/tn-MGMT_LAN` |
| Tenant | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB` |
| Tenant | RB-Tenant | `uni/tn-RB-Tenant` |
| Tenant | TESTING123 | `uni/tn-TESTING123` |
| Tenant | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01` |
| Tenant | TN-LAB-K01 | `uni/tn-TN-LAB-K01` |
| Tenant | TN-LAB-K02 | `uni/tn-TN-LAB-K02` |
| Tenant | Tenant-Ahmed | `uni/tn-Tenant-Ahmed` |
| Tenant | Tenant_RG | `uni/tn-Tenant_RG` |
| Tenant | Test100 | `uni/tn-Test100` |
| Tenant | Test_9112026 | `uni/tn-Test_9112026` |
| Tenant | VY-TN | `uni/tn-VY-TN` |
| Tenant | Zangief | `uni/tn-Zangief` |
| Tenant | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9` |
| Tenant | iTenant | `uni/tn-iTenant` |
| Tenant | mjay_dev | `uni/tn-mjay_dev` |
| Tenant | tenant_mylab | `uni/tn-tenant_mylab` |
| Tenant | tn_example_tenant | `uni/tn-tn_example_tenant` |
| Tenant | zzzps4021 | `uni/tn-zzzps4021` |
| Tenant | zzzps4021_BGP | `uni/tn-zzzps4021_BGP` |
| VRF | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ctx-cursor2_vrf` |
| VRF | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ctx-cursor3_vrf` |
| VRF | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ctx-cursor_vrf` |
| VRF | Cursor_tenant5 | `uni/tn-Cursor_tenant5/ctx-cursor5_vrf` |
| VRF | LAB-TENANT | `uni/tn-LAB-TENANT/ctx-LAB-VRF` |
| VRF | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/ctx-VRF-PROD` |
| VRF | RB-Tenant | `uni/tn-RB-Tenant/ctx-RB-VRF` |
| VRF | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/ctx-VRF-LAB` |
| VRF | TN-LAB-K01 | `uni/tn-TN-LAB-K01/ctx-vrf-lab01` |
| VRF | TN-LAB-K02 | `uni/tn-TN-LAB-K02/ctx-VRF-LAB` |
| VRF | Tenant-Ahmed | `uni/tn-Tenant-Ahmed/ctx-VRF-1` |
| VRF | Tenant_RG | `uni/tn-Tenant_RG/ctx-RG_EXT_VRF` |
| VRF | Tenant_RG | `uni/tn-Tenant_RG/ctx-VRF_RG` |
| VRF | Test100 | `uni/tn-Test100/ctx-DEV` |
| VRF | Test100 | `uni/tn-Test100/ctx-PROD` |
| VRF | Test_9112026 | `uni/tn-Test_9112026/ctx-IAAS-PSNXXX_VRF` |
| VRF | Test_9112026 | `uni/tn-Test_9112026/ctx-IAAS-STRE-SHRP01-PSN-COL_VRF` |
| VRF | VY-TN | `uni/tn-VY-TN/ctx-VY-VRF` |
| VRF | VY-TN | `uni/tn-VY-TN/ctx-VY-VRF02` |
| VRF | VY-TN | `uni/tn-VY-TN/ctx-VY-VRF03` |
| VRF | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/ctx-billing-test-DPYD6hPFFmE9-vrf` |
| VRF | tn_example_tenant | `uni/tn-tn_example_tenant/ctx-my_example_vrf` |
| VRF | zzzps4021 | `uni/tn-zzzps4021/ctx-DEV` |
| VRF | zzzps4021 | `uni/tn-zzzps4021/ctx-PROD` |
| VRF | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ctx-VY-VRF` |
| VRF | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ctx-VY-VRF02` |
| VRF | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ctx-VY-VRF03` |
| BD | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd` |
| BD | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/BD-cursor3_bd` |
| BD | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_app_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_db_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_app_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_db_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_dmz_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_web_bd` |
| BD | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_web_bd` |
| BD | LAB-TENANT | `uni/tn-LAB-TENANT/BD-LAB-BD` |
| BD | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-APP` |
| BD | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-DB` |
| BD | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-WEB` |
| BD | RB-Tenant | `uni/tn-RB-Tenant/BD-RB-BD` |
| BD | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-APP` |
| BD | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-DB` |
| BD | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-WEB` |
| BD | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-APP` |
| BD | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-DB` |
| BD | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-WEB` |
| BD | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-APP` |
| BD | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-DB` |
| BD | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-WE` |
| BD | Tenant_RG | `uni/tn-Tenant_RG/BD-L2_BD_RG` |
| BD | Tenant_RG | `uni/tn-Tenant_RG/BD-RG_BD_EXT_L2` |
| BD | Test100 | `uni/tn-Test100/BD-DEV-APP` |
| BD | Test100 | `uni/tn-Test100/BD-DEV-DB` |
| BD | Test100 | `uni/tn-Test100/BD-PROD-APP` |
| BD | Test100 | `uni/tn-Test100/BD-PROD-DB` |
| BD | VY-TN | `uni/tn-VY-TN/BD-VY-BD` |
| BD | VY-TN | `uni/tn-VY-TN/BD-VY-BD02` |
| BD | VY-TN | `uni/tn-VY-TN/BD-VY-BD03` |
| BD | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/BD-bd-vlan102` |
| BD | tn_example_tenant | `uni/tn-tn_example_tenant/BD-Production-BD` |
| BD | zzzps4021 | `uni/tn-zzzps4021/BD-DEV-APP` |
| BD | zzzps4021 | `uni/tn-zzzps4021/BD-DEV-DB` |
| BD | zzzps4021 | `uni/tn-zzzps4021/BD-PROD-APP` |
| BD | zzzps4021 | `uni/tn-zzzps4021/BD-PROD-DB` |
| BD | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/BD-VY-BD` |
| BD | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/BD-VY-BD02` |
| BD | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/BD-VY-BD03` |
| Subnet (BD) | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd/subnet-[10.250.3.1/24]` |
| Subnet (BD) | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/BD-cursor3_bd/subnet-[10.250.4.1/24]` |
| Subnet (BD) | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd/subnet-[10.250.2.1/24]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_app_bd/subnet-[10.250.52.1/24]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_db_bd/subnet-[10.250.53.1/24]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_app_bd/subnet-[10.250.59.33/28]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_db_bd/subnet-[10.250.59.49/28]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_dmz_bd/subnet-[10.250.59.1/28]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_fw_web_bd/subnet-[10.250.59.17/28]` |
| Subnet (BD) | Cursor_tenant5 | `uni/tn-Cursor_tenant5/BD-cursor5_web_bd/subnet-[10.250.51.1/24]` |
| Subnet (BD) | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-APP/subnet-[10.10.20.1/24]` |
| Subnet (BD) | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-DB/subnet-[10.10.30.1/24]` |
| Subnet (BD) | NZ-ACI-LAB | `uni/tn-NZ-ACI-LAB/BD-BD-WEB/subnet-[10.10.10.1/24]` |
| Subnet (BD) | RB-Tenant | `uni/tn-RB-Tenant/BD-RB-BD/subnet-[10.10.10.1/24]` |
| Subnet (BD) | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-APP/subnet-[10.10.20.1/24]` |
| Subnet (BD) | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-DB/subnet-[10.10.30.1/24]` |
| Subnet (BD) | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/BD-BD-WEB/subnet-[10.10.10.1/24]` |
| Subnet (BD) | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-APP/subnet-[192.168.20.1/24]` |
| Subnet (BD) | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-DB/subnet-[192.168.30.1/24]` |
| Subnet (BD) | TN-LAB-K01 | `uni/tn-TN-LAB-K01/BD-BD-WEB/subnet-[192.168.10.1/24]` |
| Subnet (BD) | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-APP/subnet-[10.10.10.1/24]` |
| Subnet (BD) | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-DB/subnet-[10.10.30.1/24]` |
| Subnet (BD) | TN-LAB-K02 | `uni/tn-TN-LAB-K02/BD-BD-WE/subnet-[10.10.20.1/24]` |
| Subnet (BD) | Test100 | `uni/tn-Test100/BD-DEV-APP/subnet-[192.168.3.1/24]` |
| Subnet (BD) | Test100 | `uni/tn-Test100/BD-DEV-DB/subnet-[192.168.4.1/24]` |
| Subnet (BD) | Test100 | `uni/tn-Test100/BD-PROD-APP/subnet-[192.168.2.1/24]` |
| Subnet (BD) | Test100 | `uni/tn-Test100/BD-PROD-DB/subnet-[192.168.1.1/24]` |
| Subnet (BD) | VY-TN | `uni/tn-VY-TN/BD-VY-BD/subnet-[10.2.2.254/24]` |
| Subnet (BD) | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/BD-bd-vlan102/subnet-[10.102.0.1/24]` |
| Subnet (BD) | tn_example_tenant | `uni/tn-tn_example_tenant/BD-Production-BD/subnet-[192.0.2.1/29]` |
| Subnet (BD) | zzzps4021 | `uni/tn-zzzps4021/BD-DEV-APP/subnet-[198.18.12.1/24]` |
| Subnet (BD) | zzzps4021 | `uni/tn-zzzps4021/BD-DEV-DB/subnet-[198.18.13.1/24]` |
| Subnet (BD) | zzzps4021 | `uni/tn-zzzps4021/BD-PROD-APP/subnet-[198.18.11.1/24]` |
| Subnet (BD) | zzzps4021 | `uni/tn-zzzps4021/BD-PROD-DB/subnet-[198.18.10.1/24]` |
| Subnet (BD) | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/BD-VY-BD/subnet-[198.18.30.1/24]` |
| AP | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap` |
| AP | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ap-cursor3_ap` |
| AP | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap` |
| AP | Cursor_tenant5 | `uni/tn-Cursor_tenant5/ap-cursor5_ap` |
| AP | LAB-TENANT | `uni/tn-LAB-TENANT/ap-LAB-APP` |
| AP | MGMT_LAN | `uni/tn-MGMT_LAN/ap-AP-MGMT` |
| AP | RB-Tenant | `uni/tn-RB-Tenant/ap-FTP` |
| AP | RB-Tenant | `uni/tn-RB-Tenant/ap-WWW` |
| AP | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL` |
| AP | TN-LAB-K01 | `uni/tn-TN-LAB-K01/ap-AP-LAB01` |
| AP | TN-LAB-K02 | `uni/tn-TN-LAB-K02/ap-WEB-APP` |
| AP | Tenant-Ahmed | `uni/tn-Tenant-Ahmed/ap-App-X` |
| AP | Tenant_RG | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3` |
| AP | Test100 | `uni/tn-Test100/ap-DEV` |
| AP | Test100 | `uni/tn-Test100/ap-PROD` |
| AP | VY-TN | `uni/tn-VY-TN/ap-VY-AP` |
| AP | Zangief | `uni/tn-Zangief/ap-LEGACY-DIAG-APP` |
| AP | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal` |
| AP | tn_example_tenant | `uni/tn-tn_example_tenant/ap-app-profile` |
| AP | zzzps4021 | `uni/tn-zzzps4021/ap-DEV` |
| AP | zzzps4021 | `uni/tn-zzzps4021/ap-PROD` |
| AP | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ap-VY-AP` |
| EPG | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` |
| EPG | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` |
| EPG | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` |
| EPG | Cursor_tenant5 | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-app` |
| EPG | Cursor_tenant5 | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-db` |
| EPG | Cursor_tenant5 | `uni/tn-Cursor_tenant5/ap-cursor5_ap/epg-web` |
| EPG | LAB-TENANT | `uni/tn-LAB-TENANT/ap-LAB-APP/epg-WEB-EPG` |
| EPG | RB-Tenant | `uni/tn-RB-Tenant/ap-FTP/epg-FTP-EPG` |
| EPG | RB-Tenant | `uni/tn-RB-Tenant/ap-WWW/epg-WWW` |
| EPG | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-APP` |
| EPG | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-DB` |
| EPG | TN-LAB-ANS01 | `uni/tn-TN-LAB-ANS01/ap-AP-PORTAL/epg-EPG-WEB` |
| EPG | TN-LAB-K01 | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-APP` |
| EPG | TN-LAB-K01 | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-DB` |
| EPG | TN-LAB-K01 | `uni/tn-TN-LAB-K01/ap-AP-LAB01/epg-EPG-WEB` |
| EPG | TN-LAB-K02 | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-APP` |
| EPG | TN-LAB-K02 | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-DB` |
| EPG | TN-LAB-K02 | `uni/tn-TN-LAB-K02/ap-WEB-APP/epg-EGP-WEB` |
| EPG | Tenant_RG | `uni/tn-Tenant_RG/ap-EXTERNAL_L2_L3/epg-EXT_L2` |
| EPG | Test100 | `uni/tn-Test100/ap-DEV/epg-D-APP` |
| EPG | Test100 | `uni/tn-Test100/ap-DEV/epg-D-DB` |
| EPG | Test100 | `uni/tn-Test100/ap-PROD/epg-P-APP` |
| EPG | Test100 | `uni/tn-Test100/ap-PROD/epg-P-DB` |
| EPG | VY-TN | `uni/tn-VY-TN/ap-VY-AP/epg-EPG2` |
| EPG | VY-TN | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG` |
| EPG | VY-TN | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG02` |
| EPG | VY-TN | `uni/tn-VY-TN/ap-VY-AP/epg-VY-EPG03` |
| EPG | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-app` |
| EPG | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-db` |
| EPG | billing-test-DPYD6hPFFmE9 | `uni/tn-billing-test-DPYD6hPFFmE9/ap-billing-portal/epg-testers` |
| EPG | zzzps4021 | `uni/tn-zzzps4021/ap-DEV/epg-D-APP` |
| EPG | zzzps4021 | `uni/tn-zzzps4021/ap-DEV/epg-D-DB` |
| EPG | zzzps4021 | `uni/tn-zzzps4021/ap-PROD/epg-P-APP` |
| EPG | zzzps4021 | `uni/tn-zzzps4021/ap-PROD/epg-P-DB` |
| EPG | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-EPG2` |
| EPG | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG` |
| EPG | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG02` |
| EPG | zzzps4021_BGP | `uni/tn-zzzps4021_BGP/ap-VY-AP/epg-VY-EPG03` |

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
| 13 | 4 | 492 | 727 | 0 | 6 | 1242 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
