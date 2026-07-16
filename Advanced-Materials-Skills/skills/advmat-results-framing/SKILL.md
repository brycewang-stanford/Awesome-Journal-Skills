---
name: advmat-results-framing
description: Use when an Advanced Materials result is sound but its central advance and significance are not yet sharp, or when a Communication's opening paragraph must double as its abstract. Structures the one-advance narrative; does not run characterization or design figures.
---

# Advanced Materials Results Framing (advmat-results-framing)

## When to trigger

- You have the data but the "why this is an advance" is fuzzy
- The draft reads like a chronological synthesis-then-characterization log, not one argument
- You have several results and have not chosen the headline advance
- You are writing a Communication and must fold the abstract into the opening paragraph
- `advmat-scope-fit` returned Adv. Mater. but flagged the impact framing as weak

## The one-advance discipline

An Adv. Mater. paper is organized around **one central advance** — a new material, a new mechanism, or a new property regime. Everything else is support.

- **Primary advance** — the single sentence the title and abstract (or opening paragraph) both encode.
- **Supporting results** — the structure–property evidence and the device demonstration that establish the advance.
- **Everything else** — process-optimization sweeps, ancillary characterization, secondary samples → Supporting Information (see `advmat-supplementary`).

If you have two co-equal advances, you likely have two papers, or one belongs in a sibling journal.

## The structure → property → function chain

Materials referees reward a clean causal chain. Frame the paper so each link is explicit:

1. **Structure/composition** — what the material *is* (new phase, architecture, interface, composition).
2. **Property** — the measured property that structure produces (transport, mechanical, optical, electrochemical).
3. **Function/device** — the property demonstrated in a working device, benchmarked against the state of the art.

The advance lives at whichever link is genuinely new; name it, and show the chain holds end to end. A paper that jumps from structure to a device metric without the property mechanism in between invites the "why does it work?" rejection.

## The opening (Communication: opening paragraph = abstract)

In a Communication, there is no separate abstract — the **first paragraph carries the significance and must read as a self-contained mini-paper**. A reliable four-move pattern (also the model for a Research Article abstract):

1. **The materials context** — one or two sentences a non-specialist materials scientist understands.
2. **The open problem / limitation** — the trade-off, instability, or missing material that has blocked progress.
3. **What this work reports** — the central advance, stated plainly, with the key metric or qualitative surprise.
4. **Why it matters broadly** — the design consequence for a wider materials or device community.

Do not open with a paragraph-long literature tour. The advance should appear in the first paragraph.

## Framing decision branches

| Symptom                                             | Move                                                        |
|-----------------------------------------------------|-------------------------------------------------------------|
| Two co-equal headline advances                       | Split, or demote one to support / SI                        |
| Result stated as a metric only ("we reached X%")     | Reframe as the new material principle that produced it      |
| Novelty asserted, not shown                          | Tie it to the design rule / trade-off it changes            |
| Structure→property→function chain has a gap          | Add the missing mechanism link, or scope the claim down     |
| Opening buried under background                      | Cut to 2–3 sentences; move detail to the body or SI         |

## Checklist

- [ ] Exactly one primary advance, expressible in one sentence
- [ ] Title encodes the advance (new material/mechanism/property), not just the topic
- [ ] Structure → property → function chain is explicit and unbroken
- [ ] Opening / abstract reaches the advance within the first paragraph
- [ ] For a Communication, the opening paragraph stands alone as the abstract
- [ ] Significance tied to a design rule or trade-off it changes, not asserted
- [ ] Supporting results genuinely reinforce the primary advance; the rest is in the SI

## Anti-patterns

- A "kitchen-sink" paper reporting every sample the project produced
- Metric-first framing with no new material science behind the number
- A structure-to-device leap that skips the property mechanism
- Overclaiming applications the material has not been shown to enable
- A Communication opening paragraph that reads as background, not as an abstract

## Output format

```
【Primary advance】one sentence
【Title encodes advance】yes / fix
【Structure→property→function】all links present?  yes / gap: ...
【Opening moves】context / problem / advance / significance — all present?
【Communication abstract-in-paragraph-1】yes / n/a / fix
【Demoted to SI】list
【Next】advmat-methods (characterization) or advmat-figures (lead figure)
```

> Abstract/keyword/opening rules differ by article type and evolve — verify the current requirements on the official Wiley Advanced Materials author page.
