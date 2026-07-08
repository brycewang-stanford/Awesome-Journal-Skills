> **Illustrative teaching example.** The paper, system, datasets, and every number
> below are **fictional**, invented solely to demonstrate the WSDM register. No real
> results are quoted and no venue policy is invented. Companion skills:
> [`wsdm-writing-style`](../../skills/wsdm-writing-style/SKILL.md),
> [`wsdm-experiments`](../../skills/wsdm-experiments/SKILL.md),
> [`wsdm-author-response`](../../skills/wsdm-author-response/SKILL.md).

# Worked Example: A WSDM-Style Abstract + Introduction (before → after)

The rewrite demonstrates the three WSDM-specific disciplines this pack teaches:

1. **Behavior-first framing** - open on a measured fact about users or platforms,
   not on a model family (`wsdm-writing-style`).
2. **Bias-aware claims** - every effectiveness statement carries its evaluation
   regime, because this PC assumes interaction data is biased until told otherwise
   (`wsdm-experiments`).
3. **Self-containment** - WSDM historically has no rebuttal, so the introduction
   pre-answers the objections a reviewer would otherwise raise into silence
   (`wsdm-author-response`).

**Fictional paper:** *"Dwell-Debiased Ranking for Short-Session Marketplace
Search."* Fictional setting: search over a second-hand marketplace where sessions
are short and clicks are dominated by photo attractiveness rather than item
relevance.

---

## Before (a competent draft that would struggle at WSDM)

> **Abstract.** Deep learning has revolutionized search ranking. In this paper, we
> propose DwellRank, a novel end-to-end framework that leverages dwell time signals
> with a transformer architecture. Extensive experiments on real-world datasets
> demonstrate that DwellRank significantly outperforms state-of-the-art baselines.
> We also deploy DwellRank in a real system, where it achieves substantial gains.
>
> **Introduction.** Search is important for e-commerce platforms. Recently, deep
> models have achieved great success in ranking. However, existing methods do not
> fully exploit dwell time. We propose DwellRank, which incorporates dwell time via
> a novel attention mechanism. Our contributions are: (1) a novel framework; (2) a
> new attention mechanism; (3) extensive experiments demonstrating superiority.

**Why this fails the WSDM read**, mapped to the skills:

- Opens on "deep learning has revolutionized" - a model-first move that tells a
  single-track audience nothing about the behavioral problem
  (`wsdm-writing-style`: behavior-first openings).
- "Real-world datasets," "significantly outperforms," "substantial gains" - three
  entries straight from the tells table: no dataset identity, no test, no
  measurement protocol, no evaluation regime.
- Dwell time is treated as a free signal. Any WSDM reviewer immediately objects
  that dwell is confounded (long dwell can mean confusion, not satisfaction) and
  position-biased - and there is no rebuttal in which to answer them.
- "Novel framework" twice, mechanism never named (`wsdm-writing-style`).
- The deployment claim is unquantified and un-protocolled - an *attested* result
  presented without its protocol (`wsdm-reproducibility` honesty ladder).

---

## After (the WSDM register)

> **Abstract.** In marketplace search, half of all sessions end within two result
> pages, and clicks concentrate on visually salient listings regardless of
> relevance - so a ranker trained on raw clicks learns photo quality, not item
> match. We show on twelve weeks of logs from a European second-hand marketplace
> (anonymized; 41M sessions) that click-trained rankers overweight image salience
> relative to human relevance judgments, and that raw dwell time inherits the same
> confound because salient-but-irrelevant listings also hold attention. We
> introduce **dwell-curve debiasing (DCD)**: a two-parameter correction that
> models dwell as a mixture of inspection and engagement, estimated per category
> from abandonment behavior with no editorial labels. Under temporal splits and
> full-corpus ranking, DCD improves nDCG@10 over the strongest click-model
> baseline on both our logs and a public e-commerce benchmark (paired test over
> queries, p < 0.01, 5 seeds), with the largest gains on tail queries. A four-week
> 5%-traffic A/B test showed purchase-per-search improvements consistent with the
> offline deltas; we report the protocol and a category where the correction
> underperforms. Code and the public-benchmark pipeline are released; the log
> data cannot be shared, and we document sampled statistics to support
> replication.
>
> **Introduction (first two paragraphs).** Buyers on second-hand marketplaces
> decide fast: in our logs, the median session inspects 1.7 result pages, and the
> click-through curve by position is steeper than published web-search curves.
> Under such truncated exposure, click-trained rankers face a compounded bias -
> position bias determines *what is seen*, and image salience determines *what is
> clicked among the seen*. The practical consequence, which we measure in
> Section 3, is that a production-grade click ranker ranks visually attractive
> mismatches above plainly photographed exact matches for one query in nine.
>
> Dwell time is the standard remedy, on the intuition that users linger on
> relevant items. We show the intuition breaks in this regime: dwell on salient
> mismatches is statistically indistinguishable from dwell on true matches for
> short sessions (Section 3.2), so dwell-weighted training reproduces the
> confound it was meant to fix. Our correction starts from a different behavioral
> observation - *abandonment after long dwell* separates inspection from
> engagement...

**What changed, move by move:**

| Move | Before | After |
| --- | --- | --- |
| Opening | Model family ("deep learning has...") | Measured behavior (session depth, salience-click concentration) |
| Data identity | "real-world datasets" | Named regime: 12 weeks, 41M sessions, anonymized marketplace + public benchmark |
| Claim regime | "significantly outperforms SOTA" | Metric @ cutoff, temporal splits, full-corpus ranking, paired test, seeds |
| The obvious objection | Unaddressed (dwell is confounded) | Made into a *finding* (Section 3.2) that motivates the method |
| Mechanism | "novel framework/attention" | Named and scoped: two-parameter mixture correction, estimated from abandonment |
| Deployment | "substantial gains" | Attested with protocol: duration, traffic share, metric, plus a reported failure category |
| Artifact honesty | Silent | Code + public pipeline released; log-data limits stated with a replication path |

The deepest change is the third row of the table: the strongest objection to the
draft (dwell is confounded) became the paper's second contribution. That is the
no-rebuttal discipline in action - at a venue where you will never get to reply,
the best place for your rebuttal is Section 3.

---

> Next: check your own draft against the objection-inventory method in
> [`wsdm-author-response`](../../skills/wsdm-author-response/SKILL.md), then
> benchmark the framing against the real, DOI-verified papers in
> [`../exemplars/library.md`](../exemplars/library.md).
