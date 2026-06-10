---
name: artbull-workflow
description: Use as the entry point for any The Art Bulletin manuscript in art history. Routes to the right Art Bulletin sub-skill based on where you are in the lifecycle, with early attention to the image-and-permissions workload that art-historical publishing requires. It dispatches; it does not draft content.
---

# Art Bulletin Workflow Router (artbull-workflow)

The orchestrator for an Art Bulletin submission. Figure out the stage and send the user to the
matching skill. The Art Bulletin is the **leading English-language journal of art history** (College
Art Association); a paper turns on an **original art-historical argument** carried by **close visual
analysis** and **documentary evidence** — and on a **heavy image-permissions workflow** that, unlike
in the social sciences, must start early.

## When to trigger

- Starting a new Art Bulletin article and unsure where to begin
- Mid-project and unsure which skill applies next
- Worried that image rights / reproduction costs will not clear in time
- Returning with a decision letter (route to `artbull-revision-and-response`)

## First instinct: start the image clearance early

Permissions and high-resolution image supply are the **author's responsibility** and are **slow and
costly**. The router's recurring reminder: run `artbull-images-and-permissions` in **parallel** with
the intellectual work — do not leave it until submission.

## Routing map (stage → skill)

```text
Is the topic a fit / a contribution? → artbull-topic-selection
Where does it sit in the field?       → artbull-scholarly-positioning
What is the argument?                 → artbull-argument-development
How do the objects look / mean?       → artbull-visual-analysis
What is the evidence (archives etc.)? → artbull-evidence-and-sources
Can I get / afford the images?        → artbull-images-and-permissions
How is it organized on the page?      → artbull-structure-and-exposition
Is the prose & citation Chicago-clean?→ artbull-writing-style-and-citation
How will it be judged?                → artbull-review-process
Ready to submit?                      → artbull-submission
Got an R&R / decision?                → artbull-revision-and-response
```

## Default order

`topic-selection → scholarly-positioning → argument-development → visual-analysis →
evidence-and-sources → images-and-permissions → structure-and-exposition →
writing-style-and-citation → review-process → submission → revision-and-response`

Iterate: most articles loop argument ↔ visual-analysis ↔ evidence several times, while
images-and-permissions runs continuously in the background.

## Anti-patterns

- Leaving rights clearance until the end — it is the slowest, costliest step and can sink a paper
- Treating the journal like a social-science venue (no datasets/statistics/replication here)
- Description without argument — cataloguing objects is not an art-historical contribution
- Choosing illustrations the budget or rights will never allow

## Symptom-to-skill dispatch table

Most users arrive with a symptom, not a stage name. Match what they say to the right sub-skill for the
College Art Association's quarterly, and check the image-clearance clock every time.

| What the user says | Route to |
|---|---|
| "Is this even right for the journal?" | `artbull-topic-selection` |
| "A reviewer said I ignore key scholarship" | `artbull-scholarly-positioning` |
| "Reviewers can't find my argument" | `artbull-argument-development` |
| "My looking was called thin" | `artbull-visual-analysis` |
| "A source / provenance was questioned" | `artbull-evidence-and-sources` |
| "I'm worried about image rights / costs" | `artbull-images-and-permissions` |
| "The draft wanders / is front-loaded" | `artbull-structure-and-exposition` |
| "I'm submitting this week" | `artbull-submission` |
| "I got an R&R / decision letter" | `artbull-revision-and-response` |

## Worked vignette: routing a project from idea to submission

Suppose a scholar arrives with "I found an amazing unpublished drawing and want to write it up." The
router does not jump to drafting. First it tests fit (`artbull-topic-selection`) — is there a
contribution beyond "this drawing is new"? — and, in the same breath, asks whether the drawing and its
comparanda can be cleared, flagging that the image-permissions clock starts **now**. Once a
contribution emerges, it routes to positioning, then argument, looping argument ↔ visual-analysis ↔
evidence as the reading firms up, with `artbull-images-and-permissions` running continuously in the
background, before structure, style, review-process, and finally submission.

## Routing pitfalls and the dispatch correction

- *Treating it like a social-science venue.* There are no datasets, statistics, or replication here;
  route evidence work to archival, provenance, and technical sources, not data analysis.
- *Leaving image clearance for the end.* Send the user to `artbull-images-and-permissions` early and in
  parallel; it is the slowest, costliest step and can sink a finished paper.

## Calibration anchor (hedge where uncertain)

- The default order is a guide, not a rail: most articles loop argument, looking, and evidence several
  times while the image-and-permissions workload — what most distinguishes this lifecycle from
  social-science venues — runs continuously underneath; volatile caps and formats belong to
  `artbull-submission` and should be confirmed against the journal's current submission guidelines.

## Output format

```
【Stage】topic / positioning / argument / visual / evidence / images / structure / writing / review / submit / revise
【Route to】artbull-<skill>
【Image clearance started?】Y/N (start now if N)
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — image sources, rights agencies, archives, Chicago tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official Art Bulletin / CAA URLs behind every fact in this pack
