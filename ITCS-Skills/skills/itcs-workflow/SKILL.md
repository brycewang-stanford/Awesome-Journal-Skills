---
name: itcs-workflow
description: Use to plan an ITCS campaign end to end on its single annual cycle — backward from the early-September deadline through the no-rebuttal review, the November notification, the LIPIcs camera-ready, and the January conference with its Graduating Bits session.
---

# ITCS Workflow

ITCS runs on **one annual cycle** with a distinctive rhythm: submit in **early September**, get a
**yes/no in November with no rebuttal in between**, and present the following **January**, with
open-access publication in **LIPIcs**. There is no second round, no revise-and-resubmit, and no
author-response phase, so the leverage is almost entirely *before* the deadline. Plan the year
backward from that September date. Every date below is the **ITCS 2026 snapshot** (Bocconi,
Milan); reopen the current call — see
[`../../resources/official-source-map.md`](../../resources/official-source-map.md).

## The single-cycle calendar (ITCS 2026 anchor)

| Phase | ITCS 2026 date | What actually happens |
|---|---|---|
| Abstract / registration | **4 Sep 2025** (7:59:59 PM EDT) | Title, abstract, authors, conflicts locked in HotCRP; the abstract drives PC bidding |
| Full-paper submission | **6 Sep 2025** (7:59:59 PM EDT) | Anonymized PDF with complete proofs uploaded |
| Reviewing (no rebuttal) | Sep-Oct 2025 | PC + external reviewers read; **no author-response phase** |
| Notification | **~10 Nov 2025** | Accept / reject; there is no Major Revision category |
| Camera-ready | Late 2025 (per call) | `lipics-v2021` class, de-anonymized, LIPIcs metadata |
| Conference | **27-30 Jan 2026** | Talks, Graduating Bits session, community mixing at Bocconi |

Because there is no rebuttal and no second deadline, treat the September upload as **final** in a
way authors from rebuttal venues underestimate: the paper must answer the reviewer's objections
on its own.

## Working backward from the deadline

```text
D-day (early Sep)      : full paper, complete proofs, anonymized, uploaded and re-downloaded
D-2 days               : abstract/registration + conflicts locked (earlier than the paper!)
D-1 to 2 weeks         : full version to arXiv/ECCC/ePrint (encouraged; lightweight double-blind)
                         final proof-completeness pass (no "proof omitted" on a central claim)
D-3 to 4 weeks         : freeze the model and definitions; polish the first-10-pages merits window
D-2 months             : decide ITCS vs STOC/FOCS/SODA on the novelty axis (itcs-topic-selection)
```

The two commonest self-inflicted failures: (1) missing the **abstract/registration** cutoff,
which is ~2 days *before* the paper deadline — no registration, no submission slot; and (2)
carrying a rebuttal-venue mindset that leaves objections for "later," when there is no later.

## The no-rebuttal consequence, planned for

Since you cannot answer reviewers after they read, you must **answer them inside the paper**:

- Anticipate the "is this model empty/trivial?" question with an anchoring result up front.
- Anticipate the "is this actually new?" question with an honest related-work delta.
- Anticipate the "why should I care?" question with a first-page conceptual payoff.
- State scope and limitations yourself, so a reviewer does not raise them as your blind spot.

See [`itcs-author-response`](../itcs-author-response/SKILL.md) for how the *absence* of a rebuttal
reshapes strategy, and [`itcs-writing-style`](../itcs-writing-style/SKILL.md) for pre-empting
objections in the prose.

## After notification

- **Accept:** move to [`itcs-camera-ready`](../itcs-camera-ready/SKILL.md) — switch to
  `lipics-v2021`, de-anonymize, complete ACM CCS / keywords / funding, and hit the LIPIcs
  production deadline. Register at least one author to present. Consider submitting a Graduating
  Bits talk if a coauthor is near graduation.
- **Reject:** there is no resubmission to a later ITCS round this year (single cycle). Route the
  paper — often to STOC/FOCS/SODA on depth, or to a journal — via the table in
  [`itcs-topic-selection`](../itcs-topic-selection/SKILL.md). The reviews, though not rebuttable,
  are usually substantive; use them to sharpen the next submission.

## The Graduating Bits and community layer

ITCS is a **smaller-community** venue with a strong direction-setting culture. The **Graduating
Bits** session — short talks by researchers near graduation (on either side) presenting results,
plans, and themselves — is a fixture worth planning for if you or a coauthor is on the market. The
conference is as much about *seeding directions* as reporting finished work, which is why bold,
early ideas fare well here; budget time for the hallway and session conversations, not just the
talk.

## Reverify each cycle

- The exact abstract and paper deadlines, and the AoE/EDT timezone of the cutoff.
- Whether the current call still runs **no rebuttal** (the theory-venue norm, but confirm).
- The camera-ready deadline and the current LIPIcs class/version.
- The host, city, and dates — **ITCS 2027 is 待核实** as of 2026-07-09; do not carry Bocconi
  forward.

## Output format

```text
[ITCS cycle status] on track / at risk
[Registration] title/abstract/authors/conflicts locked by the earlier cutoff? yes/no
[Paper] complete proofs present? anonymized? first-10-pages merits window done?
[Preprint] full version posted (arXiv/ECCC/ePrint)? yes/no
[Post-notification] accept -> camera-ready owner+date ; reject -> reroute target
[Calendar risks] <ordered, with dates before the early-September cutoff>
```
