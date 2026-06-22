---
name: jf-submission
description: Use when running the final pre-submission preflight for The Journal of Finance (JF) — the AFA online portal, the tiered submission fee, the 60-page limit, the bundled Internet Appendix, code sharing, and disclosure statements.
---

# Pre-Submission Preflight (jf-submission)

## When to trigger

- "We're submitting tomorrow" — the last check before the submit button
- Unsure which files and statements the AFA portal expects
- Unsure about the submission fee tier or whether a cover letter is needed

> ACCURACY NOTE: fees, limits, and editor lists change. Verify current specifics on afajof.org/submissions before submitting. Fee tiers and the editor masthead were **re-verified 2026-06-22** against the live AFA pages (amounts unchanged; current Co-Editors confirmed below); the JF Submission Guidelines PDF is Rev. March 12, 2024.

## Submission logistics (JF-specific)

- JF submissions go through the **AFA's online submission system** (afajof.org/submissions); the fee is paid by credit card (Visa / MasterCard / Amex) as part of the submission.
- **Tiered submission fee by author economy and AFA membership** (high-income: **AFA member $400, non-member $525**; middle-income: **$100 / $150**; low-income: **no fee**). All authors must reside in a low/middle-income country to qualify for the reduced/zero tier.
- **Refund policy**: a flat **$200** is returned on a desk rejection (high-income; not for resubmissions of previously rejected papers); the **entire fee is refunded if the first decision takes more than 100 days**. Applies to the first submission only.
- **Editor: Antoinette Schoar (MIT)**, with Co-Editors **Kogan, Lewellen, Philippon, and Sunderam** (Adi Sunderam replaced Urban Jermann on 1 July 2025) and 50+ Associate Editors, plus a **Data Editor (Hong Ru)** — masthead confirmed on afajof.org/editorial-board 2026-06-22; re-verify before submission.

## Cover letter (JF norm — usually skip it)

- JF explicitly states **a cover letter is usually NOT necessary**. Include one **only** for specific information: a **request for exemption from the code-sharing policy**, or a conflict of interest among editors/AEs/referees. If you have nothing specific, do not attach one.

## Formatting (confirm against current guidelines)

- [ ] Manuscript **no more than 60 pages**, **at least 1.5 line spacing**, **12-point font**
- [ ] Title page with abstract and JEL codes; keywords as requested
- [ ] References in the journal's style; every in-text citation appears in the list and vice versa
- [ ] Tables/figures numbered with the journal's running scheme; each self-contained
- [ ] Standard-error/clustering conventions stated in every table note

## Internet Appendix (JF-specific placement)

- [ ] Internet Appendix placed **at the END of the same PDF** (not a separate upload), with **"Internet Appendix"** on its first page
- [ ] It **does not count toward the 60-page limit**
- [ ] Every IA item is referenced from the main text; main text is self-contained

## Code, disclosures & statements

- [ ] Disclosure statement prepared (AFA disclosure policy: relevant financial interests)
- [ ] **Replication code** ready — the **Data and Code Sharing Policy (in force since Sept 2016; current rev. 1 April 2024)** requires code with the final accepted version, published in Supplementary Information and checked by the Data Editor
- [ ] Funding/acknowledgments drafted; suggested/opposed reviewers if asked (see `jf-referee-strategy`)

## Worked vignette — the night-before preflight

*Illustrative.* A team submits tomorrow and the preflight surfaces three issues. The body is 63 pages — over the limit — so two robustness tables move to the Internet Appendix, bringing it to 57 pp. All authors reside in a high-income country and one is an AFA member, so the fee is the high-income member tier (confirm the figure on the AFA page). They drafted a generic cover letter — which JF says to skip; they delete it, having nothing specific to flag. With the IA bundled and code staged for the Data Editor, the submission is clean.

### Desk-reject-adjacent preflight traps
| Trap caught at preflight                            | The fix before submitting                                      |
|-----------------------------------------------------|-----------------------------------------------------------------|
| Body over 60 pp                                     | Move non-decisive exhibits to the Internet Appendix             |
| IA uploaded as a separate file                      | Re-bundle in the same PDF, titled "Internet Appendix"           |
| Stale fee tier quoted                               | Re-check the current tier on the AFA submission page            |

## Anti-patterns

- Attaching a cover letter with no specific purpose (JF says skip it)
- Submitting a paper over 60 pages and counting the Internet Appendix against the limit
- Uploading the Internet Appendix as a separate file instead of bundling it in the same PDF
- Treating code sharing as optional — JF's Data Editor verifies it at acceptance
- Quoting an old fee tier without checking afajof.org/submissions

## Output format

```
【Portal】AFA online submission system — account ready: yes/no
【Fee tier (member/economy) confirmed?】yes / no — $amount
【≤60 pp, 1.5 spacing, 12pt?】yes / no
【Internet Appendix bundled in same PDF + all items cited?】yes / no
【Cover letter only if needed (exemption/COI)?】yes / no
【Disclosure + replication code ready?】yes / no
【Next step】jf-referee-strategy → (after decision) jf-rebuttal
```

## Related resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JF-oriented manuscript skeleton (title page, abstract, body, Internet Appendix pointers, references)
- [`templates/checklist.md`](templates/checklist.md) — Eight-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Finance data sources (CRSP / Compustat / TAQ / WRDS / Refinitiv) and Stata / R / Python packages
