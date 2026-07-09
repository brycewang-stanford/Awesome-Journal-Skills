> **Illustrative teaching example.** The paper, method, setting, and every number below are
> **fictional** and exist only to demonstrate RecSys house style. No real-paper facts, datasets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`recsys-writing-style`](../../skills/recsys-writing-style/SKILL.md),
> [`recsys-topic-selection`](../../skills/recsys-topic-selection/SKILL.md), and
> [`recsys-experiments`](../../skills/recsys-experiments/SKILL.md).

# Worked Example: A RecSys-Style Abstract + Introduction (before → after)

This demonstrates the **RecSys first-page arc** from `recsys-writing-style`:
**recommendation problem → why current methods mislead → method → offline evidence with tuned
baselines → the offline-to-deployment bridge → why it matters to a recommender audience** — with
the RecSys rules that the contribution is a **recommendation** result, that **baselines are tuned
with an equal budget**, and that the paper is **honest about the gap between an offline metric and
live user behavior**.

The framing also reflects `recsys-topic-selection`: RecSys is strongest when the claim is about
**recommendation** — ranking, user/item modeling, feedback loops, deployed behavior — not a generic
learning advance (which would route to a ML venue) or a search/ranking result untethered from
recommendation (which leans SIGIR).

**Illustrative paper (fictional):** *"Exposure-Aware Off-Policy Ranking for Session Recommenders."*
Fictional method: a session ranker trained against a logged-feedback estimator that corrects for
which items the previous system exposed.

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Recommender systems are widely used in industry. In this work we propose a new deep
> session-based recommendation model that combines an attention mechanism with a novel loss and
> achieves state-of-the-art results on three datasets, outperforming strong baselines on Recall@20
> and nDCG@20.
>
> **Introduction.** Recommendation has been studied for decades. Many neural approaches exist,
> including RNN, attention, and graph models. In this paper we use an attention-based architecture
> with an auxiliary loss, trained on logged clicks, to rank the next item in a session. We evaluate
> on standard datasets with a random 80/20 split and show our method works well. Section 2 reviews
> related work, Section 3 describes the model, Section 4 presents experiments, Section 5 concludes.

**What's wrong (against `recsys-writing-style` / `recsys-topic-selection` / `recsys-experiments`):**

- **No recommendation contribution on the first page** — leads with "widely used in industry,"
  not a problem, a gap, or a mechanism.
- **The reproducibility red flag is baked in** — "outperforming strong baselines" with no word on
  whether baselines were **tuned with the same budget**; this is the exact `recsys-experiments`
  reject pattern the 2019 "Are we really making much progress?" paper made famous.
- **A random split on session data leaks the future** — training on clicks that occur *after* test
  clicks; RecSys reviewers expect a **temporal** split for sequential data.
- **Logged clicks treated as ground truth** — no acknowledgement of **exposure bias**: the model is
  scored on items the old system chose to show, so offline gains may not transfer.
- **No offline-to-online bridge** — "works well" is never connected to any claim about deployed
  behavior, an A/B test, or an off-policy estimate.
- **Venue-misfit framing** — pitched as a generic deep-learning win, not a recommendation result.

---

## After (RecSys arc — problem → gap → method → tuned evidence → deployment bridge → why it matters)

> **Abstract.** Session recommenders are trained and evaluated on **logged clicks**, but those clicks
> only cover items the *previous* system exposed, so offline Recall can rise while live engagement
> does not. We introduce **exposure-aware off-policy ranking (EOR)**, which trains a session ranker
> against a **self-normalized inverse-propensity estimate** of next-item reward, using logged
> exposure propensities to correct for what the old policy showed. On three public session datasets
> with a **temporal** split, EOR improves nDCG@20 over baselines that are each **tuned under an equal
> search budget**, and — the load-bearing result — its **off-policy estimated reward** tracks a
> simulated online metric where a naively-trained ranker's offline gain does not. We report mean ±
> standard deviation over five seeds and release an anonymous repository that regenerates every
> ranking table. *(problem → gap → method → tuned offline evidence → deployment bridge → uncertainty
> reported — all on the first page.)*
>
> **Introduction.** *(¶1 — problem + contribution, first breath.)* A session recommender is judged by
> whether its next-item ranking improves **real engagement**, yet it is trained on **clicks logged by
> a previous policy**, which only ever exposed a subset of items. We give **exposure-aware off-policy
> ranking**, which optimizes an estimator of next-item reward that corrects for that exposure, so the
> offline objective is aligned with the quantity deployment cares about.
>
> *(¶2 — gap: why current practice misleads.)* Standard practice is insufficient for nameable
> reasons. Training on raw logged clicks inherits **exposure bias**: unshown-but-relevant items are
> invisible to the loss, so the ranker learns the old policy's blind spots. Evaluating on a **random
> split** of session data **leaks future interactions** into training, inflating offline metrics.
> And reporting a win over **under-tuned** baselines — the failure catalogued across RecSys
> reproducibility studies — can manufacture a gain that a fair tuning budget erases. *(each prior
> practice gets a specific failure, not a vague "prior work is limited.")*
>
> *(¶3 — method + the explicit assumption.)* EOR weights each logged interaction by the inverse of
> its exposure propensity and self-normalizes to control variance. The **assumption** is **positivity
> with logged propensities**: every item had nonzero exposure probability and those propensities are
> recoverable from the logs; we state where this holds and where it is approximate. *(assumption
> stated plainly, per the RecSys rule that off-policy claims hide their propensity assumptions.)*
>
> *(¶4 — evidence, each claim tuned and paired.)* On three public session datasets under a temporal
> split, EOR raises nDCG@20 over four baselines **each tuned with the same budget** (Table 1); an
> ablation removing the exposure correction removes the gain (Table 2), isolating the mechanism.
> Crucially, in a semi-synthetic simulator with a known reward, EOR's **off-policy estimate** and the
> **simulated online reward** move together, while a click-trained ranker's offline nDCG rises
> without any online gain (Fig. 1) — the offline-to-online bridge. **All numbers are mean ± sd over
> five seeds**, with the split, propensity model, and tuning grid in the appendix.
>
> *(¶5 — why it matters to recommender researchers + roadmap.)* The contribution is to make an
> **offline session-ranking objective predictive of deployed behavior** by treating exposure as the
> confounder it is — useful to anyone who must ship from offline evidence. Section 3 defines the
> estimator and its assumption; Section 4 reports the tuned offline study and the simulator bridge.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the RecSys bar

Mapped to the skill checklists:

- **Recommendation contribution on the first page** — the abstract and ¶1 name the problem
  (exposure-biased logged clicks), the gap, the method, and the deployment quantity before any
  architecture detail (`recsys-writing-style`: put the recommendation result first).
- **Tuned baselines** — the win is explicitly over baselines tuned under an **equal budget**, the
  single most important defence against the RecSys reproducibility critique
  (`recsys-experiments`; `recsys-reproducibility`).
- **Leakage-aware split** — a **temporal** split replaces the random split, matching sequential
  evaluation practice (`recsys-experiments`).
- **Offline-to-online honesty** — a simulator/off-policy bridge connects the offline metric to a
  deployment quantity instead of asserting "works well" (`recsys-experiments`: offline-vs-online).
- **Uncertainty reported** — mean ± sd over five seeds, not a single best run
  (`recsys-experiments`: report variance).
- **Right venue** — the claim is a **recommendation** result grounded in feedback loops and
  exposure, a strong RecSys fit rather than a generic-ML or SIGIR re-route
  (`recsys-topic-selection`).
- **Page discipline** — the propensity model, split, and tuning grid sit in the appendix while the
  8-page body carries the argument (`recsys-writing-style`; `recsys-supplementary`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified RecSys
> papers** (ACM DL) whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for RecSys-specific submission policy.
