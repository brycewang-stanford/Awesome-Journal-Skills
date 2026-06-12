---
name: jama-study-design
description: Use when locking the study design and internal-validity safeguards for a JAMA clinical manuscript (RCT, cohort, diagnostic, or systematic review). Strengthens design choices; it does NOT pick the reporting checklist or run the statistics.
---

# Study Design & Internal Validity (jama-study-design)

## When to trigger

- Choosing or defending the design: RCT vs cohort vs case-control vs diagnostic
- A reviewer will ask whether the analysis is intention-to-treat or per-protocol
- Bias, confounding, or missing data threaten the primary inference
- The design and the reporting checklist need to be aligned before writing

## Design-specific safeguards JAMA reviewers expect

### Randomized clinical trials
- A single, **pre-specified primary outcome**; secondary outcomes clearly labeled
- Adequate randomization (sequence generation) and **allocation concealment**
- Blinding of participants, clinicians, outcome assessors where feasible — state what was blinded
- **Intention-to-treat** as the primary analysis; per-protocol only as secondary/sensitivity
- A priori **sample-size / power** calculation tied to the primary outcome
- Pre-defined stopping rules and handling of interim analyses

### Cohort / case-control (observational)
- Explicit **confounding** control: prespecified covariates, adjustment strategy, DAG reasoning
- Clear definitions of exposure, outcome, and follow-up windows; avoid immortal-time bias
- Selection-bias and information-bias appraisal; how participants entered the sample
- **Association, not causation** — design and language must respect this

### Diagnostic-accuracy studies
- Pre-specified reference standard, applied to all participants, blinded to index test
- Consecutive or random enrollment; report spectrum of disease
- Pre-defined thresholds; report sensitivity/specificity/predictive values with CIs

### Systematic reviews / meta-analyses
- Pre-registered protocol (e.g., PROSPERO), pre-specified eligibility and outcomes
- Comprehensive, reproducible search; duplicate screening and extraction
- Risk-of-bias assessment; pre-planned heterogeneity and sensitivity analyses

## Decision table

| Question                                                  | Design / action                         |
|-----------------------------------------------------------|-----------------------------------------|
| Does an intervention cause an outcome?                    | RCT; if infeasible, strong quasi-design |
| What is the prognosis / risk of an exposure?              | Prospective cohort with confounder plan |
| How accurate is a test?                                   | Diagnostic-accuracy study (vs reference)|
| What does the totality of evidence show?                  | Systematic review ± meta-analysis       |
| Rare outcome, exposure already occurred                   | Case-control (watch selection bias)     |

## Checklist

- [ ] Primary outcome is single, pre-specified, patient-relevant
- [ ] For RCTs: randomization, allocation concealment, blinding stated; ITT is primary
- [ ] Sample-size / power calculation present and tied to the primary outcome
- [ ] Confounding/bias strategy explicit and pre-specified (observational)
- [ ] Reference standard and blinding defined (diagnostic)
- [ ] Protocol pre-registered (RCT and systematic review)
- [ ] Missing-data handling pre-specified (not improvised post hoc)
- [ ] Design choice matches the EQUATOR checklist you will use

## Anti-patterns

- Promoting a secondary or post hoc outcome to "primary" after seeing results
- Per-protocol analysis presented as primary for an RCT
- "Adjusted for everything" with no pre-specified covariate rationale
- Causal claims from an observational design
- Reference standard chosen or applied after knowing the index-test result
- No power calculation, then attributing a null result to "trends"


## Worked example: locking the design (illustrative)

Vignette (illustrative): a multicenter randomized clinical trial, N = 3,400 adults with acute kidney injury across 18 sites, early vs standard renal-replacement timing; pre-specified primary outcome 28-day all-cause mortality, 28.5% vs 31.2%, absolute risk difference -2.7 percentage points (95% CI, -6.1 to 0.7). For a Journal of the American Medical Association Original Investigation, the design safeguards a JAMA reviewer checks: a single pre-specified primary outcome, documented allocation concealment, intention-to-treat as primary (per-protocol only as sensitivity), and an a priori power calculation tied to mortality. The 95% CI crossing zero means the trial does not establish benefit — the Conclusions must say "no significant difference," not "a trend toward benefit."

## Reviewer pushback and the JAMA fix

- "Is this intention-to-treat or per-protocol?" Fix: make ITT the primary analysis and relegate per-protocol to clearly labeled sensitivity.
- "Primary outcome looks chosen after seeing the data." Fix: cite the registry/protocol; demote any post hoc outcome to exploratory.
- "Causal language from an observational design." Fix: switch to associational verbs and frame confounding as a residual threat.

Calibration anchors (hedge where uncertain): a single pre-specified primary outcome, allocation concealment, ITT-as-primary, and an a priori power calculation are durable JAMA expectations; the matching EQUATOR checklist (CONSORT/STROBE/STARD/PRISMA) follows from the design — confirm specifics against current author guidelines.

## Operating pass for JAMA

Run this as a concrete capability pass. First lock the clinical question, patient population, estimand or endpoint, safety/ethics issue, and reporting checklist; then test whether the manuscript addresses clinical reviewers who ask whether the evidence changes patient care, policy, or medical decision-making while satisfying reporting standards.

- **Primary move:** Return a claim-evidence-risk ledger; every recommendation must point to a manuscript location or missing artifact.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against NEJM for field-changing clinical medicine, Lancet for global-health breadth, specialty journals for narrower clinical domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Design】RCT / cohort / case-control / diagnostic / systematic review
【Primary outcome】... (pre-specified: yes/no)
【Key validity safeguards in place】...
【Validity gaps to fix】...
【Causal vs associational claim】...
【Matching EQUATOR checklist】CONSORT / STROBE / STARD / PRISMA
【Next skill】jama-reporting-standards
```
