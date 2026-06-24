---
name: ajs-research-design
description: Use when defending the research design of an American Journal of Sociology (AJS) manuscript on its own methodological terms — quantitative, comparative-historical, ethnographic, network, or formal. AJS judges each kind of work by the standards of its tradition; the design must support the theoretical claim. Defends the design; it does not run the analysis.
---

# Research Design (ajs-research-design)

AJS is method-pluralist: it publishes leading quantitative, **comparative-historical**, ethnographic,
network, and formal work, and it judges each by the standards of *its own tradition*. The job here is
to make the design defensible to a generalist, possibly cross-method, double-blind reviewer — and to
show the design actually supports the theoretical claim from `ajs-theory-building`.

## When to trigger

- Choosing or justifying the design before data collection or analysis
- A reader questioned identification, case selection, sampling, or evidentiary warrant
- Aligning the design with the mechanism and observable implications
- Mixed-methods work that must defend each component on its own terms

## Defend the design (by tradition)

### Quantitative / observational
- State the **estimand** and the **identifying assumptions** plainly; AJS rewards honesty over false
  precision. Where the design is descriptive or associational, say so and theorize accordingly.
- Justify sample, measurement, and model; pre-empt confounding and selection.

### Comparative-historical
- Make **case selection** and the **comparative logic** explicit (most-similar / most-different,
  typical / deviant, scope of the comparison).
- Keep a clear **evidentiary trail** from primary sources to claims; treat sequence and conjuncture as
  evidence, not decoration.

### Ethnographic / interview
- Describe **access, site/case selection, duration, and positionality**; justify why this case bears
  the theoretical weight.
- Make the **link from fieldnotes/transcripts to claims** legible (without exposing informants).

### Network / computational
- Justify **boundary specification, tie definition, and missingness**; match the model (e.g., ERGM,
  SAOM) to the relational question.

### Formal
- Tie assumptions to the substantive setting; specify what empirical patterns would corroborate or
  challenge the model.

## Match design to claim

The single most common AJS reviewer objection: **the design cannot bear the theoretical claim.** Walk
the chain: claim → mechanism → observable implication → the design's leverage on it. If a step is
weak, tighten the claim or strengthen the design — do not overclaim.

## Referee-pushback patterns by tradition (the modal AJS objection)

The most common AJS design rejection is "the design cannot bear the theoretical claim." Recurring objections by tradition; confirm method expectations against the journal's current submission guidelines.

| Referee writes… | Tradition | The AJS-appropriate fix |
|-----------------|-----------|------------------------|
| "Selecting on the outcome." | comparative-historical | add a non-outcome case or acknowledge the limit |
| "Representativeness asserted." | ethnographic | argue why this case bears the theoretical weight |
| "Identification overclaimed." | quantitative | restate as descriptive/associational and theorize it |

## Calibration with a quick example (hedged)

AJS judges each tradition by its own standard, not a single template; unlike a parsimony-first sibling that privileges a clean causal estimate, it accepts a richly defended interpretive or comparative design when it bears the claim. Illustrative: an author selecting four states that all underwent revolution, then theorizing "state breakdown causes revolution," is flagged for selecting on the outcome; the fix adds two negative cases (comparable fiscal crises that did *not* break down) so the comparison can see the mechanism fail as well as fire. Confirm method guidance against the journal's current submission guidelines.

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AJS is general sociology with a strong theory tradition; apply the chain below to its quantitative-empirical lane.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference, `romano_wolf` for many-outcome
  family-wise control, and `mediate` for mediation (not naive controlling-away).
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the effect size in interpretable units; route the full battery to the
appendix/supplement. A run end-to-end (synthetic data, real returns) is in the
[JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Anti-patterns

- Borrowing a quantitative identification template for work that is interpretive or comparative
- Case selection that quietly guarantees the result (selecting on the outcome without acknowledging it)
- Ethnography that asserts representativeness it cannot support
- Overclaiming causality from an associational design
- A design that tests something adjacent to, but not, the stated theoretical claim
- Designing only to confirm the mechanism, with no case where it could be seen to fail


## Design pass for American Journal of Sociology

Treat this skill as an executable review pass, not a prose hint. First lock the social process, data leverage, causal or interpretive warrant, and theoretical payoff; then judge whether the current manuscript answers the venue's real reader: sociology reviewers who value deep theory, durable empirical leverage, and careful social-mechanism claims.

- **Do the pass:** Lock the unit, scope, comparison, validity threat, and minimum decisive evidence before recommending collection, analysis, or submission.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ASR for broader empirical sociology, Social Forces for wider substantive range, Demography for population mechanisms; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Tradition】quantitative / comparative-historical / ethnographic / network / formal / mixed
【Claim it must support】from theory-building
【Design leverage】how this design bears on the claim
【Key assumptions / threats】identification, selection, access, boundary, etc.
【Evidentiary trail】sources → claims is legible? [Y/N]
【Verdict】supports the claim / needs tightening / overclaims (fix)
【Next】ajs-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — design and method tooling by tradition
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS method-pluralism and reviewer-matching policy
