---
name: jmis-theory-development
description: Use when building the theoretical engine of a Journal of Management Information Systems (JMIS) manuscript — an IT-business-value logic, a platform/network-effects mechanism, an economic model of IS, or a technology-specific behavioral theory. Adapts the form of "theory" to JMIS's management-and-economics-of-IS identity; it does not run the analysis (jmis-data-analysis) or frame the contribution (jmis-contribution-framing).
---

# Theory Development (jmis-theory-development)

## When to trigger

- Your claims are descriptive ("IT spend correlates with performance") with no economic or behavioral mechanism
- You built an artifact or ran a regression but cannot say what *IS knowledge* it advances
- A reviewer says "the theoretical contribution is unclear" or "this is a technical/empirical exercise"
- You need hypotheses, propositions, or signed predictions derived *before* you look at results

## Theory takes a different shape in each JMIS style

JMIS spans empirical, economic-analytical, and design-oriented IS work, so "develop theory" means different things. Pick the row that matches your study; JMIS's distinctive pull is toward the **economics and management of IS**, so even behavioral papers benefit from naming the value or incentive at stake.

| Style | What "theory" means here | What you must produce |
|-------|--------------------------|------------------------|
| **IT business value** | A mechanism by which a specific IT capability creates, captures, or destroys value | Causal logic from IT capability → intermediate process → firm/market outcome, with complementarities and contingencies named |
| **Platform / e-commerce** | Network effects, two-sidedness, matching, governance, or pricing logic | A model or argument yielding directional predictions about adoption, cross-side effects, competition, or platform revenue |
| **Economics of IS** | An economic mechanism (incentives, information asymmetry, signaling, security/privacy economics) | Comparative-static, signed, falsifiable predictions and the assumptions they rest on |
| **Behavioral IS** | A technology-specific cognitive/behavioral mechanism (not generic TAM) | A priori hypotheses with the IT artifact in the causal path, boundary conditions, and mediation/moderation logic |

## IT business value: make the mechanism, not the correlation, the theory

A JMIS IT-value paper is not "more IT, more performance." State *which* IT capability, acting through *what* organizational process, under *which* complementary conditions (process redesign, human capital, governance), produces *which* outcome. Theorize the **complementarities and contingencies** — JMIS reviewers reward a contingent value mechanism over a universal "IT pays" claim, because the field already knows the productivity-paradox debate.

## Platform and economics-of-IS: derive signed predictions a priori

State the economic force in words before any math: *who has what incentive, what information, and how does the IT-mediated market structure change behavior?* Then write comparative-static predictions (e.g., "stronger same-side network effects raise the platform's optimal openness"). For an analytical model, the contribution is the **insight the model yields**, not the model's existence. Avoid HARKing — predictions precede estimation.

## Behavioral IS: keep the artifact load-bearing

If your hypotheses would survive deleting the technology, they are not IS theory. Anchor the mechanism in a feature of the system (recommendation transparency, gamification, anonymity, automation) and theorize *why that feature* shifts cognition or behavior, and where the effect reverses. Generic TAM/UTAUT re-tests are a desk-reject risk; extend or challenge a mechanism instead.

## Make boundary conditions and level of analysis explicit

IS effects are contingent on the artifact, the user, the firm, the market, and the period. Name the level (individual, firm, platform, market) and the scope where the theory holds and breaks — an honest scope condition beats an over-claimed law.

## Worked vignette: from "AI improves productivity" to a JMIS mechanism (illustrative)

A draft claims "generative-AI tools raise analyst productivity." As stated it is a correlation with no IS theory. The JMIS mechanism names *which* capability of the tool (it lowers the cost of drafting but not of verification), acting through *what* organizational process (task reallocation toward judgment-heavy work), under *which* complementarity (it pays only where the firm redesigns review workflows and has the human capital to vet output), producing *which* contingent outcome (productivity rises for routine tasks, is flat or negative for novel ones where verification cost dominates). That contingent, complementarity-laden statement is theory; "AI helps" is not. The hypotheses then follow a priori, including where the effect reverses.

## Referee pushback mapped to a theory fix

- *"This is descriptive — where is the mechanism?"* → State the IT-enabled force, the channel, the population, and the reversal condition before any estimation.
- *"This is just TAM/UTAUT again."* → Anchor the mechanism in a specific system feature and theorize why *that feature* shifts behavior; extend or contest a mechanism rather than re-confirm acceptance.
- *"Your model has no insight beyond its setup."* → Present the comparative static that surprises — the result the model yields that intuition would not predict.

## Checklist

- [ ] The correct *form* of theory is used (value mechanism / platform model / economic model / behavioral mechanism)
- [ ] The IT artifact or capability is load-bearing, not decorative
- [ ] Hypotheses / propositions / signed predictions are derived *before* results (no HARKing)
- [ ] IT-value papers theorize complementarities and contingencies, not a universal effect
- [ ] Economic/platform papers state assumptions and yield falsifiable comparative statics
- [ ] Level of analysis and boundary conditions are explicit
- [ ] Any borrowed reference-discipline theory has a named, IS-forced extension
- [ ] The theory implies a concrete decision a manager, firm, or platform could make differently

## Tie the theory to a managerial decision

JMIS theory earns its place when it implies a decision a manager, firm, or platform could make differently. After stating the mechanism and predictions, ask: *whose choice does this theory inform, and how?* A platform-openness model should tell a platform operator when to open vs. close an API; an IT-value mechanism should tell a CIO which complementary investments make a system pay; a privacy-economics model should tell a firm when disclosure deters vs. invites harm. Theory with no decision attached can still be correct, but at JMIS it reads as under-motivated — the journal's center of gravity is the *management* of IS, so the managerial hook belongs in the theory, not only in a closing implications paragraph.

## Anti-patterns

- "More IT → more performance" with no process, complementarity, or contingency
- A generic TAM/UTAUT replication offered as the theoretical contribution
- An analytical model whose contribution is "we model X" rather than an insight
- "We applied [reference-discipline theory] to [IS setting]" with no new IS mechanism
- Hypotheses that merely restate correlations the data already revealed
- Importing a reference-discipline theory with no IS-forced extension (application, not contribution)
- Theory with no managerial decision attached — correct but under-motivated for JMIS
- Boundary conditions left implicit, so the claim reads as an over-generalized universal law

## Borrow reference-discipline theory, but earn an IS extension

Much JMIS theory imports machinery from economics, psychology, or operations — that is expected and fine. What is not fine is stopping at the import. "We apply [transaction-cost economics / regulatory focus / queueing theory] to [an IS setting]" is an application, not a contribution; the IS field already knows the borrowed theory. The contribution comes from the **extension the IS context forces**: a digital artifact that changes the cost structure the borrowed theory assumed, a platform feature that creates a moderator the parent theory never anticipated, an automation that breaks a behavioral mechanism's boundary. Name explicitly what the IS context adds to or revises in the parent theory, and that addition — not the import — is your theoretical contribution.

## Output format

```text
【Style & theory form】IT-value / platform / economics-of-IS / behavioral
【Core mechanism】IT capability or feature → channel → on whom → outcome
【Claims】H1..Hn / propositions P1..Pn / signed comparative statics
【Complementarities / boundary conditions】where it holds / reverses
【Level of analysis】individual / firm / platform / market
【Next step】jmis-literature-positioning
```
