---
name: jacs-length-management
description: Use when choosing between an Article and a Communication and meeting ACS format norms for a Journal of the American Chemical Society (JACS) manuscript. Decides format and trims to fit — it does not add new results.
---

# Article vs Communication and Format Norms (jacs-length-management)

## When to trigger

- You must decide Article vs Communication
- The manuscript feels over- or under-length for the chosen format
- You are unsure what moves to the SI to fit format norms
- Figure/scheme count is high and needs disciplining

## Choosing the format

| Question | Communication | Article |
|----------|---------------|---------|
| Is the core advance a single, urgent, high-impact result? | Yes | Often part of a larger story |
| Can full proof live in the SI with a concise main text? | Yes | No — needs full main-text treatment |
| Is broad scope / multi-system / deep mechanism central to the claim? | No | Yes |
| Timeliness vs completeness | Timeliness dominates | Completeness dominates |

> Verify the **current** article types, length, figure, and word limits on the
> JACS author page — these change and differ by format. Do not hard-code limits.

## Right-sizing the main text

- Lead with the advance; the introduction should be tight (frame the gap, state the thesis).
- Results & Discussion carries only what proves the claim and its generality/mechanism; exhaustive variation goes to the SI.
- One headline scheme/figure per major point; merge panels rather than adding figures.
- Conclusion is short: what is established and what is now enabled.

## What stays vs what moves to SI

| Keep in main text | Move to SI |
|-------------------|-----------|
| Central scheme/result and one scope figure | Full substrate tables and optimization grids |
| Key mechanism figure + decisive evidence | Complete kinetic/labeling datasets |
| Crystal-structure figure + CCDC # | Full crystallographic tables, checkCIF |
| One or two essential spectra (if needed) | All spectra copies, procedures |

## Trimming tactics (without losing rigor)

- Convert prose describing a table into the table; delete the prose.
- Remove optimization narration; cite the SI optimization table for the chosen conditions.
- Cut redundant restatements between intro, results, and conclusion.
- Combine related schemes; move "also worked" examples to the SI scope table.

## Checklist

- [ ] Format chosen with an explicit reason (urgency/impact vs completeness)
- [ ] Main text contains only claim-essential evidence; rest in SI
- [ ] Figure/scheme count disciplined; panels merged where possible
- [ ] No section repeats another; conclusion is not the abstract again
- [ ] Current JACS format/limit norms verified on the author page
- [ ] If Communication: the claim is fully supported by SI + concise main text

## Anti-patterns

- Choosing Communication for a story that needs Article-level support
- Padding an Article with optimization narration better suited to the SI
- Figure sprawl: many near-duplicate schemes instead of merged panels
- Hard-coding outdated word/figure limits instead of checking current norms
- Trimming so hard that a key claim loses its supporting evidence


## Operating pass for Journal of the American Chemical Society

Treat this skill as an executable review pass, not a prose hint. First lock the chemical novelty, characterization chain, controls, and scope or mechanism evidence; then judge whether the current manuscript answers the venue's real reader: chemistry reviewers who expect a molecule/material/reaction claim to be supported by rigorous characterization and mechanistic insight.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ACS Central Science for broad conceptual reach, Angewandte for communication style, specialized ACS journals for narrower chemistry; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Format】Article / Communication (+ reason)
【Main-text load】essential only? Y/N — move to SI: [...]
【Figure count】N; merges suggested: [...]
【Limits verified】Y/N (on JACS author page)
【Next】jacs-cover-letter → jacs-submission
```

## Related resources

- [`../jacs-submission/templates/manuscript_template.md`](../jacs-submission/templates/manuscript_template.md) — section skeleton for both formats
