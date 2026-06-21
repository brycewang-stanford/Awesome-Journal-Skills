---
name: joap-topic-selection
description: Use when deciding whether an I-O / applied-psychology project fits the Journal of Applied Psychology (JAP) and which article type to target. JAP wants a genuine theoretical contribution to work-and-organizational science backed by rigorous measurement, not a rigorous study with no theoretical advance. Frames the question and tests fit; it does not collect data.
---

# Topic Selection & Fit (joap-topic-selection)

JAP publishes original work that **advances theory about individual, team, and organizational
phenomena at work** — motivation, leadership, selection and assessment, teams, job attitudes and
well-being, justice, training, turnover. The cardinal fit test is **dual**: a real **theoretical
contribution** *and* the **measurement/design rigor** to support a causal or cumulative claim. Use this
skill to pressure-test fit before investing.

## When to trigger

- Choosing among possible projects or framings for JAP
- A reader said the work feels "atheoretical," "applied-but-not-novel," or "a better fit elsewhere"
- Deciding between a **Feature Article** and a **Research Report**
- Deciding whether the contribution is empirical, theory-development, or meta-analytic

## The fit test

A strong JAP paper usually clears all four:

1. **Theoretical contribution.** It changes how I-O scholars understand a work phenomenon — a new
   mechanism, boundary condition, integration, or construct — not just a new context for a known
   effect. State the theoretical advance in one sentence.
2. **Measurement & design rigor.** Constructs are validly measured; the design supports the inference
   (causation, mediation, multilevel structure). A cross-sectional single-source correlation rarely
   clears the bar (see `joap-study-design`).
3. **Applied + scientific relevance.** The phenomenon matters for work and organizations *and* for
   theory; JAP is applied science, not consulting.
4. **Cumulative footing.** It is preregisterable / replicable and its data, materials, and code can be
   shared under the journal's TOP-aligned policy (see `joap-open-science-and-transparency`).

## Article type

- **Feature Article** — a full, programmatic contribution; length commensurate with the contribution.
- **Research Report** — a focused, shorter empirical contribution (often a tight multi-study package);
  confirm the current page/length cap on the official page (待核实).
- **Theory-development / integrative review** — a conceptual advance or cumulative synthesis with no
  new primary data; `joap-theory-and-hypotheses` carries it.
- **Qualitative research** — an I-O contribution built on qualitative evidence with explicit
  trustworthiness criteria.
- **Meta-analysis** — a cumulative quantitative synthesis; transparency of coding and data is essential.

## Fit scoring — worked example (illustrative)

Score a candidate against the four gates before investing. A leadership project, two framings:

```
Candidate A (off-fit): one cross-sectional survey (N = 220), servant
            leadership ↔ performance, all self-report, no theory advance.
  Theory ✗ (known correlation, new sample)   Rigor ✗ (single-source CSV)
  Relevance ~ moderate   Cumulative ~ (shareable but thin)
  Verdict: off-fit → reframe with a mechanism + multilevel/temporal design, or
            place in an applied outlet.

Candidate B (strong): two-wave multilevel field study (N = 612 in 74 teams)
            + lab experiment; servant leadership → psychological safety →
            team performance; open data/materials, lab study preregistered.
  Theory ✓ (cross-level mechanism, boundary condition)
  Rigor ✓ (temporal separation, nesting modeled, experimental causal leg)
  Relevance ✓   Cumulative ✓
  Verdict: strong fit → Feature Article.
```

## Article-type decision rules

| If the work is... | Target type | Why |
|-------------------|-------------|-----|
| Programmatic, multi-study, theory + rigor | Feature Article | the standard high-impact empirical slot |
| Focused, shorter, still a clear contribution | Research Report | tighter budget; confirm current cap (待核实) |
| A conceptual advance with no new data | Theory-development article | `joap-theory-and-hypotheses` is the spine |
| A cumulative synthesis of an effect | Meta-analysis / integrative review | transparency of coding decisions is essential |
| A qualitative I-O contribution | Qualitative research | state trustworthiness/credibility criteria |

## Reviewer / editor pushback at the fit stage

- "No theoretical contribution" → name the new mechanism, boundary, or integration; rigor alone will
  not save an atheoretical paper here.
- "Single-source cross-sectional" → add temporal separation, a second source, or an experimental leg
  before submitting (route to `joap-study-design`).
- "Better fit for an applied/practitioner outlet" → if the advance is to practice but not to I-O
  theory, JAP is the wrong venue; reframe the scientific contribution or place elsewhere.

## Anti-patterns

- A rigorous study with no advance in I-O theory (the most common JAP desk reject)
- A known effect demonstrated in one new sample or context, framed as novel
- Cross-sectional single-source self-report as the entire evidentiary base
- Choosing a Feature Article when the contribution is genuinely a Research Report (over-claiming scope)
- Confusing JAP with a sibling (Personnel Psychology, AMJ, OBHDP, JOB) and writing to the wrong bar

## Output format

```
【Question / phenomenon】one sentence
【Theoretical contribution】new mechanism / boundary / integration / construct
【Rigor】design + measurement adequate for the claim? [Y/N]
【Relevance】applied + scientific stakes
【Cumulative】shareable + preregisterable under TOP? [Y/N]
【Type】Feature Article / Research Report / theory-development / review / qualitative / meta-analysis
【Fit verdict】strong / needs reframing / off-fit (why)
【Next】joap-theory-and-hypotheses
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration, repositories, I-O measurement and meta-analysis tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — scope, accepted article types, and length policy
