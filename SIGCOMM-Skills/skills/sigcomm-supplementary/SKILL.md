---
name: sigcomm-supplementary
description: Use when organizing the material around an ACM SIGCOMM paper — deciding what lives in the 12-page body versus references versus optional appendices, keeping the main paper self-contained, anticipating the shepherd's appendix-necessity approval, and placing extended measurements and proofs outside the cap without hiding load-bearing content.
---

# SIGCOMM Supplementary

Use this when splitting a SIGCOMM paper across body, references, and appendices. The controlling
rule: the 12 single-spaced pages before references must carry the argument on their own;
appendices and references sit outside the cap but do not rescue an incomplete body. Reopen the
current CFP to confirm this edition's appendix handling.

## What goes where

- **Body (≤ 12 single-spaced pages, figures and tables included):** the measured problem, the
  design principle, the mechanism, and the decision-critical evaluation. A reviewer must
  understand and believe the contribution without turning to an appendix.
- **References (outside the cap):** as many as needed; never trimmed for space or anonymity.
- **Appendices (optional, after references, outside the cap):** extended measurement sweeps,
  additional topologies, proofs or derivations, detailed configuration, and workload
  specifics — support, not substitute.

## The appendix-necessity rule changes the calculus

Unlike venues where appendices are a free overflow bin, SIGCOMM's **shepherd approves whether
each appendix is necessary** at camera-ready. Write appendices you can defend as load-bearing,
and never park a step the argument depends on where a shepherd might cut it. A safe test: if
removing an appendix would make a body claim unverifiable, that content probably belongs in
the body or the artifact, not in a droppable appendix.

## Placement table

| Content | Home | Why |
|---|---|---|
| The core mechanism and its principle | Body | The contribution reviewers evaluate |
| The one or two decision-critical figures | Body | The evidence the accept/reject turns on |
| Extra topology / parameter sweeps | Appendix | Depth without crowding the 12 pages |
| Full configuration and workload spec | Appendix or artifact | Reproducibility detail, referenced from the body |
| Proof or derivation for an analytical claim | Appendix | Body keeps the statement and a sketch |
| Raw logs and per-run tables | Artifact | Never the paper's job to hold these |

## Keep the body self-contained

- Every appendix and artifact item must be **cross-referenced from the body** at least once;
  orphaned supplementary material is invisible and, at camera-ready, deletable.
- Order appendix sections to mirror the body's flow so a reader navigates by section, not by
  hunting.
- State results in the body and defer only the *support* — a reader who never opens an
  appendix should still be able to reconstruct why the contribution holds.

## Vignette: splitting a congestion-control paper

A submission proposes a new congestion signal with a testbed evaluation and a small stability
argument. The body keeps the measured motivation, the signal and its principle, the two
decision-critical tail-latency figures, and a one-paragraph stability sketch. The appendix
holds the full stability derivation, a switch-buffer sweep, and the fairness-across-flows
tables; the artifact carries the driver and logs. Nothing the accept decision depends on lives
only in a droppable place.

## Output format

```text
[Body self-contained] yes / no (what breaks without an appendix)
[Body budget] within 12 single-spaced pre-reference pages? yes/no
[Placement map] <content -> body / appendix / artifact>
[Appendix necessity] each appendix defensible to a shepherd? yes/no
[Cross-reference gaps] <orphaned supplementary items>
```
