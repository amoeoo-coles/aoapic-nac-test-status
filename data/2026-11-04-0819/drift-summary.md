# ACI drift report: 2026-11-04

## DRIFT DETECTED - tests 45/129 passed, 84 failed; 10 added, 84 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-11-04 08:19:36 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

## nac-test

- Tests: **129** total, **45** passed, **84** failed, 0 skipped (nac-test exit code 84)

| Suite | Test | Kind | Reason |
|---|---|---|---|
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
| Tenant | 16 | 8 | 2 | 10 |
| VRF | 18 | 10 | 2 | 10 |
| BD | 23 | 9 | 3 | 17 |
| Subnet (BD) | 23 | 7 | 3 | 19 |
| AP | 16 | 8 | 0 | 8 |
| EPG | 33 | 13 | 0 | 20 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (10)

| Type | Tenant | DN |
|---|---|---|
| Tenant | TENANT-LAB | `uni/tn-TENANT-LAB` |
| Tenant | dev-demo | `uni/tn-dev-demo` |
| VRF | TENANT-LAB | `uni/tn-TENANT-LAB/ctx-VRF-PRODUCAO` |
| VRF | dev-demo | `uni/tn-dev-demo/ctx-vrf-dev-poc` |
| BD | TENANT-LAB | `uni/tn-TENANT-LAB/BD-BD-APP` |
| BD | TENANT-LAB | `uni/tn-TENANT-LAB/BD-BD-WEB` |
| BD | dev-demo | `uni/tn-dev-demo/BD-BD-INTERNAL-POC` |
| Subnet (BD) | TENANT-LAB | `uni/tn-TENANT-LAB/BD-BD-APP/subnet-[10.10.20.1/24]` |
| Subnet (BD) | TENANT-LAB | `uni/tn-TENANT-LAB/BD-BD-WEB/subnet-[10.10.10.1/24]` |
| Subnet (BD) | mgmt | `uni/tn-mgmt/BD-inb/subnet-[192.168.1.1/24]` |

## Removed since baseline (84)

| Type | Tenant | DN |
|---|---|---|
| Tenant | MUHC | `uni/tn-MUHC` |
| Tenant | OS1 | `uni/tn-OS1` |
| Tenant | ROR | `uni/tn-ROR` |
| Tenant | TEST | `uni/tn-TEST` |
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
| Tenant | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB` |
| Tenant | Test-Tenant | `uni/tn-Test-Tenant` |
| Tenant | UT | `uni/tn-UT` |
| Tenant | prod | `uni/tn-prod` |
| Tenant | tn-MGK | `uni/tn-tn-MGK` |
| VRF | OS1 | `uni/tn-OS1/ctx-OS1` |
| VRF | ROR | `uni/tn-ROR/ctx-ROR_VRF` |
| VRF | TEST-ABC1 | `uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1` |
| VRF | TEST | `uni/tn-TEST/ctx-TEST` |
| VRF | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ctx-VRF-LAB` |
| VRF | Test-Tenant | `uni/tn-Test-Tenant/ctx-Test-VRF` |
| VRF | UT | `uni/tn-UT/ctx-FWVRF` |
| VRF | UT | `uni/tn-UT/ctx-UVRF` |
| VRF | prod | `uni/tn-prod/ctx-prod.prod-vrf` |
| VRF | tn-MGK | `uni/tn-tn-MGK/ctx-ctx-MGK` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2780_BD` |
| BD | OS1 | `uni/tn-OS1/BD-VLAN1` |
| BD | OS1 | `uni/tn-OS1/BD-vlan` |
| BD | ROR | `uni/tn-ROR/BD-ROR_DB_BD` |
| BD | ROR | `uni/tn-ROR/BD-ROR_WEB_BD` |
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
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD/subnet-[172.26.200.1/24]` |
| Subnet (BD) | OS1 | `uni/tn-OS1/BD-vlan/subnet-[10.10.10.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_DB_BD/subnet-[10.33.6.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_DB_BD/subnet-[fd00:a:17:6::1/64]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_WEB_BD/subnet-[203.0.113.1/24]` |
| Subnet (BD) | ROR | `uni/tn-ROR/BD-ROR_WEB_BD/subnet-[3fff:cb:0:71::1/64]` |
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
| AP | MUHC | `uni/tn-MUHC/ap-LEGACY_APR` |
| AP | OS1 | `uni/tn-OS1/ap-APP-Prod` |
| AP | ROR | `uni/tn-ROR/ap-ROR_WEB_AP` |
| AP | TEST | `uni/tn-TEST/ap-TEST_AAEP` |
| AP | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB/ap-AP-LAB` |
| AP | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01` |
| AP | UT | `uni/tn-UT/ap-UAP` |
| AP | prod | `uni/tn-prod/ap-vlans` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` |
| EPG | OS1 | `uni/tn-OS1/ap-APP-Prod/epg-APP-WEB` |
| EPG | ROR | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_DB_EPG` |
| EPG | ROR | `uni/tn-ROR/ap-ROR_WEB_AP/epg-ROR_WEB_EPG` |
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
| 51 | 2 | 14 | 595 | 0 | 12 | 674 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
