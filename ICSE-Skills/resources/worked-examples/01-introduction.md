> **Illustrative teaching example.** The paper, tool, datasets, participants,
> and every number in this file are **invented** to demonstrate ICSE first-page
> craft. No real paper is paraphrased, and no venue policy is stated beyond
> what [`../official-source-map.md`](../official-source-map.md) verifies.
> Companion skills:
> [`icse-writing-style`](../../skills/icse-writing-style/SKILL.md),
> [`icse-topic-selection`](../../skills/icse-topic-selection/SKILL.md),
> [`icse-experiments`](../../skills/icse-experiments/SKILL.md).

# Worked Example: An ICSE-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening for a technique-plus-evaluation paper
and rebuild it to the ICSE bar — an evidenced engineering problem, research
questions visible from page 1, claims scoped to the study, and the
verifiability story started in the abstract. The research track's four
criteria (novelty, rigor, relevance, verifiability and transparency) are the
grading rubric throughout.

**Fictional paper:** *"FlakeShield: Quarantining Flaky Tests by Learning
Failure Provenance from CI Histories."* Invented tool: classifies test
failures as flaky or fault-revealing by mining each test's historical failure
context from continuous-integration logs, and auto-quarantines suspected
flakes.

---

## Before (a typical first draft)

> **Abstract.** Flaky tests are a serious problem in software testing and
> have attracted increasing attention from researchers and practitioners. In
> this paper, we propose FlakeShield, a novel AI-powered framework for
> detecting flaky tests. FlakeShield leverages machine learning on CI data to
> classify failures with high accuracy. Extensive experiments demonstrate
> that FlakeShield significantly outperforms state-of-the-art baselines and
> can greatly reduce developer effort.
>
> **Introduction.** Software testing is a crucial part of modern development.
> Unfortunately, many tests are flaky, i.e., they pass and fail
> non-deterministically. Flaky tests waste developer time and undermine trust
> in CI. Many approaches have been proposed, but they suffer from various
> limitations. Inspired by recent advances in machine learning, we propose a
> new framework. Our contributions are: (1) a novel approach; (2) an
> implementation; (3) extensive experiments showing superior performance.

**Why this fails the ICSE rubric:**

- **Relevance asserted, never evidenced.** "Serious problem", "attracted
  increasing attention", "waste developer time" — no measured cost, no cited
  study, no practitioner grounding. The relevance criterion wants the pain
  quantified or witnessed, not proclaimed (`icse-writing-style`).
- **No research questions.** An SE empiricist reads for the RQ contract;
  this opening never states what will be measured, on what subjects, against
  what baselines (`icse-experiments`).
- **Unscoped superlatives.** "High accuracy", "significantly outperforms",
  "greatly reduce" — numbers exist in the paper, so the abstract's refusal to
  name even one reads as evasion under the rigor criterion.
- **"Various limitations" as related-work analysis** — the delta over prior
  flaky-test detectors is exactly what the novelty criterion scores, and it
  is absent (`icse-related-work`).
- **Verifiability invisible.** No mention of dataset scale, availability, or
  artifact — the fourth criterion is unaddressed until (maybe) the last page.
- **Genre tell:** "AI-powered framework" markets the model; ICSE evaluates
  the engineering question. If the classifier were swapped, what remains?

---

## After (rebuilt to the ICSE bar)

> **Abstract.** Flaky test failures interrupt continuous integration: in the
> 48 open-source projects we mined (2.1M CI runs over three years), 14% of
> failing builds contained at least one failure unconnected to the triggering
> change. Existing detectors rerun tests — costly at CI scale — or classify
> from test code alone, ignoring the failure's context. We present
> FlakeShield, which classifies each failure using its *provenance*: the
> historical co-occurrence of that test's failures with changed files,
> execution environments, and failure messages mined from the project's own
> CI logs. We study three questions on held-out time-ordered data: RQ1
> (detection) — FlakeShield attains a median F1 of 0.83 vs 0.71 for the best
> rerun-free baseline, without rerunning tests; RQ2 (cost) — classification
> adds under 40 ms per failure; RQ3 (deployment risk) — auto-quarantine at
> our default threshold would have masked 1.9% of fault-revealing failures,
> which we analyze case by case. Tool, mined dataset, and all analysis
> scripts are available in our replication package.
>
> **Introduction (opening moves).** When a test fails, someone must decide
> whether the code or the test is lying. [¶1: the triage cost, evidenced —
> mined frequency from our dataset plus the developer-survey findings of
> published studies, cited.] [¶2: why the two existing detector families —
> rerun-based and static — trade cost against context-blindness, with the
> delta stated per family.] [¶3: the idea — failure provenance from CI
> history — and why it is information neither family uses.] [¶4: RQ1–RQ3,
> each naming its measure and its subjects.] [¶5: contributions as checkable
> claims — technique (§4), 48-project time-split evaluation (§5–6), risk
> analysis of quarantine (§6.3), released package — each with its section
> pointer.]

**What changed, criterion by criterion:**

| Criterion | Before | After |
|---|---|---|
| Relevance | "serious problem" | Measured interruption rate from a named corpus; triage cost grounded in cited studies |
| Novelty | "various limitations" | Two prior families named, each with the specific information they discard |
| Rigor | "extensive experiments" | Time-ordered held-out design, medians with baselines, and the *unflattering* number (1.9% masked faults) reported up front |
| Verifiability | absent | Corpus scale stated; package with tool, dataset, scripts promised in the abstract |

The most ICSE-characteristic move is reporting the risk number the technique
would rather hide: reviewers trained on threats-to-validity reasoning trust a
paper that audits its own failure mode before they do.

---

## Reusable checklist for your own opening

1. First paragraph: the engineering pain, with one number or citation a
   skeptic can check.
2. Prior work as named families with stated deltas, not "limitations".
3. RQs on page 1, each with its measure and subject population implied.
4. Every abstract adjective replaced by its number, scoped to the study.
5. One honest cost or risk of your own approach, stated before a reviewer
   finds it.
6. The availability story begun in the abstract, not appended to the end.
