---
name: annual-computer-security-applications-conference
description: Use when targeting Annual Computer Security Applications Conference (ACSAC) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for applied security.
---

# Annual Computer Security Applications Conference (ACSAC)

## Conference positioning

Annual Computer Security Applications Conference (ACSAC) is a top computer-science conference venue for applied computer security, assurance, usable security, systems, and operational defenses. It rewards an applied-security paper with deployable lessons and careful risk framing. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ACSAC / Annual Computer Security Applications Conference as the target venue.
- A manuscript in applied computer security needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: applied computer security, assurance, usable security, systems, and operational defenses.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ACSAC's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ACSAC as a applied security venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: applied computer security, assurance, usable security, systems, and operational defenses.
- Distinctive fingerprint for reviewer calibration: applied, security, assurance, usable, operational, defenses, venue-specific, contribution, acsac.
- Official anchor domain: www.acsac.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in applied
  security and the author can say why ACSAC reviewers are the primary audience, not merely a
  convenient deadline.
- Closest roster neighbors to compare before final routing: `network-and-distributed-system-
  security-symposium` (NDSS), `privacy-enhancing-technologies-symposium` (PETS), `european-
  symposium-on-research-in-computer-security` (ESORICS), `acm-asia-conference-on-computer-and-
  communications-security` (ASIACCS). Break ties by contribution type, evidence shape,
  reviewer community, and the current official CFP from www.acsac.org.

## What distinguishes this venue from its closest siblings

- **What ACSAC is.** The **Annual Computer Security Applications Conference** (ACSA) — **applied** and deployment-oriented security research.
- **vs ESORICS.** ESORICS is the broad European research symposium (Springer LNCS); route applied/operational work here.
- **vs PETS.** PETS is privacy-specific; ACSAC spans applied security broadly, below the IEEE S&P / USENIX Security / CCS / NDSS flagships.

## ACSAC-specific routing detail

- Prefer ACSAC when the security contribution is applied, operational, or deployment-facing: enterprise defenses, usable security in practice, applied measurement, or security engineering lessons.
- Route European research-community general security work to ESORICS, privacy-first work to PETS, finance/cryptocurrency work to FC, and broad flagship submissions to CCS/S&P/USENIX/NDSS.
- ACSAC evidence should include operational assumptions, deployment constraints, realistic adversaries, usability or administrative context, and lessons that transfer to security practice.

## Method & evidence bar

- Define the threat model, attacker capabilities, disclosure posture, and ethics review before presenting results.
- Use realistic targets, baselines, and measurement methodology; avoid sensational claims unsupported by evidence.
- For defenses, evaluate adaptive attacks and deployment costs; for attacks, document responsible handling.
- For ACSAC, the evidence must support the venue-specific signature: an applied-security paper with deployable lessons and careful risk framing.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Make the security claim precise: vulnerability class, adversary model, defense guarantee, or measurement finding.
- Explain impact without overstating exploitability beyond the tested conditions.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.acsac.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current security-conference CFP, ethics/disclosure policy, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ACSAC, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle applied security papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Vague threat model or unhandled ethical risk.
- Defense evaluated only against weak or non-adaptive attacks.
- Measurement paper with biased sampling and no validation.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ACSAC reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ACSAC's bar, compare against `ieee-symposium-on-security-and-privacy` / `usenix-security-symposium` / `acm-conference-on-computer-and-communications-security` / `network-and-distributed-system-security-symposium`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Annual Computer Security Applications Conference (ACSAC)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
