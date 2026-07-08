---
name: cvpr-topic-selection
description: Use when deciding whether a project belongs at CVPR or should route elsewhere, covering what counts as a vision contribution at the field's flagship, fit tests for methods, datasets, and application papers, realistic odds at 25% acceptance and 16k submissions, and routing to ICCV, ECCV, WACV, 3DV, NeurIPS, or a journal.
---

# CVPR Topic Selection

CVPR is the largest venue in computer vision and one of the largest in all of science —
16,092 reviewed submissions and 4,090 acceptances in 2026. Size cuts both ways: almost
any vision-adjacent topic has a reviewer pool there, and almost any weakness has a
reviewer who has seen it a hundred times. This skill decides *whether* to feed the
machine before other skills decide *how*.

## The core question

Strip the engineering and ask: **is the contribution a claim about visual data or
visual computation?** CVPR's 2026 program clustered exactly there — the largest areas
were image/video synthesis and generation; vision+language and reasoning; multimodal
learning; 3D from multi-view and sensors; and medical/biological vision (official
program announcement). Contributions where vision is merely the demo domain — a generic
optimizer tested on ImageNet, an ML theory result with a CIFAR table — historically
route better to NeurIPS/ICML, where the reviewer pool evaluates the actual claim.

## Fit tests by contribution type

| You have… | CVPR-shaped if… | Warning sign |
|---|---|---|
| A method/architecture | It solves a visual mechanism (geometry, temporal, pixels-to-structure), with benchmark wins + ablations | Gain vanishes under matched backbones |
| A dataset/benchmark | It unlocks a task the field cannot currently study, with baselines and analysis | "Bigger than the last one" is the whole pitch (and release is due at camera-ready) |
| A systems/efficiency result | Accuracy-per-FLOP frontier moves; CRF-style reporting is your friend | Speedup only on your hardware story |
| A vision-language model result | The *visual* grounding is the contribution | It's an LLM paper wearing an image encoder |
| An application (medical, agriculture, driving) | A general vision insight travels beyond the application | Domain novelty only → domain venue or WACV |
| Theory about vision | Predicts something checkable in experiments | Pure theory → NeurIPS/ICML/SIGGRAPH-adjacent |

## The honesty checklist before committing a semester

1. **Leaderboard reality**: are you within striking distance of the current SOTA on the
   benchmarks reviewers will demand, with the compute you actually have?
2. **Delta nameable**: can you state, in one sentence, the mechanism that differs from
   the three nearest papers? (If not yet, see `cvpr-related-work` first.)
3. **Ablatable**: does the idea decompose into testable design decisions, or is it one
   entangled trick?
4. **Visual evidence exists**: will qualitative results/figures show the improvement,
   or is it only a fourth-decimal metric story?
5. **Team can pay the process tax**: November triple deadline, coauthor reviewer
   duties with desk-reject enforcement, a one-page January rebuttal — the process
   itself consumes a person-month.

## Routing map

```text
Contribution core                    → First-choice venue
──────────────────────────────────────────────────────────
Flagship vision method/benchmark     → CVPR (Nov) — or ICCV/ECCV, same bar,
                                       different months: pick by readiness date
Solid but not flagship-flashy;       → WACV (applications-friendly CVF venue)
  applications emphasis
3D/geometry-centric community        → 3DV (also CVF-affiliated), or CVPR 3D areas
Learning theory / generic ML         → NeurIPS / ICML / ICLR
Graphics-adjacent synthesis          → SIGGRAPH (different review culture entirely)
Mature, extended, archival           → TPAMI / IJCV (journal timelines, no rebuttal
                                       sprint, room beyond 8 pages)
Early or niche idea                  → CVPR workshops (separate CFPs, lower stakes,
                                       same audience walking past your poster)
```

CVPR vs. ICCV/ECCV is rarely a quality question — the bar is comparable and reviewer
pools overlap — it is a *calendar* question: which deadline does your evidence mature
for? Submitting a month early to the "bigger name" with a missing ablation is how teams
donate a cycle.

## Three worked verdicts (fictional projects)

- *"We fine-tuned an open VLM on our agriculture dataset and accuracy rose 6 points."*
  → **Not CVPR-shaped yet.** The contribution is domain data + recipe. Routes: WACV
  (applications) or a domain venue — unless analysis reveals a *general* insight about
  when VLM grounding fails, which could anchor a CVPR paper with broader experiments.
- *"A test-time geometry constraint makes any monocular depth model temporally
  consistent, +X on three benchmarks, 2ms overhead."* → **CVPR-shaped.** Visual
  mechanism, plug-in generality, ablatable, cheap to evaluate broadly; the risk to
  audit is baseline freshness.
- *"A new loss improves classification on CIFAR/ImageNet, with a convergence
  theorem."* → **Split decision.** As stated, it is an ML-methods paper (NeurIPS/ICML
  reviewers evaluate the theorem properly). It becomes CVPR-shaped only if the loss
  exploits something visual (spatial structure, augmentation geometry) and the
  evidence spans vision tasks beyond classification.

## Scale realism

25.42% acceptance means the modal outcome for a competent paper is rejection, and tier
outcomes concentrate attention further (in 2026, ~3–4% of the program presented orally).
Choose CVPR when the upside justifies that variance: maximal audience (about 12,200
registrants in 2026), industrial visibility, and the strongest possible signal when a
benchmark claim survives this particular gauntlet.

## Main conference vs. CVPR workshops

The workshop program (separate CFPs, typically spring deadlines for a June
conference) is a legitimate destination, not a consolation prize: new-task papers
build their first community there, datasets get early adopters, and the audience
walking past a workshop poster is the same 12,000-person crowd. Route to a workshop
when the idea is promising but the main-conference evidence bar (leaderboard
proximity, full ablations) is a cycle away — and note that workshop publication may
interact with later dual-submission rules, so check both CFPs before using one as a
stepping stone.

## Reverify each cycle

- Current CFP topic list — areas are re-cut per edition (待核实 for 2027 until its CFP
  posts).
- Sibling-venue deadline calendar for the routing decision.
- Workshop CFPs, which appear months after the main-conference CFP.
- Acceptance-rate and program-shape statistics for the newest completed edition; the
  16k/25% figures above are the 2026 snapshot, not a constant.

## Output format

```text
[Verdict] CVPR / sibling (which) / journal / workshop / not yet
[Core claim] <one sentence, visual-contribution phrasing>
[Fit evidence] leaderboard distance · nameable delta · ablatable · visual evidence
[Process tax] team can cover duties + rebuttal week: yes/no
[Route if not CVPR] <venue + verified deadline>
[Ripeness gap] <what must exist before committing>
```
