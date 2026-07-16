---
name: advmat-writing-style
description: Use when polishing the prose of an Advanced Materials manuscript for Wiley house style, concision, precise materials nomenclature and units, and readability across materials subfields. Polishes language; does not restructure the advance or manage the length budget.
---

# Advanced Materials Writing Style (advmat-writing-style)

## When to trigger

- Prose is wordy, hedged, or dense with un-glossed jargon
- Materials nomenclature, chemical formulae, or units are inconsistent
- A reader from a neighboring materials subfield would stumble on the opening
- The draft narrates the experiment chronologically instead of arguing the advance
- You are in late polish, after the science, characterization, and figures are stable

## Wiley / Adv. Mater. house-style essentials

- **Concision serves impact.** Adv. Mater. prizes a crisp, high-signal narrative; every sentence should advance the structure → property → function argument.
- **Argue, don't log.** Write "the doping raises carrier density, which lifts conductivity to X" — not "first we synthesized, then we measured, then we observed."
- **Nomenclature discipline.** Define every abbreviation and material acronym on first use; keep chemical formulae, phase labels, and sample names identical across text, figures, and SI.
- **Units and numbers.** SI units throughout, consistent significant figures, a space between number and unit, and every headline metric with its uncertainty and measurement conditions.
- **British or American English** consistently (Wiley accepts either) — do not mix within a manuscript.
- **References** follow the current Wiley Advanced Materials style; cite the prior art that establishes novelty and the work a reader needs to trust the characterization.

## Concision moves

| Wordy pattern                                     | Tightened                                    |
|---------------------------------------------------|----------------------------------------------|
| "It is worth noting that the material exhibits"    | "The material exhibits"                       |
| "In order to investigate"                          | "To probe"                                    |
| "We have successfully synthesized"                 | "We synthesized" (drop "successfully")        |
| "Due to the fact that"                             | "Because"                                     |
| "novel and unprecedented" (stacked novelty claims) | one calibrated claim, tied to the design rule |
| Restating every figure value in prose              | interpret the figure; don't transcribe it     |
| A background paragraph before the result           | one-sentence context, then the advance        |

Adv. Mater. abstracts and openings are notorious for hype-word inflation ("novel," "unprecedented," "significantly," "remarkable"). Delete the adjective and let the number and the mechanism carry the claim.

## Readability across subfields

Adv. Mater. is read across materials chemistry, physics, energy, electronics, and biomaterials — a battery reviewer may assess a photovoltaics paper. So:

- Open with materials context a non-specialist grasps before introducing subfield notation.
- Gloss a specialized concept in one clause rather than assuming it.
- Put the physical/chemical interpretation next to every key metric.
- Prefer the spelled-out concept over acronym soup where space allows.

## Worked micro-rewrite (Adv. Mater. register)

**Before (log-style, hype-stacked, un-benchmarked):**

> "In this work, a novel and unprecedented material was successfully synthesized via a facile method. It was found that the sample exhibits remarkably enhanced performance, which is significantly higher than previous works and may have great potential for future applications."

**After (advance-first, calibrated, benchmarked):**

> "We report a layered oxide whose expanded interlayer spacing accommodates reversible multivalent intercalation. The resulting cathode delivers 220 mAh g⁻¹ at 1C with 92% capacity retention over 500 cycles — outperforming the best reported oxides of this family (Table 1) — because the spacing suppresses lattice strain during cycling."

What changed: "novel/unprecedented/facile/remarkable/significant" all deleted; the metric arrives with conditions and a benchmark; the mechanism ("spacing suppresses strain") replaces vague "great potential."

## Precision discipline

- State claims at the strength the evidence supports — no over- or under-claiming.
- "Significantly" means statistically significant, not "a lot."
- Quote uncertainty and conditions with every headline number.
- Present tense for established facts; past tense for what you did.

## Checklist

- [ ] Every sentence advances the structure → property → function argument
- [ ] All abbreviations, formulae, and sample names defined and consistent across text/figures/SI
- [ ] Hype words ("novel," "unprecedented," "remarkable") removed or earned
- [ ] Opening readable by an out-of-subfield materials scientist
- [ ] Interpretation accompanies every key metric; conditions and uncertainty stated
- [ ] SI units, consistent significant figures, number–unit spacing
- [ ] One English variant used consistently
- [ ] References follow current Wiley Advanced Materials style

## Anti-patterns

- Hype-word inflation instead of a benchmarked, mechanistic claim
- Undefined acronyms or drifting sample names between text, figures, and SI
- Chronological lab-log narration instead of an argument
- Prose that transcribes figure values instead of interpreting them
- Subfield jargon in the opening that excludes the broad readership
- Mixed British/American spelling within one manuscript

## Output format

```
【Concision / de-hype pass】done?  yes / list
【Nomenclature】abbreviations, formulae, sample names consistent?  yes / fix
【Broad readability】opening accessible out-of-subfield?  yes / fix
【Interpretation + conditions on every metric】yes / fix
【Claim calibration】matched to evidence?  yes / fix
【Next】advmat-length-management (fit format) or advmat-cover-letter
```

> Reference and typesetting conventions are set by Wiley and evolve — verify current Advanced Materials style on the official author page.
