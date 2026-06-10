---
name: jme-writing-style
description: Use when applying Journal of Monetary Economics (JME) house style — the 100-word abstract that may not begin with "This paper" or "We", author-date references with journal titles spelled out, double-spaced 12-point formatting with line numbers, footnotes not endnotes, up to five keywords, and at least one JEL code.
---

# JME House Style (jme-writing-style)

## When to trigger

- The abstract is over 100 words or begins with "This paper" / "We"
- References are numbered or use abbreviated journal titles
- You are unsure of the manuscript formatting JME requires at submission
- Final polish before the Editorial Manager preflight

## Implementing JME style (verified specifics)

- **Abstract**: **no more than 100 words**, and it **must not start with "This paper" or "We."** Open with the finding or the question instead.
- **References**: **author-date** style ("Smith (1992) reported that..."; "(e.g., Smith et al., 1969)"). **Journal titles are spelled out in full — never abbreviated.** The **reference list appears after appendices but before tables and figures.**
- **Formatting**: manuscripts **double-spaced, 12-point type, 1-inch margins**, with **line numbers** on both submissions and final manuscripts.
- **Notes**: use **footnotes**, numbered consecutively with **superscript Arabic numerals — not endnotes.**
- **Keywords / classification**: up to **five keywords** and **at least one JEL (Journal of Economic Literature) classification code** are required.
- **Tables and figures**: numbered consecutively with Arabic numerals.
- **Length**: accepted papers must not exceed **40 pages** of text/references/footnotes, with no more than **10 tables and figures** combined (online supplements exempt) — write to that target.
- **AI declaration**: include a declaration of any use of generative AI in manuscript preparation, per Elsevier policy.

## Writing for a macro audience

JME readers are macroeconomists and central bankers. The intro should state the **question, the identified shock or mechanism, the headline result, and the policy lesson** quickly. Define the shock units (e.g., a 100-bp policy surprise) early. Keep the prose disciplined: the 40-page cap rewards a tight argument, with derivations and extra robustness in the online supplement.

## Checklist

- [ ] Abstract ≤ 100 words and does **not** begin with "This paper" or "We"
- [ ] References author-date; journal titles spelled out in full
- [ ] Reference list after appendices, before tables/figures
- [ ] Double-spaced, 12-point, 1-inch margins, **line numbers** on
- [ ] Footnotes (superscript Arabic), not endnotes
- [ ] Up to five keywords and ≥ one JEL code
- [ ] Generative-AI use declared if applicable


## Style execution pass for Journal of Monetary Economics

Treat this skill as an executable review pass, not a prose hint. First lock the main macro object, the identifying variation, and the policy-relevant counterfactual; then judge whether the current manuscript answers the venue's real reader: macro and monetary economists who expect the shock, mechanism, and policy margin to be visible early.

- **Do the pass:** Rewrite the first two pages so each paragraph starts from the venue-level claim, not from chronology or method inventory; preserve exact source-map limits and move technical overflow to appendix or supplement.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against JIE for open-economy trade/finance emphasis, RED for dynamic macro theory, AEJ Macro for broader field positioning; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Abstract】word count + first word (≤100, not "This paper"/"We")? Y/N
【References】author-date, full journal titles? Y/N
【Formatting】double-spaced 12pt, line numbers, footnotes? Y/N
【Keywords/JEL】≤5 keywords + ≥1 JEL code? Y/N
【AI declaration】present if used? Y/N
【Next step】jme-replication-and-data-policy
```
