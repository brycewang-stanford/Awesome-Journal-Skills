---
name: cc-peer-review-revision
description: Use when responding to Cancer Cell (Cell Press) reviewer reports — planning new experiments, writing a point-by-point response, and calibrating claims for revision. It structures the rebuttal and revision; it does not run the experiments or design them from scratch.
---

# Peer Review & Revision (cc-peer-review-revision)

## When to trigger

- A decision letter with reviewer reports has arrived (major/minor revision)
- You must triage requested experiments vs. textual changes
- Reviewers ask for additional in vivo / human validation or rigor fixes
- A consultative / cross-referee comment requires reconciling reviews

## Cell Press review context

Cancer Cell uses editorial assessment plus external peer review, and Cell Press can run **consultative (cross-referee) review** where reviewers see each other's comments. Practical implications:

- Reviewers may converge on shared concerns — address the **cross-cutting** issue, not just each bullet.
- The editor's letter signals which points are **essential** vs. optional; prioritize those.
- New experiments that strengthen orthogonal validation (in vivo / human) carry the most weight.

## Triage every comment

| Reviewer ask | Response mode |
|--------------|---------------|
| "Does this hold in vivo / in patients?" | New experiment (highest priority) — plan via `cc-study-design` |
| "Cell line unauthenticated / antibody not validated" | Rigor fix — `cc-reporting-standards` |
| "n unclear / pseudo-replication / wrong test" | Reanalyze + report — `cc-statistics` |
| "Representative image without quantification" | Quantify across replicates — `cc-figures-tables` |
| "Overstated claim" | Narrow the claim — `cc-writing-style` |
| "Missing control / rescue" | Add control experiment |
| Disagreement / out-of-scope request | Respectful, evidence-based pushback |

## Point-by-point response structure

For **each** comment:

1. Quote the reviewer's point verbatim.
2. State the change: new data, reanalysis, or text edit.
3. Point to **where** in the revision it appears (new Figure 4C, Methods p. X, lines Y–Z).
4. If you disagree, give a courteous, data-backed rationale — do not ignore it.

Open the response with a brief summary of the major new experiments and how the paper improved. Keep tone professional and concrete; reviewers and editor read this closely.

## Revision discipline

- Do not over-revise into a different paper; address what was asked.
- When adding in vivo / human data, carry through the **same rigor** (controls, `n`, randomization, blinding, deposition of any new datasets).
- Update the Key Resources Table, availability statement, and statistics for any new experiments.
- Re-run the `cc-submission` preflight before resubmitting.
- If you cannot do an experiment, explain why and offer the strongest feasible alternative.

## Worked micro-example: a point-by-point entry

**Reviewer 2, comment 3 (verbatim):** "The MARK7 phenotype is shown only in cell lines. Does loss of
MARK7 restrain tumor growth in an immunocompetent in vivo setting?"

**Response (the Cancer Cell pattern):**

> We agree this was the central gap. We generated *Mark7*-conditional autochthonous tumors and, in a
> new **Figure 5D–F**, show that MARK7 loss reduced tumor burden and restored intratumoral CD8⁺ T cell
> infiltration (n=9 vs. 10 mice; randomized to arms; blinded histology scoring; log-rank p reported in
> the legend). The in vivo RNA-seq is deposited under GEO [accession] (KRT updated). We have accordingly
> revised the Summary and Discussion to state a "candidate vulnerability for checkpoint combination"
> rather than a "therapeutic target," matching the evidence now in hand.

Note the moves: it concedes the point, delivers the highest-value experiment (in vivo, immunocompetent),
carries full rigor (`n`, randomization, blinding), deposits the new data, and **narrows the claim in the
same breath** — the reviewer sees the manuscript improve, not merely defend itself.

## Framing pushback that survives consultative review

Because reviewers may see each other's reports, a rebuttal that dismisses one referee can alienate the
panel. When you decline an experiment:

- Grant the scientific premise before explaining the constraint (feasibility, timeline, model
  availability, or that the request tests a different hypothesis).
- Offer the strongest feasible substitute (orthogonal assay, existing cohort reanalysis, published data).
- Where a request is genuinely out of scope, say what the paper *does* claim and confine the finding
  accordingly rather than arguing the reviewer is wrong.

## Cancer Cell revision failure modes

- Adding an in vivo experiment with a lower bar than the original (no randomization, `n` of 3, no
  blinded scoring) — reviewers notice the rigor drop immediately.
- Answering the "does it hold in patients?" comment with more cell-line data.
- Depositing nothing new even though the revision generated sequencing or proteomics data.
- Re-broadening the Summary/Highlights after narrowing the Results — front matter and body must agree.
- A rebuttal letter that resolves minor textual points in detail but leaves the essential mechanistic
  ask half-answered.

## Checklist

- [ ] Every reviewer point addressed individually; none skipped
- [ ] Essential (editor-flagged) points prioritized and fully resolved
- [ ] Cross-cutting concern shared across reviewers identified and answered
- [ ] New experiments carry full rigor and `n`; new datasets deposited
- [ ] Each response points to the exact location of the change
- [ ] Claims narrowed where evidence did not grow
- [ ] Polite, evidence-based rationale for any disagreement
- [ ] KRT, statistics, and availability statement updated; preflight re-run

## Anti-patterns

- Selectively answering easy comments and ignoring hard ones
- Adding new data with weaker rigor than the original (no controls, undefined `n`)
- Dismissive or defensive rebuttals to disagreements
- Claiming a change was made without pointing to where
- Re-broadening claims the reviewers asked you to narrow
- Forgetting to deposit datasets generated during revision

## Output format

```
【Decision】major / minor revision
【Essential points】editor-flagged: [...]
【Cross-cutting concern】...
【New experiments planned】(rigor + n + deposition): [...]
【Per-comment plan】R1.1 → ...; R1.2 → ...; R2.1 → ...
【Claims to narrow】...
【Pushback (with rationale)】...
【Next step】execute revisions → re-run cc-submission preflight
```
