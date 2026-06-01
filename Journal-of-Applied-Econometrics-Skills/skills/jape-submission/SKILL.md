---
name: jape-submission
description: Use when running the final pre-submission preflight for the Journal of Applied Econometrics (JAE) via Editorial Express — Free Format PDF submission, the 100-word citation-free summary, the 35-page limit, any-consistent-style references, the no-submission-fee policy, the optional open-access charge, and the three-papers-under-review cap. Final checks; it does not draft content.
---

# Submission Preflight for JAE (jape-submission)

## When to trigger

- About to press submit on Editorial Express for a JAE paper
- Confirming which files and limits JAE expects at first submission
- Checking the fee/open-access situation and the per-author cap

## Process facts (re-confirm volatile items on the official page)

- Published by **John Wiley & Sons**; submitted via **Editorial Express** at `editorialexpress.com/jae`; manuscripts handled in **PDF**.
- **Free Format** first submission: strict formatting is **not** required initially, and references may be in **any consistent style**.
- **No submission fee.** Hybrid open access is **optional** and triggers an Article Publication Charge **only if you choose OA on acceptance** (a Wiley APC; the exact ~USD 4,230 / GBP 2,800 / EUR 3,570 figure is **待核实** — the live funded-access page was bot-blocked). Non-OA publication is free.
- **Cover letter optional.** Categories: Research Articles and the dedicated **Replication Articles** track.
- **Cap:** no more than **three papers** from the same author under review at once.

## Preflight checklist

- [ ] Single **PDF** uploaded to Editorial Express
- [ ] Main article within **35 pages**; extended material in the **online appendix** (no cap)
- [ ] **Summary ≤ 100 words**, self-contained, **no citations**; **≤ six keywords**; title without abbreviations
- [ ] References in **one consistent style** (Free Format)
- [ ] **Conflict-of-interest statement** present; acknowledgments do **not** thank reviewers
- [ ] No more than **three** of your papers under review at once
- [ ] Data exportable to plain **ASCII/CSV** + readme; programs staged for the **JAE Data Archive**

## Output format

```
【PDF】single PDF via Editorial Express? [Y/N]
【Limits】≤35pp; summary ≤100w no-cites; ≤6 keywords? [Y/N]
【Refs】one consistent style (Free Format)? [Y/N]
【Fee】no fee; OA optional (APC 待核实)? [Y/N]
【Pipeline】≤3 papers under review? [Y/N]
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Editorial Express, Free Format, limits, fee/OA sources
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — staging the replication package
