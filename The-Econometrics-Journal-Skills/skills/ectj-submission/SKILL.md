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

## Output format

```text
[Submission readiness] Ready / Needs fixes / Not ready
[Format checks] <template/page/summary/proofs/appendix>
[Content checks] <leading case/empirical application/simulations>
[Administrative checks] <Editorial Express/fee/cover letter/replication disclosure>
[Blocking fix] <one issue to resolve first>
```
