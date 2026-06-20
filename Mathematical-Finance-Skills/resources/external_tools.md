# External Tools & Resources for Mathematical Finance

Tools, references, and software useful when preparing a *Mathematical Finance* (Wiley)
submission — a **mathematically rigorous** contribution in financial mathematics: stochastic
analysis, stochastic calculus, probability theory, and proofs, applied to derivative pricing,
risk, portfolio theory, and market microstructure. This is a theory-first venue: numerical
experiments are welcome **only** when they support rigorous theoretical developments, never as
a stand-alone empirical exercise. Check licenses and current terms before use.

## 1. Typesetting & proof workflow (LaTeX-centric)

- **LaTeX**: TeX Live / MacTeX / Overleaf — *Mathematical Finance* uses a strong LaTeX workflow; Research Exchange expects the `.tex` source ("Main Document - LaTeX .tex File"), a compiled PDF ("Main Document - LaTeX PDF"), and supporting files ("LaTeX Supplementary File").
- **Wiley LaTeX template / class** — use the publisher's article class where available; keep custom macros minimal so the source compiles cleanly on the editor's side.
- **Proof / theorem environments**: `amsthm`, `thmtools`, `mathtools`, `amssymb` for theorem–lemma–proof structure and aligned displays.
- **Cross-referencing**: `cleveref` for consistent "Theorem 3.2 / Assumption (A1)" references; `hyperref` for navigation.
- **References**: BibLaTeX / BibTeX via Zotero or JabRef. Confirm the journal's current
  named reference style on the Wiley author page before final upload.

## 2. Classification codes (required-style metadata)

- **JEL codes** — economics classification (e.g., G13 derivative pricing, C61 optimization, G11 portfolio choice).
- **Mathematics Subject Classification (AMS/MSC 2020)** — e.g., 91G (mathematical finance), 60H (stochastic analysis / SDEs), 60G (stochastic processes), 49 (calculus of variations / optimal control), 93E (stochastic control).
- **Keywords** — supply field keywords alongside both code sets, as the journal expects.

## 3. Symbolic & numerical computation (for illustrative experiments only)

| Tool | Typical use |
|------|-------------|
| Mathematica / Maple / SymPy | Symbolic checks of closed-form pricing/PDE solutions, transform inversions |
| MATLAB / Julia / Python (NumPy, SciPy) | Numerical PDE/SDE solvers, Monte Carlo, transform methods illustrating a theorem |
| QuantLib | Reference implementations of pricing models for sanity checks |
| `numpy`/`scipy`, `cvxpy` | Convex optimization, utility maximization examples |
| Julia (`DifferentialEquations.jl`, `JuMP`) | SDE simulation and optimization in self-contained examples |

Use these to *illustrate* and *stress-test* a theoretical result (convergence rates, error
bounds, qualitative behavior). Routine application of computational methods to financial data,
with no supporting rigorous analysis, is explicitly out of scope for this journal.

## 4. Mathematical toolkit by subfield

| Subfield | Core machinery | Typical objects |
|----------|----------------|-----------------|
| Derivative pricing | Risk-neutral valuation, PDE/PIDE, transform methods | Martingale measures, Feynman–Kac, Lévy/jump models |
| Portfolio & utility | Stochastic control, duality, BSDEs | HJB equations, convex duality, martingale optimality |
| Risk measures | Convex analysis, robust representation | Coherent/convex risk measures, time-consistency |
| Optimal stopping / American options | Free-boundary problems, Snell envelope | Variational inequalities, smooth pasting |
| Market microstructure | Stochastic optimal control, mean-field games | Limit-order-book models, optimal execution |
| Arbitrage theory | Functional analysis, separating measures | FTAP, NFLVR, semimartingale theory |

## 5. Reproducible computation (lighter than empirical journals)

- This is **not** a data-archive journal: there is **no** mandatory JAE-style replication
  package. The emphasis is on **self-contained proofs**, not empirical data replication.
- Still include a **Data Availability Statement** per Wiley policy, even when no data are used
  (state that no new data were generated, if applicable).
- If you include numerical experiments, make them reproducible: pin software versions, set and
  report random seeds for Monte Carlo, and consider depositing illustrative code on Zenodo /
  GitHub and citing it per the Joint Declaration of Data Citation Principles.

## 6. Process & portal

| Item | Note |
|------|------|
| Submission portal | Wiley Research Exchange (`submission.wiley.com`) / Author Services |
| Review model | Single-blind (author identity may remain) |
| Submission fee | No separate submission fee was found in the checked Wiley/BFS sources; live-check the Wiley submission flow before advising an author |
| Open Access | Optional hybrid route; confirm current APC terms on Wiley's OA/APC pages if the author selects Open Access |
| Society access | Bachelier Finance Society members get free online access via their BFS account |
| Publisher | Wiley-Blackwell |

## 7. Cautions

1. **Rigor is mandatory, not optional** — every formal result needs a full, self-contained
   proof; "numerical evidence" does not substitute for a theorem.
2. **Move detailed analysis to the Appendix** — keep the main text on results and intuition.
3. **Numerics must serve theory** — purely computational data applications are out of scope.
4. **Verify volatile specifics** (editor, APC amount, abstract limit, reference style) on the
   official Wiley page immediately before upload.
