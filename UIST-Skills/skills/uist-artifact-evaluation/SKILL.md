---
name: uist-artifact-evaluation
description: Use when packaging the artifacts behind a UIST paper — code, toolkits, hardware design files, and datasets — first as anonymous review-time evidence that the system is real, then as a public release engineered for reuse, in a venue with no formal badge committee doing the checking for you.
---

# UIST Artifact Evaluation

UIST has no artifact-evaluation committee or badge track (none was found for the
2026 cycle — 待核实 each year); the CFP-level instrument of proof is the video
figure. That absence raises rather than lowers the packaging bar: your artifacts are
judged twice, informally — at review time as *evidence the system exists as
claimed*, and after publication as *infrastructure other builders adopt*. Nobody
will certify either; both simply succeed or fail.

## What counts as the artifact, by paper type

| Paper type | Review-time artifact | Reuse-time artifact |
|---|---|---|
| Interaction technique | Reference implementation + demo scene | Portable library with the technique isolated |
| Toolkit / authoring system | Runnable toolkit + the example apps from the paper | Documented API, tutorials, package registry entry |
| Hardware / fabrication | Design files, firmware, BOM, assembly photos | Fab-ready files + sourcing notes + calibration guide |
| Sensing / recognition pipeline | Trained models + capture data + eval harness | Dataset with collection protocol + retraining scripts |
| Human-AI / LLM system | Prompts, orchestration code, pinned model IDs, logged transcripts | Same, plus cost and drift notes |

## Review-time packaging: the five-minute skeptic

A reviewer gives your supplement five minutes, anonymously, on a machine you don't
control. Optimize for that reader:

- One `README` at the archive root: what this is, which paper section each
  directory backs, and one command (or one video) per claim.
- Prefer a **recorded run alongside the code** for anything with hardware, drivers,
  or GPU dependencies — reviewers cannot rebuild your rig, so show the harness
  producing the paper's numbers.
- Pin everything (lockfiles, container image digests, model checkpoints); "latest"
  is a broken artifact by review week.
- Anonymize as strictly as the PDF: repository history, notebook authorship cells,
  hardcoded home paths, calibration files named after lab members (see
  `uist-submission` for the sweep).

```text
supplement.zip
├── README.md              # claim → artifact map; 5-minute quickstart
├── technique/             # core implementation, pinned deps
├── hardware/              # schematics, PCB, STL/STEP, BOM.csv, firmware/
├── eval/                  # harness + raw logs behind Tables 1-2
│   └── rerun.sh           # regenerates the paper's numbers from logs
├── media/                 # per-claim capture clips (beyond the video figure)
└── LICENSES.md            # third-party components and their terms
```

## Release-time packaging: engineering for strangers

At camera-ready (see `uist-camera-ready`), the audience flips from three skeptics
to an open-ended stream of builders:

1. **De-anonymize deliberately** — publish to the real org, restore attribution,
   add the paper citation and BibTeX to the README.
2. **Cut a release tag** matching the camera-ready ("as-published") so later
   development never orphans the paper's claims.
3. **Choose licenses by artifact class**: code (e.g. MIT/Apache-2.0), hardware
   designs (e.g. CERN-OHL), data (e.g. CC-BY) — one archive often needs all three,
   and institutional tech-transfer rules for hardware are worth checking early.
4. **Archive beyond the repo**: deposit the tagged release with a DOI service so
   the URL in the proceedings outlives your hosting choices.
5. **State the support posture** honestly in the README — "research prototype,
   issues welcome, no maintenance promised" is respectable; silence is not.

## What the informal evaluators open first

Order the package for actual reading behavior:

1. **README, thirty seconds.** If the claim → artifact map is not visible without
   scrolling, the evaluation is over.
2. **The media directory, two minutes.** Clips of the harness producing the
   paper's numbers get watched; they are the highest-credibility artifact per
   byte, especially for hardware.
3. **One quickstart command, two minutes.** Whatever you name in the README as
   "run this" will be run in a fresh environment; test it in a container or a
   colleague's clean machine, not your dev box.
4. **Source spot-checks.** Reviewers grep for the mechanism the paper claims is
   novel; if the "self-calibrating controller" is a 30-line stub, the paper's
   credibility inverts. Never ship scaffolding that contradicts the prose.

## Toolkit papers: adoption is the long evaluation

For toolkit and authoring-system contributions, the release *is* the deferred
evaluation, and small engineering choices compound:

- Publish to the ecosystem's registry (pip/npm/crates/Arduino library manager) —
  installability is adoption's first filter.
- Ship the paper's example applications as runnable starters; they are the
  tutorials people actually read.
- Keep the API surface documented at the level of the paper's abstractions, so
  citations of the toolkit describe your concepts in your vocabulary.
- Track downstream uses; a "built with X" list is both maintenance motivation
  and the evidence base for the retrospective the venue's decade-scale memory
  eventually invites.

## Hardware honesty

Physical artifacts cannot be uploaded, so their evidence standard is
reconstruction: exact part numbers with sources, tolerances that matter, assembly
sequence photos, firmware flashing instructions, and the calibration procedure with
expected readings. A paper whose device only the authors can build has published a
demo, not a contribution — reviewers from fabrication-heavy labs apply exactly that
test (see `uist-reproducibility` for the replication ledger).

## Output format

```text
[Artifact class] technique / toolkit / hardware / pipeline / hybrid
[Review package] five-minute test passes? claim→artifact map complete?
[Anonymity] archive-level sweep clean?
[Release plan] tag · licenses (code/hardware/data) · DOI deposit · support posture
[Gap list] <artifacts named in the paper but absent from the package>
```
