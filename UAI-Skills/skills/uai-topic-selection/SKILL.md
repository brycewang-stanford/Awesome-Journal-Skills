---
name: uai-topic-selection
description: Use when deciding whether a project belongs at UAI, where uncertainty representation, probabilistic reasoning, graphical models, causal inference, or decision making under uncertainty must be the contribution itself, and when to route instead to AISTATS, NeurIPS, ICML, COLT, CLeaR, or a statistics journal before drafting begins.
---

# UAI Topic Selection

Use this before writing a line. UAI — the AUAI's annual conference, running since the
1980s — is the venue where uncertainty is the subject, not the seasoning. The 2026 CFP
invited novel theory, methodology, and applications spanning AI, machine learning, and
statistics, but the reviewer pool and the accepted-paper record reward a specific
shape: papers whose contribution is a probabilistic representation, an inference
procedure, a causal identification result, or a decision rule under uncertainty.

## The one-question filter

*If you deleted every probabilistic element from this paper, would anything remain?*

- Remains a strong paper → the probability is decoration; route to a general ML venue.
- Nothing remains → you are holding a UAI candidate; now check the evidence shape.
- A weaker but real paper remains → the venue call depends on which half is novel;
  interrogate with the table below.

## Signal table

| Project signal | UAI reading |
|---|---|
| New inference algorithm (MCMC, SMC, variational, belief propagation) with analysis | Home territory since the venue's founding |
| Identifiability or discovery result for causal or graphical structure | Core — UAI is a first-choice causality venue |
| Calibration, conformal, or coverage guarantee for predictive models | Strong fit; growing lane in recent volumes |
| Decision making / planning under uncertainty, Bayesian experimental design | Core, especially with formal treatment |
| Probabilistic programming semantics or inference | Distinctive UAI lane, rare elsewhere |
| Deep architecture, uncertainty used only as an evaluation metric | Re-route: NeurIPS / ICML / ICLR |
| General estimation theory, uncertainty incidental | Often better at AISTATS |
| Pure regret/sample-complexity theory, no probabilistic-modeling core | COLT or ALT |
| Causal ML with an applied-community audience | Compare CLeaR before defaulting to UAI |
| Journal-depth asymptotics needing 40 pages | JMLR or a statistics journal |

## Sibling-venue geometry

AISTATS and UAI are the commonly confused pair — both single-deadline, PMLR-published,
statistics-adjacent, and of comparable scale. A working separation: AISTATS emphasizes
the statistics–ML interface broadly (estimators, rates, high-dimensional methods);
UAI concentrates on the representation and use of uncertainty itself — graphical
models, causality, Bayesian reasoning, decisions. A debiased estimator with a
convergence rate leans AISTATS; an identifiability theorem over MAGs leans UAI; a
calibrated-prediction method with finite-sample coverage plays at either, so decide by
which reviewer conversation helps the work more.

Timing is a legitimate tiebreaker between honest fits: UAI's cycle (submission ~February,
decision ~June) interleaves with AISTATS (~October submission) and NeurIPS/ICML, and a
paper genuinely at home in two venues may reasonably pick the calendar that meets it
ready. Never let timing overrule fit — a misrouted paper burns a cycle anyway.

## Sharpening a genuine fit

1. Name the probabilistic object the paper contributes: a posterior approximation, a
   graph class, an identification condition, an interval, a policy. No object, no UAI
   framing.
2. Name the guarantee or diagnostic attached to it: consistency, coverage, ESS
   efficiency, SHD improvement, regret bound. This becomes the page-1 promise.
3. Check the evidence shape fits an 8-page main part with appendices — one decisive
   exact-truth experiment beats six benchmark sweeps here.
4. Scan the current CFP's topic list (2026 spanned inference families, optimization,
   probabilistic programming, and application areas from computational biology to
   robotics) to phrase your subject areas in the venue's own vocabulary.

## Borderline vignettes

Three recurring hard calls, with the reasoning that resolves them:

- **"We add a Bayesian layer to a transformer and report accuracy plus ECE."**
  The deletion test partially survives (the architecture stands alone), and the
  uncertainty content is evaluation-grade, not contribution-grade. As described:
  NeurIPS/ICML material. It becomes UAI-shaped only if the paper's center of gravity
  moves — e.g., a posterior-approximation scheme with analyzed bias, or a calibration
  guarantee — and the architecture becomes the test bed.
- **"We prove a regret bound for Thompson sampling in a structured bandit."**
  Probabilistic object (posterior sampling policy) and guarantee (regret) both
  present. The split: if the novelty is the *analysis technique*, COLT/ALT readers
  value it most; if the novelty is the *modeling of uncertainty in the structure*
  (priors over graphs, correlated arms), UAI is the natural room.
- **"We identify treatment effects under a new missingness mechanism, with an
  estimator and simulations."** Identification result + estimator + coverage
  simulations is simultaneously UAI-core and AISTATS-core. Decide by conversation:
  UAI if the paper leans on graphical criteria and reasoning about the mechanism;
  AISTATS if it leans on estimation theory and rates. Either way, do not split the
  difference in the framing — pick one audience and write for it.

## Calendar map for re-routes

If the verdict is "route elsewhere", the practical question becomes *when*. Approximate
rhythm of the neighbors (always verify each venue's current dates):

- AISTATS: submissions historically in early autumn, conference in spring — the
  natural next stop after a February UAI miss.
- NeurIPS: late-spring deadline; ICML: winter deadline close to UAI's own — an ICML
  reject can often turn around for UAI in the same season, and vice versa.
- COLT: winter deadline, summer conference; CLeaR: autumn-ish deadline for the
  causality community.
- JMLR / statistics journals: rolling — the release valve when the contribution
  outgrew 8 pages, not a consolation prize.

Keep the re-route target written down *before* the UAI decision arrives; deciding
while disappointed produces prestige-chasing, not fit-chasing.

## Anti-signals worth trusting

- The draft's introduction cites no UAI, AISTATS, or CLeaR papers at all — the
  community you are addressing does not include the one you are submitting to.
- The strongest section is a systems/scaling result and the probabilistic section
  defends design choices rather than proving properties.
- The reviewers you would wish for are all from one distant subfield.
- You cannot fill the `[Attached guarantee]` line below without the word "hope".

## Output format

```text
[Deletion test] survives without probability? yes / partially / no
[Probabilistic object] <posterior / graph / interval / policy / condition>
[Attached guarantee] <the formal or diagnostic promise>
[Verdict] UAI-first / UAI-viable / route to <AISTATS | NeurIPS/ICML | COLT | CLeaR | journal>
[Next step] <framing fix, missing experiment, or venue switch>
```
