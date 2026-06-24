---
name: aejmic-robustness
description: Use when extensions, edge cases, or applied robustness checks are missing for an American Economic Journal: Microeconomics (AEJ: Micro) manuscript — covering theory extensions (relaxed assumptions, alternative concepts, perturbations) and applied/experimental robustness. Decides which extensions earn their place; it does not prove the main result (see aejmic-theory-model).
---

# Robustness, Extensions & Edge Cases (aejmic-robustness)

## When to trigger

- The main result is proved but referees will ask "does it survive [relaxation]?"
- You have many possible extensions and must decide which belong in the paper
- A knife-edge or boundary case is unaddressed
- (Applied) The empirical/experimental result needs a robustness battery

## What robustness means at AEJ: Micro

For a theory paper, robustness is about the **mechanism's reach**: which relaxations preserve the result, which break it, and which boundary cases need care. AEJ: Micro values knowing the *edges* of a result as much as the result. For structural/experimental work, it is the standard robustness battery. The discipline is the same: every extension must earn its place — it either **broadens the contribution** or **defends a load-bearing assumption** flagged in `aejmic-identification`.

### Theory extensions — the menu (include only what earns its place)
- **Relax a substantive assumption:** continuum vs. finite types, asymmetric vs. symmetric players, correlated vs. independent values. Show the qualitative result survives or pin down where it changes.
- **Alternative solution concept / refinement:** does the result hold under a coarser or finer equilibrium notion? If it is concept-specific, say so.
- **Perturbations:** small changes to the information structure, timing, or commitment level (full → partial). Continuity/upper-hemicontinuity arguments belong here.
- **Boundary and knife-edge cases:** tie-breaking, measure-zero events, corner solutions — handle explicitly, do not hand-wave.
- **Negative extensions are informative:** an extension that *fails* and explains *why* sharpens the contribution and pre-empts a referee.

### Applied / experimental robustness
- Alternative specifications/estimators; sensitivity to grids, tuning, and seeds (structural/simulation).
- Placebo / falsification; multiple-testing adjustment; subsample stability.
- Report as **SEs / coverage sets**, never significance asterisks.

### The "earns its place" test
Before adding an extension, ask which of two jobs it does. If it does neither, cut it.
1. **Broadens the contribution** — the result now covers a setting readers care about (continuum types, dynamics, asymmetry) that the base model excluded.
2. **Defends a load-bearing assumption** — it answers the specific "is this knife-edge?" objection that `aejmic-identification` flagged.

An extension that merely re-derives the base result under a cosmetic re-parameterization fails the test and dilutes the paper.

### Placement discipline
- Core extensions that change the reading: **main text**. Supporting extensions: **online appendix**. Do not bury a result-defining extension in supplementary material, and do not pad the main text with extensions that add nothing.
- A negative extension that explains a *boundary* of the result often belongs in the main text precisely because it sharpens the contribution; a routine confirmation belongs in the appendix.

## Execution bridge (StatsPAI / Stata MCP)

Run the battery, don't just enumerate it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). AEJ: Micro spans applied and structural micro; the chain below is for the reduced-form / causal lane — structural estimation uses the field's own solvers.

- **Many outcomes / specifications:** `romano_wolf` (step-down FWER, accounts for
  cross-test correlation) or `benjamini_hochberg` — report the adjusted threshold.
- **OVB sensitivity:** `oster_delta` / `sensemakr` — the confounder strength that would
  overturn the headline.
- **Inference:** `wild_cluster_bootstrap` (few clusters), `twoway_cluster` / `conley`.
- **Re-fit off one handle:** `audit_result(result_id)` lists the missing checks and the
  exact `suggest_function` for each — no guessing the battery.
- **Exhibits:** `etable` / `did_summary_to_latex` from the handle — no retyped numbers.

Keep the decisive checks in the body and the exhaustive (now actually-run) battery in
the appendix. See the executed chain in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Listed candidate extensions; kept only those that broaden the contribution or defend a load-bearing assumption
- [ ] At least one substantive relaxation shows the qualitative result survives (or pins down where it changes)
- [ ] Boundary / knife-edge / tie-breaking cases handled explicitly
- [ ] Concept-dependence stated if the result is specific to one equilibrium notion
- [ ] (Applied) specification/placebo/seed-sensitivity battery run; SEs not asterisks
- [ ] Placement decided: result-defining → main text; supporting → appendix

## Anti-patterns

- An extensions section that adds robustness checks no referee asked for and the result does not need (padding)
- Hand-waving a knife-edge assumption ("generically this does not matter") without argument
- Hiding a result-defining extension in the online appendix
- A robustness table with significance stars
- Claiming the mechanism is general while every extension quietly re-imposes the key assumption

## Worked vignette (illustrative)

A contest-design paper proves the optimal prize structure is winner-take-all under risk-neutral, symmetric players. The earned extensions: (1) **risk aversion** — show winner-take-all survives up to a curvature threshold, beyond which prizes spread (broadens contribution and locates the edge); (2) **asymmetry** — show the result fails and explain why (a negative extension that sharpens the mechanism). A *non*-earned extension would be re-deriving the symmetric case with a trivially different payoff normalization — drop it.

## Output format

```
【Extension menu considered】[...]
【Kept (and why)】broadens contribution / defends load-bearing assumption
【Survives】[relaxation → result holds, with any new condition]
【Breaks / boundary】[case → what changes, handled how]
【Applied robustness】[specs / placebo / seeds] — SEs not asterisks
【Placement】main text: [...]; appendix: [...]
【Next step】aejmic-tables-figures
```
