# *RAND Journal of Economics* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in **_The RAND Journal of Economics_** (RJE) — the flagship industrial-organization
> journal, continuation of the *Bell Journal of Economics*, sponsored by the **RAND Corporation** and
> published in partnership with **Wiley** — with year and volume/issue, against the Wiley Online Library
> record and the RePEc **`rje/randje`** / **`bla/randje`** series records
> (`ideas.repec.org/a/rje/randje/...`), corroborated by Google Scholar lookups carrying the journal name.
> Papers that could not be fully verified **as _RAND Journal of Economics_** were **omitted** — this is
> deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** RJE is **not** the *Journal of Industrial Economics* (JIE), the *International
> Journal of Industrial Organization* (IJIO), the *American Economic Journal: Microeconomics*, the *Journal
> of Econometrics*, or the general-interest top-5 (AER, QJE, JPE, Econometrica, ReStud). Many famous "IO"
> papers live in those venues; the [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-rje)
> section records the traps checked and rejected — several canonical demand and entry papers are in
> Econometrica, JPE, or AER, **not** RJE.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent elasticities, markups, or specific findings — read the original on Wiley before
> citing any number. For RJE-specific scope, the 100-word abstract, 40/50-page caps, author-date citations
> without page numbers, and house usage rules, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × market question** is closest to yours, then study how that paper turns an
estimated market primitive into a **competition / regulation / welfare lesson legible to an IO audience** —
the RJE bar (see [`../../skills/rje-identification-strategy/SKILL.md`](../../skills/rje-identification-strategy/SKILL.md),
[`../../skills/rje-contribution-framing/SKILL.md`](../../skills/rje-contribution-framing/SKILL.md), and
[`../../skills/rje-writing-style/SKILL.md`](../../skills/rje-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "RJE-shaped." The cross-cutting design checks live in
[`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).

---

## By method

### Structural discrete-choice demand with endogenous prices (differentiated-products demand)

- **Berry, "Estimating Discrete-Choice Models of Product Differentiation," _RAND Journal of Economics_ 1994, 25(2):242–262.**
  Verified: `ideas.repec.org/a/rje/randje/v25y1994isummerp242-262.html`; DOI `10.2307/2555829`.
  - **Why it is an exemplar:** sets out how to estimate demand for differentiated products when **prices are
    correlated with unobserved product quality**, using instruments and an inversion from market shares to
    mean utilities — the foundational
    [`rje-identification-strategy`](../../skills/rje-identification-strategy/SKILL.md) Branch A move
    (instrument price; argue validity in market terms) that underlies modern IO demand estimation.
  - **Self-check:** is price endogeneity confronted with instruments whose validity you argue from market
    institutions, rather than treated as exogenous?

### Structural estimation of a private-value auction (auctions)

- **Li, Perrigne & Vuong, "Structural Estimation of the Affiliated Private Value Auction Model," _RAND Journal of Economics_ 2002, 33(2):171–193.**
  Verified: `ideas.repec.org/a/rje/randje/...`; Wiley `10.2307/3087430`.
  - **Why it is an exemplar:** maps **observed bids to the underlying value distribution** through the
    first-price equilibrium first-order condition, establishing nonparametric identification of the
    affiliated-private-value model — the
    [`rje-identification-strategy`](../../skills/rje-identification-strategy/SKILL.md) Branch D auctions move
    (state the information paradigm; recover values from bids via equilibrium), done with explicit
    identification rather than assumed functional forms.
  - **Self-check:** do you state the information paradigm (private vs. common values) and recover the value
    distribution from bids through the equilibrium, not impose it?

### Reduced-form bidding analysis to detect conduct (collusion / antitrust)

- **Porter & Zona, "Ohio School Milk Markets: An Analysis of Bidding," _RAND Journal of Economics_ 1999, 30(2):263–288.**
  Verified: `econpapers.repec.org/article/rjerandje/v_3a30_3ay_3a1999_3ai_3asummer_3ap_3a263-288.htm`; Wiley `10.2307/2556080`.
  - **Why it is an exemplar:** compares the bidding behavior of suspected colluders to a control group and
    ties the pattern to **institutional detail of the procurement process** to argue conduct is collusive,
    quantifying the price effect — the
    [`rje-contribution-framing`](../../skills/rje-contribution-framing/SKILL.md) "substantive-empirical
    contribution with a competition lesson" shape, with the antitrust payoff stated plainly.
  - **Self-check:** is your conduct inference disciplined by institutional facts and a credible control
    group, with the competition/antitrust lesson made explicit?

### Entry game with incomplete information and product positioning (entry / market structure)

- **Seim, "An empirical model of firm entry with endogenous product-type choices," _RAND Journal of Economics_ 2006, 37(3):619–640.**
  Verified: `ideas.repec.org/a/rje/randje/v37y20063p619-640.html`; Wiley `10.1111/j.1756-2171.2006.tb00034.x`.
  - **Why it is an exemplar:** models **entry and location/product positioning as a game of incomplete
    information**, recovering returns to differentiation and the demand-vs-competition tradeoff from observed
    market configurations — the
    [`rje-identification-strategy`](../../skills/rje-identification-strategy/SKILL.md) Branch C entry-games
    move, with the equilibrium concept and estimation (nested fixed point) stated, not hand-waved.
  - **Self-check:** is your entry model's equilibrium concept and treatment of multiplicity / information
    explicit, so the recovered competition primitives are credible?

### Merger simulation from estimated demand (mergers / market power)

- **Nevo, "Mergers with Differentiated Products: The Case of the Ready-to-Eat Cereal Industry," _RAND Journal of Economics_ 2000, 31(3):395–421.**
  Verified: `ideas.repec.org/a/rje/randje/v31y2000iautumnp395-421.html`; Wiley `10.2307/2601000`.
  - **Why it is an exemplar:** estimates a brand-level demand system, **recovers marginal costs from the
    pricing first-order conditions**, then simulates post-merger price equilibria and welfare under stated
    conduct — the
    [`rje-data-analysis`](../../skills/rje-data-analysis/SKILL.md) discipline of disciplining a
    counterfactual by the model and reporting it under explicit maintained assumptions (fixed product set,
    Bertrand conduct).
  - **Self-check:** is your counterfactual disciplined by the estimated model with conduct and the product
    set stated as maintained assumptions, and are recovered markups/costs economically sensible?

---

## By topic (each cell is a verified _RAND Journal of Economics_ paper above)

| Topic (IO question) | Verified _RJE_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Differentiated-products demand | Berry, "Estimating Discrete-Choice Models" | 1994, 25(2) | Structural demand w/ endogenous prices |
| Auctions | Li, Perrigne & Vuong, "Affiliated Private Value Auction" | 2002, 33(2) | Structural auction estimation |
| Collusion / antitrust | Porter & Zona, "Ohio School Milk Markets" | 1999, 30(2) | Reduced-form bidding / conduct |
| Entry / market structure | Seim, "Firm Entry with Endogenous Product-Type Choices" | 2006, 37(3) | Entry game (incomplete information) |
| Mergers / market power | Nevo, "Mergers with Differentiated Products" | 2000, 31(3) | Merger simulation from demand |

---

## Omitted for lack of full verification (do not attribute to _RJE_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _The RAND Journal of Economics_** (the sibling-journal traps the
brief warned of):

- **Berry, Levinsohn & Pakes, "Automobile Prices in Market Equilibrium" (1995)** — verified in
  **_Econometrica_** 63(4):841–890, **not _RJE_**. The canonical BLP random-coefficients demand paper.
- **Bresnahan & Reiss, "Entry and Competition in Concentrated Markets" (1991)** — verified in the **_Journal
  of Political Economy_** 99(5):977–1009, **not _RJE_**.
- **Bresnahan & Reiss, "Empirical Models of Discrete Games" (1991)** — verified in the **_Journal of
  Econometrics_** 48(1–2):57–81, **not _RJE_**.
- **Hendricks & Porter, "An Empirical Study of an Auction with Asymmetric Information" (1988)** — verified in
  the **_American Economic Review_** 78(5):865–883, **not _RJE_**. The OCS drainage-lease auction classic.
- **Li, Perrigne & Vuong, "Conditionally Independent Private Information in OCS Wildcat Auctions" (2000)** —
  verified in the **_Journal of Econometrics_** 98(1):129–161, **not _RJE_** (the same authors' APV paper
  *is* in RJE; this companion is not).

Before adding any new paper to this library, confirm it on Wiley Online Library (or the RePEc
`rje/randje` / `bla/randje` record) with volume/issue, and update the access-date header. When in doubt,
**omit**.
