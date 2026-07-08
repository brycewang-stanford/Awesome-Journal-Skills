---
name: stoc-writing-style
description: Use when drafting or revising a STOC (ACM Symposium on Theory of Computing) paper — the theorem-forward first page, informal/formal statement pairing, the technical-overview section that carries acceptance, notation economy for a cross-area committee, and prose that survives the twelve guaranteed pages.
---

# STOC Writing Style

A STOC submission is read by two different people you must satisfy at once: a
program-committee member from a neighboring sub-area deciding whether the result
is a big deal, and a specialist subreviewer deciding whether it is true. STOC's
reading contract (abstract + table of contents + first twelve pages guaranteed;
STOC 2026 CFP, checked 2026-07-08) forces both conversations into the same
window. The house style below is how successful papers manage that.

## The first page: theorem before context

Theory flagship papers state the result almost immediately, then earn it.
The standard device is the informal/formal pair:

```latex
\begin{theorem}[Main result, informal]\label{thm:main-informal}
Every $n$-vertex planar graph admits a spanning structure of weight
$O(\log n)$ times optimal, computable in near-linear time.
\end{theorem}
% Section 2 then states Theorem 2.1, the formal version with the exact
% model, the constant regime, and the failure probability — and the text
% says explicitly: "Theorem 1.1 is the special case of Theorem 2.1 with
% \epsilon = 1/2."
```

Rules for the pair: the informal statement may simplify but must not lie (no
hidden model changes, no suppressed hypotheses that reverse the interest of the
result); and the formal statement must be findable from it in one hop.

## The technical overview is the paper

Modern STOC papers devote two to four of the twelve pages to a section titled
"Technical Overview" or "Our Techniques." This is where acceptance is decided:

- Narrate the proof as a sequence of *obstacles and moves*: what the natural
  approach is, exactly where it breaks, and what new idea gets past the break.
- Attribute honestly inside the overview — "steps 1–2 follow [XY]; the novelty
  is step 3" reads as confidence, and subreviewers will reconstruct the
  attribution anyway.
- Use one running example or one figure if the construction is geometric;
  cross-area readers hold pictures longer than notation.
- The overview must be faithful to the real proof. An overview describing last
  month's broken strategy while the appendix executes a different one is a
  correctness flag reviewers specifically look for.

## Notation economy

| Habit | Why it matters at STOC |
|---|---|
| Introduce notation at first use, never in a front-loaded glossary dump | Cross-area PC members drop off during page-2 symbol walls |
| Prefer words for one-off concepts ("the heavy vertices") over fresh symbols | Every symbol is a tax on the non-specialist reader |
| State parameter regimes next to results, not in a global convention | "Throughout, $\varepsilon < 1/\log n$" declared on page 3 and used on page 40 will be missed |
| Reserve display math for statements that get referenced | Inline-display balance is how twelve pages stay readable |
| Standard names for standard things | Renaming expanders or conductance costs goodwill and space |

## Sentence-level house norms

- Claims are exact: "we give a $1.99$-approximation" not "we significantly
  improve the approximation ratio." Theory readers convert vague claims to the
  weakest consistent reading.
- "To the best of our knowledge" once, if ever; a related-work section that
  actually knows the literature (`stoc-related-work`) does this job.
- Open problems at the end are a genre convention and a service: two or three
  crisp questions, each with its parameterization pinned down.
- Under double-blind (in force for STOC 2026), self-reference goes third
  person: "extending the technique of [12]" even when [12] is you.

## Budgeting the twelve pages

A workable allocation for a single-result paper: one page of introduction and
main statement; one to two pages of context, related work, and open problems;
two to four pages of technical overview; the remainder for preliminaries plus
the proof spine of the main theorem, with routine steps deferred under the
pointer discipline of `stoc-supplementary`. Two smells that the budget failed:

- **Preliminaries bloat** — three pages of imported definitions before anything
  new happens. Compress by citing standard sources and defining only what the
  overview needs.
- **Statement crowding** — eight theorems in the window, none proved there.
  Committees prefer one theorem they believe over eight they must take on
  faith; demote secondary results to a single summarizing paragraph.

## Titles and abstracts, theory register

- Titles state the result when the result is statable: "Undirected
  ST-Connectivity in Log-Space" is the genre's ideal — problem plus resource
  bound, no verbs of enthusiasm. Technique-forward titles ("... via Lazy
  Hierarchies") are the accepted alternative when the technique is the story.
- Self-deprecating precision is house-respected: a title admitting the
  improvement is slight, with the barrier story carried inside, reads as
  confidence (see the exemplars library for a Best Paper that did exactly
  this).
- The abstract carries exact bounds and models, because theory abstracts are
  read as claims: any constant, exponent, or model qualifier in the abstract
  is quotable and will be quoted.
- No citations in the abstract by convention; name prior bounds ("improving
  the best known $O(\log^2 n)$") and cite in the introduction.

## Revision passes that pay at this venue

1. **The skim pass:** read only the abstract, ToC, section heads, and theorem
   statements. Is the contribution and its scale unambiguous? That is the
   five-minute PC read.
2. **The skeptic pass:** at every "clearly," "standard," and "it follows,"
   either write the missing sentence or verify a graduate student could.
3. **The breadth pass:** find the three sentences a distributed-computing (or
   crypto, or quantum) PC member needs to care; make sure they exist on page 1.
4. **The consistency pass:** every constant, exponent, and model detail in the
   abstract must match the formal statements exactly — abstract inflation is
   the most commonly caught overclaim.

## Cycle-volatility warnings

- The guaranteed-read geometry (and hence all page budgeting above) follows the
  current CFP; the window was 10 pages in earlier cycles and 12 in 2026
  (待核实 each year).
- Anonymization phrasing rules apply only in double-blind cycles; confirm the
  live policy before rewriting self-references.

## Output format

```text
[First-page verdict] theorem-forward / buried lede <- fix
[Overview quality] obstacles-and-moves / summary-only <- rewrite
[Notation audit] <symbols to cut, regimes to localize>
[Budget] <pages per role; bloat or crowding found>
[Skim-pass result] <what a 5-minute reader takes away>
```
