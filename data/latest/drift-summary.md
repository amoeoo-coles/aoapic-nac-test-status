# ACI drift report: 2026-11-18

## DRIFT DETECTED - tests 42/129 passed, 87 failed; 147 added, 82 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-11-18 07:26:01 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

## nac-test

- Tests: **129** total, **42** passed, **87** failed, 0 skipped (nac-test exit code 87)

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
| Mgmt | Verify Tenant mgmt | changed | Parent suite setup failed: Url: https://sandboxapicdc.cisco.com/api/aaaLogin.json Expected status: 503 != 200 |
| Mgmt | Verify VRF mgmt/inb | changed | Parent suite setup failed: Url: https://sandboxapicdc.cisco.com/api/aaaLogin.json Expected status: 503 != 200 |
| Mgmt | Verify VRF mgmt/oob | changed | Parent suite setup failed: Url: https://sandboxapicdc.cisco.com/api/aaaLogin.json Expected status: 503 != 200 |
| Mgmt | Verify BD mgmt/inb | changed | Parent suite setup failed: Url: https://sandboxapicdc.cisco.com/api/aaaLogin.json Expected status: 503 != 200 |
| OS1 | Verify Tenant OS1 | missing | Object uni/tn-OS1 not found on APIC |
| OS1 | Verify VRF OS1/OS1 | missing | Object uni/tn-OS1/ctx-OS1 not found on APIC |
| OS1 | Verify BD OS1/VLAN1 | missing | Object uni/tn-OS1/BD-VLAN1 not found on APIC |
| OS1 | Verify BD OS1/vlan | missing | Object uni/tn-OS1/BD-vlan not found on APIC |
| OS1 | Verify Subnet OS1/vlan/10.10.10.1/24 | missing | Object uni/tn-OS1/BD-vlan/subnet-[10.10.10.1/24] not found on APIC |
| OS1 | Verify AP OS1/APP-Prod | missing | Object uni/tn-OS1/ap-APP-Prod not found on APIC |
| OS1 | Verify EPG OS1/APP-Prod/APP-WEB | missing | Object uni/tn-OS1/ap-APP-Prod/epg-APP-WEB not found on APIC |
| Oneaciapp | Verify Tenant oneaciapp | changed | Parent suite setup failed: Url: https://sandboxapicdc.cisco.com/api/aaaLogin.json Expected status: 503 != 200 |
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
| Tenant | 16 | 35 | 29 | 10 |
| VRF | 18 | 30 | 22 | 10 |
| BD | 23 | 35 | 28 | 16 |
| Subnet (BD) | 23 | 30 | 24 | 17 |
| AP | 16 | 23 | 15 | 8 |
| EPG | 33 | 41 | 29 | 21 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (147)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Charlie_Test_Dev | `uni/tn-Charlie_Test_Dev` |
| Tenant | DEV | `uni/tn-DEV` |
| Tenant | DevNetAcademy | `uni/tn-DevNetAcademy` |
| Tenant | Jacob | `uni/tn-Jacob` |
| Tenant | Koushik | `uni/tn-Koushik` |
| Tenant | KoushikM | `uni/tn-KoushikM` |
| Tenant | LAB_KK | `uni/tn-LAB_KK` |
| Tenant | Lab1-TN | `uni/tn-Lab1-TN` |
| Tenant | Lab_Tenant_SAMBI_MTL | `uni/tn-Lab_Tenant_SAMBI_MTL` |
| Tenant | PRD | `uni/tn-PRD` |
| Tenant | PROD | `uni/tn-PROD` |
| Tenant | Pruebas | `uni/tn-Pruebas` |
| Tenant | Pune-Tenants | `uni/tn-Pune-Tenants` |
| Tenant | RB-Tenant | `uni/tn-RB-Tenant` |
| Tenant | SCADA | `uni/tn-SCADA` |
| Tenant | Sistemas | `uni/tn-Sistemas` |
| Tenant | Suresh_Tenant | `uni/tn-Suresh_Tenant` |
| Tenant | TENANT_PROD | `uni/tn-TENANT_PROD` |
| Tenant | TenantPython | `uni/tn-TenantPython` |
| Tenant | TenantPython2 | `uni/tn-TenantPython2` |
| Tenant | Tenant_DEVOPS | `uni/tn-Tenant_DEVOPS` |
| Tenant | User-Applications | `uni/tn-User-Applications` |
| Tenant | XYZ | `uni/tn-XYZ` |
| Tenant | aci_p03_tenant | `uni/tn-aci_p03_tenant` |
| Tenant | aci_p03_vrf | `uni/tn-aci_p03_vrf` |
| Tenant | charlie_terraform | `uni/tn-charlie_terraform` |
| Tenant | l3out-bfd | `uni/tn-l3out-bfd` |
| Tenant | test | `uni/tn-test` |
| Tenant | test-tenant | `uni/tn-test-tenant` |
| VRF | DEV | `uni/tn-DEV/ctx-DEV-VRF` |
| VRF | DevNetAcademy | `uni/tn-DevNetAcademy/ctx-PRIVATE` |
| VRF | DevNetAcademy | `uni/tn-DevNetAcademy/ctx-PUBLIC` |
| VRF | LAB_KK | `uni/tn-LAB_KK/ctx-LAB_VRF` |
| VRF | Lab1-TN | `uni/tn-Lab1-TN/ctx-Lab1-VRF` |
| VRF | PRD | `uni/tn-PRD/ctx-PRD-VRF` |
| VRF | PRD | `uni/tn-PRD/ctx-PRD2-VRF` |
| VRF | PROD | `uni/tn-PROD/ctx-PROD_VRF` |
| VRF | Pune-Tenants | `uni/tn-Pune-Tenants/ctx-PUNE-VRF` |
| VRF | RB-Tenant | `uni/tn-RB-Tenant/ctx-RB-VRF` |
| VRF | SCADA | `uni/tn-SCADA/ctx-SCADA_APP_VRF` |
| VRF | SCADA | `uni/tn-SCADA/ctx-SCADA_DB_VRF` |
| VRF | SCADA | `uni/tn-SCADA/ctx-SCADA_WEB_VRF` |
| VRF | Suresh_Tenant | `uni/tn-Suresh_Tenant/ctx-Suresh_VRF` |
| VRF | Suresh_Tenant | `uni/tn-Suresh_Tenant/ctx-vrf_1` |
| VRF | TENANT_PROD | `uni/tn-TENANT_PROD/ctx-VRF_PROD` |
| VRF | User-Applications | `uni/tn-User-Applications/ctx-PROD` |
| VRF | XYZ | `uni/tn-XYZ/ctx-DEV` |
| VRF | aci_p03_vrf | `uni/tn-aci_p03_vrf/ctx-aci_p03_tennt` |
| VRF | l3out-bfd | `uni/tn-l3out-bfd/ctx-vrf-test` |
| VRF | test-tenant | `uni/tn-test-tenant/ctx-vrf1` |
| VRF | test | `uni/tn-test/ctx-test` |
| BD | DEV | `uni/tn-DEV/BD-10.1.200.0_24` |
| BD | DEV | `uni/tn-DEV/BD-10.1.201.0_24` |
| BD | DEV | `uni/tn-DEV/BD-10.1.255.0_24` |
| BD | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-10.20.30.0` |
| BD | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-113.211.23.0` |
| BD | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-93.0.12.0` |
| BD | LAB_KK | `uni/tn-LAB_KK/BD-LAB_BD` |
| BD | Lab1-TN | `uni/tn-Lab1-TN/BD-Lab1-App-BD` |
| BD | Lab1-TN | `uni/tn-Lab1-TN/BD-Lab1-Web-BD` |
| BD | PRD | `uni/tn-PRD/BD-10.2.200.0_24` |
| BD | PRD | `uni/tn-PRD/BD-10.2.201.0_24` |
| BD | PROD | `uni/tn-PROD/BD-BD-DB` |
| BD | PROD | `uni/tn-PROD/BD-BD-WEB` |
| BD | PROD | `uni/tn-PROD/BD-TEST-BD` |
| BD | Pune-Tenants | `uni/tn-Pune-Tenants/BD-PUNE-BD` |
| BD | RB-Tenant | `uni/tn-RB-Tenant/BD-BD-PRod` |
| BD | SCADA | `uni/tn-SCADA/BD-SCADA_APP_BD` |
| BD | SCADA | `uni/tn-SCADA/BD-SCADA_DB_BD` |
| BD | SCADA | `uni/tn-SCADA/BD-SCADA_WEB_BD` |
| BD | Suresh_Tenant | `uni/tn-Suresh_Tenant/BD-BD_1` |
| BD | Suresh_Tenant | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh` |
| BD | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD-DMZ` |
| BD | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD_CLIENTS` |
| BD | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD_SERVERS` |
| BD | User-Applications | `uni/tn-User-Applications/BD-Jumpbox` |
| BD | User-Applications | `uni/tn-User-Applications/BD-Wordpress` |
| BD | XYZ | `uni/tn-XYZ/BD-DEV` |
| BD | test-tenant | `uni/tn-test-tenant/BD-bd1` |
| Subnet (BD) | DEV | `uni/tn-DEV/BD-10.1.201.0_24/subnet-[10.1.201.1/24]` |
| Subnet (BD) | DEV | `uni/tn-DEV/BD-10.1.255.0_24/subnet-[10.1.255.1/24]` |
| Subnet (BD) | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-10.20.30.0/subnet-[10.20.30.1/29]` |
| Subnet (BD) | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-93.0.12.0/subnet-[93.0.12.1/29]` |
| Subnet (BD) | DevNetAcademy | `uni/tn-DevNetAcademy/BD-NET-93.0.12.0/subnet-[93.0.12.9/29]` |
| Subnet (BD) | Lab1-TN | `uni/tn-Lab1-TN/BD-Lab1-App-BD/subnet-[10.50.20.1/24]` |
| Subnet (BD) | Lab1-TN | `uni/tn-Lab1-TN/BD-Lab1-Web-BD/subnet-[10.50.10.1/24]` |
| Subnet (BD) | PRD | `uni/tn-PRD/BD-10.2.200.0_24/subnet-[10.2.200.1/24]` |
| Subnet (BD) | PRD | `uni/tn-PRD/BD-10.2.201.0_24/subnet-[10.2.201.1/24]` |
| Subnet (BD) | PROD | `uni/tn-PROD/BD-BD-DB/subnet-[30.30.30.1/24]` |
| Subnet (BD) | PROD | `uni/tn-PROD/BD-BD-WEB/subnet-[20.20.20.1/24]` |
| Subnet (BD) | PROD | `uni/tn-PROD/BD-TEST-BD/subnet-[192.168.255.1/24]` |
| Subnet (BD) | Pune-Tenants | `uni/tn-Pune-Tenants/BD-PUNE-BD/subnet-[10.10.21.1/24]` |
| Subnet (BD) | SCADA | `uni/tn-SCADA/BD-SCADA_APP_BD/subnet-[20.0.0.1/24]` |
| Subnet (BD) | SCADA | `uni/tn-SCADA/BD-SCADA_DB_BD/subnet-[10.0.0.1/24]` |
| Subnet (BD) | SCADA | `uni/tn-SCADA/BD-SCADA_WEB_BD/subnet-[30.0.0.1/24]` |
| Subnet (BD) | Suresh_Tenant | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh/subnet-[10.1.1.1/24]` |
| Subnet (BD) | Suresh_Tenant | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh/subnet-[10.1.2.1/24]` |
| Subnet (BD) | Suresh_Tenant | `uni/tn-Suresh_Tenant/BD-Bridgedomain_Suresh/subnet-[10.1.3.1/24]` |
| Subnet (BD) | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD-DMZ/subnet-[10.10.30.1/24]` |
| Subnet (BD) | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD_CLIENTS/subnet-[10.10.20.1/24]` |
| Subnet (BD) | TENANT_PROD | `uni/tn-TENANT_PROD/BD-BD_SERVERS/subnet-[10.10.10.1/24]` |
| Subnet (BD) | User-Applications | `uni/tn-User-Applications/BD-Jumpbox/subnet-[10.100.211.1/24]` |
| Subnet (BD) | User-Applications | `uni/tn-User-Applications/BD-Wordpress/subnet-[10.100.210.1/24]` |
| AP | DEV | `uni/tn-DEV/ap-VLANS` |
| AP | DevNetAcademy | `uni/tn-DevNetAcademy/ap-DATACENTER` |
| AP | DevNetAcademy | `uni/tn-DevNetAcademy/ap-OFFICE` |
| AP | LAB_KK | `uni/tn-LAB_KK/ap-LAB_AP` |
| AP | PRD | `uni/tn-PRD/ap-VLANS` |
| AP | PROD | `uni/tn-PROD/ap-APP-PROFILE` |
| AP | Pune-Tenants | `uni/tn-Pune-Tenants/ap-PUNE-AP` |
| AP | SCADA | `uni/tn-SCADA/ap-SCADA_AP` |
| AP | TENANT_PROD | `uni/tn-TENANT_PROD/ap-APP_PROD` |
| AP | User-Applications | `uni/tn-User-Applications/ap-Jumpbox` |
| AP | User-Applications | `uni/tn-User-Applications/ap-Wordpress-Instace1` |
| AP | XYZ | `uni/tn-XYZ/ap-LEGACY-XYZ-APP` |
| AP | aci_p03_tenant | `uni/tn-aci_p03_tenant/ap-aci_p03` |
| AP | test-tenant | `uni/tn-test-tenant/ap-ap1` |
| AP | test | `uni/tn-test/ap-test_test_AP` |
| EPG | DEV | `uni/tn-DEV/ap-VLANS/epg-VLAN1200` |
| EPG | DEV | `uni/tn-DEV/ap-VLANS/epg-VLAN1201` |
| EPG | DevNetAcademy | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-CLIENTS` |
| EPG | DevNetAcademy | `uni/tn-DevNetAcademy/ap-DATACENTER/epg-FINANCE` |
| EPG | DevNetAcademy | `uni/tn-DevNetAcademy/ap-OFFICE/epg-CLIENTS` |
| EPG | DevNetAcademy | `uni/tn-DevNetAcademy/ap-OFFICE/epg-GUESTS` |
| EPG | LAB_KK | `uni/tn-LAB_KK/ap-LAB_AP/epg-LAB_EPG` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-APP` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-DB` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2200-SRV-WEB` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2201` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-APP` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-DB` |
| EPG | PRD | `uni/tn-PRD/ap-VLANS/epg-VLAN2201-WEB` |
| EPG | PROD | `uni/tn-PROD/ap-APP-PROFILE/epg-DB-EPG` |
| EPG | PROD | `uni/tn-PROD/ap-APP-PROFILE/epg-TEST-EPG` |
| EPG | PROD | `uni/tn-PROD/ap-APP-PROFILE/epg-WEB-EPG` |
| EPG | Pune-Tenants | `uni/tn-Pune-Tenants/ap-PUNE-AP/epg-PUNE-EPG` |
| EPG | SCADA | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_APP_EPG` |
| EPG | SCADA | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_DB_EPG` |
| EPG | SCADA | `uni/tn-SCADA/ap-SCADA_AP/epg-SCADA_WEB_EPG` |
| EPG | TENANT_PROD | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_CLOIENTS` |
| EPG | TENANT_PROD | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_DMZ` |
| EPG | TENANT_PROD | `uni/tn-TENANT_PROD/ap-APP_PROD/epg-EPG_SERVERS` |
| EPG | User-Applications | `uni/tn-User-Applications/ap-Jumpbox/epg-Jumpbox` |
| EPG | User-Applications | `uni/tn-User-Applications/ap-Wordpress-Instace1/epg-Web-Tier` |
| EPG | XYZ | `uni/tn-XYZ/ap-LEGACY-XYZ-APP/epg-LEGACY-XYZ` |
| EPG | test-tenant | `uni/tn-test-tenant/ap-ap1/epg-epg1` |

## Removed since baseline (82)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Heroes | `uni/tn-Heroes` |
| Tenant | MUHC | `uni/tn-MUHC` |
| Tenant | OS1 | `uni/tn-OS1` |
| Tenant | TEST | `uni/tn-TEST` |
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
| Tenant | TN-DEDUP-LAB | `uni/tn-TN-DEDUP-LAB` |
| Tenant | Test-Tenant | `uni/tn-Test-Tenant` |
| Tenant | UT | `uni/tn-UT` |
| Tenant | prod | `uni/tn-prod` |
| Tenant | tn-MGK | `uni/tn-tn-MGK` |
| VRF | Heroes | `uni/tn-Heroes/ctx-Heroes_Only` |
| VRF | OS1 | `uni/tn-OS1/ctx-OS1` |
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
| 49 | 10 | 20 | 626 | 0 | 3 | 708 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
