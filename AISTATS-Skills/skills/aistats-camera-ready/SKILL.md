---
name: aistats-camera-ready
description: Use when preparing accepted AISTATS papers for PMLR camera-ready submission, covering the 9-page final body, two-column layout reflow, author de-anonymization, proceedings forms, metadata, final appendix handling, registration, in-person presentation obligations, and public artifact release.
---

# AISTATS Camera Ready

Use this after acceptance. Reopen the current AISTATS camera-ready instructions, PMLR author
kit, registration page, presentation policy, and OpenReview decision email before advising
authors.

## Camera-ready audit

- Convert the anonymous submission to the public proceedings version: names, affiliations,
  acknowledgements, funding, code/data links, and author metadata.
- Apply the current final-page limit. AISTATS 2026 allowed a 9-page camera-ready body,
  excluding references and supplementary material.
- Check PMLR formatting, title/abstract metadata, author order, bibliography, appendix
  placement, and any required release or copyright forms.
- Resolve reviewer and meta-review concerns without changing the accepted contribution beyond
  normal camera-ready clarification.
- Prepare public artifacts: repository, data, model checkpoints, environment files, and
  archival links after anonymity no longer matters.
- Confirm registration and presentation obligations. AISTATS 2026 required in-person
  attendance by at least one author for each accepted paper, with no remote presentation.

## PMLR two-column reflow

- AISTATS proceedings use a two-column PMLR layout; switching the style file from anonymous
  to accepted mode changes spacing, so recheck every page break, figure placement, and table
  width after the flip.
- Wide theorem environments, long display equations, and multi-panel rate plots often need
  full-width spans; verify nothing is clipped at column boundaries.
- Material that fit the submission body can overflow once the author block, acknowledgements,
  and funding lines are added; the extra camera-ready page usually absorbs this, but confirm
  rather than assume.
- Keep theorem, assumption, and equation numbering identical to the reviewed version so the
  meta-review and discussion record remain traceable to the final text.

## De-anonymization sweep

- Restore the author block, acknowledgements, grants, and any contribution statements the
  anonymous version stripped.
- Rewrite self-citations into natural first-person form where it improves clarity.
- Replace anonymized repository placeholders with the public, licensed, citable archive and
  test every link from a logged-out browser.

## Worked example: integrating a reviewer fix

The meta-review asked that a bounded-noise assumption move from the appendix into the main
text. Camera-ready move: add the assumption to the theorem statement, one justification
sentence, and a pointer to the appendix discussion — without strengthening the result into
something the reviewers never evaluated.

## Hedged logistics

- Registration pricing, copyright-form mechanics, and exact camera-ready dates change every
  cycle; confirm against the decision email and the current proceedings instructions.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/source/bib/metadata/PMLR forms/artifacts>
[Policy checks] <page/authors/presentation/registration/artifact release>
[Reviewer-change map] <concern -> final edit>
[Remaining owner] <person -> task>
```
