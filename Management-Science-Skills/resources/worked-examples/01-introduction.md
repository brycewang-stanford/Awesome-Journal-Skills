> **Illustrative teaching example.** The paper, model, setting, and every number below are **fictional**
> and exist only to demonstrate *Management Science* (INFORMS) house style. No real-paper facts are
> stated, and no policy is invented. Corresponding skills:
> [`mgsci-writing-style`](../../skills/mgsci-writing-style/SKILL.md),
> [`mgsci-contribution-framing`](../../skills/mgsci-contribution-framing/SKILL.md),
> [`mgsci-topic-selection`](../../skills/mgsci-topic-selection/SKILL.md), and
> [`mgsci-theory-development`](../../skills/mgsci-theory-development/SKILL.md).

# Worked Example: A *Management Science*-Style Introduction (before → after)

This demonstrates the Management Science introduction discipline from `mgsci-writing-style` and
`mgsci-contribution-framing`: **front-load the result, pair every symbol with plain-language intuition,
write for a cross-department reader, and state — in words — the decision-relevant insight that travels
beyond one niche.** Management Science is deliberately **bimethodological and multi-department**: an
analytical model (Optimization, Operations Management, Stochastic Models, economic theory) and a sharp
empirical/behavioral study are equally at home, but each must clear the same bar — *rigor in service of
a managerial insight that a reader in another Department still finds informative*
(`mgsci-topic-selection`).

We illustrate with the **analytical lane** on purpose, because that is where the symbol-dump anti-pattern
is most common, and we flag where the contribution is framed to **travel across Departments** (here:
Operations Management → Revenue Management → Finance).

**Illustrative paper (fictional):** *"When to Promise: Lead-Time Quotation under Demand the Firm Cannot
See."* Fictional model: a firm quotes a delivery lead time to each arriving customer; customers are
impatient and balk if the quote is too long; the firm cannot observe the true demand state and must infer
it from the order stream.

---

## Before (symbol dump — buries the result, reads as a proof transcript)

> Consider a continuous-time M/M/1 make-to-order queue with arrival rate $\lambda$, service rate $\mu$,
> and an unobserved modulating state $\theta \in \{\theta_L, \theta_H\}$ governed by a generator matrix
> $Q$. Let $\pi_t$ denote the firm's posterior belief that $\theta = \theta_H$, evolving per the
> Wonham filter $d\pi_t = \kappa(\pi_t)\,dt + \sigma(\pi_t)\,dN_t$. The firm chooses a quoted lead time
> $\ell(\pi_t)$ to maximize the discounted objective $J = \mathbb{E}\!\int_0^\infty e^{-rt}\,
> [p\,\mathbf{1}\{\text{accept}\} - c\,W_t]\,dt$ subject to the customer acceptance rule
> $\mathbf{1}\{v - \beta \ell \ge 0\}$. We characterize the Hamilton–Jacobi–Bellman equation and prove
> existence of a stationary optimal policy. Section 2 reviews the queueing-control literature. Section 3
> sets up the model. Section 4 derives the HJB equation. Section 5 proves Theorem 1. Section 6 concludes.

**What's wrong (against `mgsci-writing-style` / `mgsci-theory-development` / `mgsci-topic-selection`):**

- **Symbol dump with no verbal reading.** Eight symbols ($\lambda, \mu, \theta, Q, \pi_t, \kappa, \sigma,
  \beta$) arrive before the reader learns *what decision the paper is about* — the named anti-pattern
  "an analytical paper reads as a symbol dump with no verbal intuition."
- **No result on the first page.** The HJB equation and "existence of a stationary policy" are machinery,
  not a finding; a Department Editor desk-screening cannot see what changes for a manager.
- **Sub-niche jargon undefined** ("Wonham filter," "modulating state") in a venue read across Departments.
- **No decision relevance and no cross-department travel** — `mgsci-contribution-framing` requires naming
  the decision that moves and who *else* learns from it; neither appears.
- **Over-signposted roadmap** standing in for an argument; reads as a methodology paper aimed at a sister
  journal (Operations Research), not the managerial-science angle Management Science wants.

---

## After (Management Science arc — result first, symbol ↔ intuition, cross-department insight)

> **When a firm cannot directly see how busy demand is about to get, how long a delivery lead time should
> it promise an arriving customer — and what does getting this wrong cost?** We show that the optimal
> quote should be *more cautious than the firm's current backlog alone would justify*: it should lengthen
> the promised lead time as soon as the recent order stream hints that demand is shifting up, **before**
> the backlog actually builds. In our model this "promise-ahead-of-the-backlog" rule raises long-run
> profit by **6–9%** relative to the common practice of quoting off observed workload, and it cuts the
> rate of broken promises by roughly a third. *(decision + result + magnitude, in the first breath —
> `mgsci-writing-style`: front-load the result.)*
>
> The problem is hard because the firm must act on a demand state it never observes. We model demand as
> switching between a slow and a busy regime that the firm cannot see, and let it form a belief $\pi$ —
> read simply as **the firm's current confidence that demand has turned busy** — that it updates from the
> stream of incoming orders. The only lever is the quoted lead time $\ell$; customers accept if the quote
> is short enough to be worth waiting for, and walk away otherwise. *(every symbol introduced with its
> plain-language reading; notation minimal and used immediately — `mgsci-theory-development`, Lane A.)*
>
> Our main result is a **threshold rule with a lead**: there is a confidence level above which the firm
> should already be quoting the long lead time, and that level sits *below* the point at which the backlog
> would, on its own, call for caution. The comparative statics give the managerial reading directly — the
> more abruptly demand can switch, and the more impatient customers are, the larger this lead should be.
> *(proposition stated in words first; comparative statics carry the intuition, not the algebra —
> `mgsci-writing-style`: pair every symbol with intuition.)*
>
> The decision-relevant insight is that **lead-time quotation is an inference problem, not just a capacity
> problem**: a firm that quotes purely off its visible workload is structurally late, and the cost of that
> lateness is largest exactly when demand is most volatile — precisely when reliable promises matter most.
> *(the "so what for a decision" stated explicitly — `mgsci-contribution-framing`, axis 2.)* This travels
> across Departments. For **Operations Management** it reframes due-date quoting as filtering under
> uncertainty. For **Revenue Management & Market Analytics** it says the same belief that should move the
> lead-time promise should move the *price*, since both ration the same hidden capacity. And for
> **Finance**, the broken-promise rate is a tractable, order-flow-based proxy for a firm's operational
> risk that an outside analyst could in principle estimate. *(cross-department travel named concretely —
> `mgsci-contribution-framing`, axis 3; the multi-department reach is the case for Management Science over
> a focused sister journal, per `mgsci-topic-selection`.)*
>
> The paper proceeds as follows. Section 2 sets up the model and the belief dynamics; Section 3 derives
> and interprets the threshold-with-lead rule; Section 4 quantifies the profit and reliability gains and
> shows which results survive when customers are heterogeneous. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the Management Science bar

Mapped to the skill checklists:

- **Result front-loaded** — the decision (how long a lead time to promise), the rule (promise ahead of the
  backlog), and the magnitude (6–9% profit; ~⅓ fewer broken promises) appear in the first paragraph, not
  after the HJB machinery (`mgsci-writing-style`: "front-load the result… the result, the mechanism, and
  the decision relevance early").
- **Every symbol paired with intuition** — $\pi$ is "the firm's confidence demand has turned busy," $\ell$
  is "the quoted lead time"; the proposition is stated in words before any threshold algebra, so a reader
  never holds five symbols at once (`mgsci-writing-style`; `mgsci-theory-development`, Lane A comparative
  statics + plain-language intuition).
- **Written for a cross-department reader** — no undefined "Wonham filter"; the inference idea is legible
  to an operations, marketing, *and* finance reader (`mgsci-writing-style`: write for a cross-department
  reader).
- **Decision-relevant, cross-department contribution stated explicitly** — what decision changes
  (quote off *beliefs*, not workload), in which direction, and who else learns from it (OM, Revenue
  Management, Finance) — the three contribution axes of `mgsci-contribution-framing`, and the
  cross-department travel that makes the fit case for Management Science over Operations Research /
  M&SOM in `mgsci-topic-selection`.
- **Magnitude calibrated honestly** — a bounded 6–9% range with a stated robustness check (customer
  heterogeneity) rather than an inflated universal claim (`mgsci-contribution-framing`: calibrate
  magnitude honestly).
- **Method demoted to a tool** — the belief-updating machinery is mentioned only where the model is set
  up, never as the lead, avoiding the symbol-dump / methodology-paper anti-pattern that routes papers to
  a sister journal.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified** Management
> Science papers spanning its method and Department diversity, and
> [`../code/`](../code/) for the empirical-lane command chain (the analytical lane above is illustrated in
> prose; for analytical tooling see [`../external_tools.md`](../external_tools.md)). The cross-cutting
> design and reporting guidance lives once in the shared hub:
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).
