---
name: uai-review-process
description: Use when reasoning about UAI peer review on OpenReview, including bidding, double-blind evaluation against the correctness, novelty, backing, and clarity criteria, the author-response window, the reviewer-and-area-chair discussion that follows it, decision timing, spotlight versus poster outcomes, and PMLR publication of accepted papers.
---

# UAI Review Process

Use this to model what happens to a UAI submission after upload, and to time author
effort where it changes outcomes. Stage dates below are the published 2026 pipeline
(verified 2026-07-08); the shape tends to persist across cycles, the dates never do.

## The 2026 pipeline, stage by stage

| Stage | 2026 window | Who acts | Author leverage |
|---|---|---|---|
| Submission closes | Feb 25 (AoE) | Authors | Total — last moment anything enters the record |
| Bidding | Mar 2–9 | SACs, ACs, reviewers | Indirect: title, abstract, subject areas drive matching |
| Review writing | Mar 21 – Apr 11 | Reviewers | None — the paper speaks alone |
| Author response | Apr 23 – May 2 | Authors | High on misreadings; low on true weaknesses |
| Reviewer–AC discussion | May 2–8 | Reviewers + ACs | Only via the response already filed |
| Notification | Jun 1 | Program Chairs | None |
| Camera-ready | Jul 27 | Authors | Presentation of accepted content |
| Conference | Aug 17–21 | Everyone | Talks, posters, corridor conversations — reputation, not decision |

Note the gaps: reviews are written weeks before authors see them, and the decisive
reviewer–AC conversation happens after authors go silent. Both asymmetries reward
papers and responses that anticipate objections rather than react to them.

## Matching is an author-controlled variable

Bidding means your title, abstract, and subject-area selections are routing decisions.
An abstract that says "probabilistic" but hides the causal-identification core will be
bid on by the wrong reviewers, and misrouted reviews are the hardest to respond to.
Choose OpenReview subject areas to describe what a reviewer must know to verify the
paper, not what makes it sound broad.

## Who reviews at UAI

The pool concentrates on probabilistic inference, graphical models, causality, Bayesian
statistics, decision theory, and learning theory. The 2026 reviewer instructions asked
reviewers to state clearly what clarification they want from authors — expect direct,
technical questions. Planning consequences:

- At least one reader will attempt your proofs or re-derive your estimator. Write
  assumption chains for verification, not persuasion.
- Empirical-only papers face a pool that instinctively asks "where is the uncertainty in
  your uncertainty estimate?" — variance reporting is table stakes.
- The author agreement (one author reviews if asked) means your own team may be inside
  someone else's pipeline simultaneously; wall off conflicts early and honor
  confidentiality both ways — review misconduct falls under the AUAI code of conduct.

## Scale and format context

UAI is a compact meeting by ML-conference standards — each edition fits a single
PMLR volume (2025: v286), far smaller than NeurIPS-scale venues. Practically: your
paper is likelier to be read by people who work on exactly its topic, reviewer
anonymity is thinner in niche subfields (write accordingly), and poster sessions
carry real technical conversation. Session structure and track layout are set per
edition — verify rather than assume.

## Reading a UAI decision

Accepted papers are all presented as posters plus spotlights (physically or remotely in
2026), with longer slots for selected papers. So an acceptance may arrive with a
presentation-format distinction; treat a longer slot as a visibility bonus, not a
different publication class — the PMLR volume records all accepted papers identically.

For rejections, extract signal by axis:

```text
Post-decision triage (fill one line per review):
R1: axis=correctness  fixable=yes  action=repair Lemma 2 edge case before resubmission
R2: axis=backing      fixable=yes  action=add multi-seed study + calibration curves
R3: axis=novelty      fixable=no   action=re-scope contribution or change venue
→ If any "novelty, fixable=no" comes from a correct reading, the next venue decision
  matters more than any revision (see uai-topic-selection).
```

## What authors see versus what actually happens

Planning improves when the hidden half of the pipeline is explicit:

- **Visible to authors:** the submission form, the reviews when released, the response
  box, the decision, and (post-decision) the meta-review if issued.
- **Hidden from authors:** bidding outcomes and assignment quality; reviewer
  confidence scores as ACs weigh them; the May reviewer–AC discussion; how borderline
  stacks are ranked at the program level.
- **Consequences:** you cannot fix a bad assignment after bidding — only prevent it
  via abstract and subject areas; you cannot join the May discussion — only arm it
  with a response ACs can quote; you cannot appeal taste — only demonstrable factual
  error, through the chairs.

## Signals to log for the next cycle

Whatever the outcome, the review set is calibration data about how this venue reads
your group's work. Record: which criterion drew the most text; whether the appendix
was demonstrably read; which baselines reviewers asked for unprompted; which
subject-area choices produced well-matched reviewers. Two cycles of such notes
outperform any generic advice about "what UAI wants".

## If the process misfires

- A review that misstates what the paper does (not disputes — misstates) is
  response-window material: quote the submission, politely, with locations.
- A review that appears to have skipped the appendix proofs is still your problem to
  solve: restate the two-line version in the response and point at the full argument.
- Suspected conflicts, plagiarized review text, or conduct issues go to the program
  chairs privately — never into the public forum thread.
- After a final decision, the productive appeal is a better paper at the next venue;
  UAI has no rolling revise-and-resubmit track.

## Confidentiality and conduct boundaries

- Submissions are confidential inputs to the process; do not quote reviews publicly or
  contact reviewers. Escalation path is the program chairs (uai2026chairs+program
  address for that cycle).
- The AUAI code of conduct covers the review ecosystem, official communication
  channels, and social media, and names fabrication, falsification, and plagiarism as
  misconduct.
- LLM-use policy for authors or reviewers was not published for 2026 (待核实); where a
  cycle is silent, default to the confidentiality rule — no feeding others' submissions
  or reviews into external services.

## Output format

```text
[Stage now] pre-submission / under review / response window / awaiting decision / decided
[Days to next transition] <n, from the current official dates>
[Routing quality] subject areas + abstract match actual verifiers? 
[Predicted objection axes] <correctness / novelty / backing / clarity, ranked>
[Process risks] <conflicts, confidentiality, volunteer-reviewer load>
```
