---
name: jeea-submission
description: Use when running the final pre-submission preflight for the Journal of the European Economic Association (JEEA) via the EEA submission system — EEA membership gate, submission fee, single-blind format, online appendix, the no-asterisks house style, and the data-policy declarations. Final checks; it does not draft content.
---

# Submission Preflight (jeea-submission)

## When to trigger

- "Submitting tomorrow" — last check before pressing submit on the EEA / JEEA portal
- Unsure which files, fees, and declarations the submission expects
- Confirming the format and house style are JEEA-compliant
- Checking the membership gate and fee before you reach the payment step

## Process facts (source map refreshed 2026-06-20)

- JEEA is the **EEA's general-interest journal**, published by **Oxford University Press** (Online ISSN 1542-4774; Print ISSN 1542-4766). Submission starts through the **EEA member area**; after payment, a "Submit a paper to JEEA" link appears.
- **Membership gate:** the **submitting author must be a current EEA member** to submit *and* to resubmit a revised paper (join/renew via the EEA site).
- **Submission fee:** a **standard submission fee of €100 is in force (introduced Feb 1, 2026; re-verified 2026-06-22)**, paid through the EEA membership profile at submission; **waived if the submitting author and all coauthors are based in low- and middle-income countries** (World Bank classification); non-refundable. Re-confirm the live EEA fee page before paying.
- **Single-blind review:** referees see the authors; manuscript anonymization is **not** required, but keep tone and self-citation professional.
- **Editorial flow:** a **co-editor** reads first and may **desk-reject without review**; otherwise it goes to referees, with a **fast-decision target (≈8 weeks where possible)**.
- **Data & code:** for empirical/simulation/experimental work, JEEA applies **DCAS**; the **JEEA Data Editor verifies replication before formal acceptance**, packages are posted to the **JEEA Zenodo community**, and the package ZIP is submitted through the online data submission platform at Editorial Express (prepare via `jeea-replication-package`).
- **AI / disclosure:** AI use beyond spelling and grammar checks should be explicitly disclosed and precisely described; disclosure/COI and funding statements should be prepared.

## Preflight checklist

### Format & style
- [ ] Manuscript prepared per the current JEEA author guidelines
- [ ] Abstract present and concise; title, keywords, JEL codes, and affiliations on the title page
- [ ] Alt text prepared for figures in final files; online appendix uses A, B, etc. labels where needed
- [ ] Figures and tables legible and self-contained; **no asterisks or boldface for statistical significance** — report SEs / confidence sets
- [ ] Online appendix (if any) carries auxiliary results/proofs; the main paper is self-contained
- [ ] References complete and consistent (OUP house style applied at copyediting; the submitted file need not pre-conform)

### Files & fees for the EEA portal
- [ ] Main manuscript file ready in the required format
- [ ] **EEA membership confirmed for the submitting author**; submission fee ready (€100) or LMIC exemption applies
- [ ] Online appendix / supplementary files attached if applicable
- [ ] Experimental papers: instructions / survey transcripts and pre-registration details ready

### Declarations & policy
- [ ] Data-availability statement consistent with DCAS; replication package assembled or in progress (`jeea-replication-package`)
- [ ] Disclosure / conflict-of-interest and funding statements prepared
- [ ] Confirmed the paper is not under review elsewhere; AI not listed as an author
- [ ] For restricted data: exemption / limited-access request stated **now**, at initial submission

## Sequencing the final steps

The order of the last mile matters because two of the gates are administrative, not editorial:

1. **Confirm EEA membership for the submitting author first** — without it you cannot start (or resubmit).
2. **Have the fee ready** (€100) or confirm the LMIC exemption applies to **all** coauthors.
3. **Run the content preflight** (format, no-asterisks house style, abstract, online appendix).
4. **Confirm the replication package is in progress** (`jeea-replication-package`) — it is not needed to submit, but it gates acceptance, so do not leave it to the end.
5. **Prepare declarations** (data-availability, disclosure/COI, funding) and confirm the paper is not under review elsewhere.

Do not pay the fee before the membership and content checks pass — a failed gate after payment wastes the cycle.

## Anti-patterns

- Submitting when the submitting author is not an EEA member (hard gate, also blocks resubmission)
- Asterisks / boldface for significance, or exhibits a generalist cannot read
- Treating the paper as a field submission with no general-interest hook (desk-reject bait)
- Forgetting the LMIC fee exemption applies only if **all** coauthors qualify
- Leaving the data/code package until acceptance — the Data Editor check gates acceptance
- Assuming the portal anonymizes for you — review is single-blind, but keep tone/self-citation clean

## Output format

```
【Membership + fee】submitting author is EEA member; €100 ready or LMIC exemption? [Y/N]
【Format/style】abstract + title page; no significance asterisks? [Y/N]
【Online appendix】auxiliary results only; main paper self-contained? [Y/N]
【Data policy】DCAS statement + package in progress? [Y/N]
【Declarations】disclosure / COI / funding prepared? [Y/N]
【Next step】submit via the EEA member-area flow → jeea-referee-strategy for what to expect
```

## Supplementary resources

- [`templates/checklist.md`](templates/checklist.md) — 8-section pre-submission self-check
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official EEA / OUP URLs behind every fact
