---
name: duke-mathematical-journal
description: Use when targeting Duke Mathematical Journal (Duke Math. J.) or deciding whether a pure mathematics manuscript fits this top-tier broad-scope Duke University Press venue. Encodes the journal's fit, framing, proof standard, house style, official-submission re-check, and desk-reject heuristics.
---

# Duke Mathematical Journal (duke-mathematical-journal)

## Journal positioning

Duke Mathematical Journal, published by Duke University Press, is one of the leading general journals in pure mathematics, with a long-standing reputation for publishing deep, high-quality research across the full range of mathematical fields. Its defining character is depth at top-tier breadth: Duke publishes results of major significance from algebra, geometry, topology, number theory, analysis, dynamics, and mathematical physics, and is regarded as sitting near the very top of the general-journal hierarchy. The journal rewards substantial, conceptually significant theorems and methods presented with full rigor; it is not a home for routine extensions or narrowly technical notes.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the Duke Mathematical Journal site (Duke University Press) and confirm submission procedures.

## When to trigger

- The author is considering Duke Mathematical Journal for a deep, significant pure-mathematics paper.
- A result is of major significance and the author is choosing among Duke, `annals-of-mathematics`, and `inventiones-mathematicae`.
- A strong paper spans sub-fields or sits in a core area (number theory, geometry, analysis) where Duke has particular strength.
- The author needs Duke's significance and rigor bar, plus common rejection reasons, before submission.

## Scope & topic fit

- Pure mathematics across all major areas: number theory and arithmetic geometry, algebraic and differential geometry, topology, representation theory, analysis and PDE, probability, dynamical systems, mathematical physics.
- Deep theorems of major significance and methods whose impact reaches across sub-areas.
- Results that resolve substantial open questions or build new theory in a core mathematical field.
- Work bridging sub-fields at a high level of depth and significance.
- Survey or purely expository work is not the focus; contributions must be primary research with new, fully proved results.

## Method & evidence bar

- The primary standard is mathematical correctness: every claim must be fully proved; no proof sketches, unresolved cases, or conditional results in place of complete arguments (unless conditionality is the explicit contribution).
- Significance is judged on depth and importance to mathematics broadly, not on citation counts or problem fame alone; the bar is comparable to the top general journals.
- Novelty of result or technique is expected; incremental extensions of known arguments are unlikely to clear the bar.
- Exposition must let expert referees verify correctness: precise statements, complete proofs, and clear separation of new from standard material.
- MSC (Mathematics Subject Classification) codes must be assigned correctly to signal scope and assist referee assignment.
- arXiv posting is standard practice; most submissions appear on arXiv before or contemporaneously with submission.

## Structure & house style

- No imposed structural template beyond mathematical convention: introduction (context, precise statement of results, proof strategy), preliminaries, core proof sections, optional appendices.
- The introduction should state main results precisely, explain significance to a broad mathematical audience, and outline key proof ideas — read first by referees and the editorial board.
- LaTeX is standard; Duke University Press formatting conventions apply — re-check the current style file and reference style on the submission site.
- References must be complete and correctly formatted; preprint citations should carry stable arXiv identifiers.
- Length is set by mathematical necessity; there is no fixed page limit, but unnecessary length attracts scrutiny — concise, complete arguments are valued.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current Duke Mathematical Journal submission instructions on the Duke University Press site and re-verify the submission system and procedure.
- Assign MSC primary and secondary classification codes.
- Post to arXiv (or confirm prior posting) with the identifier ready for correspondence.
- Prepare a cover letter stating the main result, its significance, and suggested/excluded referees with conflicts noted.
- Confirm all co-authors have approved the submission and re-check any current fee/open-access arrangements.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main theorem and why it is of major importance to mathematics broadly.
- [ ] Every claim is fully proved; no gaps, sketches, or unresolved cases.
- [ ] The result is genuinely significant and novel, not a routine extension of known arguments.
- [ ] The introduction states results precisely, explains significance, and outlines proof ideas for a broad audience.
- [ ] The paper is posted or ready to post on arXiv with correct MSC codes.
- [ ] An honest assessment: is this best at Duke, or does its significance warrant `annals-of-mathematics` or `inventiones-mathematicae` first?

## Common desk-reject triggers

- A correct but incremental result extending known techniques without a substantially new idea.
- A narrowly specialized paper of interest only to a small sub-community, better suited to a field journal.
- An incomplete proof: any identifiable gap, unresolved case, or unjustified claim.
- An introduction that fails to convey major significance to a broad editorial board.
- Expository or survey material submitted as primary research without new theorems.

## Re-routing decision

Result of exceptional, field-reshaping significance → `annals-of-mathematics`. Top-tier general advance of comparable depth → `inventiones-mathematicae`. High-quality broad research perhaps slightly below the Duke bar → `advances-in-mathematics`. Deep analysis / PDE / applied-analysis with substantial theorem content → `communications-on-pure-and-applied-mathematics`. Narrowly specialized result → an area-specific society journal.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Duke Mathematical Journal
[Topic tags] <2–3 MSC areas>
[Method/evidence] <is the main result fully proved, novel, and of major significance?>
[Top risk] <the single most likely reason for rejection — usually significance level>
[Official items to re-check] <submission procedure / MSC codes / arXiv posting / cover letter / style file>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
