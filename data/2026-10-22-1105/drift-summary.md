# ACI drift report: 2026-10-22

## DRIFT DETECTED - tests 129/129 passed, 0 failed; 21 added, 0 removed

- APIC: https://sandboxapicdc.cisco.com
- Generated: 2026-10-22 11:05:38 AEDT (Australia/Melbourne)
- Baseline: `baseline/data/` (frozen 2026-10-22 10:47 AEDT (Australia/Melbourne) by `scripts/drift_report.sh`)
- Status: `drift`

> Tenants Production_Tenant, Production_Tenant2, Production_Tenant22, tn_TEST1 already existed on the shared sandbox when the baseline data was pulled (22 Oct 2026 ~10:15 AEDT) but were deliberately left out of scope; they are reported as added since baseline.

## nac-test

- Tests: **129** total, **129** passed, **0** failed, 0 skipped (nac-test exit code 0)

No failed tests.

## Object counts (REST pull vs baseline)

| Type | Baseline | Current (APIC, all tenants) | Added | Removed |
|---|---:|---:|---:|---:|
| Tenant | 16 | 22 | 6 | 0 |
| VRF | 18 | 22 | 4 | 0 |
| BD | 23 | 27 | 4 | 0 |
| Subnet (BD) | 23 | 23 | 0 | 0 |
| AP | 16 | 19 | 3 | 0 |
| EPG | 33 | 37 | 4 | 0 |

Subnets are bridge-domain subnets only (EPG-level subnets are not in the baseline model).

## Added since baseline (21)

| Type | Tenant | DN |
|---|---|---|
| Tenant | Production_Tenant | `uni/tn-Production_Tenant` |
| Tenant | Production_Tenant2 | `uni/tn-Production_Tenant2` |
| Tenant | Production_Tenant22 | `uni/tn-Production_Tenant22` |
| Tenant | js_10018 | `uni/tn-js_10018` |
| Tenant | js_10118 | `uni/tn-js_10118` |
| Tenant | tn_TEST1 | `uni/tn-tn_TEST1` |
| VRF | Production_Tenant | `uni/tn-Production_Tenant/ctx-Prod_VRF` |
| VRF | Production_Tenant2 | `uni/tn-Production_Tenant2/ctx-Prod_VRF2` |
| VRF | Production_Tenant22 | `uni/tn-Production_Tenant22/ctx-Prod_VRF22` |
| VRF | js_10118 | `uni/tn-js_10118/ctx-prod_vrf` |
| BD | Production_Tenant | `uni/tn-Production_Tenant/BD-Prod_BD_100` |
| BD | Production_Tenant2 | `uni/tn-Production_Tenant2/BD-Prod_BD_200` |
| BD | Production_Tenant22 | `uni/tn-Production_Tenant22/BD-Prod_BD_300` |
| BD | js_10118 | `uni/tn-js_10118/BD-prod_bd` |
| AP | Production_Tenant | `uni/tn-Production_Tenant/ap-Prod_App_Profile` |
| AP | Production_Tenant2 | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2` |
| AP | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22` |
| EPG | Production_Tenant | `uni/tn-Production_Tenant/ap-Prod_App_Profile/epg-Web_EPG` |
| EPG | Production_Tenant2 | `uni/tn-Production_Tenant2/ap-Prod_App_Profile2/epg-Web_EPG2` |
| EPG | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG22` |
| EPG | Production_Tenant22 | `uni/tn-Production_Tenant22/ap-Prod_App_Profile22/epg-Web_EPG222` |

## Removed since baseline (0)

None.

## APIC faults (faultInst, context only)

| critical | major | minor | warning | info | cleared | total |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 17 | 74 | 692 | 0 | 15 | 808 |

## Artifacts

`report.html`, `log.html`, `output.xml`, `xunit.xml`, `drift-summary.{md,html,json}`, `live-snapshot.json`
