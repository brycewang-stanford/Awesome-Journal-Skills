# ICSE Exemplars Library (contribution shape × decade)

> **Verified 2026-07-08.** Every row below was confirmed against archival
> records — ACM Digital Library or IEEE Xplore entries, dblp keys — and, where
> an award is claimed, against the SIGSOFT/ICSE award pages or a university
> press announcement naming the award. Titles, authors, venues, and award
> facts are quoted from those records; nothing else is asserted.
>
> **Companion-volume trap:** an "ICSE" hit in a digital library may live in
> the companion proceedings (NIER, SEIP, Demonstrations, workshops), which
> are different review bars. Check that the record names the main research/
> technical track proceedings before using a paper as a research-track
> exemplar.
>
> **Zero-hallucination rule:** this library is for positioning only. It
> quotes no result numbers and no findings beyond what titles and award
> citations state. Read the paper before citing its content. If you add a row
> you cannot verify live, mark it 待核实 with no attribution.

---

## How to use this library

Three of the five exemplars carry the **Most Influential Paper** award — given
at each ICSE to the paper from ten years prior judged most influential on SE
theory or practice — which makes them unusually informative: the community
itself certified, with a decade of hindsight, that these are what ICSE papers
are for. Find the row nearest your contribution shape, then study how the
paper couples its idea to empirical evidence; pair with the fit test in
[`../../skills/icse-topic-selection/SKILL.md`](../../skills/icse-topic-selection/SKILL.md)
and the evidence ladder in
[`../../skills/icse-experiments/SKILL.md`](../../skills/icse-experiments/SKILL.md).

---

## Verified exemplars

### Technique + evaluation, field-founding

- **Weimer, Nguyen, Le Goues & Forrest, "Automatically Finding Patches Using
  Genetic Programming," ICSE 2009** — ICSE 2019 Most Influential Paper
  (award confirmed via SIGSOFT/ICSE award lineage and CMU/UNL announcements).
  - **Why an exemplar:** the automated-program-repair founding shape — a
    generate-and-validate technique on real defects — that a decade later had
    seeded an entire subfield and industrial tooling. The MIP citation is the
    community defining "impact on practice."
  - **Self-check:** if your technique works, what research area or practice
    changes? If the answer is only "our numbers beat baselines," the
    relevance criterion is unprotected.

### Empirical insight that rewired a research agenda

- **Hindle, Barr, Su, Gabel & Devanbu, "On the Naturalness of Software,"
  ICSE 2012** — ICSE 2022 Most Influential Paper (award confirmed via the
  UC Davis announcement and the ICSE 2022 MIP talk record).
  - **Why an exemplar:** an empirical claim — code is repetitive enough for
    statistical language models — evidenced with corpus studies, that became
    the intellectual charter for today's ML-on-code work. Proof that a
    *measurement* paper can outrank technique papers in long-run influence.
  - **Self-check:** does your study change what the community believes, or
    only add a data point to what it already believed?

### Negative/corrective empirical result

- **Inozemtseva & Holmes, "Coverage Is Not Strongly Correlated with Test
  Suite Effectiveness," ICSE 2014** — ICSE 2024 Most Influential Paper
  (award confirmed via the UBC announcement).
  - **Why an exemplar:** a debunking study aimed at a metric the whole field
    leaned on. ICSE rewards well-designed results that *complicate* accepted
    practice — provided the design (subjects, suite generation, effectiveness
    measures) survives the same rigor bar it turns on others.
  - **Self-check:** is your corrective claim evidenced across enough subjects
    and operationalizations that it cannot be dismissed as one setup's quirk?

### Qualitative / human-factors study

- **Li, Ko & Zhu, "What Makes a Great Software Engineer?", ICSE 2015**
  (dblp `conf/icse/LiKZ15`; ACM DL record in the ICSE 2015 proceedings).
  - **Why an exemplar:** interview-based qualitative research — 59 engineers
    at one company, per the paper's own record — carried into the flagship
    track by methodological transparency: sampling, protocol, and analysis
    documented to empirical-SE standards.
  - **Self-check:** could a methods-focused reviewer reconstruct your
    qualitative pipeline (sampling → instrument → codebook → agreement) from
    the paper plus package alone?

### AI-era technique with SE evaluation discipline

- **Fan, Gao, Mirchev, Roychoudhury & Tan, "Automated Repair of Programs from
  Large Language Models," ICSE 2023** (DOI `10.1109/ICSE48619.2023.00128`,
  ACM DL / IEEE Xplore).
  - **Why an exemplar:** an early flagship-track treatment of LLM-generated
    code as an SE object of study — applying the repair community's
    evaluation machinery to model output rather than marveling at the model.
    The template for making "SE for AI" pass the deletion test in
    `icse-topic-selection`.
  - **Self-check:** if the underlying model were swapped, would your research
    question and evaluation design still make sense? They should.

---

## Contribution-shape index

| Shape | Exemplar | Edition | Decade-later verdict |
|---|---|---|---|
| New technique + empirical evaluation | Weimer et al. | ICSE 2009 (31st) | MIP at ICSE 2019 |
| Corpus-driven empirical insight | Hindle et al. | ICSE 2012 (34th) | MIP at ICSE 2022 |
| Corrective/negative result | Inozemtseva & Holmes | ICSE 2014 (36th) | MIP at ICSE 2024 |
| Qualitative human-factors study | Li, Ko & Zhu | ICSE 2015 (37th) | Standard methods citation |
| LLM-era technique study | Fan et al. | ICSE 2023 (45th) | Recent; lineage forming |

Note what the set shows jointly: every shape couples a claim to evidence an
empiricist can audit — the pack's recurring theme — and three of five earned
their status precisely by changing what practitioners or researchers do.

---

## Adding rows without hallucinating

1. Find the archival record (ACM DL or IEEE Xplore) and confirm the
   proceedings line names the main technical/research track, not a companion
   volume.
2. Cross-check the dblp entry; quote title/authors/year from it.
3. For award claims, require a second source: the SIGSOFT/ICSE award pages or
   an institutional announcement naming paper, authors, and award year.
4. Record the edition number (ICSE 2027 = 49th) to catch year-arithmetic
   errors.
5. If any step fails, omit the row or mark it 待核实 with no attribution.
