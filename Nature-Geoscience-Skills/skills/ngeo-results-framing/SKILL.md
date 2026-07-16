---
name: ngeo-results-framing
description: Use when a Nature Geoscience result is correct but its headline advance and cross-disciplinary significance are not yet sharp. Structures the one-advance narrative and the "Here we show" abstract; does not run analysis or design figures.
---

# Nature Geoscience Results Framing (ngeo-results-framing)

## When to trigger

- You have the data/model output but the "so what for the Earth system" is fuzzy
- The draft reads like a chronological expedition or model-run report, not a single argument
- You have several findings and have not chosen the headline one
- The opening buries the result under a literature or regional-setting tour
- `ngeo-scope-fit` returned a Nature Geoscience verdict but flagged the breadth framing as weak

## The one-advance discipline

A Nature Geoscience Article makes **one** headline advance. Everything else is support. Decide the headline result first; demote the rest to corroboration, to the online Methods, or to Supplementary Information.

- **Primary advance** — the single sentence the title and abstract both encode, phrased as what the Earth system *does*, not what you *measured*.
- **Supporting results** — at most two or three, and only if they reinforce the primary one.
- **Everything else** — regional context, extended sensitivity tests, secondary proxies → SI (see `ngeo-supplementary`).

If you have two co-equal advances, you likely have two papers, or one belongs in a community journal.

## The abstract: the "Here we show" convention

Nature abstracts follow a recognizable arc and are capped at **200 words, unreferenced** (verify). The house pattern:

1. **Background / why the question matters** — one to three sentences a non-specialist Earth scientist grasps.
2. **The gap or controversy** — what was unknown, unresolved, or assumed.
3. **"Here we show ..."** — the headline advance, stated plainly with the key quantitative result and its uncertainty.
4. **Mechanism / interpretation** — what the result means physically.
5. **Broad implication** — the consequence for the wider Earth system or a neighboring field.

Lead into the advance with the literal "Here we show" (or a close equivalent); Nature editors and readers expect it, and it forces finding-first framing.

## The opening (first paragraphs carry the gate)

The main-text opening front-loads significance, not setting. A reliable arc:

1. **The Earth-system context** — one or two sentences on the first-order process at stake.
2. **The open question / controversy** — the specific unknown, framed as a scientific problem, not a regional description.
3. **What this study shows** — the headline advance with the key number.
4. **Why it matters across the field** — the cross-disciplinary consequence.

Do not open with the study region's geography or a paragraph of instrument history. The advance should be legible within the first paragraph.

## Framing decision branches

| Symptom                                              | Move                                                            |
|------------------------------------------------------|-----------------------------------------------------------------|
| Two co-equal headline advances                        | Split, or demote one to support / SI                           |
| Result stated only operationally ("we measured X")    | Reframe as the Earth-system conclusion it implies              |
| Significance asserted, not shown                      | Tie it to a first-order question or a prior belief it changes  |
| Regional setting dominates the opening                | Cut to 1–2 sentences; move detail to Methods / SI              |
| Abstract lists methods before findings                | Reorder: "Here we show ..." first, method as an enabling clause |
| Overreaching climate/impact claim                     | Calibrate to what the evidence and uncertainty license         |

## Checklist

- [ ] Exactly one primary advance, expressible in one sentence
- [ ] Title (≤ ~90 characters) encodes the advance, not just the topic or region
- [ ] Abstract uses "Here we show" and leads with the finding + its uncertainty
- [ ] Abstract is unreferenced and within the ~200-word limit
- [ ] Opening reaches the result within the first paragraph or two
- [ ] Significance is tied to a first-order question or belief it changes
- [ ] Interpretation (mechanism) is stated, not just the observation
- [ ] Supporting results (≤3) genuinely reinforce the primary one

## Anti-patterns

- A "kitchen-sink" Article that reports every measurement the campaign produced
- Operational framing ("we observe X in region Y") with no mechanistic interpretation
- Significance claims that overreach beyond the data and its uncertainty
- An abstract that is a methods or fieldwork summary rather than a result statement
- A title naming the region and method instead of the advance
- Saving the punchline for a "conclusions" paragraph the reader may never reach

## Output format

```
【Primary advance】one sentence (Earth-system framing)
【Title】≤ ~90 chars, encodes the advance?  yes / fix
【Abstract】"Here we show" + finding + uncertainty, ≤200 words, unreferenced?
【Opening moves】context / gap / advance / broad significance — all present?
【Supporting results】≤3, each justified
【Demoted to Methods / SI】list
【Next】ngeo-methods (grounding) or ngeo-figures (lead figure)
```

> Abstract and title conventions are durable; verify the current word/character limits and the "Here we show" guidance on the official Nature Geoscience author pages (Checked: 2026-07-16).
