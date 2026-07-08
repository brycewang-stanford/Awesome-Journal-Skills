---
name: colm-writing-style
description: Use when drafting or revising COLM paper prose — leading with a finding about language models rather than a leaderboard delta, scoping claims to tested models and scales, naming versions in text, keeping the 9-page main text self-sufficient, and matching the measured, analysis-forward voice of COLM's award lineage.
---

# COLM Writing Style

COLM prose has a recognizable register, visible in the venue's Outstanding Papers:
it reads like measurement, not marketing. The model under study is named precisely,
the claim is scoped to what was tested, and the interesting sentence is about *what
was learned*, not *who is winning*. Edit toward that register.

## Lead with the finding, not the delta

The weakest COLM opening is "LLMs have shown impressive capabilities, but..." — a
frame that positions the paper as a reaction to hype. The strongest openings state
the phenomenon or question directly:

- *Delta-first (avoid):* "We improve long-context QA by 4.2 points over strong
  baselines."
- *Finding-first (prefer):* "Accuracy on items written before a model's data cutoff
  exceeds accuracy on items written after it — the gap, not the score, is what a
  static leaderboard measures."

If the paper's most interesting sentence is a number on a benchmark, the framing is
not done; find the sentence about language models that the number supports.

## Scope discipline: the "for the models tested" rule

Unscoped generalization is the most common COLM prose bug. Claims about "LLMs" must
either carry coverage (multiple families, multiple scales) or shrink to their
evidence:

| Draft sentence | Scoped rewrite |
|---|---|
| "LLMs cannot do multi-step planning." | "None of the six models tested (App. A) exceeds 40% on depth-3 planning items." |
| "Instruction tuning destroys calibration." | "Across both model families, instruction-tuned variants are less calibrated than their bases at every scale we test." |
| "GPT-4 solves this task." | "<exact-version-string> (queried 2026-03-1x) solves 87% of instances under the App. B prompt." |
| "Our method generalizes to any decoder." | "The method assumes access to token logprobs; it applies to open-weight decoders and APIs that expose them." |

Version strings and query dates belong *in the text or a footnote at first mention*,
not only in an appendix — at this venue they are part of the noun.

## The 9-page architecture

The 2026 format is a strict 9-page main text with unlimited citation pages, and
appendices that reviewers may not read closely. Structure for that reality:

- Main text must be **self-sufficient**: setup, the evaluation's design logic, the
  contamination story, headline evidence, and limitations all inside the 9 pages.
- Appendices hold *depth*, not *load-bearing content*: full prompt texts, per-task
  tables, extra ablations. If removing an appendix breaks a main-text claim, the
  claim's support is misplaced.
- Prompts deserve first-class treatment: show one representative prompt (or its
  skeleton) in the main text so readers can judge the evaluation, and push the full
  set to the appendix verbatim.
- Do not fight the cap with typography. The template is the template; win space by
  cutting the second-weakest experiment, merging near-duplicate tables, and turning
  paragraph-length related work into claims with citations.

## Voice calibration

```text
Overclaiming register (edit away)        COLM register (edit toward)
"remarkable emergent abilities"       →  "accuracy rises from 12% to 61% between
                                          the 7B and 70B models"
"we are the first to..."              →  state the contribution; let §2 (related
                                          work) establish priority with citations
"significantly better"                →  "better by 4.1 points (95% CI ±1.3,
                                          n = 5 samples/item)" — or delete
                                          "significantly" if untested
"solves reasoning"                    →  "improves on the three reasoning suites
                                          tested; transfer beyond them is open"
"due to hallucination"                →  name the observed behavior: fabricated
                                          citation, unsupported premise, etc.
```

Two vocabulary cautions specific to this literature: **"emergent"** invites a
methodological fight about metric nonlinearity — use it only if you engage that
debate; **"understands/knows/wants"** anthropomorphize — fine informally, risky in
claims; prefer behavioral statements.

## Limitations as evidence of competence

COLM's culture (a venue founded partly to *critique* LM technology) reads a sharp
limitations discussion as expertise, not weakness. Name the models you could not
test and why (cost, access), the benchmarks that may be contaminated, the decoding
configs not explored, and the populations your human evaluation does not represent.
Specific limitations pre-empt rebuttal questions; generic ones ("more experiments
needed") waste the section.

## Titles and abstracts, COLM register

The title should name the finding or the object, not the aspiration: "X happens in
Y models under Z conditions" outperforms "Towards better X" at a venue whose
readers triage hundreds of LM papers by title alone. The abstract follows the same
arc as the paper's first page — phenomenon, why existing instruments miss it, what
you measured, on which (pinned) models, with what uncertainty, and the one-sentence
scoped conclusion. Save the memorable system name for the second sentence; the
first sentence belongs to the question. And because the March abstract deadline
feeds reviewer bidding days before the paper exists (`colm-submission`), write the
abstract as if it is the only thing a bidding reviewer will see — in March, it is.

## Revision passes, in order

1. **Finding pass** — can a reader quote the paper's claim about language models
   after page 1?
2. **Scope pass** — grep for "LLMs are/can/cannot", "models in general", "always",
   "never"; scope or support each hit.
3. **Pinning pass** — every model name in prose carries a version at first mention.
4. **Self-sufficiency pass** — read only the 9 pages; note every claim whose
   evidence lives in an appendix, and move a summary of it up.
5. **Register pass** — apply the voice table; delete superlatives that carry no
   information.

## Output format

```text
[Register] measurement-grade / marketing residue at: <locations>
[Finding sentence] "<the paper's one-line claim about LMs>"
[Scope violations] <count> — worst: <example>
[Unpinned mentions] <model names lacking versions in text>
[9-page audit] self-sufficient / load-bearing appendix content: <what>
[Edit order] <passes still to run>
```
