---
name: corl-artifact-evaluation
description: Use when packaging the artifacts of a CoRL paper — code, training configs, demonstration datasets, policy checkpoints, simulation environments, and benchmark definitions — as anonymous review-time evidence and as durable public releases after acceptance, in a venue with no formal artifact-badging track.
---

# CoRL Artifact Evaluation

CoRL has no separate artifact-evaluation track or badge system in the 2026
materials verified for this pack (a formal AE track remains 待核实 each cycle).
Artifacts are instead judged twice, informally: by reviewers deciding whether to
trust your tables, and by the community deciding — for years afterward — whether
your method becomes a baseline. Package for both audiences from the start.

## Artifact inventory for a robot-learning paper

| Artifact | Review-time form (anonymous) | Public form (post-acceptance) |
|---|---|---|
| Training code + configs | Scrubbed ZIP in the supplementary | GitHub repo, tagged release matching the paper |
| Evaluation harness | Same ZIP; scripts + fixed init-state lists | Same repo; the part reused most by others |
| Demonstration data | Small sample in ZIP; full set described | Archive with DOI + datasheet, license stated |
| Policy checkpoints | Optional if small; else described | Hosted weights keyed to each results table |
| Sim environments / tasks | Env definitions + versions in ZIP | Repo or upstream PR to the benchmark suite |
| Hardware recipe | Appendix spec (rig, control interface) | Project page: BOM-level detail, photos |
| Overview video | Supplementary upload (≤ 250 MB, 2026 cap) | Project page / video host — PMLR takes no video |

## The reuse test

Design the release around one question: *can a stranger reproduce your evaluation
without emailing you?* Concretely, a competent robot-learning grad student
should be able to (1) install, (2) run evaluation with a released checkpoint,
and (3) regenerate one paper table, in an afternoon, in simulation. Training
reproduction and hardware reproduction are aspirational tiers above this floor —
label the tiers honestly rather than implying all three.

```text
Release tiers — declare one per artifact in the README:
  T1  evaluate: released checkpoint + eval script reproduce Table N in sim
  T2  retrain:  configs + data (or data recipe) reproduce the training run
                within the reported seed spread
  T3  re-embody: rig documentation sufficient to attempt hardware replication
```

## Review-time packaging (anonymous)

- One ZIP, one top-level README, a table mapping `paper table → command`.
- Determinize what you can: fixed evaluation seeds, fixed init-state lists,
  pinned dependency versions (`corl-reproducibility` owns the manifest format).
- Anonymize mechanically, then by eyeball: repo history stripped, paths cleaned,
  no W&B/HF org names, no grant numbers in license headers, and remember the
  URL rule — an anonymized page on a lab-named domain still leaks.
- Keep it runnable without a robot: reviewers do not have your hardware, so the
  artifact's demonstrable slice is sim evaluation plus logs/video of the
  hardware runs. Ship episode-level logs (CSV) for every hardware table.

## Post-acceptance: durable release

- **Timing.** The 2026 camera-ready deadline (October 12) is when links get
  frozen into the PMLR record — stand up the public repo, dataset archive, and
  project page *before* finalizing the PDF so the printed URLs are real.
- **Durability ladder.** Lab web servers die with funding cycles: put datasets
  and static artifacts in DOI-granting archives, code in a tagged repository
  release, and treat the project page as a pointer hub rather than the sole home.
- **Checkpoint provenance.** Key each released checkpoint to its table and seed
  ("`ckpt_t3_s2` = Table 3, seed 2"); publishing only a best-seed checkpoint
  while the paper reports seed means invites a mismatch report you'll answer
  publicly — CoRL reviews of accepted papers are public, and so is the follow-up
  scrutiny.
- **License deliberately.** Code (permissive vs copyleft), data (usage terms,
  consent constraints for human video), and weights (increasingly their own
  license class) are three separate decisions; "no license" means "nobody may
  legally build on this."

## Benchmarks and datasets as first-class artifacts

If the artifact *is* the contribution (a task suite, a large demo corpus), the
bar rises from reuse to stewardship:

- Version the benchmark explicitly (v1.0 at camera-ready) and changelog any
  post-publication fix; silent edits corrupt every downstream comparison.
- Publish the evaluation protocol as executable code, not prose — episode
  counts, init distributions, success criteria — so future papers cite numbers
  produced by *your* harness rather than reimplementations.
- Provide a datasheet: collection method, operator demographics if teleop,
  filtering, known biases, consent/licensing status of any human footage.

## Failure patterns that surface after publication

Because CoRL reviews of accepted papers are public and the community reuses
artifacts aggressively, release defects surface fast and visibly:

- **The vanished environment**: the eval harness imports a benchmark fork whose
  branch was deleted; vendor the environment code or pin an archived copy.
- **The config drift**: the repo's default config differs from the paper's
  runs; ship the exact configs used, named per table, and make defaults match.
- **The GPU-only afternoon**: an evaluation that silently requires 8×A100 to
  run at all; document minimum hardware and offer a reduced smoke-test target.
- **The consent surprise**: teleop or human-video data released without the
  consent scope to permit it; resolve data-rights questions before the paper
  promises release, not after.

## Release checklist

```text
[ ] Tier (T1/T2/T3) declared per artifact; T1 actually tested by a
    teammate on a clean machine
[ ] README: install steps, table→command map, expected tolerances
[ ] Checkpoints keyed to tables and seeds; selection rule stated
[ ] Dataset archived with DOI, datasheet, and license
[ ] Hardware logs + uncut eval video published for hardware tables
[ ] Licenses chosen for code, data, and weights separately
[ ] All URLs live before camera-ready freeze (2026: Oct 12 AoE)
[ ] Anonymous variant retired only after decisions are out
```

Re-check the live cycle for any new artifact policy, badge program, or required
availability statement at https://www.corl.org/contributions/instruction-for-authors
— venue policy here is young and moves quickly, like the field itself.
