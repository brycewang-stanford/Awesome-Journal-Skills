---
name: ieee-international-conference-on-acoustics-speech-and-signal-processing
description: Use when targeting IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) or deciding whether a computer-science manuscript fits this venue. Encodes conference fit, framing, evidence bar, submission-cycle checks, rebuttal posture, and desk-reject risks for signal processing.
---

# IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)

## Conference positioning

IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) is a top computer-science conference venue for signal processing, speech, audio, image, ML for signals, and communications signal methods. It rewards a signal-processing paper with mathematical framing and reproducible empirical validation. Treat this skill as a **fit / venue-selection / re-framing** tool for conference submission strategy, not as a substitute for the current year's CFP, author kit, ethics policy, or submission portal.

Because CS conferences change deadlines, templates, page limits, review workflow, artifact rules, AI-use policy, and rebuttal formats every cycle, always verify the live official instructions before making a submission-ready recommendation. Start from the official source anchor recorded for this venue in `../../resources/conference-roster.md` and `../../resources/official-source-map.md`.

## When to trigger

- The author names ICASSP / IEEE International Conference on Acoustics, Speech and Signal Processing as the target venue.
- A manuscript in signal processing needs a conference-fit read before being formatted or submitted.
- The paper must be re-framed from journal style or arXiv style into a selective CS conference narrative.
- The author needs an evidence-gap, anonymity, artifact, rebuttal, or re-routing diagnosis for this venue.

## Scope & topic fit

- Core fit: signal processing, speech, audio, image, ML for signals, and communications signal methods.
- Best submissions make a precise contribution type visible: algorithm, theorem, system, dataset, benchmark, empirical finding, design artifact, tool, or socio-technical analysis.
- The paper should explain why the result matters to ICASSP's reviewers, not just why it is interesting to the authors' lab or product context.
- Position related work against the most recent conference-cycle papers in this venue and its closest siblings; stale comparisons are a common early-review weakness.
- If the contribution is interdisciplinary, state which part is CS research and which part is domain evidence.

## Venue-specific calibration

- Reviewer lens: Treat ICASSP as signal processing first: mathematical signal models, audio/speech/image processing, estimation, transforms, communications signals, and reproducible experiments matter. A paper that is only generic deep learning without signal insight will look misplaced.
- Contribution hook to foreground: the venue-specific contribution bar.
- Scope vocabulary to use naturally in the abstract and introduction: signal processing, speech, audio, image, ML for signals, and communications signal methods.
- Distinctive fingerprint for reviewer calibration: signal, processing, speech, audio, image, signals, communications, methods, venue-specific, contribution, ieeeicassp.
- Official anchor domain: 2026.ieeeicassp.org. Quote annual rules only after opening that source and the current-year CFP/author kit.

## Close-neighbor routing guardrail

- Use this profile only when the manuscript's central contribution is genuinely in signal
  processing and the author can say why ICASSP reviewers are the primary audience, not merely
  a convenient deadline.
- Closest roster neighbors to compare before final routing: `ieee-conference-on-virtual-reality-
  and-3d-user-interfaces` (IEEE VR), `international-conference-on-computational-linguistics`
  (COLING), `acm-sigir-conference-on-human-information-interaction-and-retrieval` (CHIIR),
  `acm-ieee-joint-conference-on-digital-libraries` (JCDL). Break ties by contribution type,
  evidence shape, reviewer community, and the current official CFP from 2026.ieeeicassp.org.

## Method & evidence bar

- Clone-audit guardrail: ICASSP should stay signal-processing first. A paper fits
  when the contribution changes representation, estimation, filtering,
  source separation, speech/audio modeling, beamforming, coding, image/signal
  restoration, or communications-signal inference. If the manuscript is mainly
  planning, NLP, information retrieval, knowledge capture, or generic ML
  benchmarking with no signal model, compare ICAPS/COLING/SIGIR/K-CAP/NeurIPS
  before recommending ICASSP.
- Compare against current strong baselines and explain exactly what changes in the algorithm, objective, data, or inference procedure.
- Report ablations that isolate the claimed mechanism; do not rely on aggregate benchmark wins alone.
- Document data, compute, hyperparameters, model selection, and failure cases so the result can be reviewed as science rather than demo output.
- For ICASSP, the evidence must support the venue-specific signature: a signal-processing paper with mathematical framing and reproducible empirical validation.
- Include limitations, negative results, compute/resource reporting, data provenance, and ethics details when they affect the claim.

## Structure & house style

- Frame the contribution as a reusable idea: method, theory, benchmark, dataset, system, or socio-technical finding.
- Separate main claims from exploratory results; reviewers at top AI venues punish overclaiming and hidden cherry-picking.
- Use the current official template exactly; do not guess page limits, font sizes, supplement rules, anonymity exceptions, or camera-ready requirements from old cycles.
- The introduction should answer: problem, why now, what is new, why this venue, and what evidence proves the claim.
- Put the strongest result in the main paper, not only in the appendix or supplement; reviewers should not have to reconstruct the contribution.

## Official-cycle checklist

- Open the live official venue page: https://2026.ieeeicassp.org/
- Re-check the current cycle's CFP, author kit, submission system, abstract/paper deadlines, page limits, supplementary-material rules, anonymity policy, dual-submission policy, ethics policy, AI-use policy, artifact/code/data expectations, rebuttal/author-response format, and camera-ready requirements.
- Confirm the review workflow and portal: OpenReview / CMT / HotCRP / PCS / START or society portal, as specified for the current cycle.
- Check whether accepted papers require in-person presentation, separate registration, artifact badges, proceedings copyright, or post-acceptance release forms.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence states why this manuscript belongs at ICASSP, using the venue's scope rather than generic "top conference" language.
- [ ] The claim is calibrated to the evidence: no broader than the datasets, proofs, systems, user studies, deployments, or threat model support.
- [ ] Related work includes the nearest current-cycle signal processing papers and explains the technical delta.
- [ ] The paper satisfies the current official template, anonymity, ethics, artifact, and rebuttal requirements.
- [ ] The main paper is self-contained enough for reviewers to evaluate novelty and correctness without hunting through external links.

## Common desk-reject triggers

- Leaderboard-only novelty with weak explanation of why the method works.
- Unclear data contamination, missing baselines, or evaluation that cannot be reproduced.
- Claims about safety, fairness, health, or society without matching evidence and limitations.
- Formatting, anonymity, dual-submission, external-link, or supplement violations under the current-year policy.
- A contribution framed for a neighboring field while giving ICASSP reviewers too little technical or empirical substance.

## Re-routing decision

If the paper misses ICASSP's bar, compare against `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence`. Re-route based on contribution type, not prestige: theory to a theory venue, systems to a systems venue, application-heavy work to a domain venue, and early ideas to workshops or shorter tracks when the official CFP supports them.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)
[Contribution type] algorithm / theory / system / dataset / benchmark / empirical / design / security / other
[Main evidence gap] <single most important missing proof, experiment, study, artifact, or policy check>
[Official items to re-check] CFP / author kit / deadline / format / anonymity / ethics / AI-use / artifact / rebuttal / camera-ready
[Top rejection risk] <venue-specific risk>
[Re-route suggestion] <better-matched conference or journal if not a fit>
```
