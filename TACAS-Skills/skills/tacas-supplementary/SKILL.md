---
name: tacas-supplementary
description: Use when deciding what belongs in a TACAS (ETAPS) paper body versus its appendix, supplementary website, and artifact, covering the 16-page (or 6-page) llncs.cls budget that excludes references and appendix, the rule that decision-critical content stays in the reviewed pages, category-appropriate anonymity of supplementary material, and how to split a verification paper between body, appendix, and a mandatory-or-voluntary artifact.
---

# TACAS Supplementary

Use this when assembling TACAS supplementary material. The governing rule: **the paper must be
judgeable from the reviewed pages alone.** The appendix, the supplementary website, and the artifact
support the paper; they do not hold the argument. Reviewers read supplementary material at their
discretion, so anything the decision depends on lives in the body.

## What goes where

| Content | Body (within page limit) | Appendix / website / artifact |
|---|---|---|
| Problem, contribution, and the soundness claim | Yes | — |
| The core algorithm / tool architecture | Yes | Full pseudocode variants, extra config |
| The soundness argument | Theorem + proof sketch in body | Full proof in appendix |
| Headline benchmark results | Yes (key table) | Full per-benchmark tables, extra plots |
| Benchmark setup (machine, timeout, baseline) | Stated in body | Full logs, raw outputs |
| The tool itself + reproduction scripts | A pointer | The artifact (mandatory for tools) |
| Extra examples, secondary optimizations | Summary | Appendix / website |

If a reviewer would need to open the appendix or artifact to know whether the result is sound or the
comparison is fair, the paper is mis-partitioned — move that into the body.

## The page-budget discipline

TACAS's `llncs.cls` budget (16 pages for research / case-study / regular tool; **6 pages** for
tool-demonstration) **excludes references and a clearly marked end appendix**. Consequences:

- Keep the **soundness claim, the core algorithm, and the headline comparison in the body** — they
  are decision-critical.
- Full proofs, per-benchmark tables, and secondary material go to the **appendix** (at the end,
  clearly marked) or a **supplementary website**, with explicit forward references.
- Do not use the appendix or artifact to smuggle in a result that would not otherwise fit — an
  argument that only closes with out-of-body material reads as unreviewable. Appendices are read at
  the reviewer's discretion.

## Category-appropriate anonymity of supplementary material

```text
[Research (double-blind)]  appendix, website, and any review artifact must be anonymous: no authors,
                           affiliations, acks, grants, cluster paths, tool identity, or repo owners;
                           route the website through an anonymizing host
[Tool / case-study (single-blind)]  supplementary material is named; the tool identity is expected,
                           but still ship a clean archive (no credentials, no .git cruft)
[Clean archive]            no .git history, .DS_Store, credentials, caches, or huge irrelevant files
[Opens clean]              verify the appendix/website/artifact is navigable and the README orients a
                           reader in one minute
```

## The mandatory-artifact interaction (tool and tool-demo papers)

For a **regular tool** or **tool-demonstration** paper the artifact is not "supplementary" in the
optional sense — it is a **mandatory, evaluated** deliverable submitted after the paper. Split so
that the body makes the paper judgeable *and* the artifact makes every claim reproducible; the two
must agree. See `tacas-artifact-evaluation` and `tacas-reproducibility`.

## Vignette: splitting a research paper with a long proof

A paper with a new algorithm, a substantial soundness proof, and a large benchmark table: the body
keeps the algorithm, the theorem with a proof sketch, the key benchmark comparison with the setup
stated, and the external-validity limits; the appendix holds the full proof and the per-benchmark
tables; the (voluntary) artifact holds the tool and the scripts that regenerate the tables. Nothing
decision-critical — soundness or comparison fairness — lives only outside the body.

## Output format

```text
[Supplement status] ready / needs fixes / not ready
[Partition check] anything decision-critical (soundness/fairness) outside the body? <none / move: what>
[Page budget] body within 16/6 limit? references + appendix excluded correctly? yes/no
[Anonymity] (research) appendix/website/artifact clean of identity + metadata? passed/issues
[Body dependency] <what a reviewer can decide without opening the appendix/artifact>
```
