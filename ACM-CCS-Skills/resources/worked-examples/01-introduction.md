> **Illustrative teaching example.** The paper, system, attacker, and every number below are
> **fictional** and exist only to demonstrate CCS house style. No real-paper facts, targets, or
> results are stated, and no policy is invented. Corresponding skills:
> [`ccs-writing-style`](../../skills/ccs-writing-style/SKILL.md),
> [`ccs-topic-selection`](../../skills/ccs-topic-selection/SKILL.md), and
> [`ccs-experiments`](../../skills/ccs-experiments/SKILL.md).

# Worked Example: A CCS-Style Abstract + Introduction (before → after)

This demonstrates the **CCS first-page arc** from `ccs-writing-style`:
**problem → attacker (threat model) → gap in existing attacks/defenses → mechanism →
evidence → why it matters to the security community** — with the CCS rules that the threat
model is **explicit and early**, and **every claim is paired with a demonstration, a
measurement, a proof, or a cost number** (no exploitability claims beyond what was tested).

The framing also reflects `ccs-topic-selection`: CCS is strongest when there is a **concrete
adversary and demonstrated impact**, not an abstract weakness — here, a working key-recovery
attack plus a measured defense, not a systems win that would route to a systems venue.

**Illustrative paper (fictional):** *"Silent Keys: Practical Key Recovery from a Deployed TLS
Library via a Shared-Cache Side Channel, and a Constant-Time Defense."*

---

## Before (buries the contribution — typical first-draft abstract + intro)

> **Abstract.** Side channels are an important security problem. In this work we study cache
> side channels, which have been researched extensively. We present a new technique that
> exploits shared caches and show that it works well against cryptographic software. We also
> propose a defense. Our approach outperforms prior work in most settings.
>
> **Introduction.** Cryptography is widely deployed. Many side-channel attacks exist,
> including timing attacks, cache attacks, and power analysis. In this paper, we use a shared
> cache to attack a library and recover secrets. We evaluate our attack and show it is
> effective, and we add a defense that mitigates it. Section 2 reviews related work, Section 3
> describes our attack, Section 4 our defense, Section 5 experiments, and Section 6 concludes.

**What's wrong (against `ccs-writing-style` / `ccs-topic-selection` / `ccs-experiments`):**

- **No threat model on the first page** — who is the attacker, where do they sit, what do they
  know? CCS reviewers reject on an undefined or shifting adversary.
- **No concrete target** — "a library," "cryptographic software" names nothing measurable; the
  `ccs-experiments` rule is to name the exact version and configuration.
- **Overclaims** ("works well," "outperforms in most settings") with **no attacker cost and no
  defense overhead** reported.
- **No claim → evidence pairing**: "effective" is not tied to a key-recovery demonstration or a
  measured query budget.
- **Defense asserted, never adapted against** — the classic CCS defense reject (`ccs-experiments`).
- **Over-signposted roadmap** standing in for an argument.

---

## After (CCS arc — problem → attacker → gap → mechanism → evidence → why it matters)

> **Abstract.** Constant-time discipline is widely assumed to protect TLS key material, but we
> show a **co-located attacker sharing an L3 cache** can recover a 2048-bit RSA private key
> from **LibFoo v3.2 on x86-64** using a shared-cache side channel, despite the library's
> partial constant-time hardening. Our attack, **Silent Keys**, exploits a data-dependent
> table access left in the modular-exponentiation path; it recovers the full key in a median
> of **12,000 victim TLS handshakes** without privileged access. We responsibly disclosed to
> the LibFoo maintainers, who assigned a CVE and merged our patch. We then present a
> **constant-time exponentiation rewrite** and show it blocks Silent Keys and two adaptive
> variants at **1.8% handshake-latency overhead**. All attack and overhead numbers are
> reported over 50 trials with confidence intervals. *(problem → attacker → gap → mechanism →
> evidence → cost — all on the first page.)*
>
> **Introduction.** *(¶1 — problem + attacker, first breath.)* TLS libraries adopt constant-time
> coding to deny side-channel attackers, but "constant-time" is often **partial**. We consider
> a realistic adversary: an **unprivileged process co-located on the same host** as a TLS
> server — the standard public-cloud tenancy threat model — with no access to the victim's
> memory and only the ability to contend for the shared L3 cache.
>
> *(¶2 — gap: why existing attacks and defenses are insufficient.)* Prior cache attacks on this
> library targeted the multiplication path, which the maintainers hardened; the community
> treated the library as side-channel-safe. But the hardening **missed a table lookup** in the
> exponentiation routine. Existing defenses either assume the whole path is already
> constant-time or impose overheads too large for production TLS. *(each prior line gets a
> specific gap, not a vague "prior work is limited.")*
>
> *(¶3 — mechanism + the explicit assumption.)* Silent Keys uses a Prime+Probe primitive on the
> table's cache set to leak a data-dependent access pattern, then reconstructs the key from the
> leaked bits. The **only** assumptions are **co-location** and **shared inclusive L3**; we
> require no privilege escalation and no victim cooperation. *(threat model stated plainly, per
> the CCS rule that a shifting adversary is review risk.)*
>
> *(¶4 — evidence, each claim paired.)* We demonstrate full key recovery against **LibFoo v3.2
> on two Intel microarchitectures** (Section 5), reporting the median and distribution of
> handshakes required over 50 trials (Table 1). We disclosed responsibly; the ethics section
> (Appendix E) gives the timeline. Our constant-time rewrite (Section 6) blocks the original
> attack and two adaptive attackers that target the rewritten path (Section 7), at **1.8%
> measured latency overhead** on a standard handshake workload (Table 3). *(every claim →
> demonstration, table, or ethics location.)*
>
> *(¶5 — why it matters to the security community + roadmap.)* The contribution is to show that
> **partial constant-time hardening gives false assurance** in a common cloud threat model, and
> to provide a deployable fix with measured cost. Section 2 states the threat model and
> background; Section 3 the attack; Sections 6-7 the defense and its adaptive evaluation.
> *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the CCS bar

Mapped to the skill checklists:

- **Threat model on the first page** — the abstract and ¶1 name the co-located unprivileged
  attacker and the cloud tenancy setting before any mechanism detail (`ccs-writing-style`:
  "state attacker capabilities, knowledge, position, and goal before results").
- **Concrete target** — LibFoo v3.2 on named microarchitectures, not "a library"
  (`ccs-experiments`: name the exact version and configuration).
- **Every claim paired with evidence** — key recovery → Section 5/Table 1; disclosure →
  Appendix E; defense → Section 6; adaptivity → Section 7; overhead → Table 3
  (`ccs-writing-style` and `ccs-experiments` claim→evidence map).
- **No overclaiming** — "median 12,000 handshakes," "1.8% overhead," reported "over 50 trials
  with confidence intervals," not "works well" (`ccs-experiments`: report attacker budget and
  measured defense cost).
- **Adaptive evaluation present** — the defense is tested against two attackers that know the
  rewrite, not only the original attack (`ccs-experiments`: the middle element of the defense
  triad).
- **Ethics handled** — responsible disclosure, CVE, and a dedicated ethics appendix
  (`ccs-supplementary`, `ccs-reproducibility`).
- **Right venue** — a concrete adversary with demonstrated impact plus a deployable defense is
  a strong CCS fit, not an abstract-crypto or systems re-route (`ccs-topic-selection` fit test).
- **12-page discipline** — the full proof of reconstruction and the ethics timeline sit in
  appendices while the body stays judgeable on its own (`ccs-writing-style`: use the 12-page
  body for the core argument).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified CCS
> papers** (ACM DL, including Test-of-Time winners) whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for CCS-specific submission policy.
