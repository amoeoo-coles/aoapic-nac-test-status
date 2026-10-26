# Changes since previous morning (2026-10-26-0807 -> 2026-10-27-0816)

Previous snapshot 2026-10-26 08:07:40 AEDT; current snapshot 2026-10-27 08:16:45 AEDT.

| Tests | Prev | Now | Delta |
|---|---:|---:|---:|
| integrity total | 18 | 122 | +104 |
| integrity passed | 18 | 121 | +103 |
| integrity failed | 0 | 1 | +1 |
| drift total | 129 | 129 | +0 |
| drift passed | 20 | 44 | +24 |
| drift failed | 109 | 85 | -24 |

Tenants: 5 -> 11; broken 0 -> 2
- added: DEMO, Pune-Lab, ROR, TN-DEDUP-LAB, TN-POC-LN, TN-PROD
- removed: none
- newly broken: Pune-Lab (new), TN-DEDUP-LAB (new)
- fixed: none

Broken relations: 0 -> 10
- ADDED Pune-Lab | Subject without filters | `uni/tn-Pune-Lab/brc-Pune-Ping-allow/subj-HTTPS-SERVICE` | Contract subject has no filter, so it permits nothing.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-BACKUP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-DNS-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F0758: Service graph  for tenant TN-DEDUP-LAB could not be instantiated. Info: Unable to find LDevCtx for node:); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-MGMT-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-L3OUT-WEB-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-LDAP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-MONITORING-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-SMTP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.
- ADDED TN-DEDUP-LAB | Contract service graph not instantiated | `uni/tn-TN-DEDUP-LAB/brc-C-WEB-APP-FW` | Contract redirects through service graph tn-TN-DEDUP-LAB/AbsGraph-SG-FW which cannot be deployed (4 faults, e.g. F1690: Configuration is invalid due to No device context found for LDev); traffic on this contract is dropped.

New critical faults:
- none

| Drift type | Baseline | Prev | Now | Delta | +vs baseline | -vs baseline |
|---|---:|---:|---:|---:|---:|---:|
| Tenant | 16 | 5 | 11 | +6 | 5 | 10 |
| VRF | 18 | 7 | 15 | +8 | 7 | 10 |
| BD | 23 | 5 | 19 | +14 | 12 | 16 |
| Subnet (BD) | 23 | 1 | 17 | +16 | 11 | 17 |
| AP | 16 | 3 | 10 | +7 | 5 | 11 |
| EPG | 33 | 2 | 23 | +21 | 10 | 20 |
