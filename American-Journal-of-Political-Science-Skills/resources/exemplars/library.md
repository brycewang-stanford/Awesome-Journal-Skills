# AJPS Exemplars Library (subfield × method)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked to confirm it
> actually appeared in the *American Journal of Political Science* (AJPS) — the **flagship journal of the
> Midwest Political Science Association (MPSA), published by Wiley** — with year and volume(issue):page
> range. The checks used the Wiley AJPS article pages (`onlinelibrary.wiley.com/doi/.../ajps...` or the
> legacy `10.1111/j.1540-5907...` DOIs) and the RePEc `wly:amposc` series records
> (`ideas.repec.org/a/wly/amposc/...`). Candidates that could **not** be confirmed as AJPS were
> **omitted** and logged below — a short verified list is preferred over a long uncertain one.
>
> **Sibling-confusion guardrail.** AJPS is easily confused with neighboring venues. It is **NOT** the
> *American Political Science Review* (APSR), the *Journal of Politics* (JOP), *Political Analysis* (PA),
> *World Politics*, or *International Organization* (IO). Several famous, plausible-looking papers in this
> space were placed elsewhere — see the omissions section.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent findings, coefficients, or quotations — read the original on Wiley before citing any
> result. For AJPS-specific policy (10,000-word cap, double-blind, the pre-publication third-party
> verification differentiator) and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

AJPS publishes across every subfield but holds **identification and inference to a high standard**: a
paper earns its place by making a **testable** argument whose design credibly licenses the claim (see
[`../../skills/ajps-theory-building/SKILL.md`](../../skills/ajps-theory-building/SKILL.md) and
[`../../skills/ajps-research-design/SKILL.md`](../../skills/ajps-research-design/SKILL.md)). Pick the row
whose **subfield × method** is closest to yours, then study how it (1) states the estimand or the model's
testable implication, and (2) rules out the strongest rival on its own methodological terms. Run the
self-check before claiming your paper is "AJPS-shaped."

---

## By method

### Survey / conjoint experiment (American politics, public opinion)

- **Hainmueller & Hopkins, "The Hidden American Immigration Consensus: A Conjoint Analysis of Attitudes toward Immigrants," AJPS 2015, 59(3):529–548.**
  Verified: Wiley `10.1111/ajps.12138` + `ideas.repec.org/a/wly/amposc/v59y2015i3p529-548.html`.
  - **Why it is an exemplar:** uses a **conjoint design** to estimate the effect of many immigrant
    attributes at once — disentangling traits that observational and single-factor experiments confound —
    and reports effects as **average marginal component effects** with honest uncertainty, the
    quantity-first reporting [`ajps-data-analysis`](../../skills/ajps-data-analysis/SKILL.md) expects.
  - **Self-check:** does your experiment vary the dimensions your theory says are confounded in the real
    world, so the estimand is the marginal effect you actually claim — not a bundled treatment?

### Design validation / regression discontinuity (methods + American politics)

- **Eggers, Folke, Fowler, Hainmueller, Hall & Snyder, "On the Validity of the Regression Discontinuity Design for Estimating Electoral Effects: New Evidence from Over 40,000 Close Races," AJPS 2015, 59(1):259–274.**
  Verified: Wiley `10.1111/ajps.12127` + `ideas.repec.org/a/wly/amposc/v59y2015i1p259-274.html`.
  - **Why it is an exemplar:** stress-tests whether the **close-election RD design** is valid by checking
    for manipulation/sorting across tens of thousands of races in many settings — turning a methodological
    worry (precise control near the threshold) into an empirical question with density and balance tests.
    The model of the [`ajps-research-design`](../../skills/ajps-research-design/SKILL.md) move "defend the
    identifying assumption, don't assert it."
  - **Self-check:** have you tested the assumption your design *relies on* (here, no sorting at the
    cutoff), rather than assuming it and reporting the estimate?

### Formal / game-theoretic model (American politics, institutions)

- **Dziuda & Howell, "Political Scandal: A Theory," AJPS 2021, 65(1):197–209.**
  Verified: Wiley `10.1111/ajps.12568` + `ideas.repec.org/a/wly/amposc/v65y2021i1p197-209.html`.
  - **Why it is an exemplar:** a transparent model in which scandals arise **endogenously** — parties
    trade off the value of working with a suspect politician against reputational fallout — yielding
    non-obvious comparative statics about *when* past misbehavior becomes present scandal. The
    [`ajps-theory-building`](../../skills/ajps-theory-building/SKILL.md) formal-mode bar: "say what the
    model buys" in testable implications, not just an equilibrium.
  - **Self-check:** does your model deliver a comparative static that surprises, and could in principle be
    disconfirmed — or does it only rationalize what we already observe?

### Cross-national observational panel / mechanism test (comparative politics)

- **Eifert, Miguel & Posner, "Political Competition and Ethnic Identification in Africa," AJPS 2010, 54(2):494–510.**
  Verified: Wiley `10.1111/j.1540-5907.2010.00443.x` + `ideas.repec.org/a/wly/amposc/v54y2010i2p494-510.html`.
  - **Why it is an exemplar:** pools survey respondents across many countries and uses **proximity to
    competitive elections** as the source of variation to test whether political competition *activates*
    ethnic identity — an observational design that isolates a mechanism rather than reporting a cross-
    sectional correlation (see [`ajps-research-design`](../../skills/ajps-research-design/SKILL.md):
    "say what the variation is").
  - **Self-check:** is your comparative claim driven by a *source of variation* you can name and defend,
    or by a regression on a pile of country covariates?

### Theory-driven IPE / conditional-effect argument (comparative / international political economy)

- **Wright, "How Foreign Aid Can Foster Democratization in Authoritarian Regimes," AJPS 2009, 53(3):552–571.**
  Verified: Wiley `10.1111/j.1540-5907.2009.00386.x` + `ideas.repec.org/a/wly/amposc/v53y2009i3p552-571.html`.
  - **Why it is an exemplar:** the contribution is a **conditional** claim — aid encourages
    democratization only for leaders who expect to survive it — derived from an explicit account of
    leaders' incentives and then tested, so the empirics target a **specific interaction** the theory
    predicts rather than an average effect (the [`ajps-theory-building`](../../skills/ajps-theory-building/SKILL.md)
    scope-condition move feeding [`ajps-research-design`](../../skills/ajps-research-design/SKILL.md)).
  - **Self-check:** does your design test the *interaction* your theory implies (who, when, under what
    constraint), not just a main effect that pools the cases where the mechanism should and should not
    operate?

---

## By subfield × method (each cell is a verified AJPS paper above)

| Subfield | Method | Verified AJPS exemplar | Year / vol(issue):pages |
| --- | --- | --- | --- |
| American politics (public opinion) | Survey / conjoint experiment | Hainmueller & Hopkins, "Hidden American Immigration Consensus" | 2015, 59(3):529–548 |
| Methods / American politics | Regression discontinuity, design validation | Eggers et al., "Validity of the RD Design … 40,000 Close Races" | 2015, 59(1):259–274 |
| American politics / institutions | Formal / game theory | Dziuda & Howell, "Political Scandal: A Theory" | 2021, 65(1):197–209 |
| Comparative politics | Cross-national observational panel | Eifert, Miguel & Posner, "Political Competition and Ethnic Identification in Africa" | 2010, 54(2):494–510 |
| Comparative / IPE | Theory-driven conditional effect | Wright, "How Foreign Aid Can Foster Democratization" | 2009, 53(3):552–571 |

---

## Omitted for lack of AJPS verification (do NOT attribute to AJPS without re-checking)

To keep the list zero-hallucination, the following plausible candidates were **excluded** after web
search placed them in a *sibling* journal, not AJPS. They are listed only as guardrails:

- **Acharya, Blackwell & Sen, "Explaining Causal Findings Without Bias: Detecting and Assessing Direct
  Effects" (2016)** — verified in the *American Political Science Review* 110(3):512–529, **not AJPS**.
  (The same authors' "Political Legacy of American Slavery" is in the *Journal of Politics* 78(3),
  **also not AJPS** — do not conflate either with AJPS.)
- **Gerber, Green & Larimer, "Social Pressure and Voter Turnout: Evidence from a Large-Scale Field
  Experiment" (2008)** — verified in the *American Political Science Review* 102(1):33–48, **not AJPS**.
  The canonical social-pressure GOTV field experiment.
- **Hainmueller, Hopkins & Yamamoto, "Causal Inference in Conjoint Analysis" (2014)** — verified in
  *Political Analysis* 22(1):1–30, **not AJPS**. (The *applied* conjoint paper by Hainmueller & Hopkins,
  2015, *is* AJPS and is listed above — do not conflate the methods paper with the application.)
- **Hainmueller, "Entropy Balancing for Causal Effects" (2012)** — verified in *Political Analysis*
  20(1):25–46, **not AJPS**.
- **Fearon, "Rationalist Explanations for War" (1995)** — verified in *International Organization*
  49(3):379–414, **not AJPS**. A frequent cross-IR misattribution.

Before adding any new paper to this library, confirm it on the Wiley AJPS site
(`onlinelibrary.wiley.com` / DOI `10.1111/ajps.*` or legacy `10.1111/j.1540-5907.*`), cross-check the
RePEc `wly:amposc` record with volume/issue/pages, and update the access-date header. When in doubt,
omit.
