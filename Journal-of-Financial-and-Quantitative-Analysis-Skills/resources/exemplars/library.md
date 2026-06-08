# *JFQA* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Financial and Quantitative Analysis_** (JFQA) — published by
> **Cambridge University Press** on behalf of the **Michael G. Foster School of Business, University of
> Washington** — with year and volume/issue, against the journal's own Cambridge Core article pages
> (`cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/...`), the JFQA
> editor-selected "sample content" list on Cambridge Core, and the RePEc IDEAS `cup/jfinqa` record. Papers
> that could not be fully verified **as _JFQA_** were **omitted** — this is deliberately a short, clean
> list, not a long, uncertain one.
>
> **Sibling-journal guard.** *JFQA* is **not** the *Journal of Finance* (JF, Wiley/AFA), the *Review of
> Financial Studies* (RFS, Oxford/SFS), or the *Journal of Financial Economics* (JFE, Elsevier) — the
> **top-3 traps**. It is *especially* confused with **JFE** (both publish reduced-form empirical corporate
> finance and asset pricing of the same shape) and, to a lesser degree, with RFS. Many famous "JFQA-sounding"
> papers live in those venues; the [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-jfqa)
> section records the traps checked and rejected.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, t-statistics, or specific findings — read the original on Cambridge
> Core before citing any number. For *JFQA*-specific scope, fees, blinding, and the code-sharing policy,
> see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × finance question** is closest to yours, then study how that paper turns a
financial-economics quantity into a contribution that clears the *JFQA* bar — a clean **identification or
measurement** advance in corporate finance, investments, capital markets, or financial institutions, with
**quantitative discipline** (see [`../../skills/jfqa-topic-selection/SKILL.md`](../../skills/jfqa-topic-selection/SKILL.md),
[`../../skills/jfqa-identification-strategy/SKILL.md`](../../skills/jfqa-identification-strategy/SKILL.md), and
[`../../skills/jfqa-contribution-framing/SKILL.md`](../../skills/jfqa-contribution-framing/SKILL.md)). For each,
ask the self-check question before claiming your paper is "*JFQA*-shaped."

---

## By method

### Difference-in-differences off a policy/market discontinuity (financial institutions)

- **Akins, Li, Ng & Rusticus, "Bank Competition and Financial Stability: Evidence from the Financial Crisis," _JFQA_ 2016, 51(1):1–28.**
  Verified: `cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/bank-competition-and-financial-stability-evidence-from-the-financial-crisis/02EA25A2BB6353F16DCEE34962152F43` (also the JFQA editor-selected sample-content list; RePEc `cup/jfinqa`).
  - **Why it is an exemplar:** exploits **state-level variation in banking competition** and treats the
    crisis as a stress test, so the competition–stability link is identified off cross-state differences
    rather than a raw correlation — the [`jfqa-identification-strategy`](../../skills/jfqa-identification-strategy/SKILL.md)
    move of finding plausibly exogenous variation in the right-hand-side variable.
  - **Self-check:** is your treatment variation defensibly exogenous to the outcome, or could a third factor
    drive both competition and stability in the same states?

### Event study with a structurally interpreted magnitude (corporate governance / misconduct)

- **Karpoff, Lee & Martin, "The Cost to Firms of Cooking the Books," _JFQA_ 2008, 43(3):581–611.**
  Verified: `cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/cost-to-firms-of-cooking-the-books/4BFFF52B30A4997F2ED5EA8BDA69CD1A` (RePEc `cup/jfinqa/v43y2008i03p581-611`).
  - **Why it is an exemplar:** decomposes the market value lost on revelation of financial misrepresentation
    into a **legal/regulatory penalty** and a much larger **reputational penalty**, turning an event-study
    abnormal return into an economically interpretable cost per dollar inflated — the
    [`jfqa-contribution-framing`](../../skills/jfqa-contribution-framing/SKILL.md) discipline of reporting a
    magnitude with an economic interpretation, not just a sign.
  - **Self-check:** can you decompose your event-window value change into named economic components, or do you
    only have a significant abnormal return?

### Cross-country institutional panel (capital structure / international finance)

- **Fan, Titman & Twite, "An International Comparison of Capital Structure and Debt Maturity Choices," _JFQA_ 2012, 47(1):23–56.**
  Verified: `cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/an-international-comparison-of-capital-structure-and-debt-maturity-choices/683E740C9E453346363FB692B52BC914` (RePEc `cup/jfinqa`; JFQA sample-content list).
  - **Why it is an exemplar:** uses **39 countries** to let legal system, tax code, corruption, and the
    preferences of capital suppliers explain leverage and debt-maturity, exploiting cross-country
    institutional variation a single-country study cannot — the [`jfqa-topic-selection`](../../skills/jfqa-topic-selection/SKILL.md)
    "use the institutional cross-section as the source of identifying variation" move.
  - **Self-check:** does your cross-country design isolate a specific institutional channel, or just add
    country fixed effects to a pooled regression?

### Laboratory experiment with physiological measurement (behavioral finance)

- **Kuhnen & Knutson, "The Influence of Affect on Beliefs, Preferences, and Financial Decisions," _JFQA_ 2011, 46(3):605–626.**
  Verified: `cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/influence-of-affect-on-beliefs-preferences-and-financial-decisions/09587FE55D92A6CBF1CA3D968F7893F1` (RePEc `cup/jfinqa/v46y2011i03p605-626`).
  - **Why it is an exemplar:** uses a **controlled experiment with exogenous affect manipulation** to show
    that emotional state changes both risk preferences and belief updating — clean identification of a
    mechanism that observational market data cannot isolate, the [`jfqa-identification-strategy`](../../skills/jfqa-identification-strategy/SKILL.md)
    experimental-control route to causality.
  - **Self-check:** does your experiment manipulate exactly one channel and measure both the preference and
    the belief response, or does it confound them?

### Descriptive decomposition that reframes a stylized fact (IPOs / market structure)

- **Gao, Ritter & Zhu, "Where Have All the IPOs Gone?," _JFQA_ 2013, 48(6):1663–1692.**
  Verified: `cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/where-have-all-the-ipos-gone/4687B99460F170D9F290EA9EC587B41A` (DOI 10.1017/S0022109014000015; JFQA sample-content list).
  - **Why it is an exemplar:** documents and **decomposes** the post-2000 collapse in small-firm IPOs,
    weighing a regulatory-overreach story against an economies-of-scope story — a measurement/decomposition
    contribution that disciplines competing narratives with data, the [`jfqa-contribution-framing`](../../skills/jfqa-contribution-framing/SKILL.md)
    "name the rival explanations and let the decomposition adjudicate" move.
  - **Self-check:** does your descriptive paper *adjudicate between named explanations*, or does it stop at
    documenting the pattern?

---

## By topic (each cell is a verified _JFQA_ paper above)

| Topic | Verified _JFQA_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Financial institutions / banking | Akins, Li, Ng & Rusticus, "Bank Competition & Financial Stability" | 2016, 51(1) | DiD off cross-state competition |
| Corporate governance / misconduct | Karpoff, Lee & Martin, "Cost to Firms of Cooking the Books" | 2008, 43(3) | Event study + cost decomposition |
| Capital structure / international | Fan, Titman & Twite, "International Comparison of Capital Structure" | 2012, 47(1) | Cross-country institutional panel |
| Behavioral finance | Kuhnen & Knutson, "Influence of Affect on … Financial Decisions" | 2011, 46(3) | Lab experiment w/ affect manipulation |
| IPOs / market structure | Gao, Ritter & Zhu, "Where Have All the IPOs Gone?" | 2013, 48(6) | Descriptive decomposition |

---

## Omitted for lack of full verification (do not attribute to _JFQA_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _JFQA_** (the sibling-journal traps the brief warned of):

- **Hou, Xue & Zhang, "Digesting Anomalies: An Investment Approach" (2015)** — verified in the **_Review of
  Financial Studies_** 28(3):650–705, **not _JFQA_**. The q-factor model paper (RFS, the near-sibling).
- **Bessembinder, "Do Stocks Outperform Treasury Bills?" (2018)** — verified in the **_Journal of Financial
  Economics_** 129(3):440–457, **not _JFQA_**. (Note: Bessembinder is a JFQA Managing Editor, which makes this
  an easy mis-attribution — but the paper is JFE, the closest sibling.)
- **Goldstein, Ozdenoren & Yuan, "Trading Frenzies and Their Impact on Real Investment" (2013)** — verified
  in the **_Journal of Financial Economics_** 109(2):566–582, **not _JFQA_**.
- **Chang, Hong & Liskovich, "Regression Discontinuity and the Price Effects of Stock Market Indexing" (2015)**
  — verified in the **_Review of Financial Studies_** 28(1):212–246, **not _JFQA_**. The canonical S&P 500
  index-inclusion RDD.
- **Brunnermeier & Pedersen, "Market Liquidity and Funding Liquidity" (2009)** — verified in the **_Review of
  Financial Studies_** 22(6):2201–2238, **not _JFQA_**.

Before adding any new paper to this library, confirm it on Cambridge Core
(`cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis`) with volume/issue, and update
the access-date header. When in doubt, **omit**.
