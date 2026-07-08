---
name: rss-writing-style
description: Use when revising an RSS (Robotics: Science and Systems) draft to meet the science-first bar — a falsifiable claim about robotics up front, evidence sized to claim scope, honest failure reporting, concision under an 8-page ceiling that rewards brevity, and prose that pre-answers reviewers because a rebuttal may never come.
---

# RSS Writing Style

Revise the manuscript for the venue where "the robot worked" is the beginning of a
paper, not its conclusion. RSS expects a scientific claim; the writing's job is to
make that claim visible, falsifiable, and already defended.

## The claim-first page

By the end of page one, a reader should be able to fill in:

- **Claim:** what is asserted about robotics (a mechanism, a property, a bottleneck,
  a transferable capability) — one sentence, no system name required.
- **Stakes:** what the field does differently if the claim is true.
- **Test:** what evidence in this paper could have falsified it.

If the draft's first page instead inventories modules and integrations, it is a
systems report; either surface the insight the integration proves, or reroute
(`rss-topic-selection`).

## Sizing prose to the claim

The cardinal RSS writing sin is claim-evidence inflation: general words resting on
narrow trials. Enforce the match at sentence level:

| Sentence habit | Failure it causes | Repair |
|---|---|---|
| "robust manipulation of everyday objects" | Generality unearned by 5 objects | Name the object distribution and count |
| "significantly outperforms" | No statistics behind the adverb | Effect size + interval + trials per condition |
| "works in the real world" | One lab bench ≠ the world | State the environments actually tested |
| "can be applied to X, Y, Z" | Speculation formatted as result | Move to a labeled limitations/outlook sentence |
| "novel framework" | Novelty asserted, not located | One sentence naming the delta vs the nearest method |

## Pre-answering, because there may be no rebuttal

Only above-threshold papers got a 2026 rebuttal; write as if you will not. For each
major claim, plant the defense where the objection arises:

- The obvious confound → name it and point at the ablation that kills it, in the same
  paragraph as the result.
- The "did it just memorize the setup?" worry → the transfer/perturbation condition,
  cited inline.
- The cherry-picking suspicion → the sentence stating all trials are reported,
  including failures, with the failure table's number.

## Brevity as a scored trait

The 8-page limit (excluding references, 2026) is a ceiling the CFP pointedly frames
as not a floor. Compression tactics that preserve rigor:

1. Merge related-work prose into contrastive sentences attached to your claims rather
   than a stand-alone tour.
2. One figure that carries the causal story beats three that decorate it; every
   figure caption should state a finding, not a scene.
3. Protocol details reviewers need for *belief* stay in the body; details needed only
   for *replication* go to the supplement — the CFP's self-containment rule drawn as
   a line.
4. Delete capability sentences the evaluation never touches. Each one is a free
   objection.

## An 8-page budget that respects the ceiling

A workable allocation for a claim-plus-hardware paper (adjust, don't worship):

```text
p.1        claim, stakes, falsification test, contribution list
p.2        related work as contrasts (not a tour)
p.3-4      method: the mechanism, then the system carrying it
p.5-6.5    experiments: protocol, results, ablations, failure table
p.6.5-7.5  analysis: what the failures say about the claim
p.7.5-8    limitations with scope sentences; conclusion in 4 lines
refs       excluded from the count (2026 rule)
```

Two structural rules the budget encodes: analysis gets real space (RSS reviewers
reward interpretation over raw scoreboards), and limitations are body text, not a
camera-ready afterthought.

## Sentence-level rewrites

| Draft reflex | RSS register |
|---|---|
| "To the best of our knowledge, first to..." | Name the nearest prior and state the delta |
| "Extensive experiments demonstrate..." | "600 trials across 6 conditions show..." |
| "We leave X for future work" (for a load-bearing X) | Test X or narrow the claim now |
| "Our approach is general" | "The mechanism assumes A and B; within them..." |
| "Qualitative results are in the video" | Put the quantitative version in the body |

## Honest-failure register

RSS's reviewer culture reads failure reporting as competence, not weakness. The
stylistic move: report failures with the same grammatical confidence as successes.
"CSD fails on high-friction fabrics (9/40 trials), consistently at the release step"
is stronger writing than a defensive footnote — it demonstrates the authors know
where the boundary is.

## Cross-stack terminology discipline

RSS papers span perception, planning, control, and learning in eight pages, and
vocabulary collisions cost belief:

- One name per object across the stack: if the policy's output is an "action" in
  §3, it cannot become a "command" in §5's tables.
- Define task-success vocabulary once, operationally, and reuse it verbatim in
  protocol, tables, and captions.
- Symbols survive the whole paper: reusing θ for joint angles and then for policy
  parameters is a classic cross-subfield paper wound.
- Write for the adjacent-subfield reviewer the single-track format guarantees you:
  each subfield's jargon gets a half-sentence gloss at first use.

## Output format

```text
[Claim sentence] <one sentence, falsifiable, system-name-free>
[Claim-evidence mismatches] <sentence -> repair>
[Unplanted defenses] <objection -> where to pre-answer it>
[Compression targets] <cut / merge / demote-to-supplement>
[Failure register] present and confident / defensive / missing
```
