# JFE Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-07.** Every paper below was checked to confirm it
> actually appeared in *The Journal of Financial Economics* (Elsevier / North-Holland, ISSN 0304-405X) —
> not the *Journal of Finance* (Wiley) or the *Review of Financial Studies* (Oxford), which are the two
> journals most easily confused with JFE. Verification used the article's ScienceDirect `0304-405X` /
> `S0304405X...` identifier and/or its RePEc handle `RePEc:eee:jfinec` (`eee` = Elsevier, `jfinec` = JFE).
> Papers that could not be confirmed as JFE were **omitted** and are listed at the bottom as guardrails —
> it is deliberately a short, clean list rather than a long, uncertain one.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent regression coefficients, alphas, or specific findings — read the original on
> ScienceDirect / the authors' pages before citing any number. For JFE-specific policy, masthead, scope,
> and a "do-not-misattribute" list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*credible, exhaustively-defended* result carry a *first-order* financial-economics lesson — the JFE bar
(see [`../../skills/jfe-topic-selection/SKILL.md`](../../skills/jfe-topic-selection/SKILL.md),
[`../../skills/jfe-empirical-design/SKILL.md`](../../skills/jfe-empirical-design/SKILL.md), and
[`../../skills/jfe-identification/SKILL.md`](../../skills/jfe-identification/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JFE-shaped."

The two JFE best-paper prizes mark the two lanes: the **Jensen Prize** (best corporate-finance /
organizations paper) and the **Fama-DFA Prize** (best asset-pricing / capital-markets paper). Aim at a
paper that could plausibly compete in one of them.

---

## By method

### The theory foundation a JFE empirical paper extends (financial-economics theory)

- **Jensen & Meckling, "Theory of the Firm: Managerial Behavior, Agency Costs and Ownership Structure," JFE 1976, 3(4):305–360.**
  Verified: ScienceDirect `pii/0304405X7690026X`; RePEc `eee/jfinec/v3y1976i4p305-360`.
  - **Why it is an exemplar:** the single most-cited JFE paper; it states one mechanism — the agency
    conflict between managers and owners — so cleanly that it became the lineage essentially every
    corporate-finance JFE paper now positions against. The JFE register rewards a plainly-stated
    economic mechanism (see [`../../skills/jfe-literature-positioning/SKILL.md`](../../skills/jfe-literature-positioning/SKILL.md)).
  - **Self-check:** does your corporate-finance result name the economic mechanism (agency, information,
    incentives) it identifies, or only a correlation?

### Cross-sectional asset pricing — a return pattern that breaks a model (asset pricing)

- **Banz, "The Relationship Between Return and Market Value of Common Stocks" (the size effect), JFE 1981, 9(1):3–18.**
  Verified: ScienceDirect `pii/0304405X81900180`; RePEc `eee/jfinec/v9y1981i1p3-18`.
  - **Why it is an exemplar:** documents a cross-sectional return pattern (small firms earn higher
    risk-adjusted returns) that the CAPM cannot price — a disciplined-inference finding that reshaped the
    factor-pricing agenda. The construction bar a new characteristic must clear descends from here.
  - **Self-check:** is your return pattern shown to survive correct risk adjustment, not just a raw
    average-return sort?

### Multi-factor model construction and spanning (asset pricing)

- **Fama & French, "Common Risk Factors in the Returns on Stocks and Bonds," JFE 1993, 33(1):3–56.**
  Verified: RePEc `eee/jfinec/v33y1993i1p3-56`; ScienceDirect `pii/0304405X93900235`.
  - **Why it is an exemplar:** the canonical JFE asset-pricing construction — size and book-to-market
    factors built from disciplined sorts, validated against the cross-section. It defines the benchmark
    set (CAPM → FF3 → FF5) that [`jfe-empirical-design`](../../skills/jfe-empirical-design/SKILL.md)
    requires a new factor to be spanned against.
  - **Self-check:** are your portfolio sorts, breakpoints, and weighting defined precisely enough to
    replicate, and is your factor's alpha measured against multiple benchmark models?

### Governance and firm value, panel regression with controls (corporate finance)

- **Yermack, "Higher Market Valuation of Companies with a Small Board of Directors," JFE 1996, 40(2):185–211.**
  Verified: ScienceDirect `pii/0304405X95008445`; RePEc `eee/jfinec/v40y1996i2p185-211`.
  - **Why it is an exemplar:** an early, careful governance–value study whose contribution is a robust
    *fact* (board size is inversely related to valuation) defended with an exhaustive control battery —
    the kind of measurement-and-inference discipline JFE referees demand even before a causal design.
  - **Self-check:** if your headline is an association, is it defended against the full control set and
    selection stories a JFE referee will raise — or does it need an identifying design (see
    [`jfe-identification`](../../skills/jfe-identification/SKILL.md))?

### Event study around corporate transactions (corporate finance / capital markets)

- **Schwert, "Markup Pricing in Mergers and Acquisitions," JFE 1996, 41(2):153–192.**
  Verified: RePEc `eee/jfinec/v41y1996i2p153-192`.
  - **Why it is an exemplar:** a disciplined event-study design that decomposes target returns into
    pre-bid runup versus post-bid markup, and uses that decomposition to adjudicate competing hypotheses
    about deal pricing — abnormal returns put to work answering an economic question, not just reported.
  - **Self-check:** does your event study estimate abnormal returns to *test a hypothesis about a
    mechanism*, with a defensible event window and benchmark, rather than tabulate CARs for their own
    sake?

### Cross-sectional predictor with horse-race / subsumption discipline (asset pricing)

- **Ball, Gerakos, Linnainmaa & Nikolaev, "Accruals, Cash Flows, and Operating Profitability in the Cross Section of Stock Returns," JFE 2016, 121(1):28–45.**
  Verified: ScienceDirect `pii/S0304405X16300307`; RePEc `eee/jfinec/v121y2016i1p28-45`.
  - **Why it is an exemplar:** a modern cross-sectional asset-pricing paper that does not merely add a
    predictor but shows a *cash-based* profitability measure **subsumes** accruals and the
    profitability-with-accruals factor — exactly the horse-race / spanning discipline
    [`jfe-empirical-design`](../../skills/jfe-empirical-design/SKILL.md) asks for when a characteristic is
    one of many candidates.
  - **Self-check:** does your predictor survive a horse race against the closest existing factors, with a
    spanning regression showing what it adds beyond them?

---

## By topic (each cell is a verified JFE paper above)

| Topic | Verified JFE exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Agency / theory of the firm | Jensen & Meckling, "Theory of the Firm" | 1976, 3(4) | Financial-economics theory |
| Size effect / cross-section | Banz, "Return and Market Value of Common Stocks" | 1981, 9(1) | Cross-sectional asset pricing |
| Factor models / risk | Fama & French, "Common Risk Factors" | 1993, 33(1) | Portfolio sorts + factor construction |
| Board governance / firm value | Yermack, "Small Board of Directors" | 1996, 40(2) | Panel regression + controls |
| Mergers & acquisitions | Schwert, "Markup Pricing in M&A" | 1996, 41(2) | Event study |
| Anomalies / profitability | Ball, Gerakos, Linnainmaa & Nikolaev, "Accruals, Cash Flows…" | 2016, 121(1) | Cross-sectional horse race / spanning |

---

## Omitted for being a different journal (do NOT attribute to JFE)

To keep the list zero-hallucination, the following famous finance papers were checked and **excluded**
because they are *not* JFE — they are the exact confusions JFE referees notice (see the
"do-not-misattribute" note in [`../official-source-map.md`](../official-source-map.md)):

- **Carhart (1997), "On Persistence in Mutual Fund Performance"** — *Journal of Finance* (Wiley), **not
  JFE**. The momentum-persistence four-factor result is JF; do not position against it as JFE house
  lineage. (Already flagged in the skills.)
- **Jegadeesh & Titman (1993), "Returns to Buying Winners and Selling Losers"** — *Journal of Finance*
  48(1):65–91 (Wiley), **not JFE**.
- **Chava & Roberts (2008), "How Does Financing Impact Investment? The Role of Debt Covenants"** —
  *Journal of Finance* 63(5):2085–2121 (RePEc `bla:jfinan`), **not JFE**. A canonical covenant-violation
  RDD, but in JF.
- **Bertrand & Mullainathan (2003), "Enjoying the Quiet Life? Corporate Governance and Managerial
  Preferences"** — *Journal of Political Economy* 111(5):1043–1075, **not JFE**.
- **Bennedsen, Nielsen, Pérez-González & Wolfenzon (2007), "Inside the Family Firm"** — *Quarterly
  Journal of Economics* 122(2):647–691, **not JFE**.

Before adding any new paper to this library, confirm it on ScienceDirect (an `0304-405X` / `S0304405X...`
identifier) or RePEc (`RePEc:eee:jfinec`), and update the access-date header. When the venue is in doubt
between JFE, JF, and RFS, **omit**.
