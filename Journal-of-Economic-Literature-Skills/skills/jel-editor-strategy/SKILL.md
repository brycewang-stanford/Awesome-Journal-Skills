---
name: jel-editor-strategy
description: Use when working with the editor and referees of a Journal of Economic Literature (JEL) survey — scope negotiation, what survey referees evaluate, and revision expectations. Plans the interaction; it does not run the submission preflight (jel-submission) or draft the response letter (jel-revision).
---

# Editor & Referee Strategy for a Survey (jel-editor-strategy)

## When to trigger

- The editor encouraged the proposal and you are negotiating the survey's scope
- You want to anticipate what JEL referees of a *survey* will push on (different from a paper)
- The editor has asked you to expand, cut, or rebalance coverage
- You are calibrating how many revision rounds and how long a JEL survey typically takes

## How review differs for a survey

JEL referees do **not** check an identification strategy or replicate results — there are none of the author's own. They evaluate the survey **as a survey**:

| Referee question | What they are really checking |
|------------------|-------------------------------|
| Is the coverage complete? | the saturation/comprehensiveness from `jel-literature-synthesis` — can they name an omitted literature? |
| Is it balanced? | even-handedness across schools; no self-promotion (`jel-comprehensiveness-and-balance`) |
| Is there a real framework? | the spine vs. an annotated bibliography (`jel-organizing-framework`) |
| Is it accessible? | can a non-specialist (the JEL reader) follow it (`jel-writing-style`) |
| Are the appraisals fair and correct? | does the author characterize each study's contribution and limits accurately |
| Is it the right scope? | not too narrow (field-journal review) nor unfinishably broad |

Referees of a survey are often **the surveyed authors themselves** — the people whose work is being weighed will read how you weighed it. This makes balance and accurate attribution not just ethical but strategic.

> A useful frame: the editor recruits referees partly to *test coverage and fairness*, not to re-run statistics. A referee who can name an omitted literature, or who feels their school was caricatured, is the single most common cause of a major-revision verdict on a survey — both are preventable upstream by `jel-literature-synthesis` and `jel-comprehensiveness-and-balance`.

## Scope negotiation with the editor

The editor is your primary partner on a survey. Use the relationship deliberately:

- **Lock scope early, in writing.** The proposal stage (`jel-proposal-and-commissioning`) is where scope is cheapest to change. Get the editor's agreement on the boundaries before months of reading.
- **Negotiate, don't capitulate, on coverage asks.** If the editor wants an added literature, assess whether it fits the spine; propose where it goes or explain why it is out of scope — a survey cannot grow without bound.
- **Surface conflicts of interest.** If a likely referee is a central author you must critique, tell the editor; it protects both the process and you.
- **Calibrate timeline.** JEL surveys are large; revision can be substantial and multi-round. Confirm current timelines on the AEA JEL pages (检索于 2026-06；以官网为准) and plan for real revision effort, not cosmetic edits.
- **Keep a coverage ledger for the editor.** Maintain a short, sharable record of what is in scope and why (and what was deliberately excluded), so when the editor or a referee asks "why not X?", you can answer with a decision already made rather than scrambling.

## Checklist

- [ ] Scope agreed with the editor in writing at the proposal stage
- [ ] Anticipated the six survey-referee questions (coverage, balance, framework, accessibility, appraisal, scope)
- [ ] Coverage-expansion asks evaluated against the spine before agreeing
- [ ] Conflicts of interest (referees who are surveyed authors) flagged to the editor
- [ ] Attribution and appraisals double-checked, knowing surveyed authors may referee
- [ ] Timeline and likely revision depth calibrated from the official pages (volatile)
- [ ] A plan for which asks you will accept vs. push back on, with reasons

## Anti-patterns

- Treating the editor as a gatekeeper rather than a scope partner on a commissioned-style article
- Accepting every "please also cover…" until the survey loses its spine and finish-ability
- Mischaracterizing a surveyed author's work when that author may be your referee
- Hiding a conflict of interest instead of disclosing it to the editor
- Assuming a survey gets a light revise; budgeting for cosmetic edits when substantial rework is normal
- Asserting current timelines/process from memory rather than the live AEA pages

## Output format

```
【Scope agreement】boundaries locked with editor in writing? Y/N
【Referee anticipation】coverage / balance / framework / accessibility / appraisal / scope — prepared each? Y/N
【Coverage asks】evaluated against the spine; accept/push-back plan? Y/N
【COI】surveyed-author referees flagged to editor? Y/N
【Timeline】revision depth + rounds calibrated from official pages? Y/N
【Next step】→ jel-submission (preflight) → jel-revision (after the letter)
```
