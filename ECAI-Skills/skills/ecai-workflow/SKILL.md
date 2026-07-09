---
name: ecai-workflow
description: Use to plan an ECAI campaign end to end — run the single-round year backward from the paper deadline through the abstract/registration step, summary-reject phase, rebuttal window, notification, and the open-access camera-ready, adapting to whether the edition is a standalone ECAI (FAIA/PAIS) or the joint IJCAI-ECAI 2026.
---

# ECAI Workflow

Plan the ECAI year **backward from the paper deadline**, because ECAI is a **single-round** process
with a **two-deadline** front (abstract, then paper) and **no revision round** to catch a gap later.
First fix which regime the edition is in — it changes the calendar owner, the template, and whether
PAIS is available:

- **Standalone ECAI** (e.g. 2024): EurAI + a host society; FAIA/`ecai.cls`; PAIS co-located.
- **IJCAI-ECAI 2026**: joint with IJCAI in Bremen (15-21 Aug 2026); IJCAI process/template/proceedings.

## The IJCAI-ECAI 2026 calendar (verify on the live page)

```text
Abstract deadline .............. 12 January 2026 (AoE)   <- title/abstract/authors/topics locked
Full paper deadline ............ 19 January 2026 (AoE)   <- anonymized PDF + supplement
Summary-reject notification .... 4 March 2026            <- early filter; below-bar/out-of-scope out
Author response (rebuttal) ..... 7-10 April 2026         <- one short window, factual corrections
Final notification ............. 29 April 2026           <- accept / reject (no revision round)
Camera-ready ................... (per author kit)         <- de-anonymize, open-access production
Conference ..................... 15-21 August 2026, Bremen
```

For a standalone ECAI the shape is the same (registration ~1 week before the PDF; double-blind
review with a rebuttal; open-access FAIA proceedings) but the dates and organizer differ — read the
current call.

## Backward plan from the paper deadline

- **Deadline − 12 weeks:** decide **ECAI vs IJCAI/AAAI** and **main track vs PAIS**
  (`ecai-topic-selection`). Routing before writing is the highest-leverage move, because the 7-page
  budget and the venue's breadth shape the paper.
- **− 10 weeks:** lock the contribution and the **evidence type** (proof vs experiment) per claim
  shape (`ecai-experiments`); name threats/assumptions now — you cannot add them in a later round.
- **− 8 weeks:** draft the body to the **first-page arc** and the 7-page budget
  (`ecai-writing-style`); start the anonymized supplement (`ecai-reproducibility`).
- **− 4 weeks:** finish full proofs / complete experiments with seeds and spread; write delta-first
  related work (`ecai-related-work`).
- **− 2 weeks:** internal review; run the **double-blind sweep** and the **body/supplement split**
  (`ecai-supplementary`).
- **Abstract deadline:** register title/abstract/authors/topics with the *real* text.
- **Paper deadline:** run `ecai-submission` end to end on the final PDF, supplement, template, and
  per-author cap.

## After submission

- **Summary-reject phase:** nothing to do but ensure you did not invite it — scope, formatting,
  anonymity, and page budget must have been correct at upload.
- **Rebuttal window:** `ecai-author-response` — one short, precise, double-blind reply; fix factual
  misreadings and supply asked-for numbers; promise only minor camera-ready edits.
- **Notification:**
  - **Accept** → `ecai-camera-ready` (de-anonymize, correct template/publisher regime, open-access
    forms, DOI/citation, register to present) and make the supplement a permanent open release
    (`ecai-artifact-evaluation`).
  - **Reject** → revise substantively and reroute (AAAI/IJCAI/specialist venue) or aim at the next
    ECAI; there is no appeal that reopens the decision (`ecai-review-process`).

## Parallel tracks to run early

- **Reproducibility is not a last-minute task.** Seeds, cached outputs, and full proofs must be
  produced *as you do the work*; they cannot be retrofitted at the deadline (`ecai-reproducibility`).
- **PAIS decision is a fork, not an afterthought.** A deployed-application paper aimed at PAIS
  leads with real-world impact and has its own call — decide before the abstract deadline.
- **Per-author submission cap** (IJCAI-ECAI 2026: 8) — coordinate across your group early so you do
  not have to withdraw a paper at the deadline.

## Milestone checklist

```text
[ ] Regime fixed: standalone ECAI (FAIA/PAIS) or joint IJCAI-ECAI (IJCAI)
[ ] Track chosen: main track vs PAIS
[ ] Evidence type set per claim (proof vs experiment); threats/assumptions named
[ ] Body drafted to 7-page arc; supplement started and anonymized
[ ] Abstract registered by the earlier deadline
[ ] Double-blind sweep + body/supplement split done before paper upload
[ ] Rebuttal plan ready for the response window
[ ] Camera-ready path (template/publisher/forms/DOI/registration) mapped
```

## Reverify each cycle

Regime (standalone vs joint), all dates and AoE cutoffs, the per-author cap, the ethics/AI policy,
and the camera-ready production instructions — none are stable across editions.
