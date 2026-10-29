# ACI drift report: 2026-10-30

## DRIFT DETECTED - tests 35/129 passed, 94 failed; 67 added, 93 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-10-30 08:16:24 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

## nac-test

- Tests: **129** total, **35** passed, **94** failed, 0 skipped (nac-test exit code 94)

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
| MUHC | Verify BD MUHC/VLAN_2780_BD | missing | Object uni/tn-MUHC/BD-VLAN_2780_BD not found on APIC |
| MUHC | Verify BD MUHC/VLAN_2701_BD | missing | Object uni/tn-MUHC/BD-VLAN_2701_BD not found on APIC |
| MUHC | Verify Subnet MUHC/VLAN_2701_BD/172.26.200.1/24 | missing | Object uni/tn-MUHC/BD-VLAN_2701_BD/subnet-[172.26.200.1/24] not found on APIC |
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
| TN-DEDUP-LAB | Verify Tenant TN-DEDUP-LAB | changed | Ansible test running != Testumgebung fuer aci_contract_dedup.yml |
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
| Tenant | 16 | 17 | 11 | 10 |
| VRF | 18 | 20 | 13 | 11 |
| BD | 23 | 16 | 11 | 18 |
| Subnet (BD) | 23 | 12 | 10 | 21 |
| AP | 16 | 10 | 5 | 11 |
| EPG | 33 | 28 | 17 | 22 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (67)

| Type | Tenant | DN |
|---|---|---|
| Tenant | ASN-02 | `uni/tn-ASN-02` |
| Tenant | ASN_01 | `uni/tn-ASN_01` |
| Tenant | Automation-Test | `uni/tn-Automation-Test` |
| Tenant | Irelia-TEST | `uni/tn-Irelia-TEST` |
| Tenant | T1_FIRST | `uni/tn-T1_FIRST` |
| Tenant | TN-AUTO | `uni/tn-TN-AUTO` |
| Tenant | TN_PROD | `uni/tn-TN_PROD` |
| Tenant | Test101 | `uni/tn-Test101` |
| Tenant | TestTenant | `uni/tn-TestTenant` |
| Tenant | ddso | `uni/tn-ddso` |
| Tenant | gtest | `uni/tn-gtest` |
| VRF | ASN-02 | `uni/tn-ASN-02/ctx-VRF_ASN-02A` |
| VRF | ASN-02 | `uni/tn-ASN-02/ctx-VRF_PRUEBA` |
| VRF | ASN_01 | `uni/tn-ASN_01/ctx-VRF_A1` |
| VRF | ASN_01 | `uni/tn-ASN_01/ctx-VRF_A2` |
| VRF | ASN_01 | `uni/tn-ASN_01/ctx-VRF_A3` |
| VRF | T1_FIRST | `uni/tn-T1_FIRST/ctx-V1_First` |
| VRF | TN-AUTO | `uni/tn-TN-AUTO/ctx-VRF_AUTO` |
| VRF | TN_PROD | `uni/tn-TN_PROD/ctx-VRF_PROD` |
| VRF | Test101 | `uni/tn-Test101/ctx-DEV` |
| VRF | Test101 | `uni/tn-Test101/ctx-PROD` |
| VRF | TestTenant | `uni/tn-TestTenant/ctx-TestVRF` |
| VRF | ddso | `uni/tn-ddso/ctx-VRF11` |
| VRF | gtest | `uni/tn-gtest/ctx-gtest-vrf` |
| BD | ASN_01 | `uni/tn-ASN_01/BD-BD01` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2341_BD` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2342_BD` |
| BD | T1_FIRST | `uni/tn-T1_FIRST/BD-BD_FIRST` |
| BD | TN-AUTO | `uni/tn-TN-AUTO/BD-BD_AUTO` |
| BD | Test101 | `uni/tn-Test101/BD-BD10` |
| BD | Test101 | `uni/tn-Test101/BD-BD100` |
| BD | Test101 | `uni/tn-Test101/BD-BD20` |
| BD | Test101 | `uni/tn-Test101/BD-BD200` |
| BD | ddso | `uni/tn-ddso/BD-BD11` |
| BD | gtest | `uni/tn-gtest/BD-gtest-bridge` |
| Subnet (BD) | ASN_01 | `uni/tn-ASN_01/BD-BD01/subnet-[10.1.1.1/24]` |
| Subnet (BD) | ASN_01 | `uni/tn-ASN_01/BD-BD01/subnet-[11.1.1.1/24]` |
| Subnet (BD) | ASN_01 | `uni/tn-ASN_01/BD-BD01/subnet-[12.1.1.1/24]` |
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2341_BD/subnet-[172.26.193.97/27]` |
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2342_BD/subnet-[172.26.193.129/27]` |
| Subnet (BD) | T1_FIRST | `uni/tn-T1_FIRST/BD-BD_FIRST/subnet-[192.168.20.254/24]` |
| Subnet (BD) | Test101 | `uni/tn-Test101/BD-BD10/subnet-[192.168.10.1/24]` |
| Subnet (BD) | Test101 | `uni/tn-Test101/BD-BD100/subnet-[192.168.100.1/24]` |
| Subnet (BD) | Test101 | `uni/tn-Test101/BD-BD20/subnet-[192.168.20.1/24]` |
| Subnet (BD) | Test101 | `uni/tn-Test101/BD-BD200/subnet-[192.168.200.1/24]` |
| AP | ASN-02 | `uni/tn-ASN-02/ap-AP` |
| AP | T1_FIRST | `uni/tn-T1_FIRST/ap-Users_APP_Profile` |
| AP | Test101 | `uni/tn-Test101/ap-DEV` |
| AP | Test101 | `uni/tn-Test101/ap-PROD` |
| AP | gtest | `uni/tn-gtest/ap-gtest-apps` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2341_EPG` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2342_EPG` |
| EPG | T1_FIRST | `uni/tn-T1_FIRST/ap-Users_APP_Profile/epg-USERS_EPG` |
| EPG | Test101 | `uni/tn-Test101/ap-DEV/epg-DEV-APP` |
| EPG | Test101 | `uni/tn-Test101/ap-DEV/epg-DEV-DB` |
| EPG | Test101 | `uni/tn-Test101/ap-PROD/epg-PROD-APP` |
| EPG | Test101 | `uni/tn-Test101/ap-PROD/epg-PROD-DB` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Arizona` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-California` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Florida` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Idaho` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Nebraska` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Nevada` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Oklahoma` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Texas` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Utah` |
| EPG | gtest | `uni/tn-gtest/ap-gtest-apps/epg-Washington` |

## Removed since baseline (93)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Heroes | `uni/tn-Heroes` |
| Tenant | OS1 | `uni/tn-OS1` |
| Tenant | ROR | `uni/tn-ROR` |
| Tenant | SnV | `uni/tn-SnV` |
| Tenant | TEST | `uni/tn-TEST` |
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
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
| AP | OS1 | `uni/tn-OS1/ap-APP-Prod` |
| AP | ROR | `uni/tn-ROR/ap-ROR_WEB_AP` |
| AP | SnV | `uni/tn-SnV/ap-Chaos` |
| AP | SnV | `uni/tn-SnV/ap-Evolution_X` |
| AP | SnV | `uni/tn-SnV/ap-Power_Up` |
| AP | SnV | `uni/tn-SnV/ap-Rescue` |
| AP | TEST | `uni/tn-TEST/ap-TEST_AAEP` |
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
| EPG | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01` |
| EPG | UT | `uni/tn-UT/ap-UAP/epg-USER_EPG` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan100` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan101` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan102` |

## APIC faults (faultInst, context only)

| critical | major | minor | warning | info | cleared | total |
|---:|---:|---:|---:|---:|---:|---:|
| 17 | 9 | 49 | 604 | 0 | 6 | 685 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
