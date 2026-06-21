> **Illustrative teaching example.** The paper, model, sample, and every number below are **fictional**
> and exist only to demonstrate Cognitive Psychology house style. No real-paper facts and no journal
> policy are invented here — policy lives in [`../official-source-map.md`](../official-source-map.md).
> Corresponding skills: [`cogpsych-writing-style`](../../skills/cogpsych-writing-style/SKILL.md),
> [`cogpsych-literature-positioning`](../../skills/cogpsych-literature-positioning/SKILL.md),
> [`cogpsych-theory-and-hypotheses`](../../skills/cogpsych-theory-and-hypotheses/SKILL.md),
> [`cogpsych-study-design`](../../skills/cogpsych-study-design/SKILL.md), and
> [`cogpsych-data-analysis`](../../skills/cogpsych-data-analysis/SKILL.md).

# Worked Example: A Cognitive Psychology Introduction (before → after)

This demonstrates the **Cognitive Psychology Introduction arc** that the pack's skills require:
**theoretical question framed as a live debate between formal accounts → name the rival models and what
each predicts → why prior evidence cannot settle the fork → the discriminating, multi-experiment design
→ the model-driven contribution**. Cognitive Psychology favors **longer, integrative, model-driven**
articles, so the Introduction does real theoretical work: it sets up a model comparison the experiments
will resolve (`cogpsych-literature-positioning`, `cogpsych-theory-and-hypotheses`).

A note on scope for this pack: the contribution here is a **model fit to data across several
experiments**, not a single effect. The persuasive work is **formalization, a discriminating design,
and model comparison with recovery** — see [`cogpsych-data-analysis`](../../skills/cogpsych-data-analysis/SKILL.md).

**Illustrative paper (fictional):** *"One Signal or Two? Adjudicating Continuous-Strength and
Dual-Process Accounts of Recognition Memory."* Fictional setting: three preregistered confidence-rating
recognition experiments engineered to make the z-ROC shape diagnostic, with two competing formal models
fit and compared.

---

## Before (buries the theory — typical first-draft intro)

> Recognition memory has been studied extensively for many decades, and a large literature has examined
> how people distinguish previously seen items from new ones. Many experiments have used confidence
> ratings and ROC analysis, and various models have been proposed. In the present research we conducted
> three experiments on recognition memory using a confidence-rating procedure. We fit a model to the
> data and examined how well it accounted for the results. We predicted that our model would fit the
> data well. Recognition memory is an important topic with applications to eyewitness testimony and
> aging. The remainder of this article describes our experiments, presents the model fits, and discusses
> the implications.

**What's wrong (against `cogpsych-literature-positioning` / `cogpsych-theory-and-hypotheses` /
`cogpsych-topic-selection`):**

- **No theoretical fork.** The reader cannot tell which accounts are in contention or what separates
  them — the venue is built on adjudicating models (`cogpsych-literature-positioning`).
- **The model is "a model."** No rival, no discriminating prediction; "we predicted our model would fit
  well" is the **"just a curve fit"** anti-pattern (`cogpsych-theory-and-hypotheses`).
- **Throat-clearing history** ("studied extensively") that does no theoretical work.
- **No design logic** — nothing says why three experiments, or what each adds; the multi-experiment
  program reads as a pile of studies (`cogpsych-study-design`).
- **No signal of rigor** — no model comparison, no recovery, no mention of reproducible code, which is
  exactly what this venue treats as load-bearing (`cogpsych-data-analysis`,
  `cogpsych-open-science-and-transparency`).
- **Over-signposted roadmap** doing work the argument should do.

---

## After (Cognitive Psychology arc — a model fork the experiments resolve)

> **Does recognition memory rest on a single continuous memory-strength signal, or on a distinct
> threshold recollection process operating alongside familiarity?** This question has organized memory
> theory for decades, and it remains unresolved because the two accounts are usually tested one at a
> time, on designs where their predictions barely diverge. *(the theoretical fork, framed as a live
> debate — not "little is known.")*
>
> The continuous-strength view is formalized by the unequal-variance signal-detection (UVSD) model, in
> which old and new items differ in mean and variance of a single strength axis. The dual-process view
> (DPSD) adds a threshold recollection process to a familiarity signal. Critically, the two models make
> a **divergent qualitative prediction about the shape of the z-transformed ROC**: UVSD predicts a
> linear z-ROC with slope below one, whereas DPSD predicts a characteristic curvature. *(rival models in
> matched formal language, and the signature that separates them — per
> [`cogpsych-theory-and-hypotheses`](../../skills/cogpsych-theory-and-hypotheses/SKILL.md).)*
>
> Most prior tests cannot adjudicate the accounts because their list structures leave the z-ROC shape
> only weakly diagnostic, and because they fit one model without a matched-flexibility rival or a
> recovery check. *(why the existing evidence cannot settle the fork — a theoretical gap, not a
> coverage gap.)*
>
> We report **three preregistered confidence-rating experiments engineered to make the z-ROC shape
> diagnostic**. Experiment 1 establishes the pattern under a high-resolution confidence scale;
> Experiment 2 rules out a list-composition confound; Experiment 3 tests a further divergent prediction
> under a strength manipulation. Sample sizes and trials per confidence bin were fixed in advance by
> model-recovery simulation, so the design can recover the generating model at our N and trial counts.
> *(the discriminating, multi-experiment design; each experiment adds inference — per
> [`cogpsych-study-design`](../../skills/cogpsych-study-design/SKILL.md).)*
>
> Fitting both models under matched flexibility with hierarchical Bayesian estimation, we find that
> across all three experiments the z-ROC is reliably **linear**, the signature UVSD predicts and DPSD
> forbids; UVSD is favored by penalized comparison (illustrative dBIC = 14; Bayes factor ~ 30) and the
> comparison is interpretable because parameter and model recovery succeed. *(the model-driven result —
> a crossed qualitative prediction corroborated by a recovered, penalized comparison, not a fit index
> alone; per [`cogpsych-data-analysis`](../../skills/cogpsych-data-analysis/SKILL.md).)*
>
> Our contribution is to **adjudicate** a long-running debate with a design built to discriminate the
> models rather than to fit one of them: recognition behaves, across these conditions, as a single
> continuous-strength process. This constrains the memory models inherited by research on cognitive
> aging, eyewitness identification, and confidence-based decision making. *(contribution stated early,
> relative to a specific theoretical fork, with breadth made explicit.)* All data, model-fitting code,
> and materials are openly available so the reported fits regenerate in a fresh session (see
> [`cogpsych-open-science-and-transparency`](../../skills/cogpsych-open-science-and-transparency/SKILL.md)).

---

## Why the "after" meets the Cognitive Psychology bar

Mapped to the pack's skill checklists:

- **A theoretical fork, not an effect** — the Introduction sets up UVSD vs. DPSD and the z-ROC signature
  that separates them, the adjudication the venue rewards (`cogpsych-literature-positioning`,
  `cogpsych-topic-selection`).
- **Formal models with a discriminating prediction** — both rivals are stated in matched formal
  language and the crossed qualitative prediction is named, defusing the "just a curve fit" objection
  (`cogpsych-theory-and-hypotheses`).
- **Design logic is explicit** — three experiments each add inference (establish, rule out a confound,
  test a further prediction), with sample size fixed by **model-recovery simulation**
  (`cogpsych-study-design`).
- **Model comparison + recovery, not a single fit** — UVSD is favored by a penalized criterion and the
  comparison is interpretable because recovery succeeds (`cogpsych-data-analysis`).
- **Reproducibility signposted** — open data, **model code**, and materials are flagged where the venue
  expects them; exact policy is deferred to [`../official-source-map.md`](../official-source-map.md),
  not invented.
- **One-sentence hook is fillable:** "We show that [recognition rests on a single continuous-strength
  signal] by [engineering three experiments to make the z-ROC diagnostic and comparing UVSD against
  DPSD with recovery]" — both brackets filled, as `cogpsych-topic-selection` asks.

> Next: formalize your own model fork in
> [`cogpsych-theory-and-hypotheses`](../../skills/cogpsych-theory-and-hypotheses/SKILL.md), then design
> the discriminating experiments in
> [`cogpsych-study-design`](../../skills/cogpsych-study-design/SKILL.md).
