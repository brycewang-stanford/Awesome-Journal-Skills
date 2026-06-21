---
name: aejpol-rebuttal
description: Use when an AEJ: Economic Policy decision letter (R&R or reject-and-resubmit) has arrived and a response-letter strategy and revision plan are needed. Structures the response to referees and editor with policy-relevance front and center; it does not run new estimation or redesign identification from scratch.
---

# Rebuttal & Response Letter (aejpol-rebuttal)

## When to trigger

- An AEJ: Policy R&R or major-revision letter arrived and you must plan the response
- Referee reports conflict and you need an editor-anchored prioritization
- You need to convert reports into a revision plan plus a point-by-point letter
- A resubmission needs a cover note showing how every comment was addressed

## How to run an AEJ: Policy revision

The editor's letter is the contract — **prioritize what the editor emphasizes**, then address every referee point. At AEJ: Policy the recurring high-stakes asks are about (a) the **credibility of the causal claim**, (b) the **welfare / policy reading**, and (c) **robustness and reproducibility**. Treat the response as a chance to make the policy contribution *more* prominent, not just to patch holes.

### Structure of the response
1. **Editor-first summary.** Open the letter with a short paragraph naming the 2–3 changes that address the editor's main concerns, and how the paper is now a stronger *policy* contribution.
2. **Point-by-point, per referee.** Quote each comment; respond with what you changed, where (section/table/figure), and the result. Concede where the referee is right; defend with evidence where they are not — politely and with a specific exhibit.
3. **A "what's new" map.** A table mapping each major comment to the revision so the editor can verify coverage at a glance.

### AEJ: Policy-specific response moves
- **"Not a policy paper" / "so what":** strengthen the policy question in the abstract/intro and add or sharpen the welfare/cost-benefit reading (`aejpol-theory-model`); do not just add caveats.
- **Identification doubts:** add the heterogeneity-robust estimator, the honest-DID bound, or the density/first-stage diagnostic into the **main text** and reference it in the letter.
- **Welfare hand-waving:** derive the sufficient statistic / MVPF explicitly and propagate uncertainty.
- **Reproducibility flagged:** confirm the AEA-compliant package and restricted-data path are ready (`aejpol-replication-package`).
- **Conflicting referees:** state the conflict, follow the editor's steer, and where you cannot satisfy both, explain the trade-off transparently.

### Tone and discipline
Respectful, specific, evidence-led. Every "we agree" is followed by a concrete change; every "we respectfully disagree" is followed by an exhibit or a citation. Keep claims calibrated — over-defending invites a second round.

## Checklist

- [ ] Editor's main concerns identified and addressed first in the letter
- [ ] Every referee comment answered point-by-point with section/exhibit references
- [ ] Concessions made where warranted; pushback backed by specific evidence
- [ ] Identification / robustness additions placed in the main text, not buried
- [ ] Welfare/policy reading strengthened, not just caveated
- [ ] Reproducibility package and restricted-data path confirmed ready
- [ ] A comment→revision map included; revised manuscript carries the front matter (single-blind)

## Anti-patterns

- Answering the easy referee points and dodging the editor's central concern
- Defending a contested identification choice with rhetoric instead of a new diagnostic
- Adding caveats to dodge a "no policy point" critique instead of strengthening the welfare reading
- Burying the new robustness result in an appendix and hoping the referee notices
- A combative tone that turns a revisable R&R into a rejection
- Treating the response letter as adversarial rather than a good-faith revision record

## Per-comment response template

For each referee point, write three short moves so the editor can verify coverage quickly:
1. **Restate** the comment in one neutral sentence (quote the key phrase).
2. **Act** — "We agree and have [change], now in [Section/Table/Figure]," or "We respectfully disagree; [exhibit/citation] shows [evidence]."
3. **Point** — name the exact location in the revised manuscript where the change lives.

Keep the agree:disagree ratio honest — concede the genuine points fully and reserve disagreement for
places where you have a concrete exhibit. A letter that disagrees with everything reads as defensive and
invites a second round.

## Worked vignette (illustrative)

An R&R on a transfer-program paper: the editor stresses "the welfare interpretation is not convincing"; Referee 1 doubts parallel trends; Referee 2 wants external validity. Plan: (1) letter opens with the new MVPF derivation answering the editor; (2) R1 → add honest-DID bounds and flat leads to Section 4, cite in the letter; (3) R2 → add heterogeneity by state characteristics and a scope paragraph. A comment→revision table closes the letter. The contribution reads as a sharper policy answer than the original.

## Output format

```
【Editor's main concern】+ the 2–3 changes that address it (letter opener)
【Per-referee responses】[comment → change → location → result]
【Concede vs. defend】list, each with its evidence
【Welfare/policy strengthening】what was added (not just caveated)
【Reproducibility】package + restricted-data path confirmed? [Y/N]
【Comment→revision map】attached? [Y/N]
【Next step】resubmit via AEA system
```
