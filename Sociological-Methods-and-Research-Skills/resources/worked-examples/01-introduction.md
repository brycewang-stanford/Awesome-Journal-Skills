> **Illustrative teaching example.** The paper, the estimator, the simulation, and every number
> below are **fictional** and exist only to demonstrate the Sociological Methods & Research house
> style. No real-paper facts are stated and no policy is invented. Corresponding skills:
> [`smr-method-contribution`](../../skills/smr-method-contribution/SKILL.md),
> [`smr-writing-style`](../../skills/smr-writing-style/SKILL.md),
> [`smr-topic-selection`](../../skills/smr-topic-selection/SKILL.md),
> [`smr-derivation-and-properties`](../../skills/smr-derivation-and-properties/SKILL.md),
> [`smr-simulation-studies`](../../skills/smr-simulation-studies/SKILL.md),
> [`smr-empirical-illustration`](../../skills/smr-empirical-illustration/SKILL.md), and
> [`smr-software-and-reproducibility`](../../skills/smr-software-and-reproducibility/SKILL.md).

# Worked Example: An SMR-Style Introduction (before → after)

This demonstrates the **SMR methods-paper arc** — the kind of paper Sociological Methods & Research
publishes: a **method other researchers can adopt** (a new estimator, diagnostic, or correction),
backed by **derived properties + a Monte Carlo study + a real-data illustration + released software**.
It is built only from this pack's own skills:

- **`smr-topic-selection`**: a *method* contribution (develop / evaluate / critically assess), not an
  application — strip the dataset and a methods takeaway must remain; the method must travel.
- **`smr-method-contribution`**: lead with the methodological problem in an applied setting, name the
  incumbent and the regime where it fails, state the fix mechanism and its honest cost, keep claims
  proportional.
- **`smr-derivation-and-properties`**: state the estimand, assumptions, and properties before
  derivations; pair every property with a finite-sample check.
- **`smr-simulation-studies`**: compare against the real competitors, calibrate one DGP to the
  application, report coverage where the claim is about inference.
- **`smr-writing-style`**: abstract ≤150 words with no parenthetical citations; estimand before
  estimator; label proved vs. simulated claims.

**Illustrative paper (fictional):** *"Coverage-Corrected Inference for Indirect Effects When the
Mediator Is Misclassified."* Fictional advance: a bias-corrected estimator and variance for the
indirect (mediation) effect when a binary mediator is measured with error, validated by Monte Carlo
and illustrated on a (fictional) public education-survey panel.

---

## Before (buries the contribution — typical first-draft intro)

> Mediation analysis has become increasingly popular in sociology. Researchers often decompose a
> total effect into direct and indirect components. However, mediators are sometimes measured with
> error. In this paper we propose a new estimator for the indirect effect. We derive its properties
> and conduct a simulation study to examine its performance. We also apply it to data on educational
> attainment. The remainder of the paper is organized as follows. Section 2 reviews the literature,
> Section 3 presents the model, Section 4 reports the simulation, Section 5 presents the application,
> and Section 6 concludes.

**What's wrong (against the SMR skills):**

- **No methodological problem stated.** `smr-method-contribution` requires leading with *where the
  current method fails*; "has become increasingly popular" is throat-clearing.
- **The contribution is unnamed.** "We propose a new estimator" names no advance — what does
  misclassification do to the standard estimator, and what can a researcher now do?
- **Properties are vague.** `smr-derivation-and-properties` wants the estimand, the assumptions, and
  the specific property (here, coverage) stated up front.
- **Simulation framed as a formality**, and the application is decorative — violating
  `smr-simulation-studies` (compare real competitors) and `smr-empirical-illustration` ("it changes
  the answer").
- **No mention of released software**, which SMR readers expect for an adoptable method
  (`smr-software-and-reproducibility`).
- **Over-signposted roadmap** doing the work the argument should do (`smr-writing-style`).

---

## After (SMR arc — problem → why methods fail → the contribution → properties → evidence → software)

> **When a binary mediator is misclassified — a survey indicator records "completed the program" with
> error — the standard product-of-coefficients estimator of the indirect effect is biased toward
> zero, and its confidence intervals under-cover, so researchers routinely understate mediation and
> mislabel it as non-significant.** *(the methodological problem in an applied setting —
> `smr-method-contribution`.)*
>
> Existing corrections assume the mediator is continuous or that misclassification rates are known;
> neither holds for the self-reported binary mediators common in social-survey data, so applied
> mediation analyses have no usable fix. *(why existing methods fail — the gap, not a literature
> tour.)*
>
> We **develop a bias-corrected estimator of the indirect effect, $\widehat{\theta}_{c}$, and a
> variance estimator whose Wald intervals attain nominal coverage** when the mediator's sensitivity
> and specificity are estimated from a validation subsample. The estimand is the **natural indirect
> effect** under sequential ignorability; the correction uses the validation data to deconvolve the
> misclassification, requiring only that a validation subsample exists. *(estimand + assumptions +
> estimator + the property claimed, stated before any derivation — `smr-derivation-and-properties`.)*
>
> The correction is closed-form given the validation estimates, so it is **as easy to compute as the
> uncorrected estimator** and adds only the validation-subsample requirement. *(the fix mechanism and
> its honest cost — `smr-method-contribution`, kept proportional.)*
>
> In a Monte Carlo study spanning $n \in \{500, 2000\}$ and misclassification rates from 5% to 20%,
> the uncorrected estimator's interval coverage falls to 71% at the 20% rate while
> $\widehat{\theta}_{c}$ holds coverage at 94–95%, and it beats both a naive estimator and an existing
> known-rate correction across the grid; at the boundary, coverage degrades when the validation
> subsample is below 100, which we report. *(one compact simulation paragraph with real competitors and
> the boundary — `smr-simulation-studies`.)*
>
> Applied to a (fictional) panel of 6,200 students, the uncorrected analysis concludes that program
> participation has **no significant indirect effect** on attainment through course completion;
> **$\widehat{\theta}_{c}$ recovers a significant positive indirect effect**, reversing the
> substantive conclusion a researcher would otherwise draw. *(the application changes the answer —
> `smr-empirical-illustration`.)*
>
> We release an open R package and a seed-fixed replication script that reproduce every table, figure,
> and the simulation grid. *(released, reproducible software — `smr-software-and-reproducibility`.)*
> Section 2 states the estimator and its properties; Section 3 reports the simulation and the
> education-panel illustration. *(compact roadmap — no over-signposting.)*

---

## Why the "after" meets the SMR bar

Mapped to the skill checklists:

- **Leads with the methodological problem in an applied setting**, then states *why existing methods
  fail* — the `smr-method-contribution` order, not a literature review.
- **The contribution is explicit and proportional**: a bias-corrected estimator + a coverage-valid
  variance, framed as "misclassified binary mediator with a validation subsample," not marketed as a
  general measurement-error framework (`smr-method-contribution` guardrail; `smr-topic-selection`
  develop test).
- **Estimand and property stated before derivations** — natural indirect effect, sequential
  ignorability, and the coverage claim — satisfying `smr-derivation-and-properties`.
- **Simulation is compact, has real competitors, and reports coverage and the boundary** per
  `smr-simulation-studies` (naive + known-rate correction; degradation at small validation samples).
- **The empirical illustration carries substantive consequence** — it *reverses the conclusion* —
  meeting `smr-empirical-illustration`'s "it changes the answer" standard.
- **Released software is named** in the introduction, meeting the SMR expectation that a method be
  adoptable (`smr-software-and-reproducibility`).
- **Abstract-ready:** the contribution sentence ("researchers who study [mediation with a misclassified
  binary mediator] can now [recover unbiased, coverage-valid indirect effects] because we [develop a
  validation-based bias correction]") fits the ≤150-word, no-parenthetical-citation abstract rule
  (`smr-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified**
> Sociological Methods & Research papers (causal inference, missing data, SEM/fit, decomposition,
> networks, computational text) whose introductions execute this method-plus-evidence arc, and
> [`../official-source-map.md`](../official-source-map.md) for the ≤150-word non-parenthetical
> abstract, ASA-style, and data-and-code availability rules this example is written to.
