# ACI drift report: 2026-10-22

## DRIFT DETECTED - tests 123/129 passed, 6 failed; 70 added, 6 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-10-22 19:50:06 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

> Tenants Production_Tenant, Production_Tenant2, Production_Tenant22, tn_TEST1 already existed on the shared sandbox when the baseline data was pulled (22 Oct 2026 ~10:15 AEDT) but were deliberately left out of scope; they are reported as added since baseline.

## nac-test

- Tests: **129** total, **123** passed, **6** failed, 0 skipped (nac-test exit code 6)

| Suite | Test | Kind | Reason |
|---|---|---|---|
| TEST-ABC1 | Verify Tenant TEST-ABC1 | missing | Object uni/tn-TEST-ABC1 not found on APIC |
| TEST-ABC1 | Verify VRF TEST-ABC1/VRF-INT-TESTABC1 | missing | Object uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1 not found on APIC |
| TEST-ABC1 | Verify BD TEST-ABC1/BD-INT-TESTABC1 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1 not found on APIC |
| TEST-ABC1 | Verify Subnet TEST-ABC1/BD-INT-TESTABC1/10.10.10.1/24 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.10.1/24] not found on APIC |
| TEST-ABC1 | Verify Subnet TEST-ABC1/BD-INT-TESTABC1/10.10.20.1/24 | missing | Object uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.20.1/24] not found on APIC |
| TEST-ABC1 | Verify BD TEST-ABC1/BD-L2-TESTABC1 | missing | Object uni/tn-TEST-ABC1/BD-BD-L2-TESTABC1 not found on APIC |

## Object counts (REST pull vs baseline)

| Type | Baseline | Current (APIC, all tenants) | Added | Removed |
|---|---:|---:|---:|---:|
| Tenant | 16 | 28 | 13 | 1 |
| VRF | 18 | 28 | 11 | 1 |
| BD | 23 | 34 | 13 | 2 |
| Subnet (BD) | 23 | 29 | 8 | 2 |
| AP | 16 | 27 | 11 | 0 |
| EPG | 33 | 47 | 14 | 0 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (70)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2` |
| Tenant | Cursor_tenant1 | `uni/tn-Cursor_tenant1` |
| Tenant | DEMO1 | `uni/tn-DEMO1` |
| Tenant | KoolKid_Tenant | `uni/tn-KoolKid_Tenant` |
| Tenant | NE-LAB-1021 | `uni/tn-NE-LAB-1021` |
| Tenant | Production_Tenant | `uni/tn-Production_Tenant` |
| Tenant | Production_Tenant2 | `uni/tn-Production_Tenant2` |
| Tenant | Production_Tenant22 | `uni/tn-Production_Tenant22` |
| Tenant | Shaver_API | `uni/tn-Shaver_API` |
| Tenant | WebServer-Demo | `uni/tn-WebServer-Demo` |
| Tenant | Yellow_Tenant | `uni/tn-Yellow_Tenant` |
| Tenant | lab-t01 | `uni/tn-lab-t01` |
| Tenant | tn_TEST1 | `uni/tn-tn_TEST1` |
| VRF | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ctx-cursor2_vrf` |
| VRF | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ctx-cursor_vrf` |
| VRF | KoolKid_Tenant | `uni/tn-KoolKid_Tenant/ctx-Context` |
| VRF | NE-LAB-1021 | `uni/tn-NE-LAB-1021/ctx-NE-VRF` |
| VRF | Production_Tenant | `uni/tn-Production_Tenant/ctx-Prod_VRF` |
| VRF | Production_Tenant2 | `uni/tn-Production_Tenant2/ctx-Prod_VRF2` |
| VRF | Production_Tenant22 | `uni/tn-Production_Tenant22/ctx-Prod_VRF22` |
| VRF | WebServer-Demo | `uni/tn-WebServer-Demo/ctx-demo_vrf` |
| VRF | Yellow_Tenant | `uni/tn-Yellow_Tenant/ctx-Context` |
| VRF | lab-t01 | `uni/tn-lab-t01/ctx-vrf-a` |
| VRF | lab-t01 | `uni/tn-lab-t01/ctx-vrf-b` |
| BD | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd` |
| BD | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd` |
| BD | KoolKid_Tenant | `uni/tn-KoolKid_Tenant/BD-BridgeDomain` |
| BD | NE-LAB-1021 | `uni/tn-NE-LAB-1021/BD-NE-BD` |
| BD | Production_Tenant | `uni/tn-Production_Tenant/BD-Prod_BD_100` |
| BD | Production_Tenant2 | `uni/tn-Production_Tenant2/BD-Prod_BD_200` |
| BD | Production_Tenant22 | `uni/tn-Production_Tenant22/BD-Prod_BD_300` |
| BD | WebServer-Demo | `uni/tn-WebServer-Demo/BD-demo_bd` |
| BD | Yellow_Tenant | `uni/tn-Yellow_Tenant/BD-BridgeDomain` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-b` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-db` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-shared` |
| BD | lab-t01 | `uni/tn-lab-t01/BD-bd-web` |
| Subnet (BD) | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/BD-cursor2_bd/subnet-[10.250.3.1/24]` |
| Subnet (BD) | Cursor_tenant1 | `uni/tn-Cursor_tenant1/BD-cursor_bd/subnet-[10.250.2.1/24]` |
| Subnet (BD) | NE-LAB-1021 | `uni/tn-NE-LAB-1021/BD-NE-BD/subnet-[192.168.100.1/24]` |
| Subnet (BD) | WebServer-Demo | `uni/tn-WebServer-Demo/BD-demo_bd/subnet-[10.250.1.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-b/subnet-[10.20.1.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-db/subnet-[10.10.2.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-shared/subnet-[10.30.1.1/24]` |
| Subnet (BD) | lab-t01 | `uni/tn-lab-t01/BD-bd-web/subnet-[10.10.1.1/24]` |
| AP | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap` |
| AP | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap` |
| AP | DEMO1 | `uni/tn-DEMO1/ap-AP-DEMO1` |
| AP | KoolKid_Tenant | `uni/tn-KoolKid_Tenant/ap-EPG` |
| AP | NE-LAB-1021 | `uni/tn-NE-LAB-1021/ap-NE-APP` |
| AP | Production_Tenant | `uni/tn-Production_Tenant/ap-Prod_App_Profile` |
| AP | Production_Tenant2 | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2` |
| AP | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22` |
| AP | WebServer-Demo | `uni/tn-WebServer-Demo/ap-demo_ap` |
| AP | Yellow_Tenant | `uni/tn-Yellow_Tenant/ap-Yellow_AppProfile` |
| AP | lab-t01 | `uni/tn-lab-t01/ap-ap-01` |
| EPG | Cursor_Tenant2 | `uni/tn-Cursor_Tenant2/ap-cursor2_ap/epg-web` |
| EPG | Cursor_tenant1 | `uni/tn-Cursor_tenant1/ap-cursor_ap/epg-web` |
| EPG | KoolKid_Tenant | `uni/tn-KoolKid_Tenant/ap-EPG/epg-KoolKid_EPG` |
| EPG | NE-LAB-1021 | `uni/tn-NE-LAB-1021/ap-NE-APP/epg-NE-WEB` |
| EPG | Production_Tenant | `uni/tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG` |
| EPG | Production_Tenant2 | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2/epg-Web_EPG2` |
| EPG | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG22` |
| EPG | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG222` |
| EPG | WebServer-Demo | `uni/tn-WebServer-Demo/ap-demo_ap/epg-web` |
| EPG | Yellow_Tenant | `uni/tn-Yellow_Tenant/ap-Yellow_AppProfile/epg-Yellow_EPG` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-b` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-db` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-shared` |
| EPG | lab-t01 | `uni/tn-lab-t01/ap-ap-01/epg-epg-web` |

## Removed since baseline (6)

| Type | Tenant | DN |
|---|---|---|
| Tenant | TEST-ABC1 | `uni/tn-TEST-ABC1` |
| VRF | TEST-ABC1 | `uni/tn-TEST-ABC1/ctx-VRF-INT-TESTABC1` |
| BD | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1` |
| BD | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-L2-TESTABC1` |
| Subnet (BD) | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.10.1/24]` |
| Subnet (BD) | TEST-ABC1 | `uni/tn-TEST-ABC1/BD-BD-INT-TESTABC1/subnet-[10.10.20.1/24]` |

## APIC faults (faultInst, context only)

| critical | major | minor | warning | info | cleared | total |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 23 | 74 | 694 | 0 | 7 | 809 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
