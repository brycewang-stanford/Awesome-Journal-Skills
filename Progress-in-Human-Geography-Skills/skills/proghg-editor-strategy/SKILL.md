---
name: proghg-editor-strategy
description: Use when working with the Progress in Human Geography (PiHG) editors and SAGE — handling a commissioned progress report vs. a submitted review, anticipating what referees of a review evaluate, and negotiating scope. Plans the interaction; it does not run the submission preflight (proghg-submission) or draft the response letter (proghg-revision).
---

# Editor Strategy (proghg-editor-strategy)

## When to trigger

- You are writing a **commissioned progress report** and coordinating with the editors on scope/series
- You have **submitted a review or intervention** and want to anticipate referee expectations
- The editor has asked you to expand, cut, or rebalance coverage
- You are calibrating how PiHG's two routes (commissioned vs. submitted) differ in the editor relationship

## Who you are working with at PiHG

PiHG is edited by a team of **editors** (verified 2026-06-22: **editor-in-chief Noel Castree**, supported by additional editors and an international Editorial Advisory Board; re-confirm on the live SAGE page, as editors rotate), with **SAGE** handling production. Your relationship differs sharply by route:

| Route | Editor relationship | Acceptance logic |
|-------|---------------------|------------------|
| **Commissioned progress report** | collaborative; the editors **invited** you as the subfield's reporter and want the series to succeed | still edited for critical quality and scope, but not competing in an open submission pool |
| **Submitted review / intervention** | standard peer review; the editors decide on referee advice | assessed on significance, coverage, fairness, and conceptual contribution; competitive |

Know which you are in: a progress report is a coordinated, short, recurring artefact; a submitted review is a competitive, free-standing argument.

## How review differs for a review article

PiHG referees do **not** check an identification strategy or replicate results — there are none of the author's own. They evaluate the piece **as a critical review**:

| Reviewer question | What they are really checking |
|-------------------|-------------------------------|
| Is the coverage complete across traditions? | the coverage account from `proghg-literature-synthesis` / `proghg-transparency-and-reproducibility` — can they name an omitted literature or tradition? |
| Is it fair and reflexive? | even-handedness across traditions; no self-promotion or partisanship (`proghg-comprehensiveness-and-balance`) |
| Is there a real conceptual argument? | the spine vs. an annotated bibliography or neutral roundup (`proghg-organizing-framework`) |
| Is it accessible? | can a geographer from another subfield follow it (`proghg-writing-style`) |
| Are the appraisals fair and correct? | does the author characterize each work's contribution and limits accurately |
| Is it conceptual, not empirical? | no original data or detailed cases smuggled into a "review" |
| Is it the right scope/strand/length? | fits the chosen strand and word envelope; not a monograph |

Referees of a PiHG review are often **the reviewed authors themselves** — the people whose work and tradition are being appraised will read how you appraised them. This makes balance and accurate attribution strategic, not just ethical.

## Scope negotiation with the editors

- **Lock scope early, in writing.** For a commission, confirm the report's boundaries — period, sub-themes, which turns are in — before reading. For a submission, the cover letter sets the scope you are claiming.
- **Negotiate, don't capitulate, on coverage asks.** If a referee or editor wants an added literature, assess whether it fits the spine; propose where it goes or explain why it is out of scope — a review cannot grow without bound and must stay in the strand's word envelope (检索于 2026-06；以官网为准).
- **Surface conflicts of interest.** If a likely referee is a central author you must critique, tell the editor — PiHG/SAGE expect COI disclosure, and it protects both the process and you.
- **Respect the schedule.** A commissioned progress report runs against an issue/series timeline; a submitted review against the normal SAGE cycle. Confirm deadlines and plan backward.
- **Keep a coverage ledger.** Maintain a short, sharable record of what is in scope and why (and what was deliberately excluded), so when the editor or a referee asks "why not X?", you answer with a decision already made.

## Checklist

- [ ] Route identified (commissioned report vs. submitted review) and editor relationship calibrated accordingly
- [ ] Scope agreed in writing (report boundaries for a commission; cover-letter scope for a submission)
- [ ] Anticipated the seven review-referee questions (coverage, fairness/reflexivity, argument, accessibility, appraisal, conceptual-not-empirical, scope/strand)
- [ ] Coverage-expansion asks evaluated against the spine and the strand's word envelope before agreeing
- [ ] Conflicts of interest (referees who are reviewed authors) flagged to the editor
- [ ] Attribution and appraisals double-checked, knowing reviewed authors may referee
- [ ] Timeline (series/issue or SAGE cycle) calibrated (volatile — confirm)
- [ ] A plan for which asks to accept vs. push back on, with reasons

## Anti-patterns

- Treating a commission as a blank check — invited progress reports are still edited for critical quality and scope
- Treating a submission as collaborative — it is competitive peer review on significance and contribution
- Accepting every "please also cover…" until the review loses its spine and overruns the strand limit
- Mischaracterizing a reviewed author's work when that author may be your referee
- Hiding a conflict of interest instead of disclosing it (SAGE/COPE expect disclosure)
- Asserting current editors / timeline / process from memory rather than the live SAGE pages

## Output format

```text
【Route】commissioned progress report / submitted review-or-intervention
【Editor relationship】collaborative-series / competitive-peer-review — calibrated? Y/N
【Scope agreement】boundaries (period/sub-themes/traditions) locked in writing or claimed in cover letter? Y/N
【Referee anticipation】coverage / fairness / argument / accessibility / appraisal / conceptual / scope — prepared each? Y/N
【Coverage asks】evaluated against spine + strand envelope; accept/push-back plan? Y/N
【COI】reviewed-author referees flagged to editor? Y/N
【Timeline】series/issue or SAGE cycle calibrated? Y/N · 待核实
【Source status】current editors/process re-confirmed on SAGE pages? Y/N
【Next step】→ proghg-submission (SAGE ScholarOne preflight)
```
