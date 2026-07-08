---
name: sigir-author-response
description: Use when reviews arrive for a SIGIR submission and the authors must decide how to answer — triaging IR-reviewer objections (weak baselines, missing significance tests, collection choice), writing within whatever response mechanism the current SIGIR cycle actually offers, and planning the resubmission path if the answer is no.
---

# SIGIR Author Response

First establish what response channel exists this cycle. SIGIR does **not** have a
famous institutionalized rebuttal ritual the way ICLR or KDD do, and whether a given
edition runs an author-response or discussion phase for full/short papers was not
verifiable for 2026 (待核实 — check the track page and the OpenReview timeline of your
own submission). This skill therefore covers three situations: a real response window,
no window at all, and the post-rejection letter.

## Situation 1: the cycle offers a response window

Treat it as a precision instrument, not a second paper. SIGIR reviewers are IR
methodologists; the objections cluster predictably, and each cluster has a strongest
honest answer:

| Objection cluster | Weak reply | Strong reply |
|---|---|---|
| "Baselines are outdated / not tuned" | "We will add X" | Name the tuning protocol already in the paper (grid, budget, dev split) and cite the table row proving parity of effort |
| "No significance testing" | "Differences are large" | Report the paired test you ran (test, correction, p or CI) with exact table coordinates; if you truly didn't run one, concede and state what you will report |
| "Only one collection" | "Others are future work" | Explain the claim's scope: which property of the collection the claim depends on, and why generalization is or is not asserted |
| "Metric choice hides the effect" | Defend the metric abstractly | Show the effect on the reviewer's preferred metric if it is computable from your runs — run files make this a one-line answer |
| "This is a known result" | Assert novelty | Contrast mechanisms against the specific cited paper: what it does, what yours does, what breaks if the delta is removed |

Rules of engagement:

- Answer from the submitted PDF and its cited repository. New experiments are only
  safe if small, decisive, and clearly labeled as response-phase additions the
  camera-ready would absorb.
- Quote coordinates ("Table 3, row 4; §5.2 ¶2"), never re-argue the whole section.
- Keep each reviewer's reply self-contained; meta-reviewers read per-review.
- Never break anonymity — no links that reveal a team, no "as we showed at TREC."

## Situation 2: no response window

Then the response happens *before submission*. Write the paper so the predictable
objections above are pre-answered: a tuning-protocol paragraph, a significance-testing
sentence under every close comparison, an explicit claim-scope sentence for the
collection lineup. Budget half a page of the 9 for pre-emption; it is the cheapest
acceptance probability you can buy at a venue where you may never get to talk back.

## Situation 3: after rejection

- Reviews are a free experiment-design consult from three IR specialists. Extract the
  demanded evidence into a checklist before feelings archive the folder.
- Route options in the SIGIR family and neighbors: the next SIGIR cycle, **SIGIR-AP**
  (which has advertised a revise-and-resubmit route accepting a 1-3 page response
  letter with a revised previously-rejected paper — verify its current CFP), ECIR,
  CIKM, WSDM, or a TOIS journal version if the work outgrew conference page budgets.
- If resubmitting to any SIGIR-family venue, keep a diff-log: R2's "missing BEIR
  evaluation" answered in §5.3 is a sentence in the next cover letter or R&R note.

## Drafting discipline

```text
Reply skeleton per reviewer (aim: fits on one screen)
---------------------------------------------------
Thanks + one-line summary of what we changed/clarify.
[W1] <reviewer's words, 1 line>
  -> Answer with coordinates. (Table/§/Fig)
  -> If conceded: what we will do, where it will go.
[W2] ...
Closing: the one thing we most want re-weighed, stated once.
```

Anti-patterns that reliably backfire with IR reviewers:

- Arguing that nDCG@10 improvements are "obviously meaningful" without a test —
  this community invented much of the significance-testing-in-IR literature.
- Dumping new tables for every complaint: it signals the submission was premature.
- Answering the meta-question ("is this SIGIR material?") defensively instead of
  restating the contribution type (ranking model / evaluation method / resource /
  analysis) and its intended reader.
- Promising camera-ready changes that exceed what the page budget could ever absorb —
  reviewers do the arithmetic (appendices count inside the budget at SIGIR).

## Tone calibration for a small community

IR is a small field: the reviewer you bruise this cycle chairs your session next
year. Calibrate register per line, not per document:

> **Too hot:** "R2 clearly has not read Section 5, where this is addressed."
> **Too cold:** "We thank the reviewer for this insightful comment and will
> carefully consider it in future work."
> **Right:** "§5.2 ¶3 reports this experiment (Table 4, rows 2-3); we agree the
> pointer from §3 was too subtle and will add a forward reference."

The pattern: locate, concede the *findability* problem even when the content
exists, and commit to the small fix. Reserve firm disagreement for factual errors,
and spend it at most once per reviewer — a response that disputes everything is
read as disputing nothing.

## Evidence you can compute during a short window

Because run files exist (if `sigir-artifact-evaluation` was followed), several
reviewer requests are answerable in hours without new training:

- A different metric or cutoff on existing runs — minutes with `ir_measures`.
- A different significance test or correction — minutes on per-topic scores.
- A per-query breakdown by query length/type — an afternoon.
- A new baseline or a new collection — **not** window material; promise it only if
  the camera-ready budget can honestly absorb the result either way.

## Deciding whether to fight or fold

- Fight when the misunderstanding is factual and the correction has coordinates.
- Fold (and fix) when two or more reviewers independently hit the same evidence gap —
  at SIGIR that convergence usually means the gap is real.
- A borderline paper with one champion is worth a careful, warm, precise response;
  a paper whose scores agree at reject is worth a better next submission instead.

## Output format

```text
[Response channel] confirmed window / none this cycle / post-rejection
[Reviewer map] R1: <stance, key ask> | R2: ... | R3: ...
[Triage] answerable-with-coordinates / concede-and-fix / out-of-scope
[New-evidence budget] <what, if anything, gets computed during the window>
[Resubmission route] next SIGIR cycle / SIGIR-AP R&R / ECIR / CIKM / WSDM / TOIS
[One ask] <the single re-weighing request to close with>
```
