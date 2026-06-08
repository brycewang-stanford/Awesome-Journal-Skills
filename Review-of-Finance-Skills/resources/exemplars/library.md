# *Review of Finance* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in **_Review of Finance_** (RoF) — the official journal of the **European Finance
> Association (EFA)**, published by **Oxford University Press** — with year and volume/issue, against the
> journal's own Oxford Academic article pages (`academic.oup.com/rof/...`), the EFA/journal site
> (`revfin.org/...`), and the RePEc IDEAS `oup/revfin` record. Papers that could not be fully verified
> **as _Review of Finance_** were **omitted** — this is deliberately a short, clean list, not a long,
> uncertain one.
>
> **Sibling-journal guard.** *Review of Finance* is **not** the *Journal of Finance* (JF, Wiley/AFA), the
> *Review of Financial Studies* (RFS, Oxford/SFS), or the *Journal of Financial Economics* (JFE, Elsevier)
> — the **top-3 traps**. It is *especially* confused with **RFS** (both are Oxford-published, both run
> reduced-form empirical asset pricing and corporate finance of the same shape, and an `academic.oup.com`
> URL alone does not tell them apart — check whether the path is `/rof/` or `/rfs/`). Many famous
> "RoF-sounding" papers live in those venues; the
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-review-of-finance) section records
> the traps checked and rejected.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, t-statistics, or specific findings — read the original on Oxford
> Academic before citing any number. For *RoF*-specific scope, the EUR fee schedule, Fast-Track, two-round
> philosophy, and code-sharing policy, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × finance question** is closest to yours, then study how that paper turns a
financial-economics quantity into a contribution that clears the *RoF* bar — referees are explicitly asked
to apply **top-three-finance-journal standards**, so a clean **identification or measurement** advance is
the price of entry (see [`../../skills/rof-topic-selection/SKILL.md`](../../skills/rof-topic-selection/SKILL.md),
[`../../skills/rof-identification-strategy/SKILL.md`](../../skills/rof-identification-strategy/SKILL.md), and
[`../../skills/rof-contribution-framing/SKILL.md`](../../skills/rof-contribution-framing/SKILL.md)). For each,
ask the self-check question before claiming your paper is "*RoF*-shaped."

---

## By method

### Difference-in-differences off an administrative natural experiment (financial institutions)

- **Gopalan, Kalda & Manela, "Hub-and-Spoke Regulation and Bank Leverage," _Review of Finance_ 2021, 25(5):1499–1545.**
  Verified: `academic.oup.com/rof/article-abstract/25/5/1499/6327711` (also `revfin.org/hub-and-spoke-regulation-and-bank-leverage/`; RePEc `oup/revfin`).
  - **Why it is an exemplar:** uses **closures of a bank regulator's field offices** as a natural
    experiment, comparing affected banks to similar banks at the same time and place, and shows the effect
    scales with the increase in supervisor driving distance — the
    [`rof-identification-strategy`](../../skills/rof-identification-strategy/SKILL.md) move of finding an
    administrative shock that is plausibly exogenous to the banks' own choices, plus a dose-response check.
  - **Self-check:** is your shock exogenous to the treated units' decisions, and does the effect vary with
    the intensity of treatment as the mechanism predicts?

### Regression discontinuity off a ratings threshold (asset management)

- **Reuter & Zitzewitz, "How Much Does Size Erode Mutual Fund Performance? A Regression Discontinuity Approach," _Review of Finance_ 2021, 25(5):1395–1432.**
  Verified: `academic.oup.com/rof/article-abstract/25/5/1395/6287626` (also `revfin.org/how-much-does-size-erode-mutual-fund-performance/`; RePEc `oup/revfin`).
  - **Why it is an exemplar:** exploits that small differences in returns cause **discrete jumps in
    Morningstar ratings**, which generate discrete differences in fund size, to identify the causal effect
    of size on performance separately from the skill that drives both — a textbook
    [`rof-identification-strategy`](../../skills/rof-identification-strategy/SKILL.md) RD that breaks the
    skill/size confound and directly tests a Berk–Green-style diseconomies-of-scale prediction.
  - **Self-check:** does a known threshold create as-good-as-random variation in your treatment, and does
    the RD isolate the parameter the theory actually disputes?

### Governance panel using a clean institutional setting (corporate governance)

- **Hamdani & Yafeh, "Institutional Investors as Minority Shareholders," _Review of Finance_ 2013, 17(2):691–725.**
  Verified: `academic.oup.com/rof/article-abstract/17/2/691/1597072` (RePEc `oup/revfin`).
  - **Why it is an exemplar:** studies institutional investors' **actual voting patterns in a
    concentrated-ownership environment**, separating proposals where the minority can affect outcomes from
    those where it cannot, so the design isolates whether institutions *value* their votes — the
    [`rof-topic-selection`](../../skills/rof-topic-selection/SKILL.md) move of choosing an institutional
    setting that turns a governance question into a sharp, observable test.
  - **Self-check:** does your governance setting create a contrast (where the right is binding vs. not) that
    distinguishes your hypothesis from the obvious alternative?

### Cross-country institutional panel (banking / regulation)

- **Delis, Hasan & Kazakis, "Bank Regulations and Income Inequality: Empirical Evidence," _Review of Finance_ 2014, 18(5):1811–1846.**
  Verified: `academic.oup.com/rof/article-abstract/18/5/1811/1574038` (RePEc `oup/revfin`).
  - **Why it is an exemplar:** links **variation in bank regulatory policy across countries and time** to
    the income distribution, using the cross-country panel as the source of identifying variation in
    regulatory liberalization — the [`rof-topic-selection`](../../skills/rof-topic-selection/SKILL.md)
    "use the institutional cross-section to identify a financial-system-level effect" move.
  - **Self-check:** does your cross-country design isolate a specific regulatory channel, or merely correlate
    a regulation index with an outcome under country fixed effects?

### Portfolio / cross-sectional asset pricing with international data (investments)

- **Goyal, Jegadeesh & Subrahmanyam, "Empirical Determinants of Momentum: A Perspective Using International Data," _Review of Finance_ 2025, 29(1):241–273.**
  Verified: `academic.oup.com/rof/article/29/1/241/7772889` (also `revfin.org/empirical-determinants-of-momentum-a-perspective-using-international-data/`; RePEc `oup/revfin/v29y2025i1p241-273`).
  - **Why it is an exemplar:** tests whether U.S.-based explanations of momentum survive **out of sample in
    international data**, using regression-based and portfolio approaches to adjudicate among competing
    behavioral and risk stories — the [`rof-contribution-framing`](../../skills/rof-contribution-framing/SKILL.md)
    discipline of using fresh data to discriminate between named explanations rather than re-document the
    anomaly.
  - **Self-check:** does your asset-pricing test *discriminate between competing explanations*, or does it
    just re-estimate a known premium in a new sample?

---

## By topic (each cell is a verified _Review of Finance_ paper above)

| Topic | Verified _Review of Finance_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Financial institutions / banking | Gopalan, Kalda & Manela, "Hub-and-Spoke Regulation & Bank Leverage" | 2021, 25(5) | DiD off field-office closures |
| Asset management / funds | Reuter & Zitzewitz, "How Much Does Size Erode Mutual Fund Performance?" | 2021, 25(5) | Regression discontinuity (ratings) |
| Corporate governance | Hamdani & Yafeh, "Institutional Investors as Minority Shareholders" | 2013, 17(2) | Voting panel in concentrated ownership |
| Banking / regulation | Delis, Hasan & Kazakis, "Bank Regulations & Income Inequality" | 2014, 18(5) | Cross-country institutional panel |
| Investments / asset pricing | Goyal, Jegadeesh & Subrahmanyam, "Empirical Determinants of Momentum" | 2025, 29(1) | International cross-sectional/portfolio |

---

## Omitted for lack of full verification (do not attribute to _Review of Finance_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _Review of Finance_** (the sibling-journal traps the brief warned
of):

- **Brunnermeier & Pedersen, "Market Liquidity and Funding Liquidity" (2009)** — verified in the **_Review
  of Financial Studies_** 22(6):2201–2238, **not _Review of Finance_**. The closest-sibling trap: same
  Oxford publisher, different journal (`/rfs/`, not `/rof/`).
- **Hou, Xue & Zhang, "Digesting Anomalies: An Investment Approach" (2015)** — verified in the **_Review of
  Financial Studies_** 28(3):650–705, **not _Review of Finance_**.
- **Aggarwal, Saffi & Sturgess, "The Role of Institutional Investors in Voting: Evidence from the Securities
  Lending Market" (2015)** — verified in the **_Journal of Finance_** 70(5):2309–2346, **not _Review of
  Finance_** (an easy confusion with Hamdani & Yafeh's RoF voting paper above).
- **Chang, Hong & Liskovich, "Regression Discontinuity and the Price Effects of Stock Market Indexing" (2015)**
  — verified in the **_Review of Financial Studies_** 28(1):212–246, **not _Review of Finance_** (an easy
  confusion with the Reuter & Zitzewitz RoF RD above).
- **Bennedsen, Nielsen, Pérez-González & Wolfenzon, "Inside the Family Firm: The Role of Families in
  Succession Decisions and Performance" (2007)** — verified in the **_Quarterly Journal of Economics_**
  122(2):647–691, **not _Review of Finance_**.

Before adding any new paper to this library, confirm it on `academic.oup.com/rof` (path must contain
`/rof/`, not `/rfs/`) with volume/issue, and update the access-date header. When in doubt, **omit**.
