# IEEE S&P Exemplars Library (contribution-type × topic)

> **Verified via web search, access date 2026-07-08.** Every paper below was
> checked against **dblp's `conf/sp` stream** and, where possible, **IEEE
> Xplore**, to confirm it actually appeared at the **IEEE Symposium on
> Security and Privacy (S&P / "Oakland")** — matching title, authors, year,
> and page range — as opposed to a sibling venue (USENIX Security, CCS, NDSS,
> EuroS&P, or a co-located SPW workshop). Papers that could not be cleanly
> confirmed as **main-conference S&P** were omitted and documented below.
> It is deliberately a short, verified list (6 verified > 20 guessed).
>
> **Sibling-confusion guard:** S&P is **not** USENIX Security, CCS, NDSS, or
> EuroS&P. Many famous security papers live in those venues; a "SP" string in
> a citation can also mean the **EuroS&P** or a workshop proceedings. Each row
> below was checked to be the main IEEE S&P specifically.
>
> **Use principle (zero hallucination):** this file gives **design
> positioning only**. It does not reproduce or invent results, attack success
> rates, or table numbers — read the original before citing anything. For
> S&P-specific policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution type × topic** is closest to yours, then
study how that paper (a) states its adversary on the first page, (b) closes
the evidence loop appropriate to its type — end-to-end demo for an attack,
adaptive evaluation for a defense, sampling+validity for a measurement,
taxonomy for an SoK — and (c) scopes its claim to what it demonstrates. That
is the S&P bar (see
[`../../skills/ieeesp-writing-style/SKILL.md`](../../skills/ieeesp-writing-style/SKILL.md),
[`../../skills/ieeesp-topic-selection/SKILL.md`](../../skills/ieeesp-topic-selection/SKILL.md),
and [`../../skills/ieeesp-experiments/SKILL.md`](../../skills/ieeesp-experiments/SKILL.md)).
Ask the self-check question before claiming your paper is "Oakland-shaped."

---

## By contribution type

### Attack — adversarial machine learning

- **Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks,"
  IEEE S&P 2017, pp. 39–57.** Verified: dblp `conf/sp/Carlini017`; IEEE Xplore
  DOI 10.1109/SP.2017.49.
  - **Why an exemplar:** defines a threat model precisely, then builds attacks
    for all three norms and shows a proposed defense (defensive distillation)
    fails against an *adaptive* attacker — the canonical S&P move of breaking
    a defense on its own terms rather than a weak one.
  - **Self-check:** does your attack target the strongest form of the defense,
    with an adversary that knows it exists?

### Attack — privacy of ML models

- **Shokri, Stronati, Song & Shmatikov, "Membership Inference Attacks Against
  Machine Learning Models," IEEE S&P 2017, pp. 3–18.** Verified: dblp
  `conf/sp/ShokriSSS17`; DOI 10.1109/SP.2017.41.
  - **Why an exemplar:** a crisp black-box threat model (a data record + query
    access) and an end-to-end demonstration against *commercial* MLaaS
    providers — a realistic target, not a toy, which is what makes the privacy
    claim land.
  - **Self-check:** is your privacy adversary's access realistic, and is the
    leakage shown against a system someone actually deploys?

### Attack — hardware / microarchitecture

- **Kocher et al., "Spectre Attacks: Exploiting Speculative Execution," IEEE
  S&P 2019, pp. 1–19.** Verified: dblp `conf/sp/Kocher0HFGGHHL19`.
  - **Why an exemplar:** an existence proof against real CPUs with a clearly
    stated attacker model (co-resident code reading victim memory), the kind
    of hardware-pinned result whose reproducibility depends on exact silicon
    (`ieeesp-reproducibility`).
  - **Self-check:** is your microarchitectural result pinned to specific
    hardware/microcode, with expected drift stated?

### Attack — networked systems / cryptocurrency

- **Apostolaki, Zohar & Vanbever, "Hijacking Bitcoin: Routing Attacks on
  Cryptocurrencies," IEEE S&P 2017, pp. 375–392.** Verified: dblp
  `conf/sp/ApostolakiZV17`; DOI 10.1109/SP.2017.29.
  - **Why an exemplar:** grounds the adversary in the real BGP routing
    infrastructure and quantifies impact (how few prefixes/ASes suffice) — a
    measurement-backed attack whose realism is the contribution.
  - **Self-check:** is your network adversary anchored in how the real
    infrastructure behaves, with quantified reach?

### SoK — systematization

- **Szekeres, Payer, Wei & Song, "SoK: Eternal War in Memory," IEEE S&P 2013,
  pp. 48–62.** Verified: dblp `conf/sp/SzekeresPWS13`; IEEE Xplore doc 6547101.
  - **Why an exemplar:** a model of the `SoK:` lane — builds one general model
    of memory-corruption attacks, maps which policies stop which attacks, and
    exposes weaknesses of deployed defenses. The taxonomy *is* the evidence.
  - **Self-check:** does your SoK impose a single framework that reconciles or
    invalidates prior work, rather than listing it?

---

## By contribution type × topic (each cell is a verified S&P paper above)

| Contribution | Topic | Verified S&P exemplar | Year / pages |
| --- | --- | --- | --- |
| Attack | Adversarial ML | Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks" | 2017 / 39–57 |
| Attack | ML privacy | Shokri et al., "Membership Inference Attacks Against ML Models" | 2017 / 3–18 |
| Attack | Microarchitecture | Kocher et al., "Spectre Attacks" | 2019 / 1–19 |
| Attack | Network / crypto | Apostolaki et al., "Hijacking Bitcoin" | 2017 / 375–392 |
| SoK | Memory safety | Szekeres et al., "SoK: Eternal War in Memory" | 2013 / 48–62 |

> Five verified papers across attack and SoK lanes. The Carlini–Wagner and
> Shokri lines also show a **research trajectory** — adversarial robustness
> and ML-privacy attacks that later spawned whole subfields — useful when
> positioning an incremental-but-principled security contribution.

---

## Omitted for lack of clean main-conference S&P verification

To keep the list zero-hallucination, the following were **excluded** after
checking — several are exactly the sibling-venue confusions the header warns
about:

- **Many canonical systems-security papers** (e.g., foundational USENIX
  Security and CCS attacks) — omitted because their home venue is not S&P; a
  "security flagship" is not interchangeable with "Oakland."
- **EuroS&P papers** — the IEEE *European* S&P is a distinct venue with its
  own dblp stream (`conf/eurosp`); do not attribute EuroS&P work to S&P.
- **SPW / workshop papers** co-located with S&P — the Security and Privacy
  Workshops publish separately and must not be cited as main-conference S&P.
- **A defense paper** is deliberately not force-fit here: pick your own recent
  S&P defense exemplar and verify it, since defense norms (adaptive-adversary
  evaluation) evolve fastest.

Before adding any new paper, confirm it on **dblp `conf/sp`** (the volume
landing names "IEEE Symposium on Security and Privacy") and cross-check pages
and DOI on **IEEE Xplore**, then record authors, year, and pages and update
the access-date header. When in doubt, omit. If web search is unavailable,
add the row as **待核实 / TO VERIFY** with **no attribution**.
