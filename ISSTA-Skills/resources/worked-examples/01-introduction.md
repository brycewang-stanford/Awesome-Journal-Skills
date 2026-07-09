> **Illustrative teaching example.** The tool, technique, subjects, and every number below are
> **fictional** and exist only to demonstrate ISSTA house style. No real-paper facts, benchmarks,
> or results are stated, and no policy is invented. Corresponding skills:
> [`issta-writing-style`](../../skills/issta-writing-style/SKILL.md),
> [`issta-topic-selection`](../../skills/issta-topic-selection/SKILL.md), and
> [`issta-experiments`](../../skills/issta-experiments/SKILL.md).

# Worked Example: An ISSTA-Style Abstract + Introduction (before → after)

This demonstrates the **ISSTA first-page arc** from `issta-writing-style`:
**problem in a real testing/analysis setting → why existing techniques miss it → the technique →
evaluation contract (subjects, baselines, metric) → the finding** — against the criteria the
call actually names: originality, soundness, evaluation, and verifiability/transparency.

The framing also reflects `issta-topic-selection`: ISSTA is strongest when the contribution is a
**technique that finds, characterizes, or reasons about software behaviour**, evaluated on real
subjects — not a process or human-organization result (which routes to ICSE/FSE).

**Illustrative paper (fictional):** *"Deflake: Confirming Order-Dependent Flaky Tests by Targeted
Schedule Perturbation."* Fictional technique: a dynamic analysis that reruns a test suite under
adversarially chosen execution orders to classify each flaky test's root cause.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Flaky tests are a well-known problem in software testing and cause many issues for
> developers. In this paper we propose a new tool that detects flaky tests using a novel approach.
> We evaluate our tool on several projects and show that it works well and outperforms existing
> approaches, finding many flaky tests.
>
> **Introduction.** Software testing is important. Flaky tests, which pass or fail
> non-deterministically, have been studied by many researchers. Various approaches exist to detect
> them, including rerunning tests many times. In this paper, we present a tool that reruns tests in
> different orders and reports flaky tests. We evaluate it on some open-source Java projects and
> show it is effective. Section 2 discusses related work, Section 3 presents our approach,
> Section 4 our evaluation, and Section 5 concludes.

**What's wrong (against `issta-writing-style` / `issta-topic-selection` / `issta-experiments`):**

- **No specific contribution on the first page** — "a new tool ... a novel approach" names nothing
  a reader could reuse or falsify. ISSTA reviewers want the technique and its scope up front.
- **The bug class is not scoped** — "flaky tests" broadly, when the technique only addresses
  *order-dependent* flakiness. Overclaiming scope is a soundness flag.
- **"Outperforms existing approaches" with no evaluation contract** — no subjects, no baseline
  named, no metric, no statistic. This is exactly the evidence gap the criteria score.
- **No claim → evidence pairing:** "works well" and "finds many" are not tied to a benchmark, a
  ground-truth labelling, or a measured detection rate.
- **Verifiability absent** — no mention of an artifact, subjects, or reproducibility, which the
  ISSTA criteria list explicitly.
- **Over-signposted roadmap** stands in for an argument.

---

## After (ISSTA arc — problem → gap → technique → evaluation contract → finding)

> **Abstract.** *Order-dependent* flaky tests — those that pass or fail depending on the order in
> which the suite runs them — are costly to diagnose because reproducing the failing order by
> chance is rare. Existing detectors rerun tests in random orders, which finds order dependence
> only when the triggering order is sampled and cannot say *why* a test is order-dependent. We
> present **Deflake**, a dynamic analysis that (i) identifies the shared state a test reads, (ii)
> searches for an execution order that perturbs that state, and (iii) classifies the root cause as
> a *polluter*, *victim*, or *cleaner* relationship. On a benchmark of 220 labelled
> order-dependent tests across 18 open-source Java projects, Deflake confirms 94% of known
> order-dependent tests versus 61% for random-order reruns at an equal rerun budget, and assigns
> the correct root-cause category for 88% of confirmed cases; all subjects, labels, and the tool
> are archived. *(problem → gap → technique → evaluation contract → finding, all on the first
> page.)*
>
> **Introduction.** *(¶1 — the specific problem.)* A flaky test that fails only under a particular
> execution order wastes developer time twice: once when it fails in CI for no code change, and
> again when the developer cannot reproduce it locally because their run happens to use a benign
> order. We target this **order-dependent** subclass specifically, and set aside flakiness caused
> by concurrency or external resources, which needs different machinery.
>
> *(¶2 — gap: why existing techniques are insufficient, each named.)* Random-order rerunning
> detects order dependence only when it *samples* a failing order, so its recall is bounded by luck
> and its cost grows with suite size. Techniques that rerun in a fixed reversed order catch a
> narrow pattern and miss multi-test interactions. Neither approach explains the dependence, so a
> developer still has to find *which* other test pollutes the shared state. *(each prior line gets
> a concrete limitation, not a vague "prior work is limited.")*
>
> *(¶3 — the technique and its scope.)* Deflake instruments reads and writes of static and
> heap-reachable shared state, builds a dependence relation between tests, and then *directs* the
> order search toward orders that flip a suspected polluter–victim pair, rather than sampling
> orders blindly. Its one assumption is that the shared state is observable through the
> instrumented JVM; native-state interactions are out of scope and reported as such.
>
> *(¶4 — evaluation contract + finding, each claim paired.)* We evaluate on 220 order-dependent
> tests we labelled by manual confirmation across 18 projects (subjects and labels in the
> artifact). We compare against random-order and reversed-order rerunning **at an equal rerun
> budget**, report confirmation rate and root-cause accuracy, and test the difference with a
> paired non-parametric test reporting effect size (Table 1). Deflake's higher confirmation rate
> holds across project sizes; we report the two projects where instrumentation overhead made it
> slower, rather than hiding them. *(every claim → benchmark, baseline, metric, or artifact
> location.)*
>
> *(¶5 — why it matters + roadmap.)* The contribution is a detector that not only *confirms*
> order-dependent flakiness more reliably at a fixed budget but *explains* it in terms developers
> act on. Section 2 defines the shared-state model; Section 3 presents the directed order search;
> Section 4 reports the evaluation and threats to validity. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ISSTA bar

Mapped to the skill checklists:

- **Contribution and scope on the first page** — the abstract and ¶1 name the technique and *bound
  its scope to order-dependent flakiness* before any implementation detail
  (`issta-writing-style`: state the technique and its threat model early).
- **Gap is specific** — random-order and reversed-order rerunning each get a concrete failure, not
  a blanket dismissal (`issta-related-work` delta-first positioning).
- **Every claim paired with evidence** — confirmation rate → Table 1 on a labelled benchmark;
  root-cause accuracy → the same benchmark; fairness → equal rerun budget; honesty → the two
  slower projects reported (`issta-experiments` claim→evidence map).
- **Soundness over reach** — the shared-state observability assumption is stated and native-state
  cases are declared out of scope, rather than silently overclaimed (`issta-writing-style`).
- **Verifiability built in** — subjects, labels, and tool archived, matching the criterion the call
  names (`issta-reproducibility`, `issta-artifact-evaluation`).
- **Right venue** — the contribution is a **testing/analysis technique evaluated on real subjects**,
  a strong ISSTA fit rather than an ICSE process contribution or an ML-leaderboard result
  (`issta-topic-selection` fit test).
- **18-page discipline** — the shared-state formalism and full per-project tables go later or into
  the artifact while the body carries the argument (`issta-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, archival-verified
> ISSTA papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ISSTA-specific submission policy.
