# ACI drift report: 2026-10-26

## DRIFT DETECTED - tests 20/129 passed, 109 failed; 3 added, 109 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-10-26 08:07:37 AEDT (Australia/Melbourne)
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
| Tenant | 16 | 5 | 1 | 12 |
| VRF | 18 | 7 | 1 | 12 |
| BD | 23 | 5 | 1 | 19 |
| Subnet (BD) | 23 | 1 | 0 | 22 |
| AP | 16 | 3 | 0 | 13 |
| EPG | 33 | 2 | 0 | 31 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (3)

| Type | Tenant | DN |
|---|---|---|
| Tenant | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN` |
| VRF | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN/ctx-VRF_PROD` |
| BD | TF_LAB_SAMAN | `uni/tn-TF_LAB_SAMAN/BD-BD_10` |

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
| 2 | 4 | 3 | 626 | 0 | 5 | 640 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
