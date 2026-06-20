---
name: jmis-review-process
description: Use when calibrating expectations for the Journal of Management Information Systems (JMIS) editorial process — the EIC-led, email-intake, double-anonymized review by Associate Editors and expert referees, likely decision types, and timing. Sets expectations and revision posture; it does not draft the response letter (jmis-rebuttal).
---

# Review Process (jmis-review-process)

## When to trigger

- Before submitting, to understand who decides and how long it takes at JMIS
- A decision letter arrived and you need to read its severity correctly before responding
- You are weighing JMIS against MISQ/ISR/JAIS on process and turnaround
- You want to know what a desk-reject vs. a review-and-reject signals

## How JMIS review actually runs

JMIS is an **Editor-in-Chief-led** journal: founding and current EIC **Vladimir Zwass** receives submissions directly by email and steers the process. Papers are **refereed in a double-anonymized process** by internationally recognized expert referees and by **Associate Editors** on the Editorial Board. Practically, this means:

- **The EIC is the first gate.** A paper that is out of scope (not an IS-management/economics question), over length, or not anonymized can be returned or desk-rejected before external review. Fit is judged against JMIS's management/economics-of-IS identity, not generic IS breadth.
- **AEs and referees carry the substantive review.** Expect method-literate referees who will press on identification (empirical), assumptions and insight (analytical), measurement and CMB (behavioral), and utility-vs-baselines (design-science) — and on whether the contribution matters for IS management.
- **Decisions** typically span reject, major revision, minor revision, and (rarely on a first round) accept. A major revision is an opportunity, not a soft reject; a reject-and-resubmit is distinct from a revision and resets the clock. (检索于 2026-06；以官网为准.)

## Read the decision letter for what it is asking

| Signal in the letter | What it usually means | Posture |
|----------------------|-----------------------|---------|
| "Contribution to IS is unclear / incremental" | A framing problem, possibly fatal if the question is not IS-management-shaped | Revisit `jmis-contribution-framing`; consider fit |
| "Identification / endogeneity" (empirical) | Reviewers doubt the causal claim | Strengthen design/analysis before reframing |
| "Construct validity / common-method bias" (behavioral) | Measurement is not trusted | Fix measurement model; re-test CMB |
| "Robustness / generalizability" | Effect believed but not yet solid | Add robustness; bound the claim |
| Desk return for length/anonymization | Process, not substance | Fix and resubmit per `jmis-submission` |

## What the EIC-led model means for you, concretely

Because intake is the EIC's email and the EIC steers assignment, two things follow that a portal-driven journal would not surface. First, **scope discipline is front-loaded**: the EIC can return a paper that is not an IS-management/economics question before it ever reaches a referee, so the time you spend at `jmis-topic-selection` and `jmis-contribution-framing` is the cheapest insurance against a fast return. Second, the **AE is your interlocutor on the substance**: the AE synthesizes the referees and signals the editorial direction, so when you eventually respond (`jmis-rebuttal`) you are persuading the AE that concerns are *resolved*, not just answered. Read the AE letter as the decision; read the referee reports as the evidence the AE is weighing.

## Match the review style to your evidence type

The substantive pressure differs by archetype, and anticipating it shortens the cycle:

| Archetype | Where referees press hardest |
|-----------|------------------------------|
| IT-value / firm econometrics | endogeneity of IT investment; whether the design supports a causal verb |
| platform / e-commerce | selection on platform data; whether the network mechanism is identified, not assumed |
| behavioral survey / experiment | construct validity, discriminant validity, common-method bias, manipulation realism |
| analytical / economic model | the assumptions, and whether the insight survives relaxing them |
| design-science / ML | utility vs. credible baselines and managerial relevance, not algorithmic novelty |

## Calibrate timing and expectations

JMIS is a quarterly with a single EIC and a board of AEs; turnaround depends on referee availability, so plan for a multi-month first round and budget real time for a major revision. Exact current turnaround statistics are **待核实** — check the journal page or recent author reports rather than assuming. Treat a major-revision invitation as a genuine path to acceptance if you can answer the substantive concerns, and do not confuse it with a reject.

## Checklist

- [ ] You know the decision type (desk return / reject / reject-resubmit / major / minor / accept) and what resets the clock
- [ ] The binding concern is classified (fit / identification / measurement / robustness / process)
- [ ] You have separated fatal framing problems from fixable evidence gaps
- [ ] Expectations on timing are realistic for an EIC-led quarterly
- [ ] Any quoted turnaround/acceptance statistic is marked 待核实 unless sourced
- [ ] The revise-vs-reroute decision rule has been applied to the binding concern
- [ ] The AE letter, not the raw referee reports, is read as the decision signal

## Anti-patterns

- Reading a major revision as a polite rejection (or vice versa)
- Responding before classifying whether the core problem is fit, evidence, or process
- Assuming a fast portal-style turnaround — this is an EIC-led email process
- Treating a desk return for length/anonymization as a substantive rejection
- Quoting acceptance rates or review times as fact without a source
- Revising a paper whose core problem is fit, on sunk-cost grounds, instead of rerouting
- Treating the referee reports as the decision rather than the AE's synthesizing letter
- Underestimating how front-loaded scope discipline is in an EIC-managed intake

## Decide whether to revise or reroute

Not every revision invitation is worth taking, and a clean reject sometimes signals a fit problem better solved by rerouting. Use a simple decision rule: if the binding concern is **fit/contribution** and the question is not really an IS-management/economics question, a revision will likely fail again — reconsider whether MISQ, ISR, JAIS, or an economics/CS venue is the true home before reinvesting. If the binding concern is **evidence** (identification, measurement, robustness) and you can plausibly produce the missing analysis within the revision window, a major revision is a genuine path to acceptance. If it is **process** (length, anonymization, scope-of-claims), fix and resubmit. Sunk-cost reasoning — "we already emailed it to JMIS" — is not a reason to revise a paper whose question belongs elsewhere.

## Set author expectations before the wait

Tell coauthors what an EIC-led quarterly looks like so silence is not misread: a multi-month first round is normal, a major revision is the most common positive first-round outcome at a top journal, and the AE's letter — not the harshest referee — sets the agenda for the revision. Decide up front who will own which class of revision (identification, measurement, exhibits, prose) so that when the letter arrives the team moves into `jmis-rebuttal` without relitigating roles.

## Output format

```text
【Decision type】desk-return / reject / reject-resubmit / major / minor / accept
【Binding concern】fit / identification / measurement / robustness / process
【Fatal vs. fixable】[...]
【Timing expectation】realistic horizon (statistics 待核实)
【Next step】jmis-rebuttal (if revision) or revisit earlier skill (if framing/fit)
```
