---
name: jmr-rebuttal
description: Use when a Journal of Marketing Research (JMR) Revise-and-Resubmit arrives — planning the revision and drafting a point-by-point response that satisfies two independent reviewers and the Coeditor, addresses rigor-bar concerns (identification, exact statistics, replication) and substance-bar concerns (contribution), and uses the 'W'-prefixed Web Appendix to absorb new analyses without breaking the 50-page limit.
---

# R&R Revision & Response (jmr-rebuttal)

## When to trigger

- You received a JMR R&R and need to plan revisions and the response letter
- Reviewers and the Coeditor raise concerns spanning rigor and contribution
- New studies/analyses are needed but the print paper is near the 50-page limit
- You must reconcile conflicting reviewer requests

## Plan before you draft

1. **Triage every point** by which bar it targets — **rigor** (identification, manipulation, exact p-values/SEs/effect sizes, robustness, replication) or **substance** (contribution, framing, "what do we learn?"). JMR's dual standard means both must end up satisfied.
2. **Find the Coeditor's priorities.** The editor's letter signals which concerns are pivotal; weight your effort there. With **two independent reviewers**, expect some conflict — resolve it explicitly rather than splitting the difference silently.
3. **Decide where new material lives.** New robustness, additional studies, and estimation detail usually belong in the **'W'-prefixed Web Appendix** (excluded from the 50-page limit), with a short pointer in the print text — this lets you respond fully without blowing the page budget.

## Draft the point-by-point response

- Reproduce each comment verbatim, then respond directly beneath it.
- For each: state **what you changed**, **where** (section / page / "Table W3 in the Web Appendix"), and **why** it resolves the concern.
- For **rigor** points: run the requested test, report **exact p-values (three digits), standard errors, and effect sizes** in AMA number style, and add the supporting exhibit (main text or Web Appendix).
- For **substance** points: sharpen the contribution sentences (see `jmr-contribution-framing`); if a new study is needed to establish the mechanism or generalizability, run it and report it.
- Where you **disagree**, do so respectfully with evidence — JMR reviewers are domain experts; a reasoned, data-backed pushback is acceptable when the editor's framing allows.
- Reconcile **conflicting** reviewer requests openly: explain the trade-off and the choice, and let the editor adjudicate.

## Keep conformance intact

- Re-check the **50-page limit** after additions; move overflow to the Web Appendix.
- Keep the Web Appendix a **single PDF** with **'W'-prefixed** exhibits; update the **Data Availability Statement** and **AI disclosure** if methods changed.
- Maintain double-anonymization in the revised manuscript and response letter.

## Rigor/substance response ledger

Track each reviewer item in a ledger before writing the letter:

| Comment | Bar | Revision evidence | Location |
| --- | --- | --- | --- |
| Identification, mediation, robustness, exact stats, replication | Rigor | New estimate, diagnostic, p/SE/effect-size correction, or deposit update | Main text or Table W# |
| Contribution, theory, managerial relevance, scope | Substance | Revised contribution sentence, new boundary condition, clearer managerial implication | Introduction, discussion, or study rationale |
| Conflicting request | Editor arbitration | Chosen path and why it preserves rigor/substance | Cover note plus response entry |

The ledger should reveal whether the revision is balanced. A response that fixes all rigor points but leaves the "what do we learn?" objection untouched is still at risk; a response that improves framing but leaves exact-statistics or replication gaps is also not ready.

## Anti-patterns

- A response letter written before the manuscript is actually revised.
- Cosmetic replies ("we have addressed this") with no concrete change or location.
- Letting new analyses push the print paper over 50 pages instead of using the Web Appendix.
- Capitulating to a reviewer in a way that breaks identification or over-claims.
- Reporting added results with thresholds/asterisks instead of exact statistics.
- Treating rigor and substance as separate reviewer silos instead of satisfying both in the revised claim.

## Output format

```text
[Target] JMR
[Decision round] R&R #
[Per-comment plan] bar (rigor/substance) → change → location (main / Table Wx)
[Response ledger] all comments mapped to rigor/substance evidence
[Conflicts] reviewer A vs B → resolution + editor adjudication
[New material] Web Appendix additions; 50-page check
[Conformance] DAS / AI disclosure / anonymization updated
[Next step] resubmit → jmr-review-process
```

## Resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md)
- [`../../resources/external_tools.md`](../../resources/external_tools.md)
