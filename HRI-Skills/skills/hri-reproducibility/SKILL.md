---
name: hri-reproducibility
description: Use when building the openness and replicability story for an ACM/IEEE HRI full paper — sharing study materials, robot-behavior specifications, de-identified data, and analysis code; reporting Wizard-of-Oz and pre-registration; and stating honestly what can and cannot be reproduced in an embodied human-subjects study.
---

# HRI Reproducibility

Reproducibility means something specific — and harder — at HRI than at a benchmark-driven venue. You
cannot "re-run" a study of an embodied robot and real people the way you re-run a model on a test
set: the participants, the room, the exact robot, and the moment are gone. So HRI reproducibility is
about making the **procedure, stimulus, and analysis** transparent enough that another team could
**replicate the method** and readers can audit your inferences. This skill builds that story; it
pairs with the shared kit in [`../../resources/code/README.md`](../../resources/code/README.md).

## What "reproducible" can and cannot mean here

Be honest about the limits, and design the artifact around what *is* reproducible:

- **Reproducible (aim for this):** the **study protocol**, the **robot behavior/stimulus**, the
  **measures**, the **analysis code**, and the **de-identified data** — enough to re-analyze your
  results and to run the same study elsewhere.
- **Not reproducible (say so):** the exact human responses. A replication is a *new* sample; framing
  it otherwise overclaims. State this plainly rather than let a reviewer catch the overclaim.

## The replication package for an HRI study

Assemble, and reference from the paper:

- **Study materials** — consent-form summary, instructions/scripts, questionnaires with exact items
  and scoring, interview guides, and coding schemes for qualitative work.
- **Robot-behavior specification** — the behaviors/conditions the robot exhibited, at enough
  granularity to reproduce the *stimulus*: for autonomous behavior, the software version and
  parameters; for **Wizard-of-Oz**, the wizard's action space, protocol/script, and error rates
  (see `hri-experiments`).
- **De-identified data** — participant-level data with identifiers removed, plus a codebook. Scrub
  free-text and metadata that could re-identify participants.
- **Analysis code** — scripts that reproduce every reported statistic, figure, and table from the
  shared data, with fixed seeds and pinned dependencies.
- **Pre-registration** — a link/ID if you pre-registered the hypotheses and analysis, with any
  deviations documented.

## Report the things that make a study re-runnable

- **Sample and procedure** in reproducible detail: recruitment, inclusion criteria, N and how it was
  determined, session flow, timing, compensation.
- **Apparatus**: the robot platform and version, sensors, environment, and anything that would change
  the interaction if swapped.
- **Wizard-of-Oz disclosure** and constraints, so the stimulus is not an unlogged human performance.
- **Analysis decisions**: exclusions and why, transformations, the exact tests, and the
  confirmatory/exploratory split.

## De-identification and the video

HRI artifacts contain **people**, which raises obligations a code-only artifact does not:

- **De-identify data** before sharing; get consent for data sharing at study time — retrofitting it
  is usually impossible.
- The **video figure** and any recordings need consent for the *use you are making* (review-time
  sharing, public archival, or conference presentation are different permissions). For review, blur
  faces and mute identifying audio if consent for public use was not obtained (see
  `hri-supplementary`).
- Vulnerable populations (children, older adults, clinical) demand extra care in what is shared at
  all.

## Openness at HRI (calibrated to the venue)

HRI's open-science and artifact-badge culture is **less formalized than SIGSOFT's** — there is not a
long-standing, uniformly enforced ACM badge track for every edition (**待核实** per cycle). So treat
openness as a **credibility and community-norm** move, not a checkbox:

- Share what ethics allows via a DOI-issuing archive (e.g., OSF, Zenodo, figshare); avoid a personal
  homepage link that both rots and de-anonymizes.
- Where confidentiality or human-subjects constraints prevent full sharing, **say what and why** —
  an honest limitation reads far better than silence or "available on request."
- If the edition *does* run an artifact/reproducibility evaluation, follow it and see
  `hri-artifact-evaluation`.

## Anonymization for double-blind

Everything above must be **anonymized at review time**: strip author/institution names from
materials and code, host the archive behind an anonymizing view, and scrub the video and data of
identity leaks. See `hri-submission` for the mechanical sweep.

## Anti-patterns HRI reviewers flag

- **Overclaiming reproducibility** — implying a human study can be exactly re-run.
- **Unlogged Wizard-of-Oz** — no way to reproduce the stimulus.
- **"Data available on request"** — treated as not available.
- **Identifiable data or video** shared without consent for that use.
- **Analysis not reproducible from the shared data** — figures that no script regenerates.

## Output format

```text
[Repro scope] procedure/stimulus/analysis reproducible? human responses correctly framed as not?
[Package] materials · robot-behavior spec (incl. WoZ) · de-identified data + codebook · analysis code
[Pre-registration] link/ID · deviations documented?
[De-identification] data scrubbed · video/audio consent for the use made?
[Openness] DOI archive · honest statement of what cannot be shared and why
[Anonymization] materials/code/archive/video anonymized for review?
[Fix queue] <ordered>
```
