---
name: ieeesp-reproducibility
description: Use when hardening the reproducibility of an IEEE S&P (Oakland) paper's evidence before submission, including environment pinning for exploits and side channels, seed and trial reporting for probabilistic attacks, measurement snapshotting of live systems, and honest availability statements under ethical release limits.
---

# IEEE S&P Reproducibility

Use this while the evidence is being produced — months before
`ieeesp-artifact-evaluation` packages it. Security results decay in ways ML
results do not: targets get patched, infrastructure changes, and an attack
that "worked in March" can be unreproducible by review time. Reproducibility
at S&P is first about **freezing the world you measured**.

## Freeze the target, not just the code

| Evidence type | What must be pinned | Decay risk if not |
|---|---|---|
| Software exploit | Target version, build flags, distro, patch level | Silent fix ships mid-review |
| Microarchitectural attack | CPU model + stepping, microcode, OS mitigations state | Microcode update changes timing |
| Network measurement | Scan dates, vantage points, target-list snapshot | Internet moved; sample unrecoverable |
| Web/API study | Crawl date, client fingerprint, geographic origin | Server-side behavior shifts |
| ML attack/defense | Model weights hash, dataset version, threat-budget ε | "Same" model retrained differently |

Record these in the paper, not only in lab notes — a reviewer asking "does
this still work after <vendor>'s April update?" is a reproducibility question
about the *world*, and the answer is a documented snapshot date.

## Determinism ledger for probabilistic evidence

Attacks with success probabilities, fuzzing campaigns, and randomized
defenses need trial discipline:

- Report **trials, not anecdotes**: success rate over n runs with n stated,
  plus dispersion — a "9/10 successful" exploit and a "measured once" exploit
  are different claims.
- Fuzzing comparisons follow the field's known pitfalls: equal CPU-time
  budgets, multiple campaigns, identical seed corpora — state all three.
- Randomized defenses (ASLR-like, moving-target): evaluate across the
  randomness, not one lucky layout.
- Timing measurements: report the noise floor and the machine's quiescence
  conditions (isolated cores, frequency pinning) or the numbers will not
  transfer.

```text
Reproducibility ledger (one row per experiment in the paper):
  exp_id | claim it supports | target snapshot (ver/date/hw) |
  trials & seeds | dispersion reported? | rerun cost (time/hw/$) |
  rerunnable by outsider? (yes / gated / world-dependent)
```

The last column becomes the availability statement and the honest badge
target later.

## When ethics limits release, say exactly what and why

S&P reviewers accept withheld material when the reasoning is specific:

- "Exploit for CVE-pending issue withheld until the fix ships; released to
  reviewers via the chairs on request" beats a silent gap.
- User-derived datasets: describe schema and collection so others can
  re-collect ethically, even when raw data cannot ship.
- Never fabricate openness — a promised-but-empty repository found during
  review or after publication is a reputation event, and at this venue
  reviewers do check.

## Cheap habits that pay at rebuttal time

- One `env.lock` per experiment directory: container digest, package list,
  kernel and microcode versions, dumped automatically by the run script.
- Raw outputs archived before aggregation; the rebuttal question is always
  about a number two steps upstream of the figure.
- A `regenerate_figures.sh` that goes from archived raw data to every figure
  — this is also the artifact-evaluation core later.
- Date-stamped disclosure and measurement logs, because ethics questions in
  review are answered with timelines (`ieeesp-author-response`).

## What this venue does not require

Keep effort calibrated: S&P has no submission-time reproducibility checklist
in the verified 2026/2027 materials (待核实 each cycle), artifact evaluation
is post-acceptance and optional, and appendices are explicitly not
guaranteed reader attention. The reproducibility work above is therefore
aimed at three audiences in order: your own rebuttal, the shepherd, and the
AE committee — not at a submission-form requirement.

## Output format

```text
[Ledger status] <n>/<total> experiments with snapshot + trials + dispersion
[World-dependence] <which results cannot be re-run by anyone, ever — flagged in text?>
[Release plan] open / gated (reason) / withheld (reason) — per component
[Rebuttal readiness] raw data archived ✓/✗ · env locks ✓/✗ · figure regen ✓/✗
[Gaps to close before registration week] <ordered list>
```
