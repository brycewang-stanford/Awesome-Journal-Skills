# The Lancet Exemplars Library (topic × design)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in ***The Lancet*** itself — a DOI in the `10.1016/S0140-6736…` series and a
> `thelancet.com/journals/lancet/…` article page. Papers that could not be fully verified as *The Lancet*
> were **omitted** — this is deliberately a short, clean list (6 verified) rather than a long, uncertain
> one.
>
> **Sibling-confusion guard.** *The Lancet* is **not** the *New England Journal of Medicine*, *JAMA*, or
> *The BMJ*, and it is **not** a Lancet specialty journal (*The Lancet Oncology*, *The Lancet Infectious
> Diseases*, *The Lancet Global Health*, *The Lancet Respiratory Medicine*, etc.). Specialty-journal DOIs
> use other PII prefixes (e.g. `S2213-2600…` for Respiratory Medicine, `S1473-3099…` for Infectious
> Diseases); only `S0140-6736…` is *The Lancet*. Several landmark papers commonly mis-remembered as *The
> Lancet* are in fact in sibling journals — see the omissions section.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. With one exception
> noted inline (a single primary-outcome figure quoted from the verified source), it does not reproduce or
> invent specific findings — read the original on `thelancet.com` before citing any number. For
> Lancet-specific submission and policy facts, see [`../official-source-map.md`](../external_tools.md).

---

## How to use this library

Pick the row whose **design × topic** is closest to yours, then study how that paper executes the Lancet
artifacts this pack teaches: a structured **Findings/Interpretation** abstract
([`../../skills/lancet-abstract/SKILL.md`](../../skills/lancet-abstract/SKILL.md)), the **Research in
context** panel ([`../../skills/lancet-research-in-context/SKILL.md`](../../skills/lancet-research-in-context/SKILL.md)),
and the EQUATOR reporting guideline + flow diagram for its design
([`../../skills/lancet-reporting/SKILL.md`](../../skills/lancet-reporting/SKILL.md)). For each, ask the
self-check question before claiming your manuscript is "Lancet-shaped."

---

## By design

### Randomised controlled trial — vaccine efficacy (CONSORT)

- **Voysey M, Clemens SAC, Madhi SA, et al. "Safety and efficacy of the ChAdOx1 nCoV-19 vaccine (AZD1222)
  against SARS-CoV-2: an interim analysis of four randomised controlled trials in Brazil, South Africa,
  and the UK." *The Lancet* 2021; 397(10269):99–111.**
  Verified: DOI 10.1016/S0140-6736(20)32661-1; `thelancet.com/journals/lancet/article/PIIS0140-6736(20)32661-1`.
  - **Why it is an exemplar:** a pooled, multi-country randomised design reporting vaccine efficacy with
    the CONSORT discipline The Lancet expects — registration, masking, and a pre-specified primary
    analysis. The template for a high-stakes trial Article.
  - **Self-check:** is your primary efficacy outcome pre-specified, with a flow diagram and an
    intention-to-treat population the abstract's Findings reconcile to?

### Randomised platform trial — therapeutics (CONSORT, harms)

- **RECOVERY Collaborative Group. "Tocilizumab in patients admitted to hospital with COVID-19 (RECOVERY):
  a randomised, controlled, open-label, platform trial." *The Lancet* 2021; 397(10285):1637–1645.**
  Verified: DOI 10.1016/S0140-6736(21)00676-0; `thelancet.com/journals/lancet/article/PIIS0140-6736(21)00676-0`.
  Primary outcome (quoted from the verified source): 28-day mortality 621/2022 (31%) tocilizumab vs
  729/2094 (35%) usual care; rate ratio 0·85, 95% CI 0·76–0·94, p=0·0028.
  - **Why it is an exemplar:** an open-label *platform* trial that still meets the Lancet statistics bar —
    a rate ratio with a 95% CI and an exact P value, an effect framed in both relative and absolute terms,
    and a clearly defined population. Model for `lancet-statistics` reporting.
  - **Self-check:** does every key estimate carry an effect measure **and** a 95% CI (not a bare P), with
    the analysis population named?

### Systematic review / meta-analysis — therapeutics (PRISMA)

- **Ettehad D, Emdin CA, Kiran A, et al. "Blood pressure lowering for prevention of cardiovascular disease
  and death: a systematic review and meta-analysis." *The Lancet* 2016; 387(10022):957–967.**
  Verified: DOI 10.1016/S0140-6736(15)01225-8; `thelancet.com/journals/lancet/article/PIIS0140-6736(15)01225-8`.
  - **Why it is an exemplar:** a large, pre-specified evidence synthesis that adjudicates a clinical
    controversy (how far to lower blood pressure) — exactly the "Evidence before this study" → "Added
    value" arc the Research in context panel formalises, executed as the whole paper.
  - **Self-check:** does your review document a reproducible search and pool with a stated model, so the
    PRISMA flow diagram and the abstract's Findings agree?

### Prospective cohort — nutritional / cardiovascular epidemiology (STROBE)

- **Dehghan M, Mente A, Zhang X, et al. "Associations of fats and carbohydrate intake with cardiovascular
  disease and mortality in 18 countries from five continents (PURE): a prospective cohort study."
  *The Lancet* 2017; 390(10107):2050–2062.**
  Verified: DOI 10.1016/S0140-6736(17)32252-3; `thelancet.com/journals/lancet/article/PIIS0140-6736(17)32252-3`.
  - **Why it is an exemplar:** a multi-country prospective cohort that reports associations — and is
    careful to keep the language associational, not causal, the calibration `lancet-writing` and
    `lancet-statistics` demand of observational designs.
  - **Self-check:** does your observational paper match STROBE, with a participant-flow diagram and causal
    language calibrated strictly to the design?

### Global descriptive epidemiology — disease burden (systematic analysis)

- **GBD 2019 Diseases and Injuries Collaborators. "Global burden of 369 diseases and injuries in 204
  countries and territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study
  2019." *The Lancet* 2020; 396(10258):1204–1222.**
  Verified: DOI 10.1016/S0140-6736(20)30925-9; `thelancet.com/journals/lancet/article/PIIS0140-6736(20)30925-9`.
  - **Why it is an exemplar:** the prototype of large-scale, globally-minded descriptive epidemiology The
    Lancet is known for — an old, broad question (what makes the world sick, and where) answered with a
    standardised systematic analysis across 204 countries.
  - **Self-check:** does your descriptive work answer a question an international readership — not one
    country — would care about, with transparent methods?

### Global descriptive epidemiology — risk factors (systematic analysis)

- **GBD 2019 Risk Factors Collaborators. "Global burden of 87 risk factors in 204 countries and
  territories, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019."
  *The Lancet* 2020; 396(10258):1223–1249.**
  Verified: DOI 10.1016/S0140-6736(20)30752-2; `thelancet.com/journals/lancet/article/PIIS0140-6736(20)30752-2`.
  - **Why it is an exemplar:** the companion risk-factor analysis — same standardised machinery turned to
    *attributable* burden, the kind of equity- and policy-relevant global framing the "Implications of all
    the available evidence" part of the panel is built for.
  - **Self-check:** are your global estimates comparable across place and time, and framed for their
    public-health and equity implications?

---

## By topic (each cell is a verified The Lancet paper above)

| Topic | Verified The Lancet exemplar | Year; vol(issue):pages | Design / guideline |
| --- | --- | --- | --- |
| Vaccines / infectious disease | Voysey et al., ChAdOx1 nCoV-19 efficacy | 2021; 397(10269):99–111 | RCT (pooled) / CONSORT |
| Therapeutics (critical care) | RECOVERY, tocilizumab in COVID-19 | 2021; 397(10285):1637–1645 | RCT platform / CONSORT |
| Cardiovascular prevention | Ettehad et al., blood-pressure lowering | 2016; 387(10022):957–967 | Systematic review / PRISMA |
| Nutrition / CV epidemiology | Dehghan et al., PURE fats & carbohydrate | 2017; 390(10107):2050–2062 | Prospective cohort / STROBE |
| Global disease burden | GBD 2019, 369 diseases & injuries | 2020; 396(10258):1204–1222 | Systematic analysis |
| Global risk factors | GBD 2019, 87 risk factors | 2020; 396(10258):1223–1249 | Systematic analysis |

---

## Omitted for lack of verification *as* The Lancet (do not attribute without re-checking)

To keep the list zero-hallucination, the following commonly-confused candidates were **excluded** after
checking — most are real and important, but **not in *The Lancet* itself**:

- **RECOVERY dexamethasone primary result (Horby et al., 2021)** — the landmark mortality result was
  published in the ***New England Journal of Medicine***, **not** *The Lancet*. (A separate, later
  *higher-dose* corticosteroid RECOVERY paper does appear in *The Lancet*, but is a different study; not
  listed here to avoid conflation.)
- **HOPE-3 (Yusuf et al., 2016)** — the primary cardiovascular-prevention trial results appeared in the
  ***New England Journal of Medicine***, not *The Lancet*. Listed here only as a guardrail.
- **Doll & Peto, "Mortality in relation to smoking: 50 years' observations on male British doctors"
  (2004)** — published in ***The BMJ***, not *The Lancet*.
- **Specialty-journal landmarks** (e.g. trials whose DOI is `S2213-2600…` / `S1473-3099…`) belong to
  *The Lancet Respiratory Medicine* / *The Lancet Infectious Diseases* etc., **not** *The Lancet* — verify
  the `S0140-6736` prefix before attributing.

Before adding any paper to this library, confirm it on `thelancet.com/journals/lancet/…` with an
`S0140-6736` DOI, volume/issue, and pages, and update the access-date header. When in doubt, omit.
