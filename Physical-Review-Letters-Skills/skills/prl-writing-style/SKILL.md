---
name: prl-writing-style
description: Use when polishing the prose of a Physical Review Letters manuscript for APS house style, concision, precise notation, and out-of-subfield readability. Polishes language; does not restructure the result or manage length budget.
---

# PRL Writing Style (prl-writing-style)

## When to trigger

- Prose is wordy, hedged, or jargon-dense
- Notation is inconsistent or symbols are undefined on first use
- An out-of-subfield physicist would stumble on the opening
- The draft uses long subordinate clauses where a Letter wants directness
- You are in late polish, after the result, figures, and SM are stable

## APS house-style essentials

- **Concision is a feature, not a constraint.** A Letter says what it must and stops. Every sentence should advance the central claim.
- **Active, direct voice** where it sharpens meaning; "We measure ..." / "The data show ..." beats passive circumlocution.
- **Define every symbol on first use**; keep notation consistent across Letter, figures, and SM.
- **Spell out acronyms on first use**; avoid undefined subfield jargon in the abstract and opening.
- **SI units**, consistent significant figures, and proper math typesetting.
- **Reference style** follows the current APS format; cite the prior work that establishes importance and the work the reader needs to trust the result.

## Concision moves

| Wordy pattern                                  | Tightened                                  |
|------------------------------------------------|--------------------------------------------|
| "It is important to note that X"               | "X"                                        |
| "In order to"                                  | "To"                                       |
| "We have performed measurements of"            | "We measure"                               |
| "Due to the fact that"                         | "Because"                                  |
| Three hedges in one sentence                   | one calibrated qualifier                   |
| Background paragraph before the result          | one-sentence context, then the result      |
| Restating the figure in prose                  | interpret the figure, don't transcribe it   |

## Readability for a broad audience

PRL's broad-interest gate is also a *writing* requirement: a condensed-matter referee may read an AMO Letter. So:

- Open with physics a non-specialist understands before introducing subfield notation.
- Gloss specialized concepts in one clause rather than assuming them.
- Put the physical interpretation next to every key equation or number.
- Avoid acronym soup; prefer the spelled-out concept when space allows.

## Worked micro-rewrite (Letter register)

**Before (subfield-first, hedged):**

> "In recent years there has been growing interest in the possibility that certain frustrated magnets may, under some circumstances, potentially host exotic excitations. Motivated by this, we have investigated our samples using a variety of techniques."

**After (finding-first, one calibrated qualifier):**

> "Fractionalized excitations are the defining signature of a quantum spin liquid, but direct thermodynamic evidence has been lacking. We observe a residual linear term in the low-temperature thermal conductivity of X, consistent with mobile fermionic excitations in an insulator."

What changed: the physics question opens in words any physicist can parse; the finding arrives in sentence two; three stacked hedges collapse into one; the vague "variety of techniques" becomes the actual observable.

## Sentence architecture for a four-page format

Every paragraph has one job, and its first sentence should announce it:

- **Paragraph openers carry the argument.** A referee skimming only first sentences should still reconstruct the claim chain.
- **The final paragraph earns the breadth claim.** Close with the concrete consequence for the neighboring field, not "our results pave the way."

## Precision discipline

- State claims at the strength the evidence supports — neither over- nor under-claiming.
- "Significantly" should mean statistically significant, not "a lot."
- Quote uncertainties with every headline number.
- Match tense conventions: present for established facts, past for what you did.

## Checklist

- [ ] Every sentence advances the central claim; no padding
- [ ] All symbols defined on first use; notation consistent throughout
- [ ] Acronyms spelled out on first use; abstract is jargon-light
- [ ] Opening readable by an out-of-subfield physicist
- [ ] Physical interpretation accompanies key equations/numbers
- [ ] Claims calibrated to the evidence (no over/under-claiming)
- [ ] First sentences of paragraphs alone reconstruct the argument
- [ ] Closing paragraph names a concrete cross-field consequence
- [ ] SI units and consistent significant figures
- [ ] References follow current APS format

## Anti-patterns

- "Letterese" that is dense and unreadable rather than crisp
- Undefined symbols or acronyms, especially in the abstract
- Hedging stacks ("may possibly suggest that perhaps ...")
- Prose that transcribes a figure instead of interpreting it
- Subfield jargon in the opening that excludes the broad audience
- Overclaiming significance the data do not support

## Output format

```
【Concision pass】padding removed?  yes / list
【Notation】all symbols defined, consistent?  yes / fix
【Broad readability】opening accessible out-of-subfield?  yes / fix
【Interpretation by every key number】yes / fix
【Claim calibration】matched to evidence?  yes / fix
【Next】prl-length-management (fit limit) or prl-cover-letter
```

> Reference and typesetting conventions evolve — verify current APS style on the official PRL author page.
