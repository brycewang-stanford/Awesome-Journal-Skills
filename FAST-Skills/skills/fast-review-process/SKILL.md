---
name: fast-review-process
description: Use when reasoning about how a USENIX FAST submission is evaluated, covering double-blind program-committee review with outside referees, the author-response (rebuttal) period, the Accept / Accept-with-shepherding / One-shot-Revision / Reject decision set, how a one-shot revision differs from a journal R&R and from OSDI/ATC handling, and where author leverage exists.
---

# FAST Review Process

Model the pipeline before interpreting any single review. FAST — the USENIX Conference on File and
Storage Technologies — uses the USENIX systems-review machinery: **double-blind** program-committee
review, an **author-response** period, PC **shepherding** for accepted papers, and a **one-shot
revision** track. The most consequential mental shift for authors is understanding that FAST has
*four* outcomes, not two, and that a one-shot revision is a real, bounded second chance — not a soft
accept and not an open-ended journal R&R.

## Process model

- Submission and review run on **HotCRP** (a separate instance per deadline) with **double-blind**
  anonymity: identities are hidden from reviewers; authors anonymize the PDF and references and refer
  to their own prior work in the third person.
- The **program committee** reviews, assisted by **outside referees** when needed. Storage papers are
  matched to reviewers from their subarea (file systems, SSD/NVM, KV stores, caching, reliability),
  so device details and evaluation state are scrutinized, not skimmed.
- There is an **author-response (rebuttal) period** before notification: a short window to answer
  reviewer questions and correct misreadings.
- First decisions fall into **Accept**, **Accept-with-shepherding**, **One-shot Revision**, or
  **Reject**. Accepted papers are shepherded by a PC member to closure. Proceedings are open access
  via USENIX.

## Reading a decision against the categories

| Decision | What it means | Author move |
|---|---|---|
| Accept | Contribution and evidence hold; polish only | Camera-ready + artifact; do not reopen scope |
| Accept-with-shepherding | Accepted subject to specific, bounded fixes overseen by a PC shepherd | Make exactly the requested changes; keep the shepherd informed |
| One-shot Revision | Likely-acceptable *if* specific changes (possibly new experiments) are made | Treat as a second deadline: do every required item, resubmit next cutoff |
| Reject | Structural: wrong metric, no real-device evidence, thin storage contribution | Reframe or reroute (OSDI/ATC/EuroSys/HotStorage/TOS); do not lightly resubmit unchanged |

The strategic reading: write the initial submission so that whatever is weakest is **fixable in a
one-shot revision** (a measurement you can add, a baseline you can tune, a crash test you can run)
rather than **structural** (a study design or device set you cannot redo). The process rewards
papers whose gaps are experiments, not premises.

## What a one-shot revision actually is

- **Bounded:** the decision comes with a summary of merits and a concrete list of required changes;
  detailed resubmission instructions follow within days.
- **Can require new experiments:** unlike light shepherding, the instructions may say "compare
  against system X" or "measure at steady state on device Y" — real work, not just editing.
- **One shot:** the revised paper, resubmitted at the *subsequent* deadline, can only be **accepted
  or rejected** — there is no second revision. The revision must fully satisfy the list.
- **Exclusive:** during the revision the paper is **still under review at FAST** and may not be
  submitted elsewhere unless withdrawn.

## How FAST differs from its siblings

- **vs. OSDI/ATC/SOSP:** those are general-systems venues; FAST is storage-specialized, so the
  review weights storage-specific evidence (device state, endurance, crash consistency) that a
  general-systems PC might not probe as hard. Never assume a shared calendar or template.
- **vs. a journal R&R:** a one-shot revision is *bounded and terminal* (accept/reject after one
  round), unlike an open-ended journal revise-and-resubmit that can iterate.
- **vs. a single-deadline conference:** FAST's two deadlines mean a revision or a near-miss has a
  scheduled next on-ramp within the same year — plan around it.

## Who reads you

Expect storage-subarea reviewers. They look for the device table and firmware, ask whether SSDs were
preconditioned and whether latency is reported at the tail, check that baselines are tuned, and often
want the crash-consistency test for any durability claim. Vague measurement descriptions get caught,
not skimmed.

## Where author leverage actually exists

```text
[Before submission]  topic tags + a crisp storage framing -> reviewer pool   (largest lever)
[Author response]    factual corrections, pointers to existing evidence, a concrete feasible plan
[Shepherding]        make exactly the bounded fixes; the shepherd is an ally, not an adversary
[One-shot revision]  the strongest lever: do every required item (incl. new experiments), resubmit
[After reject]       no lengthy appeal; reroute to a sibling storage/systems venue or ACM TOS
```

A response moves borderline papers when it corrects a misreading or supplies a measurement a
reviewer said was missing; it does not move papers when it argues taste. In a one-shot revision, a
required item left undone is what turns the terminal second read into a rejection.

## Misreadings to avoid

- **Treating a one-shot revision as a guaranteed accept** — it is terminal and can be rejected;
  budget its experiments like a deadline.
- **Treating shepherding as license to expand scope** — do the bounded fixes, nothing more.
- **Treating the response as a debate** — the PC discussion decides; your text is evidence for an
  advocate.
- **Projecting last year's cadence** — deadline count, response windows, and revision timing are
  decided per edition.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / response / shepherding / one-shot revision / accepted
[Decision category] accept / accept-with-shepherding / one-shot revision / reject, with the driving criterion
[Criterion map] each review point -> storage-contribution | device evidence | baseline | tail latency | consistency | clarity
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / parallel submission during revision / unsupported new claims
```
