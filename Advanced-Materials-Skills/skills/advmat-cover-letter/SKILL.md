---
name: advmat-cover-letter
description: Use when drafting the cover letter for an Advanced Materials submission, whose core job is to convince the editor that the work is a genuine materials advance of broad impact worthy of the journal. Argues the impact case; does not fix the science or format the manuscript.
---

# Advanced Materials Cover Letter (advmat-cover-letter)

## When to trigger

- You are about to submit and need a cover letter that earns editorial review
- `advmat-scope-fit` returned "Adv. Mater. with impact framing" and you must make that case
- An editor previously desk-rejected similar work as "not a sufficient advance"
- You need to distinguish this work from your own or others' recent related papers
- You are resubmitting after transfer from, or rejection by, another journal

## The editor's triage question

Advanced Materials editors desk-triage on **advance and impact before sending anything to review**. The cover letter's one job is to answer, in the editor's language: *why is this a broadly important materials advance, not incremental optimization, and why here?* Everything else is secondary.

## Structure (one page, tight)

1. **Submission line** — article type (Communication / Research Article), title, and that it is submitted to Advanced Materials.
2. **The advance in two sentences** — the new material / mechanism / property, stated plainly. Lead with the finding, not the background.
3. **Why it is an advance, not an increment** — name the design rule or the trade-off it breaks; contrast explicitly with the prior state of the art (including your own prior work if relevant).
4. **Why broad impact** — name the concrete out-of-subfield or device community that will build on this, and why. This is the leg most letters omit.
5. **Evidence in brief** — the multi-technique characterization proves the structure–property claim, and the device is benchmarked against the best reported systems.
6. **Housekeeping** — originality and not-under-consideration-elsewhere; any prior preprint (e.g. ChemRxiv/arXiv) disclosed; related manuscripts under review; suggested and opposed referees (see `advmat-referee-strategy`).

## What makes the impact case land

- **Contrast, don't assert.** "Unlike prior layered oxides limited to X, this material achieves Y because Z" beats "this is a highly novel and important material."
- **Name the neighbor.** Editors weigh breadth; a specific out-of-field beneficiary ("solid-state battery groups pursuing sulfide interfaces") is more persuasive than "the community."
- **Quantify the advance.** One benchmarked number with conditions signals rigor; a hype adjective signals its absence.
- **Pre-empt the venue question.** If the work could be read as AFM/Small-scale, say in one sentence why the advance is broad enough for Adv. Mater.

## Micro-model (the two-sentence advance + impact)

Aim for a middle that reads like this, not like an abstract:

> "We report a layered oxide whose interlayer pillaring enables near-zero-strain multivalent
> intercalation — a design rule, not a single composition. Unlike prior high-capacity oxides that crack
> during cycling, this cathode retains 94% capacity over 800 cycles (Table 1), which we expect solid-state
> battery, catalysis, and intercalation-electronics groups to build on."

The finding leads, the contrast shows it is not incremental, one benchmarked number signals rigor, and a
named neighbor community carries the breadth — all in two sentences.

## Checklist

- [ ] Article type and title stated; addressed to Advanced Materials
- [ ] The advance is in the first short paragraph, finding-first
- [ ] Explicit contrast with the state of the art shows it is not incremental
- [ ] A concrete out-of-subfield / device audience is named for broad impact
- [ ] One benchmarked headline metric with conditions is cited
- [ ] Originality, preprint disclosure, and related-manuscript status stated
- [ ] Suggested/opposed referees prepared (cross-check `advmat-referee-strategy`)
- [ ] One page, no hype-word padding

## Anti-patterns

- A letter that summarizes the abstract instead of arguing impact
- Hype adjectives ("groundbreaking," "first-ever") with no contrast or number
- Omitting the broad-impact leg — the most common reason a strong result reads as specialist
- Failing to distinguish the work from the authors' own recent related papers
- Not disclosing a preprint or a related manuscript under review elsewhere
- Overclaiming applications the data do not support

## Output format

```
【Article type + title】...
【Advance (2 sentences, finding-first)】...
【Not incremental because】contrast with SOTA: ...
【Broad impact】named neighbor audience + why: ...
【Benchmarked metric】value + conditions: ...
【Housekeeping】originality / preprint / related MSS / referees — all covered?
【Next】advmat-submission (preflight) or advmat-referee-strategy
```

> Cover-letter expectations and required disclosures evolve — verify current Wiley Advanced Materials submission requirements on the official author page.
