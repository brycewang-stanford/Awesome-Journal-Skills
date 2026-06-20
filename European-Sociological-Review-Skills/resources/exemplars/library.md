# ESR Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06.** Every paper below was checked to confirm it
> actually appeared in the **European Sociological Review** (ECSR / Oxford University Press), with
> author, year, and volume/issue/pages, against the OUP article page (`academic.oup.com/esr/...`, DOI
> prefix `10.1093/esr`). Papers that could not be fully verified as ESR were **omitted**, and several
> well-known European-sociology papers that turned out to be in *sibling* journals are listed in the
> "do-not-misattribute" section below as guardrails. This is deliberately a short, clean, verified list
> rather than a long, uncertain one.
>
> **Sibling-confusion warning.** ESR is **not** the *American Sociological Review* (ASR, ASA/SAGE), the
> *American Journal of Sociology* (AJS), *European Societies* (the other ESA-linked journal), the
> *European Journal of Sociology / Archives Européennes de Sociologie* (Cambridge), *Sociological
> Methods & Research*, or *Social Forces*. ESR is the **quantitative-sociology flagship of the European
> Consortium for Sociological Research (ECSR)**, published by OUP.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does **not**
> reproduce or invent coefficients, effect sizes, or specific findings — read the original on OUP before
> citing any number. For ESR-specific scope, length caps, anonymity, replication policy, and house
> citation style, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*credible, on-its-own-terms* quantitative finding carry a **portable mechanism with comparative or
longitudinal leverage** — the ESR bar (see
[`../../skills/eursr-topic-selection/SKILL.md`](../../skills/eursr-topic-selection/SKILL.md),
[`../../skills/eursr-theory-building/SKILL.md`](../../skills/eursr-theory-building/SKILL.md), and
[`../../skills/eursr-research-design/SKILL.md`](../../skills/eursr-research-design/SKILL.md)). For each,
ask the self-check before claiming your paper is "ESR-shaped." Model the introduction on
[`../worked-examples/01-introduction.md`](../worked-examples/01-introduction.md).

---

## By method

### Cross-national multilevel design (comparative, individuals nested in contexts)

- **Schmidt, Kristen & Mühlau, "Educational Selectivity and Immigrants' Labour Market Performance in Europe," ESR 2022, 38(2):252–268.**
  Verified: OUP `doi.org/10.1093/esr/jcab042` (`academic.oup.com/esr/article/38/2/252/6400294`).
  - **Why it is an exemplar:** a three-level model (immigrants in cohorts within origin countries)
    across 18 destinations turns a measurement idea (educational *selectivity* relative to the origin
    distribution) into a comparative mechanism for labour-market incorporation — exactly the
    cross-national multilevel design ESR favors. Pairs with the multilevel tooling in
    [`../external_tools.md`](../external_tools.md).
  - **Self-check:** is your higher-level claim identified by genuine cross-national variation, and are
    the SEs/df honest about the number of clusters (`eursr-data-analysis`)?

### SEM with measurement invariance (cross-national attitudes / values)

- **Davidov, Meuleman, Billiet & Schmidt, "Values and Support for Immigration: A Cross-Country Comparison," ESR 2008, 24(5):583–599.**
  Verified: OUP `doi.org/10.1093/esr/jcn020` (`academic.oup.com/esr/article-abstract/24/5/583/567371`).
  - **Why it is an exemplar:** before comparing value effects across 19 ESS countries, the authors
    establish **measurement equivalence** with multiple-group SEM — the move `eursr-research-design`
    treats as the comparative gate. The substantive claim (self-transcendence vs. conservation) is only
    made where the measures are shown to be comparable.
  - **Self-check:** have you tested configural/metric/scalar invariance and stated what your invariance
    level licenses, before any cross-national latent comparison?

### Panel / within-person change (longitudinal attitudes)

- **Kros & Coenders, "Explaining Differences in Welfare Chauvinism Between and Within Individuals Over Time...," ESR 2019, 35(6):860–873.**
  Verified: OUP `doi.org/10.1093/esr/jcz034` (`academic.oup.com/esr/article/35/6/860/5519994`).
  - **Why it is an exemplar:** a four-wave panel with latent-growth modeling separates **between-person**
    from **within-person** variation — showing whether *changes* in economic risk drive *changes* in
    attitudes, a claim a cross-section cannot make. Models exactly the within-person leverage
    `eursr-theory-building` and `eursr-research-design` reward.
  - **Self-check:** does your panel identify within-person change matched to the theoretical quantity,
    and is attrition handled (`eursr-research-design`)?

### Register / genetically informed variance decomposition (stratification)

- **Erola, Lehti, Baier & Karhula, "Socioeconomic Background and Gene–Environment Interplay in Social Stratification across the Early Life Course," ESR 2022, 38(1):1–17.**
  Verified: OUP `doi.org/10.1093/esr/jcab026` (`academic.oup.com/esr/article/38/1/1/6339981`).
  - **Why it is an exemplar:** high-quality Finnish **register twin data** and ACE variance decomposition
    push a classic stratification question (how much of attainment is shared-environment vs. genetic) onto
    full-population administrative data — a register-based design ESR increasingly publishes, with the
    careful modeling such data demand.
  - **Self-check:** does your administrative/register design deliver a quantity a survey could not, and is
    the modeling (here, decomposition assumptions) defended on its own terms?

### Comparative cross-national stratification (institutional differentiation)

- **Triventi, "Stratification in Higher Education and Its Relationship with Social Inequality: A Comparative Study of 11 European Countries," ESR 2013, 29(3):489–502.**
  Verified: OUP `doi.org/10.1093/esr/jcr092` (`academic.oup.com/esr/article-abstract/29/3/489/463114`).
  - **Why it is an exemplar:** uses cross-national institutional variation (vertical/horizontal
    differentiation of higher-education systems) to explain how social origin maps onto graduate outcomes
    — the institution-as-moderator logic that gives a comparative paper its `eursr-theory-building`
    macro–micro contribution.
  - **Self-check:** does the cross-national institutional contrast do theoretical work, or is "country"
    just a dummy (`eursr-theory-building`)?

### Comparative social mobility over cohorts (mobility tables, long-run change)

- **Bukodi & Goldthorpe, "Understanding trends in social fluidity in Western Europe: class structural change and the OED triangle," ESR 2025, 41(3):363–381.**
  Verified: OUP `doi.org/10.1093/esr/jcae033` (`academic.oup.com/esr/advance-article/doi/10.1093/esr/jcae033/7826647`).
  - **Why it is an exemplar:** combines ESS and Generations & Gender Survey data across 17 societies and
    cohorts born 1923–1977 to decompose social-fluidity trends via the origin–education–destination (OED)
    triangle — comparative mobility analysis with an explicit causal-structural framework rather than a
    descriptive trend. (Advance/issue details current as of 2026-06; confirm final pagination on OUP.)
  - **Self-check:** does your mobility analysis specify the structural mechanism (here, the OED triangle)
    and extract a logic that travels across cohorts and countries (`eursr-research-design`)?

---

## By topic (each cell is a verified ESR paper above)

| Topic | Verified ESR exemplar | Year / vol(issue):pp | Method |
| --- | --- | --- | --- |
| Migration & labour markets | Schmidt, Kristen & Mühlau, "Educational Selectivity..." | 2022, 38(2):252–268 | Cross-national multilevel |
| Attitudes & values | Davidov, Meuleman, Billiet & Schmidt, "Values and Support for Immigration" | 2008, 24(5):583–599 | Multiple-group SEM / invariance |
| Welfare attitudes over time | Kros & Coenders, "Welfare Chauvinism Between and Within Individuals" | 2019, 35(6):860–873 | Panel / latent growth |
| Stratification & attainment | Erola, Lehti, Baier & Karhula, "Gene–Environment Interplay..." | 2022, 38(1):1–17 | Register / ACE decomposition |
| Education & inequality | Triventi, "Stratification in Higher Education..." | 2013, 29(3):489–502 | Comparative cross-national |
| Social mobility | Bukodi & Goldthorpe, "Trends in social fluidity..." | 2025, 41(3):363–381 | Comparative mobility / OED |

---

## Omitted for sibling-journal / verification reasons (do not attribute to ESR without re-checking)

To keep the list zero-hallucination, candidate papers were **excluded** unless verified on an OUP ESR
article page with volume/issue. When sourcing new exemplars, watch these sibling traps:

- **American Sociological Review (ASR)** and **American Journal of Sociology (AJS)** — US flagships; many
  "classic" stratification and mobility papers (e.g., Pager's audit work, Brand & Xie on returns to
  college) are in ASR/AJS, **not ESR**. Do not import an ASR exemplar here.
- **European Societies** — the journal of the European Sociological Association (ESA), Taylor & Francis;
  a different venue from ESR despite the similar name.
- **European Journal of Sociology / Archives Européennes de Sociologie** — Cambridge University Press, a
  more theoretical/historical venue; **not ESR**.
- **Sociological Methods & Research** and **Sociological Science** — methods and open-access venues; ESR
  publishes substantive quantitative articles, not pure methods notes.

Before adding any new paper to this library, confirm it on `academic.oup.com/esr/...` (ESR article page
with volume/issue, DOI `10.1093/esr/...`), update the access-date header, and watch the ASR / AJS /
European Societies / European Journal of Sociology traps. **When in doubt, omit.**
