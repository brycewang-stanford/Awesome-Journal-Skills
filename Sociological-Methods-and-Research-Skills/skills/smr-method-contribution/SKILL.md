---
name: smr-method-contribution
description: Use when sharpening the core methodological claim of a Sociological Methods & Research (SMR) paper — the new estimator/design/diagnostic and exactly what it fixes versus existing methods. Frames and bounds the contribution; does not derive its properties or run simulations.
---

# SMR Method Contribution

Use this to make the contribution explicit, proportional, and adoptable. SMR reviewers reward a
method that a working researcher can pick up and run; they punish vague "we propose a framework"
claims and overreaching generality.

## The contribution sentence (write this before anything else)

Fill both brackets, no hedging:

> *Researchers who study [problem/setting] can now [do X they could not do, or stop doing Y that
> misled them], because we [develop / evaluate / correct] [the method] under [the conditions].*

If the second bracket is "get a slightly different number," the contribution is too thin. If it is
"do everything," it is overclaimed. The right size is **one named problem, one named method, one
named condition set**.

## Position against the incumbent, not the void

Every SMR method displaces or repairs something. State the incumbent and its failure precisely:

- **What practitioners do now** (the default method, named).
- **Where it breaks** (a concrete regime: few clusters, weak instruments, non-invariance, MAR
  failure, short panels, sparse networks, small df) — with the *symptom* a user would observe.
- **Why your method fixes it** (the mechanism: orthogonalization, bias correction, a weaker
  assumption, a better small-sample approximation, a new estimand).
- **What it costs** (extra assumptions, computation, data requirements) — honest costs build trust.

A contribution framed only against "the literature" reads as throat-clearing; one framed against a
named default that fails in a named regime reads as a methods paper.

## Contribution-type templates

| Type | The claim must specify | The reviewer will check |
|---|---|---|
| New estimator | estimand, consistency conditions, efficiency vs. incumbent | does it beat the incumbent where the incumbent is valid? |
| New diagnostic/test | null, alternative, size, power region | size control under the null; power where it matters |
| Evaluation paper | methods compared, DGP space, decision rule | are the realistic regimes covered, not a strawman? |
| Critique + fix | the hidden assumption, the misuse, the correction | is the corrected procedure actually usable? |
| Computational tool | what it makes feasible, accuracy/scaling | does it match the exact method or approximate it? |

## Proportionality guardrails

- Claim a **leading case**, then say what does *not* extend. Reviewers trust authors who bound their
  own claims.
- Distinguish "we prove" from "we show by simulation" from "we conjecture." Never let a simulated
  result wear the language of a theorem.
- Resist the "general framework" frame unless you genuinely deliver generality with proofs; a sharp
  special case beats a vague general one at SMR.

## Checklist

- [ ] The contribution sentence is written with both brackets filled and no hedging.
- [ ] The named incumbent method and its concrete failure regime are stated.
- [ ] The fix mechanism is named (not just "performs better").
- [ ] The honest cost of the method (assumptions/computation/data) is stated.
- [ ] Proof-backed claims are separated from simulation-backed and conjectured claims.
- [ ] The claim is bounded: what does not extend is stated.

## Anti-patterns

- **Framework inflation**: "we develop a general framework" with no estimand, no theorem, no usable
  procedure.
- **Strawman incumbent**: beating a method no one uses, or using it outside its stated domain.
- **Mislabelled evidence**: presenting Monte Carlo regularities as proven properties.
- **Cost concealment**: hiding the extra assumption or the computational burden the method requires.
- **Undifferentiated novelty**: a variant whose advantage over the closest existing method is never
  pinned to a specific regime.

## Output format

```text
[Contribution sentence] <filled template>
[Incumbent + failure regime] <named method -> where it breaks>
[Fix mechanism] <orthogonalization / bias correction / weaker assumption / new estimand / ...>
[Honest cost] <assumptions / computation / data>
[Evidence type per claim] proved / simulated / conjectured
[Next SMR skill] smr-literature-positioning
```
