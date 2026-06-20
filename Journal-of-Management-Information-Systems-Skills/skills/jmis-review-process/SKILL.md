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

## Calibrate timing and expectations

JMIS is a quarterly with a single EIC and a board of AEs; turnaround depends on referee availability, so plan for a multi-month first round and budget real time for a major revision. Exact current turnaround statistics are **待核实** — check the journal page or recent author reports rather than assuming. Treat a major-revision invitation as a genuine path to acceptance if you can answer the substantive concerns, and do not confuse it with a reject.

## Checklist

- [ ] You know the decision type (desk return / reject / reject-resubmit / major / minor / accept) and what resets the clock
- [ ] The binding concern is classified (fit / identification / measurement / robustness / process)
- [ ] You have separated fatal framing problems from fixable evidence gaps
- [ ] Expectations on timing are realistic for an EIC-led quarterly
- [ ] Any quoted turnaround/acceptance statistic is marked 待核实 unless sourced

## Anti-patterns

- Reading a major revision as a polite rejection (or vice versa)
- Responding before classifying whether the core problem is fit, evidence, or process
- Assuming a fast portal-style turnaround — this is an EIC-led email process
- Treating a desk return for length/anonymization as a substantive rejection
- Quoting acceptance rates or review times as fact without a source

## Output format

```text
【Decision type】desk-return / reject / reject-resubmit / major / minor / accept
【Binding concern】fit / identification / measurement / robustness / process
【Fatal vs. fixable】[...]
【Timing expectation】realistic horizon (statistics 待核实)
【Next step】jmis-rebuttal (if revision) or revisit earlier skill (if framing/fit)
```
