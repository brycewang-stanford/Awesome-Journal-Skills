# External Tools & Resources for GEB-Style Game Theory

Software and resources useful when preparing a *Games and Economic Behavior* (GEB) submission —
a general-interest game-theoretic contribution spanning **theory** (equilibrium analysis,
mechanism design, learning dynamics), **behavioral** modelling, and **experiments**. GEB is a
specialist game-theory journal: tools should serve clean theorem exposition, verified
computation, or a well-powered experiment. Check licenses and current terms before use.

## 1. Typesetting & theorem exposition (theory papers)

- **LaTeX** with the Elsevier **elsarticle** class (the published format; `elsarticle-num` for
  citations). Both LaTeX and Word are accepted at submission; strict formatting is deferred until
  acceptance.
- `amsmath`, `amsthm`, `mathtools` — theorem/lemma/proof environments; number theorems so referees
  and the Editor in Charge can reference them precisely.
- `cleveref` — stable cross-references to numbered results across rounds of revision.
- `tikz` / `tikz-cd` — extensive-form game trees, information sets, commuting diagrams, simplex /
  best-response plots.
- `bimatrixgame` / hand-drawn payoff tables — normal-form payoff matrices.

## 2. Symbolic & numeric game solving (results, counterexamples, examples)

- **Gambit** — compute Nash equilibria of finite normal- and extensive-form games; enumerate all
  equilibria for small games; sanity-check propositions and build worked examples.
- **Mathematica / SymPy (Python)** — symbolic verification of payoff algebra, comparative statics,
  fixed-point and incentive-compatibility conditions; turn a hand proof into a checkable derivation.
- **`nashpy` (Python)** — support enumeration, Lemke–Howson, fictitious play / replicator dynamics
  for two-player games; quick numerical illustrations of learning and stability claims.
- **`QuantEcon` (Python/Julia)** — dynamic games, Markov / stochastic games, repeated-game tooling.
- **CVXPY / linear-programming solvers** — zero-sum value computation, mechanism-design /
  optimal-auction LPs, IC/IR constraint feasibility.

## 3. Mechanism design & market design

- LP / MIP solvers (Gurobi, HiGHS, OR-Tools) for optimal mechanisms and allocation problems.
- Matching / market-design code (deferred acceptance, top trading cycles) for constructive results.
- Numerical revenue / welfare comparisons across mechanisms as appendix illustrations.

## 4. Experiments (for GEB's experimental / empirical work)

- **oTree** (Python/Django) — browser-based interactive games (public goods, bargaining, auctions,
  beauty contest); the modern standard for game-theory experiments.
- **z-Tree** — classic lab-experiment platform still common in the literature.
- **Pre-registration:** AEA RCT Registry, OSF — register hypotheses and the analysis plan for a
  behavioral-game experiment before data collection.
- **Power analysis:** `pwr` (R), `statsmodels` power tools, or simulation — justify the sample size
  per treatment cell; under-powered experimental games are a common referee objection.

## 5. Statistics for experimental analysis

- **R** — `lme4` (random effects for repeated play / session clustering), `sandwich`/`clubSandwich`
  (cluster-robust SEs at the session level), `fixest`, nonparametric tests
  (Wilcoxon / Mann–Whitney, permutation).
- **Python** — `pandas`, `numpy`, `statsmodels`, `scipy.stats`; cluster-robust and bootstrap inference.
- **Structural behavioral estimation** — quantal response equilibrium (QRE), level-k / cognitive
  hierarchy, social-preference models (Fehr–Schmidt, Charness–Rabin); maximum-likelihood fitting.
- Cluster at the **independent-session** level, not the individual — sessions are the unit of
  independent observation in interactive games.

## 6. Reproducible computation (GEB data policy is *encouraged, not mandatory*)

- GEB does **not** operate a mandatory data/code archive (unlike AER / Econometrica / JAE). Sharing is
  encouraged via repositories such as **Mendeley Data** (free, open access), with an optional
  data-availability statement or Data Brief — verify current wording on the Guide for Authors.
- Even though deposit is optional, make results checkable: pin versions (`renv.lock`,
  `requirements.txt`, recorded Gambit/oTree versions), set and report random seeds for any simulation
  or randomization, and ship a `run_all` script that regenerates every numerical example, figure, and
  experimental table from raw data or solver inputs.
- Archive on a stable repository (Mendeley Data, Zenodo, OSF) with a README, even when not required.

## 7. References & disclosure

- Reference managers: Zotero, BibTeX/BibLaTeX — no strict reference style is imposed at submission as
  long as it is **consistent**; the published style is `elsarticle-num`.
- **Generative-AI disclosure:** any use of generative AI / AI-assisted tools in manuscript preparation
  must be declared in a dedicated section titled *"Declaration of generative AI and AI-assisted
  technologies in the manuscript preparation process,"* placed before the reference list (basic
  grammar/spell-check tools are exempt). Track AI use as you write so the declaration is accurate.

## 8. Cautions

1. **Verify volatile specifics** (chief editor, the seven Editors, ~45 Advisory Editors, APC, abstract
   cap, AI-declaration wording, desk-reject / acceptance rates) on the official Guide for Authors and
   the Game Theory Society page — they change, and some were drawn from search snippets (待核实).
2. **Disclose any conference version.** GEB receives substantial CS / EC-conference-adjacent work; the
   cover letter must state how the submission differs from any prior conference paper.
3. **Match the toolkit to the claim** — a numerically "verified" equilibrium is an illustration, not a
   proof; theory claims still need a complete written proof.
4. **Cluster experimental inference at the session level** and justify power; these are routine GEB
   referee checks.
