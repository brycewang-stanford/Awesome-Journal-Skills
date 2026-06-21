---
name: smr-writing-style
description: Use when revising prose for a Sociological Methods & Research (SMR) manuscript — methods-paper introduction arc, ASA citation style, the ≤150-word non-parenthetical abstract, and clear exposition of estimands, assumptions, and results. Edits prose and conformance; does not derive or simulate.
---

# SMR Writing Style

Use this to make the prose match a methods journal. SMR readers are methodologists who want the
contribution stated early, the assumptions visible, and the math legible — and they want ASA style and
the abstract rules honored exactly, because conformance signals seriousness.

## The methods-paper introduction arc

Open in this order (model it on `resources/worked-examples/01-introduction.md`):

1. **The methodological problem in an applied setting** — what goes wrong when researchers use the
   current method, stated concretely, not "X has received much attention."
2. **Why existing methods fail** — the gap, named, not a literature tour.
3. **The contribution** — develop / evaluate / correct, in one proportional sentence (from
   `smr-method-contribution`).
4. **The properties and evidence** — what you prove, what the simulation shows, what the illustration
   demonstrates, each labeled by evidentiary status.
5. **The applied payoff** — what researchers can now do, and that usable software is released.

A compact roadmap closes the introduction; do not over-signpost.

## The abstract (a hard, checkable rule)

- **≤150 words** and **no parenthetical citations** (检索于 2026-06；以官网为准). SAGE allows
  non-parenthetical citations ("Smith (2015) showed…") but not "(Smith 2015)". Rewrite any parenthetical
  cite or drop it.
- The abstract must name the **method, the problem it solves, and the evidence type** — not just the
  topic. A methods abstract that reads like a substantive abstract signals scope confusion.

## Exposition discipline for math-heavy prose

- **State the estimand before the estimator**; state assumptions near the result they support.
- **Short interpretation over algebra restatement**: after a theorem, say what it means for a user, do
  not re-narrate the derivation.
- **Label evidentiary status** in the prose: "we prove," "the simulation shows," "we conjecture." A
  methods reader tracks these precisely.
- **Define notation once, use it consistently**; a methods paper cannot afford symbol drift.

## ASA style and house conventions

- In-text citations and references in **ASA style**; **dataset references in DataCite style** (检索于
  2026-06；以官网为准). Use a reference manager configured for ASA rather than hand-formatting.
- Keep the **title page separate** from the main document for double-anonymized review; remove
  self-identifying phrasing ("in our previous paper") from the body.
- Disclose **generative-AI tool use** in the back matter when applicable; if none was used, no
  acknowledgement is needed.

## Checklist

- [ ] The introduction follows problem → why methods fail → contribution → evidence → payoff.
- [ ] The contribution sentence is proportional and appears early.
- [ ] The abstract is ≤150 words with zero parenthetical citations.
- [ ] The abstract names method, problem, and evidence type.
- [ ] Estimand precedes estimator; assumptions sit near their results.
- [ ] Evidentiary status (proved/simulated/conjectured) is labeled in prose.
- [ ] ASA citation style and DataCite dataset references are used.
- [ ] No self-identifying language; AI-use disclosed if applicable.

## Anti-patterns

- **Substantive-paper opening**: "much attention has been paid to…" instead of the methodological gap.
- **Parenthetical citations in the abstract**: a direct violation of the stated rule.
- **Algebra narration**: restating the derivation instead of interpreting the result.
- **Status blur**: simulation regularities written in the language of proof.
- **Hand-formatted citations**: ASA inconsistencies that signal carelessness at a methods venue.
- **Deanonymizing phrasing** left in the body under double-anonymized review.

## Output format

```text
[Prose status] ready / needs revision / not ready
[Intro arc] complete / missing step (which)
[Abstract] words=<n>, parenthetical cites=<n>, names method+problem+evidence? yes/no
[Style] ASA + DataCite applied? yes/no
[Anonymization] clean / risk where
[Next SMR skill] smr-software-and-reproducibility
```
