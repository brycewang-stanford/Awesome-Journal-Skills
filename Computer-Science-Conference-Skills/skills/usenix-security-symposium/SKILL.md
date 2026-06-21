---
name: usenix-security-symposium
description: Use when targeting USENIX Security Symposium (USENIX Security) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for security flagship.
---

# USENIX Security Symposium (USENIX Security)

## Conference positioning

USENIX Security Symposium (USENIX Security) is a top computer-science conference venue for systems security, network security, privacy, usable security, software security, and measurement. It rewards a security paper with rigorous artifact, measurement, or vulnerability analysis and responsible disclosure. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names USENIX Security / USENIX Security Symposium as the target venue.
- A manuscript in systems security needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: systems security, network security, privacy, usable security, software security, and measurement.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to USENIX Security's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as adversarial-method reviewers. Threat model, ethics, disclosure, adaptive attacks, and reproducible evidence are central.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: systems security, network security, privacy, usable security, software security, and measurement.
- Distinctive fingerprint for reviewer calibration: security, network, privacy, usable, software, measurement, venue-specific, contribution, flagship, usenix.
- Official anchor domain: www.usenix.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in security
  flagship and the author can say why USENIX Security reviewers are the primary audience, not
  merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `ieee-symposium-on-security-and-
  privacy` (IEEE S&P), `acm-conference-on-computer-and-communications-security` (CCS),
  `network-and-distributed-system-security-symposium` (NDSS). Break ties by contribution type,
  evidence shape, reviewer community, and the current official CFP from www.usenix.org.

## USENIX Security-specific routing detail

- Prefer USENIX Security when the claim is a systems-security, vulnerability-analysis, usable-security, privacy, measurement, or artifact-heavy contribution whose evidence can be audited and reused by other security researchers.
- Use NDSS as the closest contrast: NDSS is often the cleaner venue for network/protocol-centered security stories, while USENIX Security is especially strong when the artifact, empirical measurement, exploit/defense analysis, or software-security engineering is the main contribution.
- Route to IEEE S&P or CCS when the paper needs a broader security-theory or policy/security-systems framing, PETS when privacy is the dominant contribution, and SOUPS when the human-subject/usable-security component is the paper's center.

## Method & evidence bar

- Define the threat model, attacker capabilities, disclosure posture, and ethics review before presenting results.
- Use realistic targets, baselines, and measurement methodology; avoid sensational claims unsupported by evidence.
- For defenses, evaluate adaptive attacks and deployment costs; for attacks, document responsible handling.
- For USENIX Security, the evidence must support the venue-specific signature: a security paper with rigorous artifact, measurement, or vulnerability analysis and responsible disclosure.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Make the security claim precise: vulnerability class, adversary model, defense guarantee, or measurement finding.
- Explain impact without overstating exploitability beyond the tested conditions.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.usenix.org/conferences/byname/108
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current security-conference CFP, ethics/disclosure policy, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at USENIX Security, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle security flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Vague threat model or unhandled ethical risk.
- Defense evaluated only against weak or non-adaptive attacks.
- Measurement paper with biased sampling and no validation.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving USENIX Security reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses USENIX Security's bar, compare against `ieee-symposium-on-security-and-privacy` / `acm-conference-on-computer-and-communications-security` / `network-and-distributed-system-security-symposium` / `privacy-enhancing-technologies-symposium`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] USENIX Security Symposium (USENIX Security)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
