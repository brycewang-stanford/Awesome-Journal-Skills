---
name: fast-author-response
description: Use when drafting USENIX FAST author responses, covering the short pre-notification rebuttal during the author-response period and — distinctively — the one-shot-revision change ledger that maps every required change (including any newly required storage experiments) to a concrete result, resubmitted at the next deadline for a terminal accept/reject.
---

# FAST Author Response

Use this after FAST reviews arrive. FAST has **two distinct speaking turns**, and conflating them is
a common mistake: a short **author-response (rebuttal)** during the pre-notification window, and — if
you receive a **one-shot revision** — a full **change ledger** accompanying a revised paper that is
re-read for a terminal accept/reject. Both keep double-blind: the response and any revision material
must not reveal authors, institutions, systems by name, or a private repository.

## Triage (both turns)

- Answer what affects the decision: the storage contribution's significance, soundness of the
  measurement, device/state credibility, baseline fairness, tail-latency and endurance evidence,
  crash-consistency, and clarity.
- Use evidence that already exists or that the revision will concretely add — never a vague promise.
- Correct factual misreadings first; a reviewer who misread a device table or a steady-state caveat
  is often persuadable.
- Keep every word double-blind. Do not name your system's real name, institution, funder, datacenter,
  or a private trace URL, even to strengthen a point.

## Turn 1 — the author-response rebuttal

Short and decision-focused, written to fit the response form. One decision-critical point per
reviewer beats an exhaustive reply. Concede what is true, correct what is misread, and point to
exactly where the answer already lives in the submitted paper or artifact. Typical high-value moves
for a storage paper:

- Point to the testbed table / firmware / preconditioning detail a reviewer thought was missing.
- Clarify that a number is a device-counter measurement, not an estimate, with the section reference.
- If asked for a baseline or a crash test you cannot run in the window, say what you *can* commit to
  and how you would bound the gap — do not paste unverifiable new results.

## Turn 2 — the one-shot-revision change ledger (the distinctive FAST move)

A one-shot revision is a bounded, **terminal** revise-and-resubmit: the revised paper, submitted at
the next deadline, can only be accepted or rejected. The response is a **change ledger**: for every
required item, either do it and show it, or (rarely) explain precisely why it is infeasible and what
you did instead.

```text
[R1.1] Required: "Compare against the tuned stock compactor at steady state"
       -> Action: DONE  | added §5.3 + Table 4: bytes-written on <SSD, firmware> at steady state,
          tuned baseline with equal budget; 2.1x reduction (95% CI ...)
       -> Where: §5.3, Table 4; artifact/reproduce/rq2/
[R2.1] Required: "Show crash consistency is preserved"
       -> Action: DONE  | added §6: block-level record-and-replay at 500 injected crash points,
          all recover a consistent state
       -> Where: §6, artifact/crashtest/
[R2.2] Required: "Report tail latency, not mean"
       -> Action: DONE  | Fig. 7 now shows p50/p99/p99.9 under load
[R3.1] Requested: "Add a second datacenter trace"
       -> Action: PARTIAL | added one archived production trace; a second is under NDA and cannot be
          shared, so external validity is bounded explicitly in §7
```

The rule that turns a one-shot revision into an acceptance: **every required item is visibly done.**
Because the second read is terminal, a required change that is neither done nor squarely addressed is
what causes the reject — there is no third round to fix it.

## Reviewer pushback patterns

| Pushback | What it signals | FAST-ready response |
|---|---|---|
| "Was the SSD preconditioned?" | Steady-state / device-state doubt | Show the preconditioning protocol and re-report at steady state |
| "You report mean, not tail, latency" | Latency-distribution objection | Add p99/p99.9 distributions under load |
| "Baseline isn't tuned / is old hardware" | Comparison-fairness doubt | Re-run tuned, same hardware and state; report new numbers |
| "You never crash-test the durability claim" | Consistency-verification gap | Add fault-injection / record-and-replay recovery results |
| "WA is estimated, not measured" | Measurement-soundness doubt | Read bytes-written from device counters; show the script |
| "Does this hold beyond one drive/datacenter?" | External-validity limit | Add devices/traces or bound the claim explicitly |

## Anonymity in the response (easy to slip)

- Refer to your own prior work in the third person, as in the paper.
- Describe artifact/trace additions without linking an identity-revealing repository or host; use the
  anonymized location.
- Do not thank a named collaborator, funder, or hardware donor inside the response.
- Do not name your system, product, or datacenter even when a new result would read better with it.

## Calibration

- Respond to the criterion the reviewer actually raised, not the one you would rather defend.
- Length and format norms for the response, and the exact one-shot-revision instructions, vary by
  cycle; follow the current instructions precisely.
- The revised paper — not the ledger — must carry the argument; the ledger is a map to the changes.

## Output format

```text
[Turn] author-response rebuttal / one-shot-revision change ledger
[Priority issue] <reviewer concern>
[Decision dimension] significance / measurement soundness / device state / baseline / consistency / clarity
[Change ledger] <required item -> DONE/PARTIAL/infeasible-with-reason + where in paper/artifact>
[Anonymity check] <no identity leak in the response: passed/issues>
```
