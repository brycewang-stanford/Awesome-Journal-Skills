# USENIX Security Exemplars Library (topic × evidence shape)

> **Verified 2026-07-08.** Each row below is a USENIX Security paper whose title,
> authorship, and USENIX Security '24 (33rd Symposium) Distinguished Paper Award were
> confirmed through multiple independent institutional announcements and award listings
> cross-referenced on 2026-07-08. Direct fetches of usenix.org and dblp.org returned 403
> in the verification environment (see [`../official-source-map.md`](../official-source-map.md));
> attribution here rests on the cross-referenced award announcements, not a single source.
>
> **Sibling-venue trap:** USENIX Security, IEEE S&P, ACM CCS, and NDSS overlap heavily
> and papers of similar titles appear across them. Confirm the venue line ("USENIX
> Security Symposium") on the usenix.org presentation page before attributing a paper.
> A CVE or a Black Hat talk of the same name is not the academic paper.
>
> **Zero-hallucination rule:** this library provides design positioning only. It states
> no result numbers, no attack success rates, and no claim beyond what the award records
> establish. Read the paper on usenix.org before citing anything from it. If you add a
> row you cannot verify live, mark it 待核实 with no attribution.

---

## How to use this library

Find the row nearest your project's topic × evidence-shape cell, then study how that
paper makes an **auditable security contribution** — a reproducible attack, a
measured population, a defense with an adaptive-attacker evaluation — which is the fit
bar in
[`../../skills/usenixsec-topic-selection/SKILL.md`](../../skills/usenixsec-topic-selection/SKILL.md).
Pair each exemplar with the evidence discipline in
[`../../skills/usenixsec-experiments/SKILL.md`](../../skills/usenixsec-experiments/SKILL.md)
and the framing rules in
[`../../skills/usenixsec-writing-style/SKILL.md`](../../skills/usenixsec-writing-style/SKILL.md).
All five rows are USENIX Security '24 Distinguished Paper Award winners — a deliberate
choice: the award marks papers the committee itself held up as exemplary at this venue.

---

## Verified exemplars

### Protocol attack with concrete, disclosed impact

- **Bäumer, Brinkmann & Schwenk, "Terrapin Attack: Breaking SSH Channel Integrity By
  Sequence Number Manipulation," USENIX Security '24** (Distinguished Paper Award).
  - **Why an exemplar:** a precise cryptographic-protocol flaw in a ubiquitous protocol,
    demonstrated end-to-end and coordinated with implementers before publication. The
    contribution shape is "named attack + exact mechanism + real-world scope + responsible
    disclosure" — the template for offensive protocol work here.
  - **Self-check:** is your attack mechanism stated precisely enough that a reader could
    reproduce it, and is the disclosure timeline in the paper?

### Measurement study exposing socio-technical harm

- **Ablove, Chandrashekaran, Sundara Raman, Ramesh, Le, Oppenheimer & Ensafi, "Digital
  Discrimination of Users in Sanctioned States: The Case of the Cuba Embargo," USENIX
  Security '24** (Distinguished Paper Award).
  - **Why an exemplar:** internet measurement turned toward a policy-relevant harm, with
    the vantage-point and validity discipline this venue's measurement reviewers demand.
    The finding matters because the method is defensible across vantages and time.
  - **Self-check:** can you state where you measured from, when, and what your vantage
    cannot see — before stating the finding?

### Electronic-voting security with privacy impact

- **Crimmins, Narayanan & Halderman, "DVSorder: Ballot Randomization Flaws Threaten
  Voter Privacy," USENIX Security '24** (Distinguished Paper Award).
  - **Why an exemplar:** a real-system vulnerability with direct privacy consequences,
    handled with the disclosure and public-interest care the venue expects for
    consequential deployed systems.
  - **Self-check:** does the paper make the threat model and the affected population
    concrete, and document the responsible-handling steps?

### LLM security, evaluated as security

- **Yu & Zhang, "Don't Listen to Me: Understanding and Exploring Jailbreak Prompts of
  Large Language Models," USENIX Security '24** (Distinguished Paper Award).
  - **Why an exemplar:** an emerging-topic (LLM) paper that earns a security venue by
    treating jailbreaks as an attack surface with systematic measurement, not a demo.
    Shows how to bring a trend topic in without losing rigor.
  - **Self-check:** if your topic is fashionable, is the contribution a measured,
    reproducible security result rather than a curated set of examples?

### Web attack synthesis and evaluation

- **Kirchner, Möller, Musch, Klein, Rieck & Johns, "Dancer in the Dark: Synthesizing and
  Evaluating Polyglots for Blind Cross-Site Scripting," USENIX Security '24**
  (Distinguished Paper Award).
  - **Why an exemplar:** a software-security contribution centered on a technique
    (polyglot synthesis) with a systematic evaluation and a reusable artifact — the
    artifact-forward shape the Open Science era rewards.
  - **Self-check:** is your technique's evaluation systematic (a corpus, baselines) and
    is the artifact built to be reused?

---

## Topic × evidence-shape index

| Topic | Verified USENIX Security exemplar | Edition | Evidence shape |
| --- | --- | --- | --- |
| Cryptographic protocol attack | Bäumer, Brinkmann & Schwenk (Terrapin) | '24 | Named attack + disclosure |
| Internet measurement / harm | Ablove et al. (Cuba Embargo) | '24 | Multi-vantage measurement |
| Deployed-system vulnerability | Crimmins, Narayanan & Halderman (DVSorder) | '24 | Real-system flaw + privacy impact |
| LLM / emerging-topic security | Yu & Zhang (Jailbreak prompts) | '24 | Systematic attack-surface study |
| Web / software security | Kirchner et al. (Dancer in the Dark) | '24 | Technique synthesis + artifact |

Five verified rows across five distinct lanes. What the set demonstrates jointly: every
row makes a security contribution **another researcher could audit, reproduce, or
extend** — the pack's recurring theme and the reason the Open Science and artifact
machinery exists.

---

## Adding rows without hallucinating

1. Locate the paper on `usenix.org/conference/usenixsecurity<NN>/presentation/...` and
   confirm the venue line names the USENIX Security Symposium.
2. Prefer quoting title/authors from the usenix.org presentation page or the DBLP
   `conf/uss` record (both 403'd to automated fetch on 2026-07-08 — read via search
   rendering and cross-check a second source).
3. Do not attribute a paper from a CVE, advisory, or conference talk of the same name;
   those are not the academic publication.
4. Award status (Distinguished Paper, Internet Defense Prize, Test of Time) must trace
   to an official USENIX announcement or the awarding institution's notice.
5. When verification fails, omit the row or mark it 待核实 with no author attribution.
