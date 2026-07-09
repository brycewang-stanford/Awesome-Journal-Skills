---
name: ecai-artifact-evaluation
description: Use when planning the reproducibility/artifact story for an ECAI paper — noting that ECAI/FAIA has NO ACM/IEEE-style artifact-badging committee, so credibility is carried by the paper and its supplement and judged by the same reviewers, and adapting an ML-style reproducibility package (or a complete proof appendix for theory work) to that reality.
---

# ECAI Artifact Evaluation

Start with a correction that saves authors from importing the wrong workflow: **ECAI does not run an
ACM/IEEE-style artifact-evaluation track with a separate badge committee.** There is no
"Artifacts Available / Functional / Reusable / Reproduced" pipeline as at ACM SIGSOFT venues, and
no separate artifact deadline to hit after acceptance. In ECAI, the reproducibility story is
**carried by the paper and its supplement and judged by the same reviewers** who read the paper,
during the one review round.

That makes the "artifact" a **submission-time asset**, not a post-acceptance badge chase. Its job is
to make the reviewer trust the claim inside a 7-page body. (Confirm on the current call whether the
edition adds any optional reproducibility checklist or appendix mechanism — this is **待核实** per
cycle and can differ between a standalone ECAI and the joint IJCAI-ECAI 2026.)

## Match the artifact to the contribution shape

ECAI is a **general-AI** venue, so "artifact" means different things:

| Contribution shape | The credibility artifact is... |
|---|---|
| Theory / KR / argumentation | A **complete proof appendix** (full proofs the body only sketches) plus, if applicable, a reference solver/encoding |
| Planning / search / optimization | The **domain files, instances, seeds**, and a runnable implementation reproducing the reported node/quality numbers |
| Machine learning | Code, data (or a loader), configs, seeds, and **cached outputs** so results reproduce without live API calls |
| Multi-agent systems | The environment, agent code, and the exact evaluation protocol (episodes, seeds, metrics) |
| Applied AI (PAIS) | Enough of the pipeline and (sanitized) data to make the **deployment claim** credible |

## What "good" looks like at review time

- **Anonymized.** The supplement is read under double-blind review; strip repository owners,
  institution names, and system names that identify you (`ecai-submission`).
- **Self-contained.** A reviewer opens it once, in a short window; it must run or be readable
  without chasing dependencies or your lab's private data.
- **Decision-critical content stays in the body.** The supplement holds *support* (full proofs,
  extra tables, code) — not the claim itself. Nothing a reviewer needs to *judge* the paper may
  live only in the supplement (`ecai-supplementary`).
- **Proportional.** Match effort to the claim: a theory paper's artifact is a rigorous proof
  appendix, not a Docker image; an empirical paper's artifact is a runnable, seeded package.

## A pragmatic checklist (adapt, don't badge-chase)

```text
[ ] Full proofs present for every theorem the body sketches (theory work)
[ ] Code runs from a clean checkout with a documented entrypoint (empirical work)
[ ] Data included or a script fetches a versioned public source; seeds fixed
[ ] Cached model/API outputs included so results do not re-sample at run time
[ ] A short README maps each paper claim/table -> the file that reproduces it
[ ] Archive anonymized: no owner, institution, funding, or system-name leaks
[ ] Total size and runtime reasonable for a reviewer's one-pass read
```

## Do not import the wrong machinery

- **No ACM/IEEE badges.** Do not promise "Artifacts Evaluated - Reusable" or design around a badge
  committee — none exists at ECAI. Credibility is reviewer-judged, in-band.
- **No separate artifact-track deadline.** Everything ships with the paper (abstract 12 Jan / paper
  19 Jan for IJCAI-ECAI 2026); there is no later artifact submission.
- **Not a leaderboard.** ECAI values understanding (a proof, a fair comparison) over a single
  benchmark number; an artifact that only re-prints a leaderboard score misses the venue's bar
  (`ecai-experiments`).

## Post-acceptance: make it permanent and open

Once accepted, convert the anonymized supplement into a **permanent, open** release to match ECAI's
open-access ethos:

- Deposit code/data in a DOI-issuing archive (e.g. Zenodo/Software Heritage) with an open license.
- De-anonymize repository owners and restore acknowledgements (`ecai-camera-ready`).
- Put the permanent link in the camera-ready so the open-access paper points to a stable artifact.

## Output format

```text
[Artifact type] proof appendix / runnable code+data / environment+protocol / deployment pipeline
[Anonymity] clean / leaks: <where>
[Claim map] each theorem/table -> proof or reproducing file
[Self-containment] runs/readable in one pass? missing deps: <list>
[Reality check] no ACM/IEEE badge assumed; nothing decision-critical hidden in the supplement
[Post-acceptance] DOI archive + open license + de-anonymized link planned for camera-ready
```
