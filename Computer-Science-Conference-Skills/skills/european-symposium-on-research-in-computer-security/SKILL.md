---
name: european-symposium-on-research-in-computer-security
description: Use when targeting European Symposium on Research in Computer Security (ESORICS) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for security.
---

# European Symposium on Research in Computer Security (ESORICS)

## Conference positioning

European Symposium on Research in Computer Security (ESORICS) is a top computer-science conference venue for European computer security research across privacy, systems, cryptography, and applications. It rewards a security paper suited to a broad European security audience. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ESORICS / European Symposium on Research in Computer Security as the target venue.
- A manuscript in European computer security research across privacy needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: European computer security research across privacy, systems, cryptography, and applications.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ESORICS's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ESORICS as a security venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: European computer security research across privacy, systems, cryptography, and applications.
- Distinctive fingerprint for reviewer calibration: european, security, across, privacy, cryptography, applications, venue-specific, contribution, esorics.
- Official anchor domain: esorics.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in security and
  the author can say why ESORICS reviewers are the primary audience, not merely a convenient
  deadline.
- Closest roster neighbors to compare before final routing: `privacy-enhancing-technologies-
  symposium` (PETS), `annual-computer-security-applications-conference` (ACSAC), `acm-asia-
  conference-on-computer-and-communications-security` (ASIACCS), `iacr-conference-on-
  cryptographic-hardware-and-embedded-systems` (CHES). Break ties by contribution type,
  evidence shape, reviewer community, and the current official CFP from esorics.org.

## What distinguishes this venue from its closest siblings

- **What ESORICS is.** The flagship **European** computer-security research symposium (Springer **LNCS** proceedings), broad security scope.
- **vs PETS.** PETS is **privacy-specific** (publishes in PoPETs); route privacy-enhancing-technology work there and general security here.
- **vs ACSAC.** ACSAC is **applied** security; reserve ESORICS for research contributions, and remember the big-four flagships are IEEE S&P, USENIX Security, ACM CCS, NDSS.

## ESORICS-specific routing detail

- Prefer ESORICS when the paper fits the European computer-security research community: systems security, privacy, applied crypto, formal security, or network security with full research evidence.
- Route operational security practice to ACSAC, privacy-first protocol or measurement work to PETS, and finance/cryptocurrency security to FC when those communities are the natural audience.
- ESORICS evidence should present a rigorous threat model, security argument, empirical validation, and related-work positioning against European and flagship security venues.

## Method & evidence bar

- Define the threat model, attacker capabilities, disclosure posture, and ethics review before presenting results.
- Use realistic targets, baselines, and measurement methodology; avoid sensational claims unsupported by evidence.
- For defenses, evaluate adaptive attacks and deployment costs; for attacks, document responsible handling.
- For ESORICS, the evidence must support the venue-specific signature: a security paper suited to a broad European security audience.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Make the security claim precise: vulnerability class, adversary model, defense guarantee, or measurement finding.
- Explain impact without overstating exploitability beyond the tested conditions.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://esorics.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current security-conference CFP, ethics/disclosure policy, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ESORICS, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle security papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Vague threat model or unhandled ethical risk.
- Defense evaluated only against weak or non-adaptive attacks.
- Measurement paper with biased sampling and no validation.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ESORICS reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ESORICS's bar, compare against `ieee-symposium-on-security-and-privacy` / `usenix-security-symposium` / `acm-conference-on-computer-and-communications-security` / `network-and-distributed-system-security-symposium`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] European Symposium on Research in Computer Security (ESORICS)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
