# Mathematical Finance Exemplars Library (theme × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against the
> Wiley Online Library article listing (`onlinelibrary.wiley.com`) **and** its Crossref record
> (`api.crossref.org/works/<DOI>`), which independently confirmed `container-title = Mathematical
> Finance` together with the title, authors, year, volume, issue, and pages. Each DOI uses a genuine
> *Mathematical Finance* prefix — either the legacy `10.1111/j.1467-9965.<year>...` / `10.1111/1467-9965...`
> form or the current `10.1111/mafi...` form. Papers not confirmed as *Mathematical
> Finance* were **omitted** (see the guardrail list) — this is deliberately a short, clean list rather
> than a long, uncertain one (**6 verified > 15 guessed**).
>
> **Sibling-confusion guard.** *Mathematical Finance* (Wiley; ISSN 0960-1627) is **NOT** any of these
> adjacent venues, and a paper in one of them does **not** belong in this library:
> *Finance and Stochastics* (Springer, `10.1007/s00780...`), *SIAM Journal on Financial Mathematics*
> (SIAM), *Quantitative Finance* (Taylor & Francis), or the *Journal of Mathematical Economics*
> (Elsevier). Several famous results commonly mis-cited to "Mathematical Finance" actually live in
> those siblings or in *Econometrica* / *Annals of Applied Probability* — see the guardrail list.
>
> **Use principle (zero hallucination):** this file gives **theorem-level design positioning only**. It
> does **not** reproduce or invent theorem statements, constants, rates, or numerical findings — read
> the original on Wiley before citing any result. For *Mathematical Finance*-specific policy, scope,
> and current live-check notes, see [`../official-source-map.md`](../official-source-map.md).
>
> **Verification caveat.** At the 2026-06-08 exemplar pass, automated article-page access did not expose
> full Wiley article pages. Bibliographic facts below were therefore confirmed via the freely-readable
> **Crossref** record for each DOI plus the Wiley search-result listing; reopen the live Wiley page
> before quoting anything load-bearing.

---

## How to use this library

Pick the row whose **financial-modelling problem × mathematical method** is closest to yours, then
study how that paper makes a *rigorous* theorem carry a *financial-modelling* payoff — the
*Mathematical Finance* bar (see
[`../../skills/mathfin-topic-selection/SKILL.md`](../../skills/mathfin-topic-selection/SKILL.md) and
[`../../skills/mathfin-contribution-framing/SKILL.md`](../../skills/mathfin-contribution-framing/SKILL.md)).
For each, ask the self-check question before claiming your paper is "*Mathematical Finance*-shaped."

---

## By theme × method

### Arbitrage theory — a sharp counterexample (functional analysis / NFLVR)

- **Schachermayer, "A Counterexample to Several Problems in the Theory of Asset Pricing," *Mathematical
  Finance* 1993, 3(2):217–229.** DOI `10.1111/j.1467-9965.1993.tb00089.x`.
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9965.1993.tb00089.x` +
  Crossref `api.crossref.org/works/10.1111/j.1467-9965.1993.tb00089.x`.
  - **Why it is an exemplar:** a single, precisely-constructed counterexample settles several
    conjectured equivalences in no-arbitrage theory at once — the canonical "one sharp object closes
    open problems" contribution the topic-selection skill calls a structural result.
  - **Self-check:** does your result *resolve* a stated open question (a counterexample, an
    equivalence, a sharp bound), not just add a special case?

### Risk measures — an axiomatic representation (convex analysis)

- **Artzner, Delbaen, Eber & Heath, "Coherent Measures of Risk," *Mathematical Finance* 1999,
  9(3):203–228.** DOI `10.1111/1467-9965.00068`.
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/10.1111/1467-9965.00068` +
  Crossref `api.crossref.org/works/10.1111/1467-9965.00068`.
  - **Why it is an exemplar:** four axioms define "coherence" and a representation theorem turns them
    into a concrete class of risk measures — a *new mathematical object with financial meaning*
    (exactly the `mathfin-topic-selection` novelty type) that reorganized risk measurement.
  - **Self-check:** can your contribution be stated as axioms + a representation theorem a referee can
    check, rather than a definition with no structural consequence?

### Term-structure modelling — a new tractable model (Gaussian random fields)

- **Kennedy, "The Term Structure of Interest Rates as a Gaussian Random Field," *Mathematical Finance*
  1994, 4(3):247–258.** DOI `10.1111/j.1467-9965.1994.tb00094.x`.
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/10.1111/j.1467-9965.1994.tb00094.x` +
  Crossref `api.crossref.org/works/10.1111/j.1467-9965.1994.tb00094.x`.
  - **Why it is an exemplar:** proposes a genuinely new tractable object (the whole forward curve as a
    Gaussian random field) and derives its pricing implications — the "new tractable model with a
    provable characterization" pattern.
  - **Self-check:** is your model a new tractable *object* whose pricing/hedging properties you can
    *prove*, not a reparametrization of an existing one?

### Derivative pricing — a Lévy / jump model (subordinated processes)

- **Madan & Milne, "Option Pricing With V.G. Martingale Components," *Mathematical Finance* 1991,
  1(4):39–55.** DOI `10.1111/j.1467-9965.1991.tb00018.x`.
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9965.1991.tb00018.x` +
  Crossref `api.crossref.org/works/10.1111/j.1467-9965.1991.tb00018.x`.
  - **Why it is an exemplar:** replaces Brownian dynamics with a variance-gamma (subordinated) driver
    and derives option-pricing consequences — a tractable non-Gaussian pricing model in the journal's
    stochastic-analysis tradition. **Note:** the closely-related Madan–Carr–Chang variance-gamma paper
    is in the *European Finance Review*, **not** *Mathematical Finance* — cite this one for the MF
    placement.
  - **Self-check:** does a richer driving process buy you a *provable* pricing characterization, or just
    a better empirical fit (which would be off-fit here)?

### Portfolio choice with frictions — stochastic control (free boundaries / singular control)

- **Shreve, Soner & Xu, "Optimal Investment and Consumption With Two Bonds and Transaction Costs,"
  *Mathematical Finance* 1991, 1(3):53–84.** DOI `10.1111/j.1467-9965.1991.tb00016.x`.
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/10.1111/j.1467-9965.1991.tb00016.x` +
  Crossref `api.crossref.org/works/10.1111/j.1467-9965.1991.tb00016.x`.
  - **Why it is an exemplar:** transaction costs turn the Merton problem into a singular-control /
    free-boundary problem, and the paper characterizes the optimal policy rigorously — the
    "stochastic-control verification with financial payoff" pattern. **Note:** the often-cited
    Davis–Norman transaction-cost paper is in *Mathematics of Operations Research*, **not** MF.
  - **Self-check:** does your control problem yield a *characterized* optimal strategy (verification /
    free boundary), not just a numerically-solved HJB with no theorem?

### Stochastic volatility — a rough, affine model (Volterra / fractional processes)

- **El Euch & Rosenbaum, "The Characteristic Function of Rough Heston Models," *Mathematical Finance*
  2019, 29(1):3–38.** DOI `10.1111/mafi.12173` (current `mafi` prefix).
  Verified: Wiley listing `onlinelibrary.wiley.com/doi/abs/10.1111/mafi.12173` +
  Crossref `api.crossref.org/works/10.1111/mafi.12173`.
  - **Why it is an exemplar:** recovers tractability for a *non-Markovian* (rough) volatility model by
    characterizing its characteristic function via a fractional Riccati equation — a *new method* that
    makes a richer model pricable, and the modern-era counterpart of the classic exemplars above.
  - **Self-check:** when your model loses Markovianity/closed forms, do you restore tractability with a
    *proved* characterization (transform, BSDE, Volterra equation) rather than simulation alone?

---

## By theme (each cell is a verified *Mathematical Finance* paper above)

| Theme | Verified MF exemplar | Year / vol(issue):pages | DOI | Method |
| --- | --- | --- | --- | --- |
| Arbitrage / asset-pricing theory | Schachermayer, "A Counterexample..." | 1993, 3(2):217–229 | `10.1111/j.1467-9965.1993.tb00089.x` | Functional analysis / NFLVR |
| Risk measures | Artzner, Delbaen, Eber & Heath, "Coherent Measures of Risk" | 1999, 9(3):203–228 | `10.1111/1467-9965.00068` | Axioms + representation theorem |
| Term-structure modelling | Kennedy, "Term Structure as a Gaussian Random Field" | 1994, 4(3):247–258 | `10.1111/j.1467-9965.1994.tb00094.x` | Gaussian random fields |
| Derivative pricing (Lévy / jumps) | Madan & Milne, "Option Pricing With V.G. Martingale Components" | 1991, 1(4):39–55 | `10.1111/j.1467-9965.1991.tb00018.x` | Subordinated (variance-gamma) process |
| Portfolio choice with frictions | Shreve, Soner & Xu, "...Two Bonds and Transaction Costs" | 1991, 1(3):53–84 | `10.1111/j.1467-9965.1991.tb00016.x` | Singular stochastic control / free boundary |
| Stochastic volatility (rough) | El Euch & Rosenbaum, "Characteristic Function of Rough Heston Models" | 2019, 29(1):3–38 | `10.1111/mafi.12173` | Fractional Riccati / affine Volterra |

---

## Omitted for lack of *Mathematical Finance* placement (do NOT attribute to MF without re-checking)

To keep the list zero-hallucination, these frequently-mis-cited results were **excluded** after
checking — each is a real, important paper, but **not** in *Mathematical Finance*:

- **Föllmer & Schied, "Convex measures of risk and trading constraints" (2002)** — published in
  ***Finance and Stochastics*** 6:429–447 (`10.1007/s007800200072`), a **sibling** journal, **not** MF.
  Listed here only as a guardrail.
- **Kramkov & Schachermayer, "The asymptotic elasticity of utility functions and optimal investment in
  incomplete markets" (1999)** — published in the ***Annals of Applied Probability*** 9(3):904–950,
  **not** MF.
- **Heath, Jarrow & Morton, "Bond Pricing and the Term Structure of Interest Rates: A New Methodology
  for Contingent Claims Valuation" (1992)** — published in ***Econometrica*** 60(1):77–105, **not** MF.
  (Related implementations such as Brace, "A Multifactor Gauss–Markov Implementation of Heath, Jarrow
  and Morton," *do* appear in MF — verify the specific DOI before citing.)
- **Föllmer & Schweizer, "Hedging of contingent claims under incomplete information" (1991)** —
  published as a chapter in *Applied Stochastic Analysis* (Stochastics Monographs, Gordon & Breach),
  **not** in a journal.
- **Davis & Norman, "Portfolio Selection with Transaction Costs" (1990)** — published in ***Mathematics
  of Operations Research*** 15:676–713, **not** MF.

Before adding any new paper to this library, confirm it on `onlinelibrary.wiley.com` (article page with
volume/issue) **and** its Crossref record (`container-title = Mathematical Finance`), and update the
access-date header. When in doubt, omit.
