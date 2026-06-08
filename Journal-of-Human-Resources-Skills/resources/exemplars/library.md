# *Journal of Human Resources* Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the **_Journal of Human Resources_** (JHR) — the empirical-microeconomics journal
> founded in 1965, published by the **University of Wisconsin Press** and housed at the UW–Madison
> Institute for Research on Poverty — with year and volume/issue, against the journal's own article pages
> (`jhr.uwpress.org/content/...`, `muse.jhu.edu/...`) and the RePEc **`uwp/jhriss`** series record
> (`ideas.repec.org/a/uwp/jhriss/...`), corroborated by Google Scholar lookups carrying the journal name.
> Papers that could not be fully verified **as _Journal of Human Resources_** were **omitted** — this is
> deliberately a short, clean list, not a long, uncertain one.
>
> **Sibling-journal guard.** JHR is **not** the *Journal of Labor Economics* (JOLE), the *ILR Review*
> (Industrial and Labor Relations Review), *Labour Economics*, the *Economic Journal*, *International
> Economic Review*, or the general-interest top-5 (AER, QJE, JPE, Econometrica, ReStud). Recall too that
> JHR is an **empirical-microeconomics** journal despite its name — it does **not** publish HR-management
> or personnel research. Many famous "human-resources" papers live in sibling venues; the
> [Omitted](#omitted-for-lack-of-full-verification-do-not-attribute-to-jhr) section records the traps
> checked and rejected — notably one half of the *Blinder–Oaxaca* decomposition is in JHR while the other
> is in *International Economic Review*.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, returns, or specific findings — read the original on UW Press /
> Project MUSE before citing any number. For JHR-specific scope, the 40-page limit, the CC0 data policy,
> and house style, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × empirical-micro question** is closest to yours, then study how that paper
turns identifying variation into a **policy-relevant parameter reconciled with prior estimates** — the JHR
bar (see [`../../skills/jhr-identification-strategy/SKILL.md`](../../skills/jhr-identification-strategy/SKILL.md),
[`../../skills/jhr-contribution-framing/SKILL.md`](../../skills/jhr-contribution-framing/SKILL.md), and
[`../../skills/jhr-writing-style/SKILL.md`](../../skills/jhr-writing-style/SKILL.md)). For each, ask the
self-check question before claiming your paper is "JHR-shaped." The cross-cutting design checks live in
[`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).

---

## By method

### Wage-decomposition into explained vs. unexplained components (discrimination / wage gaps)

- **Blinder, "Wage Discrimination: Reduced Form and Structural Estimates," _Journal of Human Resources_ 1973, 8(4):436–455.**
  Verified: `ideas.repec.org/a/uwp/jhriss/v8y1973i4p436-455.html`; DOI `10.2307/144855`.
  - **Why it is an exemplar:** introduces the regression-based decomposition (one namesake of the
    "Blinder–Oaxaca" method) that splits a group wage gap into a part **explained** by characteristics and an
    **unexplained** residual — the founding
    [`jhr-data-analysis`](../../skills/jhr-data-analysis/SKILL.md) decomposition move, and a model of the
    [`jhr-identification-strategy`](../../skills/jhr-identification-strategy/SKILL.md) discipline of saying
    plainly what is descriptive and what supports a discrimination interpretation.
  - **Self-check:** is your decomposition explicit about which component is descriptive and which (if any)
    licenses a causal/discrimination reading?

### Difference-in-differences off an income shock (family economics / fertility)

- **Lindo, "Are Children Really Inferior Goods? Evidence from Displacement-Driven Income Shocks," _Journal of Human Resources_ 2010, 45(2):301–327.**
  Verified: `ideas.repec.org/a/uwp/jhriss/v45y2010i2p301-327.html`; `jhr.uwpress.org/content/45/2/301`.
  - **Why it is an exemplar:** uses **husband's job displacement** as a quasi-experimental income shock to
    identify the causal effect of income on fertility, separating it from the confound that poorer and
    richer families differ in many ways — the
    [`jhr-identification-strategy`](../../skills/jhr-identification-strategy/SKILL.md) DID-off-a-shock branch,
    with the public-policy interpretation tied to the identified variation.
  - **Self-check:** is your "income effect" identified off a shock plausibly orthogonal to tastes, rather
    than read off a raw income–outcome correlation?

### Regression discontinuity at an eligibility cutoff (education / school entry)

- **McEwan & Shapiro, "The Benefits of Delayed Primary School Enrollment: Discontinuity Estimates Using Exact Birth Dates," _Journal of Human Resources_ 2008, 43(1):1–29.**
  Verified: `ideas.repec.org/a/uwp/jhriss/v43y2008i1p1-29.html`; `jhr.uwpress.org/content/43/1/1`.
  - **Why it is an exemplar:** exploits a **school-entry birth-date cutoff** in a regression-discontinuity
    design to estimate the effect of starting school a year later on grade repetition and test scores — the
    [`jhr-identification-strategy`](../../skills/jhr-identification-strategy/SKILL.md) RDD branch done with
    exact running-variable data, the right local comparison, and heterogeneity (by sex) that is policy-
    relevant rather than fished.
  - **Self-check:** is your running variable manipulation-free at the cutoff, and is the estimated effect a
    clean local comparison rather than a polynomial artifact?

### Structural model of selection with unobserved ability (returns to education)

- **Rodríguez, Urzúa & Reyes, "Heterogeneous Economic Returns to Post-Secondary Degrees: Evidence from Chile," _Journal of Human Resources_ 2016, 51(2):416–460.**
  Verified: `ideas.repec.org/a/uwp/jhriss/v51y2016i2p416-460.html`; `jhr.uwpress.org/content/51/2/416`.
  - **Why it is an exemplar:** posits a **schooling-choice model with unobserved ability**, degree-specific
    costs, and earnings to recover the *distribution* of returns — uncovering heterogeneity (even negative
    returns for some) that an average treatment effect hides — the
    [`jhr-data-analysis`](../../skills/jhr-data-analysis/SKILL.md) move of modeling selection on
    unobservables rather than assuming it away, with returns reconciled against the prior literature.
  - **Self-check:** does your design recover the *heterogeneity* in returns that matters for policy, and is
    selection on unobserved ability modeled rather than ignored?

### Sharp RDD policy evaluation off an administrative poverty index (education / teacher labor markets)

- **Cabrera & Webbink, "Do Higher Salaries Yield Better Teachers and Better Student Outcomes?," _Journal of Human Resources_ 2020, 55(4):1222–1257.**
  Verified: `ideas.repec.org/a/uwp/jhriss/v55y2020i4p1222-1257.html`; `jhr.uwpress.org/content/55/4/1222`.
  - **Why it is an exemplar:** uses a **poverty-index cutoff** assigning a teacher salary premium to evaluate
    whether higher pay attracts experienced teachers and raises achievement — a regression-discontinuity
    program evaluation that carefully distinguishes the **teacher-experience first stage from the student-
    outcome reduced form**, the
    [`jhr-identification-strategy`](../../skills/jhr-identification-strategy/SKILL.md) RDD branch with an
    honest reading of a small reduced-form effect.
  - **Self-check:** do you separate the policy's first-stage effect (on the input) from its effect on the
    final outcome, and report the null/small reduced form honestly rather than over-reading it?

---

## By topic (each cell is a verified _Journal of Human Resources_ paper above)

| Topic (empirical-micro field) | Verified _JHR_ exemplar | Year / vol(issue) | Method |
| --- | --- | --- | --- |
| Discrimination / wage gaps | Blinder, "Wage Discrimination" | 1973, 8(4) | Wage decomposition |
| Family economics / fertility | Lindo, "Are Children Really Inferior Goods?" | 2010, 45(2) | DID off an income shock |
| Education / school entry | McEwan & Shapiro, "Delayed Primary School Enrollment" | 2008, 43(1) | Regression discontinuity |
| Returns to education | Rodríguez, Urzúa & Reyes, "Heterogeneous Returns … Chile" | 2016, 51(2) | Structural selection model |
| Education / teacher labor markets | Cabrera & Webbink, "Do Higher Salaries Yield Better Teachers?" | 2020, 55(4) | Sharp RDD policy evaluation |

---

## Omitted for lack of full verification (do not attribute to _JHR_ without re-checking)

To keep the list zero-hallucination, these strong candidates were **excluded** after web-checking — each
is a real, important paper, but **not in _Journal of Human Resources_** (the sibling-journal traps the
brief warned of):

- **Oaxaca, "Male-Female Wage Differentials in Urban Labor Markets" (1973)** — verified in **_International
  Economic Review_** 14(3):693–709, **not _JHR_**. The other half of the Blinder–Oaxaca decomposition
  (Blinder's half *is* in JHR; Oaxaca's is not).
- **Currie & Thomas, "Does Head Start Make a Difference?" (1995)** — verified in the **_American Economic
  Review_** 85(3):341–364, **not _JHR_**.
- **Oreopoulos, "Estimating Average and Local Average Treatment Effects of Education when Compulsory
  Schooling Laws Really Matter" (2006)** — verified in the **_American Economic Review_** 96(1):152–175,
  **not _JHR_**.
- **Black, Devereux & Salvanes, "Staying in the Classroom and out of the Maternity Ward?" (2008)** —
  verified in the **_Economic Journal_** 118(530):1025–1054, **not _JHR_**.
- **Heckman, "Sample Selection Bias as a Specification Error" (1979)** — verified in **_Econometrica_**
  47(1):153–161, **not _JHR_**. The canonical selection-correction method.

Before adding any new paper to this library, confirm it on `jhr.uwpress.org` or Project MUSE (or the RePEc
`uwp/jhriss` record) with volume/issue, and update the access-date header. When in doubt, **omit**.
