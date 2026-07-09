---
name: mobisys-artifact-evaluation
description: Use when packaging a MobiSys artifact for the Artifact Evaluation Committee — choosing among the three independent ACM badges (Available, Evaluated–Functional, Results Reproduced), building the workflow scripts the single-blind AEC runs on its own machines, and providing a hardware-optional path for evaluators who lack the exact phone, wearable, or board.
---

# MobiSys Artifact Evaluation

Use this for the MobiSys artifact submission. MobiSys has a strong, **script-first** artifact
culture: the single-blind AEC runs the authors' workflow scripts on the reviewers' own
systems, so an artifact that only works on your bench is not an artifact.

## The three ACM badges

Authors may seek one, two, or all three independent badges; passing badges are printed on the
paper and recorded in the ACM DL:

| Badge | What it certifies | What the AEC does |
|---|---|---|
| Artifacts Available | The artifact is publicly archived at a stable location | Checks the archival link and license |
| Artifacts Evaluated — Functional | The artifact runs and does what the paper says | Runs your workflow scripts on the AEC's machines |
| Results Reproduced | Key paper results are reproduced independently | Regenerates headline numbers/figures from your package |

Choose badges as **claim calibration**: *Available* is a release commitment; *Functional*
needs a runnable package; *Results Reproduced* needs the headline device results to come back
on machines you do not control — the hardest badge for on-device work.

## Artifact plan

- Decide what evidence supports each badge: source, build scripts, model files, workload
  traces, and the measurement/plotting pipeline.
- Provide a **top-level workflow script** and a README that orients an evaluator in one minute:
  environment, dependencies, one command to smoke-test, one to reproduce a headline figure,
  expected outputs, and runtime.
- Anonymize repository history, paths, screenshots, notebook metadata, license headers, and
  device serial numbers for the review round; de-anonymize only at camera-ready.
- Pin framework, runtime, and model checkpoint hashes; on-device results drift across
  framework minor versions.

## The hardware-optional path (the MobiSys-specific move)

On-device artifacts fail *Functional* most often because the evaluator lacks the exact phone,
wearable, or board. Design for that from the start:

```text
Hardware-optional package layout:
  /device      full pipeline for the exact hardware (Results Reproduced target)
  /emulated    downscaled or emulator path an evaluator can run without the device
  /logs        recorded runs so plots regenerate even if nothing executes
  /README      states which claims each path can and cannot reproduce
```

State plainly which headline numbers the emulated path *cannot* reproduce (typically absolute
energy and thermal behavior) so the AEC grades the right badge instead of failing the whole
package.

## What AEC reviewers open first

- The README and the top-level workflow script — if these do not run cleanly, the badge stalls
  regardless of how good the system is.
- The one-command smoke test — make it fast and hermetic.
- The plotting pipeline for a headline figure — emit figures directly from logged results so
  the paper numbers and artifact numbers cannot drift.

## Calibration anchors

- Artifact evaluation is single-blind and separate from paper review; the badge names and the
  artifact deadline are cycle-specific — verify against the current Artifact Evaluation page
  rather than past years.
- Absolute on-device energy and latency are the least portable results; scope
  *Results Reproduced* claims to what survives on another evaluator's hardware.

## Output format

```text
[Badges sought] Available / Functional / Results Reproduced
[Package contents] <source/scripts/models/traces/plotting>
[Hardware-optional path] present? which claims it cannot reproduce
[Anonymity risks] <paths/screenshots/serials/repo owners>
[Reproduction level] turnkey / scripted / descriptive / weak
[Fixes before upload] <ordered list>
```
