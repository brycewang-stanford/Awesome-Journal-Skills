---
name: jim-theory-development
description: Use when building or repairing the conceptual framework of a Journal of International Marketing (JIM) manuscript — theorizing why effects differ across countries, choosing cultural/institutional lenses, and drafting cross-national hypotheses. It builds the mechanism; jim-literature-positioning stakes the claim against prior work.
---

# Cross-National Theory Development (jim-theory-development)

## When to trigger

- Hypotheses exist but the "because" clause is missing for every country difference
- Culture is mentioned only in the discussion section, explaining results after the fact
- The framework is a domestic theory with country dummies bolted on
- Reviewers (or coauthors) ask "why would this differ across borders at all?"

## The bar: country differences must be predicted, not discovered

JIM reviewers read the front end asking one question: *did the authors theorize the cross-national variation before seeing it?* Culture invoked post hoc — "the effect was weaker in Japan, perhaps because of collectivism" — is the single most cited theory failure in JIM rejections. The fix is architectural, not cosmetic: pick the country-level construct first, derive directional predictions from it, and let the data confirm or refute.

## Choose the country-level lens deliberately

| Lens | Constructs | Use when |
|------|-----------|----------|
| Cultural values | Hofstede dimensions, GLOBE practices/values, Schwartz value types | consumer psychology mechanisms shift with shared values |
| Institutions | regulatory quality, contract enforcement, institutional voids, IP protection | firm strategies (channels, entry modes, signaling) depend on the rules of the game |
| Economic development | income, market maturity, retail infrastructure, digital penetration | the mechanism requires resources or infrastructure to operate |
| Distance | cultural, psychic, institutional, geographic (CAGE-style decomposition) | dyadic home–host questions: exporting, entry, partner selection |
| Global consumer culture | perceived brand globalness, GCC positioning, consumer ethnocentrism/animosity | the global-local identity tension is the mechanism itself |

Rules of engagement: (1) name the **specific dimension** doing the work — "culture" is not a variable; (2) justify the lens against alternatives — if individualism and income level make the same prediction, say why you credit one; (3) prefer **measured** country variables over country dummies whenever more than a handful of countries are available.

## Respect levels of analysis

Most JIM theory spans levels: mechanisms live in consumers or firms, moderators live in countries. Three discipline rules:

- **State each construct's level.** A hypothesis mixing a country-level cause with an individual-level outcome must say how the levels connect (a cross-level moderation, not a vague "context effect").
- **Avoid the ecological fallacy.** Country-mean Hofstede scores do not describe individuals; if the mechanism is individual-level cultural orientation, measure it at the individual level (e.g., independent vs. interdependent self-construal) and treat national scores as the macro moderator.
- **Avoid the reverse error too:** individual-level values aggregated up do not automatically constitute national culture.

## Hypothesis craft for cross-national claims

- Write the **baseline mechanism** first (H1: X → Y through M), then the **cross-national moderation** (H2: the X → Y effect strengthens where <country dimension> is higher, because <dimension> amplifies/suppresses M).
- Every moderation hypothesis carries its own "because" clause tied to the mechanism M — not to a country stereotype.
- If theory genuinely permits opposite signs across countries, hypothesize the **crossover** explicitly; it is a stronger, more falsifiable claim than "weaker/stronger."
- Cap the framework: one mechanism, one or two theorized country moderators. Six moderators signal fishing.
- Pre-commit the framework in a conceptual figure: boxes with levels labeled, the country-level moderator visibly at its own level.

## Conceptual papers and theory-building at JIM

JIM also publishes conceptual and framework papers, but the bar mirrors the empirical one: the framework must generate *new, testable* cross-national propositions and must engage marketing constructs — not re-summarize IB theory. A useful skeleton: identify a tension two literatures leave unresolved across borders; build the integrating construct; derive propositions that specify which countries (by dimension, not by name) sit where; close with the research agenda and the managerial decision map.

## Checklist

- [ ] Country-level lens named at the dimension level, chosen over stated alternatives
- [ ] Every cross-national hypothesis written *before* data analysis, with a mechanism-tied "because"
- [ ] Levels of analysis labeled for every construct; cross-level links explicit
- [ ] No ecological fallacy: individual-level mechanisms measured at the individual level
- [ ] Crossover predictions made where theory supports sign reversal
- [ ] Conceptual figure drawn with the country moderator at its own level
- [ ] Framework parsimonious: one mechanism, at most two theorized country moderators

## Anti-patterns

- Culture as a post-hoc rescue for unexpected results — the canonical JIM theory failure
- "Hofstede said so" hypotheses with no marketing mechanism in between
- Country dummies presented as theory ("effects differ across our six countries")
- National-score reasoning applied to individuals (ecological fallacy) or vice versa
- Borrowing a domestic framework wholesale and asserting it "should generalize"
- Ten moderators from three cultural frameworks stapled onto one model

## Output format

```text
【Mechanism】X → Y through M (level: consumer / firm / dyad)
【Country lens】dimension + framework (e.g., in-group collectivism, GLOBE) + why over rivals
【Cross-national hypotheses】H#: direction + because-clause tied to M
【Levels】each construct labeled; cross-level moderation stated
【Falsifiability】what pattern across countries would disconfirm
【Next skill】jim-literature-positioning
```
