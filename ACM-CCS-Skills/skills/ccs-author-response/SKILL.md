---
name: ccs-author-response
description: Use when drafting an ACM CCS rebuttal during the HotCRP author-response window, covering threat-model defenses, adaptive-attack objections, ethics and disclosure questions, anonymity constraints, adversarial reviewer pushback patterns, and decision-focused replies aimed at the meta-reviewer.
---

# CCS Author Response

Use this after CCS reviews are released. Reopen the current HotCRP rebuttal instructions and
any length or format limits before drafting, because response mechanics are set per cycle.

## Triage

- Answer concerns that affect the decision: threat-model soundness, novelty, correctness,
  evidence quality, ethics, and disclosure. Skip cosmetic complaints unless space allows.
- Use evidence already in the submission: sections, appendices, measurement tables, and the
  ethics section. The rebuttal clarifies the submitted paper; it does not add a new paper.
- Keep the reply anonymous. Do not reveal institution, authorship, private URLs, or the
  identity of a disclosed vendor if that would deanonymize you.
- Correct factual misreadings first, then address the strongest objection to the attacker
  model or the adaptive evaluation.
- Do not promise experiments you cannot run before camera-ready; promise only edits that add
  no unsupported claim.

## Drafting pattern

1. State the decision-critical correction or concession in the first line.
2. Point to exact submitted evidence (section, figure, appendix).
3. Explain the security consequence — why the attack still holds, or the defense still binds.
4. Offer a scoped camera-ready edit only where it clarifies without over-claiming.

## Adversarial reviewer pushback patterns

| Pushback | What it signals | CCS-ready fix |
|---|---|---|
| "The attacker assumes too much" | The threat model looks unrealistic | Point to where the capability is justified, or scope the claim to the realistic subset and concede the rest |
| "You never tested an adaptive attacker" | The defense evaluation looks incomplete | Reference the adaptive experiment if present; if absent, concede and commit to a bounded camera-ready addition only if honestly feasible |
| "This is already a known CVE" | A prior-art gap | Distinguish root cause, scope, or impact from the CVE, with the specific technical delta |
| "The ethics of this are unaddressed" | Disclosure or harm concern | State the disclosure timeline, the harm-minimization steps, and the reasoning, quoting the ethics section |

## Response micro-example

Reviewer objection: the key-recovery attack assumes co-located measurement that real
attackers cannot achieve. Reply skeleton:

1. Concede the strongest form needs co-location; scope the practical claim to that setting.
2. Point to Section 6 where a remote variant with degraded rate is already measured.
3. Note the defense in Section 7 blocks both variants, so the contribution stands.
4. Offer one camera-ready sentence making the co-location assumption explicit in the intro.

## Rebuttal calibration

- One decision-critical point per reviewer beats an exhaustive rebuttal; CCS meta-reviewers
  read for whether the central threat-model or ethics objection was actually resolved.
- Never paste new experimental results the reviewers cannot verify; describe what exists and
  anchor it in the submission.
- Answer the ethics reviewer directly and early; an unaddressed disclosure concern outweighs
  resolved technical nits at decision time.

## Output format

```text
[Priority issue] <reviewer concern>
[Decision dimension] threat model / novelty / correctness / evidence / ethics
[Draft response] <CCS-ready anonymous text>
[Evidence anchor] <section / figure / appendix item>
[Forbidden content removed] <identity leaks, unverifiable new results, over-promises>
```
