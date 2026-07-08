---
name: wsdm-author-response
description: Use when planning author-side communication for WSDM, a venue that historically runs no rebuttal - covers preemptive objection engineering inside the submitted PDF, the narrow legitimate channels to chairs after submission, reading reviews you cannot answer, and converting a rejection into a stronger next-cycle or sibling-venue submission.
---

# WSDM Author Response

At most ML and data-mining venues this skill would script a rebuttal. WSDM is
different: the venue historically runs **no author response phase** - a fact
documented as far back as the 2017 reviewing experiment conducted at the
conference itself, and consistent with the short review window (August
submission, October notification in the 2026 cycle). Plan as if you will never
speak to your reviewers. If the current edition's CFP announces a response
phase, that instruction supersedes everything here; check it first.

## Preemptive rebuttal: the objection inventory

Since answers must ship inside the PDF, build the rebuttal *before* submission.
Two weeks out, run an adversarial read with coauthors playing three WSDM
reviewer archetypes - the IR-methods specialist, the applied/industry reader,
and the graph/social-data reader - and log every objection in an inventory:

```text
# objection-inventory.md (one row per anticipated objection)
| # | Likely objection | Archetype | Answer exists? | Where in PDF | Action |
| 1 | Position bias not controlled in log data | IR methods | yes | §4.2 + Tab.3 | none |
| 2 | Baseline X (WSDM'25) missing            | IR methods | no  | -            | add or scope claim |
| 3 | Gains may not survive online serving    | industry   | partial | §5.3     | add latency table |
| 4 | Graph sampled non-uniformly             | graph      | yes | App.A (in-budget) | keep |
```

Then enforce the rule that makes this venue-specific: every "Answer exists?"
row must resolve to **yes + a location** or to a **claim reduction**. "We would
explain in the response" is not an available move at WSDM.

Placement discipline for the answers:

- Objections about validity (leakage, bias, confounds) get answered in the main
  evaluation text, not an appendix - reviewers who find the flaw first and the
  defense never will score on the flaw.
- Objections about scope get answered by narrowing the claim sentence itself.
- Objections about missing baselines get answered by running the baseline or by
  one honest sentence saying why it is out of scope - silence reads as evasion.

## What channels do exist after submission

| Channel | Legitimate use | Never use for |
|---|---|---|
| EasyChair note / email to PC chairs | Withdrawal; a factual error you discovered (broken figure, corrupted PDF); a conflict-of-interest problem | Arguing merit, adding results, lobbying |
| Ethics/conduct contact | Reporting reviewer misconduct or a genuine breach | Disagreement dressed as misconduct |
| Camera-ready revision (if accepted) | Implementing reviewer-requested fixes the SPC noted | Adding claims reviewers never vetted |

The bar for contacting chairs is high and the message should be three sentences
or fewer. A team that emails chairs to "clarify a misunderstanding" in a review
is spending reputation at a small, single-track community venue where the same
SPCs return every year.

## Reading reviews you cannot answer

Notification arrives with reviews attached and no reply box. Triage them for
the *next* version, not for argument:

1. **Consensus objections** (raised by 2+ reviewers) are the revision contract.
   They almost always concern evaluation validity or missing comparisons at this
   venue - fix them with experiments, not prose.
2. **Misreadings** are your fault at a no-rebuttal venue: if a competent
   specialist misread it, the paper afforded the misreading. Find the sentence
   that permitted it and rewrite that sentence in the next version.
3. **Taste objections** ("not exciting," "incremental") signal venue or framing
   mismatch - route through `wsdm-topic-selection` before resubmitting anywhere.

## The rejection fork

WSDM accepts roughly one in six submissions (2025: >100 of >600), so plan the
fork in advance:

- **Same work, next WSDM (12 months away):** worth it when reviews attack
  execution, not fit. Fold in every consensus fix; expect PC overlap - reviewers
  remember resubmissions that ignored their reports.
- **Sibling venue, sooner:** SIGIR (typically January/February deadlines) for
  IR-centric work, KDD Cycle 2 (typically February) for general mining, CIKM
  (typically May) for a broad CIKM-shaped result, RecSys (spring) for
  recommendation, TheWebConf (typically October) for web-platform work. Re-frame
  for the destination - a WSDM-tuned paper is not automatically SIGIR-tuned.
- **Short paper at the next WSDM:** since 2026 the series has a short-paper
  track with September deadlines; a focused core finding can land there when the
  long version keeps losing on breadth.

## Worked micro-example: rewriting an answer into the PDF

Suppose the inventory flags: "an IR reviewer will ask why gains shrink on head
queries." At a rebuttal venue you would draft a reply; at WSDM you edit:

- **Draft state:** results table shows the shrinkage; text ignores it.
- **Bad fix:** delete head-query column (reviewers run the slice themselves,
  and hiding it converts a weakness into an integrity question).
- **WSDM fix:** one paragraph after the table: "Gains concentrate on tail
  queries (+4.1 nDCG@10) and shrink on head queries (+0.6), consistent with
  our mechanism - head queries already receive abundant feedback, so
  debiasing has little to correct. This is the intended behavior, not a
  failure mode." The objection now has a printed answer with a mechanism
  attached, and the SPC can quote it in the meta-review.

The pattern generalizes: locate the evidence that would have gone into the
rebuttal, then write the two sentences of interpretation next to that evidence.

## If the current edition adds a response phase

Editions can change process; if the CFP or a chairs' email announces author
responses, adapt rather than assume:

1. Re-read the announced format limits (word caps, scope rules) - do not
   import another venue's rebuttal habits.
2. Recycle the objection inventory: rows that made it into the PDF get a
   one-line pointer ("§4.3 addresses this"); rows that did not get the
   evidence directly.
3. Keep the no-links discipline typical of ACM-venue responses unless the
   instructions explicitly allow links.
4. Answer reviewers in their own vocabulary and number the replies against
   review points - SPCs skim responses in minutes.

## Output format

```text
[WSDM response posture] no-rebuttal cycle confirmed? yes / no (source: current CFP)
[Objection inventory] N objections; unresolved rows: <list or none>
[In-PDF placements] <objection -> section/table map for the top 5>
[Chair-contact check] any legitimate reason to write? yes+draft / no
[Post-decision fork] resubmit WSDM / SIGIR / KDD / CIKM / RecSys / short paper, with re-framing note
```
