# AEJ: Applied Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06.** Every paper below was checked to confirm it actually
> appeared in the ***American Economic Journal: Applied Economics*** (the American Economic Association's
> quarterly applied-micro journal) and carries a **`10.1257/app.` DOI stem** — the marker that confirms
> AEJ: Applied specifically. Year, volume(issue), and pages were read off the AEA article pages. Papers without
> an AEJ: Applied placement were **omitted** — this is deliberately a short, clean list
> rather than a long, uncertain one.
>
> **Sibling-confusion guard (do not misattribute).** AEJ: Applied is **not** any of these, which share the
> AEA `10.1257` prefix or the applied-micro subject area:
> *American Economic Review* (`10.1257/aer…`), *AEJ: Economic Policy* (`10.1257/pol…`), *AEJ: Macro*
> (`10.1257/mac…`), *AEJ: Micro* (`10.1257/mic…`), *JEP* (`10.1257/jep…`), or field journals such as the
> *Journal of Health Economics*, *Journal of Labor Economics*, *Journal of Development Economics*, and
> *QJE*. Only the **`10.1257/app.`** stem confirms AEJ: Applied. The omissions section below records papers
> excluded on exactly this ground.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not reproduce
> or invent estimates, magnitudes, or specific findings — read the original before citing any number. For
> AEJ: Applied-specific policy, scope, and house rules, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a *credibly
identified* estimate answer a *substantive applied-micro* question — the AEJ: Applied bar (see
[`../../skills/aeja-topic-selection/SKILL.md`](../../skills/aeja-topic-selection/SKILL.md) and
[`../../skills/aeja-identification/SKILL.md`](../../skills/aeja-identification/SKILL.md)). For each, ask the
self-check question before claiming your paper is "AEJ: Applied-shaped." Remember the AEA house rule: AEA
permits significance stars but **expects standard errors**, and the identification figure carries half the
persuasion ([`aeja-tables-figures`](../../skills/aeja-tables-figures/SKILL.md)).

---

## By method

### Randomized controlled trial — development / microfinance

- **Banerjee, Abhijit, Esther Duflo, Rachel Glennerster & Cynthia Kinnan, "The Miracle of Microfinance? Evidence from a Randomized Evaluation," AEJ: Applied 2015, 7(1):22–53.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20130533` (DOI `10.1257/app.20130533`).
  - **Why it is an exemplar:** a large randomized rollout of group lending answers a first-order development
    question — does microcredit transform poor households? — with an ITT design and pre-specified outcomes.
    The contribution is a credibly identified *answer*, not a new estimator. Routes to
    [`../../skills/aeja-identification/SKILL.md`](../../skills/aeja-identification/SKILL.md) Path A (RCT).
  - **Self-check:** does your RCT have a pre-specified estimand and an honest verdict, even when the headline
    effect is modest?

### Randomized controlled trial — health insurance markets

- **Fischer, Torben, Markus Frölich & Andreas Landmann, "Adverse Selection in Low-Income Health Insurance Markets: Evidence from an RCT in Pakistan," AEJ: Applied 2023, 15(3):313–340.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20200639` (DOI `10.1257/app.20200639`).
  - **Why it is an exemplar:** a field experiment is engineered to *separate* adverse selection from moral
    hazard — the design is built to identify a specific economic object, the AEJ: Applied ideal of design
    serving the question. Pairs with [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do) only
    as a coding analogue; the identification is experimental.
  - **Self-check:** is your experiment designed to isolate one economic mechanism rather than just estimate a
    program's overall effect?

### Regression discontinuity — health / early-childhood intervention

- **Billings, Stephen B. & Kevin T. Schnepel, "Life after Lead: Effects of Early Interventions for Children Exposed to Lead," AEJ: Applied 2018, 10(3):315–344.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20160056` (DOI `10.1257/app.20160056`).
  - **Why it is an exemplar:** uses a blood-lead-test eligibility threshold as a regression-discontinuity
    cutoff to identify the causal effect of early intervention on children's later outcomes — a clean RD on a
    policy-relevant population. Connects to
    [`../../skills/aeja-identification/SKILL.md`](../../skills/aeja-identification/SKILL.md) Path C
    (density/bandwidth/bias-corrected CIs) and [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do).
  - **Self-check:** is your RD cutoff genuinely as-good-as-random near the threshold, with a manipulation
    (density) test and bandwidth sensitivity shown?

### Quasi-experiment / difference-in-differences — health spillovers

- **Freedman, Seth, Daniel W. Sacks, Kosali Simon & Coady Wing, "Direct and Indirect Effects of Vaccines: Evidence from COVID-19," AEJ: Applied 2026, 18(1):1–43.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20230717` (DOI `10.1257/app.20230717`).
  - **Why it is an exemplar:** exploits an age-based eligibility delay as a natural experiment to identify
    *both* the direct effect of vaccination and the indirect (spillover) effect on close contacts — a design
    that decomposes a known effect into channels, exactly the
    [`aeja-theory-model`](../../skills/aeja-theory-model/SKILL.md) "new mechanism" contribution type. Uses
    near-universal administrative microdata. Routes to
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** does your quasi-experiment identify a mechanism (direct vs. indirect, channel A vs. B),
    not just an average effect?

### Panel data / measurement — labor (unemployment dynamics)

- **Cohen, Jonathan, Andrew C. Johnston & Attila Lindner, "Skill Depreciation during Unemployment: Evidence from Panel Data," AEJ: Applied 2025, 17(3):208–235.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20230195` (DOI `10.1257/app.20230195`).
  - **Why it is an exemplar:** links panel skill measures to administrative data to test a long-standing
    labor mechanism (does human capital decay during unemployment?), and reports a credible *null* on skill
    decline — a measurement contribution that disciplines a popular explanation. Shows AEJ: Applied values an
    honestly identified null over an overclaimed effect.
  - **Self-check:** if your finding is a null, is the measurement precise enough that the null is informative
    rather than under-powered?

### Field experiment — public economics / firms & labor

- **Harju, Jarkko, Simon Jäger & Benjamin Schoefer, "Voice at Work," AEJ: Applied 2025, 17(3):271–309.**
  Verified: `aeaweb.org/articles?id=10.1257/app.20220451` (DOI `10.1257/app.20220451`).
  - **Why it is an exemplar:** studies how worker representation institutions affect labor-market outcomes
    using credible variation — a public/labor question with broad applied-micro appeal.
  - **Self-check:** does your institutional-variation design rule out the obvious confound that institutions
    are chosen by the firms/workers they affect?

---

## By topic (each cell is a verified AEJ: Applied paper above)

| Topic | Verified AEJ: Applied exemplar | Year / vol(issue) | Method | DOI |
| --- | --- | --- | --- | --- |
| Microfinance & development | Banerjee, Duflo, Glennerster & Kinnan, "Miracle of Microfinance?" | 2015, 7(1) | RCT (ITT) | 10.1257/app.20130533 |
| Health insurance / selection | Fischer, Frölich & Landmann, "Adverse Selection... Pakistan" | 2023, 15(3) | RCT (mechanism separation) | 10.1257/app.20200639 |
| Early-childhood health policy | Billings & Schnepel, "Life after Lead" | 2018, 10(3) | Regression discontinuity | 10.1257/app.20160056 |
| Vaccine direct/indirect effects | Freedman, Sacks, Simon & Wing, "Direct and Indirect Effects of Vaccines" | 2026, 18(1) | Quasi-experiment / DiD | 10.1257/app.20230717 |
| Unemployment & human capital | Cohen, Johnston & Lindner, "Skill Depreciation during Unemployment" | 2025, 17(3) | Panel data / measurement | 10.1257/app.20230195 |
| Worker voice / labor institutions | Harju, Jäger & Schoefer, "Voice at Work" | 2025, 17(3) | Field/quasi-experiment | 10.1257/app.20220451 |

---

## Omitted for sibling-confusion (do not attribute to AEJ: Applied without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking:

- **Almond & Doyle, "After Midnight: A Regression Discontinuity Design in Length of Postpartum Hospital
  Stays" (2011)** — a natural RD-in-health candidate, but web search confirms it is in ***AEJ: Economic
  Policy*** (3(3):1–34, DOI `10.1257/pol.3.3.1`), **not AEJ: Applied**. Listed here only as a
  sibling-confusion guardrail: the `pol` stem, not `app`, is the tell.
- **Bharadwaj, Løken & Neilson, "Early Life Health Interventions and Academic Achievement" (2013)** — a
  well-known VLBW regression-discontinuity paper, but it appeared in the ***American Economic Review***
  (103(5):1862–1891, `10.1257/aer…`), **not AEJ: Applied**. The `aer` stem is the tell.
- **Duflo & Hanna (teacher-absence camera-monitoring) and Jensen (mobile phones and fish-market price
  dispersion)** — frequently cited development/field-experiment papers, but both were published in the
  ***Quarterly Journal of Economics***, **not AEJ: Applied**. Excluded to avoid misattribution.
- Several recent AEJ: Applied papers surfaced via indexing pages but were left off until their AEA article
  page and `10.1257/app.` DOI are checked to the same standard.

Before adding any new paper to this library, confirm it on `aeaweb.org` (article page with volume/issue/
pages) **and** that the DOI begins `10.1257/app.`, then update the access-date header. When in doubt, omit.
