---
name: ccs-writing-style
description: Use when revising an ACM CCS paper for a precise threat model, calibrated attack/defense claims, 12-page ACM sigconf compression, double-blind wording, adaptive-evaluation honesty, and the security house style that survives an adversarial SIGSAC program committee.
---

# CCS Writing Style

Use this when revising the main paper. CCS papers must state who the attacker is, what the
contribution defends or breaks, and enough measured evidence that an adversarial reviewer
cannot poke the central claim.

## Revision rules

- Put the security contribution on the first page: the problem, the attacker, the gap in
  existing defenses or attacks, the mechanism, and the evidence that it works.
- Make the threat model explicit and early. State attacker capabilities, knowledge, position,
  and goal before results; CCS reviewers reject on hidden or shifting adversary assumptions.
- Pair every claim with proof, measurement, exploit demonstration, or a cost number. A
  security claim without a bound on the adversary or a measured cost reads as marketing.
- Use the 12-page body for the core argument; move protocol transcripts, extra measurements,
  and formal proofs to appendices without making the body unintelligible.
- Do not overstate exploitability beyond the conditions tested; scope every "practical" claim
  to the environment, versions, and configuration measured.
- Keep double-blind wording in self-citations, tool names, acknowledgements, and artifact
  descriptions.

## Threat-model discipline

- Give the adversary a named model with capabilities enumerated once and referenced by name;
  CCS readers audit whether every attack step stays inside those capabilities.
- Separate what the attacker knows from what it can do from where it sits in the system; a
  conflated model is the most common source of "the attack assumes too much" reviews.
- State the security goal as a property (confidentiality, integrity, availability,
  unlinkability) and say what "broken" means quantitatively.
- When a defense is evaluated, name the adaptive attacker it was tested against; a defense
  measured only against the attack it was designed to stop is a standing CCS complaint.
- Label conjecture, heuristic argument, and proved result distinctly; mixing them near a
  security claim is a credibility leak at this venue.

## Sentence-level rewrites

| Draft pattern | CCS-safe rewrite |
|---|---|
| "Our attack is highly effective..." | "recovers the key in N queries against library X vY on platform Z" |
| "Under realistic assumptions..." | "Under threat model T (network MITM, no host access)..." |
| "Our defense is secure..." | "resists the adaptive attacker of Section 5 at C% overhead" |
| "We significantly reduce risk..." | Claim scoped to the deployment and versions measured |

## Vignette: compressing into twelve two-column pages

A draft with a full protocol description, four attack variants, a formal proof, and six
measurement figures: keep the threat model, the strongest attack variant end to end, one
proof sketch, and the two decision-critical figures (leakage rate and defense overhead);
push the other variants, the full proof, and raw measurement tables to appendices with
forward references. The test of a good cut: a reviewer should be able to judge novelty and
soundness of the attack without opening the appendix.

## Output format

```text
[Writing diagnosis] clear / under-specified threat model / overclaimed / overloaded
[First-page fix] <new framing>
[Claim discipline] <claim -> proof/measurement/exploit/cost>
[Compression cuts] <move/delete/merge>
[Anonymity edits] <phrases to rewrite>
```
