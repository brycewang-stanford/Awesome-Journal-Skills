---
name: osdi-writing-style
description: Use when drafting or revising an OSDI paper's prose and structure — building the pain → abstraction → mechanism → measurement narrative, fitting it into the 12-page reviewed body with no appendix escape hatch, and writing for a PC told to down-rank padded papers and given no rebuttal to clarify with.
---

# OSDI Writing Style

Shape the paper the way OSDI reviewers read. Format numbers below are the OSDI '26
rules (12 reviewed pages including figures and tables, unlimited references, no
appendices at submission — verified 2026-07-08); recheck the live CFP before trusting
any of them for a later cycle.

## The narrative arc

An OSDI paper is an argument that a design decision was right, carried by a built
system. The arc, section by section:

1. **Pain** — something operational breaks, stalls, or costs money, and the trend
   makes it worse. Not "X is important."
2. **Why existing designs cannot fix it** — each plausible alternative dispatched
   with a mechanism-level reason. In a no-response cycle this paragraph is your
   rebuttal, delivered in advance.
3. **The idea, named** — one abstraction, principle, or mechanism another builder
   could reuse, stated in a sentence a reviewer could repeat in the PC meeting.
4. **The design that realizes it** — decisions justified against the idea, with the
   trade-offs admitted where they are made, not in a limitations afterthought.
5. **The system that exists** — implementation reality: lines, language, what is
   real versus mocked.
6. **Measurements that answer questions** — evaluation organized by research
   question, each answered by an experiment (see `osdi-experiments`).

The worked rewrite in
[`../../resources/worked-examples/01-introduction.md`](../../resources/worked-examples/01-introduction.md)
executes this arc on a fictional storage system; the verified papers in
[`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) execute
it for real.

## Writing under the 12-page regime

Two 2026 rules jointly define the discipline:

- **No appendices in the submission.** References are unlimited, but everything
  reviewers may weigh lives in the 12 pages. There is no "details in Appendix B"
  move — either the detail earns body space or the paper must be convincing without
  it.
- **Padding is penalized, not just wasted.** The CFP tells authors the paper should
  be "the right length," possibly under 12 pages, and tells reviewers to down-rank
  overly padded papers. Twelve pages is a cap, not a target.

Practical consequences:

| Draft habit | Under OSDI '26 rules | Replacement |
|---|---|---|
| "See appendix for proof/protocol" | Nothing to point at | Compress the invariant into the body or cut the claim |
| Restating results in intro, design, and eval | Down-rank bait | Say each result once, where it lands hardest |
| Screenshot-quality figure walls | Page cost without argument | One figure per claim; captions that state the takeaway |
| Ten-line contribution bullet lists | First-page budget burned | Three claims a reviewer can test |
| Related-work essay | Crowds out the design | Positioning by difference (see `osdi-related-work`) |

## Sentence-level habits of accepted systems prose

- **Numbers carry their context.** "3.2x faster" is meaningless until the baseline,
  workload, and cost ride in the same sentence.
- **Agency stays with the design.** "Ledger bounds recovery" not "recovery is
  bounded" — passive voice hides which component does the work.
- **Trade-offs are sentences, not subordinate clauses.** "This costs 11% write
  amplification" standing alone reads as honesty; buried mid-sentence it reads as
  concealment.
- **Present tense for the system, past tense for the experiments.** The system *is*;
  the runs *were*.
- **No unresolved forward references.** With no rebuttal, a reviewer confused on page
  4 stays confused into the PC meeting.

## Mechanical format anchors (2026 cycle)

```text
Body:        <= 12 pages, single-spaced, 8.5" x 11", incl. figures & tables
References:  unlimited pages, excluded from the 12
Appendices:  NOT permitted in the submission (final papers: allowed, 14pp body)
Type:        10-point Times-like font on 12-point leading
Layout:      two columns, text block 7" wide x 9" deep
Anonymity:   authors AND institutions anonymized (see osdi-submission)
```

Use the current USENIX template unmodified. Space is recovered by cutting argument
redundancy — never by geometry, font, or leading tricks that chairs detect
mechanically and treat as violations.

## The abstract in seven sentences

OSDI abstracts follow the arc in miniature; a reliable skeleton:

1. The operational pain, with its worsening trend.
2. Why the standard fixes fail (one clause each is enough here).
3. "We present <System>," plus the named idea in the same sentence.
4. The mechanism that realizes the idea, one sentence.
5. The trade-off, admitted plainly.
6. Build fact + evaluation anchor: what was built, measured against what, on what.
7. The headline result *with its cost attached*.

Sentence 5 is the one first drafts omit and the one that most changes how a triage
reviewer scores honesty. The worked example shows the skeleton filled in.

## Revision passes, in order

1. **Arc pass** — can a reader reconstruct pain → gap → idea → evidence from section
   openers alone?
2. **Objection pass** — list the five likeliest reviewer objections; verify each is
   answered in the text, since no response period will exist to answer it later.
3. **Claim audit** — every superlative gets a number; every number gets a baseline,
   a workload, and a cost.
4. **Compression pass** — cut to the right length; hunt duplicated explanation,
   decorative figures, and throat-clearing openers.
5. **Cold read** — a colleague outside the project reads pages 1–2 and states the
   contribution back; if they name the wrong idea, rewrite the front, not them.

## Output format

```text
[Arc] intact / broken at: <pain|gap|idea|design|build|eval>
[Named idea] <the one-sentence reusable claim, quoted from the draft>
[Padding risk] low / medium / high + worst offender section
[Unanswered objections] <list — each is a rebuttal you will never get to make>
[Page verdict] current length vs "right length" judgment
[Rewrite order] <ordered list of passes still needed>
```
