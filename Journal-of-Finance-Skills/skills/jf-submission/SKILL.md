---
name: jf-submission
description: Use when running the final pre-submission preflight for The Journal of Finance (JF) — the AFA online portal, the tiered submission fee, the 60-page limit, the bundled Internet Appendix, code sharing, and disclosure statements.
---

# Pre-Submission Preflight (jf-submission)

## When to trigger

- "We're submitting tomorrow" — the last check before the submit button
- Unsure which files and statements the AFA portal expects
- Unsure about the submission fee tier or whether a cover letter is needed

> ACCURACY NOTE: fees, limits, and editor lists change. Verify current specifics on afajof.org/submissions before submitting. Fee tiers, format rules, the disclosure-statement and AI policies, and the editor masthead were **re-verified 2026-11-23** against the live AFA pages (amounts unchanged; current Co-Editors confirmed below); the JF Submission Guidelines PDF is Rev. March 12, 2024.

## Submission logistics (JF-specific)

- JF submissions go through the **AFA's online submission system** — **Editorial Express**, reached from the "Submit a Paper" link on afajof.org/submissions; the fee is paid by credit card (Visa / MasterCard / Amex) as part of the submission.
- Refereeing is **single-blind**: the title page carries the title, **all author names**, and an **abstract of no more than 100 words**.
- **Tiered submission fee by author economy and AFA membership** (high-income: **AFA member $400, non-member $525**; middle-income: **$100 / $150**; low-income: **no fee**). All authors must reside in a low/middle-income country to qualify for the reduced/zero tier.
- **Refund policy**: a flat **$200** is returned on a desk rejection (high-income; not for resubmissions of previously rejected papers); the **entire fee is refunded if the first decision takes more than 100 days**. Applies to the first submission only.
- **Editor: Antoinette Schoar (MIT)**, with Co-Editors **Kogan, Lewellen, Philippon, and Sunderam** (Adi Sunderam replaced Urban Jermann on 1 July 2025) and 50+ Associate Editors, plus a **Data Editor (Hong Ru)** — masthead confirmed on afajof.org/editorial-board 2026-11-23; re-verify before submission.

## Cover letter (JF norm — usually skip it)

- JF explicitly states **a cover letter is usually NOT necessary**. Include one **only** for specific information: a **request for exemption from the code-sharing policy**, or a conflict of interest among editors/AEs/referees. If you have nothing specific, do not attach one.

## Formatting (confirm against current guidelines)

- [ ] Manuscript **no more than 60 pages** — the limit **includes internal appendices, references, figures, and tables** (over-length papers are desk-rejected automatically) — **at least 1.5 line spacing**, **12-point font**, 1-inch side and 1.5-inch top/bottom margins, PDF
- [ ] Title page with author names and an **abstract of no more than 100 words**; JEL codes and keywords as requested
- [ ] References in the journal's style; every in-text citation appears in the list and vice versa
- [ ] Tables/figures numbered with the journal's running scheme; each self-contained
- [ ] Standard-error/clustering conventions stated in every table note

## Internet Appendix (JF-specific placement)

- [ ] Internet Appendix placed **at the END of the same PDF** (not a separate upload), with **"Internet Appendix"** on its first page
- [ ] It **does not count toward the 60-page limit**
- [ ] Every IA item is referenced from the main text; main text is self-contained

## Code, disclosures & statements

- [ ] **Disclosure statement** — a separate disclosure for **each author by name**, on the page **right after the title page** (same PDF, not a separate file; it does not count toward the 60 pages). Submissions without it are returned immediately; resubmissions need one too
- [ ] AI use: tools may help draft/edit text or code, but authors stay accountable and AI is never a co-author; a brief description of tool use may be given at submission. New datasets/analyses built with AI must use open-source or clearly time-stamped proprietary models with detailed prompt documentation
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

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue jf-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

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
