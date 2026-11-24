---
name: eurosys-review-process
description: Use when reasoning about how EuroSys decides papers — the two independent yearly rounds feeding one April conference, HotCRP double-blind reviewing, the accept/revise/reject outcome triple, the same-season resubmission ban after rejection, and community structures like the Shadow PC that shape who reviews.
---

# EuroSys Review Process

Use this to model the decision machinery around a EuroSys submission. Facts
below are the EuroSys 2027 cycle as re-verified on 2026-11-24 from the CFP and
conference pages; review counts and the PC-meeting format are not published and
live inside each HotCRP instance.

## One conference, two juries

Each EuroSys edition accepts papers through two temporally separate rounds —
for 2027: spring (papers May 14, 2026 → notification August 21, 2026) and fall
(papers September 24, 2026 → notification January 29, 2027). Both cohorts are
published in the same proceedings and presented at the same April conference.
Strategically this means:

- Your competition is round-local; the PC calibrates within the round it reads.
- A spring reject cannot simply "try again in the fall": the CFP makes a paper
  that was not accepted **ineligible for the immediately following cycle** — in
  practice it returns at the same round of the next edition, a full year later.
- A revision offer, by contrast, explicitly bridges rounds: revise-and-resubmit
  at the *following* cycle, against the issued list of concerns; the revision is
  treated as a submission to that later deadline and is not guaranteed acceptance.

## The outcome triple

| Outcome | What it means | Author's next move |
|---|---|---|
| Accept | Tentative until a PC shepherd approves the revised version | Shepherd revision, camera-ready + artifact evaluation |
| Revise-and-resubmit | Conditional path to the following cycle | Concern-by-concern execution plan |
| Reject | Ineligible for the immediately following cycle | Substantial rework, or a different venue |

The revision is evaluated once, against the concerns; a rejected revision is
ineligible for the cycle after it, so there is no chain of revision offers.

## Who is reading

- A double-blind HotCRP process: reviewers do not see authors, and conflicts
  declared at abstract registration drive assignments.
- The PC spans the breadth of European and international systems research —
  kernels, distributed systems, storage, cloud runtimes, virtualization,
  systems security, and increasingly systems-for-ML. Expect at least one
  reviewer whose home sub-area differs from yours; the paper's framing must
  carry them.
- EuroSys has repeatedly run a **Shadow PC** (e.g., `2026.eurosys.org/shadow-pc.html`),
  where early-career researchers review real submissions in parallel as
  training. Practical consequence: write for a rigorous but possibly junior
  reader, and expect the community's reviewing norms to be unusually explicit
  and well-documented.

## What moves a PC discussion here

1. **Verifiable evaluation fairness** — tuned baselines, named versions,
   disclosed hardware — because the deepest systems-review instinct is to
   distrust a benchmark table.
2. **A mechanism the reviewer can retell** — if the design section cannot be
   summarized in three sentences at the PC meeting, no champion can defend it.
3. **Claims scoped to evidence** — a paper that says where it loses earns the
   credibility spent by every paper that doesn't.
4. **Deployment plausibility** — EuroSys values systems that could run outside
   the lab; a purely synthetic setting needs an explicit bridge to practice.

## A round from the author's seat

Between the paper gate and notification (roughly fourteen weeks in the
2027 spring round: May 14 → August 21), the author-visible surface is
nearly silent. What happens behind it, in the standard HotCRP shape:

1. Bidding and assignment off the registered topics and conflicts.
2. First-round reviews; possibly a cut before additional reviews are
   commissioned on papers still alive.
3. Reviews released, then a two-day optional **author response** (2027 spring:
   July 29 → July 31, 2026; fall: January 6 → January 8, 2027), limited to factual
   corrections and answers to reviewer questions, ideally within 500 words.
4. Online PC discussion converging each paper into one of the three bins,
   with revision-condition lists drafted for the middle bin.
5. Notification, reviews, and — for the middle bin — the condition list.

The author-controllable inputs are all front-loaded: the registered
abstract (bidding quality), the conflicts (assignment sanity), and the
paper itself. Mid-round, the only lever is the two-day response.

## Conduct boundaries

- No reviewer contact outside the platform, no identity fishing, no
  parallel submission of the same work to another archival venue.
- Public talks, arXiv versions, tech reports and social-media posts are not
  concurrent submissions under the 2027 CFP, but the submitted version must use a
  substantially different title and system/tool name — so a seminar under the
  submission title is exactly what to avoid.

## Reading your reviews structurally

```text
For each review, extract:
  score-driver:   the sentence that explains the score (rarely the summary)
  fixability:     bounded experiment/rewrite  -> revision-compatible
                  identity-level objection    -> reject-compatible
  round-awareness: does the reviewer propose revision conditions?
Then ask: across reviewers, is there a coherent, enumerable condition list?
  yes -> argue toward the revision bin in the author response (facts and answers only)
  no  -> maximize the accept case on the strongest review's terms
```

## Output format

```text
[Round position] spring / fall, and days to its next gate
[Outcome forecast] accept / revision / reject, with the driving signal
[Condition-list coherence] <enumerable fixes or identity-level objections>
[Ban exposure] <date this paper may legally return if rejected>
[Response window] <reviews-available date -> responses-due date for this round>
```
