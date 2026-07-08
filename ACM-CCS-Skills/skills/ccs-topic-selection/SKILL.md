---
name: ccs-topic-selection
description: Use when deciding whether a security project fits ACM CCS versus IEEE S&P, USENIX Security, NDSS, PETS, or a crypto/theory venue, identifying the security contribution type, and sharpening the threat model and attacker capability before writing begins.
---

# CCS Topic Selection

Use this before writing. ACM CCS is the SIGSAC flagship: it rewards work with a concrete
attacker, a defensible threat model, and evidence that survives an adversarial program
committee. Decide venue by community and contribution type, never by prestige ranking.

## Fit test

- Prefer CCS when the contribution is a broad computer-security result — a new attack class,
  a defense with measured cost, an applied-cryptography protocol, a systems or web-security
  mechanism, or a measurement study — aimed at the cross-area SIGSAC community.
- Route to IEEE S&P (Oakland) when the work suits that PC's taste for foundational or
  systematization framing and the November cycle fits your calendar better.
- Route to USENIX Security when the contribution is artifact-heavy systems security whose
  evidence lives in a runnable tool and open benchmark.
- Route to NDSS when the core is network- and distributed-system security (protocols, DNS,
  routing, malware infrastructure).
- Route to PETS/PoPETs when privacy is the primary lens rather than one property among many.
- Route to CRYPTO/EUROCRYPT when the contribution is cryptographic theory whose proof, not
  its deployment, is the result.

## Fit signal table

| Signal in the project | CCS reading |
|---|---|
| New attack with a clearly bounded adversary and demonstrated impact | Core fit — the house genre |
| Defense evaluated against adaptive attacks with deployment cost | Core fit |
| Applied crypto protocol with implementation and measured overhead | Core fit |
| Internet-scale or ecosystem measurement with validated sampling | Core fit |
| Pure cryptographic hardness proof, no system | CRYPTO/EUROCRYPT or a theory venue |
| Privacy-first metrics with no other security property | PETS/PoPETs |

## Vignette: where a side-channel result goes

A project extracts keys from a deployed TLS library via a microarchitectural side channel,
with a proof-of-concept exploit and a constant-time patch. CCS reading: strong fit — a
concrete attacker, measured leakage, and a defense with overhead numbers is exactly the CCS
arc. Strip the exploit and keep only an abstract leakage bound, and it drifts toward a crypto
theory venue; expand the network-measurement of vulnerable hosts into the whole story, and
NDSS becomes plausible; foreground only the privacy harm to users, and PETS fits better.

## Sharpening moves before committing

- Name the attacker: capabilities, knowledge, position, and what success means. If you cannot
  write the threat model in three sentences, the contribution is not yet CCS-shaped.
- Decide the contribution type — attack, defense, protocol, measurement, tool, or study —
  because reviewers grade each against a different evidence bar.
- Confirm the result fits the 12-page ACM sigconf body; CCS bodies are dense, and a paper
  needing 30 pages of proofs may belong at a journal or a theory venue.
- Scope drifts across cycles; scan the current CFP topic list and recent proceedings before
  final routing.

## Output format

```text
[Fit] strong CCS / possible CCS / better elsewhere
[Best venue] CCS / IEEE S&P / USENIX Security / NDSS / PETS / crypto venue / other
[Contribution type] attack / defense / protocol / measurement / tool / study
[Threat model in one line] <adversary capability and goal>
[Top rejection risk] <threat-model / novelty / evidence / ethics / scope>
[Next action] <sharpen threat model, add evidence, reframe, or switch venue>
```
