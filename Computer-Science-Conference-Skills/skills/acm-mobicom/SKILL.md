---
name: acm-mobicom
description: Use when targeting ACM MobiCom (MobiCom) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for mobile networking.
---

# ACM MobiCom (MobiCom)

## Conference positioning

ACM MobiCom (MobiCom) is a top computer-science conference venue for mobile computing, wireless networks, edge systems, sensing, and mobile AI infrastructure. It rewards a mobile systems paper with real wireless/mobile constraints and convincing deployment evidence. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names MobiCom / ACM MobiCom as the target venue.
- A manuscript in mobile computing needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: mobile computing, wireless networks, edge systems, sensing, and mobile AI infrastructure.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to MobiCom's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat MobiCom as the mobile networking flagship: radio behavior, wireless protocols, mobility, edge connectivity, spectrum, measurement, and network performance are central. The paper should not read like a general mobile-app or sensing systems paper.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: mobile computing, wireless networks, edge systems, sensing, and mobile AI infrastructure.
- Distinctive fingerprint for reviewer calibration: mobile, computing, wireless, networks, edge, sensing, infrastructure, venue-specific, contribution, networking, sigmobile.
- Official anchor domain: www.sigmobile.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Route to MobiCom when the contribution is mobile networking, wireless systems, protocols,
  measurement, or networked mobile infrastructure.
- Compare MobiSys for mobile systems and sensing, SIGCOMM/NSDI for broader networking/systems,
  and WiSec when security/privacy is central.

## What distinguishes this venue from its closest siblings

- **What MobiCom is.** The **ACM SIGMOBILE** flagship for **mobile computing and wireless networking** — the protocol/wireless/networking side of mobile.
- **vs MobiSys.** MobiSys (also ACM SIGMOBILE) is the **mobile systems and services** venue; route systems/platform work there and wireless/networking work here.
- **Routing.** Lower-layer wireless and networking contributions fit MobiCom; end-to-end mobile systems fit MobiSys.

## MobiCom-specific routing detail

- Prefer MobiCom when the core novelty is a mobile or wireless networking mechanism: radio behavior, spectrum use, protocol design, edge connectivity, measurement at mobility scale, or network performance under realistic channel and deployment constraints.
- Use MobiSys when the research claim is an end-to-end mobile/embedded platform, sensing pipeline, wearable system, or mobile service whose artifact behavior matters more than the wireless/networking mechanism.
- Compare with SIGCOMM/NSDI for broader networked-systems claims, WiSec for security/privacy, SenSys/UbiComp for sensing and ubiquitous computing, and MobiSys for device/platform/system integration.

## Method & evidence bar

- Build the artifact or prototype far enough that the core design can be measured under realistic workloads.
- Use appropriate baselines, sensitivity analyses, and workload characterization; systems reviewers look for hidden bottlenecks.
- Separate engineering effort from research contribution: name the abstraction, mechanism, or tradeoff.
- For MobiCom, the evidence must support the venue-specific signature: a mobile systems paper with real wireless/mobile constraints and convincing deployment evidence.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Start from a systems pain point and show why existing abstractions fail.
- Use evaluation sections that answer research questions, not a tour of every benchmark run.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.sigmobile.org/mobicom/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current USENIX/ACM/IEEE author kit, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at MobiCom, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle mobile networking papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Toy implementation or microbenchmark-only evidence for a systems claim.
- No comparison to mature systems or no explanation of deployment constraints.
- Performance gains with unclear workload representativeness.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving MobiCom reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses MobiCom's bar, compare against `acm-symposium-on-operating-systems-principles` / `usenix-symposium-on-operating-systems-design-and-implementation` / `usenix-symposium-on-networked-systems-design-and-implementation` / `acm-sigcomm`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] ACM MobiCom (MobiCom)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
