---
name: sosp-artifact-evaluation
description: Use when preparing a SOSP artifact for the post-acceptance evaluation run by the sysartifacts community, registering within days of notification, packaging for the cooperative review process, and targeting the ACM badges — Artifacts Available, Artifacts Evaluated Functional, and Artifacts Evaluated Reusable.
---

# SOSP Artifact Evaluation

Use this once a SOSP paper is accepted and the artifact-evaluation (AE) invitation
arrives. SOSP's AE is optional, runs **after** acceptance (so it never threatens the
paper decision), and is operated through the shared systems-community infrastructure at
`sysartifacts.github.io` with its own HotCRP instance (for 2025:
`sysartifacts.github.io/sosp2025/`, `sosp25ae.hotcrp.com`; verified 2026-07-08). The
CFP describes the clock plainly: a few days after notification to **register** the
artifact, then a few more days to polish it before evaluation begins.

## The process is cooperative — plan to be online

SOSP AE is explicitly interactive: evaluators report problems, authors fix them during
the window, and reasonable response time is an expectation, not a courtesy. The
strongest predictor of a failed evaluation is not code quality; it is an author team
that treated submission as fire-and-forget during the same weeks the camera-ready and
conference logistics were competing for attention.

- Name an AE owner who is not the shepherd-thread owner.
- Watch the AE HotCRP for evaluator comments daily during the window.
- Fixes during evaluation are legitimate; ship them as tagged revisions so evaluators
  can tell what changed.

## Badge targeting

SOSP badges follow the ACM artifact-review taxonomy. Choose targets deliberately — each
badge has its own checklist, and chasing all of them with a hardware-bound artifact is
a common own-goal.

| Badge | What evaluators check | Typical blocker |
|---|---|---|
| Artifacts Available | Artifact deposited in a public archival repository with a DOI/stable link | Only a GitHub URL — repos are not archival; cut an archived release |
| Artifacts Evaluated — Functional | Documented, consistent, complete, exercisable; evidence of verification | "Works on our cluster" scripts with hardcoded paths and hostnames |
| Artifacts Evaluated — Reusable | Functional bar plus docs and structure that let others build on it | No way to run on inputs other than the paper's |

Artifacts earning all available badges compete for the **Distinguished Artifact**
award — worth targeting when the artifact is genuinely the paper's contribution.

## Packaging for an OS-adjacent artifact

SOSP artifacts frequently need kernels, custom modules, specific NICs, or multi-node
clusters — things an evaluator cannot conjure. Tier the claims:

1. **Anyone-can-run tier**: build + unit-level functionality in a container or VM
   image, minutes not hours. This alone can carry Functional.
2. **Provided-hardware tier**: reserved access to your cluster or a public testbed
   (CloudLab-style) with exact node profiles, for headline performance results.
3. **Documented-only tier**: results needing unobtainable hardware or proprietary
   traces; state clearly that these are documented, not re-runnable, and do not claim
   badges over them.

```text
artifact/
  README.md            # claims map: paper claim -> experiment -> expected output & tolerance
  ARTIFACT-CHECKLIST   # target badges, per-badge self-assessment
  kick-the-tires/      # <30 min smoke path evaluators run first
  build/               # container/VM definitions, pinned toolchain and kernel version
  experiments/         # one dir per paper figure/table, run.sh + plot.sh each
  hardware/            # node specs, testbed profile, reservation instructions
  LICENSE
```

The claims map matters more than any script: evaluators reproduce **claims**, so state
for each figure what "success" means numerically (for example, "throughput within 10%
of Fig. 7's trend; absolute numbers vary with hardware").

## Kick-the-tires discipline

Most SOSP-style AE processes open with a smoke-test phase. Whatever the current year
calls it, build for it: a top-level path that a stranger on a fresh machine can
complete in under half an hour, exercising the build and one small end-to-end run.
Rehearse it literally on a fresh VM with a lab member who did not write the code, and
time it. Every minute of evaluator confusion in the first session is paid back as
skepticism for the rest of the window.

## What AE cannot do

- It cannot change the acceptance decision, and evaluators are anonymous to authors —
  keep interactions inside the AE HotCRP.
- It does not certify performance portability; badges say the artifact was exercised,
  not that your speedups hold on other silicon.
- Badge names, phases, and dates are re-announced per cycle by the sysartifacts chairs;
  the 2026-cycle SOSP AE page details were not yet pinned when this pack was written
  (待核实) — read the year's call before promising badges to co-authors.

## Output format

```text
[AE decision] participate? badges targeted
[Clock] registration due / polish window / evaluation window
[Tier map] claim -> anyone-can-run / provided-hardware / documented-only
[Kick-the-tires] rehearsed on fresh machine? duration?
[Owner] AE-window responder (distinct from shepherd owner)
[Risk] <single most likely evaluator blocker>
```
