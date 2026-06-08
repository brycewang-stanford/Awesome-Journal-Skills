> **Illustrative teaching example.** The paper, setting, and every number below are **fictional** and
> exist only to demonstrate Journal of Marketing (JM) house style. No real-paper facts are stated, and
> no policy is invented. Corresponding skills:
> [`jm-writing-style`](../../skills/jm-writing-style/SKILL.md),
> [`jm-contribution-framing`](../../skills/jm-contribution-framing/SKILL.md), and
> [`jm-topic-selection`](../../skills/jm-topic-selection/SKILL.md).

# Worked Example: A Journal-of-Marketing-Style Introduction (before → after)

This demonstrates the **JM introduction arc** distilled from this pack's own skills:
**phenomenon → why it matters → question → substantive contribution + managerial/policy contribution
(both, explicitly) → brief roadmap** — under the JM rule from `jm-writing-style` that the **first
paragraph states the real-world phenomenon, why it matters, and the question**, written for JM's
**general managerial-and-scholarly audience**, with the **dual contribution** (substantive *and*
managerial/societal) stated early. JM "emphasizes substantive marketing impact": a contribution that
rests on a new estimator rather than a new marketing insight is, per `jm-contribution-framing`, not yet
a JM paper.

**Illustrative paper (fictional):** *"When the Subscribe Button Backfires: Default Auto-Renewal and the
Hidden Cost of Coerced Retention."* Fictional setting: a streaming-service field setting in which some
sign-up flows default new customers into auto-renewal and others into an explicit opt-in.

---

## Before (buries the idea — typical first-draft intro)

> The relationship between contract defaults and consumer behavior has received attention in the
> literature. Prior research has examined opt-in versus opt-out structures in various domains. In this
> paper, we use a difference-in-differences design with a Callaway and Sant'Anna (2021)
> heterogeneity-robust estimator, supplemented by a double/debiased machine-learning specification, to
> study auto-renewal defaults at a subscription firm. We assemble a panel of customers and estimate
> event-study models. Subscription retention is an important managerial topic. Section 2 reviews the
> literature, Section 3 describes the data, Section 4 presents the empirical strategy, Section 5 reports
> results, and Section 6 concludes.

**What's wrong (against this pack's `jm-writing-style`, `jm-contribution-framing`, `jm-topic-selection`):**

- **Buried lede** — the substantive marketing question does not appear in paragraph one; the opening is
  throat-clearing ("has received attention," "is an important topic"). `jm-writing-style` names the
  buried lede as an anti-pattern.
- **Method theater** — it **leads with the estimator** (Callaway–Sant'Anna, DML) rather than the
  marketing phenomenon; all three skills flag method-first framing as an anti-pattern.
- **No managerial relevance early, and no decision maker named** — `jm-contribution-framing` requires the
  managerial/policy contribution to be *stated*, not implied, and to name a decision and a decision maker.
- **No effect size in managerial units** in the prose (`jm-writing-style` asks for magnitudes in words).
- **New-context risk unaddressed** — reads like "opt-out, already studied, now in streaming," the exact
  "new-context replication" `jm-topic-selection` rejects.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (JM arc — phenomenon + stakes + question first; dual contribution early)

> **Subscription firms increasingly default new customers into automatic renewal — but does retention
> won by default actually create value, or does it buy short-term revenue at the cost of the customer
> relationship?** We find that defaulting customers into auto-renewal raises 3-month retention by 11
> percentage points yet *lowers* their 18-month customer lifetime value by \$23 per customer (standard
> error \$6), because coerced subscribers disengage, stop recommending the service, and churn angrily
> when they discover the charge. *(phenomenon → why it matters → question, with the headline effect in
> managerial units, in the first breath.)*
>
> The question matters because default-based retention is now a routine growth lever, and because
> regulators and consumer advocates are actively scrutinizing "negative-option" billing. *(why it
> matters — managerial *and* policy stakes, made visible early.)*
>
> We study a streaming service that, for budget-reporting reasons unrelated to customer quality, rolled
> out an explicit opt-in renewal screen to some sign-up cohorts while others retained the auto-renewal
> default. Comparing customers acquired just before and just after the change, and verifying no
> pre-existing differences in engagement, lets us isolate the effect of the default itself rather than of
> who signs up. *(setting and the variation that identifies the effect — the design serves the question,
> it does not lead.)*
>
> Auto-renewal defaults raise short-run retention by **11 percentage points** but reduce 18-month CLV by
> **\$23** (SE \$6; p = .001), with the loss concentrated among customers who never actively used the
> service after sign-up; these "dormant retained" customers generate **3.4×** more negative service
> contacts and are **19%** less likely to recommend the brand. *(headline result restated with the
> mechanism, effect sizes in words and managerial units, exact SE and p-value per AMA style.)*
>
> Our **substantive contribution** is to show that a retention gain and a relationship gain can move in
> *opposite* directions: defaults manufacture the metric managers track (retention) while eroding the
> asset they actually own (the customer relationship and its lifetime value). *(substantive contribution
> — a new, consequential understanding, stated relative to the metric managers currently optimize.)*
> Our **managerial and policy contribution** is concrete: a subscription manager choosing between
> auto-renewal and explicit opt-in should price the decision in CLV, not retention — here the default
> *destroys* about \$23 of lifetime value per acquired customer despite looking like a win — and the same
> evidence gives regulators a measured consumer-welfare cost of negative-option defaults. *(managerial +
> policy contribution — named decision, named decision maker, quantified stake; both contributions stated
> in the intro, per the dual mandate.)*
>
> The paper proceeds as follows. Section 2 describes the setting and design; Section 3 reports the
> retention-versus-CLV divergence and its mechanism; Section 4 draws out the managerial and policy
> implications. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the JM bar

Mapped to this pack's skill checklists:

- **First paragraph = phenomenon → matters → question** — the `jm-writing-style` lede rule; the headline
  effect (11 pp retention; −\$23 CLV) appears immediately, in managerial units.
- **Dual contribution stated early** — a **substantive** advance (retention and relationship diverge) *and*
  a **managerial/policy** one (price the choice in CLV; a welfare cost for regulators), both in the intro,
  exactly as `jm-contribution-framing` requires ("if you can only write one, it is not yet a JM paper").
- **Substantive impact, not method, carries the paper** — the estimator is demoted to where the design is
  discussed and never leads, defusing the shared method-first anti-pattern; JM's emphasis on substantive
  marketing impact is honored.
- **New-context challenge pre-empted** — the contribution is a *reversal* (retention up, CLV down), not
  "opt-out defaults, now in streaming," which `jm-topic-selection` would reject as new-context replication.
- **General managerial-and-scholarly audience** — the question is legible to a CMO, a subscription product
  manager, *and* a policy maker; the outcome that matters (CLV, recommendation, welfare) is substantive,
  not a process-only psychological construct.
- **AMA statistics-in-text discipline** — exact effect sizes, SE, and p-value in the prose (no
  thresholds/stars), per `jm-writing-style`.

> Next: see [`../code/`](../code/) for the DiD / event-study command chain referenced above. For what JM
> specifically requires (AMA house style, page and abstract limits), defer to this pack's skills and
> [`../official-source-map.md`](../official-source-map.md).
