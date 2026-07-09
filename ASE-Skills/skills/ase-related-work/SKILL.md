---
name: ase-related-work
description: Use when writing the related-work and positioning of an ASE (IEEE/ACM Automated Software Engineering) paper, covering the automated-SE literature lanes, delta-first positioning against prior tools/techniques, fair head-to-head framing, and double-anonymous self-citation.
---

# ASE Related Work

Position the paper against **prior automation**, not against a topic. At ASE the question a reviewer
holds is "what does this tool/technique do that the existing automated approaches do not?" — so
related work is a **delta argument**, and the strongest deltas are stated against named,
runnable prior tools you can (and often must) compare against empirically.

## Cover the ASE literature lanes

An automated-SE paper usually sits at the intersection of several lanes; name your position in each
that applies:

- **Program analysis** — static/dynamic analysis, symbolic/concolic execution, abstract
  interpretation, invariant inference.
- **Test generation and testing** — search-based, specification-based, fuzzing, regression and
  flaky-test handling.
- **Fault localization, debugging, and repair** — spectrum-based localization, automated program
  repair, patch synthesis.
- **Synthesis and recommendation** — program/code synthesis, API recommendation, refactoring
  automation.
- **Comprehension and documentation** — summarization, code search, clone and change analysis.
- **Learning-based / AI4SE** — learned code representations, models applied to SE tasks, LLM-based
  automation — and **SE4AI**, applying SE automation to ML systems.

## Delta-first positioning

Write each related-work cluster as: *prior automation X does A; it cannot do B because C; we do B.*
Then, where B is comparable, **compare against X empirically** — ASE reviewers expect a head-to-head
against the closest runnable baseline, not just a prose distinction.

```text
[Cluster] spectrum-based fault localization
  Prior: ranks statements by suspiciousness from pass/fail spectra.
  Gap: assumes a fixed test suite; degrades when tests are flaky.
  Delta: our technique estimates and corrects for flakiness before ranking.
  Evidence of delta: head-to-head on the same faulty subjects, §5.2, Table 3.
```

## Fair head-to-head framing (the ASE credibility test)

- Compare against the **strongest, most recent** automated baseline you can run, at an **equal,
  documented budget** (time, iterations, tuning). An under-configured baseline is the classic
  soundness objection and a Revision criterion waiting to happen.
- If a baseline tool cannot run on your subjects, say why explicitly and choose the nearest viable
  alternative — do not quietly omit the obvious competitor.
- Distinguish **reimplementation** from the original tool, and note version/commit — reviewers who
  built the baseline will check.

## Distinguish ASE from sibling-venue prior work

Because automated-SE ideas appear across venues, position precisely: a testing-theory result may
live at ISSTA, a broad empirical study at FSE, a language mechanism at a PL venue. When you cite
across venues, make the ASE delta — *the automation you add* — explicit, so a reviewer does not read
your contribution as a reheated sibling-venue result.

## Double-anonymous self-citation

- Cite your own prior tools and papers in the **third person** ("Prior work by [Anonymous] proposed
  ...", or neutrally "The X tool [12] ...") so the citation does not deanonymize you.
- Do not write "our earlier tool" or link to a repository whose owner is you.
- Keep the count of self-citations honest; a cluster of third-person citations to one hidden group
  is itself a leak.

## Coverage checks

```text
[Recency]   at least the last 2-3 years of ASE/ICSE/FSE/ISSTA automation in your subarea cited?
[Closest baseline] is the single most similar runnable tool named AND compared, not just cited?
[Cross-venue] PL/ML/testing neighbors positioned so your automation delta is explicit?
[Anonymity] every self-citation in the third person; no repository ownership revealed?
[Honesty]   any obvious competitor conspicuously missing? (a reviewer will notice)
```

## Output format

```text
[Lanes] which automated-SE lanes the paper touches
[Delta table] prior tool -> what it does -> gap -> your delta -> where the head-to-head lives
[Baseline fairness] closest runnable baseline named, version pinned, equal budget?
[Anonymity check] self-citations third-person, no repo owner revealed
```
