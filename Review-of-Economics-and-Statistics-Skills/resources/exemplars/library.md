# REStat Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06.** Every paper below was checked to confirm it actually
> appeared in ***The Review of Economics and Statistics*** (REStat, MIT Press, edited at the Harvard Kennedy
> School). Year, volume(issue), and pages were read off the **MIT Press Direct** REStat article pages
> (`direct.mit.edu/rest/article/...`) or the matching `10.1162/rest...` DOI / REStat Harvard Dataverse
> record. Papers that could not be fully verified as REStat were **omitted** — this is deliberately a short,
> clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard (do not misattribute).** REStat is **not** any of these, which share the subject
> area: *Journal of Econometrics* (methods-development), *AEJ: Applied* / *American Economic Review* (AEA,
> openICPSR data archive), *Econometrica* / *Quantitative Economics* (`10.3982/...` DOI stem), or the
> *Journal of Applied Econometrics* (JAE Data Archive). Only a **REStat article page / `10.1162/rest...`
> DOI** confirms REStat. The omissions section records papers excluded on exactly this ground.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not reproduce
> or invent estimates or specific findings — read the original before citing any number. For REStat-specific
> policy, scope, and house rules, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **method × question** is closest to yours, then study how that paper makes a
*credibly identified or carefully measured* result answer a *substantive applied* economic question — the
REStat bar (see [`../../skills/restat-topic-selection/SKILL.md`](../../skills/restat-topic-selection/SKILL.md)
and [`../../skills/restat-writing-style/SKILL.md`](../../skills/restat-writing-style/SKILL.md)). For each, ask
the self-check question before claiming your paper is "REStat-shaped." Remember REStat's house norm: report
**standard errors** (stars permitted, but never instead of the SE)
([`restat-tables-figures`](../../skills/restat-tables-figures/SKILL.md)).

---

## By method

### Measurement of inequality with large micro data (decomposition / applied measurement)

- **Autor, Katz & Kearney, "Trends in U.S. Wage Inequality: Revising the Revisionists," REStat 2008, 90(2):300–323.**
  Verified: `direct.mit.edu/rest/article/90/2/300` (REStat article page).
  - **Why it is an exemplar:** a measurement-and-decomposition paper that pins down *what* in the data drives
    rising wage inequality, reconciling competing prior accounts — REStat's measurement tradition answering a
    first-order applied question. Routes to
    [`../../skills/restat-identification/SKILL.md`](../../skills/restat-identification/SKILL.md) (Branch D, measurement).
  - **Self-check:** does your measurement work *change an applied conclusion*, rather than just re-describe a series?

### Heterogeneity-robust difference-in-differences (applied econometrics put to use)

- **de Chaisemartin & D'Haultfœuille, "Difference-in-Differences Estimators of Intertemporal Treatment Effects," REStat 2024.**
  Verified: DOI `10.1162/rest_a_01414` (REStat article page, `direct.mit.edu/rest/article-abstract/doi/10.1162/rest_a_01414`).
  - **Why it is an exemplar:** an applied-econometrics contribution — event-study estimators for non-binary,
    non-absorbing treatments — published at REStat because it is built to be *applied* to substantive
    staggered-treatment settings, not as a free-standing theorem. Pairs with
    [`../code/stata/03_did_modern.do`](../code/stata/03_did_modern.do).
  - **Self-check:** if your contribution leans methodological, is it framed and demonstrated for a substantive
    applied use (not method-for-its-own-sake, which belongs at *J. Econometrics*)?

### Regression discontinuity — extrapolation & external validity

- **Dong & Lewbel, "Identifying the Effect of Changing the Policy Threshold in Regression Discontinuity Models," REStat 2015, 97(5):1081–1092.**
  Verified: `direct.mit.edu/rest/article/97/5/1081` (REStat article page).
  - **Why it is an exemplar:** extends RD beyond the LATE-at-the-cutoff to the *treatment-effect derivative*,
    giving a tool for external validity and extrapolation — a credibly identified object that widens what an
    applied RD can say. Matches [`restat-identification`](../../skills/restat-identification/SKILL.md) Branch B.
  - **Self-check:** does your RD say something about effects *away from* the cutoff, with the extra assumption
    stated and defended?

### Regression discontinuity — optimized / bias-aware estimation

- **Imbens & Wager, "Optimized Regression Discontinuity Designs," REStat 2019, 101(2):264–278.**
  Verified: `direct.mit.edu/rest/article/101/2/264`; replication data on the **REStat Harvard Dataverse**
  (`doi:10.7910/DVN/8SATPR`).
  - **Why it is an exemplar:** an applied-econometrics paper delivering minimax-optimal, bias-aware RD
    inference — and its replication package on the REStat Harvard Dataverse is a concrete model for
    [`restat-replication-package`](../../skills/restat-replication-package/SKILL.md).
  - **Self-check:** is your RD inference honest about bias (bias-corrected / robust CIs), and is your code
    deposited in the REStat Harvard Dataverse the way this one is?

### Regression discontinuity in program evaluation (education / public)

- **Jacob & Lefgren, "Remedial Education and Student Achievement: A Regression-Discontinuity Analysis," REStat 2004, 86(1):226–244.**
  Verified: `direct.mit.edu/rest/article/86/1/226` (REStat article page).
  - **Why it is an exemplar:** a clean RD around a test-score promotion cutoff answering a concrete
    education-policy question — the applied-micro program-evaluation work REStat publishes across fields.
  - **Self-check:** is the cutoff plausibly unmanipulated, and does the design speak to a real policy margin?

---

## By topic (each cell is a verified REStat paper above)

| Topic | Verified REStat exemplar | Year / vol(issue) | Method | Locator |
| --- | --- | --- | --- | --- |
| Wage inequality / measurement | Autor, Katz & Kearney, "Revising the Revisionists" | 2008, 90(2) | Measurement / decomposition | rest/article/90/2/300 |
| Staggered treatment effects | de Chaisemartin & D'Haultfœuille, "Intertemporal Treatment Effects" | 2024 | Heterogeneity-robust DID | DOI 10.1162/rest_a_01414 |
| RD external validity | Dong & Lewbel, "Changing the Policy Threshold in RD" | 2015, 97(5) | RD / treatment-effect derivative | rest/article/97/5/1081 |
| RD optimized inference | Imbens & Wager, "Optimized RD Designs" | 2019, 101(2) | RD / minimax-optimal inference | rest/article/101/2/264 |
| Education program evaluation | Jacob & Lefgren, "Remedial Education and Achievement" | 2004, 86(1) | RD program evaluation | rest/article/86/1/226 |

---

## Omitted for lack of full verification, or to avoid sibling-confusion (do not attribute to REStat without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking:

- **Adão, Kolesár & Morales, "Shift-Share Designs: Theory and Inference" (2019)** — a natural shift-share
  candidate, but it is in the ***Quarterly Journal of Economics*** (134(4)), **not REStat**. Listed only as a
  sibling-confusion guardrail.
- **Borusyak, Hull & Jaravel, "Quasi-Experimental Shift-Share Research Designs" (2022)** — in the ***Review
  of Economic Studies*** (89(1)), **not REStat**; another guardrail (the near-identical journal name is the trap).
- Several frequently-cited applied papers surfaced in search were left off because their **exact REStat
  volume/issue/pages** could not be confirmed to the same standard in one pass; add them only after reading
  the MIT Press Direct REStat article page and confirming the `10.1162/rest...` DOI.

Before adding any new paper to this library, confirm it on `direct.mit.edu/rest` (article page with
volume/issue/pages) **and** that the DOI begins `10.1162/rest`, then update the access-date header. When in
doubt, omit.
