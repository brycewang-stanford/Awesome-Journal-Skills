# SODA Exemplars Library (problem-lane × technique)

> **Verified via web search, access date 2026-07-08.** Every entry below was checked
> against SIAM epubs proceedings records (`epubs.siam.org`, DOI prefix `10.1137/1.978...`)
> and/or institutional award announcements, confirming it appeared at the **ACM-SIAM
> Symposium on Discrete Algorithms** specifically. Four verified entries beat a dozen
> guessed ones; anything uncheckable was left out on principle.
>
> **Sibling-confusion guard:** the theory literature's most famous results are scattered
> across SODA, STOC, FOCS, ESA, ICALP, and journals (SICOMP/JACM), and many papers exist
> in *both* a conference and a journal version with different bounds. "I remember it was
> at SODA" is not attribution — dblp plus the SIAM epubs DOI is. When both versions exist,
> the journal version usually carries the strongest bound (see `../../skills/soda-related-work/SKILL.md`).
>
> **Zero-hallucination rule:** this library gives design positioning only. It states no
> theorem parameters, constants, or proof details beyond what titles and award pages
> assert — read the papers on epubs/arXiv before citing anything technical.

## How to use this library

Each exemplar demonstrates the SODA shape identified in
[`../../skills/soda-topic-selection/SKILL.md`](../../skills/soda-topic-selection/SKILL.md):
**a named problem, a stuck quantitative frontier, and discrete technique that moves it.**
Pick the lane nearest your draft, then ask the lane's self-check question before
declaring your paper SODA-shaped.

## Verified exemplars

### Numerical-combinatorial boundary: linear-system solving

- **Peng & Vempala, "Solving Sparse Linear Systems Faster than Matrix Multiplication,"
  SODA 2021, pp. 504-521.** Verified: `epubs.siam.org/doi/10.1137/1.9781611976465.31`;
  SODA 2021 **Best Paper Award** per the Georgia Tech ACO announcement
  (`aco.gatech.edu`).
  - **Why it is SODA-shaped:** a barrier everyone could name (matrix-multiplication
    time as the default cost of exact linear algebra) crossed for a concrete input
    class (sparse systems), by mixing randomized and algebraic tools.
  - **Self-check:** can you name, with a citation, the default bound your paper makes
    non-default — and the input class where you beat it?

### Graph algorithms: derandomization of a celebrated bound

- **Henzinger, Li, Rao & Wang, "Deterministic Near-Linear Time Minimum Cut in Weighted
  Graphs," SODA 2024, pp. 3089-3139.** Verified:
  `epubs.siam.org/doi/10.1137/1.9781611977912.111`; SODA 2024 Best Paper co-winner
  (reported by Google Research's announcement).
  - **Why it is SODA-shaped:** the purest "problem with a bound" — take a landmark
    randomized guarantee and deliver it deterministically at near-linear time in the
    weighted setting. The contribution sentence needs no adjectives, only qualifiers
    (deterministic, near-linear, weighted).
  - **Self-check:** is every qualifier in your headline sentence (deterministic?
    weighted? worst-case?) doing real work against a specific prior result?

### Algorithmic game theory / social choice: moving a stuck constant

- **Charikar, Ramakrishnan & Wang (author order per proceedings: 待核实), "Breaking the
  Metric Voting Distortion Barrier," SODA 2024.** Verified as SODA 2024 Best Paper
  co-winner via the Stanford CS department announcement (`cs.stanford.edu`); pages/DOI:
  待核实 on epubs before formal citation.
  - **Why it is SODA-shaped:** the frontier is a *constant* (a distortion ratio), stuck
    and named as a barrier by the community — evidence that SODA progress need not be
    asymptotic in `n`, only genuinely stuck beforehand.
  - **Self-check:** if your improvement is "small" (a constant, a log), can you cite
    who tried and where the previous technique provably stalls?

### Coding theory: parameter frontier in an adjacent lane

- **Srivastava, "Improved List Size for Folded Reed-Solomon Codes," SODA 2025,
  pp. 2040-2050.** Verified: `doi.org/10.1137/1.9781611978322.64`; SODA 2025 **Best
  Paper (shared) and Best Student Paper** per the DIMACS announcement
  (`dimacs.rutgers.edu`); SODA 2025 = New Orleans, January 12-15, 2025.
  - **Why it is SODA-shaped:** coding theory lives at SODA when the contribution is a
    combinatorial/algorithmic parameter (here, list size) rather than an
    information-theoretic or engineering one — a model for judging "is my adjacent
    field's paper a SODA paper?" by *which quantity moves*.
  - **Self-check:** is the quantity you improve one that the algorithms community
    tracks, and is a single author-facing table enough to show the movement?

## Lane × technique summary

| Lane | Exemplar | Cycle | Frontier moved |
|---|---|---|---|
| Numerical/algebraic algorithms | Peng & Vempala | 2021 | Sparse linear systems vs. matrix-multiplication time |
| Graph algorithms | Henzinger, Li, Rao & Wang | 2024 | Deterministic weighted min-cut to near-linear time |
| Social choice / AGT | Charikar, Ramakrishnan & Wang | 2024 | Metric voting distortion constant |
| Coding theory | Srivastava | 2025 | Folded Reed-Solomon list size |

Four lanes, four best-paper-level anchors, one shared skeleton: *named problem, stuck
frontier, quantitative movement, discrete technique.*

## Adding entries: the verification recipe

1. Locate the paper on dblp (`dblp.org/db/conf/soda/`) — confirms the venue and year.
2. Find the epubs record and note pages + DOI under the correct volume prefix
   (`10.1137/1.9781611976465` = 2021, `...977912` = 2024, `...978322` = 2025,
   `...978971` = 2026).
3. For award claims, require an institutional or SIAM source — a tweet is a lead,
   not a citation.
4. Record the access date; if any leg fails, add the entry as 待核实 with no
   attribution, or leave it out. Do not "remember" venues — the SODA/STOC/FOCS
   boundary is exactly where memory misattributes.
