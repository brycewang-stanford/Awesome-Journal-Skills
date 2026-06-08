# Worked Example — Introduction in JOM house style

> **Illustrative and FICTIONAL.** The paper, firms, and numbers below are invented to demonstrate
> *Journal of Operations Management* (JOM) house style. No real study is described. JOM style here is
> derived only from this pack's own skills (`jom-writing-style`, `jom-contribution-framing`,
> `jom-theory-development`, `jom-literature-positioning`, `jom-methods`). Confirm format rules against
> this pack's `official-source-map.md`.

JOM publishes predominantly **empirical** operations and supply-chain management research (survey,
archival, behavioral, mixed). A JOM introduction must make the **operational/SCM phenomenon** the
star, ground a **theoretical contribution** (JOM expects theory, not just a clean effect), and tie the
finding to an **operating decision a manager actually makes**.

---

## ❌ Before (effect-hunting, atheoretical, method-forward)

> Supply chain disruptions are increasingly common. We study whether supplier diversification reduces
> disruption losses. Using a sample of manufacturing firms, we run regressions of disruption losses on
> the number of suppliers, controlling for firm size and industry. We find that firms with more
> suppliers have lower losses (β = −.18, p < .05). This has implications for supply chain managers.

What's wrong (per `jom-writing-style` + `jom-contribution-framing` + `jom-theory-development`):

- **No theoretical lens.** JOM is not a place for an atheoretical correlation; *why* would
  diversification help, and through what mechanism — and when would it *not*?
- **The operational decision is vague.** "Number of suppliers" is a count, not a decision; managers
  choose *how to allocate volume across suppliers under what contracts*.
- **Endogeneity ignored.** Sourcing structure is *chosen*, plausibly by the same firms that anticipate
  disruption — the regression invites a reverse-causality and selection critique (`jom-methods`).
- **"Has implications" is not a contribution.** For whom, deciding what, differently than before?
- **Method-forward** ("we run regressions") instead of phenomenon- and theory-forward.

---

## ✅ After (phenomenon-forward, theory-grounded, decision-anchored)

> When a key supplier fails, some buyers absorb the shock in days while others lose a quarter of
> output for months. The difference is often not *how many* suppliers a firm has, but how it has
> **structured the relationships** — whether it can rapidly reallocate volume to a qualified alternate.
> Yet the operations literature has largely treated supplier diversification as a count, leaving open
> *when* redundancy actually buys resilience and when it just adds coordination cost.
>
> We draw on the **organizational information-processing view** to argue that diversification reduces
> disruption losses only when it is paired with the *coordination capability* to switch — pre-qualified
> alternates, shared forecasts, flexible contracts. Absent that capability, added suppliers raise
> information-processing requirements faster than they add real options, so redundancy and resilience
> decouple. This reframes the managerial question from "how many suppliers?" to "**redundancy plus the
> capability to use it**," and predicts an *interaction*, not a main effect.
>
> We test this with a (fictional) two-wave survey of 280 manufacturing plants matched to objective
> disruption-recovery records, using a supplier-switching instrument (a plant's exposure to a distant
> regulatory change that altered alternates' availability) to address the **endogeneity of sourcing
> structure**. By the end of this introduction the reader knows the phenomenon (uneven disruption
> recovery), the theory (information processing), the decision (structure relationships for
> switchability, not just add suppliers), and the empirical strategy that defends the causal claim.
>
> We contribute to operations theory by specifying the **boundary condition** under which
> diversification builds resilience, and to practice by redirecting sourcing investment from supplier
> *count* to switching *capability*.

Why it works:

- **The SCM phenomenon leads** (uneven recovery), and the **operational decision** is concrete and
  managerial (structure relationships for switchability) — `jom-writing-style`.
- **A theoretical lens** (information-processing view) generates a *mechanism and a boundary
  condition* (the interaction), which is the contribution — `jom-theory-development`.
- **Endogeneity of the operating choice is confronted** with an identification strategy, pre-empting
  the central referee objection that sourcing is chosen, not assigned — `jom-methods`.
- **The contribution is stated as a delta** to both theory (boundary condition) and practice
  (reallocate investment), not "has implications" — `jom-contribution-framing`.
- The vendored `code/` (IV / first-stage diagnostics) supports the switching-instrument analysis.
