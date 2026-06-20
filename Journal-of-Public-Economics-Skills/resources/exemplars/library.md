# *Journal of Public Economics* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Public Economics_** (JPubE) — the public-economics field journal
> founded in 1972 by Anthony B. Atkinson and published by **Elsevier** (ScienceDirect) — with year and
> volume/issue, against the Elsevier/ScienceDirect article record and the RePEc **`eee/pubeco`** series
> record (`ideas.repec.org/a/eee/pubeco/...`), corroborated by Google Scholar lookups carrying the journal
> name. Papers without full **_Journal of Public Economics_** venue confirmation were **omitted** —
> this is deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** JPubE is **not** the *American Economic Journal: Economic Policy* (AEJ:Policy),
> the *Journal of Public Economic Theory*, *National Tax Journal*, *International Tax and Public Finance*,
> or the general-interest top-5 (AER, QJE, Econometrica, JPE, ReStud). Many famous "public economics" papers
> live in those venues; the [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-jpube)
> section records the traps checked and rejected — several canonical bunching and tax-salience papers are
> in AEJ:Policy, QJE, or AER, **not** JPubE.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent elasticities, coefficients, or specific findings — read the original on Elsevier /
> ScienceDirect before citing any number. For JPubE-specific scope, the 250-word abstract, author-date
> references, and house style, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × public-finance question** is closest to yours, then study how that paper turns
a behavioral response into a **policy-relevant parameter feeding a welfare or revenue conclusion** — the
JPubE bar (see [`../../skills/jpube-identification-strategy/SKILL.md`](../../skills/jpube-identification-strategy/SKILL.md),
[`../../skills/jpube-contribution-framing/SKILL.md`](../../skills/jpube-contribution-framing/SKILL.md), and
[`../../skills/jpube-writing-style/SKILL.md`](../../skills/jpube-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JPubE-shaped." The cross-cutting design checks live in
[`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).

---

## By method

### Panel estimation of a behavioral elasticity off tax reforms (taxable income / optimal tax)

- **Gruber & Saez, "The elasticity of taxable income: evidence and implications," _Journal of Public Economics_ 2002, 84(1):1–32.**
  Verified: `ideas.repec.org/a/eee/pubeco/v84y2002i1p1-32.html`; ScienceDirect `10.1016/S0047-2727(01)00085-8`.
  - **Why it is an exemplar:** estimates the elasticity of taxable income (ETI) from a long panel of returns
    across 1980s reforms, then maps it directly into the optimal-tax formula — a first-order policy
    elasticity that *is* the sufficient statistic, exactly the
    [`jpube-contribution-framing`](../../skills/jpube-contribution-framing/SKILL.md) "estimate the parameter
    the welfare argument needs" move, with the reform-panel identification that
    [`jpube-identification-strategy`](../../skills/jpube-identification-strategy/SKILL.md) ranks as a
    credibly exogenous DID off reform timing.
  - **Self-check:** is your estimated object the elasticity (or sufficient statistic) your welfare claim
    actually requires, and is it cleaned of mean-reversion / non-tax inequality trends?

### Optimal-tax theory tied to estimable primitives (public-goods / charitable giving)

- **Saez, "The optimal treatment of tax expenditures," _Journal of Public Economics_ 2004, 88(12):2657–2684.**
  Verified: `ideas.repec.org/a/eee/pubeco/v88y2004i12p2657-2684.html`; ScienceDirect `10.1016/j.jpubeco.2003.09.004`.
  - **Why it is an exemplar:** derives optimal subsidy rates on a "contribution good" (e.g., charitable
    giving) expressed in **empirically estimable parameters** — the price elasticity of contributions and
    the crowd-out of public for private giving — the
    [`jpube-contribution-framing`](../../skills/jpube-contribution-framing/SKILL.md) "theoretical advance
    connected to measurable quantities" shape, where the theory tells the empiricist exactly which numbers
    to bring back.
  - **Self-check:** does your theory deliver a formula whose inputs are sufficient statistics someone could
    estimate, rather than a result that only holds for unobservable primitives?

### Difference-in-differences off a program rollout (transfers / labor supply)

- **Hoynes & Schanzenbach, "Work incentives and the Food Stamp Program," _Journal of Public Economics_ 2012, 96(1):151–162.**
  Verified: `ideas.repec.org/a/eee/pubeco/v96y2012i1p151-162.html`; ScienceDirect `10.1016/j.jpubeco.2011.08.006`.
  - **Why it is an exemplar:** uses the **county-by-county rollout of the Food Stamp Program** as quasi-
    experimental variation to identify the program's work-disincentive effect — the
    [`jpube-identification-strategy`](../../skills/jpube-identification-strategy/SKILL.md) "DID off a
    credibly exogenous reform rollout" branch — and reads the labor-supply response in transfer-policy
    rather than purely statistical terms.
  - **Self-check:** is your treatment-timing variation defensibly exogenous (staggered adoption handled),
    and is the estimate tied to the transfer-policy margin a public economist cares about?

### Structural estimation on a nonlinear budget set (saving / retirement policy)

- **Engelhardt & Kumar, "Employer matching and 401(k) saving: Evidence from the Health and Retirement Study," _Journal of Public Economics_ 2007, 91(10):1920–1943.**
  Verified: `ideas.repec.org/a/eee/pubeco/...`; ScienceDirect `10.1016/j.jpubeco.2007.02.009`.
  - **Why it is an exemplar:** formulates a life-cycle-consistent specification of 401(k) saving that builds
    in the **kinked, nonlinear budget set the employer match creates**, recovering the match-rate
    semi-elasticity of participation — the
    [`jpube-data-analysis`](../../skills/jpube-data-analysis/SKILL.md) discipline of estimating the policy
    parameter directly off the program rule's nonlinearity rather than a reduced-form proxy.
  - **Self-check:** does your specification respect the actual kinks/notches of the program rule, so the
    recovered parameter is the behavioral object the policy lever moves?

### Bunching at a kink to recover a structural elasticity (income taxation)

- **Bastani & Selin, "Bunching and non-bunching at kink points of the Swedish tax schedule," _Journal of Public Economics_ 2014, 109:36–49.**
  Verified: `ideas.repec.org/a/eee/pubeco/...`; ScienceDirect `10.1016/j.jpubeco.2013.09.010`.
  - **Why it is an exemplar:** estimates **excess mass at a large, salient kink** in the Swedish income-tax
    schedule and links the ability gradient in bunching to optimization frictions — the
    [`jpube-identification-strategy`](../../skills/jpube-identification-strategy/SKILL.md) Branch A bunching
    design done with a defensible counterfactual density and heterogeneity that informs (not data-mines) the
    elasticity.
  - **Self-check:** is your excluded region and counterfactual fit chosen on principled grounds (not to
    maximize the estimate), and do you confront frictions that attenuate observed bunching?

---

## By topic (each cell is a verified _Journal of Public Economics_ paper above)

| Topic (public-finance margin) | Verified _JPubE_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Taxable-income elasticity / optimal tax | Gruber & Saez, "The elasticity of taxable income" | 2002, 84(1) | Reform-panel ETI estimation |
| Charitable giving / public goods | Saez, "The optimal treatment of tax expenditures" | 2004, 88(12) | Optimal-tax theory w/ estimable primitives |
| Transfers / labor supply | Hoynes & Schanzenbach, "Work incentives and the Food Stamp Program" | 2012, 96(1) | DID off program rollout |
| Retirement saving | Engelhardt & Kumar, "Employer matching and 401(k) saving" | 2007, 91(10) | Nonlinear-budget-set structural |
| Income taxation / behavioral response | Bastani & Selin, "Bunching … Swedish tax schedule" | 2014, 109 | Bunching at a kink |

---

## Omitted for lack of full verification (do not attribute to _JPubE_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _Journal of Public Economics_** (the sibling-journal traps the
brief warned of):

- **Saez, "Do Taxpayers Bunch at Kink Points?" (2010)** — verified in the **_American Economic Journal:
  Economic Policy_** 2(3):180–212, **not _JPubE_**. The canonical income-tax bunching paper.
- **Chetty, Looney & Kroft, "Salience and Taxation: Theory and Evidence" (2009)** — verified in the
  **_American Economic Review_** 99(4):1145–1177, **not _JPubE_**.
- **Kleven & Waseem, "Using Notches to Uncover Optimization Frictions and Structural Elasticities … Pakistan" (2013)** —
  verified in the **_Quarterly Journal of Economics_** 128(2):669–723, **not _JPubE_**. The foundational
  notch paper.
- **Kleven & Schultz, "Estimating Taxable Income Responses Using Danish Tax Reforms" (2014)** — verified in
  the **_American Economic Journal: Economic Policy_** 6(4):271–301, **not _JPubE_**.
- **Finkelstein, "E-ZTax: Tax Salience and Tax Rates" (2009)** — verified in the **_Quarterly Journal of
  Economics_** 124(3):969–1010, **not _JPubE_**.

Before adding any new paper to this library, confirm it on Elsevier / ScienceDirect (or the RePEc
`eee/pubeco` record) with volume/issue, and update the access-date header. When in doubt, **omit**.
