---
name: mksc-workflow
description: Use when deciding which mksc-* sub-skill to invoke next, or when sequencing a Marketing Science manuscript from modeling-driven topic selection through R&R rebuttal. Routes — it does not replace — the specialized skills.
---

# Marketing Science Workflow (mksc-workflow)

## Overview

This is the router. It does not replace any specialized skill; it tells you **which mksc-* skill to use right now** for your Marketing Science manuscript.

Default assumption: unless told otherwise, the target is **Marketing Science**, the flagship quantitative-marketing journal of the INFORMS Society for Marketing Science (ISMS), published by INFORMS. Its editorial statement says it "focuses primarily on articles that answer important research questions in marketing using mathematical modeling." The dominant genres are **structural econometric models** and **analytical (game-theoretic) models**; econometrics, ML, surveys, and experiments are welcome only when they develop, test, or rigorously apply a formal model. The non-negotiable bar is therefore: an important marketing question answered through a model, not a reduced-form correlation. Senior Editors and Associate Editors (not standing departmental Area Editors) route the paper; the editor and reviewers will press equally on "does the model identify the effect?" and "what do we learn about marketing?"

> Editor-in-Chief: Puneet Manchanda (Michigan Ross), term Jan 1 2025–Dec 31 2027 (renewable through 2030), succeeding Olivier Toubia. Verify the masthead at the editorial-board page; fees and limits change.

## Routing table

| Current symptom                                                  | Next skill                   |
|------------------------------------------------------------------|------------------------------|
| Question is vague; unsure it needs a formal model or fits MKSC   | `mksc-topic-selection`       |
| No model yet; mechanism/identification logic missing             | `mksc-theory-development`    |
| Front end ignores structural/analytical precedents               | `mksc-literature-positioning`|
| Unsure: structural vs. analytical vs. causal-ML; estimable?      | `mksc-methods`               |
| Have a model and data; estimation, fit, counterfactuals unsettled| `mksc-data-analysis`         |
| Results exist but "primary contribution dimension" is unclear    | `mksc-contribution-framing`  |
| Estimate/comparative-statics/counterfactual exhibits are weak    | `mksc-tables-figures`        |
| Notation-heavy, buries model intuition, off INFORMS style        | `mksc-writing-style`         |
| Ready to submit; need ScholarOne + blinding + replication package| `mksc-submission`            |
| Want to understand double-anonymous SE/AE review                 | `mksc-review-process`        |
| Received an R&R; need to plan and draft the response             | `mksc-rebuttal`              |

## Default order

1. `mksc-topic-selection` — lock a modeling-worthy marketing question
2. `mksc-theory-development` — build the analytical/structural model + identification
3. `mksc-literature-positioning` — engage the modeling conversation you join
4. `mksc-methods` — pick the genre and make the model estimable
5. `mksc-data-analysis` — estimate, assess fit, run counterfactuals, robustness
6. `mksc-contribution-framing` — name the primary contribution dimension
7. `mksc-tables-figures` — finalize estimate/counterfactual exhibits in INFORMS style
8. `mksc-writing-style` — front-load intuition; INFORMS author-year prose
9. `mksc-submission` — ScholarOne preflight + replication-ready package
10. `mksc-review-process` — set expectations for double-anonymous multi-round review
11. `mksc-rebuttal` — after an R&R, revise then draft the response

> Decide the **Frontiers** vs. regular-article track early: Frontiers is a strict 6,000-word total cap and rewards one dominant contribution dimension. It changes scope, not polish.

## Anti-patterns

- Jumping to `mksc-data-analysis` before a model exists — MKSC rejects model-free correlation.
- Polishing exhibits (`mksc-tables-figures`) before identification is settled.
- Treating a consumer-psychology experiment with no formal model as MKSC-ready — that is a JCR paper.

## Router pass for Marketing Science

Use this as a second-pass capability check. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then test whether the manuscript addresses quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Primary move:** Run fit gate, evidence gate, writing gate, source-map gate, and output contract; stop when a gate lacks evidence.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.
