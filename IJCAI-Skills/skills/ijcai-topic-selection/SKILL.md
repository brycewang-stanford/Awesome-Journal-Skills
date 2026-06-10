---
name: ijcai-topic-selection
description: Use when deciding whether an AI project is a strong IJCAI or IJCAI-ECAI fit, comparing main track versus special tracks, Survey Track, AIJ/JAIR expedited-publication potential, or alternative AI venues such as NeurIPS, ICML, ICLR, AAAI, AISTATS, UAI, COLT, KDD, CVPR, ACL, or ICRA.
---

# IJCAI Topic Selection

Use this before writing. IJCAI main-track submissions should report significant, original,
previously unpublished AI results with broad relevance to the AI community.

## Fit test

- Ask whether the paper advances an AI problem, AI technique, AI application domain, or
  cross-disciplinary AI boundary rather than only reporting an application result.
- Prefer IJCAI when the contribution is broadly AI-facing, technically complete in a compact
  format, and can survive a two-phase review process with limited response leverage.
- Consider special tracks for human-centered AI, AI for social good, AI4Tech, AI and health,
  or AI and robotics when the venue-specific framing is stronger than a general main-track
  frame.
- Consider the Survey Track only for mature areas and author teams with established topic
  expertise.
- Route elsewhere if the contribution is primarily ML theory, representation learning,
  computer vision, NLP, robotics, HCI, systems, or data mining and a specialist venue has a
  clearer audience.
- Check policy fit early: anonymity, recent rejection disclosures, dual-submission limits,
  data ethics, LLM-use constraints, and in-person presentation feasibility.

## Venue routing matrix

IJCAI's edge is breadth and a compact format, but a sharply specialist contribution often finds
a clearer audience elsewhere. Route by where the strongest reviewers and framing sit.

| Contribution profile | Strong IJCAI fit | Consider instead |
| --- | --- | --- |
| Cross-cutting AI idea (search, KR, planning, multi-agent) readable across subfields | Yes, main track | — |
| Deep ML theory or representation learning | Sometimes | NeurIPS, ICML, COLT |
| Heavy CV or NLP system | Rarely the best home | CVPR, ACL |
| Mature area survey by established authors | Survey Track | Journal survey |
| Polished, complete result wanting fast journal route | Main track plus AIJ/JAIR ecosystem | — |
| Social-good or human-centered AI framing | Special track | Domain venue |

## Worked vignette: a game-theory mechanism

A mechanism-design result for multi-agent resource allocation could go to an economics-and-
computation venue or to IJCAI. If the contribution is an AI technique broadly relevant across
agents, search, and learning audiences and fits a compact 7-page body, IJCAI's main track is a
strong home; the game-theory/economic-paradigms scope is squarely in-bounds. If the core
advance is a fine-grained economic-theory proof aimed at a specialist EC audience, route there
instead. Decide by which reviewer pool best judges the central claim.

## Reviewer/fit pushback and the venue-specific fix

- "This is an application, not an AI advance." Reframe the AI technique or problem contribution,
  or route to a domain venue.
- "Too specialized for a broad PC." Either broaden the framing for IJCAI breadth or choose the
  specialist venue with a clearer audience.
- "Survey from a junior team." Reserve the Survey Track for mature areas and established topic
  expertise.

## Output format

```text
[Fit] strong IJCAI / possible IJCAI / better elsewhere
[Best track] main / special / survey / other venue
[Contribution sentence] <one sentence>
[Top rejection risk] <novelty/clarity/evidence/policy/scope>
[Next action] <experiment, framing, related work, or venue switch>
```
