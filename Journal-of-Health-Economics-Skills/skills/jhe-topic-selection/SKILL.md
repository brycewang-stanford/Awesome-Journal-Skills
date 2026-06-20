---
name: jhe-topic-selection
description: Use when deciding whether a question is a Journal of Health Economics (JHE) paper at all — is it a genuine health-economics contribution, not a public-finance or labor paper with health as a thin application. Frames the question and audience; it does not run the analysis or invent citations.
---

# Topic Selection (jhe-topic-selection)

## When to trigger

- A draft is being aimed at **JHE** and you are unsure it is a *health-economics* paper versus a public-finance/labor paper that happens to use health data
- A coauthor asks whether the question clears JHE's "value, production, or distribution of health or healthcare" bar
- The paper risks landing better at AJHE, Journal of Public Economics, Health Economics, or AEJ: Economic Policy
- The health-economics mechanism is not yet the center of gravity of the question

## The JHE fit test

JHE asks whether the paper advances understanding of the **value, production, or distribution of health or healthcare**, or directly informs **health policy** (检索于 2026-06；以官网为准). The decisive question is not "is there health data?" but "is the economic mechanism a *health-system* mechanism?" A paper where the health setting is interchangeable with any other market belongs elsewhere. Run the question through these health-econ cores and confirm at least one is the engine, not the backdrop:

| Health-econ core | What makes it a JHE question (not a sibling's) |
|------------------|------------------------------------------------|
| Insurance design & demand | moral hazard, adverse/advantageous selection, take-up, plan choice, cost-sharing response — the *insurance* mechanism drives the result |
| Provider incentives & payment | how DRG/P4P/capitation/ACO design changes provider behavior, intensity, coding, patient selection |
| Healthcare markets | hospital/insurer competition, consolidation, network design, market power in a regulated market |
| Health behaviors | smoking, obesity, alcohol, addiction — price/tax/information variation, internalities/externalities |
| Health & human capital | how health shocks/investments shape education, labor supply, earnings — health as the *production* input |
| Health policy & disparities | coverage expansions, mandates, access, equity across groups — the policy *is* a health-system policy |

If the mechanism is really taxation, redistribution, or labor supply with health as one outcome among many, the better home is JPubE or a labor outlet — say so early.

## Sibling boundary (where papers get misrouted)

- **vs. AJHE** — AJHE (ASHEcon, U. Chicago Press) leans US-health-policy and applied; JHE is the international Elsevier field flagship with stronger appetite for structural insurance/provider models. A US-Medicaid descriptive-policy paper may fit AJHE better; a model-disciplined selection paper fits JHE.
- **vs. Journal of Public Economics** — JPubE wants the public-finance mechanism (incidence, optimal policy, fiscal externality) front and center; JHE wants the health-system mechanism.
- **vs. Health Economics (Wiley)** — Health Economics is broader and more methods/measurement-tolerant; JHE prizes sharper causal identification and a tighter economic question.
- **vs. AEJ: Economic Policy** — AEJ:Pol is a policy generalist judged on top-5-adjacent breadth; JHE is judged by health economists on health-econ depth.

## Sharpening moves

1. State the question in one sentence naming the **health-system mechanism** and the **policy or welfare stake**.
2. Name the health economist who would referee it and the institutional fact they would test you on (e.g., does your "Medicaid effect" separate take-up from crowd-out?).
3. Identify the counterfactual policy or market a health-policy reader would care about.
4. Separate the health-econ contribution from the generic econometric contribution — JHE rewards the former.
5. Confirm a real policy or market exists that your counterfactual speaks to — JHE wants the lesson, not just the estimate.
6. Hand off to `jhe-literature-positioning` if the fit passes, or back to `jhe-workflow` to reconsider venue.

## Worked vignette (illustrative)

A draft studies how a state income-tax change affects household health-insurance purchases. The author aims at JHE. The fit test exposes the problem: the engine is a *tax* mechanism (incidence, behavioral response to a marginal rate), with insurance as the outcome — that is a Journal of Public Economics paper. The reframe that *earns* JHE: pivot the engine to the insurance-demand and selection margin — how the price change moves *who* buys coverage and the resulting selection in the risk pool — so the health-system mechanism (adverse selection, plan choice) becomes the contribution, not the tax. Same data, different engine, different journal. If the selection story is thin, the honest call is to send it to JPubE rather than dress it up.

## Quick triage when venue is genuinely ambiguous

- If the **policy lever** is fiscal (tax, transfer, subsidy) and health is one outcome → likely **JPubE**.
- If the contribution is **US health-policy description/evaluation** with light modeling → consider **AJHE**.
- If the contribution is **methods/measurement** or broader and more applied → consider **Health Economics (Wiley)**.
- If the engine is a **health-system mechanism** (insurance/provider/market/behavior/human-capital) with credible identification → **JHE**.

## Checklist

- [ ] One health-econ core is the engine of the question, not the backdrop
- [ ] The question would be weaker (not just relocated) if you stripped the health setting out
- [ ] The institutional setting (program rules, payment system, market structure) is named, not generic
- [ ] The boundary vs. AJHE / JPubE / Health Economics / AEJ:Pol is explicit
- [ ] The policy or welfare stake is stated, not implied
- [ ] Process facts cited are in `resources/official-source-map.md` or marked 待核实

## Anti-patterns

- Choosing the venue for prestige before checking which audience the mechanism actually serves
- A labor/public-finance paper with health as one of several outcomes, dressed as health economics
- "We use health data" treated as fit, with no health-system mechanism
- Picking JHE for prestige when AJHE or Health Economics is the natural audience
- Naming a program (Medicaid, Part D) but ignoring the institutional detail referees will test
- Inventing exemplar JHE papers or editor names instead of marking 待核实

## Output format

```text
【Journal】Journal of Health Economics
【Skill】jhe-topic-selection
【Verdict】fit / reframe / reroute-to-sibling
【Health-econ core】insurance / provider / markets / behavior / human-capital / policy-disparities
【Mechanism sentence】one line naming the health-system mechanism + stake
【Sibling boundary】why not AJHE / JPubE / Health Economics / AEJ:Pol
【Source status】verified URL / 待核实 / not asserted
【Next skill】jhe-literature-positioning
```

## Handoff boundary

This skill decides whether the question belongs at JHE and frames the health-system mechanism; it does not stake the marginal contribution against the literature (`jhe-literature-positioning`) or test the design (`jhe-identification`). If the fit is genuine, hand off to `jhe-literature-positioning`. If the honest verdict is "reroute," say which sibling journal fits and why, rather than forcing a frame the JHE audience will reject — a clean reroute saves a year over a desk reject.
