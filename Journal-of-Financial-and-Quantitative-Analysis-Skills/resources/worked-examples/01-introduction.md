> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *JFQA* house style. No real-paper facts are stated, and no real firm or policy
> is invoked. Corresponding skills:
> [`jfqa-writing-style`](../../skills/jfqa-writing-style/SKILL.md),
> [`jfqa-topic-selection`](../../skills/jfqa-topic-selection/SKILL.md),
> [`jfqa-contribution-framing`](../../skills/jfqa-contribution-framing/SKILL.md), and
> [`jfqa-identification-strategy`](../../skills/jfqa-identification-strategy/SKILL.md).

# Worked Example: A *JFQA*-Style Introduction (before → after)

This demonstrates the introduction arc *JFQA* rewards (from `jfqa-writing-style` and
`jfqa-contribution-framing`): **financial-economics question → headline estimate with magnitude and
interval → identification → economic mechanism → contribution relative to the literature → brief
roadmap.** The governing rules: write **result-forward** for a finance audience that knows asset pricing
and corporate finance, report **economic magnitudes in plain finance units** (bps, monthly alpha,
percentage of a standard deviation), and never let the conclusion exceed what the design supports.

**Illustrative paper (fictional):** *"Collateral Haircuts and the Maturity of Corporate Debt: Evidence
from a Discontinuity in Pledgeability."* Fictional setting: a single bond market where a regulator assigns
each issuer a collateral-eligibility score, and assets just above a known cutoff become eligible to be
pledged against central-bank funding.

---

## Before (buries the contribution — typical first-draft intro)

> The maturity structure of corporate debt has been studied extensively in corporate finance. Many
> factors have been proposed to explain why firms issue short-term versus long-term debt, including taxes,
> agency costs, asymmetric information, and refinancing risk. In this paper, we study the relationship
> between collateral and debt maturity using a large panel of bond issuers. We run regressions of debt
> maturity on a measure of collateral eligibility and a set of controls, and we also use a regression
> discontinuity design. We find a statistically significant relationship. Understanding debt maturity is
> important for firms and policymakers. Section II reviews the literature, Section III describes the data,
> Section IV presents the methodology, Section V reports results, and Section VI concludes.

**What's wrong (against `jfqa-writing-style` / `jfqa-contribution-framing` / `jfqa-identification-strategy`):**

- **Leads with a literature tour**, not the financial-economics question — the named anti-pattern in
  `jfqa-writing-style`.
- **No headline estimate, no magnitude, no interval.** "A statistically significant relationship" is the
  exact significance-without-magnitude anti-pattern; a finance reader cannot tell whether the effect is
  economically large (fails `jfqa-contribution-framing`).
- **Identification is mentioned but not motivated.** Why is a discontinuity needed, and what endogeneity
  does it break? Unstated (fails `jfqa-identification-strategy`).
- **No economic mechanism.** It is unclear *why* collateral would move maturity.
- **Throat-clearing** ("studied extensively," "is important for … policymakers") and an
  **over-signposted roadmap** doing the work the argument should do.

---

## After (*JFQA* arc — question + estimate + identification + mechanism, contribution early)

> **Does an asset becoming eligible as collateral lengthen the maturity of the debt it backs?** We show
> that crossing the regulator's pledgeability cutoff increases the average maturity of newly issued
> debt by **1.8 years (95% CI 1.2–2.4)**, a **27% increase** relative to the just-ineligible mean, and
> compresses the issue's credit spread by **34 bps (95% CI 21–47)**. *(Financial-economics question +
> headline estimate with magnitude and interval, in the first breath, in finance units.)*
>
> Estimating this is hard because pledgeable assets are not randomly assigned: issuers with safer,
> more transparent assets both pledge more and borrow longer, so an OLS maturity–collateral slope
> conflates the collateral channel with unobserved issuer quality. *(Why it is hard — the endogeneity,
> stated in corporate-finance terms, per `jfqa-identification-strategy`.)*
>
> We identify the collateral channel from a **sharp regulatory discontinuity**: assets are scored on an
> eligibility index, and only those above a fixed, publicly known cutoff may be pledged against
> central-bank funding. Issuers cannot precisely manipulate the score — we show a smooth McCrary density
> at the cutoff and balanced pre-determined covariates — so issuers just above and just below the
> threshold differ only in pledgeability. We estimate local-linear RD effects on maturity and spreads
> with bias-corrected, robust confidence intervals and a data-driven bandwidth. *(Identification: the
> design, the manipulation test, and modern RD inference in one paragraph.)*
>
> The mechanism is a **funding-liquidity channel**: once an asset is pledgeable, the marginal lender can
> refinance the loan cheaply at the central bank, lowering the lender's required term premium and making
> long-dated claims cheaper to supply. Consistent with this, the maturity effect is **concentrated in
> issuers with weak access to unsecured funding** and **absent for issuers already flush with eligible
> collateral** — the cross-sectional signature the channel predicts. *(Economic mechanism, with a
> testable cross-sectional implication — the `jfqa-contribution-framing` move.)*
>
> Our contribution is to isolate a **causal collateral-to-maturity channel** that prior panel evidence
> could only describe as a correlation, and to give it an economic magnitude a finance reader can weigh:
> pledgeability is worth roughly a fifth of a standard deviation of issue maturity, operating through
> lender funding liquidity rather than issuer quality. *(Contribution stated early and relative to the
> specific limitation of prior work — not "we add to the literature.")* The result is **portable**: any
> setting with a discrete pledgeability or eligibility threshold can use the same design to price the
> maturity value of collateral.
>
> The paper proceeds as follows. Section II develops the funding-liquidity mechanism and its
> cross-sectional predictions; Section III describes the bond and eligibility data and validates the
> discontinuity; Section IV reports the RD estimates and their robustness. *(Brief roadmap — no
> over-signposting.)*

---

## Why the "after" meets the *JFQA* bar

Mapped to the skill checklists:

- **Result-forward, in finance units** — the headline (1.8 years; 34 bps; 27%) leads with its **magnitude
  and a 95% interval**, then is interpreted, exactly the `jfqa-writing-style` / `jfqa-contribution-framing`
  rule (report economic magnitudes, not just significance).
- **Question before literature** — the first sentence is the financial-economics question, not a survey of
  prior work (avoids the `jfqa-writing-style` literature-tour anti-pattern).
- **Identification is motivated and stress-tested** — the endogeneity is named, the RD is justified, and the
  manipulation/balance tests are previewed in the intro (`jfqa-identification-strategy`: show *why* the design
  breaks the confound, with a density and covariate-balance check).
- **Mechanism with a testable signature** — the funding-liquidity channel makes a cross-sectional prediction
  (concentrated where unsecured access is weak), which the design then checks, satisfying the
  `jfqa-contribution-framing` "name the mechanism and test its implication" standard.
- **Contribution is specific and bounded** — it states what is new *relative to prior panel correlations* and
  does not over-claim beyond the local RD estimand (`jfqa-writing-style`: conclusions must not exceed the
  design).
- **Quantitative discipline** — modern RD inference (bias-corrected robust CIs, data-driven bandwidth) is
  signaled, matching the journal's quantitative-methods identity.

> Next: when the abstract is drafted, hold it to the **≤100-word, one-paragraph** JFQA cap
> (see [`../../skills/jfqa-writing-style/SKILL.md`](../../skills/jfqa-writing-style/SKILL.md)), and adapt the
> reproducible analysis skeleton in [`../code/`](../code/) to turn this introduction arc into a full
> empirical workflow.
