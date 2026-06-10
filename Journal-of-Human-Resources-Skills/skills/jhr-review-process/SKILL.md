---
name: jhr-review-process
description: Use when you need to understand and plan around the Journal of Human Resources (JHR) editorial process — single-anonymous review, the fast desk-reject without outside review, the reconciliation requirement, and the optional review-recycling shortcut. Sets expectations; it does not draft the paper.
---

# Editorial Process (jhr-review-process)

## When to trigger

- Setting expectations on timelines and decision types at JHR
- Deciding whether to attach a prior journal's reports to speed review
- Understanding why a paper might be desk-rejected without referees
- Wanting to pre-empt the reconciliation / sensitivity demands referees apply

## How JHR review works (verified 2026-06-01)

- **Single-anonymous (single-blind):** "Referees are anonymous, but author names are not kept from reviewers." The process is run by the **Editor (Anna Aizer, Brown; Michael Lovenheim, Cornell, from 2026-07-01)**, coeditors, and associate editors, with volunteer expert reviewers.
- **Fast desk-reject WITHOUT outside review.** Papers a handling editor/coeditor judges unlikely to survive review are **released quickly without being sent to referees**, at the editor's discretion. The **$175 fee does not guarantee outside review** and is **not refunded** for out-of-scope (management/personnel) papers — so the desk screen is the first real hurdle.
- **Reconciliation requirement (distinctive):** manuscripts are judged partly on whether they **reconcile their results with prior published work** on the same topic. Authors **may be required to run comparative estimation** (re-estimate under the prior literature's spec/sample) and **present sensitivity tests**. Build this in before submitting, not after a referee demands it.
- **Review-recycling shortcut (optional):** authors may **submit a prior journal's decision letter and referee reports**; JHR may use them — and may **contact the prior journal's editor or referees** — to speed review. Useful when a paper was close at another journal and the reports are constructive.

## How to act on it

- Treat the **desk screen** as the highest-leverage gate: a legible policy-relevant question, a clearly stated identifying variation, and a one-paragraph reconciliation note give the handling editor a reason to send it out.
- If a prior submission generated strong-but-fixable reports, consider attaching them — but only if your revision genuinely answers them.
- Anticipate the reconciliation ask in `jhr-data-analysis`: have the comparative estimates and sensitivity tests ready.

## Checklist

- [ ] Question and identifying variation legible in the first two pages (desk screen)
- [ ] Reconciliation with prior published estimates addressed up front
- [ ] Comparative estimation and sensitivity tests prepared
- [ ] Decision made on whether to attach prior-journal reports
- [ ] Scope confirmed (not HR-management) so the fee is not wasted

## Anti-patterns

- Assuming the fee buys outside review — it does not
- Ignoring prior published estimates that contradict yours
- Attaching old referee reports the revision does not actually address
- Burying the identifying variation past the desk-reading window

## Desk-screen simulation

Run the manuscript's first two pages against the questions a JHR handling
editor can realistically answer in one sitting:

1. Is this empirical microeconomics in a JHR field, or HR-management dressed in
   economics language?
2. What variation identifies the effect — is the design named (rollout, cutoff,
   lottery, instrument) by page two?
3. Is there a magnitude in policy units, or only "significant effects"?
4. Does the paper acknowledge the closest prior estimates and hint at the
   bridge?
5. Would a policy audience care if the answer flipped sign?

Illustrative contrast: "We examine determinants of teacher turnover" reads as
desk risk; "A pension-vesting cliff at year five lets us estimate how deferred
compensation retains teachers, and our retention effect is half the prior
descriptive literature's" survives the same screen. If two or more questions
fail, route back to `jhr-contribution-framing` before paying the fee.

## Timeline posture

JHR does not commit to public turnaround statistics, and stated desk-release
speed is "quickly" rather than a number — do not promise coauthors a specific
month, and confirm against the journal's current author guidelines for any
stated processing details. What is controllable: the desk screen is the fastest
gate, and review recycling can compress the refereeing stage when prior reports
are attached.

## What arrives with a decision

- A synthesizing letter from the handling editor — at JHR this letter, not any
  single report, defines the revision contract.
- Referee reports that commonly lead with identification (pre-trends, first
  stages, cutoff manipulation) and the reconciliation question before
  exposition.

## Output format

```
【Decision risk】desk-reject likelihood / why
【Reconciliation】prior estimates addressed? [Y/N]
【Sensitivity】comparative/robustness ready? [Y/N]
【Recycling】attach prior reports? [Y/N + reason]
【Next step】jhr-submission or jhr-rebuttal
```
