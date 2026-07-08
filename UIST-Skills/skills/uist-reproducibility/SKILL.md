---
name: uist-reproducibility
description: Use when making a UIST paper's results replicable — reporting implementation parameters and measurement protocols so a lab could rebuild the system, specifying hardware down to parts and calibration, logging technical evaluations deterministically, and writing honest availability statements for interface systems.
---

# UIST Reproducibility

Reproducibility at UIST means something different from rerunning a training script:
the question is whether a competent lab could **rebuild the artifact and reproduce
its measured behavior**. That decomposes into three ledgers — build, measurement,
and study — and most UIST papers under-specify a different one than they think.
UIST posts no reproducibility checklist (none found for 2026 — 待核实), so this
discipline is self-imposed and reviewer-enforced.

## The build ledger: could they make one?

Everything the system's behavior depends on, pinned:

- **Software**: exact framework and driver versions, OS, lockfiles; for anything
  learned, model checkpoints and training data provenance.
- **Hardware**: part numbers (not "an IMU" but which IMU), mechanical tolerances
  that matter, firmware version, and the calibration routine with expected outputs.
- **Environment**: the physical conditions the system assumes — lighting range,
  acoustic environment, mounting geometry, surface materials.
- **Magic numbers**: every threshold, filter coefficient, debounce window, and
  gain, with how each was set (tuned by hand? on which data?). These constants are
  where re-implementations actually fail.

## The measurement ledger: could they get your numbers?

A latency or accuracy figure is reproducible only with its protocol:

| Reported number | Must be pinned |
|---|---|
| Latency | Measurement boundary (sensor-to-photon? software-only?), instrument, event count, load conditions |
| Recognition accuracy | Dataset splits, per-user vs pooled, session separation, chance level |
| Tracking error | Ground-truth apparatus and its own accuracy, spatial sampling grid |
| Throughput / bitrate | Task, phrase set or corpus, session and rest structure |
| Power / weight / cost | Configuration measured, currency and date for cost |

Automate the protocol: a measurement harness checked into the supplement converts
"trust me" into "run this" (see `uist-artifact-evaluation` for packaging).

```bash
# eval/rerun.sh — regenerate every reported number from raw logs
python analyze_latency.py logs/latency_10k.jsonl --out tables/table1.csv
python analyze_accuracy.py logs/study/ --split per-user --seed 17 --out tables/table2.csv
diff -u tables/table1.csv paper_tables/table1.csv   # drift check against the PDF
```

Log at the event level with timestamps and raw sensor values, not just computed
outcomes — future you, rebuttal you (see `uist-author-response`), and replicating
labs all consume the same logs.

## The study ledger: could they rerun the human part?

For any user evaluation: full task instructions and stimuli, counterbalancing
scheme, practice/rest structure, apparatus placement (photograph it),
inclusion/exclusion criteria, compensation, and the analysis scripts from raw logs
to reported statistics. Share instruments even when raw human data cannot leave the
IRB envelope — protocol transparency and data availability are separable, and
saying so precisely is the honest move.

## The availability statement

Write one even though UIST does not require a template, and make it specific:

```text
GOOD: "Firmware, PCB design files, BOM, and the measurement harness are at
      <archive-DOI> (tag: as-published). The gesture corpus (14 of 16
      participants consented to release) is included; per-participant raw
      video is withheld under IRB #—. The two commercial tracking SDKs
      required are named in BUILD.md with tested versions."
BAD:  "Code available upon reasonable request."
```

Papers with learned components inherit ML reporting norms too — seeds, training
configs, compute — and can borrow the shared kit's checklists (see
[`../../resources/code/README.md`](../../resources/code/README.md)).

## Learned components inherit ML norms

When the system embeds recognition or generation models, the ML reporting
conventions stack on top of the systems ledgers:

- Seeds, splits, and training configs pinned; per-user vs pooled evaluation made
  explicit (interaction data is brutally user-dependent, and pooled splits
  inflate accuracy).
- For third-party or hosted models: exact model identifiers and versions, the
  full prompt set, decoding parameters, and dated transcripts — hosted models
  drift, so the logged behavior is the only permanent record of what reviewers
  saw.
- Report the interactive costs alongside accuracy: per-inference latency on the
  deployment hardware, and per-session cost for metered APIs; a technique that is
  reproducible but unaffordable to run is only half-replicable.
- The shared kit's checklists cover this lane; the adapter in
  `resources/code/README.md` scopes what it can and cannot check.

## The one-page REPRO.md

Compress the three ledgers into a single file at the archive root:

```markdown
# Reproducing <SystemName> (paper §6-7)
## Rebuild        parts: BOM.csv · firmware: v2.3 · calibration: docs/calib.md
## Environment    tested: indoor 200-800 lux, 18-26°C · assumes: mounted per Fig 4
## Constants      thresholds in config.yaml — tuned on pilot data (n=4), §5.2
## Remeasure      eval/rerun.sh regenerates Tables 1-2 from logs/ (or raw capture)
## Study          instruments/ · counterbalancing: latin square, §7.1 · IRB #—
## Known drift    accuracy drops outdoors (§9); p95 latency sensitive to BLE stack
```

The "known drift" line is the credibility multiplier: it tells replicators you
know where the envelope ends before they find out.

## Replication drift and its uses

When a rebuilt system misses the paper's numbers, the causes rank: unstated
environmental assumptions, hand-tuned constants, part substitutions, then genuine
bugs. Pre-empt the first two by stating the envelope and the tuning story in the
paper body — it costs three sentences and buys the paper years of credibility (and
Lasting Impact eligibility runs on decade-scale credibility).

## Output format

```text
[Build ledger] pinned / gaps: <software · hardware · environment · constants>
[Measurement ledger] protocols pinned for <k>/<n> reported numbers
[Study ledger] instruments · counterbalancing · analysis scripts — present?
[Availability statement] drafted? honest about withholdings?
[Top drift risk] <the unstated assumption most likely to break replication>
```
