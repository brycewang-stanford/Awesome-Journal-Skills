---
name: aamas-camera-ready
description: Use when preparing an accepted AAMAS paper for the IFAAMAS open-access camera-ready, covering author de-anonymization, proceedings metadata, two-column reflow of game figures and learning curves, resolving rebuttal-stage promises, registration, in-person presentation, and the public code and environment release for a multiagent paper.
---

# AAMAS Camera Ready

Use this after acceptance. Reopen the current AAMAS camera-ready instructions, the proceedings
author kit, the registration page, and the decision notice before advising authors; AAMAS
proceedings are published open-access by IFAAMAS.

## Camera-ready audit

- Convert the anonymous submission to the public version: author names, affiliations,
  acknowledgements, funding, and de-anonymized code, data, and environment links.
- Apply the current final-page rules and template. Confirm whether the accepted-paper mode
  changes the page budget from the 8-page submission body, and reflow accordingly.
- Check proceedings metadata: title, abstract, author order and ORCID, subject areas,
  bibliography, and any required copyright or release form.
- Integrate every rebuttal-stage promise without expanding the accepted contribution: a
  wording fix, a moved assumption, or an added caption line - not a new experiment.
- Prepare the public artifact: repository, multiagent environments, opponent/population sets,
  seeds, checkpoints, and an archival citation, now that anonymity no longer applies.
- Confirm registration and in-person presentation obligations for at least one author.

## Anonymous-to-final flip: what to recheck

| Element | Submission (anonymous) | Camera-ready (final) |
|---|---|---|
| Page one | Tracking number, no author block | Author names, affiliations, ORCID |
| Acknowledgements / funding | Removed | Restored |
| Code / environment links | Anonymized placeholder | Public, licensed, citable archive |
| Self-citation phrasing | "prior work [anon]" | Natural first-person, de-anonymized |
| Page budget | 8-page body | Confirm the accepted-paper budget, then reflow |

## Two-column reflow for multiagent papers

- Switching the style file from anonymous to final mode changes spacing; recheck every page
  break, figure placement, and table width after the flip.
- Extensive-form game trees, payoff matrices, and multi-panel learning curves often need
  full-width spans; verify nothing is clipped at the column boundary.
- Material that fit under the tracking number can overflow once the author block and
  acknowledgements are added; confirm rather than assume the budget absorbs it.
- Keep theorem, assumption, and game-definition numbering identical to the reviewed version so
  the public reviews on OpenReview remain traceable to the final text.

## De-anonymization sweep

- Restore the author block, acknowledgements, grants, and contribution statements the
  anonymous version stripped.
- Rewrite anonymized self-citations ("prior work [anon]") into natural first-person form.
- Replace anonymized repository placeholders with the public, licensed, citable archive, and
  test every link and every environment install from a logged-out machine.

## Worked example: honoring a rebuttal promise

The area chair accepted on the condition that the paper add a held-out opponent to the
evaluation, which the rebuttal promised. Camera-ready move: add the one opponent, report it
with the same seeds and standard errors as the others, and add a sentence to the protocol -
without re-tuning the method or re-framing the contribution the reviewers evaluated.

## Hedged logistics

- Registration pricing, copyright-form mechanics, the exact camera-ready date, and the
  proceedings template can change every cycle; confirm against the decision notice and current
  author kit.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/source/bib/metadata/forms/artifacts>
[Policy checks] <page/authors/presentation/registration/artifact release>
[Rebuttal-promise map] <promise -> final edit>
[Remaining owner] <person -> task>
```
