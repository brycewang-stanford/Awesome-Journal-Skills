# ITCS Exemplars Library (conceptual-contribution shape)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked across at
> least two surfaces (dblp `conf/innovations`, LIPIcs/DROPS ITCS volumes, and/or the ICS/ITCS
> proceedings) to confirm it appeared at **ITCS / ICS — Innovations in (Theoretical) Computer
> Science** — matching title, authors, year, and venue string. Papers that could not be cleanly
> confirmed as ITCS (as opposed to STOC, FOCS, SODA, CCC, TCC, or a journal) were **omitted and
> documented below**. It is deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** ITCS is **not** STOC, **not** FOCS, **not** SODA, **not** CCC,
> **not** TCC. Many landmark theory results were introduced at those venues instead; a famous
> author or a familiar concept does **not** prove ITCS. Each row was checked to be an ITCS/ICS
> edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does
> not reproduce or invent theorems, bounds, or proofs — read the original on DROPS/dblp before
> citing anything. For ITCS-specific policy, scope, and the conceptual-novelty ethos, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **conceptual-contribution shape** is closest to yours, then study how that
paper makes a reader feel a **new question, model, or connection is worth having** — the ITCS
bar (see [`../../skills/itcs-writing-style/SKILL.md`](../../skills/itcs-writing-style/SKILL.md),
[`../../skills/itcs-topic-selection/SKILL.md`](../../skills/itcs-topic-selection/SKILL.md), and
[`../../skills/itcs-related-work/SKILL.md`](../../skills/itcs-related-work/SKILL.md)). For each,
ask the self-check question before claiming your paper is "ITCS-shaped." Note the recurring
pattern: the *theorems* in these papers are often not the hardest of their year — the **idea**
is the contribution, and the venue selected on that.

---

## By conceptual-contribution shape

### A new model / definition

- **Dziembowski, Pietrzak & Wichs, "Non-Malleable Codes," ICS 2010** (1st edition, the founding
  ICS/ITCS). Verified: widely cited as "introduced by Dziembowski, Pietrzak and Wichs (ICS
  2010)"; ICS/ITCS proceedings.
  - **Why it is an exemplar:** it **defines a new object** — a code whose tampered decoding is
    either the original message or something *unrelated* to it — where classical error-correction
    is impossible. The paper's value is the definition and the model of tampering families, not a
    single hard theorem; an entire subfield followed.
  - **Self-check:** does your paper give the community a *new definition* it did not have, with a
    model general enough that others will build on it?

### A new algorithmic notion

- **Goldreich, Goldwasser & Ron, "On the possibilities and limitations of pseudodeterministic
  algorithms," ITCS 2013, pp. 127-138** (Berkeley). Verified: ITCS '13 proceedings; dblp.
  - **Why it is an exemplar:** it takes the notion of a **pseudodeterministic** (probabilistic
    but canonical-output) algorithm and asks what it can and cannot do — a *reframing* of what
    "solving" a search problem means. The contribution is the lens, which reorganizes questions
    people already cared about.
  - **Self-check:** does your paper introduce a *new way of asking* about a familiar object, such
    that old questions look different through it?

### A new object / construction (quantum)

- **Farhi, Gosset, Hassidim, Lutomirski & Shor, "Quantum money from knots," ITCS 2012.**
  Verified: "Proceedings of the 3rd Innovations in Theoretical Computer Science Conference,
  ITCS '12."
  - **Why it is an exemplar:** it proposes a **concrete new construction** for a bold model
    (publicly verifiable quantum money) by connecting it to knot invariants — an unexpected
    bridge between two areas. ITCS rewards exactly this "what if we connected X and Y" move.
  - **Self-check:** is your contribution a *surprising connection* that lets tools from one area
    attack a problem in another?

### A new model bridging fields

- **"Interactive Proofs for Verifying Machine Learning," ITCS 2021** (LIPIcs.ITCS.2021.41;
  author list reported — confirm on DROPS). Verified: LIPIcs/DROPS ITCS 2021 volume.
  - **Why it is an exemplar:** it imports the **interactive-proof** lens into **learning**,
    asking whether a verifier can check a learned hypothesis far cheaper than learning it — a new
    question at the seam of two mature areas. The novelty is the framing of the question.
  - **Self-check:** does your paper open a *seam between two established areas* that neither had
    posed on its own?

### A new model in a distributed setting

- **Fraigniaud, Le Gall, Nishimura & Paz, "distributed quantum Merlin-Arthur" (dQMA), ITCS
  2021.** Verified: cited as "introduced ... by Fraigniaud, Le Gall, Nishimura and Paz (ITCS
  2021)"; LIPIcs/DROPS ITCS 2021.
  - **Why it is an exemplar:** it **defines a new proof model** for networks (nodes verifying a
    global property with quantum proofs and local communication) and exhibits a separation that
    makes the model's power concrete. Model first, separation as evidence the model is alive.
  - **Self-check:** does your new model come with at least one crisp result (a separation, a
    surprising possibility, an impossibility) showing it is *not vacuous*?

---

## Conceptual-shape <-> exemplar (verified rows)

| Contribution shape | Verified ITCS/ICS exemplar | Edition |
| --- | --- | --- |
| New model / definition | Dziembowski, Pietrzak & Wichs, "Non-Malleable Codes" | ICS 2010 |
| New algorithmic notion | Goldreich, Goldwasser & Ron, "...pseudodeterministic algorithms" | ITCS 2013 |
| New object / construction | Farhi, Gosset, Hassidim, Lutomirski & Shor, "Quantum money from knots" | ITCS 2012 |
| New model bridging fields | "Interactive Proofs for Verifying Machine Learning" | ITCS 2021 |
| New model, distributed | Fraigniaud, Le Gall, Nishimura & Paz, dQMA | ITCS 2021 |

> Five verified papers across five conceptual shapes. In every one, the **idea** — a definition,
> a notion, a connection, a model — is the contribution the PC bought; the theorems serve the
> idea rather than the other way around. That inversion is the ITCS signature.

---

## Omitted for lack of clean ITCS verification (do not attribute to ITCS without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Rational Proofs" (Azar & Micali)** — verified to be **STOC 2012**, *not* ITCS, despite being
  a quintessentially "innovative" model (a rational prover). A direct sibling-venue trap; listed
  only as a guardrail. (ITCS 2014 has *follow-up* rational-proofs work — do not conflate the
  origin with the follow-up.)
- **"Delegating Computation: Interactive Proofs for Muggles" (Goldwasser, Kalai & Rothblum)** —
  **STOC 2008**, not ITCS. Omitted.
- **"Cryptographic Assumptions: A Position Paper" (Goldwasser & Kalai)** — an Innovations-*flavored*
  conceptual position paper, but it appeared at **TCC 2016**, not ITCS. Omitted to avoid venue
  misattribution.

Before adding any paper, confirm it on **dblp `conf/innovations`** and the **LIPIcs/DROPS ITCS**
volume (or the ICS/ITCS proceedings for 2010-2016) by matching the venue string to an ITCS/ICS
edition (not STOC, FOCS, SODA, CCC, or TCC), then record authors, year, and DOI/pages, and
update the access-date header. When in doubt, omit. If web search is unavailable, add the row as
**待核实 / TO VERIFY** with **no attribution**.
