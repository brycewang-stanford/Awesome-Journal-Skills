---
name: jfe-topic-selection
description: Use when scoping or framing a topic for a Journal of Financial Economics (JFE) manuscript and you need to test fit and contribution before investing in data work. Pressure-tests the question and contribution; it does not write the literature review or design the empirics.
---

# Topic Selection & Fit (jfe-topic-selection)

## When to trigger

- You have data or a setting but no sharp economic question yet
- You are unsure whether the idea clears the JFE contribution bar
- You cannot state in one sentence what is new relative to existing finance papers
- You are choosing between JFE, JF, and RFS as the target outlet

## What JFE rewards

JFE (Elsevier; one of the top-3 finance journals) publishes rigorous, methodologically demanding **empirical** corporate finance and asset pricing, plus the financial-economics theory that supports them. The durable preference: a clean economic question, answered with a credible design and exhaustive evidence. Verify current scope, section editors, and any registered-report option on the journal's official page.

Fit test — answer all four before proceeding:

1. **Economic question.** Is there a real financial-economics question, not just a correlation you can run? "Does X cause Y, and through what channel?" beats "X is associated with Y."
2. **Contribution.** Can you name the specific result that is new — a new fact, a new mechanism, a new identification, or overturning a believed result? Incremental "X in a new sample" rarely clears the bar.
3. **Credible answer.** Is there a plausible path to identification or to disciplined inference (see `jfe-identification`, `jfe-empirical-design`)? If the honest answer is "OLS with controls," the topic is not ready.
4. **Depth.** Can the result survive the robustness and referee culture JFE is known for? If one alternative explanation sinks it, reconsider.

## Contribution framing (draft early, refine often)

State the contribution as 2–4 explicit sentences for the introduction:

- **The gap:** what the literature currently believes or has not established.
- **The move:** the setting, design, or data that lets you resolve it credibly.
- **The finding:** the headline result, with direction and rough magnitude.
- **Why it matters:** for theory, for other empirical work, or for policy/practice.

## Corporate finance vs. asset pricing framing

- **Corporate finance:** lead with the causal question and the identifying variation (a shock, a discontinuity, an instrument). The contribution is usually "credible causal effect of X on corporate outcome Y, plus mechanism."
- **Asset pricing:** lead with the economic source of the return pattern and how you discipline inference. The contribution is usually "a return predictor/factor that is real after correct standard errors, out-of-sample, and multiple-testing scrutiny," or a mechanism for a known anomaly.

## Checklist

- [ ] One-sentence economic question written down
- [ ] Headline contribution stated in 2–4 sentences (gap / move / finding / why)
- [ ] Named the closest 3–5 papers this would sit beside and how it differs
- [ ] Plausible identification or inference path exists (not "OLS + controls")
- [ ] The result would survive an exhaustive robustness battery
- [ ] Honest read on whether JFE, JF, or RFS is the best home

## Anti-patterns

- A "kitchen-sink regression" with no economic question behind it
- "First paper to study X in country/sample Z" with no methodological or conceptual advance
- A correlation dressed as a finding, with identification deferred to "future work"
- An asset-pricing predictor pitched without any awareness of multiple-testing concerns
- Picking JFE because it is prestigious rather than because the design depth fits

## Output format

```
【Question】one-sentence economic question
【Contribution】gap / move / finding / why-it-matters
【Field】corporate finance | asset pricing | financial-economics theory
【Closest papers】[...] and how this differs
【Identification path】sketch (or "not yet — see jfe-identification")
【Fit verdict】JFE | JF | RFS | not ready
【Next】jfe-literature-positioning
```
