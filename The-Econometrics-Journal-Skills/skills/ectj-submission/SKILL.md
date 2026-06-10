---
name: ectj-submission
description: Use when running the final The Econometrics Journal pre-submission check for Editorial Express, RES/OUP template compliance, 20-page printed-paper norm, 150-word summary, empirical application, proofs placement, submission fee, cover letter, and replication-policy disclosure.
---

# EctJ Submission

Use this immediately before submission through Editorial Express.

## Preflight

- Confirm the manuscript uses the required RES/EctJ LaTeX template and the correct online
  appendix template if applicable.
- Check the current page norm. RES guidance says the paper should not normally exceed 20
  pages including the printed appendix.
- Keep the summary within the current limit; RES guidance says no more than 150 words.
- Include an empirical application, even for theory papers.
- Keep mathematical proofs in the main text or printed appendix when current RES guidance
  requires that; do not rely on the online appendix for proofs.
- Prepare a cover letter only for conflicts, exemptions, or prior reports when current
  guidance says that is the intended use.
- Budget the current submission fee. The source map records a flat fee of GBP 75 plus VAT
  under the 2026 RES policy, with no RES-member discount.
- Disclose replication restrictions or exemption needs at first submission.

## Final hour order

Run the preflight in this order:

1. **Venue facts**: reopen `resources/official-source-map.md` and verify portal, fee, page, summary, proof,
   and replication requirements against live pages.
2. **Conformance**: compile the template PDF, count printed pages, count summary words, and verify proof
   placement.
3. **Scientific gate**: read the first two pages only. They must state the leading case, applied value, and
   closest incumbent method without relying on later sections.
4. **Package gate**: confirm the replication README and master command exist even if the final package is
   delivered after conditional acceptance.
5. **Administrative gate**: fee path, cover-letter reason, data restrictions, and author metadata.

## Worked preflight: a specification-test vignette

Illustrative run of the final-hour order on a hypothetical kernel specification-test paper:

1. Venue facts reopened: fee, page norm, summary limit, and proof placement reverified on live
   RES pages; one wording change found and noted in the source map.
2. Conformance: template compile gives 22 printed pages against the 20-page norm. The fix is
   moving the secondary power grid to the online appendix and merging two bandwidth tables, not
   shrinking margins; margin tricks are exactly what conformance screens catch.
3. Summary count: 164 words. Cut the sentence restating the literature; the summary needs only the
   econometric object, the leading-case result, and the applied payoff.
4. Scientific gate: the first two pages name the incumbent test, its size distortion under
   heteroskedasticity (illustrative: 11% rejection at nominal 5%), and the application.
5. Package gate: the master script reruns the smoke simulation in about nine minutes; the README
   states that runtime.

Result after fixes: 19.5 pages, a 148-word summary, proofs in the printed appendix — submit.

## Editorial Express slip list

- Metadata fields (JEL codes, keywords) inconsistent with the PDF front page.
- PDF compiled outside the RES/EctJ template, or the online appendix mixed into the main file
  instead of the separate appendix template.
- Fee handled on an outdated amount; reconfirm the current figure and VAT treatment against the
  journal's current author guidelines on submission day.
- Cover letter used for marketing; at this venue it exists for conflicts, exemption requests, and
  prior reports only.
- Replication exemption needs known to the authors but not disclosed at first submission, which
  the RES policy expects.

## Fee and disclosure notes

- The recorded RES policy is a flat fee per new submission with no RES-member discount, and it is
  non-refundable even on desk rejection except for genuine payment errors — budget it as a sunk
  screening cost.
- Whether a resubmission after reject-and-resubmit incurs a fresh fee depends on current policy
  wording; confirm on the live fee-policy page before assuming either answer.
- Disclosing restricted data at first submission is an RES expectation, because the editorial
  board decides whether the paper can be considered at all under the replication policy.

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Format checks] <template/page/summary/proofs/appendix>
[Content checks] <leading case/empirical application/simulations>
[Administrative checks] <Editorial Express/fee/cover letter/replication disclosure>
[Blocking fix] <one issue to resolve first>
```
