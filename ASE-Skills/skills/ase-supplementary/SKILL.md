---
name: ase-supplementary
description: Use when deciding what belongs in the 10-page ASE (IEEE/ACM Automated Software Engineering) paper body versus the artifact and supplementary material, splitting content by decision-criticality so nothing that decides acceptance lives outside the reviewed pages under the 10+2 budget.
---

# ASE Supplementary

Split content by **decision-criticality**. ASE gives you **10 pages** of body (plus 2 for
references), and reviewers judge the paper on those pages. The artifact and any supplementary
material *support* reproduction and reuse — they do not carry the argument. The failure mode is
exiling a decision-critical result to the artifact and assuming reviewers will dig for it; they
judge what is in the body.

## The decision-criticality rule

- **In the body (must be within 10 pages):** anything a reviewer needs to accept the paper — the
  automated task, the technique, the headline results on real subjects, the closest baseline
  comparison, the key ablation, and the central threats argument.
- **In the artifact / supplement:** everything needed to *reproduce or reuse* — full configurations,
  complete result tables, extra subjects, proofs, additional plots, raw logs, and cached model
  outputs.

If a result decides acceptance, it lives in the body even if space is tight; cut elsewhere.

## What each container is for

| Content | Where | Why |
|---|---|---|
| Task, technique, headline evaluation, closest-baseline comparison, key ablation | Body (≤10 pp) | Decision-critical; reviewers score these |
| Central threats-to-validity argument | Body | Construct/oracle validity is judged, not reproduced |
| Data Availability Statement | Body, after Conclusions, inside 10 pp | Mandatory and reviewed |
| Full config files, seeds, environment | Artifact | Reproduction detail, not an argument |
| Complete/extra result tables, extra subjects | Artifact / supplement | Support, not headline |
| Proofs, derivations too long for the body | Artifact / supplement (if the venue permits) | Verification detail |
| Raw logs, cached LLM outputs, dataset snapshots | Artifact | Provenance and reuse |

## The reviewer-behavior reality

- Reviewers may open the artifact to check a claim, but they will **not reconstruct a headline
  result** from raw logs. State every acceptance-deciding number in the body with a pointer to where
  the artifact backs it.
- A pointer to the artifact is a promise the body's claim is verifiable — not a substitute for
  stating the claim.
- Keep the body **self-contained**: a reader who never opens the artifact should still be able to
  judge the contribution.

## Anonymity across containers

- The supplement and artifact are part of the double-anonymous submission: scrub tool names that
  encode your identity, repository owners, and file paths.
- A result table in the artifact that reveals your institution's cluster paths is as much a leak as
  a name on the PDF.

## Space-recovery moves (before cutting content)

```text
[Figures]  merge redundant plots; one figure that carries the argument beats three that decorate.
[Tables]   move exhaustive per-subject tables to the artifact; keep the summary with effect sizes.
[Prose]    delete literature-tour sentences; related work is a delta argument, not a survey.
[Config]   move full configurations to the artifact; keep the one setting that matters in the body.
[Roadmap]  cut over-signposting; the arc should be visible without a paragraph announcing it.
```

## Output format

```text
[Decision-critical in body?] task / technique / headline results / baseline / key ablation / threats — all present within 10pp?
[Data Availability] in body, after Conclusions, inside 10pp?
[Artifact-only] configs / extra tables / proofs / logs / cached outputs -> not decision-critical?
[Self-contained] judgeable without opening the artifact? yes/no
[Anonymity] supplement + artifact scrubbed of identity? yes/no
```
