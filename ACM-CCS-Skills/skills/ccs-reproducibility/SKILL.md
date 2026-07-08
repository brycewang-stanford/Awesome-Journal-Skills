---
name: ccs-reproducibility
description: Use when strengthening ACM CCS reproducibility evidence, including the artifact-availability posture, threat-model-to-evidence mapping, attack reproduction steps, defense overhead measurement, measurement-dataset provenance, environment and version pinning, and honest justification when artifacts cannot be shared.
---

# CCS Reproducibility

Use this before submission and again before the artifact-evaluation deadline. Reopen the
current CFP and call for artifacts to confirm what availability statement and packaging CCS
expects this cycle.

## Evidence map

- Map each security claim — every attack, defense guarantee, and measurement result — to a
  verifiable location: a script, a config, a dataset, a proof, or a logged run.
- For attacks, record the target's exact version and configuration, the attacker's resource
  budget, and the sequence of steps that reproduce the exploit.
- For defenses, record the workload, the overhead-measurement method, the hardware, and the
  adaptive attacker used, so the cost-versus-security tradeoff can be rechecked.
- For measurements, document the vantage point, the collection window, the sampling frame,
  known blind spots, and the ground-truth validation.
- When artifacts cannot be shared — licensing, responsible disclosure, subject safety, or
  premature-release risk — say so explicitly and offer partial, synthetic, or redacted
  artifacts that still let a reader assess the methodology.

## Availability-posture table

| Claim type | What full sharing looks like | Honest fallback when sharing is blocked |
|---|---|---|
| Exploit against deployed software | Runnable PoC plus target build | Redacted PoC, disclosed-and-patched note, synthetic target |
| Defense with overhead numbers | Instrumented build and benchmark scripts | Binaries plus measurement scripts if source is proprietary |
| Internet-scale measurement | Dataset plus collection tooling | Aggregated data with subject-privacy justification for the rest |
| Cryptographic protocol | Reference implementation and test vectors | Spec plus test vectors if the implementation is embargoed |

Claiming an artifact is unavailable without a reason CCS accepts (a license, a disclosure
embargo, subject safety) reads as evasion; state the specific reason and offer the closest
shareable substitute.

## Vignette: a measurement paper on vulnerable hosts

Consider a study scanning the Internet for a misconfiguration. Its reproducibility spine: the
scan methodology and rate-limiting, the classification rule for "vulnerable," the ground-truth
sample validated by hand, the ethics of scanning and notification, and an aggregated dataset
that preserves the finding without exposing individual vulnerable hosts to opportunistic
attackers.

## Degrees of reproducibility

- Turnkey: one command reproduces the attack or the overhead measurement from pinned configs.
- Scripted: scripts exist but need documented manual steps or gated data access.
- Descriptive: prose detailed enough that a competent security researcher could rebuild it.

For CCS, aim turnkey for anything you submit to artifact evaluation, and state the achieved
level honestly rather than overpromising a one-command reproduction that fails on a clean host.

## Output format

```text
[Claim inventory] <claim -> evidence location>
[Availability posture] full / partial / justified-withheld
[Reproducibility gaps] <versions / configs / budgets / provenance / ethics>
[Paper fixes] <must appear in main PDF or appendix>
[Artifact fixes] <packaging additions before the AE deadline>
```
