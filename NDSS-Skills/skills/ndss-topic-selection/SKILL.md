---
name: ndss-topic-selection
description: Use when deciding whether a security project belongs at NDSS — the Network and Distributed System Security Symposium — or should route to IEEE S&P, USENIX Security, CCS, PETS, IMC, or ACSAC, applying NDSS's networked-adversary and deployment-realism tests before any writing begins.
---

# NDSS Topic Selection

NDSS is the Internet Society's slice of the security big four, and its center of gravity is
literal: security of things that are *networked or distributed* — protocols, the web, DNS
and routing, cloud and edge infrastructure, IoT fleets, and the measurement of all of the
above under attack. Work can be excellent and still be mis-routed here. Run these tests
before a word is drafted; the cheapest rejection is the one you never submit into.

## Three fit tests

1. **The wire test.** Describe the contribution without mentioning a network, a protocol, a
   distributed deployment, or Internet-scale phenomena. If the description survives intact,
   the paper's heart is somewhere else — a crypto venue, a software-engineering venue, an ML
   venue — and NDSS reviewers will sense it.
2. **The deployment-envelope test.** NDSS repeatedly rewards work whose design is *forced*
   by real-world constraints: no source code, no firmware access, gateway-class hardware,
   off-path adversaries, providers who must act unilaterally. If your evaluation only runs
   in a simulator with parameters you chose, expect the "would this survive contact with
   the Internet?" objection.
3. **The adversary-ownership test.** Someone concrete must be attacking something concrete.
   A robustness study without a capability-bounded adversary is a reliability paper.

## Routing against the neighbors

| Signal in your project | Better first target | Why |
| --- | --- | --- |
| Networked/distributed adversary, deployable result | **NDSS** | Exactly the center of scope |
| Systematization (SoK) ambition | IEEE S&P | The labeled SoK lane lives there, not at NDSS |
| Broad systems security, OS/hardware depth | USENIX Security | Its community leans systems-artifact |
| Applied-crypto protocol with proofs as the core | CCS or a crypto venue | Proof-first work fits their PC composition |
| Privacy as the primary lens, PET construction | PETS | Dedicated reviewer pool, journal-style rounds |
| Internet measurement with no adversarial angle | IMC | Measurement without attack is IMC's home turf |
| Operational/practitioner defense, modest novelty | ACSAC | Applied bar, friendlier to incremental hardening |

Route by contribution shape and reviewer community, never by prestige ranking or by which
deadline lands next — the workflow skill covers calendar strategy separately.

## NDSS-specific constraints that affect the decision

- **Two cycles, no same-year retry.** A paper rejected in the 2027 summer cycle cannot
  return with major overlap in the 2027 fall cycle. Choosing NDSS prematurely can burn the
  whole edition, not one deadline (CFP, checked 2026-07-08).
- **Six submissions per author per cycle.** Large groups must ration slots; a marginal-fit
  paper spends a slot a strong-fit paper may need.
- **Ethics gate at entry.** Projects built on live scanning, user data, or unpatched
  vulnerabilities need a disclosure-and-mitigation story *at submission time*; an Ethics
  Review Board can sink an otherwise strong paper. If the ethics story cannot be told, the
  project is not NDSS-ready regardless of technical merit.
- **The 2027 edition meets in Seoul (22-26 March)** — the first move away from San Diego —
  so factor travel and funding for the team into the venue choice like any other cost.

## Decision procedure

```text
1. State the adversary: capabilities, cost, vantage (on-path / off-path / insider).
2. Name the networked or distributed system under attack or defense.
3. Say which real-world constraint forces your design (the "envelope").
4. Draft the one-sentence delta vs. the nearest big-four paper of the last 3 years.
5. Confirm the ethics story is tellable today (disclosure state, harm handling).
6. If any of 1-5 fails → run the routing table above and pick the venue whose
   reviewers naturally ask the questions your paper actually answers.
```

## Anti-patterns seen at this venue

- **ML paper wearing a security costume**: novel model, borrowed intrusion dataset, no
  adversary reasoning. NDSS accepts ML-heavy work when the deployment envelope shapes the
  method (see Kitsune in `../../resources/exemplars/library.md`); it rejects the inverse.
- **Attack without a victim population**: a clever trick demonstrated on one lab target,
  with no argument about prevalence or preconditions in the wild.
- **Defense against yesterday's attacker**: evaluation only against published, non-adaptive
  attacks — reviewers here will improvise the adaptive one during discussion.
- **Journal pacing**: saving the strongest result for a follow-up. NDSS review gives no
  credit for a roadmap.

## Output format

```text
[NDSS fit] Strong / Plausible / Mis-routed
[Wire test] pass/fail — one line
[Deployment envelope] <the real constraint that shapes the design, or "none">
[Adversary] <capabilities and vantage in one line>
[Ethics story] tellable now / blocked by <item>
[Cycle risk] <summer/fall implications, cap usage, no-retry exposure>
[Alternative venue] <name + one-line reason, if fit is not Strong>
```
