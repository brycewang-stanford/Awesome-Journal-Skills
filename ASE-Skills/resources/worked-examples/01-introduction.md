> **Illustrative teaching example.** The paper, tool, dataset, and every number below are
> **fictional** and exist only to demonstrate ASE house style. No real-paper facts, projects, or
> results are stated, and no policy is invented. Corresponding skills:
> [`ase-writing-style`](../../skills/ase-writing-style/SKILL.md),
> [`ase-topic-selection`](../../skills/ase-topic-selection/SKILL.md), and
> [`ase-experiments`](../../skills/ase-experiments/SKILL.md).

# Worked Example: An ASE-Style Abstract + Introduction (before → after)

This demonstrates the **ASE first-page arc** from `ase-writing-style`:
**an automatable development task the reader recognizes → why current automation (or manual
practice) is inadequate → the technique, embodied in a runnable tool → evaluation on real subjects
against credible baselines → what it automates for practice, threats visible from the start** —
with the ASE expectations that the contribution is an *automation* of a software-engineering task,
the idea is **runnable**, and evidence is **proportional to the claim**.

The framing also reflects `ase-topic-selection`: ASE is strongest when the heart of the paper is
**automating** analysis, testing, synthesis, repair, or comprehension — here, automatically
repairing flaky tests — rather than a broad empirical finding (which leans FSE), a
testing-theory-depth result (which leans ISSTA), or a modeling result whose SE payoff is incidental
(which routes to a PL or ML venue).

**Illustrative paper (fictional):** *"RepAIr: Root-Cause-Aware Automatic Repair of Flaky Tests."*
Fictional artifact: a tool that classifies a flaky test's root cause and synthesizes a targeted
patch, evaluated on real flaky tests mined from open-source CI logs.

---

## Before (buries the automation — typical first-draft abstract + intro)

> **Abstract.** Flaky tests are a big problem in software engineering. We propose a new
> deep-learning approach that uses a large language model to fix flaky tests. Our method achieves
> high accuracy on a dataset of tests and outperforms baselines, demonstrating the power of AI for
> software testing.
>
> **Introduction.** Testing is important and flaky tests are annoying. Recently, LLMs have shown
> impressive results on many tasks. In this paper we apply an LLM with a clever prompt to repair
> flaky tests, and we evaluate it on a dataset, showing strong results. Section 2 covers related
> work, Section 3 our approach, Section 4 experiments, Section 5 threats, and Section 6 concludes.

**What's wrong (against `ase-writing-style` / `ase-topic-selection` / `ase-experiments`):**

- **The automated task is not stated precisely on the first page** — it leads with "AI is powerful"
  rather than the specific engineering task being automated (classify a flake's root cause, then
  synthesize a patch that removes the nondeterminism).
- **Model-as-contribution.** If the LLM were swapped, nothing distinctive would remain — the
  `ase-topic-selection` re-route signal that this is an ML paper wearing an SE title. ASE wants the
  *automation design* (root-cause-aware repair), not the model, as the contribution.
- **"High accuracy" is the wrong claim shape.** For a repair tool the outcome is whether the patch
  *makes the test reliably pass without masking the real behavior*, verified by re-running, not a
  classification score against a proxy label.
- **No runnable tool, no baselines named** — an ASE reviewer immediately asks "what does it run on,
  and compared to what?"
- **No Data Availability posture** — ASE requires a Data Availability Statement, and a
  double-anonymous reviewer looks for the anonymized tool and dataset at once.
- **Over-signposted roadmap** substituting for an argument.

---

## After (ASE arc — task → inadequacy → technique+tool → real-subject evidence → what it automates)

> **Abstract.** Flaky tests pass or fail nondeterministically, and teams routinely quarantine or
> delete them, silently eroding their suites. Existing automation either *detects* flakiness or
> reruns tests to hide it; almost none **repairs** the underlying nondeterminism. We present
> **RepAIr**, a technique that first classifies a flaky test's root cause (async wait, order
> dependence, unseeded randomness, external resource) from its execution traces, then synthesizes a
> **root-cause-targeted patch** and validates it by repeated re-execution. On **1,200 real flaky
> tests mined from the CI logs of 90 open-source projects**, RepAIr produces patches that make a
> substantial majority reliably pass across 200 reruns without altering the test's assertions; we
> report repair rates with confidence intervals, a per-root-cause breakdown, an ablation isolating
> the language-model component from the program-analysis component, and a comparison against
> rerun-based and detection-then-manual baselines. The tool, dataset, and cached model outputs are
> in the anonymized artifact. *(task → inadequacy → technique → tool → real-subject evidence →
> honest scope — all on the first page.)*
>
> **Introduction.** *(¶1 — the automatable task, first breath.)* A flaky test is a test whose
> outcome changes without any change to the code under test. Developers know the symptom well; what
> they lack is a way to **automatically remove the nondeterminism** rather than rerun around it or
> delete the test. The engineering task we automate is concrete: given a flaky test, identify *why*
> it is flaky and produce a patch that makes it deterministic while preserving what it checks.
>
> *(¶2 — why current automation is inadequate.)* Detectors tell a developer *that* a test is flaky;
> rerun-based CI policies *mask* flakiness at the cost of compute and hidden real failures. Neither
> repairs the test. Generic patch-generation tools, tuned for functional bugs, do not model the
> specific mechanisms of flakiness and frequently "fix" a test by weakening its assertions — which
> is worse than leaving it flaky. No existing automation both **diagnoses the root cause** and
> **synthesizes a behavior-preserving repair**.
>
> *(¶3 — the contribution, stated as an automation design.)* We make two contributions. First, a
> **root-cause-aware repair technique** that couples a lightweight program analysis over execution
> traces (to classify the flakiness mechanism) with mechanism-specific patch templates instantiated
> by a language model, gated by a re-execution oracle. Second, **RepAIr**, a tool implementing the
> technique for JUnit projects, released as a runnable artifact.
>
> *(¶4 — evidence on real subjects, each claim paired.)* We tie every claim to evidence on real
> flaky tests: overall repair rate with bootstrap confidence intervals (Table 1); a per-root-cause
> breakdown showing where the technique succeeds and fails (Fig. 2); an **ablation** replacing the
> language-model templates with purely static rewrites, isolating each component's marginal value
> (Table 3); and a comparison against rerun-based masking and detection-then-manual repair on the
> same subjects (Table 4). Every reported "repair" is validated by 200 reruns and an
> assertion-preservation check.
>
> *(¶5 — threats posture and what it automates for SE.)* We state the central threat plainly: a test
> that passes 200 reruns is *strong evidence* of, but not a proof of, removed nondeterminism, and we
> bound it with a manually audited subsample and by reporting assertion-preservation separately from
> pass-stability. The payoff for practice is concrete: teams can **repair** flaky tests
> automatically instead of quarantining them, keeping the coverage the tests were written to
> provide. Section 3 details the technique; Section 4 RepAIr; Section 5 the evaluation; threats are
> argued alongside each result, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ASE bar

Mapped to the skill checklists:

- **The automated task is on the first page** — the abstract and ¶1 name the exact task (diagnose +
  repair flakiness) before any model detail (`ase-writing-style`: "lead with what you automate").
- **Automation design, not the model, is the contribution** — the root-cause-aware coupling of
  program analysis with templated synthesis survives swapping the language model, so it is an ASE
  contribution, not an ML re-route (`ase-topic-selection`: the model-swap test passes).
- **The idea is runnable** — RepAIr is a named tool on real JUnit projects, the ASE "automation you
  can run," matching the TestEra/monitoring exemplar lineage (`resources/exemplars/library.md`).
- **Evidence proportional to the claim** — the claim is *repair*, so the evidence is pass-stability
  across reruns plus assertion-preservation on real subjects with intervals and an ablation, not an
  accuracy score against a proxy label (`ase-experiments`: match evidence to claim shape).
- **Threats engaged where they live** — the rerun-as-proxy-for-determinism threat is named in ¶5
  and bounded with an audited subsample, reported *with* results rather than quarantined.
- **Open science by default** — the tool, dataset, and *cached* model outputs are in an anonymized
  artifact, matching ASE's double-anonymous review and its mandatory Data Availability Statement
  (`ase-reproducibility`, `ase-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ASE
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ASE-specific submission policy and
> the Accept/Revision/Reject review model.
