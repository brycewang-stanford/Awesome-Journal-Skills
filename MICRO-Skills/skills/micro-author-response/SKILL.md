---
name: micro-author-response
description: Use when reviews arrive for a MICRO submission and the rebuttal/revision window opens — triaging reviewer objections by what can change a decision, answering methodology attacks with runs and configs rather than promises, keeping anonymity intact, and staying inside MICRO's professional-conduct rules for rebuttals.
---

# MICRO Author Response

MICRO 2026 scheduled a combined **rebuttal/revision window, June 3–17** — two full
weeks, which is generous by conference standards and changes the strategy: there is
time to *run new experiments*, not merely to argue. Whether the cycle permitted an
updated PDF versus text-only responses is 待核实 on the live pages; the playbook
below works under either mechanic.

## Hour zero: classify before drafting

Read all reviews twice, then sort every distinct objection into exactly one bucket:

| Bucket | Example | Winning move |
|---|---|---|
| Factual misread | "No overhead analysis" — but Table 5 exists | Point precisely: "Table 5, rows 3–6" |
| Methodology doubt | "Baseline prefetcher looks untuned" | Run the check they imply; report numbers |
| Missing experiment | "How does this behave at 16 cores?" | Two weeks is enough — run it |
| Scope disagreement | "Should also handle GPUs" | Bound the claim; do not promise a new paper |
| Taste / significance | "Gains feel incremental" | Reframe headroom-captured %, cite the oracle bound |

Decision-relevant buckets are the middle three. A rebuttal that spends its length
on the misreads and the taste disputes has conceded the methodology fight.

## The MICRO-specific physics of rebuttals

- **Methodology objections dominate outcomes here.** This community's reviewers
  audit configs (see `micro-review-process`). The strongest rebuttal sentence at
  MICRO is a number from a run completed inside the window: "With the reviewer's
  suggested DRAM timing, geomean speedup moves from 8.4% to 8.1% (per-workload data
  in the response)."
- **The two-week window is a lab sprint.** Pre-stage it: keep the simulator tree
  and manifests warm from April (the `micro-reproducibility` ledger exists for
  this). Budget days 1–2 triage, days 3–10 runs, days 11–13 drafting, day 14 buffer.
- **Anonymity persists.** No identifying repo updates, no "in our ISCA paper" — the
  guidelines keep double-blind obligations alive through this window.
- **Tone is enumerated policy.** MICRO's 2026 guidelines make unprofessional
  language in rebuttals grounds for rejection and for reporting to ACM/IEEE. Strip
  every trace of indignation; a hostile reviewer is answered with data and courtesy.

## Response architecture

```text
Global note (3-5 lines): the one misunderstanding shared by multiple reviews,
corrected once with evidence pointers. New results summarized in one table.

Per reviewer, numbered:
  R1.Q1  [misread]     Table 5 rows 3-6 report exactly this; summary: ...
  R1.Q2  [new run]     Ran 16-core config (same manifest, cores=16):
                       geomean 6.9%, no regression beyond -1.2% (mcf). 
  R2.Q1  [scope]       Agreed this targets CPUs; title/claims already scoped; GPU
                       extension noted as future work, no claim made.
Close each: what text will change in the final version (one line, concrete).
```

Rules of the form: answer the question asked, lead with the number, never promise
what you did not run ("we will evaluate X" convinces nobody at a venue that can
check), and never introduce a result you cannot back with a manifest.

## Sentence surgery: weak versus strong response lines

| Weak (deflects) | Strong (answers) |
|---|---|
| "We believe our baseline is reasonable." | "The baseline matches [12]'s config (Table 2); its SPEC-int MPKI of 4.1 sits inside the published 3.8–4.4 envelope." |
| "We will add this experiment to the final version." | "We ran it: at 16 cores, geomean 6.9% (was 6.2% at 8), full table below." |
| "The reviewer misunderstands our mechanism." | "To clarify §4.2: marking does not evict; eviction waits for a demand miss, so a false positive costs a re-fetch only if the line was truly reused." |
| "This is orthogonal to our contribution." | "Agreed it is out of scope; the claims in §1 are already limited to CPUs, and we will make that explicit in the abstract." |

The pattern in every strong line: a location in the paper, a number, or a bounded
concession — something the reviewer can verify without trusting you.

## Prioritization under a length cap

If the cycle imposes a word/character cap (待核实), spend it in this order:

1. The objection most likely to flip a negative review — usually the sharpest
   methodology doubt from the most engaged reviewer.
2. Any misread shared by 2+ reviewers (cheap, high yield).
3. New-experiment results, compressed to geomean + worst case + pointer.
4. Everything else in one-line acknowledgments.

Reviewers who see their main concern answered with a run tend to advocate in the
discussion phase; reviewers who see it deflected tend to dig in.

## Coordinating a multi-author response

The two-week window fails most often on coordination, not content:

- Assign one **owner per reviewer** (drafts that reviewer's answers) and one
  **editor** who merges voices into a single register — patchwork tone reads as
  disarray.
- The runs and the prose proceed in parallel: owners draft placeholder sentences
  with `[NUMBER]` holes while the queue executes; the editor rejects any
  placeholder that survives to day 13.
- Freeze at day 14 minus 12 hours. Last-minute additions skip the tone audit and
  the manifest check — the two audits this venue punishes skipping.

## After submission of the response

Nothing more can be sent — hold to that even if a reviewer question haunts you;
unsolicited chair contact to append arguments reads badly at any venue. Log what was promised (the "text will change" lines) —
they become the camera-ready worklist if accepted (`micro-camera-ready`) and the
revision spec if rejected (`micro-workflow` fallback lattice). Notification for the
2026 cycle: July 7.

## Output format

```text
[Objection ledger] misread N · methodology N · new-experiment N · scope N · taste N
[Flip target] <reviewer + objection chosen as priority 1, and why>
[Run plan] experiments launchable in window: list with day estimates
[New numbers] <headline results produced during window, manifest paths>
[Tone audit] zero sarcasm/indignation: confirmed
[Promises logged] camera-ready worklist entries: N
```
