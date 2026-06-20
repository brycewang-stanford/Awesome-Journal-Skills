---
name: hrm-rebuttal
description: Use when drafting the revision and response letter after a Human Resource Management (Wiley "HRM") revise-and-resubmit — structuring point-by-point responses to the action editor and reviewers across the journal's developmental, multi-round, double-blind process. Drafts the response after revisions; it does not interpret the decision letter (hrm-review-process).
---

# R&R Response & Rebuttal (hrm-rebuttal)

## When to trigger

- You received an HRM R&R and have planned the revision (via `hrm-review-process`)
- You have made (or scoped) the manuscript changes and need to write the response document
- You must reconcile conflicting reviewer demands for the action editor
- A later-round decision asks you to defend or further revise prior changes

> Write the response letter **after** revising the manuscript, not before — it documents changes made, not promises. HRM's process is developmental and typically multi-round; resubmit the revised (still-anonymized) manuscript and the response document through Wiley **ScholarOne**, keeping the same action editor across rounds where possible (检索于 2026-06；以官网为准).

## Response-document structure

1. **Opening letter to the action editor.** Thank the editor and reviewers; summarize the most important changes in 2–4 sentences; explicitly state how you addressed the editor's stated priorities; note where reviewers conflicted and how you resolved it.
2. **Per-reviewer sections.** For each reviewer, restate every comment (verbatim or faithfully numbered), then respond.
3. **Point-by-point format** for each comment:
   - **Comment** (quoted/numbered)
   - **Response** (what you did and the theoretical/methodological reasoning)
   - **Location** (section/page/table where the change appears)
   - Quote new manuscript text where helpful.

## Responding to HRM's signature demands

- **"Deepen the theoretical mechanism / the contribution is incremental."** Revise the argument and the contribution sentences — name the mechanism, show what the field now learns. Adding citations is not a fix (see `hrm-theory-development`, `hrm-contribution-framing`).
- **"Common-method bias."** Provide designed or additional evidence (a lagged wave, a second source). If new data are impossible, give the strongest available statistical evidence (e.g., a marker-variable or unmeasured-latent-method-factor model) and frame residual risk as a boundary.
- **"HPWS adoption / the HR system is endogenous."** Add an identification strategy (panel FE, DiD, IV, or a natural experiment), report it, and explain why it resolves the concern (see `hrm-methods`, `hrm-data-analysis`).
- **"Justify the aggregation / construct validity."** Report r_wg, ICC(1)/ICC(2), the composition model, and a CFA establishing discriminant validity.
- **"What is the practice implication?"** This is HRM-specific: strengthen a **specific, conditional** practice payoff tied to your evidence — not a boilerplate "managers should attend to X" paragraph.
- **"Add a study."** A second study (often an experiment nailing the mechanism, or a replication) can be decisive in HRM's developmental culture; place heavy new material in an online supplement to respect length.

## Tone and tactics

- **Be respectful and substantive.** Reviewers are anonymous colleagues investing in your paper; thank them and engage seriously even when disagreeing.
- **Concede gracefully** where they are right; make the change.
- **Disagree with evidence, not assertion.** If you decline a request, give a theoretical or empirical reason and, where possible, an alternative analysis showing robustness.
- **Address every point.** Silent omissions read as evasion; one unanswered non-trivial point can sink a revision.
- **Surface conflicts to the editor.** When reviewers ask for opposite things, explain the trade-off and your chosen resolution for the editor to adjudicate.
- **Keep it self-contained.** A reviewer should not have to hunt the manuscript to see what changed; preserve anonymization in the resubmission.

## Checklist

- [ ] Manuscript actually revised before the letter was written
- [ ] Editor's priorities addressed first and explicitly in the opening letter
- [ ] Every reviewer comment restated and answered (none skipped)
- [ ] Each response names the location of the change and quotes new text where useful
- [ ] Theory/contribution, CMB, endogeneity, and aggregation demands met with real changes
- [ ] The **practice payoff** strengthened where reviewers questioned relevance
- [ ] Declined requests justified with evidence and, where possible, an alternative test
- [ ] Reviewer conflicts surfaced and resolved for the editor
- [ ] Resubmission still anonymized for double-blind review

## Anti-patterns

- Writing the response before making the changes
- Skipping or burying an inconvenient comment
- Answering "we added a citation" to a "deepen the theory" request
- Defensive or dismissive tone toward reviewers
- Declining a request with assertion ("we believe this is fine") and no evidence
- Fixing the rigor but ignoring a reviewer's doubt about the practice payoff
- Breaking anonymization in the revised manuscript

## Output format

```text
【Journal】Human Resource Management (Wiley "HRM")
【Skill】hrm-rebuttal
【Decision round】1st R&R / 2nd round / ...
【Editor priorities addressed】1... 2... 3...
【Per-reviewer coverage】R1: x/x, R2: x/x, R3: x/x — all answered? yes/no
【Major changes】theory: ... method/data (CMB/endogeneity/aggregation): ... new study: ...
【Practice payoff strengthened】...
【Declined requests + justification】...
【Reviewer conflicts resolved】...
【Anonymization preserved】yes/no
【Next step】resubmit via ScholarOne; on next decision → hrm-review-process
```
