---
name: jet-review-process
description: Use when interpreting the Journal of Economic Theory (JET) review pipeline — editor desk-screening, single-anonymized refereeing, at least two reviewers, editor decisions, and the generative-AI bar on referees.
---

# Review Process (jet-review-process)

## When to trigger

- You want to understand how JET evaluates a theory submission before sending it
- You are deciding how defensively to write proofs and which objections to pre-empt
- You received a decision and want to read it against JET's actual process

## How JET evaluates (verified 2026-06-20)

- **Two-stage flow.** Editors first assess **suitability** (a desk-screen / desk-rejection stage);
  papers that pass are sent out for refereeing.
- **Single anonymized review (single-blind).** Referees see author identities; authors do not see
  referee identities. This differs from QJE/AEA-style double-blind — so **do not** rely on
  anonymization to neutralize reputation effects; let the result and proofs carry the paper.
- **Minimum of two referees.** Papers that clear the desk screen go to **at least two** independent
  expert reviewers for assessment of correctness, originality, and the size of the theoretical
  contribution.
- **Editors decide.** The accept/reject decision is taken by the **editors**. JET uses a multi-editor
  **"Lead Editor + Editors"** governance: a submission is routed to whichever editor's field best
  matches, and that editor — not a single managing editor-in-chief — makes the call. The current
  official board lists **Faruk Gul** as Lead Editor, with Editors **Manuel Amador**,
  **Pierpaolo Battigalli**, **Marco Ottaviani**, and **Juuso Valimaki**.
- **Generative-AI bar on evaluators.** Reviewers and editors are **prohibited** from using
  generative-AI tools in the evaluation process; authors, separately, must disclose AI use at submission.

## What this implies for you

- The desk screen rewards a **theory-first scope fit** stated on page one (see jet-topic-selection).
- With **single-blind** review, a referee can place your prior work; phrase self-citations plainly,
  not evasively.
- Two expert referees will **check proofs**, not just read them — every step must survive a hostile read.
- Routing-by-field means the cover letter should name the subfield (mechanism design, decision theory,
  matching, etc.) so the right editor picks it up.

## What a JET referee checks first

In rough order of attention on a theory submission:

1. **Statement–proof match** — does each theorem quantify over exactly its stated assumptions?
2. **The closest-theorem question** — is the delta to the nearest *published* result real, or does
   the paper follow from a known theorem after a routine reduction?
3. **Hidden premises** — do any proof steps quietly use finiteness, continuity, compactness, or a
   common prior that the statement never grants?
4. **Tightness** — are the key assumptions defended by counterexamples, or at least flagged as open?
5. **The generality trade** — does the extra generality purchased justify the proof's complexity,
   or would the transparent special case have carried the same economics?

Write the paper so each of these five reads resolves in your favor within minutes, not hours.

## Desk-reject patterns for theory submissions

| Pattern | Why the desk screen stops it |
|---|---|
| Applied paper with a decorative model bolted on | the deliverable is not a theorem — fails the theory-first scope criterion |
| Marginal generalization of a published theorem | originality bar: the delta is not conceptually new |
| Correct but unmotivated mathematics | no economic question — JET is economic theory, not a pure-mathematics outlet |
| Sweeping "general" claims over visibly incomplete proofs | correctness cannot be presumed at the screen |
| Survey or synthesis without a new result | confirm against the journal's current author guidelines for any special article types before trying |

## Self-referee pass (run before submitting)

```text
Referee your own paper in JET's order of attention:
[ ] each theorem read in isolation: assumptions complete? claim ≤ what the proof delivers?
[ ] nearest published theorem named; your one-sentence delta survives a hostile read
[ ] every lemma checked line-by-line by a coauthor who did not write it
[ ] each key assumption: counterexample, generalization, or an explicit open-question note
[ ] subfield named in the cover letter so the matching editor claims the paper
```

## Output format

```
【Stage now】desk-screen / out-to-referees / decision
【Review model】single-anonymized, ≥2 referees, editor decides
【Pre-empt】<top correctness/generality objection to neutralize> → jet-rebuttal / jet-identification-strategy
【Editor route】subfield matched to Lead Editor / Editor roster? [Y/N]
```
