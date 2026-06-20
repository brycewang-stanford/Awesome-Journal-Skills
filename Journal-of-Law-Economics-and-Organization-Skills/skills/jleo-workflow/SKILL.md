---
name: jleo-workflow
description: Use when deciding which jleo-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for a Journal of Law, Economics, and Organization (JLEO) submission. Routes — it does not replace — the specialized skills.
---

# JLEO Workflow Router (jleo-workflow)

## Overview

This is the router. It tells you **which jleo-* skill to use at the current stage** of a manuscript aimed at *The Journal of Law, Economics, and Organization* (JLEO) — the **Oxford University Press** journal founded in **1985 by Oliver E. Williamson and Jerry L. Mashaw** at Yale, and the flagship outlet of the law-economics-**organization** tradition: transaction-cost economics, the theory of the firm, contracts and governance, and **positive political economy** (courts, legislatures, bureaucracies, federalism as institutions in the North–Weingast–Williamson line). It publishes both **formal-theoretical** and **empirical** work, triannually; Andrea Prat is Editor-in-Chief (检索于 2026-06；以官网为准).

Default assumption: unless the user says otherwise, treat the target as JLEO. Operational tells that you are at JLEO and not a sibling: the paper's payoff is an **institutional or organizational** claim, not a price-theory or pure-doctrine one; the question is "how does this governance structure / institution / political mechanism work and why does it take the form it does," and the contribution speaks to the **new-institutional / PPE** community. Submission is via the **Editorial Express** portal (editorialexpress.com/jleo); OUP is the publisher; the journal is COPE-compliant. Re-verify volatile specifics (editor, fees, exact limits, blinding) on the official OUP pages.

## When to trigger

- The user asks "what should I do next?" on a JLEO-bound manuscript
- A draft needs its current bottleneck diagnosed against the law-economics-organization bar
- Work is ping-ponging between framing, theory/model, identification, exhibits, and the response letter
- A JLEO decision letter arrived and the user needs to switch into revision mode
- The team is unsure whether the paper belongs at JLEO versus JLE, JLS, ALER, QJPS, or Organization Science

## Routing table

| Current symptom | Next skill |
|-----------------|------------|
| Scope/fit uncertain; might be price-theory L&E or pure org-theory | `jleo-topic-selection` |
| Contribution vs. the institutional/PPE frontier is fuzzy or undersold | `jleo-literature-positioning` |
| Causal credibility (reform, court/committee assignment, institutional variation) is shaky | `jleo-identification` |
| The institutional/organizational model or mechanism is loose or decorative | `jleo-theory-model` |
| Results may be specification-, sample-, or inference-sensitive | `jleo-robustness` |
| Exhibits are dense or do not answer the institutional question | `jleo-tables-figures` |
| Prose buries the institutional logic; intro/abstract do not land | `jleo-writing-style` |
| Data, code, or institutional-source documentation needs packaging | `jleo-replication-package` |
| Likely referee objections should be anticipated before submitting | `jleo-referee-strategy` |
| Ready to submit via Editorial Express; need a preflight | `jleo-submission` |
| A decision letter or referee report needs a response plan | `jleo-rebuttal` |

## Default order

1. `jleo-topic-selection` — lock a law-economics-**organization** question, not a sibling's
2. `jleo-literature-positioning` — stake the contribution vs. the institutional/PPE frontier
3. `jleo-identification` — institutional/organizational causal design where the paper is empirical
4. `jleo-theory-model` — the transaction-cost / agency / political-agency model that gives the claim teeth
5. `jleo-robustness` — threat-organized checks, not a mechanical appendix
6. `jleo-tables-figures` — exhibits that show the institutional comparison cleanly
7. `jleo-writing-style` — make the institutional logic land (intro + abstract last)
8. `jleo-replication-package` — institutional/organizational/political data paths and code
9. `jleo-referee-strategy` — anticipate the institutional-economist referee
10. `jleo-submission` — Editorial Express preflight
11. `jleo-rebuttal` — after the decision letter

> `jleo-writing-style` is a late-stage polish; do not rewrite the intro before the model and identification settle. Theory and empirics co-evolve at JLEO — `jleo-theory-model` and `jleo-identification` often loop.

## Routing by paper archetype

JLEO accepts several shapes, and the binding constraint differs by shape. Read the archetype, then enter the chain at the right link.

| Archetype | Likely first bottleneck | Enter at |
|-----------|-------------------------|----------|
| positive political economy model (legislature/court/bureaucracy) | comparative statics + an empirical or institutional test | `jleo-theory-model` → `jleo-identification` |
| transaction-cost / make-or-buy / governance-choice empirics | selection into governance form; endogenous boundaries | `jleo-identification` |
| contracts & theory of the firm (formal) | a sharp, novel mechanism vs. the canon | `jleo-theory-model` |
| institutions & reform (causal) | reform/assignment as a credible design, not OLS+controls | `jleo-identification` |
| organizational governance / personnel inside firms | mechanism + measurement of the organizational object | `jleo-topic-selection` → `jleo-theory-model` |

## Sibling boundaries (why JLEO and not its neighbors)

- **vs. Journal of Law and Economics (JLE, Chicago):** JLE is price-theory law-and-economics — antitrust, regulation, crime, empirical effects of legal rules on markets. JLEO adds **organization**: governance structures, the firm, and the political institutions that make and enforce rules. If the payoff is a market effect of a rule, lean JLE; if it is *why the institution/organization takes this form*, lean JLEO.
- **vs. Journal of Legal Studies (JLS):** JLS is broader law-and-economics with more doctrinal/legal-theory range; JLEO is tighter on institutions, organization, and PPE.
- **vs. Quarterly Journal of Political Science (QJPS) / American Political Science Review:** those are political-science homes for PPE; JLEO welcomes PPE but frames it as institutional **economics** with formal or empirical economics standards.
- **vs. American Law and Economics Review (ALER):** ALER is the AALEA's broad L&E outlet; JLEO is more organization- and governance-centric.
- **vs. Organization Science:** Org Science is management/org-theory (behavioral, sociological); JLEO is economics of organization (transaction costs, agency, formal incentives).

## Anti-patterns

- Treating JLEO as interchangeable with JLE (price-theory) or Organization Science (org-theory)
- Submitting a pure reduced-form market study with no institutional/organizational object as the payoff
- Polishing prose before the model and identification are stable
- Letting an appendix carry the institutional claim the main text must establish
- Quoting volatile process facts (editor, fee, blinding) as permanent instead of marking 待核实

## Output format

```text
【Target】The Journal of Law, Economics, and Organization (JLEO)
【Archetype】PPE model / TCE governance empirics / contracts-theory / institutions-causal / org-governance
【Current bottleneck】fit / contribution / identification / model / robustness / exhibits / style / submission / revision
【Next skill】<one jleo-* skill>
【Reason】why this is the binding constraint for an institutional/organizational claim
【Source check】official facts verified or marked 待核实
```
