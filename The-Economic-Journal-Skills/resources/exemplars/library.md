# EJ Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06.** Every paper below was checked to confirm it
> actually appeared in ***The Economic Journal*** (the Royal Economic Society's general-interest
> journal, founded 1891; older articles published with Wiley/Blackwell under the `10.1111/...` or
> `10.2307/...` DOI/JSTOR stems, articles from ~2019 onward with Oxford University Press under the
> `10.1093/ej/...` stem). Year, volume(issue), and pages were read off the OUP / Wiley / RePEc
> (`ecj:econjl` / `oup:econjl`) article pages. Papers not fully verified as EJ were
> **omitted** — this is deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard (do not misattribute).** EJ is **not** any of these, which share the
> subject area or get conflated with it:
> *JEEA* (Journal of the European Economic Association), the *European Economic Review*, *Economica*
> (LSE), *Oxford Economic Papers*, *The Econometrics Journal* (also RES, but methods/econometrics),
> the *Quarterly Journal of Economics* (Harvard/OUP), and the *American Economic Review*. The
> omissions section below records papers excluded on exactly this ground.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent estimates or specific findings — read the original before citing any number.
> For EJ-specific policy, scope, and house rules, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*technically serious* result answer a *substantial, broadly interesting* economic question — the EJ
bar (see [`../../skills/ecj-topic-selection/SKILL.md`](../../skills/ecj-topic-selection/SKILL.md)
and [`../../skills/ecj-writing-style/SKILL.md`](../../skills/ecj-writing-style/SKILL.md)). For each,
ask the self-check question before claiming your paper is "EJ-shaped." Remember EJ's house identity:
**broad relevance plus clear exposition**, magnitudes reported with standard errors
([`ecj-tables-figures`](../../skills/ecj-tables-figures/SKILL.md)).

---

## By method

### Economic theory (foundational, short, broadly cited)

- **Atkinson, A.B. & Stiglitz, J.E., "A New View of Technological Change," The Economic Journal 1969, 79(315):573–578.**
  Verified: `academic.oup.com/ej/article-abstract/79/315/573` (RePEc `ecj:econjl:v:79:y:1969:i:315`; JSTOR `10.2307/2230384`).
  - **Why it is an exemplar:** a short, sharp theoretical contribution — localised/biased technical
    change — that reframed how economists think about technology, written compactly and legibly. The
    EJ ideal of a *substantial idea of broad interest*, delivered with economy. Routes to
    [`../../skills/ecj-theory-model/SKILL.md`](../../skills/ecj-theory-model/SKILL.md).
  - **Self-check:** is your theoretical point sharp enough to state in a few pages and broad enough
    that economists outside your field would adopt the framing?

- **Acemoglu, D., "Localised and Biased Technologies: Atkinson and Stiglitz's New View, Induced Innovations, and Directed Technological Change," The Economic Journal 2015, 125(583):443–463.**
  Verified: `onlinelibrary.wiley.com/doi/pdf/10.1111/ecoj.12227` (DOI `10.1111/ecoj.12227`).
  - **Why it is an exemplar:** revisits the 1969 EJ classic with modern directed-technical-change
    theory — a contribution that engages the journal's own canonical antecedent (the
    [`ecj-literature-positioning`](../../skills/ecj-literature-positioning/SKILL.md) bar) and speaks
    to a broad audience interested in growth and inequality.
  - **Self-check:** does your paper engage the foundational theory the result speaks to, not only the
    recent frontier?

### Quasi-experimental panel causal inference (DiD / deregulation)

- **Leblebicioğlu, A. & Weinberger, A., "Credit and the Labour Share: Evidence from US States," The Economic Journal 2020, 130(630):1782–1816.**
  Verified: `academic.oup.com/ej/article-abstract/130/630/1782` (DOI `10.1093/ej/ueaa025`; RePEc `oup:econjl:v:130:y:2020:i:630`).
  - **Why it is an exemplar:** uses staggered interstate banking deregulation as identifying
    variation to give a *causal* account of a first-order macro fact (the falling labour share) that
    the whole profession cares about — credible design plus broad relevance, the EJ sweet spot. Pairs
    with [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do) and
    [`../../skills/ecj-identification/SKILL.md`](../../skills/ecj-identification/SKILL.md) Branch A.
  - **Self-check:** does your design connect a credible quasi-experiment to a macro/aggregate question
    of broad interest, with the coefficient given an economic interpretation?

### Regression discontinuity (information / market behavior)

- **Anderson, M. & Magruder, J., "Learning from the Crowd: Regression Discontinuity Estimates of the Effects of an Online Review Database," The Economic Journal 2012, 122(563):957–989.**
  Verified: `academic.oup.com/ej/article-abstract/122/563/957` (DOI `10.1111/j.1468-0297.2012.02512.x`; RePEc `ecj:econjl:v:122:y:2012:i:563`).
  - **Why it is an exemplar:** a clean RDD around a rating-rounding threshold answers a broadly
    interesting question — how much do consumer-information aggregators move real economic outcomes —
    with a transparent design a generalist immediately grasps. The
    [`ecj-identification`](../../skills/ecj-identification/SKILL.md) Branch C standard (rounding
    cutoff, smoothness, bandwidth). Pairs with [`../code/stata/05_rdd.do`](../code/stata/05_rdd.do).
  - **Self-check:** is your discontinuity a sharp, credible source of variation, and is the question
    it answers interesting beyond the specific platform?

### Experimental / behavioral economics (gender, competition, culture)

- **Booth, A., Fan, E., Meng, X. & Zhang, D., "Gender Differences in Willingness to Compete: The Role of Culture and Institutions," The Economic Journal 2019, 129(618):734–764.**
  Verified: `onlinelibrary.wiley.com/doi/abs/10.1111/ecoj.12583` (DOI `10.1111/ecoj.12583`).
  - **Why it is an exemplar:** a lab experiment that isolates the role of culture/institutions in the
    competition gender gap by comparing cohorts exposed to different institutional regimes — an
    experimental design with an identification idea, answering a question of wide interest. Routes to
    [`../../skills/ecj-identification/SKILL.md`](../../skills/ecj-identification/SKILL.md)
    (experimental branch) and [`ecj-robustness`](../../skills/ecj-robustness/SKILL.md) (mechanism).
  - **Self-check:** does your experiment have an identifying comparison (not just a treatment vs.
    control mean), and a mechanism that travels beyond the lab?

- **Hauge, K.E., Kotsadam, A. & Riege, A., "Culture and Gender Differences in Willingness to Compete," The Economic Journal 2023, 133(654):2403–2426.**
  Verified: `academic.oup.com/ej/article/133/654/2403/7143100` (DOI `10.1093/ej/uead033`; OUP article page; experimental, competition gender gap).
  - **Why it is an exemplar:** a more recent EJ experimental contribution on the same broad question,
    useful as a model of how to position an incremental experimental result against an established
    finding and still clear the broad-interest bar.
  - **Self-check:** if your result revisits an established finding, have you stated precisely what is
    new and why the profession should still care?

---

## By topic (each cell is a verified EJ paper above)

| Topic | Verified EJ exemplar | Year / vol(issue) | Method | DOI / ID |
| --- | --- | --- | --- | --- |
| Technical change & growth (theory) | Atkinson & Stiglitz, "A New View of Technological Change" | 1969, 79(315) | Economic theory | 10.2307/2230384 |
| Directed technical change (theory) | Acemoglu, "Localised and Biased Technologies" | 2015, 125(583) | Economic theory | 10.1111/ecoj.12227 |
| Falling labour share | Leblebicioğlu & Weinberger, "Credit and the Labour Share" | 2020, 130(630) | DiD / deregulation panel | 10.1093/ej/ueaa025 |
| Consumer information & markets | Anderson & Magruder, "Learning from the Crowd" | 2012, 122(563) | Regression discontinuity | 10.1111/j.1468-0297.2012.02512.x |
| Gender, competition & culture | Booth, Fan, Meng & Zhang, "Gender Differences in Willingness to Compete" | 2019, 129(618) | Lab experiment | 10.1111/ecoj.12583 |
| Gender, competition & culture | Hauge, Kotsadam & Riege, "Culture and Gender Differences in Willingness to Compete" | 2023, 133(654) | Lab experiment | 10.1093/ej/uead033 |

---

## Omitted for lack of full verification, or to avoid sibling-confusion (do not attribute to EJ without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking:

- **Sen, A., "Ingredients of Famine Analysis: Availability and Entitlements" (1981)** — a natural
  development-economics candidate often associated with Sen's EJ-era work, but web search confirms it
  is in the ***Quarterly Journal of Economics*** (96(3):433–464, 1981), **not EJ**. Listed here only
  as a sibling-confusion guardrail: the QJE venue, not EJ, is the tell.
- **Sandmo, A., "On the Theory of the Competitive Firm under Price Uncertainty" (1971)** — frequently
  recalled as a classic theory piece, but it appeared in the ***American Economic Review***
  (61(1):65–73), **not EJ**. Guardrail only.
- Several frequently-cited EJ-area applied and theory papers surfaced in search were left off because
  their **exact EJ volume/issue/pages** were not confirmed to the same standard in one pass; add
  them only after reading the OUP / Wiley / RePEc article page and confirming an EJ DOI stem
  (`10.1093/ej/...`, `10.1111/ecoj...`, `10.1111/j.1468-0297...`, or a JSTOR/`ecj:econjl` record).

Before adding any new paper to this library, confirm it on `academic.oup.com/ej`,
`onlinelibrary.wiley.com`, or RePEc (`ecj:econjl` / `oup:econjl`) with volume/issue/pages **and** an
EJ DOI stem, then update the access-date header. When in doubt, omit. For venue-neutral referee
objections by design, see
[`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
