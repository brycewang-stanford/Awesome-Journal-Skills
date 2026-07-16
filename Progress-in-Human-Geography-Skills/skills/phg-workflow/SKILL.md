---
name: phg-workflow
description: Use when starting or navigating any Progress in Human Geography (PiHG) manuscript and you need the entry point. Routes to the right sub-skill based on lifecycle stage and whether the piece is a free-standing review article or a commissioned Progress Report. It dispatches; it does not draft content.
---

# PiHG Workflow Router (phg-workflow)

The orchestrator for a *Progress in Human Geography* submission. Figure out the stage and the **genre**,
then send the user to the matching skill. PiHG is the discipline's **review and theory flagship** — the
router's first job is to make sure the piece is a **synthetic, agenda-setting review**, not an empirical
study wearing a review's clothes. **PiHG does not publish empirical results or detailed cases.**

## When to trigger

- Starting a new PiHG piece and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether you are writing a **review article** (open submission) or a **Progress Report** (commissioned)
- Unsure whether the topic is *review-worthy* at all (route to `phg-topic-selection`)
- Returning with a decision letter (route to `phg-rebuttal`)

## First question: is this even a PiHG piece?

Run the fit gate before routing anywhere else.

| Check | Pass condition | Route if it fails |
|-------|----------------|-------------------|
| Not empirical | The core is an argument about a **literature**, not new data or a single case | this is the wrong journal — stop |
| Review-worthy | The literature is **large, live, and contested**, with real stakes | `phg-topic-selection` |
| Has an intervention | You can name what the field is getting wrong and how you re-order it | `phg-critical-intervention` |
| Synthetic | The sources add up to **one argument**, not a list | `phg-argument-synthesis` |

If "not empirical" fails — the piece would be unchanged if you deleted the argument and kept the data —
PiHG is the wrong venue; consider an empirical geography journal instead.

## Second question: which genre?

| Genre | What it is | Route |
|-------|-----------|-------|
| **Review article** | Free-standing, unsolicited critical review (~4,000–8,000 words) | full default order below |
| **Progress Report** | **Commissioned** critical survey of a sub-field's recent work | same craft, but scope to the report's remit; confirm with the editor |
| **PiHG Lecture / commentary** | Invited; formats vary | confirm current practice on the SAGE page (`phg-submission`) |

Progress Reports are **invited by the editors** — you cannot submit one cold. If you have a report
commission, the same skills apply, scoped to the agreed remit.

## Routing map (stage → skill)

```text
Is the topic review-worthy?        → phg-topic-selection
What concept organizes it?         → phg-theory-building
Where does it sit in the field?    → phg-literature-positioning
Do the sources add to one arg?     → phg-argument-synthesis
What is the critical move?         → phg-critical-intervention
What is the forward agenda?        → phg-contribution-framing
Do the exhibits do synthesis?      → phg-tables-figures
Does it read as PiHG?              → phg-writing-style
Ready to submit?                   → phg-submission
How will it be judged?             → phg-review-process
Got an R&R / decision?             → phg-rebuttal
```

## Default order

`topic-selection → theory-building → literature-positioning → argument-synthesis → critical-intervention →
contribution-framing → tables-figures → writing-style → submission → review-process → rebuttal`

Iterate: most essays loop theory ↔ synthesis ↔ intervention several times before writing-style.

## Anti-patterns

- Treating PiHG as a place to publish an empirical study "framed as a review" — it is not
- Writing an annotated bibliography and calling it a review (no cumulative argument)
- Submitting something billed as a Progress Report without a commission
- Reviewing a settled, niche literature with no live debate or stakes
- Overrunning the short (~8,000-word inclusive) cap because a review "needs to be comprehensive"

## Output format

```
【Genre】review article / Progress Report (commissioned) / lecture-commentary
【Stage】topic / theory / positioning / synthesis / intervention / framing / exhibits / writing / submit / review / rebut
【Fit gate】not-empirical? review-worthy? has-intervention? synthetic? [Y/N each]
【Route to】phg-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — systematic-review, bibliometric, and reference tooling for building a corpus
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official SAGE/PiHG URLs behind every fact in this pack
