# RecSys Exemplars Library (contribution type × evaluation shape)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against the
> **ACM Digital Library** and **dblp** to confirm it appeared at the **ACM Conference on
> Recommender Systems (RecSys)** — matching the proceedings edition, author list, year, and, where
> quoted, the DOI. Papers that could not be cleanly confirmed as **RecSys** (as opposed to a
> sibling venue) were **omitted and documented below**. This is deliberately a short, verified list
> (6 verified > 15 guessed).
>
> **Sibling-confusion guard:** RecSys is **not** SIGIR, KDD, WSDM, TheWebConf/WWW, or UAI. Several
> canonical "recommendation" papers actually live in those venues — a paper being *about*
> recommenders does **not** make it a RecSys paper (see omissions). Each row below was checked to
> be a RecSys edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent metric values, dataset numbers, or table entries — read the original in the
> ACM DL before citing anything. For RecSys-specific policy, scope, and the do-not-misattribute
> list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution type × evaluation shape** is closest to yours, then study how
that paper makes a **recommendation claim** land: a named user/item modeling idea, an evaluation
protocol that a skeptical reviewer cannot dismiss, and — the RecSys signature — an honest account
of the **gap between offline metrics and deployed behavior** (see
[`../../skills/recsys-writing-style/SKILL.md`](../../skills/recsys-writing-style/SKILL.md),
[`../../skills/recsys-topic-selection/SKILL.md`](../../skills/recsys-topic-selection/SKILL.md), and
[`../../skills/recsys-experiments/SKILL.md`](../../skills/recsys-experiments/SKILL.md)). For each,
ask the self-check before calling your paper "RecSys-shaped."

**RecSys edition ↔ year (verified rows below):** 10th = 2016 (Boston); 12th = 2018 (Vancouver);
13th = 2019 (Copenhagen); 18th = 2024 (Bari); 19th = 2025 (Prague).

---

## By contribution type

### Evaluation methodology / the reproducibility crisis

- **Ferrari Dacrema, Cremonesi & Jannach, "Are We Really Making Much Progress? A Worrying Analysis
  of Recent Neural Recommendation Approaches," RecSys 2019, DOI 10.1145/3298689.3347058 (Best Long
  Paper).** Verified on ACM DL and dblp (13th ACM Conference on Recommender Systems, Copenhagen).
  - **Why it is an exemplar:** shows that several published neural recommenders fail to beat
    **properly tuned** simple baselines under matched evaluation — the paper that crystallized
    RecSys's reproducibility debate and motivated the dedicated Reproducibility Track.
  - **Self-check:** are your baselines tuned with the *same* budget as your method, and would your
    reported gain survive a re-run by a hostile reviewer?

### Deployed industrial recommender (systems / scale)

- **Covington, Adams & Sargin, "Deep Neural Networks for YouTube Recommendations," RecSys 2016,
  pp. 191-198, DOI 10.1145/2959100.2959190.** Verified on ACM DL (10th ACM Conference on
  Recommender Systems, Boston).
  - **Why it is an exemplar:** a two-stage candidate-generation-plus-ranking architecture explained
    with the **production constraints** (freshness, scale, implicit feedback, live A/B outcomes)
    that make RecSys the home for deployment papers, not a generic deep-learning venue.
  - **Self-check:** does your systems paper report a constraint or an online result that an offline
    benchmark alone could never surface?

### Top-N recommendation algorithm (model contribution)

- **Christakopoulou & Karypis, "Local Item-Item Models for Top-N Recommendation," RecSys 2016
  (Best Paper).** Verified on ACM DL / dblp (10th ACM Conference on Recommender Systems, Boston).
  - **Why it is an exemplar:** improves top-N ranking by learning **local** item-item models for
    user subsets rather than one global model — a precise, nameable modeling idea evaluated on
    ranking metrics, the classic RecSys algorithm-paper shape.
  - **Self-check:** can you state the modeling primitive in one sentence, and is it evaluated as a
    ranking task rather than rating prediction?

### Counterfactual / off-policy recommendation (causal evaluation)

- **Bonner & Vasile, "Causal Embedding for Recommendation," RecSys 2018 (Best Long Paper).**
  Verified on ACM DL / dblp (12th ACM Conference on Recommender Systems, Vancouver).
  - **Why it is an exemplar:** frames recommendation as an **intervention** and optimizes for the
    incremental effect of a recommendation rather than logged clicks — the counterfactual framing
    behind off-policy evaluation, a RecSys distinctive that IR leaderboard framing misses.
  - **Self-check:** does your objective target the effect of *recommending*, and is logged-feedback
    bias handled by an estimator (IPS/SNIPS/DR) rather than ignored?

### Conversational recommendation (interaction / user modeling)

- **Zhang, Xie, Lyu, Xin, Ren, Liang, Zhang, Kang, de Rijke & Ren, "Towards Empathetic
  Conversational Recommender Systems," RecSys 2024 (Best Paper).** Verified via the RecSys 2024
  awards record and the authors' institutional announcements (18th ACM Conference on Recommender
  Systems, Bari).
  - **Why it is an exemplar:** moves conversational recommendation beyond accuracy toward **user
    experience** (empathy modeling) while keeping a measurable evaluation — the beyond-accuracy
    turn that RecSys rewards.
  - **Self-check:** if your contribution is a user-experience quality, do you operationalize it into
    something measurable rather than asserting it?

### Beyond-accuracy safety / risk control (fairness-adjacent guarantees)

- **De Toni, Consonni, Gómez, Purificato et al., "You Don't Bring Me Flowers: Mitigating Unwanted
  Recommendations Through Conformal Risk Control," RecSys 2025 (Best Paper).** Verified via the
  RecSys 2025 (Prague) awards record and the ECAT announcement (19th ACM Conference on Recommender
  Systems).
  - **Why it is an exemplar:** attaches a **distribution-free risk guarantee** to the suppression of
    unwanted recommendations — a rigorous statistical tool applied to a concrete recommender harm,
    pairing beyond-accuracy goals with a provable control.
  - **Self-check:** is your safety/fairness claim a *guarantee or a measured bound*, not a single
    aggregate fairness number on one split?

---

## By contribution type × evaluation shape (each cell is a verified RecSys paper above)

| Contribution type | Verified RecSys exemplar | Edition / year | Evaluation shape |
| --- | --- | --- | --- |
| Evaluation methodology / reproducibility | Ferrari Dacrema, Cremonesi & Jannach, "Are We Really Making Much Progress?" | 13th / 2019 | Tuned-baseline re-evaluation |
| Deployed industrial system | Covington, Adams & Sargin, "DNNs for YouTube Recommendations" | 10th / 2016 | Offline + production A/B |
| Top-N algorithm | Christakopoulou & Karypis, "Local Item-Item Models" | 10th / 2016 | Offline ranking metrics |
| Counterfactual / off-policy | Bonner & Vasile, "Causal Embedding for Recommendation" | 12th / 2018 | Logged-feedback / interventional |
| Conversational / user modeling | Zhang et al., "Towards Empathetic Conversational RecSys" | 18th / 2024 | Beyond-accuracy + user metrics |
| Beyond-accuracy risk control | De Toni et al., "You Don't Bring Me Flowers" | 19th / 2025 | Distribution-free risk guarantee |

> Six verified papers across six contribution × evaluation cells. The 2019 reproducibility paper
> and the 2018 causal-embedding paper together explain why RecSys reviewers weight **evaluation
> honesty** as heavily as raw metric wins.

---

## Omitted for lack of clean RecSys verification (do not attribute to RecSys without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Rendle, Freudenthaler, Gantner & Schmidt-Thieme, "BPR: Bayesian Personalized Ranking from
  Implicit Feedback"** — a foundational recommendation paper, but it is **UAI 2009**, **not
  RecSys**. A direct trap: canonical to recommenders, wrong venue.
- **He, Liao, Zhang, Nie, Hu & Chua, "Neural Collaborative Filtering"** — **WWW 2017
  (TheWebConf)**, **not RecSys**. Being about recommendation does not place it at RecSys.
- **Krichene & Rendle, "On Sampled Metrics for Item Recommendation"** — the sampled-metrics
  critique that every RecSys evaluation section now cites, but it is **KDD 2020**, **not RecSys**.
  Cite it *for* RecSys evaluation practice while attributing it to KDD.
- **Rendle, Krichene, Zhang & Anderson, "Neural Collaborative Filtering vs. Matrix Factorization
  Revisited," RecSys 2020** — this one *is* RecSys, but it was omitted from the verified rows only
  to keep the list short; add it (after re-confirming on ACM DL) if you need a second
  reproducibility exemplar.

Before adding any new paper, confirm it in the **ACM Digital Library** by matching the proceedings
edition (the volume names "ACM Conference on Recommender Systems") to the year, then record author
list, year, pages, and DOI, and update the access-date header. When in doubt, omit. If web search
is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
