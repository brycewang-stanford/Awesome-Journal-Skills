---
name: ijcai-review-process
description: Use when explaining or planning around IJCAI or IJCAI-ECAI two-phase review, summary rejection, PC/SPC/AC/SAC roles, author response visibility, reviewer confidentiality, conflict-of-interest policy, ethics checks, and decision dynamics.
---

# IJCAI Review Process

Use this to reason about review-stage strategy. Reopen the current CFP, FAQ, peer-review
principles, and conflict policy before making process claims.

## Process model

- Phase 1 can be decisive. IJCAI-ECAI 2026 gave every paper two PC reviews first; papers
  with two good-quality but insufficiently positive reviews could receive summary rejection
  without author response.
- Papers advancing to full review receive additional review and discussion by PC/SPC members,
  with AC coordination and SAC cross-checking.
- The response is concise and visible to the decision group specified by current rules; it is
  not a dialogue with reviewers.
- Ethics concerns can be flagged by reviewers and escalated to the Ethics Chair.
- Conflicts include recent coauthors, advisor/student relationships, same institution,
  current grants/projects, sponsorship, personal relationships, or animosity under the IJCAI
  COI policy.
- Authors must not try to identify or contact reviewers, and reviewers must preserve
  submission confidentiality.

## Decision actors and where leverage lives

| Stage | Who decides | Author leverage | Forbidden |
| --- | --- | --- | --- |
| Phase 1 summary reject | Two PC reviewers, AC | None: there is usually no response here | Treating phase 1 as if a rebuttal will save it |
| Full review | PC, SPC, AC discussion | Concise response on pressing questions and factual errors | New experiments, code links, or scope changes |
| Decision | AC recommends, SAC cross-checks, chairs finalize | Clarity already in the paper, ethics flags resolved | Contacting or guessing reviewer identity |
| Ethics escalation | Ethics Chair | Confidential channel for unethical-review concerns | Using ethics box to argue scores |

Because IJCAI spans many AI subcommunities, a paper can draw one in-area and one out-of-area
reviewer; the out-of-area reviewer is often where summary-reject risk concentrates, so the
phase-1 readability of the contribution matters more than at single-topic venues.

## Worked vignette: surviving phase 1

A constraint-reasoning paper gets two competent reviews that are lukewarm because the second
reviewer, from a learning background, could not locate the contribution by page two. Under
IJCAI rules this profile is a summary-reject candidate before any response. The leverage is not
in the rebuttal: it is in writing so a non-specialist PC member sees the novel claim on page
one. Diagnose this risk pre-submission, since phase 1 may give no chance to reply.

## Reviewer pushback and the venue-specific fix

- "Reviewer misread the method." If it is decision-critical, correct it precisely in the
  response with a pointer to the submitted section; do not relitigate the score.
- "Two okay-but-tepid reviews." Recognize this as the classic IJCAI summary-reject pattern and
  fix readability upstream; you cannot count on a response stage.
- "Suspected reviewer is a competitor." Do not investigate; raise a conflict or ethics concern
  through the official channel only.

## Output format

```text
[Current stage] submitted / phase 1 / full review / response / decision
[Decision actors] <PC/SPC/AC/SAC/chairs>
[Likely leverage] <paper clarity / factual correction / ethics / reproducibility>
[Forbidden moves] <contact reviewers / new results / identity leakage>
```
