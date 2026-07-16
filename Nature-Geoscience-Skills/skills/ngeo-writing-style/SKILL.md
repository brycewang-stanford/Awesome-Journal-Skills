---
name: ngeo-writing-style
description: Use when polishing the prose of a Nature Geoscience manuscript for Nature house style, accessibility to non-specialists, precise terminology, and calibrated Earth-science claims. Polishes language; does not restructure the result or manage the length budget.
---

# Nature Geoscience Writing Style (ngeo-writing-style)

## When to trigger

- Prose is wordy, hedged, or dense with subfield jargon
- An oceanographer, geodynamicist, or atmospheric scientist outside your subfield would stumble on the opening
- Terminology or units are inconsistent, or acronyms are undefined on first use
- Claims over- or under-reach relative to the evidence and its uncertainty
- You are in late polish, after the result, Methods, and figures are stable

## Nature house-style essentials

- **Accessible to non-specialists.** Nature editors substantially edit for this; write so that any Earth scientist — not just your subfield — can follow the opening and the significance. This is the single most distinctive style demand.
- **Finding-first, active voice** where it sharpens meaning. "We find that ..." / "The record shows ..." beats passive circumlocution. The abstract uses "Here we show".
- **Define every acronym and symbol on first use**; keep terminology consistent across main text, Methods, figures, and SI.
- **SI units, consistent significant figures**, and every quantity with its uncertainty.
- **British or American spelling** consistently (Nature accepts either — pick one). Follow the current Nature reference and formatting style.
- **Reference discipline**: cite the work that establishes importance and that a reader needs to trust the result; the Article reference list is finite (typically up to ~50).

## Concision and de-jargoning moves

| Wordy / opaque pattern                          | Tightened / accessible                          |
|-------------------------------------------------|-------------------------------------------------|
| "It is important to note that X"                | "X"                                             |
| "In order to"                                   | "To"                                            |
| "We have carried out an analysis of"            | "We analysed"                                   |
| "Due to the fact that"                          | "Because"                                       |
| Three hedges in one sentence                    | one calibrated qualifier                        |
| A paragraph of regional setting before the result | one-sentence context, then the result         |
| Undefined subfield acronym in the abstract      | spelled-out concept                             |
| Restating a figure in prose                     | interpret the figure, don't transcribe it       |

## Readability for a broad Earth-science audience

Nature Geoscience's broad-interest gate is also a *writing* requirement — a paleoceanographer may referee a volcanology paper. So:

- Open with the Earth-system question in words any geoscientist understands before introducing subfield notation.
- Gloss specialized terms (a proxy, an index, a model acronym) in one clause rather than assuming them.
- Put the physical interpretation next to every key number, trend, or map feature.
- Avoid acronym soup; name the process, not just its abbreviation, on first mention.

## Precision discipline (Earth-science specifics)

- **Calibrate claims to evidence and uncertainty.** Do not let "consistent with" become "demonstrates," or a correlation become a mechanism.
- **Do not overreach on climate/impact.** Attribution, projection, and impact statements must stay within what the analysis and its uncertainty license — overreaching climate claims are a named rejection pattern.
- **"Significant" means statistically significant**, not "large"; state the test.
- **Distinguish correlation, association, and causation** explicitly.
- **Match tense**: present for established facts, past for what you did and found.

## Worked micro-rewrite (Nature register)

**Before (regional-first, hedged, over-reaching):**

> "In recent years there has been growing interest in the possibility that changes in ocean circulation may, under some circumstances, potentially have driven the observed regional warming, which could have important implications for future climate."

**After (accessible, calibrated, mechanism-first):**

> "Whether ocean-circulation change or local forcing drives regional warming has been unresolved. Our reconstruction shows that a X ± Y Sv weakening of the overturning preceded warming by Z years, implicating circulation as the primary driver on decadal timescales."

What changed: the question opens in words any Earth scientist parses; the finding arrives with a number and its uncertainty; three stacked hedges collapse into one calibrated claim; the vague "important implications" becomes a bounded mechanistic statement.

## Checklist

- [ ] Opening is accessible to an out-of-subfield Earth scientist
- [ ] Abstract uses "Here we show" and is jargon-light
- [ ] All acronyms/symbols defined on first use; terminology consistent
- [ ] Physical interpretation accompanies every key number/trend/feature
- [ ] Claims calibrated to evidence and uncertainty (no over/under-reach)
- [ ] No overreaching climate/attribution/impact statements
- [ ] Correlation vs. causation kept distinct
- [ ] SI units, consistent significant figures, uncertainty on every quantity
- [ ] References follow current Nature style

## Anti-patterns

- Dense subfield prose an out-of-field referee cannot follow
- Undefined acronyms/symbols, especially in the abstract
- Hedging stacks ("may possibly potentially suggest ...")
- Prose that transcribes a map or time series instead of interpreting it
- Overclaiming attribution or impact the uncertainty does not support
- Blurring correlation into causation

## Output format

```
【Accessibility】opening readable out-of-subfield?  yes / fix
【Concision / de-jargon】padding + acronym soup removed?  yes / list
【Interpretation by every key number】yes / fix
【Claim calibration】matched to evidence + uncertainty?  yes / fix
【Climate/impact overreach】none / trim
【Next】ngeo-length-management (fit limit) or ngeo-cover-letter
```

> Reference, spelling, and formatting conventions evolve — verify current Nature style on the official Nature Geoscience author pages (Checked: 2026-07-16).
