---
name: dac-reproducibility
description: Use when building the reproducibility story for an ACM/IEEE Design Automation Conference (DAC) Research Manuscript, covering pinned EDA benchmark suites and versions (ISPD, EPFL, ISCAS/ITC, TAU, CircuitNet), open-source flow provenance (OpenROAD, ABC, Yosys), PDK/library and tool-version disclosure, seed/variance reporting for stochastic and ML flows, and the anonymized-then-public repository path — absent a formal DAC artifact-badging track.
---

# DAC Reproducibility

Build the reproducibility story into the evaluation, not onto it. DAC does **not** run a formal,
badge-issuing artifact-evaluation track for research manuscripts (**待核实** per cycle), so
reproducibility at DAC is not a review checkbox — it is what makes your QoR numbers *credible* to a
skeptical EDA reviewer and *usable* by the community that cites you. The currency is **pinned
benchmarks, disclosed tool versions, and re-runnable flows**.

## The EDA reproducibility floor

- **Pin the benchmark suite and version.** Name the exact suite (ISPD 2005/2015 contests, the EPFL
  combinational suite, ISCAS'85/'89, ITC'99, a TAU contest set, CircuitNet/OpenABC-D) and the
  specific release. "Standard benchmarks" without a version is not reproducible.
- **Disclose the flow and tool versions.** State the EDA tools and versions used — open (OpenROAD,
  ABC, Yosys, KLayout) or commercial — because QoR depends heavily on the flow. If a commercial tool
  or PDK is under NDA, say which class of tool it is and give what you can.
- **Name the PDK / technology / library.** QoR numbers are meaningless without the technology node
  and standard-cell library context (e.g., an open Nangate/ASAP7 PDK, or a named foundry node under
  NDA). Report the node and library or the reason you cannot.
- **Report the hardware and runtime.** The machine, core count, and memory for every runtime number;
  a runtime with no hardware context cannot be compared.
- **Pin data provenance for ML-for-EDA.** Dataset name and version, the train/test design split, and
  cached generated data — a model that needs re-generated data or per-design retraining must say so.

## Seeds, variance, and stochastic flows

Many EDA flows are stochastic (simulated annealing, partitioning, RL-based placement/routing). A
single run is not reproducible evidence:

```text
[Seeds]      report the seeds used and fix them where the tool allows
[Runs]       multiple runs; report mean and variance/spread, not a lucky best
[Determinism] note where the flow is nondeterministic (threading, tie-breaking) and how you handled it
[Environment] container or pinned dependency list so a re-runner gets the same tool behavior
```

## The anonymized-then-public repository path

- **At submission (double-blind):** if you link code/data, anonymize it exactly like the PDF — no
  author/lab names, no personal GitHub, no cluster paths, no vendor fingerprints (`../dac-submission`).
  Reviewers may not open it, so it strengthens but cannot rescue the paper.
- **After acceptance:** publish the de-anonymized repository, ideally with a **DOI-issuing archive**
  (Zenodo/Software Heritage) for a stable citation, an OSI license, and a README that maps each
  paper claim to the script and benchmark that produce it. This is community goodwill and citation
  insurance, not a DAC badge.

## Claim-to-reproduction mapping

Even without a review requirement, build the mapping that makes your numbers checkable:

| Paper claim | What reproduces it |
|---|---|
| "X% wirelength on ISPD" | The exact ISPD release + your tool version + the run script + seeds |
| "Y% timing improvement" | The design set + PDK/library + STA tool version + the flow script |
| "ML predicts IR-drop with error E" | The dataset version + train/test split + the model checkpoint |
| "Runs in Z hours at N cells" | The hardware spec + the largest-benchmark log |

## What DAC-specific reproducibility is *not*

- It is **not** an ACM artifact-badging exercise (DAC has no standing badge track); do not design for
  a badge that does not exist.
- It is **not** empirical-SE data availability; DAC evidence is QoR on circuits, so provenance means
  benchmark/PDK/tool versions and seeds, not human-subject protocols.
- It is **not** optional for credibility: an EDA reviewer distrusts a QoR claim that no one else could
  reproduce, even where no rule compels an artifact.

## Output format

```text
[Reproducibility readiness] strong / adequate / weak
[Benchmarks pinned]   suite + version named? yes/no
[Flow disclosed]      tool versions + PDK/library + hardware reported? yes/no
[Stochasticity]       seeds + variance across runs reported? yes/no
[ML provenance]       dataset version + train/test split + cached data? yes/no/NA
[Repo path]           anonymized at review / DOI-archived + licensed after accept? planned? yes/no
```
