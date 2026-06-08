> **Illustrative teaching example.** The paper, setting, hypotheses, and every number below are
> **fictional** and exist only to demonstrate AJPS house style. No real-paper facts are stated, and no
> real policy is described. Corresponding skills:
> [`ajps-writing-style`](../../skills/ajps-writing-style/SKILL.md),
> [`ajps-topic-selection`](../../skills/ajps-topic-selection/SKILL.md),
> [`ajps-theory-building`](../../skills/ajps-theory-building/SKILL.md), and
> [`ajps-research-design`](../../skills/ajps-research-design/SKILL.md).

# Worked Example: An AJPS-Style Introduction (before → after)

This demonstrates the AJPS introduction bar from this pack's skills: by the end of the introduction the
reader knows the **question, the argument, the design, the finding, and why it matters**
(`ajps-writing-style`: "front-load the contribution"), the question is **sharp with a generalizable
answer** legible to a broad political-science audience (`ajps-topic-selection`), the **hypotheses are
stated before the results** (`ajps-theory-building`), and **identification is stated, not asserted**
(`ajps-research-design`). It is written to be tightened toward the **<= 10,000-word Article cap** and to
stay **fully anonymized** for double-blind review.

**Illustrative paper (fictional):** *"Seeing the Ballot Box: Does Polling-Place Proximity Raise Turnout
Among First-Time Voters?"* Fictional setting: a (fictional) sub-national electoral authority that
consolidated precincts on a population-threshold rule, moving some new registrants' assigned
polling places while leaving otherwise-identical registrants just across the threshold unaffected.

---

## Before (buries the contribution — typical first-draft intro)

> The relationship between the cost of voting and political participation has long been of interest to
> scholars of political behavior. A large literature examines how distance, registration rules, and
> convenience shape turnout. In this paper, we use a regression discontinuity design exploiting a
> precinct-consolidation rule to study the effect of polling-place distance on turnout. We assemble
> administrative voter-file records and estimate local linear specifications with several bandwidths.
> Turnout is an important topic for democratic theory and election administration. Section 2 reviews the
> literature, Section 3 describes the data, Section 4 presents the design, Section 5 reports results, and
> Section 6 concludes.

**What's wrong (against this pack's skills):**

- **Leads with the method** ("we use a regression discontinuity design") instead of the question —
  exactly the anti-pattern `ajps-writing-style` and `ajps-topic-selection` warn against.
- **No answer on page one.** A reader cannot tell what was found, for whom, or how large.
- **No magnitude or uncertainty** in the intro — only a method and a topic. `ajps-data-analysis` demands
  effect sizes and intervals, not just "we estimate."
- **No hypothesis stated before results** — `ajps-theory-building` wants the directional, testable
  expectation up front.
- **Identification merely named, not defended;** the continuity logic that licenses the causal reading is
  absent (`ajps-research-design`: "defend the assumption, do not assert it").
- **No contribution.** "Turnout is important" is throat-clearing, not a "so what" that moves a theory or
  the record.
- **Over-signposted roadmap** doing the work the argument should do.

---

## After (AJPS arc — question + argument + design + finding + contribution, hypotheses early)

> **Does making the polling place easier to reach turn newly registered citizens into actual voters — or
> does the convenience of voting matter mainly for those already inclined to participate?** We show that
> assigning first-time registrants a polling place 1 km closer raises their probability of voting by
> **2.1 percentage points** (95% CI: 1.3–2.9), off a first-time-voter baseline of 38%, with no detectable
> effect among habitual voters. *(question + headline answer with magnitude and uncertainty, in the first
> breath.)*
>
> Our argument is a cost-of-participation mechanism with a scope condition: for citizens who have not yet
> built a voting habit, the fixed cost of locating and traveling to an unfamiliar polling place is
> pivotal, whereas for habitual voters that cost is already sunk into routine. This yields a testable
> expectation stated before we look at the results — **H1: proximity raises turnout, and the effect is
> larger for first-time than for habitual voters** — and a pattern that would disconfirm it (a uniform or
> reversed gradient). *(argument → directional, pre-registered-style hypothesis with a disconfirming
> pattern named — `ajps-theory-building`.)*
>
> Estimating this cleanly is hard because distance to the polls is not random: people who live far from
> civic infrastructure differ systematically in income, mobility, and political interest, so a raw
> distance–turnout correlation conflates the cost of voting with who bears it. We exploit a
> precinct-consolidation rule that reassigned polling places **only for registrants on one side of a
> fixed population threshold**, leaving otherwise-identical registrants just across it unaffected. Because
> registrants cannot precisely sort around the administrative threshold, those just above and just below
> are comparable in expectation; we verify this with covariate-continuity and density (manipulation)
> tests at the cutoff and show robustness across bandwidths and to a bias-corrected estimator. *(the
> identification problem named, then the design that solves it and the checks that defend it —
> `ajps-research-design`.)*
>
> Our contribution is to separate **two explanations the literature has tended to bundle**: that lowering
> the cost of voting expands the electorate, versus that it merely eases participation for the already-
> committed. By isolating a population — first-time registrants — for whom the habit channel is absent by
> construction, we show the cost channel operates on its own, and we bound where it does not. *(contribution
> stated early, relative to a specific prior view — `ajps-topic-selection` "a contribution, not a
> finding.")* Beyond this setting, the result implies that **convenience-voting reforms should be evaluated
> by whom they activate, not by their average effect**: a reform that barely moves aggregate turnout may
> still substantially enfranchise new entrants. *(generalizable lesson for a broad political-science
> readership.)*
>
> The paper proceeds as follows. Section 2 describes the consolidation rule and the voter-file data;
> Section 3 presents the discontinuity design and the main estimates; Section 4 tests the
> first-time-versus-habitual heterogeneity and probes robustness. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the AJPS bar

Mapped to this pack's skill checklists:

- **Contribution front-loaded** — question, argument, design, finding, and "so what" are all present by
  the end of the introduction, with the headline number and its interval up front
  (`ajps-writing-style`).
- **Sharp question, generalizable answer** — phrased for a broad political-science audience (behavior,
  election administration, democratic theory), with a lesson that travels beyond the case
  (`ajps-topic-selection`).
- **Hypothesis stated before results, with a disconfirming pattern** — the directional expectation and
  its scope condition precede any estimate (`ajps-theory-building`).
- **Identification defended, not asserted** — the continuity logic, the manipulation/density test, and
  bandwidth/bias-correction robustness are named where the design is introduced
  (`ajps-research-design`); the modern-RDD checks mirror the pack's `code/` skeleton.
- **Magnitude and uncertainty, not stars** — "2.1 pp (95% CI 1.3–2.9), off a 38% base" reports an effect
  size and an interval (`ajps-data-analysis`).
- **Method demoted to a tool** — "regression discontinuity" appears only where the design is discussed,
  never as the lead, avoiding the "leading with the estimator" anti-pattern.
- **Anonymized** — no author, institution, or self-citation tells; ready for double-blind review
  (`ajps-writing-style`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified AJPS papers**
> whose introductions execute this arc, and [`../code/`](../code/) for the RDD command chain referenced
> above. For the standard referee objections to a design like this, see the shared
> [`reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and [`reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md).
