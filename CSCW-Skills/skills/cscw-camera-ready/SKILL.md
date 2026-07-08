---
name: cscw-camera-ready
description: Use when a CSCW paper is accepted and enters PACMHCI production — executing minor-change conditions, deanonymizing text and artifacts, ACM journal e-rights and TAPS steps, issue assignment, and the separate track of presenting at the next CSCW conference.
---

# CSCW Camera-Ready and Production

Acceptance at CSCW starts two parallel tracks that most venues fuse into one: the
paper becomes a **journal article in PACMHCI** on ACM's production schedule, and
separately the authors are **invited to present at the next CSCW conference**. Keep
the tracks distinct in your planning — the article's publication and the talk's
logistics run on different clocks with different owners.

## Track 1: the PACMHCI article

**Execute the conditions first.** Many acceptances arrive as Conditional Accept
with Minor Changes: a named list verified before the acceptance is final. Treat the
list as a contract — do the items, document where, and resist bundling in
unrequested rewrites that could reopen questions.

**Deanonymization is a build step, not a find-replace.** Reverse every layer the
submission masked:

- Restore authors, affiliations, and the acknowledgements section (people, funders,
  grant numbers) — this is the text most often still missing at the deadline
  because it never existed in any draft.
- Convert third-person self-citations back to first person where natural.
- Re-point anonymized repository links to the public, attributed release
  (`cscw-artifact-evaluation`'s release build), and verify each resolves.
- Revisit setting-level masking deliberately: some community pseudonyms were
  *promised to participants*, not merely required by review — those stay. Your
  consent documents, not the venue, govern what gets unmasked.

**ACM production mechanics.** Expect journal-standard steps: e-rights/copyright
forms, final source preparation through ACM's TAPS pipeline, ORCID for authors, CCS
concepts, and accessibility requirements (alt text, tagged PDFs). The precise
sequence, deadlines, and any open-access fee treatment for PACMHCI CSCW articles
were 待核实 at the 2026-07-08 check — take them from the acceptance email and the
live ACM author instructions, not from this file or from CHI-trained habits.

**Issue assignment.** Historically CSCW papers appeared in paired annual issues
(e.g., Vol. 8: CSCW1 April 2024, CSCW2 November 2024). How rolling acceptances map
to issues is part of the soft launch — confirm your article's volume/issue/article
number when production tells you, then cite yourself accordingly.

## Track 2: the conference presentation

- The rolling CFP's wording is an *invitation* to present at the next CSCW,
  pending space — confirm which conference year your paper is assigned to before
  booking anything. The next edition at check time: CSCW 2026, Salt Lake City,
  Utah, October 10-14, 2026.
- Registration and attendance obligations (who must register, remote options) were
  待核实; verify on the conference site early, because travel budgets and visas
  move slower than production deadlines.
- Prepare the talk for CSCW's mixed audience: lead with the cooperative practice
  and the concept, not the pipeline; participant-voice slides need the same
  paraphrase discipline as the paper.

## Two-track checklist

| Item | Track | Owner | Verified against |
| --- | --- | --- | --- |
| Minor-change conditions executed and documented | Article | Lead author | Decision letter |
| Deanonymization build (text, links, acknowledgements) | Article | Lead author | Submission-era mask list |
| Consent-bound masks preserved | Article | Ethics owner | Consent forms |
| E-rights, TAPS, ORCID, accessibility | Article | Corresponding author | Live ACM instructions (待核实) |
| Public artifact release live and cited by DOI | Article | Artifact owner | `cscw-artifact-evaluation` |
| Conference-year assignment confirmed | Talk | Any author | Official email |
| Registration/attendance rules checked | Talk | Presenting author | cscw.acm.org (待核实) |

## Final sweep

```text
[Conditions]  each acceptance condition → location in final text
[Identity]    authors/acks restored; consent-bound pseudonyms intact
[Links]       every URL and DOI in the final PDF resolves (run a link check)
[Metadata]    title/abstract/author order identical across TAPS, the PDF,
              and the artifact release
[Two clocks]  production deadline and presentation logistics tracked separately
```

The venue facts here (conference dates, issue anchors) were verified 2026-07-08;
production-mechanics items are flagged 待核实 above because ACM instructions
arrive with the acceptance and override anything written down in advance.
