---
name: sigmod-camera-ready
description: Use when converting an accepted SIGMOD research paper into its PACMMOD journal version, covering the port from the ACM submission template to PACMMOD format, de-anonymization, per-round issue placement, ACM DL metadata, conference presentation logistics, and the post-acceptance artifact and ARI handoff.
---

# SIGMOD Camera Ready

Acceptance at SIGMOD produces a journal article, not a conference paper: the
final version appears in an issue of PACMMOD (Proceedings of the ACM on
Management of Data), with one issue corresponding to each submission round,
and the authors are invited to present at the SIGMOD conference itself.
Camera-ready work therefore splits into a publication stream (ACM) and a
presentation stream (the conference), on different clocks. Reopen the
acceptance email and the current PACMMOD instructions before executing.

## The template flip

You submitted and revised in the standard ACM template; PACMMOD format enters
**only now**. The port is not cosmetic:

- Line widths, float placement, and page breaks all move; every figure,
  wide table, and multi-part plot needs re-inspection after conversion.
- Keep section numbering and claim wording aligned with the accepted
  version — the revision letter promised specific text at specific places,
  and shepherds or chairs may compare.
- Rebuild the bibliography against ACM reference style; DOIs for database
  papers are almost always available and expected.
- Complete ACM's rights/e-form workflow and supply ORCIDs and final
  affiliations exactly as they should render in the ACM Digital Library.

## De-anonymization inventory

| Item restored | Detail to get right |
|---|---|
| Author block | Order agreed by all authors; affiliations current, not thesis-era |
| Funding | Grant numbers reinstated after months of enforced absence |
| Acknowledgements | Colleagues and shepherd thanked; forbidden during review, expected now |
| Artifact links | Anonymous mirrors swapped for the canonical public repository |
| Self-citations | Third-person circumlocutions rewritten as honest first person |
| Prior-version notes | Relationship to any workshop or tech-report version stated |

The reverse sweep matters as much as the forward one during review: search the
final PDF for leftover "anonymous," placeholder ORCIDs, and dead anonymized
URLs before upload.

## Issue placement and timing

Because each round feeds its own PACMMOD issue, your publication date is set
by the round you cleared, not by the conference week. A Round 1 acceptance
can be citable in the ACM DL long before the conference convenes (SIGMOD 2027:
June 13–19, 2027, Huntington Beach, California). Plan announcements, preprint
updates, and artifact releases against the issue date, and registration,
travel, and talk preparation against the conference date.

## Post-acceptance checklist

```text
[ ] PACMMOD-format PDF compiles clean; all floats re-inspected post-port
[ ] Accepted-version wording preserved where the revision letter promised it
[ ] Author block, funding, acknowledgements restored and proofread
[ ] ACM rights form, ORCIDs, and DL metadata submitted
[ ] Public artifact repository live, licensed, README-tested from outside
[ ] ARI participation decided; artifact frozen at the paper's claims
[ ] Conference registration and presenting-author travel confirmed
[ ] Talk and poster drafted against the published, not submitted, numbers
```

## Artifact and ARI handoff

Camera-ready is the natural moment to convert the anonymized review-time
package into the public artifact:

- Publish the repository under its real organization with a license, a
  pinned environment, and the exact scripts behind every figure.
- If joining the Availability & Reproducibility Initiative, freeze a tagged
  release that matches the published numbers — evaluators reproduce the
  paper, not the current main branch (see `sigmod-artifact-evaluation`).
- Embed the artifact URL in the final PDF so the DL version is
  self-locating; ARI badges, if earned, attach to that same DL record.

## Concrete timeline: a Round 1 acceptance

Trace the SIGMOD 2027 Round 1 path to see the two clocks diverge:

- Jan 17, 2026 — paper submitted.
- Apr 19 or Jun 12, 2026 — acceptance (direct, or after revision).
- Following weeks — PACMMOD port, rights forms, metadata; the Round 1
  issue publishes on the journal's schedule.
- Summer/fall 2026 — paper citable in the ACM DL; artifact public; ARI
  participation window per the current edition.
- Jun 13-19, 2027 — the talk, up to a year after the science was public.

Teams routinely under-use the gap: it is enough time to earn an ARI badge,
gather adoption or feedback, and walk into the conference presenting a
paper with a track record rather than a debut.

## Failure modes at this stage

- Porting to PACMMOD format on deadline night and shipping a clipped figure
  nobody re-checked.
- Quietly "improving" a result during the port and breaking agreement with
  the version reviewers accepted.
- Announcing the paper with a repository that still 404s or carries the
  anonymized placeholder name.
- Treating the conference date as the publication date and missing the
  earlier issue-level metadata deadlines.

## Output format

```text
[Port status] not started / converted / verified post-conversion
[Fidelity check] accepted-version wording preserved yes/no, diffs listed
[Identity restore] author block / funding / acknowledgements / links
[ACM pipeline] rights form, ORCID, metadata state
[Artifact handoff] public repo state, ARI decision, tagged release
[Presentation track] registration, presenter, talk-material state
```
