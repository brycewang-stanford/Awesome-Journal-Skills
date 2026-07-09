---
name: wacv-artifact-evaluation
description: Use when packaging code, data, and models for a WACV paper, covering the anonymous review artifact versus the public post-acceptance release, reproducing constraint-based applications claims (latency, power, robustness) not just accuracy, dataset licensing and release, and keeping the artifact in sync across the two-round Revise-and-Resubmit lap.
---

# WACV Artifact Evaluation

Use this to build the two artifacts a WACV paper needs: a **sealed anonymous package** for
review and a **public release** after acceptance. WACV's applications framing means the
artifact must let a reviewer reproduce a *deployed* claim, and the two-round model means the
artifact must survive a revision. Facts are the WACV 2026/2027 cycles as read on 2026-07-09.

## Two artifacts, two audiences

| | Anonymous review artifact | Public post-acceptance release |
|---|---|---|
| Audience | Double-blind reviewers | The community, via CVF open access + IEEE Xplore paper |
| Identity | Fully anonymized: no author names, repos, or org strings | De-anonymized; real repo, license, and citation |
| Contents | Enough to reproduce the headline claims | Full code, weights, and dataset (or access instructions) |
| Timing | With the submission / supplement | By the camera-ready obligation (see `wacv-camera-ready`) |

Do not ship the review artifact with a link to a named GitHub repo or a project page — that
breaks double-blind. Ship the code and a runnable path inside the anonymized package.

## Reproduce the claim, not just the metric

For an Applications-track paper the headline is usually a constraint ("runs at 2 W on device
D under sub-10-lux"), and an artifact that only reproduces an accuracy number does not
support that claim. Include what a reviewer needs to check the *systems* result:

```text
Applications artifact must let a reviewer:
  1. Run the model and reproduce the headline metric within the stated spread.
  2. Measure (or see logged) the constraint: latency/wattage/memory on the named device.
  3. Re-run at least one baseline under the same constraint, to confirm the comparison.
  4. Do all of this without learning who the authors are.
```

## Datasets and licensing

If a dataset is a claimed contribution, plan its **public availability** for the release and
state the license (and any collection/consent basis for field or human data). In the
anonymous artifact, provide the data or a de-identified sample that reproduces the reported
rows without revealing the collecting institution. Do not defer the license decision to the
last day — an unlicensed dataset is not really released.

## Sync across the two rounds

A Revise-and-Resubmit revision often adds an experiment or re-tunes a baseline; the artifact
must move with it. Before resubmitting to Round 2, re-run the reproduction on the revised
claims and diff the artifact's outputs against the revised paper. A reviewer who finds the
Round 2 artifact reproducing the Round 1 numbers will read it as an unfinished revision.

## Reverify each cycle

- The camera-ready dataset/code-release obligation and its deadline.
- Anonymity rules for artifacts submitted with review (待核实 size/format caps for 2026).
- Any license or ethics requirements for released data.

## Output format

```text
[Artifact stage] anonymous review / public release
[Anonymized] no names/repos/org strings in review artifact: yes/no
[Claim reproducible] headline metric within spread: yes/no
[Constraint reproducible] latency/power/memory checkable on named device: yes/no
[Baseline] at least one baseline re-runnable under the constraint: yes/no
[Dataset] license + public-availability plan set: yes/no
[Round sync] artifact matches revised paper: yes/no
```
