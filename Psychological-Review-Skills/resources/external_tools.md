# External Tools & Resources for Psychological Review Theory & Modeling

Psychological Review publishes **theoretical contributions** — new theory, formal/mathematical/
computational models, and major syntheses. There is **no primary empirical study**: data appear
only to motivate or constrain the theory. So this resource list is deliberately different from an
empirical journal's: it centers on tools for *building and analyzing formal models*, *finding the
theoretical conversation*, *drawing model diagrams and simulation figures*, and *checking the logic
of an argument* — not on running experiments or vendoring datasets.

> Volatile specifics (editor, exact length/abstract limits, portal, fees, APA edition) change.
> Always verify submission-stage requirements against the official APA Psychological Review author
> page before submission. 检索于 2026-06；以官网为准.

## 1. Modeling environments (the core "tooling" for a formal-model paper)

| Tool | Use |
|------|-----|
| Python (NumPy / SciPy / SymPy) | General formal and computational modeling; SymPy for closed-form derivations |
| R | Cognitive modeling and model fitting; rich statistics for confronting existing data |
| MATLAB | Long-standing in mathematical psychology; toolboxes for dynamical systems and optimization |
| Julia | High-performance numerics for simulation-heavy models and parameter sweeps |
| Stan / PyMC / JAGS | Bayesian model fitting and parameter estimation; posterior-based model comparison |
| ACT-R, Nengo, PyTorch/JAX | Cognitive architectures and neural-network / connectionist model implementations |

These produce the **simulation-of-model-behavior** figures Psychological Review expects (see
[`../skills/psychrev-conceptual-exhibits/SKILL.md`](../skills/psychrev-conceptual-exhibits/SKILL.md)).

## 2. Model analysis: identifiability, recovery, comparison

The modeling-specific reviewer probes (see
[`../skills/psychrev-boundary-conditions/SKILL.md`](../skills/psychrev-boundary-conditions/SKILL.md)):

- **Parameter recovery** — simulate data from known parameters, refit, check recovery (custom scripts).
- **Model identifiability / mimicry** — landscaping / model-recovery designs to test whether rivals
  can mimic each other on the available data.
- **Model comparison** — AIC/BIC/WAIC/LOO, Bayes factors, and cross-validation/generalization tests.
- **Sensitivity analysis** — sweep parameters and functional forms to show the qualitative result is robust.

## 3. Locating the theoretical conversation

| Tool | Use |
|------|-----|
| Web of Science / Scopus | Citation-trail mapping: who proposed and who critiqued the rival models you must beat |
| Google Scholar | "Cited by" forward search to find the current, strongest form of each rival model |
| APA PsycInfo | The discipline database; locate the theoretical literature and prior formal accounts |
| Connected Papers / Litmaps | Visual citation graphs to see a modeling tradition's structure and find the gap |

## 4. Foundational theoretical traditions (durable, not volatile)

Knowing which modeling tradition you enter matters more than any single citation:

- Mathematical/cognitive modeling: signal detection, sequential-sampling (diffusion/accumulator), SIMPLE/REM memory models
- Connectionist / PDP and modern neural-network accounts of cognition and perception
- Bayesian / rational-analysis and resource-rational approaches
- Cognitive architectures (ACT-R, Soar) and process models
- Reinforcement learning and associative-learning theory (e.g., prediction-error accounts)
- Dynamical-systems and neural-field models; Marr's levels of analysis as an organizing frame

## 5. Reference management

| Tool | Note |
|------|------|
| Zotero | Open-source; group libraries for tracking a modeling literature |
| EndNote | Broad journal-style support; APA output |
| Mendeley / Paperpile | PDF annotation; Paperpile pairs well with Google Docs drafting |

Psychological Review follows **APA Style** (currently 7th edition; verify): author–date in-text,
full reference list. Configure your manager to APA output and verify against the current APA manual.

## 6. Model diagrams & simulation figures (the only "figures" here)

Figures carry *theoretical* work — architecture diagrams and plots of model behavior, never experiments.

| Tool | Use |
|------|-----|
| matplotlib / ggplot2 / Makie.jl | Simulation-of-behavior plots, parameter sweeps, model-vs-data overlays |
| TikZ / LaTeX | Precise model/architecture diagrams; publication-quality typesetting of equations |
| draw.io (diagrams.net) / OmniGraffle | Box-and-arrow architecture diagrams (every box a construct, every arrow a process) |
| Inkscape | Vector polishing of diagrams to APA resolution/format specs |

Design rule: every box is a defined construct/module, every arrow a specified process; every
simulation caption discloses the parameters and whether they were fit or set a priori.

## 7. Argument-logic aids

Theory papers are evaluated on logical and formal soundness:

- Argument-mapping (premise → premise → conclusion) to expose hidden assumptions before reviewers do
- Per-prediction worksheet: does each prediction *follow* from the assumptions, or is it asserted?
- Disconfirming-case worksheet: name a pattern that would falsify the theory; check whether a
  boundary condition covers it
- Signature-vs-accommodation log: mark which predictions distinguish your model from rivals vs. which merely fit known data

## 8. Submission system & official pages

| Resource | Use |
|----------|-----|
| Editorial Manager (Psychological Review portal) | Submission and masked review |
| APA Psychological Review author page | Scope, length, format, article types, ethics — the binding source |
| APA Style (apastyle.apa.org) | In-text and reference formatting; manuscript structure |
| APA Ethics Code | Authorship, originality, disclosure, conflict-of-interest rules |

## 9. Cautions

1. **No empirical study, ever.** If the contribution is a new effect or method, the project belongs at
   a JEP-family journal or Psychological Science. Data here only motivate or constrain the theory.
2. **Engage the rival models.** Reviewers are usually the rival modelers; cite their current, strongest form.
3. **Share your model code.** For a computational model, prepare your own simulation/fitting code with a
   README (this is the model's code, not a shared empirical-analysis pipeline; there is no dataset to deposit).
4. **Verify limits.** Length (15,000-word soft threshold), abstract, APA edition, and fees change —
   confirm on the current author page before you submit.
