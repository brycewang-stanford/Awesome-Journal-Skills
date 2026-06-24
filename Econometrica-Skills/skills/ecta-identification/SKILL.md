---
name: ecta-identification
description: Use when the bottleneck is identification and inference for an Econometrica manuscript — identification conditions and asymptotic distribution theory for an estimator, or axioms and existence/uniqueness for a theory model. Stress-tests the formal foundations before the proofs and simulations are written.
---

# Identification, Asymptotics, and Axiomatic Foundations (ecta-identification)

## When to trigger

- An estimator is defined and shown consistent, but its **limiting distribution** is missing
- Identification is asserted ("the parameter is identified") without a proof or counterexample analysis
- A theory model posits behavior but the **axioms** are not isolated, or existence/uniqueness is unproven
- Inference is proposed (standard errors, tests) without the asymptotic theory that justifies it

This is the formal spine. Econometrica referees check it first; a gap here sinks the paper.

**Re-slant for Econometrica.** Identification here is *not* primarily "do I have a credible
research design for a causal estimate" (that framing belongs to AER / QJE / JPE / REStud).
Econometrica's core is **identification and estimator validity inside structural and
econometric models** — is the structural parameter / functional a one-to-one image of the
data distribution, and does the proposed estimator have a derived limiting distribution that
licenses its inference? Credible-design content (Branch D) is still in scope for the
journal's applied/structural submissions, but the methodological object — completeness,
rank, support, the asymptotic law of *your* estimator — is what carries the paper. Lineage:
GMM identification and asymptotics (Hansen 1982), nested fixed-point identification of a
dynamic discrete-choice model (Rust 1987), selection-model identification (Heckman 1979).

## Branch A — Econometric theory: identification

1. **Define the parameter / object** as a functional of the data-generating process, separate
   from any estimator. Identification is a property of the population, not the sample.
2. **State the identification conditions** as numbered assumptions (rank / completeness /
   support / exclusion / monotonicity, as relevant). For each, say what fails without it.
3. **Prove identification**: show the map from distribution to parameter is one-to-one on the
   admissible class. Where identification can fail, give the explicit failure (partial
   identification, set identification, point identification under added conditions).
4. **Distinguish point vs. partial identification.** If only set identification holds, define
   the identified set and characterize it; do not silently assume point identification.

## Branch B — Econometric theory: asymptotic distribution theory

1. **Consistency** under stated conditions (which sample sizes / sequences; i.i.d., dependent,
   or panel asymptotics — be explicit about the regime).
2. **Rate of convergence** — root-n or nonstandard (n^{1/3}, boundary, super-consistent).
   A nonstandard rate must be derived, not assumed.
3. **Limiting distribution** — derive it; state the asymptotic variance and a consistent
   estimator of it. If the limit is non-normal (e.g., from a boundary, a non-differentiable
   moment, or a unit root), characterize it and justify inference accordingly.
4. **Uniformity** — is the asymptotics pointwise or uniform over the parameter space? Modern
   referees ask for uniform validity (weak-identification-robust, boundary-robust) where the
   pointwise theory is known to mislead.
5. **Regularity conditions** — smoothness, moment, and bandwidth/tuning conditions stated
   precisely; primitive where possible rather than high-level.

## Branch C — Micro / game / decision theory: axioms and existence/uniqueness

1. **Isolate the axioms** on the primitive (preference relation, choice function, payoff
   structure). Each axiom should be behaviorally interpretable and stated independently.
2. **Existence** — prove an equilibrium / representation / solution exists (fixed-point,
   topological, or constructive argument), with the topology and continuity conditions made explicit.
3. **Uniqueness** (or characterization of the set) — prove uniqueness or characterize
   multiplicity; a representation theorem should pin the functional form up to its known degrees
   of freedom (e.g., affine transformations of a utility index).
4. **Independence / tightness of axioms** — show no axiom is redundant (each is necessary) and,
   ideally, that the axiom set is tight (relaxing any one breaks the representation).
5. **Behavioral payoff** — translate the formal result into a statement about observable
   behavior or comparative statics.

## Branch D — Structural / empirical (and credible-design applied)

1. State the model's microfoundations and the **identifying restrictions** explicitly.
2. Argue identification of the structural parameters from the available variation (functional
   form, exclusion, support, instruments) — separate what is identified nonparametrically from
   what relies on parametric assumptions.
3. Provide the estimator's asymptotics or a justified inference procedure; if you use a known
   estimator off the shelf, cite the precise theorem that licenses your standard errors.
4. Counterfactuals must be objects the identification argument actually delivers.
5. **Credible-design content still belongs here** for applied/structural submissions (a DID,
   RDD, or IV used inside the paper). But at Econometrica the design alone is not the
   contribution — the methodological or identification argument is. If the design is
   off-the-shelf and the estimand is the whole point, the paper is general-interest-applied,
   not Econometrica (see `ecta-topic-selection`).

## Execution bridge (StatsPAI / Stata MCP)

Estimate and audit the design, don't only describe it. Full map:
[`execution-with-mcp`](../../../shared-resources/empirical-methods/execution-with-mcp.md). Econometrica publishes econometric theory and applied micro; the chain below serves its applied/empirical papers (weak-IV-robust and modern-DiD reporting expected) — pure theory uses its own apparatus.

- `detect_design` → `recommend` → fit with `as_handle=true` → `audit_result`.
- **Observational causal claims:** staggered DiD (`callaway_santanna` / `sun_abraham` +
  `bacon_decomposition` + `honest_did_from_result`); IV (`effective_f_test` +
  `anderson_rubin_ci`); RDD (`rdrobust` + `mccrary_test`).
- **Experiments:** randomization-based inference + `romano_wolf` for many-outcome control.
- **Sensitivity:** `oster_delta` / `sensemakr` for observational claims.

Report the magnitude in interpretable units; route the full battery to the appendix. A
run end-to-end (synthetic data, real returns) is in the [JF execution walkthrough](../../../Journal-of-Finance-Skills/resources/worked-examples/02-execution-walkthrough.md).
## Checklist

- [ ] Parameter/object defined as a population functional, separate from the estimator
- [ ] Identification conditions numbered; each shown to bind (counterexample if dropped)
- [ ] Point vs. partial identification stated honestly
- [ ] Rate of convergence derived (not assumed), including any nonstandard rate
- [ ] Limiting distribution derived; asymptotic variance + consistent estimator given
- [ ] Pointwise vs. uniform asymptotics addressed; weak-identification robustness considered
- [ ] Regularity conditions primitive and minimal
- [ ] (Theory) axioms isolated, independent, behaviorally interpretable; existence + uniqueness proven

## Anti-patterns

- "The parameter is clearly identified" with no argument and no failure analysis
- Reporting standard errors with no asymptotic theory justifying them
- Assuming root-n / normality when the moment condition is non-differentiable or on a boundary
- Pointwise asymptotics in a setting (weak IV, near-boundary) where they are known to fail
- High-level "regularity conditions" that quietly assume the hard part
- Axioms that overlap or include a redundant one; existence claimed without a fixed-point argument
- A representation theorem that does not pin the functional form (uniqueness left open)

## Output format

```
【Branch】identification / asymptotics / axioms / structural
【Object/parameter】... (population functional or representation)
【Identification】point / partial — argument: ...
【Rate & limit】rate: ...; limiting distribution: ...; variance estimator: ...
【Uniformity】pointwise / uniform / weak-id-robust
【Regularity conditions】[...]  (gaps: [...])
【Next step】ecta-theory-model
```
