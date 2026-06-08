> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate *Review of Finance* house style. No real-paper facts are stated, and no real
> firm or policy is invoked. Corresponding skills:
> [`rof-writing-style`](../../skills/rof-writing-style/SKILL.md),
> [`rof-topic-selection`](../../skills/rof-topic-selection/SKILL.md),
> [`rof-contribution-framing`](../../skills/rof-contribution-framing/SKILL.md), and
> [`rof-identification-strategy`](../../skills/rof-identification-strategy/SKILL.md).

# Worked Example: A *Review of Finance*-Style Introduction (before → after)

This demonstrates the introduction arc *Review of Finance* rewards (from `rof-writing-style` and
`rof-contribution-framing`): **financial-economics question → headline estimate with magnitude and
interval → identification → economic mechanism → contribution relative to the literature → brief
roadmap.** RoF referees are asked to apply **top-three-finance-journal standards**, so the introduction
must convince a JF/RFS/JFE-calibrated reader that the design identifies something and that the magnitude
matters. Write **result-forward** and report economic magnitudes in plain finance units (bps, monthly
alpha, percentage of a standard deviation).

**Illustrative paper (fictional):** *"Index Membership and the Cost of Equity: Evidence from a Reweighting
Threshold."* Fictional setting: a single equity market whose flagship index admits firms by a mechanical
free-float rank, creating a sharp cutoff in passive ownership.

---

## Before (buries the contribution — typical first-draft intro)

> The effect of index membership on stock prices has received considerable attention in the finance
> literature. Researchers have debated whether index inclusion affects firm value, the cost of capital,
> liquidity, and comovement. In this paper, we revisit this question using a new sample and study the
> relationship between index membership and the cost of equity. We employ panel regressions with firm and
> year fixed effects, as well as an instrumental-variables strategy. We find a significant effect.
> Understanding index effects is important for investors, firms, and regulators. The remainder of the
> paper is organized as follows. Section 2 reviews the literature, Section 3 describes the data, Section 4
> presents the empirical strategy, Section 5 reports the results, and Section 6 concludes.

**What's wrong (against `rof-writing-style` / `rof-contribution-framing` / `rof-identification-strategy`):**

- **Leads with a literature debate**, not the financial-economics question — the named anti-pattern in
  `rof-writing-style`.
- **No headline estimate, no magnitude, no interval.** "A significant effect" is significance without
  economic magnitude; a top-3-calibrated reader cannot judge importance (fails `rof-contribution-framing`).
- **Identification is asserted, not motivated.** Why fixed effects *and* IV, and what endogeneity does each
  break? Unstated, and the instrument is unnamed (fails `rof-identification-strategy`).
- **No economic mechanism** linking membership to the cost of equity.
- **Throat-clearing** ("considerable attention," "is important for … regulators") and an
  **over-signposted roadmap**.

---

## After (*RoF* arc — question + estimate + identification + mechanism, contribution early)

> **Does joining the flagship index lower a firm's cost of equity, and if so, through demand or through
> information?** We show that crossing the index's free-float inclusion cutoff lowers the implied cost of
> equity by **58 bps (95% CI 39–77)** and raises passive ownership by **4.1 percentage points**, with the
> price effect **fully reversing within two years** for firms that later drop out. *(Financial-economics
> question + headline estimate with magnitude and interval, in the first breath, in finance units.)*
>
> Estimating this is hard because index membership is **not random**: index providers admit larger, more
> liquid, more visible firms, all of which independently command a lower cost of equity, so an OLS
> membership coefficient conflates the index-demand channel with the firm characteristics that earn
> membership. *(Why it is hard — the endogeneity, stated in asset-pricing terms, per
> `rof-identification-strategy`.)*
>
> We identify the membership effect from the index's **mechanical free-float rank cutoff**: firms are
> ordered on a pre-set rule and only those above a fixed rank are admitted, so firms just above and just
> below the threshold are similar on observables but differ discretely in index demand. We estimate
> local-linear RD effects with bias-corrected robust confidence intervals and a data-driven bandwidth,
> show a smooth density at the cutoff (no manipulation of the float rank), and confirm balance on size,
> liquidity, and profitability. *(Identification: a sharp design, the manipulation test, and modern RD
> inference in one paragraph.)*
>
> The mechanism is a **price-pressure-plus-liquidity** channel, not an information channel: the cost-of-
> equity decline is **concentrated in firms with the thinnest pre-inclusion liquidity** and is
> **accompanied by lower bid-ask spreads but no change in analyst coverage or forecast dispersion** — the
> cross-sectional signature that distinguishes a demand/liquidity story from an information story. *(Economic
> mechanism, with a discriminating test between the two leading explanations — the `rof-contribution-framing`
> move.)*
>
> Our contribution is to deliver a **causal, economically sized** index-membership effect on the cost of
> equity — roughly 58 bps, a fifth of a standard deviation of implied cost of capital — and to show it
> operates through liquidity/demand rather than information, adjudicating a debate that prior panel and
> event-study evidence left open. *(Contribution stated early and relative to the specific limitation of
> prior work — not "we add to the literature.")* The design is **portable**: any index with a mechanical
> admission threshold can be used to price the cost-of-capital value of passive demand.
>
> The paper proceeds as follows. Section 2 lays out the demand and information channels and their
> competing predictions; Section 3 describes the ownership and index data and validates the cutoff;
> Section 4 reports the RD estimates, the reversal, and robustness. *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the *Review of Finance* bar

Mapped to the skill checklists:

- **Result-forward, in finance units** — the headline (58 bps; 4.1 pp; full reversal) leads with its
  **magnitude and a 95% interval**, then is interpreted, the `rof-writing-style` / `rof-contribution-framing`
  rule (economic magnitudes, not significance).
- **Question before literature** — the first sentence is the financial-economics question, not a survey
  (avoids the `rof-writing-style` literature-debate anti-pattern), which is what a top-3-calibrated referee
  expects to see immediately.
- **Identification is motivated and stress-tested** — the endogeneity is named, the RD is justified over the
  naive panel/IV gesture, and the manipulation/balance tests are previewed (`rof-identification-strategy`).
- **Mechanism is *discriminated*, not just asserted** — the demand/liquidity vs. information channels make
  opposite cross-sectional predictions, and the design tests which one holds, meeting the
  `rof-contribution-framing` "name the rival mechanisms and let the data choose" standard.
- **Contribution is specific and bounded** — it states what is new relative to prior event-study/panel work
  and stays within the local RD estimand (`rof-writing-style`: do not over-claim beyond the design).
- **Reads to top-3 standards** — modern RD inference and a reversal test signal the quantitative rigor RoF
  referees are explicitly told to demand.

> Next: hold the abstract to the RoF **≤150-word** cap and keep the manuscript within the **60-page total**
> limit (see [`../../skills/rof-writing-style/SKILL.md`](../../skills/rof-writing-style/SKILL.md) and
> [`../official-source-map.md`](../official-source-map.md)), and adapt the reproducible analysis skeleton in
> [`../code/`](../code/) to turn this introduction arc into a full empirical workflow.
