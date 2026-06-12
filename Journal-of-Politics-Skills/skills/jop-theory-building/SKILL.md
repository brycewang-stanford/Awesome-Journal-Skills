---
name: jop-theory-building
description: Use when turning a The Journal of Politics (JOP) idea into a theoretically innovative argument — formal/game-theoretic, empirical, or normative. JOP explicitly prizes theoretical innovation across all subfields and counts pages, so the argument must be sharp, general, and economical. Builds the argument; it does not run analyses.
---

# Theory & Argument Building (jop-theory-building)

JOP advertises that it publishes **theoretically innovative** work and treats theory **broadly** —
formal, empirical, interpretive, and normative all qualify. This skill turns your idea into an argument
a general reader recognizes as new, and tight enough to fit the **page budget**.

## When to trigger

- Moving from "interesting finding" to "argument that contributes"
- Specifying mechanisms, assumptions, and observable implications
- A reviewer said the theory is "thin," "post hoc," or "not novel"
- Linking a formal model to its empirical or substantive test

## Build the argument (mode-aware)

### Empirical / mechanism-based
- State the **mechanism**: what causes what, through what channel, under what scope conditions.
- Derive **observable implications** that could be **wrong** — the argument must be falsifiable.
- Separate predictions **unique to your account** from those shared with rivals (sets up `jop-research-design`).

### Formal / game-theoretic
- State primitives, equilibrium concept, and the **comparative statics** that carry the substance.
- Make the model **earn its place**: what does formalization reveal that prose could not?
- Pair it with an interpretable empirical or substantive payoff — JOP is general-interest, not a methods outlet.

### Normative / interpretive
- State the conceptual claim and the stakes; make the argument's structure explicit and contestable.
- Engage the strongest opposing position rather than a strawman.
- Show why the normative stakes matter for empirical politics or public life.

## The JOP innovation test

Write one sentence: *"Before this paper the field thought ___; this argument shows ___, which matters
to readers beyond my subfield because ___."* If the first blank is "no one had estimated this in case
X," the contribution is probably incremental for a general journal.

## Worked micro-example (illustrative)

A hypothetical project finds legislators co-sponsor more bills after office moves put them near
ideological opposites. Stated as a finding, it is a correlation. As a JOP argument it names a mechanism —
physical proximity lowers the cost of cross-party information exchange, raising co-sponsorship under the
scope condition of low electoral risk — and yields an implication that could be wrong, unique to the
proximity account and not shared by a pure homophily rival. That falsifiable contrast is what makes the
argument contribute rather than describe.

## Referee pushback patterns and the JOP fix

- *"The theory is thin — this is a list of expected signs."* Name the mechanism (what acts on what,
  through what channel, under what scope) and derive at least one implication that could fail.
- *"The formal model has no payoff here."* Pair the comparative statics with an interpretable empirical or
  substantive consequence; JOP is general-interest, not a methods outlet.

## Keep it economical (page budget)

- A general reader needs the logic, not every contingency — state the core argument cleanly.
- Long proofs, derivations, and auxiliary results go in the **Online Appendix (≤ 25 pp)**.
- Hypotheses should be few and load-bearing; a wall of H1–H12 wastes pages and dilutes the contribution.

## Anti-patterns

- A "theory" that is really a list of expected signs with no mechanism
- A formal model with no empirical or substantive payoff in a general-interest venue
- Hypotheses unconnected to the eventual test (see `jop-research-design`)
- Theory so elaborate it cannot be developed and tested within the page budget


## Operating pass for Journal of Politics

Treat this skill as an executable review pass, not a prose hint. First lock the political mechanism, evidence design, and scope condition; then judge whether the current manuscript answers the venue's real reader: political-science reviewers who want theory, identification or formal logic, and generalizable political implications in balance.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against APSR for field-wide political science, AJPS for design-heavy empirical work, World Politics for comparative/international politics; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Mode】empirical / formal / normative
【Core argument】one sentence
【Mechanism / comparative statics】the engine of the claim
【Observable implications】the falsifiable predictions
【Innovation】what changes for the general reader
【Next】jop-research-design
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — formal-modeling and simulation tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP scope ("theoretically innovative," broad on method)
