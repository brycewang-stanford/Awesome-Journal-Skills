# COLT Exemplars Library (result type × technique)

> **Verified via web search, access date 2026-07-08.** Each paper below was confirmed
> against its **PMLR proceedings page** (`proceedings.mlr.press/...`), matching the
> volume to a **Conference on Learning Theory** edition plus authors, year, and page
> range. Anything that could not be cleanly pinned to COLT was omitted and documented
> at the bottom. Five verified rows beat fifteen guessed ones.
>
> **Volume-trap warning:** PMLR volume numbers interleave COLT with AISTATS, ICML, and
> other venues. v23 is COLT 2012 but v33 is AISTATS 2014; v247 is COLT 2024 but v235
> is ICML 2024. Always confirm the volume landing page says "Conference on Learning
> Theory" before attributing a paper to COLT.
>
> **Zero-hallucination rule:** rows give positioning only. Do not quote rates,
> constants, or theorem numbers from memory — open the PMLR page first.

---

## How to use this library

Find the row nearest your result type × technique, then study how that paper (a) puts
the formal statement within reach of the first pages, (b) names its delta against
prior bounds, and (c) sells the technique — the COLT bar described in
[`../../skills/colt-writing-style/SKILL.md`](../../skills/colt-writing-style/SKILL.md)
and [`../../skills/colt-related-work/SKILL.md`](../../skills/colt-related-work/SKILL.md).

**COLT edition ↔ PMLR volume (verified rows below):** v19 = COLT 2011 (24th);
v23 = COLT 2012 (25th); v40 = COLT 2015 (28th); v65 = COLT 2017 (30th);
v247 = COLT 2024 (37th).

---

## By result type

### Framework / characterization (online learnability beyond regret)

- **Rakhlin, Sridharan & Tewari, "Online Learning: Beyond Regret," COLT 2011, PMLR
  v19:559-594.** Verified: `proceedings.mlr.press/v19/rakhlin11a.html`.
  - **Why it is an exemplar:** extends online learnability to general performance
    measures (Φ-regret, approachability, calibration) in one framework — the COLT
    "characterization paper" at its best, where the contribution is the unifying
    machinery rather than a single rate.
  - **Self-check:** if your paper is a framework, can you name at least three prior
    problems it captures as corollaries, the way this one does?

### Upper bounds under a constraint (privacy × online learning)

- **Jain, Kothari & Thakurta, "Differentially Private Online Learning," COLT 2012,
  PMLR v23:24.1-24.34.** Verified: `proceedings.mlr.press/v23/` (25th Annual
  Conference on Learning Theory, Edinburgh).
  - **Why it is an exemplar:** transports a learning guarantee into a constrained
    model (differential privacy) and prices the constraint in the regret — the
    canonical "known problem, new axis" COLT contribution shape.
  - **Self-check:** does your bound make the *cost of the constraint* explicit, so a
    reviewer can compare directly with the unconstrained rate?

### Non-convex optimization with guarantees

- **Ge, Huang, Jin & Yuan, "Escaping From Saddle Points — Online Stochastic Gradient
  for Tensor Decomposition," COLT 2015, PMLR v40:797-842.** Verified:
  `proceedings.mlr.press/v40/Ge15.html` (28th Conference on Learning Theory).
  - **Why it is an exemplar:** proves convergence guarantees for stochastic gradient
    in a structured non-convex problem — theory built to explain and enable practice,
    exactly the "theory that sheds light on empirical phenomena" the CFP invites.
  - **Self-check:** if your theory targets a practical algorithm, is the analyzed
    algorithm actually the practical one, or a cousin you must justify?

### Open problem piece (agenda-setting short form)

- **Agarwal, Krishnamurthy, Langford, Luo & Schapire, "Open Problem: First-Order
  Regret Bounds for Contextual Bandits," COLT 2017, PMLR v65:4-7.** Verified:
  `proceedings.mlr.press/v65/agarwal17a.html`.
  - **Why it is an exemplar:** four pages posing two precisely parameterized open
    questions; later work (e.g., a PMLR v80 paper titled after it) attacked them —
    proof that a well-posed COLT open problem moves the field. Model for the track
    described in [`../../skills/colt-topic-selection/SKILL.md`](../../skills/colt-topic-selection/SKILL.md).
  - **Self-check:** is your question stated with explicit target rates, so a solver
    knows exactly when they have won?

### Clean structural result in a current volume

- **Kozachinskiy & Steifer, "Simple online learning with consistent oracle," COLT
  2024, PMLR v247:3241-3256.** Verified: `proceedings.mlr.press/v247/kozachinskiy24a.html`.
  - **Why it is an exemplar:** a compact, self-contained result in a recent volume —
    evidence that COLT accepts short, sharp papers, not only 60-page monoliths, when
    the statement is clean and the simplicity is real.
  - **Self-check:** if your paper's virtue is simplicity, does the introduction claim
    it plainly and compare proof lengths honestly?

---

## By technique (each cell is a verified paper above)

| Technique | Verified COLT exemplar | Edition / PMLR vol:pages |
| --- | --- | --- |
| Minimax / sequential symmetrization framework | Rakhlin, Sridharan & Tewari | 2011 / v19:559-594 |
| Constraint-priced regret analysis | Jain, Kothari & Thakurta | 2012 / v23:24.1-24.34 |
| Stochastic-gradient escape analysis (non-convex) | Ge, Huang, Jin & Yuan | 2015 / v40:797-842 |
| Problem-posing with explicit target rates | Agarwal et al. (Open Problem) | 2017 / v65:4-7 |
| Oracle-based online learning construction | Kozachinskiy & Steifer | 2024 / v247:3241-3256 |

---

## Omitted after checking (do not attribute to COLT without re-verification)

- **"Optimal Multi-Distribution Learning" (v247:5220-5223)** — the page range is only
  four pages, suggesting an extended-abstract or open-problem-adjacent form; omitted
  from the exemplar rows rather than characterized without opening the paper.
- Classic bandit results often mis-shelved at COLT (e.g., UCB analyses, the
  adversarial-bandit EXP3 line) largely live in **journals or pre-PMLR proceedings**;
  COLT proceedings appear in PMLR only from v19 (2011) onward, so pre-2011 COLT
  papers cannot be verified by PMLR volume at all — cite their actual venue.
- Any paper known only by folklore attribution ("I think that was a COLT paper") —
  match it on proceedings.mlr.press first, or add it here as 待核实 with no
  attribution.

Before adding a row: confirm the volume's landing page names the Conference on
Learning Theory and the edition year, record authors/pages, update the access-date
header, and when in doubt, omit.
