# ACM IMC Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **ACM Digital Library** (and, where noted, the IMC program/awards pages) to
> confirm it appeared at the **ACM Internet Measurement Conference (IMC)** — matching title,
> author list, year, and venue string. Papers that could not be cleanly confirmed as IMC (as
> opposed to SIGCOMM, NSDI, CoNEXT, PAM, USENIX Security, or a journal) were **omitted and
> documented below**. It is deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** IMC is **not** SIGCOMM, **not** NSDI, **not** CoNEXT, **not** PAM,
> and **not** a security venue. Many canonical measurement-flavored tools were introduced at those
> venues instead (ZMap and Censys at USENIX Security/CCS; much systems work at SIGCOMM/NSDI). A
> famous author or a familiar dataset name does **not** prove IMC. Each row was checked to be an
> IMC edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, numbers, or tables — read the original on ACM DL before citing
> anything. For IMC-specific policy, scope, and the cycle model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
poses a **question about the real Internet practitioners recognize**, backs it with **measurement
evidence from credible vantage points**, and names its **limitations and ethics** — the IMC bar
(see [`../../skills/imc-writing-style/SKILL.md`](../../skills/imc-writing-style/SKILL.md),
[`../../skills/imc-topic-selection/SKILL.md`](../../skills/imc-topic-selection/SKILL.md), and
[`../../skills/imc-experiments/SKILL.md`](../../skills/imc-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "IMC-shaped."

Several rows are IMC **award winners**, so they also model what an outstanding measurement
contribution and a community-grade dataset look like at this venue.

---

## By contribution shape

### Internet-wide scanning + ecosystem measurement — security-critical infrastructure

- **Durumeric, Kasten, Bailey & Halderman, "Analysis of the HTTPS Certificate Ecosystem," IMC
  2013** (DOI 10.1145/2504730.2504755). Verified: ACM DL / dblp. A large-scale study of the Web
  PKI built from repeated Internet-wide scans over many months.
  - **Why it is an exemplar:** it turns an opaque, security-critical piece of the real Internet
    (who can issue certificates for any site) into a **measured, temporally fine-grained** map,
    and derives concrete lessons for operators. The contribution is *what the measurement revealed
    about deployed infrastructure*, not a new protocol.
  - **Self-check:** does your scan measure a phenomenon operators care about, over enough time and
    coverage that the finding is about the ecosystem rather than a snapshot artifact?

### Active measurement — deployed-protocol vulnerability at scale

- **Luckie, Beverly, Wu, Allman & claffy, "Resilience of Deployed TCP to Blind Off-Path Attacks,"
  IMC 2015.** Verified: dblp / ACM DL; **IMC 2015 Best Paper**. Actively probed real webservers,
  operating systems, and middleboxes to quantify susceptibility to in-window blind attacks.
  - **Why it is an exemplar:** it measures a property of **deployed** systems in the wild — not a
    lab implementation — and reports it with the vantage-point and dating discipline IMC prizes,
    while treating the active-measurement ethics seriously.
  - **Self-check:** are your subjects real deployed systems (not your own testbed), and is your
    active measurement designed to be safe, dated, and reproducible in method if not in identical
    data?

### Longitudinal empirical study — email security in the wild

- **Durumeric, Adrian, Mirian, Kasten, Bursztein, Lidzborski, Thomas, Eranti & Bailey, "Neither
  Snow Nor Rain Nor MITM: An Empirical Analysis of Email Delivery Security," IMC 2015.** Verified:
  dblp / ACM DL. Combined vantage points (including a large mail provider) to measure how well
  email is protected in transit.
  - **Why it is an exemplar:** it characterizes a real, widely used protocol's *deployed security*
    from privileged vantage points, quantifying gaps operators can act on — pure measurement
    insight into how the Internet actually behaves.
  - **Self-check:** does your study change what the community believes about real deployed
    practice, from vantage points a reviewer would accept as representative?

### Methodology / instrument validity — questioning a research input

- **Scheitle, Hohlfeld, Gamba, Jelten, Zimmermann, Strowes & Vallina-Rodriguez, "A Long Way to the
  Top: Significance, Structure, and Stability of Internet Top Lists," IMC 2018, pp. 478-493.**
  Verified: dblp `rec/conf/imc/ScheitleHGJZSV18`; IMC 2018 award winner. Interrogates the top-list
  inputs (Alexa and peers) that countless measurement studies depend on.
  - **Why it is an exemplar:** it audits a **measurement instrument the field relies on** and shows
    how its instability biases downstream results — improving how *everyone else* measures, a
    distinctly prized IMC mode (compare the "are mutants valid?" role at SE venues).
  - **Self-check:** does your paper strengthen or question a widely used measurement input or
    methodology, with an analysis whose stability and confounds are laid out explicitly?

### Dataset + framework — macroscopic ecosystem characterization (community contribution)

- **Jonker, King, Krupp, Rossow, Sperotto & Dainotti, "Millions of Targets Under Attack: A
  Macroscopic Characterization of the DoS Ecosystem," IMC 2017.** Verified: dblp
  `rec/conf/imc/JonkerKKRSD17`; ACM DL. Fuses four independent global measurement infrastructures
  (a network telescope, amplification honeypots, and DNS-based platforms) into a two-year view of
  DoS attacks and protection-service adoption.
  - **Why it is an exemplar:** it builds a **cross-infrastructure dataset and framework** that
    others can reuse — exactly the shape the **Community Contribution Award** exists to honor — and
    reasons carefully about each vantage point's coverage and bias.
  - **Self-check:** does your paper contribute a reusable dataset or platform, with honest per-
    source coverage/limitation analysis, that the community could build on?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified IMC exemplar | Edition | Method |
| --- | --- | --- | --- |
| Internet-wide scan + ecosystem | Durumeric et al., "HTTPS Certificate Ecosystem" | IMC 2013 | Repeated scanning |
| Active measurement | Luckie et al., "Resilience of Deployed TCP..." | IMC 2015 (Best Paper) | Active probing |
| Longitudinal empirical study | Durumeric et al., "Neither Snow Nor Rain Nor MITM" | IMC 2015 | Vantage-point analysis |
| Methodology / instrument validity | Scheitle et al., "A Long Way to the Top" | IMC 2018 (award) | Top-list audit |
| Dataset + framework | Jonker et al., "Millions of Targets Under Attack" | IMC 2017 | Cross-infrastructure fusion |

> Five verified papers across five contribution shapes. The two 2015 rows also show IMC's twin
> empirical modes — *actively probing* deployed systems and *analyzing* privileged vantage-point
> data — both prized here.

---

## Omitted for lack of clean IMC verification (do not attribute to IMC without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **ZMap ("Fast Internet-Wide Scanning and its Security Applications," Durumeric, Wustrow &
  Halderman)** — verified to be **USENIX Security 2013**, *not* IMC, despite being the scanning
  tool behind many IMC studies. A direct sibling-venue trap; listed only as a guardrail.
- **Censys ("A Search Engine Backed by Internet-Wide Scanning")** — **ACM CCS 2015**, not IMC.
  Omitted.
- **"Understanding the Mirai Botnet" (Antonakakis et al.)** — **USENIX Security 2017**, not IMC,
  despite being a landmark measurement of a botnet. Omitted to avoid venue misattribution.
- **Much foundational CDN/DNS/BGP systems work** — frequently lands at **SIGCOMM, NSDI, or PAM**;
  a measurement flavor does not make it IMC. Confirm the venue string before attributing.

Before adding any paper, confirm it on **dblp** and **ACM DL** by matching the venue string to an
IMC edition (not SIGCOMM, NSDI, CoNEXT, PAM, USENIX Security, or a journal), then record authors,
year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
