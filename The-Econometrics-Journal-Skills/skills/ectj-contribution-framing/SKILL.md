---
name: ectj-contribution-framing
description: Use when sharpening a contribution for The Econometrics Journal (EctJ) into a compact leading-case claim with demonstrated applied value, covering the failure mode of incumbent methods, the smallest sharp advance, the applied payoff, and scope guardrails that survive the one-week RES desk screen.
---

# EctJ Contribution Framing

Use this after the method and application are known but before final writing. EctJ seeks
original contributions of direct or potential value in applications, and explicitly favors
path-breaking, leading-case work over exhaustive treatment. Because the Editor-in-Chief
screens conforming papers within about one week and desk-rejects with little comment, the
contribution must be legible fast: the summary (no more than 150 words) and opening pages
have to make the advance and its applied payoff obvious on a single read.

## Framing checks

- Lead with the econometric problem and why existing methods fail in an applied setting.
- State the leading-case advance: new identification logic, estimator, test, approximation,
  inference method, or computation.
- Explain what applied researchers can now do that they could not do cleanly before.
- Keep claims proportional to the paper's scope; do not market a narrow special case as a
  complete framework.
- Make the empirical application more than an illustration: it should reveal practical value.

## EctJ-ready contribution pattern

Write the contribution in four linked sentences:

1. **Failure mode** - name the empirical or methodological setting where the incumbent approach breaks.
2. **Leading case** - state the estimator, test, identification result, or computational shortcut as the
   smallest sharp case that teaches the general idea.
3. **Applied value** - say what an applied user can now estimate, test, diagnose, or report with less bias,
   weaker assumptions, better inference, or feasible computation.
4. **Scope guardrail** - say which environments are outside the theorem, simulation design, or application.

If any sentence requires a page of qualification, the contribution is probably too broad for EctJ's
compact format. Route back to `ectj-topic-selection` and narrow the leading case.

## Worked vignette: few-treated-cluster inference

A hypothetical EctJ submission proposes a restricted wild bootstrap for difference-in-differences
with very few treated clusters (illustrative numbers throughout). The four-sentence pattern becomes:

1. **Failure mode**: with 6 treated clusters out of 40, conventional cluster-robust t-tests
   over-reject; in the authors' pilot simulations a nominal 5% test rejects about 13% of the time.
2. **Leading case**: a restricted wild-bootstrap test that is asymptotically valid as cluster
   counts grow and exactly controls size in a symmetric leading case with one treated cluster.
3. **Applied value**: applied researchers running state-level policy evaluations can report a test
   whose simulated size stays near 5.4% with 6 treated clusters instead of 13%.
4. **Scope guardrail**: validity is not claimed under heterogeneous cluster sizes beyond the
   simulated range or for non-binary treatments.

Each sentence is auditable against a theorem, a simulation panel, or the application exhibit. That
auditability, not rhetorical breadth, is what survives the one-week RES screen.

## Framing failure modes the EctJ screen punishes

| Framing pattern | Why it fails at EctJ | Repair |
|---|---|---|
| "We provide a general framework for..." | Reads as exhaustive treatment, the opposite of the leading-case scope | Restate as the smallest sharp case plus an extensions remark |
| Method introduced before the applied failure | Editor cannot see direct or potential applied value quickly | Open with the empirical setting where incumbents break |
| Applied value asserted, never demonstrated | EctJ expects an empirical application even for theory papers | Point the claim at a specific application exhibit |
| Novelty defined only against statistics or ML | The econometric setting must add something | Name the econometric object and assumption the paper changes |

Calibrate against recent EctJ issues: accepted papers typically spend their first page on the
failure mode and the leading-case result, deferring everything else. If the draft's first page
could open a survey at a longer-format journal instead, the framing has not yet earned this venue.

## Output format

```text
[Contribution sentence] <one EctJ-ready sentence>
[Applied-value sentence] <who benefits and how>
[Existing-method gap] <what breaks before this paper>
[Scope guardrail] <what the paper does not claim>
[Intro edit] <paragraph-level fix>
```
