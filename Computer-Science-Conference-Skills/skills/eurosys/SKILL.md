---
name: eurosys
description: Use when targeting EuroSys (EuroSys) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for systems.
---

# EuroSys (EuroSys)

## Conference positioning

EuroSys (EuroSys) is a top computer-science conference venue for European systems research across OS, distributed systems, storage, cloud, and systems security. It rewards a systems paper with implementation depth and systems-community relevance. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names EuroSys / EuroSys as the target venue.
- A manuscript in European systems research across OS needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: European systems research across OS, distributed systems, storage, cloud, and systems security.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to EuroSys's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat EuroSys as European systems research: operating systems, distributed systems, storage, cloud, and systems security should be shown through built artifacts and workloads. Do not write it as a pure networking or architecture paper.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: European systems research across OS, distributed systems, storage, cloud, and systems security.
- Distinctive fingerprint for reviewer calibration: european, across, distributed, storage, cloud, security, venue-specific, contribution, eurosys.
- Official anchor domain: 2026.eurosys.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in systems and
  the author can say why EuroSys reviewers are the primary audience, not merely a convenient
  deadline.
- Closest roster neighbors to compare before final routing: `acm-conext` (CoNEXT), `ieee-
  infocom` (INFOCOM), `usenix-annual-technical-conference` (USENIX ATC), `usenix-conference-
  on-file-and-storage-technologies` (FAST). Break ties by contribution type, evidence shape,
  reviewer community, and the current official CFP from 2026.eurosys.org.

## What distinguishes this venue from its closest siblings

- **What EuroSys is.** The **ACM (SIGOPS Europe)** flagship for **computer systems** broadly — OS, distributed systems, storage, virtualization, and systems for ML.
- **vs the networking venues.** SIGCOMM/INFOCOM/CoNEXT are networking-specific; bring OS/runtime/distributed-systems contributions to EuroSys.
- **vs SOSP/OSDI.** EuroSys is the European systems flagship alongside the USENIX/ACM OS venues; route by cycle, community, and systems sub-area rather than prestige.

## EuroSys-specific routing detail

- Prefer EuroSys when the contribution is systems research for the European systems community: OS, distributed systems, storage, cloud, runtimes, or systems infrastructure with a built artifact.
- Route networking protocol/measurement to INFOCOM/SIGCOMM/CoNEXT, flagship USENIX/ACM systems to OSDI/SOSP/NSDI, and storage-specific work to FAST.
- EuroSys evidence should show system design, workload realism, implementation depth, performance/reliability tradeoffs, and operational constraints.

## Method & evidence bar

- Build the artifact or prototype far enough that the core design can be measured under realistic workloads.
- Use appropriate baselines, sensitivity analyses, and workload characterization; systems reviewers look for hidden bottlenecks.
- Separate engineering effort from research contribution: name the abstraction, mechanism, or tradeoff.
- For EuroSys, the evidence must support the venue-specific signature: a systems paper with implementation depth and systems-community relevance.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Start from a systems pain point and show why existing abstractions fail.
- Use evaluation sections that answer research questions, not a tour of every benchmark run.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://2026.eurosys.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current USENIX/ACM/IEEE author kit, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at EuroSys, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle systems papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Toy implementation or microbenchmark-only evidence for a systems claim.
- No comparison to mature systems or no explanation of deployment constraints.
- Performance gains with unclear workload representativeness.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving EuroSys reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses EuroSys's bar, compare against `acm-symposium-on-operating-systems-principles` / `usenix-symposium-on-operating-systems-design-and-implementation` / `usenix-symposium-on-networked-systems-design-and-implementation` / `acm-sigcomm`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] EuroSys (EuroSys)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
