---
name: mgsci-review-process
description: Use to understand how Management Science (INFORMS) review and decisions work — the Department/area-editor desk screen, the high desk-reject rate, double-anonymized refereeing, the cross-department fit bar, turnaround targets, and how to read a decision letter — before or after submitting. It explains the process; it does not draft the response (mgsci-rebuttal).
---

# Review Process (mgsci-review-process)

## When to trigger

- You want to know what happens to a submission and how long it takes
- You are unsure who decides (Department Editor vs Associate Editor vs Editor-in-Chief)
- A paper was desk-rejected and you need to understand why
- You received a decision letter and want to read it correctly before responding

## How a submission flows

1. **Department/area routing.** A submission is channeled into a specific **Department** (e.g., Accounting; Behavioral Economics and Decision Analysis; Business Strategy; Data Science; Finance; Information Systems; Operations Management; Optimization and Decision Analytics; Revenue Management & Market Analytics; Stochastic Models and Simulation). The **Department Editor owns the desk screen and the standards** for that field.
2. **Desk screen.** The Department Editor decides whether the paper goes to external review. **A high share is desk-rejected** (reported ~50–60% screened out before external review — **approximate / 待核实**), commonly on **fit** ("better suited to Operations Research / M&SOM / Marketing Science") or insufficient rigor/contribution.
3. **External review.** Papers passing screen go to roughly **2–3 reviewers**, often coordinated by an **Associate Editor** (~ figures **approximate / 待核实**). Review is **double-anonymized** — neither side sees the other's identity.
4. **Decision.** The Department Editor recommends; the **Editor-in-Chief (Christoph Loch, term 2024–2026)** provides final oversight and **cross-department arbitration** for ambiguous-fit papers.

## The cross-department fit bar

Beyond field rigor, papers are judged on whether they **belong in Management Science** versus a sister INFORMS journal. Ambiguous-fit papers spanning departments are discussed across the editorial team, and a large share are redirected. Expect "fit" to be a first-order screen, not an afterthought.

## Turnaround

The journal aims for an **ambitious turnaround** — reportedly giving high-quality feedback to ~90% of authors within ~90 days (**approximate / 待核实**, among the more aggressive commitments in top-tier business publishing). Acceptance triggers **Data and Code Disclosure verification** by the Data Editor, which adds ~17 days on average before publication.

## Reading a decision letter

- **Desk reject on fit** → re-aim (see `mgsci-topic-selection`) or target the named sister journal; usually not worth appealing.
- **Reject after review** → the contribution or rigor did not clear the bar; a major reframe is needed.
- **Major revision (R&R)** → a real opportunity; the Department Editor's framing letter signals which reviewer points are decisive. Go to `mgsci-rebuttal`.
- **Minor revision** → rare early; address precisely and quickly.

Read the **Department Editor's letter first** — it tells you which reviewer concerns are binding and which are advisory.

## Desk-reject reason map

Because Management Science is the multidisciplinary INFORMS flagship, the desk screen is run by a Department Editor enforcing that department's rigor bar and the cross-department fit test.

| Desk-reject reason | What it signals | Implied next move |
|--------------------|-----------------|-------------------|
| "Better suited to a sister INFORMS journal" | A routing verdict, not necessarily quality | Re-aim or target the named journal |
| "Contribution does not clear the bar" | Rigor present, decision insight thin | Reframe; do not just resubmit |
| "No clear home department" | Ambiguous-fit; arbitration redirected it | Name a department + the bridge |

## Worked micro-example (illustrative): two letters

Letter A: "Interesting model, but the algorithmic contribution would be better appreciated at Operations Research." This is a routing verdict — the work may be excellent, just mis-homed; do not appeal. Letter B: "The identification does not rule out selection, and the managerial implication is unclear." This is a substantive reject on two flagship bars (empirical leverage and a decision-relevant contribution); a major reframe plus a stronger design is needed. Distinguishing routing from substantive rejects decides whether you re-aim or rebuild.

## Referee-pushback patterns and the venue-specific fix

- **"Which department is this, and does it clear that bar?"** Make the home department explicit at submission so the right editor desk-screens it; confirm the design meets that department's standard.
- **"This belongs at a sister INFORMS journal."** Surface the cross-department travel that distinguishes a flagship paper.

## Calibration anchor

Desk-reject shares, reviewer counts, and turnaround targets above are approximate and evolve — treat them as orientation, and confirm current figures against editorial statements.

## Anti-patterns

- Treating a fit-based desk reject as a quality verdict (it is often a routing verdict).
- Ignoring the Department Editor's prioritization and weighting all reviewer comments equally.
- Assuming acceptance means immediate publication — disclosure verification still runs.

## Output format

```
【Stage】desk screen / under review / decision received
【Department & decider】Department Editor / AE / EiC
【Decision type】desk-reject(fit) / reject / R&R / minor
【Binding concerns】[from the DE letter]
【Next step】mgsci-rebuttal (R&R) or mgsci-topic-selection (re-aim)
```
