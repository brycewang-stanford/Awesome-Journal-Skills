---
name: jf-workflow
description: Use when deciding which jf-* sub-skill to invoke next, or when sequencing manuscript work from topic selection through rebuttal for The Journal of Finance (JF). Routes — it does not replace — the specialized skills.
---

# Workflow Router (jf-workflow)

## When to trigger

- You are unsure which `jf-*` skill applies to the current task
- You want an end-to-end sequence for a JF manuscript
- You are mid-project and need the next step

## What this pack targets

The Journal of Finance: AFA flagship, founded **1946**, bimonthly, Wiley-Blackwell, finance **top-3** with JFE and RFS, **~5% acceptance / ~33–45% desk reject** (afajof.org editor reports, accessed 2026-05-30). Distinctive JF mechanics this pack encodes: the **AFA online portal with a tiered submission fee** (high-income AFA member $400 / non-member $525; low-income $0), the **60-page limit** (≥1.5 spacing, 12-pt), the **Internet Appendix bundled at the end of the same PDF**, the **Data and Code Sharing Policy** with a **Data Editor**, and a **cover letter that is normally omitted**.

## End-to-end sequence

1. **`jf-topic-selection`** — is this general-interest and flagship-level?
2. **`jf-literature-positioning`** — state the marginal contribution; attribute canon to the right top-3 journal.
3. Design: **`jf-empirical-design`** (asset pricing) or **`jf-identification`** (corporate/causal).
4. **`jf-robustness`** — decisive checks in body, exhaustive battery + multiple-testing discipline in the Internet Appendix.
5. **`jf-tables-figures`** — self-contained exhibits, JF numbering, economic units.
6. **`jf-internet-appendix`** — allocate body vs. IA; keep body ≤60 pages.
7. **`jf-writing-style`** — general-interest intro; magnitude up front.
8. **`jf-referee-strategy`** — pre-empt objections; cover letter only for COI/code-exemption.
9. **`jf-submission`** — preflight: fee tier, 60-page check, bundled IA, code, disclosure.
10. **`jf-rebuttal`** — after an R&R, answer the editor first.

## Routing table

| Symptom                                   | Go to                         |
|-------------------------------------------|-------------------------------|
| "Is this big enough for JF?"              | `jf-topic-selection`          |
| "What's new vs. prior work?"              | `jf-literature-positioning`   |
| "How do I test this anomaly/factor?"      | `jf-empirical-design`         |
| "Is my causal claim identified?"          | `jf-identification`           |
| "Which robustness / multiple testing?"    | `jf-robustness`               |
| "Exhibits look amateur"                   | `jf-tables-figures`           |
| "Body too long / what goes online?"       | `jf-internet-appendix`        |
| "Intro buries the finding"                | `jf-writing-style`            |
| "What will referees attack?"              | `jf-referee-strategy`         |
| "Final pre-submit check / the fee"        | `jf-submission`               |
| "Got an R&R"                              | `jf-rebuttal`                 |

## Stage-gate decision table

Use this to locate yourself in the AFA pipeline and to know what must be true before advancing. The flagship's selectivity means each gate is a real stop, not a formality:

| If you are here…                                  | The binding question                                   | Gate to clear before moving on            |
|---------------------------------------------------|--------------------------------------------------------|-------------------------------------------|
| Have a result, no paper                           | Would the whole AFA membership care?                   | General-interest fit (`jf-topic-selection`) |
| Writing the introduction                          | Is the marginal contribution one sentence?             | Crisp delta vs. closest work (`jf-literature-positioning`) |
| Asset-pricing test in hand                        | Does it survive the factor zoo and out-of-sample?      | Multiple-testing + OOS (`jf-empirical-design`) |
| Corporate causal claim                            | Is the source of variation named and exogenous?        | Credible identification (`jf-identification`) |
| Result is robust                                  | Are the 3–6 decisive checks in the body, rest online?  | Body/IA split (`jf-robustness`, `jf-internet-appendix`) |
| Polishing                                         | Question, answer, magnitude on page 3; ≤60 pp?         | Accessible exposition (`jf-writing-style`) |
| About to submit                                   | Fee tier, bundled IA, code, disclosure all set?        | Portal preflight (`jf-submission`)         |
| Holding an R&R                                    | Have you answered the editor first?                    | Editor-led rebuttal (`jf-rebuttal`)        |

## Worked vignette — routing a corporate natural-experiment paper

*Illustrative.* A team has a clean staggered-regulation shock and a DID showing leverage falls by, illustratively, 4 percentage points at treated firms. Where do they enter? Not at `jf-empirical-design` (that is the asset-pricing track) but at `jf-topic-selection` to confirm broad interest, then `jf-literature-positioning` to state the delta against the capital-structure canon, then straight to `jf-identification` because the staggered rollout demands a modern DID estimator and a pre-trends panel. `jf-robustness` then decides which placebo and excluded-cohort checks are load-bearing in the body versus the Internet Appendix. Only after `jf-writing-style` confirms the 4-point effect and its mechanism land on page 3 does `jf-submission` run the portal preflight. The router's job is to stop them skipping identification straight to submission — the most common JF self-inflicted desk reject.

## What this router will not do (calibration anchors)
- It will **not** adjudicate identification or factor-model choices — those belong to the specialized skills; the router only sequences them.
- It assumes the JF-specific mechanics stay constant across the project: the 60-page body limit, the bundled-in-PDF Internet Appendix, the AFA portal fee, and the Data Editor's code check. If any of these appear to have changed, confirm against the journal's current author guidelines before relying on the sequence.

## Anti-patterns

- Jumping to `jf-submission` before fit and identification are settled
- Skipping `jf-internet-appendix` and breaching the 60-page limit
- Treating any single sub-skill as a substitute for the specialized ones
- Entering the asset-pricing track for a corporate causal paper (or vice versa)

## Output format

```
【Current stage】...
【Recommended next skill】jf-...
【Why】...
```
