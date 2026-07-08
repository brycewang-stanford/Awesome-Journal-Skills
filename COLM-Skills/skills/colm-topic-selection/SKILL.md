---
name: colm-topic-selection
description: Use when deciding whether language-model research belongs at COLM or should route to ACL/EMNLP, ICLR, NeurIPS, ICML, or a workshop — applying the object-of-study test, matching against COLM's CFP lanes (training, data, evaluation, inference, safety), and weighing the trade-offs of a young venue before writing begins.
---

# COLM Topic Selection

Almost every LM paper *could* be sent to five venues; COLM exists because the authors
of such papers kept finding that none of the five was actually about their question.
This skill decides whether your project is one of those papers. Run it before the
first draft — the March abstract deadline punishes late routing changes.

## The object-of-study test

Ask one question: **is the language model the thing being studied, or the tool doing
the studying?**

- *Studied* — you train, measure, dissect, steer, attack, or critique LMs, and the
  finding is about LMs themselves. That is COLM's declared identity: a venue for
  understanding, improving, and critiquing LM technology, created (announced October
  2023, first edition 2024) because these questions sat awkwardly at every older
  venue.
- *Tool* — the LM is fixed infrastructure and the contribution lives in a task,
  domain, or application. Route to the task's home venue; COLM reviewers will ask
  what was learned about language models and find nothing.

A useful second probe: delete the specific model names from your abstract. If the
claims survive as statements about language modeling (a training dynamic, a data
effect, an evaluation artifact, an inference trade-off), COLM fits. If what remains
is a task result, it does not.

## Routing against the adjacent venues

| Your project's center of gravity | Better home | Why not COLM |
|---|---|---|
| A training method, data effect, evaluation artifact, inference algorithm, or safety property *of LMs* | **COLM** | — |
| A linguistic phenomenon, an NLP task, an annotation resource, a multilingual application | ACL or EMNLP | The finding is about language or a task, not about the model class |
| A representation-learning idea tested beyond language (vision, RL, graphs) | ICLR | Generality is the point; the LM is one instance |
| A learning-theoretic result, an optimizer, a probabilistic method where LMs are one benchmark | NeurIPS or ICML | The LM is an experiment, not the subject |
| A serving/systems contribution (kernels, scheduling, memory) with modeling untouched | MLSys or a systems venue | Reviewers there can evaluate throughput claims properly |
| An early-stage probe, negative result, or position piece not ready for archival review | A COLM or *CL workshop | Archival COLM review will demand completeness the work does not have yet |

Boundary cases worth naming: **multimodal models** fit COLM when the language model
is central to the question (a 2025 Outstanding Paper is a VLM-failure analysis);
**agents and tool use** fit when the paper studies the LM's behavior in the loop
rather than ships a product; **benchmark papers** fit when the benchmark comes with a
validity argument, not just difficulty.

## COLM's declared lanes (2026 CFP, checked 2026-07-08)

The CFP's non-exhaustive topics cluster into lanes; name yours before framing:

- **Training** — fine-tuning, instruction tuning, reinforcement learning, prompt
  tuning, in-context learning.
- **Data** — corpora and curation for pre-training, post-training, every stage.
- **Evaluation** — static and dynamic benchmarks, simulation environments, scalable
  oversight, protocols and metrics, human and machine evaluation, bias/equity/misuse
  measurement.
- **Safety** — security, privacy, misinformation, adversarial attacks and defenses.
- Plus inference/generation, interpretability, and multimodal LM work, all visible in
  the accepted lists of 2024-2025.

The award lineage (see `resources/exemplars/library.md`) tilts toward measurement,
analysis, and evaluation critique: five of the eight Outstanding Papers from the
first two editions study *how we know what LMs do*. A single leaderboard table is a
weak spine here.

## The young-venue calculus

Choosing a three-edition-old conference is itself a decision. Weigh it explicitly:

```text
FOR COLM                                  AGAINST (for this project)
- reviewer pool self-selected for LM      - no long citation tail yet; some
  work; less "why not test on vision?"      committees still ask "is COLM top-tier?"
- award lineage rewards analysis and      - norms shift per edition (policies,
  measurement, not only SOTA                dates, format have all moved 2024→2026)
- one cycle per year, October venue,      - one cycle per year: a reject costs 12
  proceedings free and open on              months at this venue
  OpenReview
```

The single-cycle point cuts both ways: COLM's March-to-July pipeline sits neatly
between the ICLR (autumn) and NeurIPS (spring) deadlines, which is why many groups
now treat it as the natural resubmission target for strong-but-rejected LM papers —
plan the fallback chain, not just the first shot.

## Vignette: one project, three venues

A group builds a retrieval-augmented clinical-notes summarizer and observes that
retrieved passages change the model's factuality unevenly across note types. Three
papers hide in this project:

- The *system* — architecture, deployment, clinician study → a clinical-NLP or
  applications track (ACL/EMNLP territory).
- The *task result* — new SOTA on a summarization benchmark → weak everywhere as a
  sole contribution, and weakest at COLM.
- The *phenomenon* — retrieval shifts factuality via an identifiable mechanism,
  measured across model families with contamination-controlled evaluation → this
  is the COLM paper, and notice the clinical domain has become incidental.

The exercise generalizes: the COLM-shaped paper inside a project is usually found
by asking what you now know about language models that you did not know before the
project — then testing whether that knowledge survives on models you did not build
the system around.

## Commit checklist before writing

- State the one-sentence finding *about language models* that survives model-name
  deletion.
- Name the CFP lane and the two nearest COLM accepted papers (2024 or 2025 lists)
  your work will be shelved next to.
- Confirm the evidence plan can clear the venue's measurement bar: pinned models,
  contamination discussion, uncertainty over runs (`colm-experiments`).
- Confirm the project can be told in 9 pages of main text — the 2026 cap is strict.
- Check the current CFP; COLM's scope wording is young enough to move between
  editions.

## Output format

```text
[Routing] COLM / ACL-EMNLP / ICLR / NeurIPS-ICML / systems venue / workshop first
[Object-of-study test] passes / fails — <what the LM is in this project>
[CFP lane] training / data / evaluation / inference / safety / interpretability
[Nearest COLM neighbors] <two accepted papers>
[Young-venue risk accepted] yes / no — <one-line reason>
[Next action] <framing fix, evidence fix, or venue switch>
```
