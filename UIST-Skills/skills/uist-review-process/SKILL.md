---
name: uist-review-process
description: Use when interpreting the UIST review pipeline — anonymous PC-plus-external review of papers and videos, the rebuttal's role, PC-meeting decisions, conditional acceptance mechanics, reading systems-reviewer psychology, and choosing the demo/poster fallback or resubmission path after a rejection.
---

# UIST Review Process

Understanding how UIST decides is mostly understanding who decides: a program
committee of people who build interactive systems, supported by external reviewers
drawn from the same community, converging in discussion and a PC meeting. The venue
is single-track and relatively intimate — the person reviewing your haptics paper
probably built a haptics device. The pipeline facts below are the 2026 cycle's
(verified 2026-07-08); exact committee mechanics beyond the published dates are
待核实 each year.

## The 2026 pipeline

| Stage | 2026 timing | What happens to your paper |
|---|---|---|
| Submission closes | Mar 31 | PDF + video + supplement enter PCS |
| Review period | April-May | PC members and externals review paper *and* video |
| Rebuttal | May 28 - Jun 5 | Authors respond in ≤ 5,000 characters |
| Discussion + PC meeting | June | Recommendations formed from submission, rebuttal, reviews, and reviewer/PC discussion |
| Notification | Jun 27 | Accept (conditional), or reject |
| Camera-ready | Jul 24 | Conditions from the rebuttal must be delivered |

Two structural notes: the decision explicitly weighs the rebuttal and the
inter-reviewer discussion, so the rebuttal is a real instrument (see
`uist-author-response`); and acceptances are **conditional** — the notification is a
contract whose terms you wrote yourself in the rebuttal.

## How systems reviewers actually read

- **Video first, skeptically.** The initial question is "does this thing exist and
  work as claimed?" A missing video for a highly dynamic system starts the review
  from doubt.
- **Novelty as capability delta.** Reviewers pattern-match against the systems
  canon; the related-work table is where they check whether you know it (see
  `uist-related-work`).
- **Implementation as competence signal.** Vague engineering prose reads as either
  concealment or shallow work; specific parameters and honest failure boundaries
  read as craft.
- **Evaluation-matching, not evaluation-maximizing.** A ritual study annoys
  reviewers more than a well-argued demonstration portfolio (see
  `uist-experiments`).
- **Enthusiasm is a real variable.** UIST reviewers reward inventiveness; a
  technically modest but genuinely delightful idea can outscore a heavy but dull
  one. Write and film for the builder's grin.

## Reading your reviews

Sort every reviewer point into one of four bins before reacting:

```text
FACTUAL ERROR      reviewer misread a mechanism/number  -> correct, citing section
EVIDENCE GAP       claim outruns measurement            -> concede scope or add data
NOVELTY CHALLENGE  "system X already does this"         -> capability-delta answer
TASTE              "I would have built it differently"  -> acknowledge, do not litigate
```

The bins predict rebuttal leverage: factual errors and novelty challenges are
winnable in 5,000 characters; evidence gaps are winnable only if the evidence
already exists; taste is never winnable and costs characters.

## Discussion dynamics in a small committee

Between rebuttal and notification, your paper's fate is a conversation you cannot
attend. What is knowable about that phase shapes what you should have done earlier:

- Reviews converge through discussion; a champion reviewer arguing from your
  rebuttal's specifics is the mechanism by which mixed reviews become accepts.
  The rebuttal's job is to arm that champion (see `uist-author-response`).
- Expertise is uneven by design — a paper spanning fabrication and ML gets one
  deep expert per half; the review that "missed the point" often belongs to the
  other half's expert, and answering it teaches the whole committee.
- Single-track scale means PC members see a broad slice of the year's
  submissions; "we saw three of these this cycle" is a real dynamic, and a crisp
  capability delta is the defense.
- Scores move at the meeting. Borderline papers with concrete, deliverable
  rebuttal promises are cheap accepts; borderline papers with defensive rebuttals
  are cheap rejects.

## Calibrating expectations by decision class

| Outcome signal | What it usually means | Your move |
|---|---|---|
| Conditional accept, short condition list | Committee wants the paper; conditions are the contract | Deliver precisely; see `uist-camera-ready` |
| Reject, reviews ask for more evaluation | Evidence gap — repairable in one cycle | Repair plan from the review bins |
| Reject, reviews dispute novelty | Related-work or delta failure | Fix positioning before anything else |
| Reject, reviews question the contribution's home | Venue mismatch | Re-run `uist-topic-selection` honestly |

## After rejection: the three exits

1. **Adjunct fallback, same conference.** A rejected paper's system is often a
   strong Demo or Poster submission to the *same* edition — the adjunct deadlines
   fall after paper notification. This keeps the work visible, collects hallway
   review, and stakes a dated adjunct publication. Remember the 2026 rule: one
   adjunct track per work, not both.
2. **Repair and resubmit** to UIST next year: use the review bins as the work plan;
   evidence-gap rejections are the most repairable class.
3. **Re-route** when reviews reveal a venue mismatch — "the contribution is the
   study, not the system" is a CHI/CSCW signal, and `uist-topic-selection` should be
   re-run rather than argued with.

## Confidentiality and conduct

Reviews, reviewer identities, and PC discussion are confidential; do not quote
reviews publicly or attempt reviewer identification. Contact the program chairs
(program2026@uist.org for the 2026 cycle) only for process failures — a genuinely
missing review, a compromised anonymity situation — not to relitigate scores.

## Output format

```text
[Phase] under review / rebuttal / decided-conditional / decided-reject
[Review bins] factual <n> · evidence <n> · novelty <n> · taste <n>
[Leverage estimate] rebuttal-winnable points and why
[If rejected] adjunct fallback / repair-resubmit / re-route — with the deciding review line
[Process flags] <anything warranting a chairs contact>
```
