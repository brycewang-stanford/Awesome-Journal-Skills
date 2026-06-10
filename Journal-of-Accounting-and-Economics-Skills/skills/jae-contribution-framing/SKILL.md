---
name: jae-contribution-framing
description: Use when articulating the contribution of a Journal of Accounting and Economics (JAE) manuscript — stating explicitly what the paper teaches about accounting's economic role (information content, contracting, disclosure, standards) and why an economics-based result advances the positive-accounting literature beyond an incremental correlation.
---

# Contribution Framing for JAE (jae-contribution-framing)

## When to trigger

- Results exist but the "so what for accounting and economics?" is thin
- A reviewer calls the contribution "incremental" or "a known result in a new sample"
- The intro promises a contribution the results do not actually deliver
- You cannot say in one sentence what economic understanding the paper changes

## What counts as a JAE contribution

JAE rewards advancing the **economic understanding** of an accounting phenomenon, not merely documenting a new association. A strong contribution does one or more of:

- **Identifies a mechanism**: shows *why* accounting matters economically (e.g., disclosure reduces information asymmetry and thereby the cost of capital), with cross-sectional evidence tied to the friction.
- **Resolves an economic tension**: adjudicates between competing economics-based explanations (efficient contracting vs. opportunism; information vs. agency).
- **Exploits a clean identification**: turns a correlation the literature knew into a credibly causal economic result via a shock/IV/RD.
- **Informs standards or regulation positively**: shows the economic consequences of a rule (SOX, IFRS, Reg FD, an ASU) — predicting and explaining effects, not prescribing policy.

## Make the contribution explicit and economic

State the contribution as a claim about the world: *"We show that [accounting feature] affects [economic outcome] through [mechanism], because [economic friction]."* Avoid framing the contribution as "first to study X in this dataset." Connect it to the specific literature stream from `jae-literature-positioning` and quantify the **economic magnitude** so the result is consequential, not just significant.

## Honest scope

JAE editors and reviewers are skeptical of overreach. State what the design can and cannot identify; do not claim causality the identification does not support, and do not extend the result beyond the sample's economic setting. A tightly scoped, well-identified contribution beats an ambitious but fragile one.

## Where it appears

The contribution belongs **up front** (intro) and is **closed** in the discussion: restate the mechanism, the magnitude, the boundary conditions, and the implications for contracting, disclosure, or standard-setting — plus concrete follow-on questions.

## Checklist

- [ ] One-sentence economic contribution statement (mechanism + outcome + friction)
- [ ] Tied to the named literature stream and the tension it resolves
- [ ] Economic magnitude, not just significance, stated
- [ ] Causal claims matched to the identification (no overreach)
- [ ] Standards/regulation implications framed positively, not normatively
- [ ] Contribution stated in the intro and closed in the discussion

## Anti-patterns

- **"First to study X"** as the contribution.
- **Mechanism-free** result presented as theory advance.
- **Overclaiming causality** beyond the design.
- **Normative drift** ("regulators should...") in place of positive consequences.
- **Magnitude silence** — significance with no economic interpretation.


## Contribution pass for Journal of Accounting and Economics

Use this as a second-pass capability check. First lock the economic mechanism, accounting setting, identification or model, and market/contracting consequence; then test whether the manuscript addresses accounting-economics reviewers who expect economics discipline, identification, and market or contracting implications.

- **Primary move:** Translate the result into who learns what, which mechanism changes, and which rival explanation is ruled out; keep the claim narrower than the evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAR for accounting research breadth, TAR for accounting flagship breadth, Review of Accounting Studies for archival/accounting focus; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Contribution (one sentence)】accounting feature → economic outcome via mechanism
【Type】mechanism / tension-resolution / identification / regulatory consequence
【Stream advanced】(from jae-literature-positioning)
【Economic magnitude】...
【Scope / boundary】what it does and does not identify
【Discussion close】implications for contracting / disclosure / standards
【Next step】jae-tables-figures
```
