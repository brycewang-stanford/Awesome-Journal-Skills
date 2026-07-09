---
name: imc-supplementary
description: Use when deciding what belongs in an ACM IMC paper body versus its appendix and released artifact, covering the acmart page limits, the rule that decision-critical evidence and the Ethics discussion stay in the reviewed pages, double-blind supplementary material, and how to split a measurement paper between body, appendix, and dataset.
---

# IMC Supplementary

Use this when assembling IMC supplementary material. IMC's `acmart` format gives an **unlimited
appendix**, which tempts authors to offload the argument — but the governing rule is strict: **the
page-limited body must be self-contained and decision-complete.** Reviewers read the appendix and
the artifact at their discretion; anything the decision depends on lives in the body.

## What goes where

| Content | Body (within page limit) | Appendix / released artifact |
|---|---|---|
| The measurement question and the headline finding | Yes | — |
| Vantage-point summary + coverage/representativeness argument | Yes | Full per-vantage-point table |
| Methodology sufficient to judge soundness | Yes | Full configs, seed/target lists |
| Key results, confidence intervals, and their limitations | Yes | Secondary plots, full result tables |
| **The Ethics discussion** | **Yes (section; details may extend to appendix)** | IRB form, extended safety analysis |
| Raw/large datasets, logs, scripts | — | Yes (released artifact) |
| Reproduction instructions | A pointer | The README and run scripts |

If a reviewer would need to open the appendix or artifact to know whether to accept, the paper is
mis-partitioned — move that evidence into the body.

## The unlimited-appendix trap

IMC's appendix is unlimited but **may not be used to abuse the page limit**. Consequences:

- Keep the finding, the vantage-point justification, the core methodology, the headline results,
  and the limitations **in the body** — they are decision-critical.
- Per-vantage-point tables, full parameter grids, extra target lists, and additional analyses go to
  the appendix with explicit forward references.
- Do **not** smuggle a load-bearing result into the appendix because the body is full — an argument
  that only closes with appendix material reads as unreviewable, and reviewers are entitled to stop
  at the body.

## The Ethics section is not optional supplementary

Unlike ordinary appendix material, the **Ethics** treatment is required and must be a clearly
marked section (details may spill to an appendix). Do not relegate the entire ethics argument to an
optional appendix the reviewer might skip — a paper without a visible Ethics section may be
rejected (`imc-submission`).

## Double-blind supplementary rules

```text
[No identity]   no authors, affiliations, acknowledgements, grants, testbed names, AS/probe IDs,
                or lab-domain links anywhere in the appendix or artifact
[Anonymized links] the dataset/tool link points at an anonymizing host, not a personal/lab repo
[Clean archive]  no .git history, credentials, API keys, cluster paths, or huge irrelevant captures
[Opens clean]    the archive unzips and the README orients a reader in a minute on a fresh machine
[Provenance]    vantage-point and timing metadata present but scrubbed of identity
```

## Appendix architecture

- Order appendix sections to mirror the paper's structure (per measurement/RQ), so reviewers
  navigate by topic, not page number.
- Reference each appendix section from the body at least once — orphaned material is invisible
  under discretionary review.
- Keep the released dataset's schema documentation with the artifact, not buried in the appendix.

## Vignette: splitting a multi-vantage-point study

A paper measuring a protocol from many vantage points over months: the body keeps the question, a
summarized vantage-point table with the coverage-bias argument, the core method, the headline
findings with confidence intervals, the limitations, and the Ethics section; the appendix holds the
full per-vantage-point breakdown, the complete target lists with capture dates, and secondary
analyses; the released artifact holds the time-stamped dataset, the schema, and the analysis
scripts. Nothing decision-critical lives only outside the body.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical outside the body? <none / move: what>
[Ethics visibility] Ethics section present in the body? yes/no
[Page limit] body self-contained within limit? appendix not abused? yes/no
[Anonymity] appendix/artifact clean of identity + infrastructure? passed/issues
[Body dependency] <what a reviewer can decide without opening the appendix/artifact>
```
