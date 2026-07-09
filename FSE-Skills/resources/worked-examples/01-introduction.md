> **Illustrative teaching example.** The paper, dataset, tool, and every number below are
> **fictional** and exist only to demonstrate FSE house style. No real-paper facts, projects, or
> results are stated, and no policy is invented. Corresponding skills:
> [`fse-writing-style`](../../skills/fse-writing-style/SKILL.md),
> [`fse-topic-selection`](../../skills/fse-topic-selection/SKILL.md), and
> [`fse-experiments`](../../skills/fse-experiments/SKILL.md).

# Worked Example: An FSE-Style Abstract + Introduction (before → after)

This demonstrates the **FSE first-page arc** from `fse-writing-style`:
**practitioner problem → why the current state is inadequate → contribution (technique and/or
finding) → evidence on real subjects → what changes for software engineering** — with the FSE
expectations that the contribution is a *software-engineering* contribution, evidence is
**proportional to the claim**, and a **threats-to-validity** posture is visible from the start
(not bolted on as a closing paragraph).

The framing also reflects `fse-topic-selection`: FSE is strongest when the lesson is about how
software is **built, maintained, tested, or reviewed** — here, whether automated review comments
actually drive code change — rather than a modeling result whose SE consequence is incidental
(which would route to a PL or ML venue), and when the study could not simply be re-labeled as an
ICSE, ASE, or ISSTA paper without loss.

**Illustrative paper (fictional):** *"Do Review Bots Change Code? A Study and a Trigger-Aware
Filter for Automated Pull-Request Comments."* Fictional artifact: a filter that predicts which
bot-generated review comments a developer will act on, evaluated on real open-source pull
requests.

---

## Before (buries the SE contribution — typical first-draft abstract + intro)

> **Abstract.** Large language models have transformed software engineering. We build a system
> that generates pull-request review comments using a state-of-the-art model and a novel prompt
> pipeline. Our approach achieves high accuracy on a large dataset and outperforms baselines,
> showing the promise of AI for code review.
>
> **Introduction.** Code review is important. Many tools now post automated comments on pull
> requests. In this paper we use an LLM with a carefully engineered prompt to generate review
> comments, and we evaluate it on a dataset of pull requests, showing strong results. Section 2
> covers related work, Section 3 our approach, Section 4 experiments, Section 5 threats, and
> Section 6 concludes.

**What's wrong (against `fse-writing-style` / `fse-topic-selection` / `fse-experiments`):**

- **No software-engineering question on the first page** — it leads with "LLMs transformed SE"
  and a systems win, not with a problem a maintainer recognizes. FSE wants the SE contribution up
  front.
- **Wrong claim shape.** "High accuracy" against a proxy label is not evidence that anything
  changes in practice; the paper never asks whether developers *act* on the comments — the actual
  SE outcome.
- **Threats to validity are a Section 5 afterthought**, so construct validity (does the proxy
  label mean what they claim?) is never engaged where it matters.
- **Model-as-contribution.** If the model were swapped, no SE lesson would remain — the
  `fse-topic-selection` re-route signal that this is an ML paper wearing an SE title.
- **No open-science posture** — no mention of a dataset, labeling protocol, or artifact, which a
  double-anonymous FSE reviewer will look for immediately.
- **Over-signposted roadmap** substituting for an argument.

---

## After (FSE arc — problem → inadequacy → contribution → real-subject evidence → what changes)

> **Abstract.** Automated review bots now post thousands of comments on pull requests daily, but
> it is unknown how often developers actually change code in response — and teams increasingly
> mute bots they find noisy. We study **48,000 bot comments across 240 open-source projects** and
> find that only a minority precede a code change, with the actionable fraction varying sharply by
> comment category (measurements reported with confidence intervals; the labeling protocol and
> inter-rater agreement are in the artifact). Building on the study, we present **TriageFilter**, a
> lightweight classifier that predicts whether a comment will be acted upon and suppresses the
> rest. On held-out projects it preserves the majority of acted-upon comments while removing a
> large share of ignored ones; we report effect sizes, a fairness-across-project-size breakdown,
> and a contamination-aware ablation isolating the language model's contribution. *(problem →
> inadequacy → finding → tool → real-subject evidence → threats posture — all on the first page.)*
>
> **Introduction.** *(¶1 — the practitioner problem, first breath.)* A maintainer's attention is
> the scarcest resource in code review. Review bots promise to spend it wisely, yet every
> unhelpful comment is a small tax that pushes teams toward disabling the bot entirely. The
> engineering question is therefore not "can a model write a plausible comment?" but **"which
> automated comments actually lead to a code change, and can we show developers only those?"**
>
> *(¶2 — why the current state is inadequate.)* Existing work evaluates review-comment generation
> against reference comments or human ratings of plausibility. Both are **proxies for usefulness,
> not usefulness itself**: a comment can read well and still be ignored, and reference-match
> penalizes correct comments phrased differently. No prior study measures the outcome that governs
> whether a team keeps the bot on — a subsequent code change — at scale on real projects.
>
> *(¶3 — contribution, stated as SE claims.)* We make two contributions. First, an **empirical
> study** of how often, and for which comment categories, bot comments precede code changes across
> 240 projects, with an openly documented labeling protocol. Second, **TriageFilter**, a filter
> that learns to predict actionability and suppresses low-value comments, evaluated for whether it
> keeps the comments developers would have acted on.
>
> *(¶4 — evidence on real subjects, each claim paired.)* We tie every claim to evidence: the
> actionable-fraction estimates carry bootstrap confidence intervals (Table 1); category
> differences are tested with corrected pairwise comparisons (Fig. 2); TriageFilter's retention
> and suppression are reported with effect sizes on **projects unseen during training** (Table 3);
> and an ablation replacing the language-model features with lexical ones isolates their marginal
> value (Table 4). Labels, code, prompts, and cached model outputs are in the anonymized artifact.
>
> *(¶5 — threats posture and what changes for SE.)* We state the central threat plainly: "a code
> change followed the comment" is a **correlational** proxy for "the comment caused it," and we
> bound it with a manually audited causal-plausibility subsample rather than claiming causation.
> The payoff for practice is concrete: teams can keep automated review *and* the attention it was
> meant to protect. Section 2 details the study design; Section 3 TriageFilter; Section 4 the
> evaluation; threats are argued alongside each result, not deferred. *(brief roadmap, no
> over-signposting.)*

---

## Why the "after" meets the FSE bar

Mapped to the skill checklists:

- **SE contribution on the first page** — the abstract and ¶1 pose a maintenance/review problem
  and an outcome-level question before any model detail (`fse-writing-style`: "lead with the
  software-engineering contribution").
- **Evidence proportional to the claim** — the claim is about *developer action*, so the evidence
  is action data on real projects with intervals and effect sizes, not accuracy against a proxy
  (`fse-experiments`: match the evidence to the claim shape).
- **Threats engaged where they live** — construct validity (proxy for causation) is named in ¶5
  and bounded with an audited subsample, and reported *with* results rather than quarantined
  (`fse-writing-style`: the threats section is an argument, not boilerplate).
- **Right venue, model-swap test passes** — the lesson (a minority of bot comments drive change;
  filtering protects attention) survives swapping the underlying model, so it is an FSE
  contribution, not an ML re-route (`fse-topic-selection`).
- **Open science by default** — labels, protocol, prompts, and *cached* model outputs are in an
  anonymized artifact, matching FSE's double-anonymous, data-availability expectations
  (`fse-reproducibility`, `fse-artifact-evaluation`).
- **Fair, contamination-aware evaluation** — held-out projects, a size-stratified fairness
  breakdown, and an ablation isolating the model's marginal value pre-empt the reviewer's first
  three objections (`fse-experiments`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified FSE
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for FSE-specific submission policy and
> the PACMSE journal-style cycle.
