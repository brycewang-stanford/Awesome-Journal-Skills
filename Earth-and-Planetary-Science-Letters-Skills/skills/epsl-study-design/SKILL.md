---
name: epsl-study-design
description: Use when designing the sampling, analytical, experimental, or modeling program for an Earth and Planetary Science Letters (EPSL) manuscript so the design can carry a process-level claim — sample context, reference materials, replication, blank control, and model resolution planned before data exist. It guides design decisions; it does not execute the campaign.
---

# Study Design (epsl-study-design)

EPSL reviewers reverse-engineer the design from the claim: if the paper says "this rate constrains
mantle upwelling," they ask whether the samples, standards, and models could ever have shown
otherwise. The predictable failures are samples without context, analytical campaigns without
traceability to reference materials, models without resolution tests, and rates without an
independent time anchor. Design against them before the first analysis. Data reduction and
uncertainty reporting live in `epsl-data-analysis`.

## When to trigger

- Planning a sampling campaign, analytical session plan, experimental run matrix, or model suite
- Choosing reference materials, blanks, replicates, and session structure for isotope work
- Setting up resolution/sensitivity tests for an inversion or geodynamic model
- A reviewer questioned sample context, standards, or model robustness

## Design principles EPSL expects

1. **Sample context is part of the design.** Location (coordinates, datum), stratigraphic or
   structural position, petrographic screening, and alteration assessment — a pristine analysis of an
   uncharacterized sample proves nothing about a process.
2. **Traceability by design.** Decide the certified/community reference materials, bracketing scheme,
   and blank-measurement cadence per session *before* the campaign; geochronology and isotope readers
   expect results tied to community standards and stated decay constants.
3. **Replication at the right level.** Full procedural replicates (dissolution → chemistry →
   measurement), not just repeat runs of one solution; independent aliquots for the headline number.
4. **Discriminating design.** Choose samples/experiments where competing hypotheses predict
   *different* outcomes — a transect across the gradient, a run matrix spanning the P–T boundary, an
   isotope pair that separates source from process.
5. **Models must be falsifiable.** Pre-plan resolution tests (checkerboard/recovery for inversions),
   parameter sweeps, and a stated criterion for what would count against the model.
6. **Anchor rates in time.** Any rate or flux needs an explicit chronologic anchor with its own
   uncertainty (U-Pb/Ar-Ar tie points, astrochronology, magnetostratigraphy) that propagates into the
   result.

## Design defenses a reviewer expects, by claim type

| If you claim... | Design must include... | Reviewer's killer question |
|-----------------|------------------------|-----------------------------|
| An age / a rate | community standards, blanks, procedural replicates, stated decay constants | "traceable to what, at what 2σ?" |
| A mantle/crust source signature | screening for alteration + a crustal-contamination test | "is this source or shallow overprint?" |
| Deep structure from an inversion | resolution/recovery tests, damping trade-off shown | "can your data even see that depth?" |
| A P–T history from experiments | demonstrated equilibrium (reversals/time series) | "did the runs equilibrate?" |
| A planetary-interior property | sensitivity to the unmeasured parameters (e.g., core size, mantle Fe) | "how much does the answer move?" |

## Worked micro-example (illustrative — dating an extinction-interval ash sequence)

To support "the eruption tempo, not total volume, drove the crisis," the design (illustrative) builds
its defenses first:

- **Context:** ash beds logged against the biostratigraphy, with the extinction horizon bracketed by
  beds above and below — otherwise tempo and crisis cannot be ordered.
- **Traceability:** chemical-abrasion U-Pb on zircon with a community tracer solution, synthetic and
  natural standards run each session, total procedural blanks measured per batch.
- **Replication:** multiple single-grain analyses per bed; the youngest-population interpretation
  pre-defined to avoid post-hoc picking.
- **Discrimination:** bed spacing chosen so a constant-rate and a pulsed eruption model predict
  resolvably different age–height patterns at the achievable ±30 kyr (illustrative) precision.
- **Time anchor:** the same beds tied into the astrochronologic framework as a cross-check.

The design's decisive move: precision requirements were derived *from the hypothesis contrast*, so the
campaign was sized to answer the question rather than hoping the errors come out small.

## Anti-patterns

- Samples with no coordinates, stratigraphic height, or petrographic screening
- Standards and blanks improvised mid-campaign instead of planned per session
- Repeat measurements of one dissolution presented as independent replication
- An inversion presented without any test of what the data can resolve
- A rate whose chronologic anchor's uncertainty is silently dropped
- A design that can only confirm the favored hypothesis, never reject it

## Output format

```
【Design】field / analytical / experimental / modeling + target observable
【Context】sample metadata + screening plan
【Traceability】standards / blanks / decay constants (or model benchmarks)
【Replication】level + n
【Discrimination】which hypotheses predict different outcomes
【Time anchor】chronology + its uncertainty (if a rate)
【Next】epsl-data-analysis
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — analytical facilities' norms, geochronology tooling, model codes
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — EPSL scope and methods-transparency expectations
