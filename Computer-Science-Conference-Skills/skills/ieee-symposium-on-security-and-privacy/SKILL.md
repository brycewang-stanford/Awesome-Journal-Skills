---
name: ieee-symposium-on-security-and-privacy
description: Use when targeting IEEE Symposium on Security and Privacy (IEEE S&P) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for security flagship.
---

# IEEE Symposium on Security and Privacy (IEEE S&P)

## Conference positioning

IEEE Symposium on Security and Privacy (IEEE S&P) is a top computer-science conference venue for computer security, privacy, cryptography applications, systems security, attacks, defenses, and measurement. It rewards a security paper with strong threat model, ethical handling, and convincing exploit/defense evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names IEEE S&P / IEEE Symposium on Security and Privacy as the target venue.
- A manuscript in computer security needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: computer security, privacy, cryptography applications, systems security, attacks, defenses, and measurement.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to IEEE S&P's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Read reviewers as adversarial-method reviewers. Threat model, ethics, disclosure, adaptive attacks, and reproducible evidence are central.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: computer security, privacy, cryptography applications, systems security, attacks, defenses, and measurement.
- Distinctive fingerprint for reviewer calibration: security, privacy, cryptography, applications, attacks, defenses, measurement, venue-specific, contribution, flagship, ieee-security.
- Official anchor domain: www.ieee-security.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to IEEE S&P when the work has security/privacy depth, rigorous threat modeling, and a
  contribution that fits the long-running S&P research community.
- Do not choose S&P by prestige alone. Compare CCS for broad ACM security, USENIX Security for
  systems/security artifacts, NDSS for networked security, PETS for privacy-first work.

## What distinguishes this venue from its closest siblings

- **What IEEE S&P (Oakland) is.** The **IEEE** Symposium on **Security and Privacy** — one of the security "big four".
- **vs CCS.** CCS (ACM) is the other top general-security flagship; with **USENIX Security** and **NDSS** they are the big four — differentiate by cycle and community.
- **Routing.** Crypto-theory → CRYPTO/EUROCRYPT; applied/regional → ESORICS/ACSAC; privacy-specific → PETS.

## IEEE S&P-specific routing detail

- Prefer IEEE S&P when the paper's security/privacy claim is rigorous enough for the Oakland community, with careful threat modeling, ethics, and deep technical or empirical evidence.
- Compare CCS for ACM general security, USENIX Security for systems/security artifacts, NDSS for networked security, and PETS when privacy is the primary research community.
- S&P evidence should avoid prestige-only framing and show why the attack, defense, measurement, or privacy result advances the long-running security/privacy conversation.

## Method & evidence bar

- Define the threat model, attacker capabilities, disclosure posture, and ethics review before presenting results.
- Use realistic targets, baselines, and measurement methodology; avoid sensational claims unsupported by evidence.
- For defenses, evaluate adaptive attacks and deployment costs; for attacks, document responsible handling.
- For IEEE S&P, the evidence must support the venue-specific signature: a security paper with strong threat model, ethical handling, and convincing exploit/defense evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Make the security claim precise: vulnerability class, adversary model, defense guarantee, or measurement finding.
- Explain impact without overstating exploitability beyond the tested conditions.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.ieee-security.org/TC/SP-Index.html
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current security-conference CFP, ethics/disclosure policy, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at IEEE S&P, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle security flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Vague threat model or unhandled ethical risk.
- Defense evaluated only against weak or non-adaptive attacks.
- Measurement paper with biased sampling and no validation.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving IEEE S&P reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses IEEE S&P's bar, compare against `usenix-security-symposium` / `acm-conference-on-computer-and-communications-security` / `network-and-distributed-system-security-symposium` / `privacy-enhancing-technologies-symposium`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE Symposium on Security and Privacy (IEEE S&P)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
