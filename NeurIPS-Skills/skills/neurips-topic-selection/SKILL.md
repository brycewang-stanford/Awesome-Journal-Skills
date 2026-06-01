---
name: neurips-topic-selection
description: Use when deciding whether a paper belongs at NeurIPS, choosing main-track versus another NeurIPS track, selecting contribution type, or rerouting to a better AI/ML venue.
---

# NeurIPS Topic Selection

Use this skill before committing to NeurIPS. The target is not "any good AI paper"; it is a paper
whose contribution will matter to the NeurIPS reviewer community and survive the current official
track rules.

## Fit signals

Strong NeurIPS candidates usually have one of these cores:

- a general ML method, model, objective, optimization, inference, or learning principle;
- a theory result that changes understanding of ML behavior or limits;
- a high-quality empirical finding about models, data, evaluation, robustness, or scaling;
- a use-inspired result with a real scientific, social, health, robotics, sustainability, or
  creative-AI problem and a clear ML contribution;
- a dataset, benchmark, or evaluation contribution that belongs in the correct current NeurIPS
  track rather than being forced into main track;
- a rigorous negative result that changes community understanding.

## Poor fit signals

- Engineering integration without a research insight.
- Domain application where the ML contribution is ordinary.
- Benchmark improvement without mechanism, error analysis, or generality.
- Safety, fairness, or societal claim with thin evidence.
- Reproduction or replication study better suited to MLRC/TMLR.
- Dataset or evaluation paper that should use the E&D track.
- Position argument that should use the Position Papers track.

## Contribution-type choice

Choose the contribution type that changes reviewer expectations. A theory paper should make proofs
central. A use-inspired paper needs a real task and ML novelty. A concept-and-feasibility paper
needs high-risk/high-reward framing and credible preliminary evidence. A negative-results paper
needs a lesson that matters beyond one failed run.

## Output format

```text
[Fit] High / Medium / Low
[Recommended track] Main / E&D / Position / MLRC / workshop / other venue
[Contribution type] General / Theory / Use-Inspired / Concept & Feasibility / Negative Results
[Why NeurIPS] <one sentence>
[Main upgrade needed] <evidence, framing, related work, artifact, ethics, or reroute>
```
