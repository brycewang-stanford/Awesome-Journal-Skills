---
name: ieee-acm-international-symposium-on-microarchitecture
description: Use when targeting IEEE/ACM International Symposium on Microarchitecture (MICRO) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for microarchitecture flagship.
---

# IEEE/ACM International Symposium on Microarchitecture (MICRO)

## Conference positioning

IEEE/ACM International Symposium on Microarchitecture (MICRO) is a top computer-science conference venue for microarchitecture, processors, accelerators, memory hierarchy, performance, and hardware/software interface. It rewards a microarchitecture paper with careful methodology, baselines, and workload characterization. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names MICRO / IEEE/ACM International Symposium on Microarchitecture as the target venue.
- A manuscript in microarchitecture needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: microarchitecture, processors, accelerators, memory hierarchy, performance, and hardware/software interface.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to MICRO's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat MICRO as a microarchitecture flagship venue whose reviewers expect the scope and evidence to match its own community. Do not submit a generic CS paper until the introduction names the exact subcommunity, contribution type, and proof or empirical standard.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: microarchitecture, processors, accelerators, memory hierarchy, performance, and hardware/software interface.
- Distinctive fingerprint for reviewer calibration: microarchitecture, processors, accelerators, memory, hierarchy, performance, hardware, software, interface, venue-specific, contribution, flagship, microarch.
- Official anchor domain: www.microarch.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in
  microarchitecture flagship and the author can say why MICRO reviewers are the primary
  audience, not merely a convenient deadline.
- Closest roster neighbors to compare before final routing: `architectural-support-for-
  programming-languages-and-operating-systems` (ASPLOS), `international-symposium-on-computer-
  architecture` (ISCA), `ieee-international-symposium-on-high-performance-computer-
  architecture` (HPCA), `international-conference-for-high-performance-computing-networking-
  storage-and-analysis` (SC). Break ties by contribution type, evidence shape, reviewer
  community, and the current official CFP from www.microarch.org.

## Method & evidence bar

- Clone-audit guardrail: MICRO is not interchangeable with systems, networking,
  or recommender venues. The central mechanism must live below or across the ISA,
  core, cache, memory hierarchy, accelerator, interconnect, branch/prefetch,
  scheduling, or hardware/software co-design boundary. If the contribution is a
  deployed OS service, network protocol, storage system, or application-level
  recommender workload with no new microarchitectural mechanism, route to
  OSDI/SOSP/ATC/NSDI/SIGCOMM/RecSys instead.
- Build the artifact or prototype far enough that the core design can be measured under realistic workloads.
- Use appropriate baselines, sensitivity analyses, and workload characterization; systems reviewers look for hidden bottlenecks.
- Separate engineering effort from research contribution: name the abstraction, mechanism, or tradeoff.
- For MICRO, the evidence must support the venue-specific signature: a microarchitecture paper with careful methodology, baselines, and workload characterization.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Start from a systems pain point and show why existing abstractions fail.
- Use evaluation sections that answer research questions, not a tour of every benchmark run.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://www.microarch.org/micro59/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: the current USENIX/ACM/IEEE author kit, artifact policy, and submission system.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at MICRO, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle microarchitecture flagship papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Toy implementation or microbenchmark-only evidence for a systems claim.
- No comparison to mature systems or no explanation of deployment constraints.
- Performance gains with unclear workload representativeness.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving MICRO reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses MICRO's bar, compare against `acm-symposium-on-operating-systems-principles` / `usenix-symposium-on-operating-systems-design-and-implementation` / `usenix-symposium-on-networked-systems-design-and-implementation` / `acm-sigcomm`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE/ACM International Symposium on Microarchitecture (MICRO)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
