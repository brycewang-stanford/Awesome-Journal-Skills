---
name: arecon-review-process
description: Use when calibrating expectations for the Annual Review of Economics (ARE) Editorial Committee review cycle on an invited article — what happens after delivery, who reviews, the accuracy/rigor/balance bar, and the annual-volume timeline. Sets expectations; it does not run the delivery preflight (arecon-submission) or draft the response letter (arecon-revision).
---

# Review Process — What to Expect (arecon-review-process)

## When to trigger

- The commissioned draft is delivered and you want to know what happens next
- You are unsure whether an invited review is auto-accepted (it is not) and what it is judged on
- You need to plan around the annual-volume production schedule
- A coauthor expects journal-style turnaround and you must reset that to the Committee cadence

## How an invited ARE review is evaluated

Being invited gets your draft *reviewed*, not *accepted*. After delivery, the Editorial Committee assesses the manuscript for **accuracy, rigor, and balance**, and may route it to **another Committee member or an external expert** as appropriate (检索于 2026-06；以官网为准). The bar is the review-article bar, not the primary-research bar:

| Stage | What happens | What it tests |
|-------|-------------|---------------|
| Commissioning | Committee invites the topic/author; scope is set | fit, author standing, ARE-shaped topic |
| Delivery | author submits the invited draft in the commissioned workflow | completeness, format, declarations |
| Committee/expert review | a Committee member and/or external referee read it | accuracy, rigor, balance, accessibility, coverage |
| Revision | author addresses comments (see `arecon-revision`) | gaps closed; fairness restored; spine sharpened |
| Production | production editor copyedits, sets figures, applies house style | format, references, figure quality |
| Volume publication | article appears in the annual volume (open access under S2O) | — |

Special-case integrity: if a Committee member is the author, they **do not participate in reviewing their own article**, which is handled by another member or external expert under the same policies (检索于 2026-06；以官网为准).

## Timeline reality

ARE runs on an **annual cadence**: one volume per year with fixed production deadlines (检索于 2026-06；以官网为准). This differs sharply from a rolling journal — there is no continuous queue, and a draft that misses a volume's production window can slip to the next volume. Treat the production editor's schedule as the binding constraint and plan revision time backward from it. Do not assume journal-style "decision in N months"; confirm the specific volume timeline with the editor.

## What referees push on (and how to pre-empt)

Because ARE referees judge the review *as a review*, the predictable pushbacks are upstream-preventable:

- **"You omit literature X."** → `arecon-literature-synthesis` saturation log; close the gap before delivery.
- **"This slights school Z / over-cites the author."** → `arecon-evidence-standards` balance + self-citation audit.
- **"This reads like an annotated bibliography."** → `arecon-organizing-framework`; make the spine explicit.
- **"A non-specialist can't follow Section 4."** → `arecon-writing-style`; intuition-first.
- **"You mischaracterize study W."** → fix precisely; the reviewed author may be the referee.

## Checklist

- [ ] Team understands invitation ≠ acceptance; the draft is reviewed for accuracy/rigor/balance
- [ ] Expectations set to the **annual-volume cadence**, not journal rolling turnaround
- [ ] Production deadline obtained; revision time planned backward from it
- [ ] The five predictable referee pushbacks pre-empted upstream before delivery
- [ ] Any author–Committee conflict-of-interest handled per Annual Reviews policy
- [ ] Volatile timeline/process re-confirmed with the editor / on the author pages

## Anti-patterns

- Assuming an invited review is rubber-stamped — it is refereed for rigor and balance
- Expecting rolling-journal turnaround instead of an annual production schedule
- Discovering a coverage or balance problem at review that the saturation log would have caught
- Missing the volume production window and slipping a full year
- Quoting a specific decision timeline from memory rather than confirming the volume schedule

## Output format

```text
【Stage】commissioning / delivery / Committee-review / revision / production
【Bar】judged on accuracy + rigor + balance + accessibility + coverage? confirmed
【Cadence】annual volume; production deadline obtained? Y/N · 待核实
【Pre-empted pushbacks】coverage / balance / framework / accessibility / appraisal — checked? Y/N
【COI】author–Committee conflicts handled per policy? Y/N
【Next step】→ arecon-revision (after the comments) → arecon-submission (re-deliver)
```
