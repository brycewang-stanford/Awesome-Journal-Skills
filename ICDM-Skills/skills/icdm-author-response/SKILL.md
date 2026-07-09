---
name: icdm-author-response
description: Use when preparing for the review phase of an ICDM (IEEE International Conference on Data Mining) submission - planning for a venue whose tradition is NO author rebuttal, pre-answering reviewer questions inside the submitted PDF and cited artifact, and, only if the current edition opens a response window, drafting a tight anonymity-safe reply.
---

# ICDM Author Response

Prepare for the ICDM review phase under its defining reality: ICDM's tradition is **no author
rebuttal**. Whether the current edition opens a response window is 待核实 (the ICDM 2025 call
mentioned responses becoming part of the submission), so this skill has two modes — the default
"there is no rebuttal" plan, and the contingency reply if a window exists. Confirm the current
Research Track call before assuming either.

## Default mode: pre-answer everything at submission

Because you may never get to reply, the submitted PDF and its cited anonymized artifact must
answer the questions a reviewer would otherwise raise. Do this *before* the deadline.

- **Baseline fairness:** state the tuning budget you gave baselines; pre-empt "you under-tuned
  the competitor."
- **Variance:** report standard deviations over seeded runs; pre-empt "is this just noise?"
- **Leakage:** state the time-respecting or edge-disjoint split; pre-empt "your split leaks."
- **Scale:** show the cost curve and hardware; pre-empt "scalable is asserted, not shown."
- **Discovery validity:** tie findings to known-truth injections; pre-empt "this is an artifact."

A weakness you notice yourself is a weakness to fix in the paper, not to defer to a rebuttal that
may not come.

## Contingency mode: if a response window opens

If the edition does provide a response, treat it as a scarce, high-value channel:

| Reviewer point | Response move |
|---|---|
| Factual misreading | Correct it with a pointer to the exact section/table already in the PDF |
| Missing-baseline ask | Report the result if you already have it; do not promise future work |
| Clarity complaint | Acknowledge and state the one-line clarification (fixable in camera-ready) |
| Fundamental gap | Concede briefly; do not oversell — honesty reads better than bluster |

```text
Response skeleton (only if a window exists; keep it tight):
  R1: [concern] -> [one-sentence answer + exact pointer to existing evidence]
  R2: [concern] -> [answer]  (report only results you already have)
  R3: [concern] -> [concede if it is a real gap]
Rule: reference evidence already in the submitted PDF/artifact; introduce nothing that
would break triple-blind anonymity or that you cannot substantiate.
```

## Keep any response anonymity-safe

- The Research Track is triple-blind; a response, if it exists, must not reveal author identity,
  institution, or a de-anonymizing link.
- Do not smuggle in new non-anonymized material or an external identifying URL.

## What not to do

- Do not plan the paper assuming a rebuttal will rescue a known weakness.
- Do not, if a window exists, argue combatively or restate the paper; answer the specific point.
- Do not promise experiments "in the final version" as a substitute for evidence reviewers can
  see now.

## Vignette: the weakness that never got a second chance

A team knew their leakage guard was easy to misread but assumed they could explain it in a
rebuttal. ICDM offered none; two reviewers flagged possible leakage and the paper was rejected on
a doubt the authors could have removed with one sentence in the submitted PDF. The lesson: at
ICDM, the rebuttal happens *before* submission — in the writing. The next cycle they stated the
split explicitly in the experimental setup and the concern never arose.

## Output format

```text
[Rebuttal exists?] no (default) / yes (verify on current call)
[Pre-answered in PDF] baselines / variance / leakage / scale / validity - list gaps
[If window exists] per-reviewer reply drafted: yes / N-A
[Anonymity] response reveals no identity: pass / N-A
[Pre-submission fixes] <questions to answer in the paper before the deadline>
```
