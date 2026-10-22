# ACI drift report: 2026-10-23

## DRIFT DETECTED - tests 71/129 passed, 58 failed; 122 added, 57 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-10-23 08:10:09 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

## nac-test

- Tests: **129** total, **71** passed, **58** failed, 0 skipped (nac-test exit code 58)

| Suite | Test | Kind | Reason |
|---|---|---|---|
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
| TN-DEDUP-LAB | Verify Tenant TN-DEDUP-LAB | changed | Testumgebung  != Testumgebung fuer aci_contract_dedup.yml |
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
| Tenant | 16 | 22 | 13 | 7 |
| VRF | 18 | 33 | 23 | 8 |
| BD | 23 | 34 | 25 | 14 |
| Subnet (BD) | 23 | 35 | 26 | 14 |
| AP | 16 | 22 | 11 | 5 |
| EPG | 33 | 48 | 24 | 9 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (122)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2` |
| Tenant | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3` |
| Tenant | Cursor_tenant1 | `uni/tn-Cursor_tenant1` |
| Tenant | DEV | `uni/tn-DEV` |
| Tenant | Demo1 | `uni/tn-Demo1` |
| Tenant | LAB-InterVRF | `uni/tn-LAB-InterVRF` |
| Tenant | LAB-MEIRLAN | `uni/tn-LAB-MEIRLAN` |
| Tenant | LAB_ASN_01 | `uni/tn-LAB_ASN_01` |
| Tenant | LAB_ASN_02 | `uni/tn-LAB_ASN_02` |
| Tenant | POC-LN | `uni/tn-POC-LN` |
| Tenant | T1 | `uni/tn-T1` |
| Tenant | hacki-tn-a | `uni/tn-hacki-tn-a` |
| Tenant | lab-t01 | `uni/tn-lab-t01` |
| VRF | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ctx-cursor2_vrf` |
| VRF | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ctx-cursor3_vrf` |
| VRF | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ctx-cursor_vrf` |
| VRF | DEV | `uni/tn-DEV/ctx-DEV-VRF` |
| VRF | Demo1 | `uni/tn-Demo1/ctx-vrf-demo1` |
| VRF | Demo1 | `uni/tn-Demo1/ctx-vrf2-demo1` |
| VRF | LAB-InterVRF | `uni/tn-LAB-InterVRF/ctx-vrfConsolas` |
| VRF | LAB-InterVRF | `uni/tn-LAB-InterVRF/ctx-vrfProduccion` |
| VRF | LAB_ASN_01 | `uni/tn-LAB_ASN_01/ctx-ASN01` |
| VRF | LAB_ASN_01 | `uni/tn-LAB_ASN_01/ctx-ASN02` |
| VRF | LAB_ASN_01 | `uni/tn-LAB_ASN_01/ctx-ASN03` |
| VRF | LAB_ASN_02 | `uni/tn-LAB_ASN_02/ctx-NewASN` |
| VRF | POC-LN | `uni/tn-POC-LN/ctx-VRF-POC-PROD` |
| VRF | T1 | `uni/tn-T1/ctx-V1` |
| VRF | T1 | `uni/tn-T1/ctx-V2` |
| VRF | hacki-tn-a | `uni/tn-hacki-tn-a/ctx-hacki-vrf` |
| VRF | hacki-tn-a | `uni/tn-hacki-tn-a/ctx-hacki-vrf2` |
| VRF | hacki-tn-a | `uni/tn-hacki-tn-a/ctx-hacki-vrf3` |
| VRF | hacki-tn-a | `uni/tn-hacki-tn-a/ctx-hacki-vrf5` |
| VRF | hacki-tn-a | `uni/tn-hacki-tn-a/ctx-hacki-vrf6` |
| VRF | lab-t01 | `uni/tn-lab-t01/ctx-vrf-a` |
| VRF | lab-t01 | `uni/tn-lab-t01/ctx-vrf-b` |
| VRF | oneaciapp | `uni/tn-oneaciapp/ctx-x` |
| BD | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd` |
| BD | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/BD-cursor3_bd` |
| BD | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd` |
| BD | DEV | `uni/tn-DEV/BD-10.1.200.0_24` |
| BD | DEV | `uni/tn-DEV/BD-10.1.201.0_24` |
| BD | DEV | `uni/tn-DEV/BD-10.1.202.0_24` |
| BD | Demo1 | `uni/tn-Demo1/BD-bd-vlan300-web-demo1` |
| BD | Demo1 | `uni/tn-Demo1/BD-bd-vlan301-dab-demo1` |
| BD | LAB-InterVRF | `uni/tn-LAB-InterVRF/BD-bdAdministracion` |
| BD | LAB-InterVRF | `uni/tn-LAB-InterVRF/BD-bdAplicacion` |
| BD | LAB_ASN_01 | `uni/tn-LAB_ASN_01/BD-BD1` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2014_BD` |
| BD | POC-LN | `uni/tn-POC-LN/BD-BD-POC-APP` |
| BD | POC-LN | `uni/tn-POC-LN/BD-BD-POC-DB` |
| BD | POC-LN | `uni/tn-POC-LN/BD-BD-POC-LEGACY` |
| BD | POC-LN | `uni/tn-POC-LN/BD-BD-POC-WEB` |
| BD | T1 | `uni/tn-T1/BD-BD2` |
| BD | T1 | `uni/tn-T1/BD-Bd1` |
| BD | hacki-tn-a | `uni/tn-hacki-tn-a/BD-hacki-bd` |
| BD | hacki-tn-a | `uni/tn-hacki-tn-a/BD-hacki-bd2` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-b` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-db` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-shared` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-web` |
| BD | oneaciapp | `uni/tn-oneaciapp/BD-x` |
| Subnet (BD) | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd/subnet-[10.250.3.1/24]` |
| Subnet (BD) | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/BD-cursor3_bd/subnet-[10.250.4.1/24]` |
| Subnet (BD) | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd/subnet-[10.250.2.1/24]` |
| Subnet (BD) | DEV | `uni/tn-DEV/BD-10.1.200.0_24/subnet-[10.1.200.1/24]` |
| Subnet (BD) | DEV | `uni/tn-DEV/BD-10.1.201.0_24/subnet-[10.1.201.1/24]` |
| Subnet (BD) | DEV | `uni/tn-DEV/BD-10.1.202.0_24/subnet-[10.1.202.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-vlan300-web-demo1/subnet-[10.10.10.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-vlan300-web-demo1/subnet-[20.20.20.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-vlan301-dab-demo1/subnet-[10.193.101.1/24]` |
| Subnet (BD) | Demo1 | `uni/tn-Demo1/BD-bd-vlan301-dab-demo1/subnet-[10.193.102.1/24]` |
| Subnet (BD) | LAB-InterVRF | `uni/tn-LAB-InterVRF/BD-bdAdministracion/subnet-[10.16.110.129/25]` |
| Subnet (BD) | LAB-InterVRF | `uni/tn-LAB-InterVRF/BD-bdAplicacion/subnet-[10.235.40.1/22]` |
| Subnet (BD) | LAB_ASN_01 | `uni/tn-LAB_ASN_01/BD-BD1/subnet-[10.1.1.1/24]` |
| Subnet (BD) | LAB_ASN_01 | `uni/tn-LAB_ASN_01/BD-BD1/subnet-[172.16.1.1/24]` |
| Subnet (BD) | LAB_ASN_01 | `uni/tn-LAB_ASN_01/BD-BD1/subnet-[192.168.1.1/24]` |
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2014_BD/subnet-[172.26.34.1/23]` |
| Subnet (BD) | POC-LN | `uni/tn-POC-LN/BD-BD-POC-APP/subnet-[10.31.20.1/24]` |
| Subnet (BD) | POC-LN | `uni/tn-POC-LN/BD-BD-POC-DB/subnet-[10.31.30.1/24]` |
| Subnet (BD) | POC-LN | `uni/tn-POC-LN/BD-BD-POC-WEB/subnet-[10.31.10.1/24]` |
| Subnet (BD) | T1 | `uni/tn-T1/BD-BD2/subnet-[192.168.60.254/24]` |
| Subnet (BD) | hacki-tn-a | `uni/tn-hacki-tn-a/BD-hacki-bd/subnet-[10.9.8.7/24]` |
| Subnet (BD) | hacki-tn-a | `uni/tn-hacki-tn-a/BD-hacki-bd2/subnet-[10.8.7.6/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-b/subnet-[10.20.1.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-db/subnet-[10.10.2.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-shared/subnet-[10.30.1.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-web/subnet-[10.10.1.1/24]` |
| AP | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap` |
| AP | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ap-cursor3_ap` |
| AP | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap` |
| AP | DEV | `uni/tn-DEV/ap-VLANS` |
| AP | Demo1 | `uni/tn-Demo1/ap-ap-demo1` |
| AP | LAB-InterVRF | `uni/tn-LAB-InterVRF/ap-apInterVRF` |
| AP | POC-LN | `uni/tn-POC-LN/ap-AP-POC-SHOP` |
| AP | T1 | `uni/tn-T1/ap-User_App_Profile` |
| AP | hacki-tn-a | `uni/tn-hacki-tn-a/ap-hacki-ap1` |
| AP | lab-t01 | `uni/tn-lab-t01/ap-ap-01` |
| AP | oneaciapp | `uni/tn-oneaciapp/ap-x` |
| EPG | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` |
| EPG | Cursor_Tenant3 | `uni/tn-Cursor_Tenant3/ap-cursor3_ap/epg-web` |
| EPG | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` |
| EPG | DEV | `uni/tn-DEV/ap-VLANS/epg-VLAN200` |
| EPG | DEV | `uni/tn-DEV/ap-VLANS/epg-VLAN201` |
| EPG | DEV | `uni/tn-DEV/ap-VLANS/epg-VLAN202` |
| EPG | Demo1 | `uni/tn-Demo1/ap-ap-demo1/epg-epg-vlan300-web-demo1` |
| EPG | Demo1 | `uni/tn-Demo1/ap-ap-demo1/epg-epg-vlan301-dab-demo1` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2781_EPG` |
| EPG | POC-LN | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-APP` |
| EPG | POC-LN | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-DB` |
| EPG | POC-LN | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-LEGACY` |
| EPG | POC-LN | `uni/tn-POC-LN/ap-AP-POC-SHOP/epg-EPG-POC-WEB` |
| EPG | T1 | `uni/tn-T1/ap-User_App_Profile/epg-Users_EPG` |
| EPG | hacki-tn-a | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-DB` |
| EPG | hacki-tn-a | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-back` |
| EPG | hacki-tn-a | `uni/tn-hacki-tn-a/ap-hacki-ap1/epg-EPG-web` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-b` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-db` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-shared` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-web` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-x/epg-2323323` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-x/epg-234` |
| EPG | oneaciapp | `uni/tn-oneaciapp/ap-x/epg-x` |

## Removed since baseline (57)

| Type | Tenant | DN |
|---|---|---|
| Tenant | OS1 | `uni/tn-OS1` |
| Tenant | TEST | `uni/tn-TEST` |
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
| Tenant | Test-Tenant | `uni/tn-Test-Tenant` |
| Tenant | UT | `uni/tn-UT` |
| Tenant | prod | `uni/tn-prod` |
| Tenant | tn-MGK | `uni/tn-tn-MGK` |
| VRF | OS1 | `uni/tn-OS1/ctx-OS1` |
| VRF | TEST-ABC1 | `uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1` |
| VRF | TEST | `uni/tn-TEST/ctx-TEST` |
| VRF | Test-Tenant | `uni/tn-Test-Tenant/ctx-Test-VRF` |
| VRF | UT | `uni/tn-UT/ctx-FWVRF` |
| VRF | UT | `uni/tn-UT/ctx-UVRF` |
| VRF | prod | `uni/tn-prod/ctx-prod.prod-vrf` |
| VRF | tn-MGK | `uni/tn-tn-MGK/ctx-ctx-MGK` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD` |
| BD | MUHC | `uni/tn-MUHC/BD-VLAN_2780_BD` |
| BD | OS1 | `uni/tn-OS1/BD-VLAN1` |
| BD | OS1 | `uni/tn-OS1/BD-vlan` |
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
| Subnet (BD) | MUHC | `uni/tn-MUHC/BD-VLAN_2701_BD/subnet-[172.26.200.1/24]` |
| Subnet (BD) | OS1 | `uni/tn-OS1/BD-vlan/subnet-[10.10.10.1/24]` |
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
| AP | OS1 | `uni/tn-OS1/ap-APP-Prod` |
| AP | TEST | `uni/tn-TEST/ap-TEST_AAEP` |
| AP | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01` |
| AP | UT | `uni/tn-UT/ap-UAP` |
| AP | prod | `uni/tn-prod/ap-vlans` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2701_EPG` |
| EPG | MUHC | `uni/tn-MUHC/ap-LEGACY_APR/epg-VLAN_2780_EPG` |
| EPG | OS1 | `uni/tn-OS1/ap-APP-Prod/epg-APP-WEB` |
| EPG | TEST | `uni/tn-TEST/ap-TEST_AAEP/epg-TESTEPG` |
| EPG | Test-Tenant | `uni/tn-Test-Tenant/ap-Test-APP-Profile-01/epg-test-epg-01` |
| EPG | UT | `uni/tn-UT/ap-UAP/epg-USER_EPG` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan100` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan101` |
| EPG | prod | `uni/tn-prod/ap-vlans/epg-vlan102` |

## APIC faults (faultInst, context only)

| critical | major | minor | warning | info | cleared | total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 13 | 55 | 720 | 0 | 15 | 833 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
