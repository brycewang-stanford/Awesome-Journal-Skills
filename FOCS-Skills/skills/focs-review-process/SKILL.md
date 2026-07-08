---
name: focs-review-process
description: Use when reasoning about how a FOCS (IEEE Symposium on Foundations of Computer Science) submission is evaluated — the TCMF-sponsored program committee, subreferee delegation, double-blind norms the venue adopted years before STOC, the summer decision arc, and what each outcome means for a theory paper.
---

# FOCS Review Process

FOCS reviewing is run by a program committee assembled per edition under IEEE
Computer Society TCMF sponsorship — for FOCS 2026, chaired by Sanjeev Khanna
(CFP checked 2026-07-08). There is no standing editorial board and no
multi-year continuity of policy: each cycle's CFP is the constitution, and
each PC interprets it once. This skill models the pipeline so authors can
predict it rather than be surprised by it.

## Pipeline anatomy (April → summer, 2026 cycle)

| Stage | Who | What actually happens |
|---|---|---|
| Assignment | PC chair + conflict data | Papers matched to 2–4 PC members using HotCRP topics and your conflict declarations — errors here trace back to sloppy metadata |
| Expert consultation | PC members → subreferees | A PC member covering a distant subarea recruits the specialist your paper needs; assume at least one reader knows the area's folklore |
| Reading under the window rule | Everyone | Breadth readers judge from abstract + references + ten pages; depth readers verify targeted proofs (`focs-supplementary`) |
| Committee discussion | Full PC (online and/or meeting) | Papers argued comparatively across all of TCS; the champion model dominates — someone must *want* your paper in |
| Decision | PC | Notification date for 2026: 待核实 (not published at check time; historically midsummer) |

No author-response round appears in the FOCS 2026 CFP, and none is
traditional at this venue (whether any PC-initiated clarification contact
occurs in 2026: 待核实). The practical consequence is architectural: your
submission is your entire side of the conversation (`focs-author-response`).

## What the committee optimizes

A flagship theory PC comparing ~85% of submissions for rejection converges on
three questions:

1. **Is it correct?** Verified by depth readers on the proofs that matter;
   papers with one delicate lemma and a clean overview get that lemma read
   hard. Unverifiable-as-written proofs draw "cannot confirm the main claim,"
   which functions as rejection regardless of significance.
2. **Does it move the field?** The consequence/obstacle case from
   `focs-topic-selection`, judged by breadth readers who will not decode
   subarea-internal significance on their own.
3. **Would the program be poorer without it?** The comparative question that
   kills technically-fine papers: a correct, novel, small step loses its slot
   to a flawed-but-fertile idea more often than authors expect.

## Double-blind, the FOCS way

FOCS moved to double-blind years before its ACM sibling — the 2023, 2024,
2025, and 2026 CFPs all mandate it (first double-blind edition: 待核实), with
consistent purpose language: enabling an unbiased initial judgment, while
accepting that determined identification (e.g., via the arXiv full version)
remains possible. Implications for authors:

- Reviewers are instructed not to hold public preprints against anonymity;
  keep posting to arXiv/ECCC.
- The bar is on *your* prose and metadata, not on the world's knowledge
  (`focs-submission` has the sweep).
- Subreferees also receive anonymized papers; a "who else could have proved
  this" guess by an expert is tolerated by design, not a policy failure.

## How authors can (and cannot) shape the process

The levers are all pre-deadline: topic selections and conflict declarations
steer assignment (`focs-submission`); the ten-page window determines what
breadth readers know; self-flagged delicate lemmas direct depth readers'
hours to where scrutiny helps you (a checked hard lemma is a champion's
strongest argument). After the deadline there are no levers — no response
round, no supplementary uploads, no revised versions. The corresponding
anti-levers: an overclaimed abstract poisons the committee's trust in
everything else; a proof the depth reader cannot verify converts a champion
into a skeptic; and any attempt to reach reviewers socially is a reportable
breach in a community small enough that it will be recognized.

## Interpreting outcomes

```text
ACCEPT           -> execute focs-camera-ready; full version public before talk
REJECT, reviews  -> triage comments into: correctness findings (fix before
  substantive      any resubmission), significance findings (usually means
                   re-aim the framing or the venue), window findings
                   ("couldn't find X" = your p.1-10 failed, not the reviewer)
REJECT, thin     -> common at flagship scale; carries almost no information
  reviews          about the paper's worth — decide the next venue on your
                   own significance audit, not on two sentences
```

The venue's rhythm gives every rejected FOCS paper an immediate second life:
the STOC deadline arrives in autumn, SODA and ITCS deadlines cluster nearby,
and the arXiv version keeps the result claimable throughout. A FOCS rejection
delays a strong theory result by months, not years — plan accordingly rather
than appealing, since no formal appeals process exists at this venue (any
genuine procedural irregularity goes to the PC chair, once, politely).

## Reading the reviews you eventually receive

Whether reviews accompany the decision, and in what depth, varies by cycle
(2026 practice: 待核实). When they arrive, decode them by reviewer role
rather than by score:

- A **breadth review** that misstates your result is data about your first
  ten pages, not about the reviewer — the window failed its one job.
- A **depth review** engaging specific lemmas is the most valuable free
  refereeing your paper will ever get; mine it fully before any
  resubmission (`focs-author-response` has the memo protocol).
- A short review with high confidence usually means a subreferee's verdict
  compressed by the PC member who commissioned it; the terseness carries no
  signal about care taken.

## Calibration notes

- Acceptance statistics vary by cycle and are not published in the CFP; do
  not quote a rate without a per-year source (待核实).
- Award decisions (Best Paper, Machtey Award for best student paper) are made
  by the PC from the accepted pool; nothing in the submission process asks
  you to apply — eligibility hygiene is covered in `focs-camera-ready`.
