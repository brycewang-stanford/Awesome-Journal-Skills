---
name: acm-conference-on-designing-interactive-systems
description: Use when targeting ACM Conference on Designing Interactive Systems (DIS) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for interaction design.
---

# ACM Conference on Designing Interactive Systems (DIS)

## Conference positioning

ACM Conference on Designing Interactive Systems (DIS) is a top computer-science conference venue for interaction design, design methods, critical computing, prototyping, and human-centered systems. It rewards a design research paper with a strong artifact, method, or theory contribution. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names DIS / ACM Conference on Designing Interactive Systems as the target venue.
- A manuscript in interaction design needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: interaction design, design methods, critical computing, prototyping, and human-centered systems.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to DIS's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat DIS as a interaction design venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: interaction design, design methods, critical computing, prototyping, and human-centered systems.
- Distinctive fingerprint for reviewer calibration: interaction, design, methods, critical, computing, prototyping, human-centered, venue-specific, contribution.
- Official anchor domain: dis.acm.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in interaction
  design and the author can say why DIS reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `acm-ieee-joint-conference-on-
  digital-libraries` (JCDL), `conference-and-labs-of-the-evaluation-forum` (CLEF), `acm-
  interactive-surfaces-and-spaces` (ISS), `international-symposium-on-research-in-attacks-
  intrusions-and-defenses` (RAID). Break ties by contribution type, evidence shape, reviewer
  community, and the current official CFP from dis.acm.org.

## DIS-specific routing detail

- Prefer DIS when the contribution is design knowledge: an artifact, design method, critical/reflective inquiry, participatory process, speculative system, or prototype that teaches the field how to design interactive systems differently.
- Use CHI when the broad HCI contribution is primarily empirical, behavioral, accessibility, social-computing, or human-centered systems evidence; DIS should not be a fallback for underpowered CHI studies.
- Compare with TEI/ISS for tangible and surface interaction, CSCW for collaborative practice, CHI for general HCI breadth, and design/HCI journals when the argument needs richer reflective or longitudinal presentation.

## Method & evidence bar

- Match the contribution type to the evidence: controlled study, field deployment, design inquiry, technical system, dataset, or theory.
- Report participants, recruitment, analysis method, consent/ethics, and limitations with enough detail for HCI review.
- For AI-infused interfaces, evaluate both model behavior and user experience; either alone is usually insufficient.
- For DIS, the evidence must support the venue-specific signature: a design research paper with a strong artifact, method, or theory contribution.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Explain who benefits, what interaction changes, and what design knowledge the paper contributes.
- Avoid treating users as a decoration for a technical system; the human evidence has to shape the claim.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://dis.acm.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current ACM PCS/Precision Conference author guide and contribution-type policy.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at DIS, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle interaction design papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Underpowered or poorly matched user study for an ambitious design claim.
- Novel interface demo without contribution to interaction knowledge.
- Ethics, accessibility, or community context handled superficially.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving DIS reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses DIS's bar, compare against `acm-chi-conference-on-human-factors-in-computing-systems` / `acm-symposium-on-user-interface-software-and-technology` / `acm-conference-on-computer-supported-cooperative-work-and-social-computing` / `acm-conference-on-intelligent-user-interfaces`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM Conference on Designing Interactive Systems (DIS)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
