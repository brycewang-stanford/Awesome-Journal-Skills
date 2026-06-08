> **Illustrative teaching example.** The paper, banks, reform, and every number below are **fictional** and
> exist only to demonstrate *Journal of Financial Intermediation* house style. No real-paper facts are
> stated, and no real bank or regulation is invoked. Corresponding skills:
> [`jfi-writing-style`](../../skills/jfi-writing-style/SKILL.md),
> [`jfi-topic-selection`](../../skills/jfi-topic-selection/SKILL.md),
> [`jfi-identification-strategy`](../../skills/jfi-identification-strategy/SKILL.md), and
> [`jfi-contribution-framing`](../../skills/jfi-contribution-framing/SKILL.md).

# Worked Example: A *Journal of Financial Intermediation*-Style Introduction (before → after)

This demonstrates the introduction arc JFI rewards (from `jfi-writing-style` and `jfi-contribution-framing`):
**intermediation question → the institution & friction → data/model & identifying variation → headline
estimate with magnitude and interval → identification → economic mechanism for the intermediary → brief
roadmap.** The governing rule from `jfi-writing-style` is **explain the intermediation mechanism before the
specifications**, and from `jfi-topic-selection`, the paper must be **centrally about banking and
intermediation**, not generic finance that happens to use bank data. Every acronym is defined on first use.

**Illustrative paper (fictional):** *"Does Losing a Relationship Lender Tighten Credit? Evidence from
Branch-Closure Shocks."* Fictional setting: a wave of bank-branch closures that severs incumbent lending
relationships for some small firms but not comparable firms nearby, observed in a credit register with
bank-firm-quarter loan data.

---

## Before (buries the contribution — typical first-draft intro)

> The role of banks in providing credit has been extensively studied in the financial intermediation
> literature. Relationship lending is an important topic, and many papers have examined how bank
> relationships affect firm financing. In this paper, we use a difference-in-differences design exploiting
> branch closures to study the effect of losing a relationship lender on firm credit. We estimate several
> specifications with firm and time fixed effects and perform robustness checks. Our results contribute to
> the literature on relationship lending and have implications for policy. Section 2 reviews the literature,
> Section 3 describes the data, Section 4 presents the methods, Section 5 reports results, and Section 6
> concludes.

**What's wrong (against `jfi-writing-style` / `jfi-topic-selection` / `jfi-identification-strategy`):**

- **Leads with the method** ("we use a difference-in-differences design") instead of the intermediation
  question — and never names the *friction* (relationship-specific soft information) that makes banks
  special, the core `jfi-contribution-framing` miss.
- **No headline estimate, no magnitude, no interval.** A referee cannot tell whether losing the lender cut
  credit by 2% or 25%, or with what precision.
- **Identifying variation is invisible.** "Branch closures" is asserted, but the reader never learns why
  closures are plausibly unrelated to the borrower's own prospects (fails the
  `jfi-identification-strategy` bar of making the variation credible and ruling out demand).
- **No intermediary mechanism.** It is unclear whether the credit drop reflects lost soft information,
  switching costs, or a pure supply contraction at the closing bank.
- **Generic-finance framing.** Nothing here would distinguish the paper from any firm-financing study; it
  does not read as banking (the `jfi-topic-selection` desk-screen failure).
- **Throat-clearing and an over-signposted roadmap** doing the work the argument should do.

---

## After (JFI arc — intermediation question + estimate + identification + mechanism, contribution early)

> **When a small firm loses the bank that holds its relationship-specific soft information — the private,
> hard-to-transfer knowledge a lender accumulates over years — can it replace that credit elsewhere, or does
> the information simply vanish with the relationship?** Using branch closures that sever incumbent lending
> relationships for some firms but not observably similar firms a few blocks away, we estimate that losing a
> relationship lender reduces a firm's total bank credit by **11.4% (95% CI 8.6–14.2)** over the next year
> and roughly doubles its probability of a credit gap, with the loss falling almost entirely on
> informationally opaque firms. *(Intermediation question + the friction + headline estimate with magnitude
> and interval, in the first breath; "relationship-specific soft information" defined in place.)*
>
> Identifying this effect is hard because firms that lose a lender may differ from those that do not: a bank
> may close branches precisely where local borrowers are deteriorating, so a raw before-after credit drop
> would confound the lost relationship with weak demand. *(Why it is hard — the endogeneity of the shock,
> stated in intermediation terms, per `jfi-identification-strategy`.)*
>
> We exploit **branch closures driven by a post-merger consolidation program** — closures determined by
> overlap in the merging banks' branch networks rather than by local borrower quality — and compare credit
> to firms whose relationship branch closed against firms of the same size, industry, and pre-shock credit
> quality whose branch survived, with firm and bank-by-quarter fixed effects and an event-study path showing
> no differential pre-trend in credit. The identifying variation is the *network-overlap* component of
> closures, which we argue is orthogonal to the borrower's own prospects. *(Data and identifying variation
> in one paragraph; the design defeats the demand confound, per `jfi-identification-strategy` and
> `jfi-data-analysis`.)*
>
> The contraction is an **information-loss** channel, not a generic supply cut: the effect is concentrated in
> opaque firms (young, no audited statements), rises with the *length* of the severed relationship — a proxy
> for accumulated soft information — and is not offset by borrowing from transaction lenders, who lack the
> private signal. A pure supply story would predict similar losses for transparent firms and full
> replacement at other banks; we observe neither. *(Economic mechanism named and adjudicated against the
> leading rival, in intermediary terms, per `jfi-contribution-framing`.)*
>
> Our contribution is to convert a long-standing claim of intermediation theory — that relationship lenders
> hold non-transferable soft information — into a **credit-supply estimate with a stated magnitude and an
> isolated information channel**, rather than an association between relationships and credit. This matters
> for financial intermediation because it quantifies the social cost of severed banking relationships and
> identifies *which* borrowers bear it, informing both merger review and branch-network policy. *(Contribution
> stated early, in intermediation terms, relative to a specific rival reading.)*
>
> The paper proceeds as follows. Section 2 describes the consolidation program and the credit register;
> Section 3 presents the overlap-based design and the event-study tests; Section 4 reports the credit
> results, the opacity and relationship-length heterogeneity, and the mechanism and robustness checks.
> *(Brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JFI bar

Mapped to the skill checklists:

- **Intermediation question and friction lead, method follows** — the opening names the institution (the
  relationship lender) and the friction (non-transferable soft information) before any estimator
  (`jfi-writing-style`: explain the intermediation mechanism before the specifications).
- **Headline estimate is quantity-first with an interval** — the 11.4% credit reduction leads with its
  magnitude **and a 95% CI**, then is interpreted, rather than "the model shows…" (`jfi-data-analysis`:
  report uncertainty, translate to economic terms).
- **Identifying variation is visible and credible** — the network-overlap component of post-merger closures
  is the exogenous variation, with covariate-matched controls and a pre-trend test, the core
  `jfi-identification-strategy` move of ruling out the demand confound.
- **The leading rival is named and adjudicated** — a pure supply cut would hit transparent firms equally and
  allow replacement at other banks; the opacity concentration and failure-to-replace are the opposite,
  satisfying the design-defense test.
- **Mechanism is about the intermediary** — the effect scales with relationship length (accumulated soft
  information) and concentrates in opaque borrowers, the contribution type `jfi-contribution-framing` calls
  an intermediation-mechanism claim, not a reduced-form sign.
- **Reads as banking, not generic finance** — soft information, relationship lenders, and transaction
  lenders are the load-bearing concepts, satisfying the `jfi-topic-selection` "centrally about
  intermediation" desk screen.

> Next: adapt the reproducible analysis skeleton in [`../code/`](../code/) when turning this introduction
> arc into a full empirical workflow, and stress-test the design against
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md).
