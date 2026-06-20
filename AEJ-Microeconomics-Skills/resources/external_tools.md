# External Tools & Resources for AEJ: Microeconomics

Tools and packages useful when preparing an *American Economic Journal: Microeconomics*
(AEJ: Micro) submission. AEJ: Micro is the AEA's **theory-first** microeconomics journal:
it "publishes theoretical work as well as both empirical and experimental work with a
theoretical framework." Most papers are built around a **model and proofs**; the empirical /
structural / experimental tooling below applies only to that subset. Check licenses and
current access terms before use; verify volatile process specifics on the official AEA pages
(检索于 2026-06；以官网为准).

## 1. Theory toolchain (the AEJ: Micro core)

### Writing math and proofs
- **LaTeX** (TeX Live / MacTeX / Overleaf) with `amsmath`, `amsthm`, `mathtools`; theorem
  environments for numbered Propositions/Lemmas/Theorems.
- The **AEA `aea-templates`** LaTeX/`aea.cls` package for AEA-formatted manuscripts (see the
  AEA author resources page).
- Reference managers: **Zotero**, **BibTeX/BibLaTeX**; the AEA `aea.bst` style.

### Working out and checking the model
- **Mathematica / SymPy / Maple** — symbolic algebra for comparative statics, envelope
  conditions, concavification, and verifying first-order/second-order conditions.
- **Numerical example sandboxes** — Python (`numpy`/`scipy`/`matplotlib`), Julia, or MATLAB
  to compute equilibria, optimal mechanisms, and the figures that illustrate a proposition.
- Monotone-comparative-statics references (Topkis; Milgrom–Shannon) for signing the key
  comparative static and naming its driving primitive.

## 2. Structural / computational (theory-with-estimation subset)

- Julia: `Optim.jl`, `JuMP`, `ForwardDiff.jl`, `QuantEcon.jl`.
- Python: `numpy`/`scipy`, `numba`/`jax` for fast solution methods, `estimagic` (MSM/MLE).
- MATLAB: Dynare, CompEcon, custom solvers.
- Report the solver, tolerances, starting values, and Monte Carlo recovery of parameters.

## 3. Empirical micro / experimental (theory-grounded subset)

- Stata: `reghdfe`, `ivreghdfe`, `csdid`/`did_multiplegt_dyn`, `rdrobust`/`rddensity`,
  `boottest` — see the vendored skeleton in [`code/`](code/).
- R: `fixest`, `did`, `rdrobust`, `sandwich`/`clubSandwich`.
- Python: `linearmodels`, `statsmodels`, `doubleml`/`econml`.
- Experiments: **oTree** / **z-Tree** to run; **Prolific** / **MTurk** to recruit;
  pre-registration via **AEA RCT Registry** / **AsPredicted** / **OSF**.

## 4. Figures & exhibits (AEJ: Micro house rules)
- Schematic theory figures: extensive-form timelines, type-space / signal partitions,
  equilibrium-region plots in parameter space, best-response diagrams. One idea per figure.
- Numerical-example plots: the key object (optimal mechanism, equilibrium strategy, welfare)
  as a primitive varies.
- For empirical/experimental content, **report standard errors / confidence sets, not
  significance asterisks**; vector output preferred.

## 5. Reproducibility (build for the AEA Data Editor)
- One master script (`run_all`) regenerating every table, figure, and **numerical example**.
- Pin versions (`requirements.txt`/`conda`, `renv.lock`, `Project.toml`/`Manifest.toml`,
  recorded Stata package versions); set and report seeds.
- README mapping each exhibit to its script; deposit to the **AEA Data and Code Repository
  (openICPSR)**. Pure-theory papers still deposit numerical-example code.

## 6. Process & portal (verify on the official AEA pages)
| Item | Note |
|------|------|
| Submission portal | AEA submission/editorial system for AEJ: Micro |
| Review | **Single-blind** (author revealed to referees; referees anonymous) |
| Abstract | **≤100 words** required |
| JEL codes | Per AEA practice; route the paper to the right co-editor |
| Submission fee | Member $200/$100/$0 (high/middle/low income); nonmember $300/$200/$0; 50% refund if rejected without review (volatile — confirm) |
| Publication fee | $15 per typeset page at proofs (papers submitted after Feb 1, 2024) |
| Data & code | AEA Data and Code Availability Policy; AEA Data Editor (Lars Vilhuber); openICPSR; checked before acceptance for empirical/simulation/experimental work |

## 7. Cautions
1. **Verify volatile specifics** (fee, abstract limit, editors, Data Editor, policy dates) on
   the official AEA pages — they change.
2. **The model and proofs are the deliverable** — reach for the theory toolchain first; the
   empirical/structural kit applies only to the relevant subset.
3. **Reproducibility is checked before acceptance** — assemble code (incl. numerical-example
   code) and documentation early.
4. **Respect data licenses**; state any restricted-data limitation at submission.
