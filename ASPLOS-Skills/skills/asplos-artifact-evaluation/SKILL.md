---
name: asplos-artifact-evaluation
description: Use when preparing an ASPLOS artifact for the post-acceptance evaluation committee — writing the ae.tex Artifact Appendix with software/hardware/dataset dependencies, targeting the Available / Functional / Reproducible badges, archiving on a public repository, and planning the collaborative back-and-forth with evaluators.
---

# ASPLOS Artifact Evaluation

Artifact evaluation at ASPLOS is a post-acceptance, opt-in, **collaborative**
process: an independent committee works with authors to validate the paper's key
results, and successful artifacts carry badges on the published paper (AE pages,
checked 2026-07-08). It is also a tradition the venue itself highlights — systems
readers increasingly treat an unbadged systems paper as a weaker citation. Treat AE
as part of the publication, budgeted like a small sixth section.

## The three badges and what each actually demands

| Badge | 2027 criterion (paraphrased from the AE pages) | Practical bar |
|---|---|---|
| **Available** | Artifact placed on a **publicly accessible archival repository** | A DOI-issuing archive (institutional or Zenodo-class); a GitHub URL alone is not archival |
| **Functional** | Evaluators can prepare and run the artifact; they document the steps they followed | Clean-machine install + a smoke experiment that completes in minutes, not hours |
| **Reproducible** | Evaluators validate the paper's **key results** | Per-claim run scripts whose output maps visibly onto specific figures/tables |

Evaluators assign scores per requested badge and record what they could and could
not reproduce — so the artifact's job is to make their success path short and their
failure modes diagnosable.

## The Artifact Appendix is the contract

ASPLOS 2027 expects an Artifact Appendix built from the provided `ae.tex` template
(or equivalent sections) covering: all **software, hardware, and dataset
dependencies**; the **key results** to be reproduced; and **how to prepare, run,
and validate** the experiments. Write it as if the evaluator is competent, busy,
and using different hardware than yours:

- Dependencies include the awkward ones: kernel versions, privileged access, BIOS
  settings, board models, expander firmware — everything from the state ledger in
  `asplos-reproducibility`.
- "Key results" means a *selected subset*: pick the claims that define the paper,
  not all 40 bars of every figure. Ambition here creates failure reports.
- Validation must be decidable: state the expected output and the tolerance within
  which the claim holds ("ordering preserved; absolute times ±15%").

## Package layout that evaluators can navigate blind

```text
artifact/
  README.md            # 10-minute quick start + full map
  APPENDIX.pdf         # the ae.tex appendix as submitted
  env/                 # container/VM recipe OR exact install script
  hardware.md          # tiered requirements + what to do without them
  run/
    smoke.sh           # minutes-scale end-to-end sanity check
    claim1_fig6.sh     # one script per key result, named for its figure
    claim2_tab3.sh
  expected/            # reference outputs + tolerance statement per claim
  data/ or data.md     # datasets, or archival pointers + checksums
```

## Hardware-dependent claims: give evaluators a path

The recurring ASPLOS AE failure is a paper whose headline number needs silicon the
committee lacks. Acceptable mitigations, in descending order of strength:

1. Provide **remote access** to the platform for the evaluation window (with an
   anonymity-safe access route if the process requires it).
2. Ship the **simulator-backed subset** as the reproducible core, and mark the
   silicon results as demonstrably-run (logs + analysis pipeline included).
3. Offer a **scaled-down proxy** (smaller FPGA, reduced workload) with an explicit
   argument for why the proxy's behavior transfers.

Say which mitigation applies *in the appendix*, per claim — evaluators score
against what you requested, so calibrated requests outperform hopeful ones.

## Collaboration protocol

- Expect rounds: evaluators report blockers, authors fix and respond. Reserve
  maintainer time in the weeks after camera-ready (exact 2027 AE dates: 待核实 —
  confirm at notification).
- Fix-forward, do not re-argue: an evaluator's confusion is a defect in the README.
- Keep the artifact frozen at a tagged version during evaluation; hotfixes go on a
  branch the evaluators are told about.

## Common evaluator blockers, pre-empted

Field experience across systems AE committees converges on a short list of
first-hour failures, all preventable:

- **Undeclared credentials or licenses** — a workload, simulator model, or
  dataset that needs a registration the evaluator lacks; declare it in the
  appendix and provide an alternative path.
- **Hidden network assumptions** — builds that fetch from internal mirrors or
  rate-limited hosts; vendor the dependencies or provide the container image.
- **Root-only steps without warning** — kernel-module or BIOS-adjacent steps
  must be flagged up front so the evaluator can pick a sacrificial machine.
- **Hour-scale first feedback** — if the smoke test takes an evening, the first
  blocker report costs a full round trip; minutes-scale smoke tests keep the
  collaboration inside the calendar.
- **Output the evaluator must interpret** — raw logs with no comparator; every
  claim script should end by printing PASS/FAIL against the tolerance.

## Anonymity boundary

AE runs after acceptance, so evaluator-facing materials need not be anonymous —
but any artifact *pointer placed in the submission itself* (an appendix teaser,
a footnoted repository) falls under the double-blind rules and must be
anonymized end to end: repository owner, commit author strings, container
registry paths, and dataset hosting all leak identity. The clean pattern is to
keep the submission's artifact story descriptive ("we will submit an artifact
covering claims 1-3") and materialize the links only in the Artifact Appendix
after notification.

## Dry-run protocol

Before submission to the AEC, have a colleague who did not build the artifact
execute the README on a clean machine, timing each stage and noting every
question they had to ask. Their questions are defects; fix the README, not the
colleague. Two such passes typically halve the evaluation rounds.

## Output format

```text
[Badges requested] available / functional / reproducible — with rationale
[Appendix status] dependencies / key results / prepare-run-validate all drafted: Y/N
[Smoke test] clean-environment runtime: N min · passes: Y/N
[Claim scripts] one per key result, mapped to figure/table: list
[Hardware path] per silicon-dependent claim: access / sim-subset / proxy
[Archive] DOI-issuing repository chosen + deposit dry-run done: Y/N
```
