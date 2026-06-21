---
name: acm-chi-conference-on-human-factors-in-computing-systems
description: Use when targeting ACM CHI Conference on Human Factors in Computing Systems (CHI) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for HCI flagship.
---

# ACM CHI Conference on Human Factors in Computing Systems (CHI)

## Conference positioning

ACM CHI Conference on Human Factors in Computing Systems (CHI) is a top computer-science conference venue for human-computer interaction, user experience, social computing, accessibility, design, and interactive systems. It rewards an HCI paper with a clear contribution type, rigorous study design, and relevance to human-centered computing. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names CHI / ACM CHI Conference on Human Factors in Computing Systems as the target venue.
- A manuscript in human-computer interaction needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: human-computer interaction, user experience, social computing, accessibility, design, and interactive systems.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to CHI's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as human-centered computing researchers. Contribution type, study design, participant context, ethics, and design implication must line up.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: human-computer interaction, user experience, social computing, accessibility, design, and interactive systems.
- Distinctive fingerprint for reviewer calibration: human-computer, interaction, user, experience, social, computing, accessibility, design, interactive, venue-specific, contribution, flagship, chi2026.
- Official anchor domain: chi2026.acm.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in HCI flagship
  and the author can say why CHI reviewers are the primary audience, not merely a convenient
  deadline.
- Closest roster neighbors to compare before final routing: `acm-conference-on-computer-
  supported-cooperative-work-and-social-computing` (CSCW), `acm-conference-on-intelligent-
  user-interfaces` (IUI). Break ties by contribution type, evidence shape, reviewer community,
  and the current official CFP from chi2026.acm.org.

## CHI-specific routing detail

- Prefer CHI when the paper makes a broad human-centered computing contribution: user behavior, interaction technique, accessibility, social computing, design implication, empirical study, or system impact with strong human evidence.
- Use DIS when the design artifact, design method, critical design inquiry, or making/prototyping contribution is the center of the paper; CHI reviewers still expect the human-centered claim to generalize beyond the artifact.
- Compare with CSCW for collaborative/social systems, UIST for interaction-technique engineering, IUI for intelligent interface behavior, and specialized accessibility/health/education venues when the domain community is the primary audience.

## Method & evidence bar

- Match the contribution type to the evidence: controlled study, field deployment, design inquiry, technical system, dataset, or theory.
- Report participants, recruitment, analysis method, consent/ethics, and limitations with enough detail for HCI review.
- For AI-infused interfaces, evaluate both model behavior and user experience; either alone is usually insufficient.
- For CHI, the evidence must support the venue-specific signature: an HCI paper with a clear contribution type, rigorous study design, and relevance to human-centered computing.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Explain who benefits, what interaction changes, and what design knowledge the paper contributes.
- Avoid treating users as a decoration for a technical system; the human evidence has to shape the claim.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://chi2026.acm.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current ACM PCS/Precision Conference author guide and contribution-type policy.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at CHI, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle HCI flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Underpowered or poorly matched user study for an ambitious design claim.
- Novel interface demo without contribution to interaction knowledge.
- Ethics, accessibility, or community context handled superficially.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving CHI reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses CHI's bar, compare against `acm-symposium-on-user-interface-software-and-technology` / `acm-conference-on-computer-supported-cooperative-work-and-social-computing` / `acm-conference-on-intelligent-user-interfaces` / `ieee-visualization-conference`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM CHI Conference on Human Factors in Computing Systems (CHI)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
