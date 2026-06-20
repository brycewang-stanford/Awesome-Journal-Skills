---
name: jel-classification-system
description: Use when assigning JEL classification codes to a Journal of Economic Literature (JEL) survey and relating the survey to the JEL code taxonomy that the journal itself maintains. Explains and applies the codes correctly; it does not write prose (jel-writing-style) or run the submission preflight (jel-submission).
---

# JEL Classification System (jel-classification-system)

## When to trigger

- The survey is drafted and you must assign JEL classification codes for submission
- You are unsure how many codes, at what level, or in what order to list them
- You want the survey's *scope* to map cleanly onto the JEL taxonomy a reader uses to find it
- You are reasoning about which JEL category the field you are surveying actually sits in

## What the JEL classification system is (and why JEL owns it)

The **JEL classification system** is the American Economic Association's subject taxonomy for economics, *maintained by the Journal of Economic Literature itself* and used across EconLit and most economics journals. A survey for JEL therefore has a dual relationship with the codes: it must be **indexed** by them like any paper, and — because JEL is the system's steward — a well-scoped survey often *corresponds to* one or a small set of categories that define its field.

**Structure (检索于 2026-06；以官网为准):**
- **Three levels.** A single **letter** (20 top categories), a **two-digit** subcategory (e.g. `J2`), and a **three-character** detailed code (e.g. `J24`).
- Assign **detailed three-character codes** for a submission; the letter/two-digit levels locate the field.

**The 20 top-level categories:**

| | | | |
|---|---|---|---|
| A General Economics & Teaching | B History of Thought / Methodology / Heterodox | C Mathematical & Quantitative Methods | D Microeconomics |
| E Macroeconomics & Monetary | F International Economics | G Financial Economics | H Public Economics |
| I Health, Education & Welfare | J Labor & Demographic Economics | K Law & Economics | L Industrial Organization |
| M Business Admin / Marketing / Accounting / Personnel | N Economic History | O Development, Innovation, Growth | P Political Economy & Comparative Systems |
| Q Agricultural, Resource & Environmental | R Urban, Rural, Regional, Real Estate, Transport | Y Miscellaneous | Z Other Special Topics |

## Assigning codes to a survey

1. **Find the field's home category** first (the letter), then the subcategory, then detailed codes — top-down, so you do not miss the natural primary code.
2. **Lead with the field's primary detailed code**, then add codes for the *methods* and *adjacent fields* the survey substantively covers (a survey is broader than a paper, so a handful of codes is normal).
3. **Mirror the organizing framework.** The codes should look like the survey's cells: if a section covers an econometric method the field relies on, include the relevant `C` code; if it spans into public economics, include the `H` code.
4. **Cross-check against the EconLit code list** for the exact current label and three-character code — labels and codes are revised; do not assign from memory (检索于 2026-06；以官网为准).
5. **Confirm count/format limits** for the manuscript in the AEA JEL style guide via `jel-submission` (JEL codes are commonly listed with keywords on the title page).

> Because JEL *maintains* the classification system, a survey is in an unusual position: it can illuminate where a field sits in the taxonomy, and occasionally a maturing field's survey is part of the case that a code's scope should be reconsidered. You are not assigning codes from outside the system — you are working inside the AEA's own subject map, so get the codes exactly right.

## Checklist

- [ ] Primary detailed (three-character) code identified top-down (letter → two-digit → detailed)
- [ ] Method codes (e.g. `C`) and adjacent-field codes added where the survey substantively covers them
- [ ] Code set mirrors the organizing framework's cells (not a random scatter)
- [ ] Each code verified against the current EconLit JEL code list (label + three-character form)
- [ ] Primary code listed first; codes ordered by centrality to the survey
- [ ] Count/format limits confirmed in the AEA JEL style guide (via `jel-submission`)
- [ ] Not over-coding: only categories the survey genuinely covers

## Anti-patterns

- Assigning only a single broad letter-level code to a wide-ranging survey (under-indexing)
- Scattering a dozen codes for fields the survey barely touches (over-indexing)
- Inventing or mis-remembering three-character codes instead of checking the live EconLit list
- Codes that contradict the organizing framework (the survey's own map of its scope)
- Treating the codes as an afterthought rather than a true description of the field's place in economics

## Output format

```
【Field home】<letter> → <two-digit> → <primary detailed code>
【Code set】<primary code first, then method + adjacent-field codes>
【Framework mirror】codes match the survey's cells? Y/N
【Verification】each code checked on current EconLit list? Y/N
【Format】count/placement confirmed in AEA JEL style guide? Y/N
【Next step】→ jel-editor-strategy / jel-submission (codes go on the title page with keywords)
```
