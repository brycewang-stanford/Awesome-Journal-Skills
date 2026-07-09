---
name: mobisys-author-response
description: Use when drafting a MobiSys rebuttal after round-2 reviews — working within the scope limit (correct factual errors, answer specific reviewer questions), adding only directly-responsive new results, promising camera-ready work honestly, staying double-blind, and giving the area chair a clean rationale for a mobile-systems accept decision.
---

# MobiSys Author Response

Use this after MobiSys round-2 reviews are released. Reopen the current rebuttal instructions
and length limit before drafting, because scope and mechanics are cycle-specific. The MobiSys
rebuttal is **narrow by design**: it is not a revision and not a place to reargue the paper.

## Scope discipline

- The rebuttal is for **correcting factual errors** in the reviews and **answering specific
  questions** reviewers posed. Stay inside that scope.
- New experiments are admissible **only if they directly address reviewer feedback**;
  alternatively, you may **promise** results expected by the camera-ready deadline — but only
  ones you can actually deliver.
- Keep the reply **double-blind**: no institution, authorship, private repository, or
  identity-revealing device/account detail.
- Use existing submitted evidence first: figures, appendix tables, device provenance, and the
  artifact — point to them precisely rather than restating them.

## Triage

- Answer concerns that affect the **decision**: is the system real, is the on-device evidence
  sufficient, is the energy/latency claim defensible, is the contribution a system.
- Correct factual misreadings first (a reviewer who thinks you tested one device when you
  tested four), then address requests for a missing baseline, an energy boundary, or a
  break-condition experiment.
- One decision-critical point per reviewer beats an exhaustive reply; the AC reads for whether
  the central objection was actually resolved.

## Drafting pattern

1. State the decision-critical correction or concession first.
2. Point to exact submitted evidence (figure, table, appendix, artifact).
3. Explain the systems consequence — what it means for the device claim.
4. Promise a camera-ready fix only if it adds no unsupported claim and you can deliver it.

## Systems-reviewer pushback patterns

| Pushback | What it signals | MobiSys-ready fix |
|---|---|---|
| "Evaluated on one device" | Generalization doubt | Point to the multi-device table, or promise the added device honestly |
| "Energy numbers are unconvincing" | Undefined instrument/boundary | Name the power monitor, sampling rate, and envelope already in App. A |
| "Only a 30-second benchmark" | Throttling hidden | Reference the sustained-load run and thermal trace, or promise one |
| "This is a better model, not a system" | Fit doubt | Re-anchor the contribution as the runtime/scheduling mechanism, with the ablation that isolates it |

## Response micro-example

Reviewer objection: the latency win might vanish once the device throttles. Reply skeleton:

1. Concede the concern is the right one to raise for sustained load.
2. Point to the 20-minute run in Fig. 1 and the thermal trace in App. A, already submitted.
3. Note the win holds to steady state on all four devices, with the numbers regenerable from
   the artifact.
4. Offer one camera-ready sentence making the steady-state result explicit in the body.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] contribution / on-device evidence / energy-latency rigor / clarity
[Draft response] <MobiSys-ready anonymous text within scope>
[Evidence anchor] <figure/table/appendix/artifact item>
[Out-of-scope content removed] <reargument, identity leaks, undeliverable promises>
```
