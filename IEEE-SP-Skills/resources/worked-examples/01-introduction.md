> **Illustrative teaching example.** The paper, attack, system, and every
> number below are **fictional** and exist only to demonstrate IEEE S&P house
> style. No real-paper facts, targets, or results are stated, and no policy is
> invented. Corresponding skills:
> [`ieeesp-writing-style`](../../skills/ieeesp-writing-style/SKILL.md),
> [`ieeesp-topic-selection`](../../skills/ieeesp-topic-selection/SKILL.md), and
> [`ieeesp-experiments`](../../skills/ieeesp-experiments/SKILL.md).

# Worked Example: An IEEE S&P Abstract + Introduction (before → after)

This demonstrates the **first-round survival arc** from `ieeesp-writing-style`.
Because S&P cuts weak papers in the first round **without a rebuttal**
(`ieeesp-review-process`), the first two pages must answer, unaided:
**who is the adversary → what is the bounded claim → what evidence closes the
loop → why now / why hard → was it done responsibly.**

The framing also reflects `ieeesp-topic-selection`: S&P is strongest when a
**real adversary** and an **end-to-end demonstration** are the contribution —
here, a practical side channel against a deployed service, not a
speed-up of an existing system (which would route to a systems venue).

**Illustrative paper (fictional):** *"Peeking Through the Cache: A Practical
Timing Side Channel in a Shared Serverless Platform."* Fictional attack: a
co-resident function recovers another tenant's request patterns via a shared
cache timing channel.

---

## Before (buries the adversary and overclaims — typical first draft)

> **Abstract.** Serverless computing has become enormously popular. Security
> and privacy are important concerns in cloud environments. In this work we
> study cache side channels, which are a significant threat. We propose a new
> attack that exploits timing differences and show it works well on a cloud
> platform, achieving high accuracy and outperforming prior attacks. Our
> results have devastating implications for cloud security.
>
> **Introduction.** Cloud computing has transformed how applications are
> deployed. Side-channel attacks have been studied for many years, including
> cache attacks, timing attacks, and power attacks. In this paper, we present
> a new cache-based attack. We evaluate it on a real platform and show it is
> effective. Section 2 reviews related work, Section 3 describes our attack,
> Section 4 presents the evaluation, and Section 5 concludes.

**What's wrong (against `ieeesp-writing-style` / `ieeesp-topic-selection` /
`ieeesp-experiments`):**

- **No threat model on page 1** — who the attacker is, what access they have
  (co-resident? same host? same cache?), and what they win is never stated.
  A first-round reviewer cannot tell if the attack is interesting or assumes
  capabilities that make it trivial.
- **Overclaims** ("works well," "high accuracy," "devastating") with no
  boundary, no n, and no dispersion — the exact language `ieeesp-experiments`
  flags.
- **No evidence map** — which section *demonstrates* end to end vs *measures*
  is invisible; "outperforming prior attacks" names no baseline.
- **No adaptive-adversary or realism framing** — is the platform's existing
  isolation defeated, and does the attack survive normal noise?
- **No ethics signal** — a cross-tenant attack on a real platform raises
  immediate disclosure and authorization questions the paper ignores.
- **Over-signposted roadmap** substituting for an argument.

---

## After (S&P arc — adversary → bounded claim → evidence → why hard → ethics)

> **Abstract.** Serverless platforms co-locate functions from mutually
> distrusting tenants on shared hosts, isolating them with per-function
> sandboxes but a **shared last-level cache**. We show that a co-resident
> attacker function, with **no privileges beyond running its own code on the
> same host**, can recover a victim function's **request-arrival pattern** by
> timing cache contention — defeating the platform's tenant-isolation claim
> without breaking the sandbox. We demonstrate the attack end to end against a
> representative open-source serverless stack, recovering arrival patterns at
> a measured **true-positive rate of 0.9X (± dispersion over 50 trials, §5)**
> under production-like noise, and we evaluate the platform's existing
> rate-limiting and cache-partitioning mitigations as an **adaptive**
> defender. We disclosed the issue to the affected maintainers (§8). *(threat
> model → bounded claim → end-to-end evidence with n → adaptive eval →
> disclosure — all on the first page.)*
>
> **Introduction.** *(¶1 — adversary + bounded claim, first breath.)* Consider
> an attacker who can deploy an ordinary function to a shared serverless host
> — **no elevated privileges, no sandbox escape, no physical access** — and
> whose only goal is to learn *when* a co-resident victim function is invoked.
> We show this weak attacker can recover the victim's request-arrival pattern
> through a **shared-cache timing channel**, contradicting the platform's
> stated tenant-isolation property.
>
> *(¶2 — why now / why hard.)* This is not a textbook cache attack.
> Serverless functions are **short-lived**, **co-location is not
> attacker-controlled**, and the platform injects scheduling noise — the
> conditions under which prior cross-core cache attacks were demonstrated do
> **not** hold. The contribution is showing the channel survives *these*
> conditions, and characterizing when it does not.
>
> *(¶3 — evidence map, each claim paired.)* We demonstrate the attack end to
> end on a representative open-source stack (§4), report the true-positive
> rate and its dispersion over 50 trials against a production-like noise model
> (§5, Table 2), and — because a defense claim is only as strong as the
> adversary it faces — evaluate the platform's rate-limiting and
> cache-partitioning options against an **adaptive** attacker who knows they
> are deployed (§6). Baselines are the strongest prior co-resident timing
> attacks at their best configuration (§5.2). *(each claim → a section, a
> table, a baseline.)*
>
> *(¶4 — scope and non-goals, stated not hidden.)* Our attacker **cannot**
> read victim memory contents and **cannot** force co-location; we assume
> co-residency is achieved with the known techniques we cite, and we scope the
> claim to **arrival-pattern leakage**, not payload recovery. *(the threat
> model's boundary is explicit, per the rule that reviewers probe unstated
> limits.)*
>
> *(¶5 — ethics + why it matters + roadmap.)* We evaluated only functions we
> deployed ourselves on our own tenant accounts, never against other tenants'
> workloads, and we disclosed to the stack's maintainers on <date>, who are
> developing a mitigation (§8, IRB determined not human-subjects research).
> The result matters because arrival-pattern leakage alone enables traffic
> analysis of confidential workloads. Section 3 states the threat model in
> full; Section 4 the attack; Sections 5–6 the evaluation and adaptive
> defenses. *(ethics is a record of actions, not a disclaimer; brief roadmap.)*

---

## Why the "after" survives S&P's first round

Mapped to the skill checklists:

- **Adversary on page 1** — capabilities *and* non-capabilities are stated in
  ¶1 and ¶4, so a first-round reviewer can judge the attack's interest
  immediately (`ieeesp-writing-style` page-2 test).
- **Claim bounded** — "recover request-arrival pattern," not "break serverless
  security"; scoped to what §5 measures (`ieeesp-writing-style` claim
  calibration).
- **Evidence loop closed for an attack** — an end-to-end demonstration against
  a realistic target, with n and dispersion, and the strongest baseline
  (`ieeesp-experiments`).
- **Adaptive defender evaluated** — mitigations are tested against an attacker
  who knows them, pre-empting the top S&P defense-paper rejection
  (`ieeesp-experiments`).
- **Ethics is a record** — self-owned targets, dated disclosure, IRB
  determination, stated on the first page, not deferred
  (`ieeesp-review-process` / REC).
- **Right venue** — the contribution is a *realistic adversary and a
  demonstrated leak*, a strong S&P fit rather than a systems re-route
  (`ieeesp-topic-selection`).
- **13-page discipline** — the full noise model, per-trial breakdowns, and
  co-location details go to a clearly-marked appendix while the body stays
  self-contained (`ieeesp-supplementary`: nothing the acceptance case needs
  lives only in the appendix reviewers need not read).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real,
> web-verified S&P papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for S&P-specific
> submission and ethics policy.
