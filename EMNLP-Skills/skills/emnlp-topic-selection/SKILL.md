---
name: emnlp-topic-selection
description: Use when deciding whether a project belongs at EMNLP, weighing its empirical-NLP identity against ACL, NAACL, EACL, AACL, CoNLL, LREC-COLING, TACL, and ML venues, matching the contribution to EMNLP's welcomed paper types including negative results and reproductions, and choosing between main conference, Findings, industry, and demo pipelines.
---

# EMNLP Topic Selection

Use this before writing. EMNLP's name is its thesis: *empirical methods*. The venue's
center of gravity is work whose contribution is established by measurement — new
evaluations, datasets, analyses of model behavior, and methods whose value is demonstrated
rather than argued. Sibling venues share the reviewer pool through ARR, so the routing
question is less "will it be reviewed differently" than "which program will want it."

## The empirical-identity test

Ask three questions of the project:

1. **Is there a language phenomenon or task behavior at the center?** EMNLP papers are
   about something a system does with language, not about an architecture that happens
   to be evaluated on text.
2. **Does the evidence plan include analysis, not just scores?** The venue's reviewing
   culture expects error analysis, ablations that isolate the mechanism, and claims
   scoped to the languages and domains actually tested.
3. **Would the paper survive its own evaluation section being adversarial?** Benchmarks
   chosen to flatter, contaminated test sets, and single-run comparisons are the
   fingerprints reviewers here are trained to find.

Three yeses: EMNLP-shaped. A no on (1) suggests an ML venue; a no on (2) or (3) is a
project problem no venue choice fixes.

## Welcomed contribution types

The 2026 call is unusually explicit that a diverse program is a goal. These genres are
all first-class, and mislabeling yours is a self-inflicted wound:

| Genre | What convinces here | Common self-sabotage |
|---|---|---|
| Empirical method | Controlled comparisons + mechanism ablations | Selling a small delta as a paradigm |
| Resource / dataset | Documented collection, agreement stats, human ceiling | Size without characterization |
| Negative result | Rigorous design that *would have* detected the effect | Underpowered study dressed as disproof |
| Reproduction | Faithful reimplementation, divergences explained | Gotcha framing instead of diagnosis |
| Survey | Organizing insight the field lacked | Annotated bibliography |
| Position | Falsifiable stakes, engagement with counterevidence | Opinion without an empirical anchor |
| Linguistic insight | Existing methods revealing something about language | Insight about the model misread as insight about language |

## Routing among the siblings

- **ACL / NAACL / EACL / AACL** — scope overlap with EMNLP is near-total; in the ARR era
  the practical differences are calendar, location, and program-committee taste. If your
  paper's strength is analytical and evaluative rather than conceptual framing, EMNLP's
  program has historically been the natural home.
- **CoNLL** — computational learning of language, cognitive and linguistic modeling
  angle; a better fit when the object of study is the learning process itself.
- **LREC-COLING lineage** — resource-centric work whose contribution is the artifact and
  its documentation more than a finding built on it.
- **TACL / Computational Linguistics** — journal pacing, revision cycles, no page fight;
  right when the work needs 20 pages or authoritative permanence more than a fall
  deadline.
- **ML venues (NeurIPS/ICML/ICLR)** — the contribution is the learning method and
  language is one testbed among several; EMNLP reviewers will ask "what did we learn
  about language?" and dislike silence.
- **EMNLP Industry Track** — deployed systems under production constraints (latency,
  cost, drift, no clean test sets); direct submission, its own deadline (June 16, 2026),
  its own reviewers. **Demo track** — working systems worth showing; verify the 2026
  demo call before planning on it (dates were unposted at check time).

## One project, three honest pitches

```text
Project: retrieval-augmented QA fails on temporally-shifted questions.

EMNLP main pitch:   "We characterize *when* and *why* RAG answers decay with temporal
                     shift (4 datasets, 3 retrieval stacks), and show index-refresh
                     policies fix only the retrieval half of the failure."
ML-venue pitch:     "A new time-conditioned retrieval scoring function with gains on
                     one QA benchmark."  (EMNLP would ask for the analysis above.)
Industry pitch:     "Operating a news QA system through 12 months of index drift:
                     what broke, what monitoring caught it, what it cost."
Pick the pitch whose evidence you actually have — not the venue with the next deadline.
```

## Timing as a fit dimension

Venue choice at an ARR conference is also a calendar choice, and the calendar can
overrule taste. Questions to settle before committing the project to EMNLP:

- Will the evidence be *complete* by the aligned ARR deadline (May 25 in 2026)?
  A dataset whose annotation finishes in June fits the next cycle and therefore a
  different conference — submitting the incomplete version to make the EMNLP date is
  how sound projects earn reject-shaped reviews.
- Does anyone on the paper need the *proceedings date* rather than the acceptance
  date? Findings and main papers publish on the same conference schedule; a graduation
  or visa timeline that needs certainty in early summer is arguing for an earlier
  cycle, whatever venue it feeds.
- Is the topic *volatile*? In fast-moving subfields (LLM evaluation especially), a
  paper reviewed in June and presented in late October will be read against an
  October literature; build the response-window and camera-ready plan expecting
  "how does this relate to <July preprint>?" questions.

## Findings in the fit calculus

Committing to EMNLP offers two acceptance surfaces: the main conference and Findings of
EMNLP — real, Anthology-indexed peer-reviewed publication, historically without a
guaranteed talk or poster. If the project's purpose requires a stage (job market,
community-building around a resource), plan for the possibility that a sound-but-not-
exciting verdict lands in Findings, and decide in advance whether that outcome ends the
project or triggers a revise-and-resubmit instead.

## The re-route that saves a cycle

If the empirical-identity test half-fails — real phenomenon, thin analysis — the
cheapest repair is usually not a venue change but an evidence change: adding the error
taxonomy, the contamination audit, and one deliberate stress test often converts an
"ML paper evaluated on text" into an EMNLP paper in four weeks of work. Change venues
when the *audience* is wrong; change the evidence when the audience is right but the
paper isn't speaking its language yet.

## Output format

```text
[Fit verdict] EMNLP-shaped / sibling-better / ML-venue-better / journal-better
[Genre] method / resource / negative / reproduction / survey / position / insight
[Empirical identity] <the phenomenon or behavior at the center, one sentence>
[Weakest fit signal] <which of the three test questions is shakiest>
[Pipeline] main via ARR / industry / demo / next-cycle target
```
