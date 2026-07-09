> **Illustrative teaching example.** The paper, dataset, tool, and every number below are
> **fictional** and exist only to demonstrate ICSME house style. No real-paper facts, projects, or
> results are stated, and no policy is invented. Corresponding skills:
> [`icsme-writing-style`](../../skills/icsme-writing-style/SKILL.md),
> [`icsme-topic-selection`](../../skills/icsme-topic-selection/SKILL.md), and
> [`icsme-experiments`](../../skills/icsme-experiments/SKILL.md).

# Worked Example: An ICSME-Style Abstract + Introduction (before → after)

This demonstrates the **ICSME first-page arc** from `icsme-writing-style`:
**maintenance/evolution problem → why the current state is inadequate → contribution (technique
and/or finding) → evidence on real evolving systems → what changes for maintainers** — with the
ICSME expectations that the contribution is grounded in the *post-release lifecycle*, evidence is
**proportional to the claim** and drawn from **real change history**, and a **threats-to-validity**
posture is visible from the start (not bolted on as a closing paragraph).

The framing also reflects `icsme-topic-selection`: ICSME is strongest when the lesson is about how
software is **maintained, evolved, comprehended, or repaired** — here, whether automated
dependency-update pull requests actually get merged and what that costs maintainers — rather than a
modeling result whose maintenance consequence is incidental (which would route to a PL/ML venue or
to MSR if it were mining-for-its-own-sake), and when the study could not simply be re-labeled as an
MSR or SCAM paper without loss.

**Illustrative paper (fictional):** *"Do Update Bots Reduce Dependency Debt? A Study of Automated
Dependency Pull Requests and a Merge-Likelihood Filter."* Fictional artifact: a filter that predicts
which bot-opened dependency-update PRs a maintainer will merge, evaluated on real open-source
repositories' change history.

---

## Before (buries the maintenance contribution — typical first-draft abstract + intro)

> **Abstract.** Dependency management is important in modern software. We build a system that uses a
> state-of-the-art model and a novel pipeline to generate dependency-update pull requests. Our
> approach achieves high accuracy on a large dataset and outperforms baselines, showing the promise
> of AI for software maintenance.
>
> **Introduction.** Software depends on many libraries. Many bots now open pull requests to update
> dependencies. In this paper we use a model with an engineered pipeline to generate update PRs, and
> we evaluate it on a dataset of repositories, showing strong results. Section 2 covers related work,
> Section 3 our approach, Section 4 experiments, Section 5 threats, and Section 6 concludes.

**What's wrong (against `icsme-writing-style` / `icsme-topic-selection` / `icsme-experiments`):**

- **No maintenance/evolution question on the first page** — it leads with "AI for maintenance" and a
  systems win, not with a problem a maintainer living under dependency debt recognizes. ICSME wants
  the maintenance contribution up front.
- **Wrong claim shape.** "High accuracy" against a proxy label is not evidence that dependency debt
  falls in practice; the paper never asks whether maintainers *merge* the PRs — the actual
  maintenance outcome recorded in the change history.
- **No evolution evidence.** It says "a dataset of repositories" but never mines the *history* of
  merges, staleness, or debt over time — so nothing supports an evolution claim.
- **Threats to validity are a Section 5 afterthought**, so construct validity (does "accuracy" mean
  the debt was actually repaid?) is never engaged where it matters.
- **Model-as-contribution.** If the model were swapped, no maintenance lesson would remain — the
  `icsme-topic-selection` re-route signal that this is an ML paper wearing a maintenance title.
- **No open-science posture** — no mention of the mined corpus, SHAs, or an artifact, which a
  double-anonymous ICSME reviewer under ROSE norms will look for immediately.

---

## After (ICSME arc — problem → inadequacy → contribution → real-history evidence → what changes)

> **Abstract.** Automated bots open millions of dependency-update pull requests, yet maintainers
> merge only some of them, and the rest accumulate as noise on top of the very dependency debt the
> bots were meant to reduce. We mine **310,000 bot-opened update PRs across 640 actively maintained
> open-source projects** and find that a minority are merged, with the merge rate varying sharply by
> update type (major/minor/patch) and by whether CI passed (measurements reported with confidence
> intervals; the mining criteria, SHAs, and extraction window are in the artifact). Building on the
> study, we present **MergeTriage**, a lightweight filter that predicts whether a bot PR will be
> merged and suppresses the rest. On projects unseen during training it preserves most merged
> updates while removing a large share of ignored ones; we report effect sizes, a
> fairness-across-project-age breakdown, and an ablation isolating the model's contribution. *(problem
> → inadequacy → finding → tool → real-history evidence → threats posture — all on the first page.)*
>
> **Introduction.** *(¶1 — the maintenance problem, first breath.)* A maintainer's review attention
> is the scarcest resource in keeping dependencies current. Update bots promise to spend it wisely,
> yet every ignored bot PR is a small maintenance tax that pushes teams toward muting the bot — and
> back into the dependency debt it was meant to pay down. The engineering question is therefore not
> "can a bot open a plausible update PR?" but **"which automated updates do maintainers actually
> merge, and can we surface only those?"**
>
> *(¶2 — why the current state is inadequate.)* Existing work evaluates update-PR generation against
> reference diffs or CI-pass rates. Both are **proxies for the maintenance outcome, not the outcome
> itself**: a PR can be well-formed and green and still sit ignored for a year. No prior study
> measures the outcome that governs whether a team keeps the bot on — a subsequent *merge* — at scale
> across real projects' change histories.
>
> *(¶3 — contribution, stated as maintenance claims.)* We make two contributions. First, an
> **empirical study** of how often, and for which update types, bot PRs are merged across 640
> projects mined over a three-year window, with openly documented selection criteria. Second,
> **MergeTriage**, a filter that learns to predict merge likelihood and suppresses low-value PRs,
> evaluated for whether it keeps the updates maintainers would have merged.
>
> *(¶4 — evidence on real history, each claim paired.)* We tie every claim to evidence mined from
> real repositories: merge-rate estimates carry bootstrap confidence intervals (Table 1); update-type
> differences are tested with corrected pairwise comparisons (Fig. 2); MergeTriage's retention and
> suppression are reported with effect sizes on **projects unseen during training** (Table 3); and an
> ablation replacing model features with heuristic ones isolates their marginal value (Table 4). The
> mined PR corpus with pinned SHAs, extraction dates, and the analysis scripts are in the anonymized
> artifact.
>
> *(¶5 — threats posture and what changes for maintenance.)* We state the central threat plainly: a
> merged PR is a **correlational** signal of a useful update, not proof the maintainer judged it so,
> and we bound it with a manually audited subsample of merge rationales rather than claiming
> causation. We also handle **survivorship** — projects that abandoned the bot mid-history — by
> reporting how truncated histories were treated. The payoff for practice is concrete: teams can keep
> automated dependency maintenance *and* the review attention it was meant to protect. Section 2
> details the study design; Section 3 MergeTriage; Section 4 the evaluation; threats are argued
> alongside each result, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the ICSME bar

Mapped to the skill checklists:

- **Maintenance contribution on the first page** — the abstract and ¶1 pose a dependency-debt and
  review-attention problem and an outcome-level question before any model detail
  (`icsme-writing-style`: "lead with the maintenance/evolution contribution").
- **Evidence proportional to the claim, from real history** — the claim is about *merges*, so the
  evidence is merge data mined from real change history with intervals and effect sizes, not accuracy
  against a proxy (`icsme-experiments`: match the evidence to the claim shape; pin mining provenance).
- **Threats engaged where they live** — construct validity (merge as a proxy) and **survivorship**
  (abandoned-bot projects) are named in ¶5 and bounded, reported *with* results rather than
  quarantined (`icsme-writing-style`: the threats section is an argument, not boilerplate).
- **Right venue, lifecycle and re-label tests pass** — the lesson (a minority of bot PRs are merged;
  filtering protects attention and pays down debt) depends on software *evolving under dependency
  change* and would lose its point re-labeled as a pure MSR or ML paper (`icsme-topic-selection`).
- **Open science by default, complete on submission** — the mined corpus, SHAs, extraction window,
  and scripts are in an anonymized artifact, matching ICSME's double-anonymous, ROSE-aligned
  expectations — and, with no revision round, the evidence is already complete
  (`icsme-reproducibility`, `icsme-review-process`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified ICSM/ICSME
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for ICSME-specific submission policy and
> the single-round IEEE cycle model.
