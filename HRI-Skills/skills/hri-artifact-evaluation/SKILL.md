---
name: hri-artifact-evaluation
description: Use when packaging the artifacts of an accepted ACM/IEEE HRI paper — code, robot behaviors, de-identified data, and study materials — for openness and any ACM badges the edition offers, while being honest about the limits of reproducing an embodied human-subjects study.
---

# HRI Artifact Evaluation

HRI's artifact and reproducibility culture is **less formalized than software-engineering venues'**:
there is not a long-standing, uniformly enforced ACM artifact-badge track at every HRI edition, and
whether a given year runs a formal reproducibility/artifact evaluation is **待核实 per cycle**. So
treat artifact work at HRI as a **credibility and openness** move first, and follow a formal badge
process only if this edition offers one. Either way, the artifact of an HRI paper is unusual: it is
the **study**, not a runnable system that reproduces a number. This skill packages it honestly. It
builds on `hri-reproducibility` and the shared kit in
[`../../resources/code/README.md`](../../resources/code/README.md).

## First: does this edition run a formal evaluation?

- Check the current call for a **reproducibility/artifact track**, its badges, and its own deadline
  (**待核实**). If it exists, follow its instructions exactly.
- If ACM badges are offered, they follow the ACM scheme (Artifacts Available / Evaluated -
  Functional / Reusable / Results Reproduced). Map your package to whichever the edition supports.
- If no formal track runs, **still** release an open, well-documented artifact — reviewers and
  readers reward it, and it is the community norm even without a badge.

## What an HRI artifact actually contains

Because the core evidence is a human study of an embodied robot, the artifact is rarely a
one-command reproduction. Assemble:

- **Study materials** — questionnaires (items + scoring), interview guides, task scripts, consent-form
  summary, and coding schemes.
- **Robot-behavior specification** — the conditions/behaviors the robot exhibited: for autonomous
  behavior, the software version and parameters; for **Wizard-of-Oz**, the wizard's action space,
  protocol, and error rates (see `hri-experiments`).
- **De-identified data** — participant-level data with identifiers removed, plus a codebook.
- **Analysis code** — scripts that regenerate every reported statistic, figure, and table from the
  shared data, with pinned dependencies and fixed seeds.
- **Pre-registration** pointer and any deviation notes.

## Make it reusable, within honest limits

- **Reproducible = re-analyzable + re-runnable-as-a-method.** An evaluator should be able to
  regenerate your results from the shared data and to understand the procedure well enough to run the
  study again — **not** to recreate your exact human responses. State this scope plainly.
- **Document the environment.** For analysis code, a `README` with dependency versions and a single
  entry point; a container helps if the toolchain is heavy.
- **License it** (an OSI-approved code license; a documented data-use/consent basis for the data).
- **Archive with a DOI** (OSF, Zenodo, figshare, or Software Heritage) rather than a personal
  homepage, so the link is permanent and citable.

## Human-subjects constraints on the artifact

An HRI artifact contains **people**, which limits what can be shared:

- Share only data/media the participants **consented** to share for that use; if consent for public
  data or video was not obtained, share what you can and **explain the gap** honestly.
- **De-identify** thoroughly — free-text responses and video are the usual re-identification risks.
- Vulnerable-population studies (children, older adults, clinical) may permit little sharing; say so
  rather than force an unethical release.
- A partial, honest artifact with a clear rationale beats an over-shared one that breaches consent.

## Camera-ready badge mechanics (if applicable)

- Badges, when a paper earns them, are displayed on the published version — coordinate with
  `hri-camera-ready` so any badge and the archive DOI appear correctly.
- Keep the **anonymized** review-time archive and the **de-anonymized** public archive separate; the
  public one carries author names, the review one must not.

## Anti-patterns

- **Overclaiming** a "reproducible" human study as if it re-runs like a benchmark.
- **"Data available on request"** — treated as unavailable.
- **Unlogged Wizard-of-Oz** — the stimulus cannot be reproduced.
- **Identifiable data or video** released without consent for that use.
- **Chasing a badge that does not exist** this cycle instead of simply releasing a good artifact.

## Output format

```text
[Formal track?] does this edition run artifact/reproducibility evaluation + badges? (verify)
[Artifact contents] materials · robot-behavior spec (incl. WoZ) · de-identified data + codebook · analysis code
[Reproducibility scope] re-analysis + method replication; human responses framed as not re-runnable
[Openness] DOI archive · license · honest statement of consent-limited gaps
[Human-subjects] de-identified · shared only what consent allows
[Badge readiness] (if offered) which ACM badge(s) targeted · public vs review archive separated
[Fix queue] <ordered>
```
