---
name: ijcai-camera-ready
description: Use when preparing an accepted IJCAI or IJCAI-ECAI paper for camera-ready submission, author de-anonymization, author-order checks, copyright and proceedings metadata, final formatting, source/package readiness, in-person presentation obligations, and artifact release timing.
---

# IJCAI Camera Ready

Use this after acceptance. Reopen the current camera-ready instructions, Author Kit,
registration page, copyright instructions, and presentation rules before advising authors.

## Camera-ready audit

- Replace anonymous placeholders with full authors, affiliations, acknowledgements, funding,
  and approved contribution statements if the current kit permits them.
- Confirm that accepted-paper author order may be changed only within current rules; IJCAI
  cycles commonly forbid adding or removing authors after the author-information deadline.
- Rebuild in the current IJCAI style without margin, font, spacing, or bibliography hacks.
- Ensure ethics, limitations, reproducibility, data, and artifact statements match what was
  promised at submission and in the response.
- Prepare source files, figures, bibliography, metadata, copyright forms, and any open-access
  proceedings forms required by current instructions.
- Arrange registration and in-person presentation. IJCAI-ECAI 2026 required at least one
  accepted-paper author to attend in Bremen and present unless an exception was approved.
- Release code/data only after checking anonymity no longer matters, licenses are valid, and
  promised artifacts are ready.

## Camera-ready gate checklist

IJCAI camera-ready adds obligations that submission did not: de-anonymization, copyright,
open-access proceedings metadata, registration, and in-person presentation. Clear each gate.

| Gate | Pass condition | Fail mode IJCAI enforces |
| --- | --- | --- |
| De-anonymization | Authors, affiliations, funding, acknowledgements restored | Leftover "Anonymous Author" or stale blind phrasing |
| Author set | Order fixed within current rules; no adds/drops past the deadline | Adding an author after author-information close |
| Format | Rebuilt in current IJCAI style, no margin/font/spacing hacks | Squeezed body to fit, broken bibliography |
| Copyright/metadata | Open-access proceedings forms and copyright signed | Missing form blocks publication |
| Registration/presentation | At least one author registered and present per current rules | Promised attendance unmet, exception not approved |
| Promised artifacts | Statements match submission and response | Released code differs from what reviewers were told |

## Acceptance-to-publication traceability

Treat the accepted submission, reviews, author response, and final proceedings record as one
auditable chain. Camera-ready edits should close reviewer concerns and production requirements
without quietly changing the scientific object that was accepted.

| Trace item | Camera-ready action | Escalate when |
| --- | --- | --- |
| Accepted claims | Keep theorem, experiment, dataset, and benchmark scope aligned with the reviewed PDF | The headline or contribution claim is stronger than the accepted version |
| Author response promises | Add only promised clarifications, corrections, and reproducibility notes | A promised artifact, limitation note, or appendix pointer is missing |
| Resubmission history | Preserve required disclosure consistency and do not rewrite around prior-review obligations | The final narrative conflicts with the submitted resubmission file |
| Ethics and LLM-use statements | Carry forward policy-sensitive disclosures in the permitted location | The final text hides or revises a disclosure reviewers relied on |
| Public artifact release | Replace anonymous links with durable public repositories only after license and anonymity checks | A repository reveals private review material or differs from promised contents |

## Final-package manifest

Before upload, build a manifest that names the owner and status for every item. Do not mark the
paper ready because the PDF compiles; IJCAI camera-ready work can still be blocked by forms,
metadata, attendance, or artifact mismatches.

| Item | Required check | Owner |
| --- | --- | --- |
| PDF | Current IJCAI style, page rules, author block, acknowledgements, no blind placeholders | corresponding author |
| Source package | TeX/Word source, figures, bibliography, style files, reproducible local build | production owner |
| Proceedings metadata | title, abstract, author order, affiliations, ORCID/author data, copyright/open-access forms | submitting author |
| Presentation | registration, in-person presenter, talk/poster assets, exception status if any | presenting author |
| Reproducibility/artifact release | code/data/license/readme/version tag match submitted claims and response commitments | artifact owner |
| Archive | submitted PDF, reviews, response, accepted PDF, source package, final public artifacts | project lead |

## Change-control rules

- Label each edit as production fix, reviewer-clarification fix, artifact-release fix, or
  scientific-content change.
- Accept production and reviewer-clarification fixes when they preserve the accepted contribution.
- Treat new experiments, new theory, new datasets, broader claims, or removed limitations as
  scientific-content changes requiring chair guidance before upload.
- Keep a short diff note for the project archive: what changed, why it was allowed, and where the
  submitted or response text already supported it.

## Worked vignette: a multi-agent paper after acceptance

A multi-agent learning paper that promised a released simulator in its reproducibility section
is accepted. Camera-ready order: restore authors and funding; confirm no coauthor was added
past the author-information deadline; rebuild in the current style without compressing the
body; sign copyright and supply proceedings metadata; register one author for in-person
presentation; write a change-control note for the promised simulator clarification; only then
publish the simulator under a valid license with the anonymized history scrubbed, so the public
artifact matches what reviewers saw.

## Reviewer/chair pushback and the venue-specific fix

- "Final PDF still says anonymous." Replace every blind placeholder before upload; chairs may
  reject non-compliant camera-ready files.
- "Author list changed." Revert to the locked set; obtain chair approval before any exception.
- "Formatting was altered to fit." Restore the official style and move overflow to the
  appendix, since proceedings consistency is enforced.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF/source/figures/bib/metadata/copyright/registration>
[Policy checks] <authors/presentation/reproducibility/artifacts/licensing>
[Traceability checks] <accepted claims / response promises / public artifact / disclosure consistency>
[Change-control risk] production fix / clarification fix / scientific-content change
[Remaining owner] <person -> task>
```
