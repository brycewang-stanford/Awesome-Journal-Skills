---
name: qe-rebuttal
description: Use when a Quantitative Economics (QE) decision letter arrives (R&R or major/conditional revision) and a response strategy and letter are needed. Structures the revision and response; it does not redo the analysis (route to the relevant qe-* skill for that).
---

# Rebuttal & Revision (qe-rebuttal)

## When to trigger

- A QE decision letter arrived: revise-and-resubmit, or a conditional/major revision
- You have referee reports and need a response strategy
- You are unsure how to prioritize conflicting referee demands
- The revised manuscript exists and you need to draft the response letter

## QE reality: the coeditor's letter is the contract, and the clock runs ~12 months

At QE a **handling coeditor** owns the decision and synthesizes the referees (often including an Associate Editor). The **coeditor's letter ranks the issues** — it tells you which referee points are binding and which are optional; read it first and let it set priorities. **Revise offers are normally valid for 12 months**, so plan the analysis, estimation, and reproducibility work against that window rather than rushing a thin resubmission. Because QE is the empirical/quantitative ES journal, expect referees to probe **identification, estimation, robustness, and reproducibility** specifically — keep the public-posting and replication obligations in view as you revise.

## Triage protocol

1. **Decode the coeditor.** A point the coeditor underscores is binding; a point only one referee raised and the coeditor ignored is lower priority (still answer it).
2. **Classify every comment.** Tag each: *fundamental* (must add/redo analysis or estimation), *clarification* (rewrite/explain), or *disagreement* (you will push back, politely, with evidence).
3. **Sequence the work.** Do the analysis first — route fundamentals to `qe-identification-strategy`, `qe-data-analysis`, or `qe-tables-figures`; update the replication package via `qe-replication-and-data-policy`; *then* write the letter.
4. **Settle it with a check, not a fight.** If a robustness check, an added moment, or a Monte Carlo settles the point, run it; reserve disagreement for where the referee is genuinely mistaken.

## Response-letter structure

- **Opening:** thank the coeditor and referees; summarize the main changes in a short paragraph.
- **Point-by-point:** quote each comment, then respond — what you did + where in the revised paper it now appears (section/table/figure/page).
- **Disagreements:** state the referee's point fairly, then give the evidence-based reason you respectfully differ; offer a compromise (e.g., add to the Supplemental Appendix, ≤25 pages) where possible.
- **Reproducibility:** note any changes to data/code so the eventual ES Data Editor check stays clean.
- **Tone:** gracious, concrete, never defensive.

## Checklist

- [ ] Coeditor's priorities decoded and used to rank responses
- [ ] Every referee comment classified (fundamental / clarification / disagreement)
- [ ] All fundamental requests resolved with actual new analysis/estimation, not promises
- [ ] Each response cites the exact location of the change in the revised paper
- [ ] Disagreements are evidence-based, fair, and offer a compromise
- [ ] Replication package and public posting updated to match the revision
- [ ] Revised manuscript updated *before* the letter was written
- [ ] No significance asterisks reintroduced; no new over-claiming

## Anti-patterns

- Writing the response letter before the manuscript reflects the changes
- Promising future work instead of doing the analysis within the ~12-month window
- Arguing where an added moment / robustness check / Monte Carlo would settle it
- Letting the replication package drift out of sync with the revised results
- Defensive or curt tone; treating reports as attacks rather than help

## Output format

```
【Decision】R&R / major / conditional
【Coeditor's binding points】[...]
【Comment classification】fundamental: [...] / clarification: [...] / disagreement: [...]
【Analysis routed to】qe-identification-strategy / qe-data-analysis / qe-tables-figures
【Letter status】point-by-point with locations? [Y/N]
【Reproducibility synced】package + posting updated? [Y/N]
【Next step】resubmit via the ES portal (qe-submission for file checks)
```
