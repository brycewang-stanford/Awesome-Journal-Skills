---
name: uist-experiments
description: Use when designing or auditing the evaluation of a UIST paper — choosing among technical benchmarks, controlled comparisons, usability walkthroughs, expert sessions, and demonstration applications, matching evaluation shape to the systems claim, and avoiding the ritual study that proves nothing the paper asserts.
---

# UIST Experiments

UIST does not have a single evaluation orthodoxy; it has a matching rule. The
evaluation must measure the claim the artifact makes, and different artifact types
make categorically different claims. The classic failure is the **ritual study**: a
12-participant SUS-and-task-time exercise bolted onto a toolkit paper whose actual
claim — "this abstraction lets developers build a class of things" — no usability
score can support.

## Match evaluation to claim type

| Artifact claim | Primary evidence | Supporting evidence |
|---|---|---|
| "This technique outperforms the status quo" (input, pointing, text entry) | Controlled within-subjects comparison against the real incumbent | Learning-curve data over sessions |
| "This hardware enables new sensing/actuation" | Technical characterization: accuracy, range, SNR, latency across conditions | Small usage session showing humans can operate it |
| "This toolkit lowers the floor / raises the ceiling" | Demonstration portfolio + developer study or expert walkthrough | Code-size/API comparisons, workshop deployments |
| "This pipeline makes X automatic" | Quantitative accuracy on held-out real inputs + failure taxonomy | End-to-end examples spanning input diversity |
| "This system supports task Y better" | Task-based study instrumented around Y | Log analysis, think-aloud excerpts |

Two smaller lanes are legitimate at UIST and often misused: **demonstration-only
evidence** carries a paper when the enabling novelty is extreme (the demo *is* the
result), and **expert sessions** (3-6 domain professionals in deep sessions) beat 20
novices when the system targets professionals.

## Technical evaluation discipline

The technical evaluation is the half UIST reviewers read most skeptically, because
they build things too:

- Characterize across the **operating envelope**, not the sweet spot: distances,
  angles, lighting, surface materials, user anthropometrics — whatever the physics of
  your system cares about.
- Report **distributions, not means**: median and 95th percentile latency; per-user
  accuracy spread. Interactive systems fail in the tails.
- Measure **with the interaction loop closed** where possible; camera-to-photon
  latency and recognition-in-context differ from component benchmarks.
- Include a **failure section**: conditions where recognition drops, actuation
  stalls, or tracking drifts. A measured failure boundary reads as competence.

## Baselines that respect the reader

Compare against what a skilled practitioner would actually use today — the shipping
technique, the standard library, the commercial device — not a strawman
reimplementation. When no incumbent exists (genuinely new capability), say so and
substitute ablations: which component of the pipeline buys which capability.

## Study mechanics for the systems context

- Counterbalance technique order; interaction studies carry strong carryover effects.
- Power the comparison for the effect you claim; 12 participants detect large
  effects only, so do not claim small ones from them.
- Report effect sizes with confidence intervals alongside any test statistic.
- Instrument the system itself — logs are free evidence and reviewers trust
  event-level data over recollection.
- IRB/ethics approval, compensation, and demographic reporting are expected whenever
  humans touch the system; plan approval months before the March deadline (see
  `uist-workflow`).

## Ablations for systems: which component buys which capability

Interactive systems are pipelines, and reviewers want the credit assignment:

- Disable or downgrade each novel component and re-measure the end-to-end
  behavior; report the deltas in one table.
- Substitute the naive version of each component (the off-the-shelf recognizer,
  the fixed calibration) to show the custom one earns its complexity.
- Where components interact, test the two-way combinations that your claims
  depend on, not the full factorial — and say that is what you did.
- Ablations also protect the rebuttal: "does the gain come from X or from Y?" is
  among the most common reviewer questions at this venue, and the answer must
  already exist by then (see `uist-author-response`).

## The objections this venue actually raises

| Recurring objection | Pre-emption |
|---|---|
| "The comparison baseline is a strawman" | Use the shipping incumbent; state its version and settings |
| "Latency/accuracy measured under ideal conditions" | Report the envelope and the tails, not the demo-day sweet spot |
| "The study tasks were designed around the system's strengths" | Include at least one task chosen from prior work's protocol |
| "n = 12 cannot support this claim" | Match claim size to power; concede small effects |
| "The applications are all variations of one scenario" | Diversify the portfolio across input contexts and user types |
| "No failure analysis" | A measured failure boundary section, always |

## Pre-submission evidence audit

```text
For each contribution claim C1..Cn in the introduction:
  [ ] name the evaluation section that tests it
  [ ] name the measure and the condition range
  [ ] name the comparison point (incumbent / ablation / none-with-justification)
  [ ] name where dispersion is reported (SD, CI, percentiles)
Orphan claims -> weaken the claim or add evidence
Orphan studies -> cut, or promote to a claim the intro actually makes
```

Run this audit against the video figure too: any capability the video shows that no
section measures is a question a reviewer will ask in exactly those words (rebuttal
implications in `uist-author-response`).

## Reporting

Put the strongest number in the abstract with its condition attached. In the body,
one summary table of the technical characterization beats four bar charts; per-cell
detail goes to the appendix, raw harness and logs to the supplement (packaging rules
in `uist-artifact-evaluation` and `uist-reproducibility`).

## Output format

```text
[Claim type] technique / hardware / toolkit / pipeline / task-support
[Evidence match] matched / partial mismatch / ritual-study warning
[Envelope coverage] <conditions characterized vs conditions claimed>
[Baseline honesty] real incumbent / ablation / missing
[Weakest link] <the claim most exposed in review + cheapest fix>
```
