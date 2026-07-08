---
name: corl-author-response
description: Use when drafting the CoRL rebuttal — a single-page PDF due days after reviews are released, aimed at reviewers, the Area Chair, and the discussion window that follows. Covers triage against the first-round gate, one-page layout economy, presenting new numbers compactly, and tone for an exchange that becomes public on acceptance.
---

# CoRL Author Response

CoRL's rebuttal is a **one-page PDF**, not a text box — a format that rewards
preparation and layout discipline over volume. In the 2026 cycle it was due
August 11, 11:59 PM AoE, with reviewer–AC discussion following August 12–19
(corl.org rebuttal instructions, read 2026-07-08). The window between reviews
arriving and the deadline is measured in days; the winning move is to have
experiments and a compiled skeleton ready before reviews exist (see
`corl-workflow`).

## First: confirm the rebuttal is live

CoRL 2026 applied a first-round rejection rule — no weak-accept-or-above score
from any reviewer or the AC makes the paper a candidate for rejection without
rebuttal. So the opening triage is not "what do I answer?" but "who is my
advocate?": identify the most positive scorer, protect their reasons for
optimism, and target the specific objections that keep others below threshold.

## The one-page economy

A page holds roughly 700–900 words in the template's footprint, less once you add
a results table. Spend it by expected score movement:

| Budget slice | Content | Why it earns its space |
|---|---|---|
| ~15% | Header: thanks (one line) + a 2–3 line summary of what the rebuttal adds | ACs skim this first; make the additions enumerable |
| ~50% | The 2–3 concerns the AC flagged or multiple reviewers share | Core-concern focus is what the official instructions ask for |
| ~25% | One compact table/figure of **new** numbers (seeds, episodes, baseline) | Evidence moves scores; prose reassurance does not |
| ~10% | Per-reviewer one-liners for smaller points, keyed as R1/R2/R3 | Shows nothing was ducked |

What does *not* fit on the page: re-explaining the paper, quoting long review
passages back, answering every minor point at equal depth, or promising future
work as a substitute for a number you could have produced.

## Compact evidence patterns

New robot-learning evidence compresses well if you design for it:

```latex
% One-page rebuttal skeleton (compile with the venue-permitted format)
\section*{Response to Reviews — Paper \#XXXX}
We thank the reviewers. This response adds: (i) 5-seed results on all
tasks (R1, R3), (ii) a real-robot spot-check of the sim claim (R2),
(iii) the missing diffusion-policy baseline (R1).

\paragraph{Seeds and episodes (R1.W1, R3.W2).}
\begin{tabular}{lccc}
Task suite & Ours & Ours (5 seeds) & DP baseline \\
Kitchen-6  & 78\% & 76.4 $\pm$ 2.1\% & 61.2 $\pm$ 3.0\% \\
...
\end{tabular}
% cite episode counts inline: "each cell = 5 seeds x 50 eval episodes"

\paragraph{Sim-to-real scope (R2.W1).} We ran task A on hardware:
64\% over 25 trials (video frames in Fig.~1); we will scope the claim
to tasks A--B in revision and state the transfer gap explicitly.
```

Rules of thumb: every number states its seeds × episodes provenance inline; every
promised revision names the section it will change; anything that cannot be shown
in one table is summarized with its single headline number.

## Answer patterns by objection type

- **"Only N seeds / episodes"** — run more *before* reviews arrive; report mean ±
  dispersion and whether conclusions changed. This is the cheapest score-mover at
  this venue.
- **"Missing baseline X"** — run X under the same evaluation protocol if at all
  feasible; if genuinely infeasible in the window, explain the concrete blocker
  (hardware access, closed weights) and give the nearest fair proxy.
- **"Claim exceeds evidence (sim vs real)"** — concede scope precisely and show
  the smallest real-robot result that preserves the paper's core; a scoped-down
  true claim beats a defended overclaim in the discussion window.
- **"Limitations section too thin"** — treat as a gift: list the 2–3 items you
  will add; this section is mandatory at CoRL and reviewers audit it.
- **Factual misreading** — quote the paper's line number, correct once, stay
  flat in tone; flag persistently wrong low-confidence reviews to the AC via a
  confidential comment, not in the shared page.

## During the discussion window (Aug 12–19 pattern)

- Reviewers are asked to remain responsive and to update scores when the rebuttal
  warrants it — so check OpenReview daily; a reviewer follow-up unanswered for
  three days reads as concession.
- Keep any follow-up replies to a few sentences anchored to the rebuttal PDF
  ("see Table 1 of our response, row 2").
- The AC and SAC will carry your case into decision meetings you cannot attend;
  a final short summary comment ("changes we commit to in revision: …") gives
  them a clean artifact to quote.

## Tone: you are writing for the public record

Reviews and rebuttals of accepted CoRL papers are made publicly available. Write
the page so you would be comfortable with it linked from the paper forever:
no sarcasm, no reviewer-blaming, no overpromising. Concessions phrased as
improvements ("we agree, and the revision will…") age well in public.

## Final checklist

```text
[ ] At least one gate-passing score exists (else: resubmission branch)
[ ] Page compiles to exactly 1 page, venue-permitted format
[ ] AC-flagged / shared concerns get the majority of the space
[ ] Every new number carries seeds x episodes provenance
[ ] Every commitment names its revision location
[ ] Anonymity preserved (no identity, no identifying links)
[ ] Submitted well before Aug 11 23:59 AoE; calendar alert for the
    Aug 12-19 discussion window
```

Rebuttal format, deadlines, and the gate rule are re-set annually — reconfirm at
https://www.corl.org/contributions/instruction-for-rebuttal for the live cycle.
