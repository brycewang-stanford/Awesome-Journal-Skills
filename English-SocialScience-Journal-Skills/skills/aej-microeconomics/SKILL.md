---
name: aej-microeconomics
description: Use when targeting American Economic Journal: Microeconomics or deciding whether a microeconomic theory manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# American Economic Journal: Microeconomics (aej-microeconomics)

## Journal positioning

AEJ: Microeconomics is the American Economic Association's field home for microeconomic theory one tier below AER's general-interest bar. It publishes micro theory, game theory, mechanism and market design, and theoretical IO — theoretical contributions with general results, established formally. The contribution can be field-specific rather than discipline-wide, but the theory must be correct, general, and economically interesting; this is the home for serious theory that is excellent but narrower than a top-5 or Econometrica swing.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the AEA site and the editorial-manager submission system.

## When to trigger

- The author names AEJ: Micro as the target, or is stepping down from a top-5 / Econometrica theory submission.
- A paper offers a micro-theory, game-theory, mechanism-design, or theoretical-IO contribution with general results.
- A strong theory paper is excellent but narrower than AER's general-interest bar and needs the right theory home.
- The author needs AEJ: Micro's desk-reject risks and a credible top-5 / theory-field alternative list.

## Scope & topic fit

- Microeconomic theory: decision theory, contract theory, information economics, and applied micro theory with general models.
- Game theory: equilibrium analysis, dynamic and repeated games, learning, and bargaining.
- Mechanism and market design: auctions, matching, allocation, and incentive design with characterization results.
- Theoretical industrial organization: oligopoly, pricing, platforms, and strategic firm behavior modeled formally.

## Method & evidence bar

- The formal bar is the filter: results must be correct, general, and proved — not a worked example or a narrow special case dressed as a theorem.
- Assumptions must be stated precisely and economically motivated; the model should illuminate a general economic force, not just generate one comparative static.
- Characterizations, existence/uniqueness, and welfare or comparative-statics results should generalize and be economically interpretable.
- Any computational or numerical illustration supports the theory; data are not required, but if present they must be handled to AEA availability and verification standards.

## Structure & house style

- The introduction states the economic question, the model, the main theoretical result, and why it matters and is general, before the formal development.
- State definitions, assumptions, and propositions/theorems cleanly in the main text; move long proofs and extensions to an appendix or online supplement.
- AEJ uses an unstructured abstract and JEL codes; notation must be consistent and economical.
- Where examples or figures are used, they should make the mechanism intuitive; the central result should be legible as a proposition.

## Official-submission checklist

- Search the live site for "AEJ: Microeconomics submission guidelines" and (for any data/computation) the AEA "Data and Code Availability Policy," and follow the current versions.
- Re-check the submission fee, LaTeX/formatting, abstract/JEL, anonymization, and proof-appendix conventions on the editorial-manager system.
- Re-check the current supplementary-material policy and, if the paper uses data or simulations, the code/replication deposit and verification workflow.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the general theoretical result and the economic force it captures.
- [ ] The contribution is stated as a general, proved result, not as an example or special case.
- [ ] The introduction positions the paper against the recent theory frontier it advances.
- [ ] All proofs are complete and correct; assumptions are minimal and economically motivated; results generalize.
- [ ] Proofs, extensions, and any code/simulation material match the current official guide.

## Common desk-reject triggers

- A "theorem" that is a narrow special case, a worked example, or a restatement of known results.
- An interesting model with incomplete, incorrect, or hand-waved proofs.
- A result with no general economic insight — one comparative static with no broader force.
- A paper better suited to an empirical or general-interest venue but framed as pure theory.

## Re-routing decision

- Top-tier general theory or a new fundamental result → `econometrica` (theorem with full proofs) or `journal-of-economic-theory`.
- Game theory specifically → `games-and-economic-behavior`; frontier theory with strong novelty → `review-of-economic-studies`.
- General-interest theory of broad importance → `american-economic-review`, `journal-of-political-economy`, or `quarterly-journal-of-economics`.
- Theory disciplined by data / structural → `aej-macroeconomics` (macro) or `aej-applied-economics` (applied empirics).

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] American Economic Journal: Microeconomics
[Topic tags] <2–3 closest topics>
[Method/evidence] <do the theory results clear the generality + rigor bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / fee / LaTeX / proof appendix / supplementary material>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
