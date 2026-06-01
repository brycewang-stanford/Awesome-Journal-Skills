---
name: ectj-replication-and-data-policy
description: Use when preparing The Econometrics Journal replication files, README, software versions, data documentation, seeds, proprietary-data exemptions, and OUP Supporting Information package after conditional acceptance or before submission risk review.
---

# EctJ Replication And Data Policy

Use this before submission for planning and after conditional acceptance for packaging.
Reopen the RES replication policy before final delivery.

## Package checklist

- Prepare a README that explains file contents, execution order, software, package versions,
  expected outputs, runtime, and system requirements.
- Include data or clear access instructions with complete variable documentation. If using
  proprietary formats, provide ASCII alternatives when required.
- Include all code needed to reproduce tables, figures, simulations, appendices, and
  supplementary results; set random seeds.
- Explain usage restrictions, confidential data, or exemption requests at first submission if
  current policy requires early disclosure.
- Expect accepted packages to appear as OUP Supporting Information when permitted.
- Treat non-compliance as publication risk; the RES policy says the board may refuse
  publication for non-compliance.

## Output format

```text
[Replication status] ready / needs fixes / blocked
[Contents] <data/code/README/software/seeds>
[Restricted-data issue] <none, access path, or exemption request>
[Reproduction command] <master script or workflow>
[Publication risk] <low/medium/high and why>
```
