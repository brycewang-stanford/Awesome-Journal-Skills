---
name: pldi-writing-style
description: Use when revising a PLDI draft for the venue's voice — design insight before tool name, mechanisms instead of adjectives, a running example that carries the semantics, honest limitation statements, and prose that fits the single-column acmsmall journal format without padding toward the page cap.
---

# PLDI Writing Style

A PLDI paper is an engineering argument written for people who will try to break
it. The style that survives has three habits: it states the *hard case* before
the solution, it explains *mechanisms* rather than accumulating adjectives, and
it scopes every claim to exactly what the evaluation shows. Since the PACMPL
switch, the published object is a journal article in single-column `acmsmall` —
roomier lines than the old two-column look, but the same conference-grade cap on
text pages, so the format rewards clarity, not length.

## The first-page contract

By the end of page one a reviewer should be able to answer four questions:

1. **What breaks today?** The concrete program, workload, or proof burden that
   existing techniques mishandle — shown, ideally, as a small code example.
2. **What is the insight?** One sentence a compiler writer could act on
   ("summarize modules by polymorphic escape signatures"), not a property wish
   ("fast and precise").
3. **Does it exist?** The implementation substrate — which compiler, which IR,
   which proof assistant.
4. **What is the headline evidence?** The number, with its suite and baseline
   attached, plus the paper's stated limit.

The worked rewrite in `resources/worked-examples/01-introduction.md` performs
this transformation end to end.

## Style table: draft reflex → PLDI voice

| Draft reflex | PLDI voice |
|---|---|
| "Our novel framework significantly outperforms..." | "On suite S, T improves geomean runtime 1.17x over B at -O2 (30 runs, 95% CI)" |
| Tool name in the title, insight in §4 | Insight in the title and abstract; the tool demonstrates it |
| Related work as a guided museum tour | Each cited line ends with the delta from *this* paper (`pldi-related-work`) |
| Limitations paragraph as an apology in §8 | Restrictions stated where introduced, with their cost measured |
| Semantics by prose | Judgments, figures, and a running example threaded through §3-§5 |
| Padding toward the cap | Whitespace returned; reviewers never reward a full 20 pages for its own sake |

## The running example discipline

Pick one small program that exhibits the hard case and reuse it everywhere: to
motivate (§1), to walk the semantics (§3), to show the transformation (§4), and
as the first row of the evaluation (§6). One example that a reviewer can trace
end-to-end beats five disconnected snippets — and it is the cheapest insurance
against the "I could not follow the analysis" review.

## Claim ledger

Before the final pass, extract every claim sentence and demand its evidence
address:

```text
CLAIM                                    -> EVIDENCE
"sound modulo first-class continuations" -> Thm 2 (§5) + restriction check (§4.4)
"majority of closures stack-allocated"   -> Table 3, 11/14 programs
"under 3% compile-time overhead"         -> Table 5, 30 timed builds, CI
"no whole-program pass required"         -> §4.2 construction, artifact demo
```

Any claim without an address gets weakened or cut; any evidence without a claim
is a candidate for the supplement (`pldi-supplementary`).

## Sentence-level habits

- Present tense for the system's behavior, past tense for the experiments run.
- Name concrete infrastructure ("an LLVM 18 pass", "a Rocq development of 12k
  lines") — abstraction here reads as evasion.
- Kill the "increasingly popular/important" opener; start at the hard case.
- Define notation once, in a figure, before first use; PLDI reviewers cite
  notation drift as a soundness smell, not a typo.

## Output format

```text
[First-page contract] hard case / insight sentence / substrate / headline number: each present?
[Running example] one program threaded through §1-§6? yes/no
[Claim ledger] n claims, n addressed, list the orphans
[Tone flags] adjectives standing in for mechanisms; apology-style limitations
[Cut list] <sections/paragraphs to compress before the cap does it for you>
```
