---
name: soda-writing-style
description: Use when writing or revising a SODA (ACM-SIAM Symposium on Discrete Algorithms) paper — headline bounds stated exactly, the title-page abstract that wins bidding, a first-ten-pages overview for triage readers, prior-bound comparison tables, and prose discipline for an uncapped full-version document.
---

# SODA Writing Style

SODA prose serves two readers with opposite budgets: a PC member triaging a
record-size pool who gives you minutes, and a subreviewer in your exact niche who
gives you days. The uncapped format (no page limit, full version encouraged —
2027 CFP, checked 2026-07-08) means you never trade completeness for space; the
craft is entirely in *layering*, so the minutes-reader and the days-reader each
get a document built for them.

## The headline bound

An algorithms paper is quoted by its bound, so engineer the quotable sentence:

- State it with exact parameters: "a deterministic `O(m log^2 n)`-time algorithm
  for weighted global min-cut," not "a faster deterministic algorithm."
- Pair it immediately with the displaced bound: "improving the
  `O(m log^4 n)` bound of [X, SODA 2019]." New readers calibrate by the delta.
- If randomization, approximation, or model caveats qualify the bound, they
  appear *in the same sentence* — a caveat discovered on page 30 reads as
  concealment.
- Resist rounding up: "near-optimal" claims invite the referee to construct the
  regime where you are not.

## The title-page abstract

SODA submissions open with a title page: title plus a one-to-two-paragraph
abstract of the contributions (2027 CFP). This abstract is the PC's bidding
surface — it decides *who* reviews you. Structure that has survived contact:

```text
Paragraph 1 (the result):
  Problem, model, headline bound, displaced prior bound, and the
  open-problem citation if one exists. Numbers, not adjectives.

Paragraph 2 (the technique):
  The one new idea, named concretely ("a recursive sparsifier that
  tolerates deletions"), plus why known approaches get stuck —
  one sentence each. This paragraph recruits the right expert.
```

## First ten pages: the overview contract

Everything after the overview is verification; the overview itself must let a
non-specialist theorist reconstruct *why the result is true* at cartoon
resolution. Ingredients, in order of most common omission:

1. **Barrier paragraph** — what specifically stops the previous technique.
   Papers that skip this get "incremental" reviews from readers who cannot see
   why the improvement was hard.
2. **Technique narrative with a running example** — a small concrete instance
   walked through the new algorithm beats three pages of notation.
3. **Proof roadmap** — lemma dependency sketch, so the back matter reads as
   planned architecture (`soda-supplementary`).
4. **Comparison table** — see below.

## The prior-bound table

Algorithms referees expect the lineage as a table and will reconstruct it if you
do not provide it — on their terms, not yours:

| Reference | Bound | Deterministic? | Model / caveat |
|---|---|---|---|
| [Karger-era result] | `O(m log^3 n)` | randomized | Monte Carlo |
| [previous best] | `O(m log^4 n)` | deterministic | — |
| **This paper** | `O(m log^2 n)` | deterministic | — |

Rules: cite the *strongest* version of each prior result (journal version if it
improved), include the inconvenient rows, and footnote incomparable results
rather than omitting them.

## Prose discipline for long documents

- **Uncapped is not unedited.** Every page must still earn verification effort;
  padding multiplies referee fatigue and referee fatigue reads as doubt.
- One notation system, declared once. Re-derivations of standard facts get a
  citation, not a subsection.
- Theorem statements are self-contained: model, input restrictions, and
  probability regime inside the statement, never "under the assumptions of
  Section 2" (referees quote theorems out of context; make that safe).
- Lemmas get names in comments ("the charging lemma") — PC discussion happens in
  nicknames, and you want yours to have them.
- Third-person self-citation throughout (lightweight double-blind,
  `soda-submission`), but keep the citations present.

## Titles that survive PC compression

The title is the unit of memory in deliberation and in citation. Patterns,
with fictional examples:

| Pattern | Fictional example | When it fits |
|---|---|---|
| Bound-carrying | "Dynamic Interval Stabbing in Polylogarithmic Worst-Case Time" | The bound is the news — the default SODA choice |
| Barrier-breaking | "Breaking the sqrt(n) Barrier for Online Recoloring" | A named threshold falls; use only if prior work called it a barrier |
| Problem-resolving | "The Communication Complexity of Threshold Joins" | You close the problem (up to stated factors) |
| Technique-forward | "Deletion-Tolerant Sparsifiers and Their Applications" | Only when the tool provably outlives the application |
| Question title | "Is Sorting by Prefix Swaps Fixed-Parameter Tractable?" | Rare; only if the answer is surprising |

Anti-patterns: pun-first titles (unquotable in a review), "Towards..." (admits
incompleteness), "A New Approach to..." (contains zero information), and
stacked qualifiers that belong in the theorem, not the marquee.

## Register calibration

| Overclaim | Calibrated version |
|---|---|
| "We settle the complexity of X" | "We resolve the deterministic time complexity of X up to `log log n` factors" |
| "Our technique is completely new" | "We are not aware of prior uses of deletion-tolerant sparsification in this setting" |
| "Experiments confirm our algorithm is practical" | "A preliminary implementation (not part of our claims) suggests the constants are moderate" |
| "It is easy to see" (×20) | Prove it once; "routine calculation, included for completeness, in Appendix D" |

## Output format

```text
[Style verdict] Submission-grade / Needs revision / Needs restructuring
[Headline audit] <bound stated exactly? caveats co-located? displaced bound named?>
[Abstract audit] <bidding-surface quality; expert-recruiting technique sentence present?>
[Overview audit] <barrier, running example, roadmap, table — which are missing>
[Register flags] <overclaims with suggested calibrated rewrites>
```
