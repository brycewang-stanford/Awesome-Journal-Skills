---
name: dac-author-response
description: Use when handling reviewer feedback for an ACM/IEEE Design Automation Conference (DAC) Research Manuscript — writing a concise, evidence-first rebuttal IF the cycle runs an author-response period (verify; DAC has historically not), and otherwise converting DAC reviews into a targeted response-to-reviewers when rerouting a rejected paper to ICCAD, DATE, ASP-DAC, or a journal.
---

# DAC Author Response

Handle reviews with DAC's process in mind. The single most important fact: DAC's Research-Manuscript
review has **historically been TPC-driven without an author rebuttal period**, and whether the
current cycle runs one is **待核实** (`resources/official-source-map.md`). So this skill covers two
situations, and the second is the common one.

## Situation A — the cycle runs a response period (verify first)

If — and only if — the live DAC cycle offers an author response, treat it as a **short, factual
correction channel**, not a debate. EDA reviewers reject mostly on **baseline fairness, benchmark
credibility, and scalability**; a response moves a borderline paper when it supplies a *number* or
corrects a *factual misreading*, and moves nothing when it argues taste.

Priorities for a tight EDA rebuttal (assume a strict word budget):

1. **Fix factual errors first** — a reviewer who thinks you did not compare against tool X when
   Table 2 does; point to the table.
2. **Answer the baseline objection with evidence** — if a reviewer names a stronger baseline, report
   the number if you have it, or commit precisely to what you will add and why it will not change the
   conclusion.
3. **Address scalability with data** — cite the largest-benchmark runtime already in the paper, or
   give the missing figure.
4. **Concede cheaply, defend what matters** — accept small corrections plainly; spend your words on
   the one or two objections that actually decide the paper.

Do not promise experiments you cannot run before camera-ready, and do not introduce
author-revealing information — the response is still within double-blind.

```text
[Reviewer 2] "No comparison to [SOTA router]."
Response: We compare against [SOTA router] in Table 2 (columns 4-6); on the full ISPD set we reduce
overflow by X% at equal wirelength. We will make this comparison more prominent.
```

## Situation B — no rebuttal, then a reject (the common case)

With no response channel, the review packet arrives *with the decision*. The productive use of DAC
reviews is then to **repair the paper and reroute it well**. DAC, ICCAD, DATE, and ASP-DAC share
reviewer pools and criteria, so a DAC reviewer's objection is very likely to resurface at the next
venue — answer it *in the paper*, not in a letter no one will read.

Turn the reviews into a fix list:

| DAC review objection | Fix before resubmitting elsewhere |
|---|---|
| Weak/untuned baseline | Add the strongest SOTA tool, tuned to equal effort, before ICCAD/DATE |
| Private benchmarks only | Re-run on ISPD/EPFL/ISCAS/ITC/TAU so the QoR is comparable |
| Scalability doubted | Add million-cell-scale results and runtime |
| Gain not isolated | Add the ablation the reviewer implicitly asked for |
| Incremental novelty | Extend the mechanism, or reframe honestly for a journal (TCAD/TODAES) |

## If you reroute to a journal (TCAD/TODAES), a response letter *does* exist

Journals *do* run revise-and-resubmit with a point-by-point response. There, write the letter DAC
never asked for: map every reviewer point to a tracked change, quote the review, state the change,
and give the new number. That is where the discipline of `../dac-experiments` pays off — a rejected
DAC paper with a strong QoR story often becomes a clean journal accept.

## What never works

- **Arguing novelty by assertion** — "our approach is fundamentally different" without a QoR delta
  persuades no EDA reviewer.
- **Blaming the benchmarks** — if the standard suite does not flatter you, that is a signal, not an
  excuse.
- **Waiting for a rebuttal that may not come** — build the paper so it needs no rebuttal; the
  baseline and benchmark choices must be unimpeachable at submission.

## Output format

```text
[Response mode]   rebuttal (cycle confirmed) / no-rebuttal reroute / journal response letter
[Decision driver] baseline | benchmark | scalability | novelty | clarity
[Point map]       each review point -> factual correction | evidence | conceded | reframe
[If rerouting]    target venue (ICCAD/DATE/ASP-DAC/TCAD) + the top fix to make first
[Anonymity]       response (if any) free of author-revealing info? yes/no
```
