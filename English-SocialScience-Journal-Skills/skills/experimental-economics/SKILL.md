---
name: experimental-economics
description: Use when targeting Experimental Economics or deciding whether a lab- or field-experiment manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Experimental Economics (experimental-economics)

## Journal positioning

Experimental Economics is the journal of the Economic Science Association (the ESA), the leading specialist outlet for experimental methods in economics. It rewards papers in which a carefully designed experiment — lab or field — answers a question about behavior, institutions, or theory that observational data cannot cleanly identify. The readership is experimental and behavioral economists who scrutinize design, incentive-compatibility, and replicability, so the experiment itself is the core of the contribution.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the ESA / Springer site and the editorial submission system.

## When to trigger

- The author names Experimental Economics (or the ESA outlet) as the target venue.
- A paper's central evidence is an experiment and the design is the contribution.
- A behavioral or theory-testing paper needs re-framing so the experimental design and incentives are foregrounded.
- The author needs this venue's desk-reject risks and a credible experimental / behavioral alternative list.

## Scope & topic fit

- Laboratory experiments testing theory, preferences, learning, or institutional rules.
- Field and lab-in-the-field experiments on economic behavior and institutions.
- Behavioral economics: social preferences, risk/time, bounded rationality, with experimental identification.
- Mechanism/market-design and game-theoretic predictions tested experimentally; methodological and replication contributions.

## Method & evidence bar

- Experimental design is the filter: clear hypotheses, appropriate treatments and controls, randomization, and adequate power.
- Incentive-compatibility and salient monetary incentives are expected; the procedure must rule out confounds and demand effects.
- Pre-registration and pre-analysis plans are increasingly the norm; replication and direct/conceptual replication studies are valued.
- Analysis must use appropriate inference (e.g., correct treatment of clustering at the session/group level) and report effect sizes, not only significance.

## Structure & house style

- The introduction states the research question, the theoretical prediction or hypothesis, the design, and the headline result early, and says why an experiment is the right tool.
- Document the design fully: instructions, treatments, sample, incentives, and procedures should be transparent and reproducible (often via an appendix with full instructions).
- Uses an unstructured abstract, JEL codes, and frequently an explicit statement of pre-registration status.
- Exhibits report treatment effects with effect sizes and uncertainty; the central comparison should be readable from one figure or table.

## Official-submission checklist

- Search the live site for "Experimental Economics submission guidelines / instructions for authors" and follow the current ESA/Springer version.
- Re-check formatting, abstract/JEL requirements, anonymization, and the requirement to include experimental instructions and procedures.
- Re-check the current data and code / replication-material deposit policy, pre-registration disclosure, and ethics/IRB requirements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why an experiment (not observational data) is necessary to answer this question.
- [ ] The contribution is stated as a designed treatment effect / mechanism test, not as statistical significance.
- [ ] The design (treatments, incentives, power, randomization) is fully documented and reproducible.
- [ ] Pre-registration status and IRB/ethics are disclosed; inference handles session/group clustering.
- [ ] Full instructions, data, and code are ready for the official deposit.

## Common desk-reject triggers

- An experiment with no clear hypothesis, weak incentives, or hypothetical (non-incentivized) choices presented as the main evidence.
- Underpowered designs or inference that ignores session/group-level dependence.
- Demand effects or confounds left uncontrolled by the design.
- "First to run this experiment" with no theoretical or methodological advance.

## Re-routing decision

- General-interest at the top with an experimental result → `american-economic-review`; broad general field → `european-economic-review`.
- Game-theory / mechanism-design predictions with theory as the core → `games-and-economic-behavior`; pure theory → `journal-of-economic-theory`.
- Field-experiment policy evaluation on labor/education/health → `journal-of-human-resources` or `journal-of-health-economics`; econometrics of experiments → `journal-of-applied-econometrics` or `international-economic-review`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Experimental Economics
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the experimental design clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / instructions / pre-registration / IRB / data-code>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
