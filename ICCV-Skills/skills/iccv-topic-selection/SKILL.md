---
name: iccv-topic-selection
description: Use when deciding whether a computer-vision project should target ICCV, weighing the biennial odd-year cadence and its two-year option cost, what the Marr Prize lineage says about ICCV taste, honest odds at 24% acceptance, and when to hold work for CVPR, ECCV, WACV, or a journal instead of forcing the March deadline.
---

# ICCV Topic Selection

ICCV happens every other year. That single fact reorganizes the whole decision:
choosing ICCV is not "which top vision venue" but "is this project ready for a
deadline that will not come again for twenty-four months." In the 2025 cycle
(Honolulu, the most recent completed edition, checked 2026-07-08), 11,239 valid
submissions competed for 2,699 acceptances — 24%. The next intake is ICCV 2027
(Hong Kong, October 2027, CFP not yet posted at check time).

## Decide the calendar before the venue

CVPR, ICCV, and ECCV share reviewer culture, format, and prestige tier. What they do
not share is timing. In an odd year, the vision calendar offers a November deadline
(next CVPR) and a March deadline (ICCV); in an even year the March-ish slot belongs
to ECCV. So the real question is never "ICCV or CVPR" in the abstract — it is:

```text
When does your evidence mature?
├── Strong by late winter of an ODD year  → ICCV (early-March deadline, 2025 anchor)
├── Strong by autumn of any year          → CVPR (November deadline)
├── Strong by late winter of an EVEN year → ECCV (spring deadline)
├── Strong but application-first          → WACV (CVF, applications-friendly)
├── Needs >8 pages or archival depth      → TPAMI / IJCV
└── One study short of the flagship bar   → workshop at any of the three,
                                            then the next big deadline
```

Submitting weak-but-early to ICCV because "the next one is two years away" is the
classic error this skill exists to block: a rejection costs you the cycle *and*
burns first-impression goodwill in reviewer pools that overlap heavily across all
three siblings.

## What ICCV has historically crowned

The Marr Prize record is a usable taste signal because it spans the field's eras:
SIFT-era local features (Lowe's scale-invariant feature paper is ICCV 1999),
instance segmentation (Mask R-CNN, Marr Prize 2017), backbone architecture (Swin
Transformer, Marr Prize 2021), controllable generation (ControlNet, Marr Prize
2023), and text-conditioned physical construction (BrickGPT, Marr Prize 2025).
The through-line is not a subfield — it is a *reusable visual capability* that other
groups adopt within one cycle. Ask of your project: could a stranger build on this
by the time the next ICCV arrives?

## Fit interrogation

Run these five questions before committing a team to the March deadline. Two "no"
answers mean route elsewhere or wait.

| Question | Passing answer looks like | Failing answer looks like |
|---|---|---|
| Is the claim about seeing? | A mechanism for pixels, geometry, video, or visual grounding | Vision is only the benchmark suite for a generic ML idea |
| Does it survive current baselines? | Within reach of leaderboard SOTA with your actual compute | Wins only against pre-foundation-model baselines |
| Is there a two-year half-life? | The capability will still matter at the *next* ICCV | A patch on a model family that will be obsolete by autumn |
| Can reviewers falsify it? | Ablations isolate the mechanism; failure cases shown | One entangled system where nothing can be turned off |
| Can the team pay the duty tax? | Coauthors can absorb reviewer assignments (every author reviews at ICCV — 2025 rule) | Nobody has review bandwidth in the post-deadline months |

## Contribution types and their ICCV posture

- **New method or architecture** — the default ICCV genre. Needs a nameable delta
  against the three nearest papers plus transplant evidence (your module inside a
  baseline).
- **Dataset or benchmark** — viable, but the paper must demonstrate what the field
  can *now study*, not report a larger row count; release logistics start at
  acceptance, not at camera-ready panic.
- **Analysis / measurement paper** — ICCV audiences reward careful negative or
  diagnostic results more than folklore suggests, but only with breadth: one model
  family analyzed is a workshop paper.
- **Vision-language / generative work** — the largest and most crowded lane after
  2023. Differentiation must be mechanistic; "we fine-tuned a VLM and it improved"
  is a domain-venue paper.
- **Theory** — route to NeurIPS/ICML unless the theorem predicts something an
  ICCV reviewer can watch happen in a table or a video.

## The option-cost calculation

Because the venue is biennial, an ICCV decision is really a portfolio decision.
Write it down explicitly:

```text
option-cost worksheet (fill before committing)
  target:            ICCV 2027, CFP 待核实 — deadline unknown until posted
  evidence gap:      <experiments missing today>
  gap closes by:     <month/year, honest>
  if later than ~Feb 2027:
      plan A becomes CVPR 2027-cycle (Nov deadline) or ECCV 2028
  cost of waiting:   <who else is racing this idea; arXiv velocity in the area>
  cost of rushing:   burned cycle + overlapping reviewer pools remember drafts
```

If the "gap closes by" line is within six weeks of the deadline, plan for the
supplement and rebuttal to carry zero new evidence — ICCV's 2025 cycle put paper
and supplementary material on the **same day** (a deliberate 2025 change), so
there is no trailing week to finish experiments in.

## Odds, stated plainly

24% acceptance means three of four reviewed submissions exited with a rejection in
2025. Orals were reported at roughly half a percent of submissions and Highlights
at 263 papers — treat both as reported figures. The rational posture: target ICCV
when the work genuinely benefits from the international flagship stage and its
two-year echo; otherwise the annual CVPR intake prices the same prestige with a
shorter retry loop.

## Cycle-check before advising

- ICCV 2027 scope, topic areas, and CFP — none published at check time (待核实);
  the 2025 CFP is the newest scope anchor.
- Whether the every-author-reviews rule and the 25-submission-per-author cap
  persist into 2027.
- Sibling deadlines for the routing decision (next CVPR and ECCV CFPs).

## Output format

```text
[Route] ICCV <year> / CVPR / ECCV / WACV / journal / workshop / wait
[Claim in one line] <the visual capability being claimed>
[Calendar logic] evidence matures <date> vs deadline <date or 待核实>
[Fit tally] seeing-claim / baselines / half-life / falsifiable / duty-tax → n/5
[Option cost] <what waiting for the next cycle costs, one line>
[Blocking gap] <the single item that decides the route>
```
