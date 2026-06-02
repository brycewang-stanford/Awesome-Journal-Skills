---
name: ajs-review-process
description: Use to understand how the American Journal of Sociology (AJS) evaluates a manuscript — its distinctive student-run, double-blind review out of the University of Chicago Department of Sociology, the "preject" screen, reviewer assignment by a Manuscript Assignment Board, and decision categories. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (ajs-review-process)

AJS's review process is **unusual** and worth understanding before submitting. It is **double-blind**,
run out of the **University of Chicago Department of Sociology**, with graduate students doing
reviewer assignment and a **"preject"** screen for papers not in dialogue with current sociology.
Knowing this lets you pre-empt the failure modes. Verify volatile specifics on the live editorial
pages (待核实; UChicago Press pages are 403 to automated fetch).

## When to trigger

- Before submitting, to stress-test the manuscript against the AJS process
- Interpreting a decision letter and setting expectations
- Understanding why "in dialogue with current sociology" and theoretical ambition both matter

## How AJS review works (distinctive features)

1. **Double-blind.** Identities are hidden from **both** authors and referees; prepare an anonymized
   manuscript with a **separate cover page** (see `ajs-submission`). AJS **will not knowingly use
   reviewers in the author's network** (current colleagues, coauthors, PhD cohort, etc.).
2. **Three levels of editorship.** The **editorial board is the entire faculty of the UChicago
   Department of Sociology**; there is an editor, and a student tier (Associate Editors) supervising
   Assistant Editors.
3. **Student-run assignment.** On first submission, a **Manuscript Assignment Board** (Assistant
   Editors under graduate-student Associate Editors) reads a **blinded** manuscript to infer
   substantive area and method, then finds reviewers who can speak to it — **not restricted to cited
   authors**. This design deliberately reduces editor-driven reviewer bias.
4. **The "preject."** AJS declines without review papers that are **not in dialogue with current
   sociology** — opinion pieces, current-events interpretations, or work that is not original
   sociological research. Editorial associates or the Assignment Board make prejects, consulting the
   editor when unsure.
5. **Decisions.** Reject, revise and resubmit, or (rarely on first round) accept. R&R is the normal
   path for promising papers; expect substantial revision.

## What reviewers weigh

| Reviewer asks | You answer with |
|---------------|------------------|
| Is this in dialogue with current sociology? | positioning in `ajs-literature-positioning` |
| Is there a portable theoretical payoff? | argument in `ajs-theory-building` |
| Is the method rigorous *for its kind*? | design defense in `ajs-research-design` |
| Do the data warrant the claim? | the evidence chain in `ajs-data-analysis` |

## Shape the paper to pass

- Make the theoretical contribution and its dialogue with the field obvious early (clears the preject).
- Write so a cross-method, generalist reviewer can follow and find the contribution.
- Present negative cases / robustness candidly — reviewers trust candor.

## Anti-patterns

- An opinion or current-events piece submitted as research (prejected)
- A subfield-only or atheoretical paper at a theory-forward generalist journal
- Leaving identifying self-references that break double-blind anonymity
- Expecting acceptance without a serious R&R round

## Output format

```
【Clears the preject】in dialogue with current sociology + original research? [Y/N]
【Theoretical payoff】portable contribution present? [Y/N]
【Method rigor】defensible for its kind? [Y/N]
【Evidence→claim】warranted and candid? [Y/N]
【Anonymity】double-blind-ready? [Y/N]
【Realistic outcome】preject / reject / R&R / (rare) accept
【Next】ajs-submission (or ajs-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — process and portal summary
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — AJS double-blind, preject, and Manuscript Assignment Board policy
