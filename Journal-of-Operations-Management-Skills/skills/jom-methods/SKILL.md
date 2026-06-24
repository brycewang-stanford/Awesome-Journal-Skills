---
name: jom-methods
description: Use when choosing and defending the research design for a Journal of Operations Management (JOM) empirical study — matching survey, archival/secondary, field, case, experimental, or intervention-based research to the operations question, anticipating the Empirical Research Methods Department's method check, and keeping the design observation-grounded rather than analytical.
---

# Research Design for Empirical OM (jom-methods)

## When to trigger

- You must pick a design that can actually test your operations hypotheses
- A reviewer questions whether the method fits the operations phenomenon or the level of analysis
- You are weighing a behavioral lab experiment vs. archival panel vs. survey vs. field/intervention
- You anticipate the **Empirical Research Methods Department** method check on incoming submissions

## JOM's empirical-only design space

JOM publishes empirical OM research and **does not** publish purely analytical models or optimization techniques. Every design must rest on **observation**. The native JOM design families are:

| Operations question / claim                                  | Design                                                        |
|--------------------------------------------------------------|---------------------------------------------------------------|
| Perceptions, practices, constructs across firms/plants       | **Survey** (validated multi-item scales; multi-respondent)    |
| Cause–effect on operational outcomes from secondary data     | **Archival/secondary** panel (recalls, inventory, supply ties)|
| Human operational decisions, biases, incentives              | **Behavioral-OM experiment** (lab/online, manipulation checks)|
| How operations work unfolds in context                       | **Field study / case study** (process, embedded, comparative) |
| Effect of an actively introduced change in a real setting    | **Intervention Based Research** (engaged scholarship)         |
| Pooling effects across studies                               | **Meta-analysis** of empirical OM findings                    |

## Match design to claim and level

State the **unit and level** (transaction, shift, line, plant, project, dyad, supply network) and ensure the design observes at that level. A plant-level claim tested with firm-level archival data is a level mismatch reviewers catch quickly. For multi-respondent supply-chain dyads, plan both-side data collection.

## Intervention Based Research (a JOM-distinctive genre)

JOM formally houses **Intervention Based Research**, where researchers actively intervene in a real operational problem (engaged scholarship). If you use it: pre-state the theorized effect, document the intervention protocol and timeline, separate researcher actions from observed effects, and address how engagement threatens (and how you protect) inference. Most flagship management journals do not formally house this genre — use it deliberately.

## Pre-empt the Empirical Research Methods check

JOM's Empirical Research Methods Department performs method checks on incoming empirical submissions. Defend, up front: sampling frame and response/coverage, construct operationalization, identification strategy (for causal claims), common-method separations (for survey), and reproducibility of secondary-data construction. Weak identification or unvalidated measures stall here.

## Execution bridge (StatsPAI / Stata MCP)

For the **empirical / causal lane**, estimate and audit rather than only specify. Full
map: [`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). JOM is empirical operations / supply-chain — survey and archival panel data; foreground endogeneity of operational choices and clustered / multilevel inference.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result` to
  enumerate the checks the design owes.
- **Panel / staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition`
  + `honest_did_from_result`. **IV:** `effective_f_test` + `anderson_rubin_ci`. **RDD:**
  `rdrobust` + `mccrary_test`.
- **Experiments:** randomization-based inference and `romano_wolf` for the many-outcome
  family-wise correction reviewers expect.

Match the toolchain to the **reviewer pool**, and report the effect size the venue
wants. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- An optimization or pure simulation model presented as the empirical contribution.
- Design that cannot observe at the claimed level.
- Single-respondent survey for a relational/dyadic operations claim.
- Intervention work that conflates the researcher's actions with the measured effect.

## Design-defense checklist the methods check applies

Each JOM design family carries its own non-negotiable evidence; the mapping below summarizes what the Empirical Research Methods check typically scrutinizes. Confirm exact expectations against current methods-department guidance.

| Design | Defense expected up front | Fatal omission |
|--------|---------------------------|----------------|
| Survey | Sampling frame, coverage, validated scales, CMB separations | Single-respondent data for a dyadic claim |
| Archival/secondary | Identification strategy, reproducible construction, clustering | Endogenous practice treated as exogenous |
| Behavioral-OM experiment | Manipulation/attention checks, random assignment, task realism | Confound between manipulation and a cue |
| Field / case study | Sampling logic, traceable data structure, audit trail | Anecdote substituted for within-case evidence |
| Intervention Based Research | Pre-stated effect, protocol/timeline, action–effect separation | Researcher actions conflated with the outcome |

## Desk-reject and return triggers on design

- An optimization or pure simulation model presented as the empirical contribution (redirected to analytical OM venues).
- A line-level claim tested only with firm-level archival data — a level mismatch.
- Survey design with no procedural remedies for common-method bias and no measurement validation plan.

## Worked vignette: archival vs. field for a quality-practice question

Does cross-training frontline operators reduce defects? Archival route: a plant panel with HR cross-training records and quality logs, identified via a phased rollout (illustrative). Field route: an intervention introducing cross-training in matched lines with pre/post measurement. The choice turns on the claim and the threat. If selection is the worry and a staggered rollout exists, the archival quasi-experiment identifies the effect at the line level with plant and time fixed effects. If the mechanism (how cross-training changes floor problem-solving) is the contribution, Intervention Based Research observes the process and pre-states the effect. Either is JOM-fit; an analytical model of optimal allocation is not.

## Design objections and the JOM-grounded response

- *"The method does not fit the operations phenomenon."* Re-state the unit and level, then show the design observes at exactly that level.
- *"This is analytical work, not empirical."* If the core contribution is a model, redirect to an analytical venue; if observed, foreground the observation.

## Output format

```
【Design family】survey / archival / experiment / field-case / IBR / meta-analysis
【Unit & level】...
【Identification / validity strategy】...
【Methods-check readiness】sampling, measures, identification, reproducibility ...
【Next step】jom-data-analysis
```
