# External Tools & Resources for JET-Style Economic Theory

Software, typesetting, and verification aids useful when preparing a *Journal of Economic
Theory* (JET) submission — a rigorous, original theoretical contribution in
definition/assumption/proposition/theorem/proof form, typeset in LaTeX. JET is theory-first:
empirical, experimental, quantitative, or computational material appears only when firmly
grounded in theory, so the toolchain centers on **proof exposition and reproducible
computation**, not large-scale data work. Check licenses and current access terms before use.

## 1. Typesetting (the JET house format)

- **LaTeX with the Elsevier `elsarticle` document class** — the standard for JET theory papers.
  Source files must be editable `.tex`; PDF is not accepted as a source file.
- **Reference style**: first submission may use any complete, consistent reference format; JET's
  proof-stage style is name-year / author-year. `elsarticle-harv` is the safest LaTeX default.
- Distributions: TeX Live / MacTeX; **Overleaf** for collaborative drafting.
- Theorem environments: `amsthm`, `amsmath`, `amssymb`, `mathtools`; `cleveref` for clean
  `\cref` cross-references to numbered results; `thm-restate` to restate theorems in an appendix.
- Numbering hygiene: a single shared counter for Theorem/Proposition/Lemma/Corollary aids referees
  navigating long proofs.

## 2. Reference managers

- Zotero, BibTeX / BibLaTeX, EndNote — set to the Elsevier name-year / author-year style.
- Keep **unpublished results / personal communications out of the reference list** (JET norm);
  cite working papers only where genuinely load-bearing.
- **References cited in the abstract must be given in full** — store complete entries, not "et al."

## 3. Proof-checking and exposition aids

- **Drafting-by-hand discipline**: write each lemma's proof, then list every assumption it actually
  invokes; flag any unused assumption (a generality opportunity) and any silent extra assumption.
- **Counterexample search** for "is assumption X necessary?": probe with small finite cases (2x2
  games, 2-type screening, 3-agent matching) before claiming necessity.
- Symbolic/numeric scratch work: `SymPy` (Python), `SageMath`, `Mathematica`, or `Maple` to check
  algebra, comparative statics signs, and candidate equilibria — kept as private verification, not
  as the paper's contribution.
- **Proof assistants** (Lean/`mathlib`, Coq, Isabelle) are optional and rarely expected at JET, but
  can harden a contested combinatorial or fixed-point argument.

## 4. Reproducible numerical examples (only if the paper has them)

JET has no journal-run replication archive, but Elsevier **Option C** applies when research data
exist: deposit/cite/link the data in a relevant repository, or explain why sharing is not possible.
When a paper includes numerical examples, simulations, or computed equilibria:

- Provide a small, self-contained script (Python + `numpy`/`scipy`, MATLAB/Octave, or Julia) that
  regenerates every numerical figure, table, and reported value.
- Pin the environment (`requirements.txt`, `Project.toml`/`Manifest.toml`, recorded toolbox
  versions) and **set/report random seeds** for any stochastic illustration.
- Share via a linked repository, **Mendeley Data**, a **Data in Brief** co-submission, or another
  appropriate repository, then cite/link it in the data statement. There is no JAE-Data-Archive
  analogue.

## 5. Figures (illustrative, not data-driven)

- Most JET figures are schematic: best-response/phase diagrams, lattices, timing trees, indifference
  maps, mechanism flow. Tools: TikZ/PGF (native to LaTeX), `pgfplots`, or matplotlib exported to PDF.
- Vector output (PDF/EPS) for print resolution; label every axis/region; keep notation identical to
  the body.

## 6. AI-use transparency

- **Authors must disclose generative-AI use at submission.** Reviewers and editors are barred from
  using generative-AI tools during evaluation — do not paste a manuscript under review into such a
  tool when acting as a referee.

## 7. Cautions

1. **Re-check volatile specifics** (editor roster, APC amount, calls, and submission-system details) on
   the official ScienceDirect guide for authors and editorial-board pages before a live submission.
2. **Do not conflate** the (apparent) no-submission-fee status with the separate open-access APC of
   USD 3,130 — the APC applies only if you choose open access after acceptance.
3. **Theory-first scope gate**: an empirical/computational result with no theoretical contribution is
   off-fit regardless of execution quality.
4. **Submit editable `.tex`**, not PDF source; embed full abstract references.
