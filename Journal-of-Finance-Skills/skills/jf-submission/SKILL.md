---
name: jf-submission
description: Use when running the final pre-submission preflight for The Journal of Finance (JF) — Manuscript Central / ScholarOne portal, submission fee and AFA membership, formatting, anonymity, Internet Appendix, and disclosure statements.
---

# Pre-Submission Preflight (jf-submission)

## When to trigger

- "We're submitting tomorrow" — the last check before the submit button
- Unsure which files and statements the portal expects
- Unsure about the submission fee / AFA-membership norms

> ACCURACY NOTE: fees, membership rules, formatting limits, and editor lists change. The items below are **durable norms**. Verify the current specifics on the official JF / AFA author pages before submitting.

## Submission logistics (verify current details)

- JF submissions go through **Manuscript Central / ScholarOne** (the AFA's electronic system).
- JF normally charges a **submission fee**, often reduced or waived for **AFA members** — confirm the current amount and any membership requirement on the official page.
- The handling structure is an **Editor plus Associate Editors**; expect a demanding, multi-round review. Do not name or assume specific current editors — check the masthead.
- Decisions and reviews are returned through the portal; turnaround can be long.

## Formatting (confirm against current author guidelines)

- [ ] Manuscript double-spaced, generous margins, numbered pages
- [ ] Title page with abstract and JEL codes; keywords as requested
- [ ] References in the journal's style; every in-text citation appears in the list and vice versa
- [ ] Tables and figures numbered with the journal's running scheme; each self-contained
- [ ] Standard-error/clustering conventions stated in every table note
- [ ] File formats and size limits per the portal's current requirements

## Internet Appendix

- [ ] Internet Appendix prepared as a separate file (proofs, secondary tables, extra robustness)
- [ ] Every Internet Appendix item is referenced from the main text
- [ ] Appendix uses IA numbering consistent with the main text

## Anonymity / blinding (if the current process requires it)

- [ ] Author-identifying content removed from the manuscript body
- [ ] Self-citations phrased neutrally ("a prior study (Author, 2022)") not "our earlier work"
- [ ] Acknowledgments / grant info kept off the blinded manuscript
- [ ] File metadata scrubbed of author names

## Disclosures & statements

- [ ] Conflict-of-interest / disclosure statement prepared (AFA/JF expects disclosure of relevant financial interests)
- [ ] Data-availability / replication statement prepared; replication package ready to share on acceptance
- [ ] Funding and acknowledgments drafted (added to the non-blinded version)
- [ ] Suggested / opposed reviewers prepared if the portal asks (see `jf-referee-strategy`)

## Anti-patterns

- Submitting without checking the **current** fee / membership rule and getting bounced
- An Internet Appendix with tables the main text never cites
- Leaving author identity in metadata or self-citations after blinding
- Missing the disclosure statement (a known JF/AFA requirement)
- References in a generic reference-manager default rather than the journal's style
- Forgetting that the replication package will be required and not having it ready

## Output format

```
【Portal】Manuscript Central / ScholarOne — account ready: yes/no
【Fee / membership verified on official page?】yes / no
【Formatting per current guidelines?】yes / no
【Internet Appendix attached + all items cited?】yes / no
【Anonymity (if required) clean?】yes / no
【Disclosure + data-availability statements ready?】yes / no
【Next step】jf-referee-strategy → (after decision) jf-rebuttal
```

## Related resources

- [`templates/manuscript_template.md`](templates/manuscript_template.md) — JF-oriented manuscript skeleton (title page, abstract, body, Internet Appendix pointers, references)
- [`templates/checklist.md`](templates/checklist.md) — Eight-section pre-submission self-check
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Finance data sources (CRSP / Compustat / TAQ / WRDS / Refinitiv) and Stata / R / Python packages
