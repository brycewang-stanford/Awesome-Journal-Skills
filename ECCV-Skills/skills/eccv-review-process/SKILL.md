---
name: eccv-review-process
description: Use when modeling how ECCV review actually works — the OpenReview pipeline from March registration to June decisions, the 2026 reviewer-duty enforcement that desk-rejects authors of late or LLM-written reviews, rebuttal-to-AC-discussion dynamics, and what the ECVA-run, Springer-published structure means for outcomes.
---

# ECCV Review Process

Use this to reason about what happens to an ECCV paper between upload and
decision. ECCV is run by the **European Computer Vision Association (ECVA)**
with per-edition program chairs; there is no standing editorial board, and
process rules are rewritten every two years — the 2026 mechanics below are
verified anchors (2026-07-08), not permanent law.

## The 2026 pipeline

| Stage | 2026 dates | What actually happens |
|---|---|---|
| Registration → submission | Feb 26 → Mar 5 | OpenReview record created; late profile fixes until Mar 2 |
| Review period | Mar 13 → Jun 17 | ACs assign; reviewers work on OpenReview |
| Reviews to authors | May 2 | Typically three reviews with ratings |
| Rebuttal | due May 11; to reviewers May 12 | One page, two-column, references included |
| AC discussion → decision | May–Jun; decisions **Jun 17** | AC synthesizes; borderline fates decided here |
| Camera-ready | Jun 30 AoE (extended) | Springer LNCS pipeline takes over |

## The 2026 enforcement regime

The distinctive 2026 process fact: **review quality was enforced against
authors**. All authors were expected to be willing to review if asked, and:

- A reviewer missing the review deadline faced desk rejection of all papers
  they co-authored.
- A review judged "highly irresponsible" — explicitly including LLM policy
  violations — triggered the same, at PC discretion.
- The LLM policy (aligned with CVPR 2026) barred using LLMs to write reviews
  or share substantial paper content, while allowing background research and
  short grammar checks; reviews were screened for violations.

Strategic consequence: your paper's risk surface includes every co-author's
reviewing inbox. Track assignments like deadlines.

## Who is reading

- Panels are internationally mixed with a strong European base; expect one
  in-niche reviewer and two adjacent-niche reviewers rather than three
  specialists.
- Adjacent-niche reviewers anchor on the benchmark table and the qualitative
  figures; the in-niche reviewer checks novelty against the last CVPR/ICCV
  cycle. Write and rebut for both audiences.
- ECCV's biennial cadence means reviewers compare against *two years* of
  intervening literature, including papers published after your development
  froze — expect and preempt "how does this compare to [March-adjacent
  arXiv]?" via the concurrent-work conventions in `eccv-related-work`.

## Reading the decision mechanics

```text
Signals that the AC discussion, not the raw scores, decides you:
- score spread >= 2 points between reviewers
- one review is short + negative (candidate for AC down-weighting)
- rebuttal directly falsified a factual claim in a review
Actions that move an AC:
- rebuttal blocks quotable into a meta-review
- reviewer-requested evidence that already existed in the submission
Actions that do not:
- appeals to effort, novelty-by-assertion, or venue prestige of prior work
```

## After the decision

- **Accept**: the Springer/ECVA machine starts (`eccv-camera-ready`); open
  access appears ~4 weeks pre-conference on ecva.net.
- **Reject**: the biennial gap makes the reroute decision urgent — reviews
  arrive in June, and CVPR's November deadline is the natural next stop.
  Convert each review point into a revision ticket while context is fresh.
- Award structure exists (ECVA's Koenderink Prize honors a ten-year-old ECCV
  paper each edition) but plays no role in decisions; ignore it during
  review, use it for taste calibration in `eccv-topic-selection`.

## Output format

```text
[Stage] pre-submission / in-review / rebuttal / discussion / decided
[Panel model] <in-niche vs adjacent reviewer count, score spread>
[Enforcement exposure] <co-author reviewing assignments + status>
[AC leverage points] <what the meta-review can quote>
[Next-stage move] <one action with its date anchor>
```
