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

## Worked vignette: a multi-agent paper after acceptance

A multi-agent learning paper that promised a released simulator in its reproducibility section
is accepted. Camera-ready order: restore authors and funding; confirm no coauthor was added
past the author-information deadline; rebuild in the current style without compressing the
body; sign copyright and supply proceedings metadata; register one author for in-person
presentation; only then publish the simulator under a valid license with the anonymized history
scrubbed, so the public artifact matches what reviewers saw.

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
[Remaining owner] <person -> task>
```
