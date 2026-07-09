---
name: wacv-reproducibility
description: Use when strengthening the reproducibility of a WACV paper, covering the recipe ledger for constraint-aware systems, benchmark and split hygiene, seed and session honesty, device and power reporting for applications claims, and keeping the reproduction package in sync with the paper across the two-round Revise-and-Resubmit lap.
---

# WACV Reproducibility

Use this to make a WACV result checkable — by a reviewer now and by you at the Round 2
resubmission. WACV's applications framing raises the bar in one direction (a systems claim
must be reproducible *as deployed*), and the two-round model adds a second (paper and
artifact must not drift between rounds). Facts are the WACV 2026/2027 cycles as read on
2026-07-09.

## The recipe ledger

Keep one ledger that regenerates every reported number, so the body, the supplement, and the
artifact cannot diverge:

| Ledger entry | Why WACV cares |
|---|---|
| Exact data splits and preprocessing | Applications datasets are often custom; a hidden split invalidates a comparison |
| Seeds (and sessions/devices for field work) | Reviewers distrust single hero runs |
| Hyperparameters per reported row | Lets a reviewer see the comparison was matched |
| **Device, power meter, and measurement method** | An applications latency/wattage claim is only reproducible if the rig is named |
| Baseline re-tuning under your constraint | Proves the comparison was fair, not defaults-vs-yours |
| Script → figure/table mapping | So a Round 2 reviewer confirms nothing changed silently |

## Constraint-aware reproducibility

An Applications-track claim ("2 W, sub-10-lux, on device D") is not reproducible from
accuracy alone. Record how the constraint was measured — the meter, the device firmware, the
ambient condition — so a reviewer or a future reader can reproduce the *constraint*, not just
the metric. A number without its measurement rig is a claim, not evidence.

```text
Repro smoke check before submission (and again before the R2 resubmission):
  1. Fresh checkout → run the pipeline for one reported row end to end.
  2. Confirm the produced number matches the paper within the stated spread.
  3. Diff the artifact's claims against the current paper's claims — zero drift allowed.
  4. Strip identity from the anonymous package (see wacv-artifact-evaluation).
```

## Seed and session honesty

Report variance over seeds, and for deployed/field systems over repeated sessions or
devices. Do not report the best of many runs as "the" result. If a gap sits within the
spread, say so — an honest small margin survives review better than an inflated one that a
reviewer's own reproduction contradicts.

## Sync across the two rounds

The Revise-and-Resubmit lap is where reproducibility quietly breaks: authors change an
experiment in the paper but not in the artifact, or vice versa. After every revision, re-run
the smoke check and re-diff the artifact against the paper. A Round 2 reviewer re-reading a
revised submission should find the package and the paper telling one story.

## Reverify each cycle

- Whether the current guidelines request a reproducibility statement or checklist.
- Data-release and licensing rules for any dataset used as evidence.
- Supplementary size/format caps that constrain what you can ship (待核实 for 2026).

## Output format

```text
[Recipe ledger] regenerates every reported number: yes/no
[Constraint rig] device/meter/condition recorded for systems claims: yes/no
[Seeds/sessions] variance reported honestly: yes/no
[Baselines] re-tuned under your constraint and logged: yes/no
[Round sync] artifact matches current paper (zero drift): yes/no
[Gap] <the number a reviewer could not currently reproduce>
```
