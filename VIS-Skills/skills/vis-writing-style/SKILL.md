---
name: vis-writing-style
description: Use when revising an IEEE VIS paper for a task-grounded visualization contribution on the first page, a design rationale that ties each visual encoding and interaction to a task, evaluation matched to the contribution type, honest limitations, and disciplined use of the VGTC/TVCG 9+2 page budget for a paper that will be read as an IEEE TVCG journal article.
---

# VIS Writing Style

Use this when revising the main paper. IEEE VIS papers are **IEEE TVCG journal articles** read by
visualization researchers, so they need a **task-grounded visualization contribution stated on the
first page** and a **design rationale a reviewer trusts**. The failure this skill prevents is a
technically fine paper that reads like a gallery of pretty pictures, or an ML/systems result with a
chart bolted on, instead of a contribution about how people see and reason with data.

## Revision rules

- **Lead with the visualization contribution:** the data-and-task problem, why existing
  representations are inadequate for it, the contribution (technique, system, study, or model), the
  evidence, and what changes for people analyzing data.
- **Justify every encoding and interaction by task.** Each visual channel (position, length, color,
  shape) and each interaction (filter, brush, link) should be tied to the analysis task it serves —
  not chosen by habit. An unjustified encoding is the fastest VIS reject.
- **Match evaluation to the contribution type.** A perceptual claim needs a controlled study; a
  technique needs a benchmark or comparison; a design study needs reflection and validation across
  abstraction levels; a system needs a demonstration of real use. Do not evaluate a system with an
  accuracy number that answers a different question.
- **Report limitations honestly.** Name where the encoding breaks down (scale, occlusion, data
  type), where the study's validity is bounded, and what you did not test — reviewers reward candor
  and punish over-claiming.
- **Respect the 9+2 page budget as a design constraint,** not a formatting afterthought; a
  figure-heavy field forces deliberate space choices.
- **Maintain double-blind wording** (if you opted in) in self-citations, system names,
  acknowledgements, and open-materials links.

## Visualization-paper skeleton

| Section | Job it must do | Common failure |
|---|---|---|
| Intro | Data/task problem, inadequacy, contribution, evidence preview, payoff — first page | Leads with a technology trend or a screenshot, not a task |
| Related work | Position against the nearest visualization prior work as a delta | Catalog of citations with no contrast |
| Data & task abstraction | What data, what tasks, at what abstraction level | Jumps to a design with no task grounding |
| Design / technique | The encoding + interaction, each justified by task | Design by aesthetics; unjustified channels |
| Evaluation | Evidence matched to the contribution type | Method mismatched to the claim (e.g., accuracy for a usability claim) |
| Limitations & discussion | Where it breaks; what generalizes | Generic paragraph untethered to this design |

## Sentence-level rewrites

| Draft pattern | VIS-safe rewrite |
|---|---|
| "Our tool is intuitive and powerful." | "supports task T; in the study, users completed T faster (effect size ..., 95% CI ...) than with <baseline>" |
| "We use color to show the values." | "we encode magnitude with a CVD-safe luminance ramp because the task is ordered comparison" |
| "The visualization looks clean." | Claim scoped to a task outcome or a measured perceptual property, not aesthetics |
| "We evaluate on a large dataset." | "we demonstrate on <dataset>, chosen because it exhibits <property> the technique targets" |
| "Users liked the system." | "in the study, N of P participants preferred it for task T; qualitative themes in §7" |

## Design-rationale discipline

```text
[Data]        what is the data type (quantitative/ordinal/nominal/temporal/network/spatial)?
[Task]        what analysis task (compare/locate/cluster/correlate/track-change)?
[Encoding]    which channel serves that task, and why is it more effective than the obvious default?
[Interaction] which interaction reduces the cost of the task, and what does it cost the user?
-> state each choice next to the view it produces, not as a separate "we chose colors" aside
```

## Vignette: rescuing a design-by-screenshots draft

A draft that opens with a system screenshot and lists features: rewrite the intro to lead with the
domain data and the analyst's task; add a data/task abstraction section; for each view, add one
sentence tying its encoding to a task; replace "users found it useful" with the study's measured
outcomes and qualitative themes; and add a limitations paragraph naming the scale at which the main
view degrades. The test of a good revision: a reviewer can answer "what task does each view serve,
and what is the evidence it serves it?" from the body alone.

## Output format

```text
[Writing diagnosis] clear / under-motivated / design-by-aesthetics / evaluation-mismatched / over-claimed
[First-page fix] <new framing leading with the data/task contribution>
[Encoding audit] <view -> channel -> task served -> justified? yes/no>
[Evaluation match] <contribution type -> evidence type -> present? yes/no>
[Anonymity edits] <system names / self-citations / links to rewrite (if double-blind)>
```
