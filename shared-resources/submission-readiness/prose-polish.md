# Prose Polish — claim-to-evidence audit and house-style pass

Stage 3 of the submission-readiness pipeline, run after the referee panel has settled what
the paper can claim. Mechanics are already clean (preflight), substance is settled (panel),
so this pass makes the text say exactly what the evidence supports, in the venue's register.

> **Suggest, never silently rewrite.** Every change is proposed as before → after with a
> reason and a location. Never change a number, an estimate, a citation, or a claim's
> scope without the author agreeing; never invent a result to make a sentence work.

## Inputs

1. The manuscript (and the preflight JSON, so number mismatches are not re-reported).
2. The panel's verified concerns (claims a referee said are unsupported are fixed here).
3. The target pack's `*-writing-style` (or `*-writing`, `*-abstract`, `*-introduction`)
   skill — the venue's house style is read from there, not assumed.

## Pass 1 — Claim-to-evidence audit (do this first)

Extract every **claim sentence** from the title, abstract, introduction and conclusion: a
sentence asserting a finding, a magnitude, a mechanism, a generality, or a novelty. For each:

| Column | What to record |
|---|---|
| Claim | The sentence (shortened) and its location |
| Evidence | The exhibit/section that supports it (Table 2 col 3, §5.2, Figure 4) |
| Strength | `supported` · `stronger than evidence` · `unsupported` · `contradicted` |
| Fix | The minimal rewrite that makes claim = evidence |

Rules of thumb the audit applies:
- **Causal verbs need a causal design.** "causes", "leads to", "drives", "the effect of"
  require an identification strategy the paper defends; otherwise "is associated with".
- **Generality needs breadth.** "LLMs", "firms", "patients" from one model/country/site
  → scope the noun ("in our sample of …").
- **Novelty claims need a search.** "first to" survives only if the related-work section
  shows why the closest papers do not already do it; prefer "to our knowledge, the first …"
  plus the distinguishing feature.
- **Mechanism claims need a mechanism test**, not only consistency with one.
- **Abstract ⇄ conclusion ⇄ results must agree** on direction, magnitude and scope.
- **Statistical language**: no "significant" without saying statistically or
  economically/clinically; effect sizes with uncertainty (CI/SE), not stars alone.

## Pass 2 — First-page test

Within the first page (economics/management: first ~3 pages of the introduction), a reader
should find: the question · the answer · the magnitude in interpretable units · why it is
credible · why it matters to this venue's readers. Report which of the five are missing or
buried, and propose the reordered paragraph.

## Pass 3 — Title and abstract against house style

Read limits and conventions from the venue (preflight already enforced hard limits):
structured vs unstructured abstract, word budget, whether the abstract states numbers,
title length and style (declarative vs descriptive; colons; acronyms), keywords/JEL fit.
Give one recommended title and at most two alternatives, each with the convention it
follows.

## Pass 4 — Consistency and clarity

- **Terminology**: one name per construct, variable, dataset, method across text, tables
  and figures (e.g. "treated firms" vs "exposed firms" vs "pilot firms").
- **Exhibit language**: the text describes each exhibit with the same sign, units and
  sample as the exhibit's notes.
- **Paragraph discipline**: topic sentence first; one idea per paragraph; signpost
  sentences at section starts.
- **Hedging balance**: remove stacked hedges ("may potentially suggest"), but keep the
  hedges the evidence needs.
- **Register by family**: economics — first person plural, present tense for findings;
  clinical — past tense for results, IMRaD terminology, no causal language for
  observational designs; ML — contribution bullets in the introduction, precise metric
  names; Chinese journals — formal academic register (avoid colloquial phrasing and
  publicity-style slogans), and standardised use of "本文" and "研究发现".

## Output format

```
【Claim audit】n claims · supported a · stronger-than-evidence b · unsupported c · contradicted d
  C1 [abstract] "X causes Y" — evidence: Table 3 (correlational) — fix: "X is associated with Y …"
  …
【First-page test】question ✓ answer ✓ magnitude ✗ (buried at p.6) credibility ✓ relevance ✗
【Title / abstract】recommended title …; abstract edits (before → after)
【Consistency】term collisions: "pilot" vs "treated" (§3, Table 2) → use "pilot" throughout
【Edit list】ranked; each: location · before → after · reason · owner skill
```

## Hard rules

1. Every edit has a location and a reason; none changes a number or scope silently.
2. Fix unsupported claims by narrowing the claim, never by asserting new evidence.
3. House style comes from the target pack, not from generic advice.
4. Preserve the author's voice; polish is subtraction and precision, not rewriting.
