---
name: jle-topic-selection
description: Use when deciding whether a law-and-economics project belongs at The Journal of Law and Economics (JLE) rather than the Journal of Legal Studies, JLEO, or the American Law and Economics Review, and what its central legal/regulatory question should be. Sets venue fit and question scope; it does not design the identification (see jle-identification).
---

# Topic Selection & Venue Fit (jle-topic-selection)

## When to trigger

- A project analyzes a law, a regulation, a court, or a legal institution economically, but you are unsure it is "JLE-shaped"
- The question reads like doctrinal legal scholarship, an organizational-governance study, or a generic applied-micro paper — and you need to place it
- The same dataset (court records, enforcement actions, statute panels) supports several framings and you must pick the one that lands here
- A co-author asks "why JLE and not the Journal of Legal Studies or JLEO?"

## The JLE fit test

JLE wants **economic analysis of law, regulation, and legal institutions** where a **real legal/regulatory question** is answered with a **credible empirical design or a disciplined theoretical model**, in the Chicago price-theory-plus-institutions tradition. The legal rule or institution must be load-bearing — not background color for a generic economics paper, and not a doctrinal argument dressed in regression.

| Signal in your project | Likely fit |
|------------------------|-----------|
| A legal rule / regulation / enforcement regime changes behavior, and you identify the effect credibly | **JLE** (core) |
| The contribution is primarily doctrinal or normative-legal, lightly empirical | lean **Journal of Legal Studies** (also UChicago, more legal/doctrinal) |
| The question is about organizations, governance, or positive political economy / institutions-as-equilibria | lean **JLEO** |
| Solid law-and-econ but incremental, field-internal, or a shorter contribution | **American Law and Economics Review** |
| The legal angle is incidental; it is really labor/public/IO with a law label | a **field journal** or AEJ, not JLE |
| Pure mechanism-design / contract theory with no legal institution | a **theory journal**, not JLE |

JLE is **question-first and institution-respecting**: an empirical paper needs the rule's mechanics right (who is bound, when it binds, what the counterfactual rule is); a theory paper needs comparative statics about a legal rule that someone could in principle test or recognize in the world.

## Sharpening the question (do this before writing anything)

1. **One-sentence legal/economic question** with the rule and the object named: "What is the effect of legal rule R on outcome Y for agents A, identified by [the change/threshold/assignment]?"
2. **Why a law-and-economics audience cares** — name the regulatory or doctrinal debate the answer informs (e.g., damages caps and litigation, merger policy and prices, sentencing and deterrence).
3. **The institutional detail that makes it real** — when does the rule bind, who is exempt, what is the counterfactual legal regime; if you cannot state this, the topic is not yet JLE-shaped.
4. **The credible-design or model seed** — a law change, a threshold, a court/case assignment, an enforcement event, or a model whose comparative statics are testable; if none, route to `jle-identification` or `jle-theory-model`.

## Checklist

- [ ] One-sentence question naming the legal rule/institution and the economic outcome
- [ ] Venue placed against the table; the reason it is JLE and not JLS / JLEO / ALER written in one line
- [ ] The legal-institutional mechanics stated (who is bound, when it binds, the counterfactual rule)
- [ ] The regulatory or doctrinal debate the answer speaks to, named
- [ ] A candidate design (law change / threshold / assignment / enforcement event) or a testable model
- [ ] No causal overclaim from a design that cannot support it, and no doctrinal argument standing in for evidence

## Anti-patterns

- A generic applied-micro paper with a thin legal label sent to JLE for "fit" — desk-reject risk
- Doctrinal/normative legal argument with token regressions (belongs at JLS, or is not yet a JLE paper)
- An organizations / positive-political-economy study that is really JLEO-shaped
- "Interesting court dataset, no question" — data availability is not a contribution
- Getting the institution wrong (treating a non-binding rule as binding, ignoring exemptions or enforcement gaps)

## Worked vignette (illustrative)

A researcher has scraped two decades of state appellate decisions and wants to "study judges and the economy." That is a dataset, not a question. Working through the fit test: the cleanest variation is the staggered random assignment of cases to judges with measurably different priors — a court-assignment design. The question becomes "what is the effect of being assigned a pro-defendant judge on firm investment after a contract dispute, identified by random case assignment?" The doctrinal debate is whether judicial discretion creates legal uncertainty that chills investment; the institution is real (assignment rules, recusal, appeal). Now it is JLE-shaped — and clearly not a doctrinal JLS note or a JLEO governance study.

## The field areas JLE is built for

A project lands more naturally if it sits in one of JLE's historical strengths. Use this to confirm the question is recognizably law-and-economics:

- **Antitrust & competition** — merger effects, collusion, market definition, the economics of enforcement and consent decrees
- **Regulation & its incidence** — who bears the cost of a rule, capture, the Stigler/Peltzman theory of regulation, deregulation episodes
- **Crime & deterrence** — the Becker margin (probability × severity), sentencing, enforcement intensity, recidivism
- **Property & contract** — entitlements and bargaining (Coase), contract enforcement, property-rights regimes
- **Corporate & securities law** — disclosure rules, governance mandates, securities enforcement, litigation
- **Litigation & courts** — selection of disputes (Priest–Klein), fee rules, damages caps, judicial behavior
- **Intellectual property** — patent/copyright scope, infringement, innovation incentives
- **Political economy of law** — lawmaking, lobbying, the supply of legal rules

If the question does not sit in or adjacent to one of these, re-examine whether the legal institution is really load-bearing.

## Sibling-placement quick test

- Is the deliverable an *economic effect of a legal rule*, credibly identified? → **JLE**
- Is it primarily a doctrinal or normative-legal argument? → **Journal of Legal Studies**
- Is it about organizations, governance, or institutions-as-equilibria? → **JLEO**
- Is it solid but incremental law-and-econ? → **American Law and Economics Review**
- Would a non-law economist cite it without caring about the rule? → a **field journal**, not JLE

## Output format

```
【Question】one sentence, legal rule + economic outcome + agents named
【Venue verdict】JLE because [not JLS: ___] [not JLEO: ___] [not ALER: ___]
【Institutional mechanics】who is bound / when it binds / counterfactual rule: ___
【Debate it informs】regulatory or doctrinal question: ___
【Design or model seed】law change / threshold / assignment / enforcement event / testable model
【Next step】jle-literature-positioning
```
