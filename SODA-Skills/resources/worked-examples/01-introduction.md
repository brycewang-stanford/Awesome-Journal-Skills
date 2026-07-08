> **Illustrative teaching example.** The paper, problem, bounds, and every citation
> tag below are **fictional**, constructed only to demonstrate SODA front-matter
> craft. No real result is described and no venue policy is invented. Companion
> skills: [`soda-writing-style`](../../skills/soda-writing-style/SKILL.md),
> [`soda-topic-selection`](../../skills/soda-topic-selection/SKILL.md),
> [`soda-supplementary`](../../skills/soda-supplementary/SKILL.md).

# Worked Example: A SODA Title-Page Abstract + Overview Opening (before → after)

The exercise: the same fictional result — a faster dynamic data structure —
written first as a page-capped-venue draft, then rebuilt for SODA's two readers
(the bidding PC member with minutes, the niche subreviewer with days) and SODA's
uncapped full-version format.

**Fictional paper:** *"Dynamic Interval Stabbing with Polylogarithmic Worst-Case
Updates."* Fictional frontier: prior structures needed `O(sqrt(n))` worst-case
update time; amortized polylog was known; worst-case polylog was open.

---

## Before (imported habits; would bid and review badly at SODA)

> **Abstract.** Interval stabbing is a fundamental problem in computational
> geometry with many applications in databases, networking, and scheduling. We
> present a novel framework based on hierarchical decomposition that significantly
> improves the update time of dynamic interval stabbing structures. Our approach
> is general and we believe it will find many further applications. Experiments
> show our structure is practical. Due to space constraints, most proofs are
> deferred to the full version.
>
> **1. Introduction.** Interval data is everywhere... [one page of application
> stories] ... Our framework has three conceptual layers, which we now describe
> at a high level before giving details in the appendix.

**Faults, keyed to the skills:**

- **No bound anywhere.** Neither the new `polylog` nor the displaced `O(sqrt(n))`
  appears; the abstract is unquotable and unbiddable (`soda-writing-style`:
  headline-bound rules). "Significantly improves" is an adjective doing a
  number's job.
- **Framework-first framing.** "Novel framework ... further applications" invites
  the SODA question *what does it buy?*; the problem lineage should lead
  (`soda-topic-selection`: framing).
- **"Deferred to the full version"** — a template fossil from capped venues. SODA
  submissions *are* the full version; the phrase advertises an incomplete record
  (`soda-supplementary`).
- **Experiments claimed in the abstract** without a claim class — at SODA,
  "practical" in the abstract must be either a claim (with protocol) or absent
  (`soda-experiments`).
- **Barrier unexplained.** Why was worst-case `polylog` hard if amortized was
  known? A referee who can't see the obstruction writes "incremental."

---

## After (SODA arc: problem → stuck frontier → bound → obstruction → technique)

> **Abstract.** In dynamic interval stabbing, a set of `n` intervals on the line
> undergoes insertions and deletions, and a query asks for an interval containing
> a given point. Worst-case update time has been stuck at `O(sqrt(n))` since
> [AB09], although `O(log^2 n)` *amortized* updates are known [CD14]; closing
> this gap was posed as an open problem in [CD14] and again in the survey [E21].
> We give a structure with `O(log^3 n)` worst-case update time and `O(log n)`
> query time, resolving the question up to a `log` factor. Matching the amortized
> bound exactly remains open.
>
> The obstruction to de-amortizing [CD14] is that its rebuild phases move
> `Theta(n)` intervals at once; standard rebuild-spreading fails because
> stabbing queries must remain correct *mid-rebuild*. Our main tool is a
> **two-generation overlay**: queries are answered from the union of an aging
> structure and its half-built successor, and a charging argument (Lemma 4.1)
> bounds the overlay's query overhead by `O(log n)` at every time step.
>
> **1.1 The frontier.** [table follows]
>
> | Reference | Update (worst-case) | Update (amortized) | Query |
> |---|---|---|---|
> | [AB09] | `O(sqrt(n))` | — | `O(log n)` |
> | [CD14] | `Theta(n)` rebuilds | `O(log^2 n)` | `O(log n)` |
> | **This paper** | `O(log^3 n)` | same | `O(log n)` |

**Why this now works at SODA:**

- **Quotable in one line** — "worst-case polylog dynamic interval stabbing" — and
  the delta is auditable from the abstract alone: `O(sqrt(n))` → `O(log^3 n)`,
  with the open-problem citations attached. Paragraph 1 wins the bid.
- **Paragraph 2 recruits the right expert**: it names the obstruction
  (mid-rebuild correctness) and the new idea (two-generation overlay, with its
  key lemma number) — the technique sentence a data-structures subreviewer
  bids on.
- **Honest edges**: the residual `log` gap is stated in the abstract, converting
  a referee's "gotcha" into the paper's own open problem.
- **The table replaces prose lineage** and includes the inconvenient amortized
  column — dominance is claimed only where it holds
  (`soda-related-work`: incomparability discipline).
- **No deferred proofs, no unclaimed practicality**: the uncapped submission
  contains every proof, and experiments either appear later with a claim-class
  label or not at all.

---

## Transfer checklist (apply to your own front matter)

1. Does the abstract contain both bounds — yours and the displaced one — with
   open-problem citations if they exist?
2. Can a non-expert say in one sentence why the previous technique gets stuck?
3. Is the new tool named concretely enough to be discussed by nickname in PC
   deliberation?
4. Does a frontier table appear within the first two pages, with the
   inconvenient rows kept?
5. Is any residual gap stated by you, before a referee states it?
