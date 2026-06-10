---
name: pom-topic-selection
description: Use when deciding whether an operations-management project fits Production and Operations Management (POM), which POM Department to route it to, or whether to target M&SOM, Management Science, JOM, or another venue. Sets the question and venue; it does not build the model (pom-theory-development).
---

# Topic Selection & Department Fit (pom-topic-selection)

## When to trigger

- The venue is still movable and you want to know if the paper is POM-shaped
- You have an OM result but are unsure which Department Editor should receive it
- You are choosing between POM and M&SOM / Management Science / JOM / a methods journal

## The POM fit test

POM is the flagship of the Production and Operations Management Society (POMS), published by SAGE, covering the **full breadth of operations management**: production, service, supply chain, healthcare, retail, sustainability, platforms, and the interfaces with finance, marketing, accounting, and information systems. Two questions gate fit:

1. **Is there a real operations decision?** Name who decides what, under which constraints (capacity, inventory, lead time, contracts, staffing, sourcing). A pure OR technique with no OM decision context is off-fit.
2. **Does it pass the practice-relevance gate?** POM weights *significant interest to practicing operations managers* alongside rigor. An elegant model with no managerial takeaway, or a domain application with no generalizable OM insight, fails.

## Pick the target Department before anything else

POM's defining structural norm: you submit to **one named Department**, and the cover letter must target it. Choosing the department shapes the framing, the reviewers, and the relevant literature. Common departments include Behavioral Operations, Supply Chain Management, Healthcare Operations, Sustainable Operations, Operations Management Data Analytics, and Manufacturing Operations, plus interface departments (POM-Finance, POM-Marketing, POM-Information Systems). The exact roster rotates — verify the live list (待核实).

## Strong vs. weak POM signals

- **Strong:** a clear operations decision; insight intelligible to a broad OM audience; a defensible department; rigor *and* a managerial/policy lever.
- **Weak:** pure method with thin OM context; pure management theory with no operational mechanism; an empirical result with no credible identification or operational interpretation; a same-data sequel that does not clearly differ from prior work (which also triggers the cover-letter disclosure requirement).

## One-shot caution

Because POM bars resubmission of a rejected paper to the same *or a different* department unless explicitly invited, choosing the right department and confirming fit **before** submitting matters more here than at most journals.

## Checklist

- [ ] Operations decision and decision maker named
- [ ] Passes the practice-relevance gate (managerial "so what")
- [ ] Target Department chosen and defensible
- [ ] Method tradition (analytical/empirical/behavioral/data-science) identified
- [ ] Same-data/related prior work noted for later disclosure


## Fit pass for Production and Operations Management

Use this as a second-pass capability check. First lock the operational decision, the performance metric, and the implementable lever; then test whether the manuscript addresses POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Primary move:** Score fit, novelty, evidence readiness, and audience ownership; reject prestige-only targeting when a sibling venue owns the contribution.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【POM fit】strong / plausible / weak / no
【Department route】best POM department + one-line rationale
【Operations decision】who decides what under which constraints
【Method track】analytical / empirical / behavioral / data-science
【Alternative venue】POM / M&SOM / Management Science / JOM / methods journal
【Next step】pom-theory-development
```
