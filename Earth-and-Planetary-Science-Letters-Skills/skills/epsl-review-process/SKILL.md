---
name: epsl-review-process
description: Use when you need to understand how Earth and Planetary Science Letters (EPSL) evaluates a manuscript — subject-editor desk screening against the frontier bar, expert review typically drawn from the sub-fields the paper joins, and editor-led decisions. It sets expectations and hardens the paper before submission; it does not contact editors.
---

# Review Process (epsl-review-process)

EPSL's review is run by working scientists: a team of editors, each handling manuscripts near their
own specialty, screening first for whether the paper is a genuine Letter — concise, decisive, of
broad Earth-and-planets interest — before sending it to expert referees. Knowing the two-gate
structure (desk screen on significance and fit, then technical review on rigor) lets you harden the
paper against each gate in advance. Volatile details (editor names, reviewer counts, timelines) drift;
re-check them on the official site.

## When to trigger

- Pre-submission stress test against the desk-screen and reviewer axes
- Interpreting a decision letter and planning the response strategy
- Anticipating which sub-fields the referees will come from
- Considering a Comment on a published EPSL paper, or facing one

## How EPSL review works

1. **Subject-editor triage.** The handling editor — a researcher in the paper's area — judges frontier
   significance, letters fit, and scope. Regional case studies without process-level insight, method
   reports, and incremental additions to settled questions are declined here, without external review.
2. **Referees drawn from the paper's intersection.** A manuscript joining geochemistry and
   geodynamics is typically reviewed by at least one specialist from each side; each referee audits
   their own layer (traceability and statistics vs physical plausibility and resolution).
3. **Editor-led decisions.** The handling editor weighs the reviews and decides — reject, major or
   minor revision, or acceptance; reviews advise, the editor adjudicates.
4. **Comments and Replies.** EPSL carries formal Comment/Reply exchanges on published papers; they are
   held to the same evidence standard as Letters and are not a venue for tone.
5. **Integrity screening.** Plagiarism checks, authorship and competing-interest declarations, and
   Elsevier's publishing-ethics framework apply at submission.

## Desk-decline grounds and where they get fixed upstream

| Desk-decline ground | What the editor read | Fix it in |
|---------------------|----------------------|-----------|
| Regional study, no process takeaway | place-name title, local conclusions | `epsl-topic-selection` |
| Incremental / does not move the frontier | gap framed as "more data needed" | `epsl-literature-positioning` |
| Not letters-shaped | sprawling scope, companion manuscript | `epsl-workflow`, `epsl-writing-style` |
| Better suited to a specialist journal | method-community audience only | `epsl-topic-selection` |
| Over length / format non-compliant | cap exceeded, missing statements | `epsl-submission` |

## What each referee audits

| Referee | Reads first | Rejects on |
|---------|-------------|------------|
| The analyst (geochem/geochron) | standards, blanks, σ-definitions, MSWD | untraceable numbers |
| The physicist (geophys/geodyn) | resolution tests, force balance, scaling | interpreting artifacts |
| The recorder (strat/paleo) | age control, correlation logic | rates without anchors |
| The planetary scientist | data provenance (mission/archive), assumed parameters | overreach beyond sensitivity |

## Worked micro-example (illustrative — forecasting the decision on the slab-fluid paper)

Stress-testing the B-isotope + tomography Letter before submission (illustrative reasoning):

- **Desk axes:** process-level (how slabs lose water) — passes; letters-shaped (one claim, 6,100
  words) — passes; portability argued in the abstract — passes.
- **Geochemist referee:** will probe the δ11B external reproducibility and crustal-assimilation
  screen — both pre-empted in the supplement.
- **Seismologist referee:** will ask whether the conduit survives the resolution test — the inset in
  Figure 1c exists precisely for this.
- **Realistic outcome:** major revision asking for an alternative-fluid-pathway discussion and one
  more sensitivity case. Budget for it; "major revision" at a high-bar venue is an invitation to
  convince, not a near-accept.

The discipline: walk the desk axes and both referees' audits yourself, in writing, before the editor
does.

## Anti-patterns

- Submitting a locally-framed paper and hoping the editor generalizes it for you
- Preparing for one referee's specialty when the paper straddles two
- Reading "major revision" as acceptance-with-chores
- Responding to a Comment with rhetoric instead of data
- Assuming timelines, reviewer counts, or editor assignments that the official page does not state

## Output format

```
【Desk screen】process-level? letters-shaped? portable? [Y/N each]
【Predicted referees】sub-fields + what each will audit
【Pre-empted objections】list, with manuscript location
【Weakest layer】named honestly + mitigation
【Realistic outcome】reject / major / minor
【Next】epsl-submission (or epsl-revision-and-rebuttal on a decision)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — editorial structure and policy links (re-check volatile items)
- [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md) — papers that survived this gauntlet, by sub-field
