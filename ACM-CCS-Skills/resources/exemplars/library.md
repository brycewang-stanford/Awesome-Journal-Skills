# ACM CCS Exemplars Library (topic × contribution type)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked against
> the **ACM Digital Library** and **dblp** to confirm it appeared at the **ACM Conference on
> Computer and Communications Security (CCS)** — matching venue, year, authors, and (where
> relevant) its **SIGSAC CCS Test-of-Time Award**. Papers that could not be cleanly confirmed
> as CCS (as opposed to a sibling security venue) were **omitted and documented below**. This
> is deliberately a short, verified list (6 verified > 15 guessed).
>
> **Sibling-confusion guard:** CCS is **not** IEEE S&P (Oakland), USENIX Security, or NDSS.
> Many landmark security papers live in those venues. Venue attribution was checked per row —
> a famous security result is not automatically a CCS paper. Each row below was confirmed to
> be a CCS edition specifically.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent results, numbers, or exploit details — read the original in the ACM
> DL before citing anything. For CCS-specific policy and the do-not-misattribute list, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × contribution type** is closest to yours, then study how that
paper puts a **precise threat model and a concrete security claim on the first page** with
**evidence paired to every claim** — the CCS bar (see
[`../../skills/ccs-writing-style/SKILL.md`](../../skills/ccs-writing-style/SKILL.md),
[`../../skills/ccs-topic-selection/SKILL.md`](../../skills/ccs-topic-selection/SKILL.md), and
[`../../skills/ccs-experiments/SKILL.md`](../../skills/ccs-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "CCS-shaped."

Several rows are **SIGSAC CCS Test-of-Time Award** winners — useful because the award marks
papers whose threat model and framing aged well, which is exactly what the writing-style and
topic-selection skills push toward.

---

## By contribution type

### New attack class / code reuse (Test-of-Time)

- **Shacham, "The Geometry of Innocent Flesh on the Bone: Return-into-libc without Function
  Calls (on the x86)," CCS 2007.** Verified: ACM DL `10.1145/1315245.1315313`; **CCS 2017
  Test-of-Time Award**.
  - **Why it is an exemplar:** gives the first general formulation of return-oriented
    programming — a reusable *attack primitive*, not one exploit, so the contribution is a
    whole class of attacks. A model of the CCS "attack that generalizes" paper.
  - **Self-check:** is your attack a reusable capability against a class of targets, with the
    attacker's assumptions stated precisely, rather than one brittle proof-of-concept?

### Defense with a stated guarantee (Test-of-Time)

- **Abadi, Budiu, Erlingsson & Ligatti, "Control-Flow Integrity," CCS 2005.** Verified:
  ACM DL `10.1145/1102120.1102165`; **CCS 2015 Test-of-Time Award**.
  - **Why it is an exemplar:** defines a defense (CFI) as an enforceable *property* with a
    threat model and an implementation, pairing the security argument with measured cost — the
    CCS defense arc that `ccs-experiments` pushes toward.
  - **Self-check:** can your defense be stated as a property an adversary must violate, and did
    you measure both its security against adaptation and its overhead?

### Applied cryptography breaking real deployments

- **Adrian, Bhargavan, Durumeric, Gaudry, Green, Halderman et al., "Imperfect Forward
  Secrecy: How Diffie-Hellman Fails in Practice," CCS 2015.** Verified: ACM DL
  `10.1145/2810103.2813707`; dblp `conf/ccs/AdrianBDGGHHSTV15`.
  - **Why it is an exemplar:** connects cryptographic weakness to *deployed* protocol behavior
    with Internet-scale measurement, so the contribution is both an attack (Logjam) and an
    ecosystem finding — the CCS blend of crypto and measurement.
  - **Self-check:** does your cryptographic result show impact on real deployments with
    measured prevalence, not only an abstract weakness?

### Privacy / machine learning at the security venue

- **Abadi, Chu, Goodfellow, McMahan, Mironov, Talwar & Zhang, "Deep Learning with
  Differential Privacy," CCS 2016.** Verified: ACM DL `10.1145/2976749.2978318`; dblp
  `conf/ccs/AbadiCGMMT016`.
  - **Why it is an exemplar:** brings a formal privacy guarantee (a differential-privacy
    accountant) to deep learning with measured utility cost — a privacy *mechanism* with a
    provable property, positioned for the security community rather than an ML venue.
  - **Self-check:** does your privacy contribution carry a formal guarantee and a measured
    cost, framed for a security PC rather than as an ML systems win?

### Oblivious memory / systems security (Test-of-Time)

- **Stefanov, van Dijk, Shi, Fletcher, Ren, Yu & Devadas, "Path ORAM: An Extremely Simple
  Oblivious RAM Protocol," CCS 2013.** Verified: ACM DL `10.1145/2508859.2516660`; **CCS 2023
  Test-of-Time Award**.
  - **Why it is an exemplar:** offers a construction whose contribution is *simplicity plus a
    proven bound* — the practicality that made ORAM deployable, with the security property
    stated and analyzed. Pairs with `ccs-writing-style`'s claim-to-proof discipline.
  - **Self-check:** is your construction the simplest one that still carries the security
    property, with the bound proved rather than asserted?

### Real-world platform security (Test-of-Time)

- **Felt, Chin, Hanna, Song & Wagner, "Android Permissions Demystified," CCS 2011.** Verified:
  ACM DL `10.1145/2046707.2046779`; **CCS 2022 Test-of-Time Award**.
  - **Why it is an exemplar:** an empirical study of how a deployed permission system is
    actually (mis)used, with a tool and a dataset — a measurement contribution that reframed a
    platform-security problem. Pairs with `ccs-experiments`' validated-measurement bar.
  - **Self-check:** does your measurement validate its methodology and overturn or sharpen a
    widely held assumption, rather than merely counting things?

---

## By topic (each cell is a verified CCS paper above)

| Topic | Verified CCS exemplar | Year / contribution type | Award |
| --- | --- | --- | --- |
| Code-reuse attacks | Shacham, "Geometry of Innocent Flesh on the Bone" | 2007 / attack primitive | ToT 2017 |
| Control-flow defense | Abadi et al., "Control-Flow Integrity" | 2005 / defense with property | ToT 2015 |
| Applied crypto + measurement | Adrian et al., "Imperfect Forward Secrecy" (Logjam) | 2015 / attack + ecosystem | — |
| Privacy-preserving ML | Abadi et al., "Deep Learning with Differential Privacy" | 2016 / privacy mechanism | — |
| Oblivious RAM / systems | Stefanov et al., "Path ORAM" | 2013 / construction + proof | ToT 2023 |
| Platform security | Felt et al., "Android Permissions Demystified" | 2011 / validated measurement | ToT 2022 |

> Six verified papers across six contribution types. Four are SIGSAC CCS Test-of-Time
> winners, which is why they double as models of durable threat-model framing.

---

## Omitted for lack of clean CCS verification (do not attribute to CCS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several
are exactly the sibling-venue confusions the header warns about:

- **Spectre / Meltdown (2018)** — the canonical transient-execution papers appeared at
  **IEEE S&P** and **USENIX Security**, **not CCS**. Omitted as a guardrail.
- **"Robust De-anonymization of Large Sparse Datasets" (Narayanan & Shmatikov, 2008)** —
  an **IEEE S&P** paper, **not CCS**. Omitted.
- **"The Matter of Heartbleed" (Durumeric et al., 2014)** — appeared at **IMC**, **not CCS**.
  Omitted despite being by overlapping authors of a CCS paper above.
- **Any paper known only from arXiv or a vendor advisory** — a preprint or CVE is not a CCS
  placement. Confirm the ACM DL CCS proceedings entry before attributing.

Before adding any new paper, confirm it in the **ACM Digital Library CCS proceedings** (the
proceedings landing page names "ACM SIGSAC Conference on Computer and Communications
Security"), match the year and author list, and update the access-date header. When in doubt,
omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
