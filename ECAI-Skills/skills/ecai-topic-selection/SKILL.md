---
name: ecai-topic-selection
description: Use before writing to decide whether a project belongs at ECAI versus IJCAI, AAAI, AAMAS, KR, or a pure-ML venue, and whether it should go to the ECAI main track or the co-located PAIS applications track — using contribution shape, the model-swap test, the European/general-AI fit, and the calendar (including the joint IJCAI-ECAI 2026 cycle).
---

# ECAI Topic Selection

Routing is the highest-leverage decision, made **before** writing. ECAI is EurAI's **general-AI**
flagship — broad by design, spanning symbolic reasoning, KR, planning, search, multi-agent systems,
ML, and applications. That breadth is a feature and a trap: many projects *could* go to ECAI, so the
real question is whether ECAI is the **best-matched** home for your contribution and calendar, and
whether it belongs in the **main track** or the co-located **PAIS** applications track.

## Is it ECAI-shaped?

ECAI wants a contribution a **general AI audience** recognizes as advancing how systems reason,
plan, learn, or decide — with evidence proportional to the claim (a proof, or a fair comparison).
Apply two tests:

- **Model-swap test.** If you replaced the underlying model/solver with another, would a lasting AI
  lesson remain? If yes → a genuine AI contribution (ECAI-shaped). If no → likely a pure-ML paper
  wearing an AI title (route to an ML venue).
- **General-audience test.** Could a reviewer from a *different* AI subfield see why the
  contribution matters? ECAI's broad pool rewards work that travels beyond one niche.

## ECAI vs the sibling flagships

| If your contribution is... | Prefer | Because |
|---|---|---|
| Broad AI (symbolic + learning), European flagship, general audience | **ECAI** | EurAI's general-AI venue; breadth is the point |
| The same, but you want the international flagship / its calendar | **IJCAI** | In **2026 they are the same event** (joint IJCAI-ECAI); in other years, different calendars/organizers |
| The same, but on the AAAI calendar / North-American flagship | **AAAI** | General AI too; different body, dates, template |
| Fundamentally about multi-agent interaction, mechanisms, negotiation | **AAMAS** | Dedicated MAS pool and reviewers |
| Pure knowledge representation / reasoning theory | **KR** | Specialist KR audience and depth |
| A benchmark-driven ML advance with no symbolic/decision lesson | **NeurIPS/ICML** | Pure-ML venues reward the leaderboard framing ECAI does not |
| A deployed, real-world AI application | **ECAI → PAIS** | PAIS is ECAI's prestigious-applications track |

Because these venues overlap, decide by **best-matched reviewer pool + calendar + community pull**,
not by prestige alone. A paper matched to a specialist pool (AAMAS/KR) can fare better there than in
ECAI's broad pool.

## The 2026 twist: ECAI is joint with IJCAI

For this cycle, **ECAI 2026 = IJCAI-ECAI 2026** (Bremen, 15-21 Aug 2026). So "ECAI vs IJCAI" is not
a choice in 2026 — it is one submission to the joint conference, following IJCAI's process,
template (`ijcai.sty`), 7+2 page budget, and open-access IJCAI proceedings. The standalone-ECAI
FAIA/`ecai.cls`/PAIS identity returns in a non-joint year. Confirm which regime your target edition
is in before routing (`ecai-submission`, `ecai-camera-ready`).

## Main track vs PAIS

Route to **PAIS** (Prestigious Applications of Intelligent Systems, co-located with a standalone
ECAI) when the contribution is a **credible real-world deployment** whose value is the application,
not a new general mechanism:

- **Main track:** the contribution is a new technique, guarantee, or understanding that generalizes.
- **PAIS:** the contribution is a *system that works in the real world* — the lesson is the
  deployment, the constraints handled, the impact demonstrated.

PAIS has its own call and page budget (ECAI 2024: 7+1) and rewards impact and real conditions over
benchmark abstractions (`ecai-experiments`). Note PAIS is a **standalone-ECAI** fixture; verify
whether an applied track exists in a joint IJCAI-ECAI year (special tracks like AI4Tech, AI &
Robotics, AI & Health, AI & Social Good may serve that role — **待核实** per cycle).

## Calendar-driven routing

- ECAI/IJCAI/AAAI run on **different calendars** (except the joint years). Route partly by which
  deadline your work will actually be ready for — a rushed ECAI submission with a gap has **no
  revision round** to save it (`ecai-review-process`).
- The two-deadline front (abstract, then paper) means you commit the title/abstract a week before
  the PDF; do not register an ECAI abstract you are not confident you can deliver.

## Red flags that you are at the wrong venue

- The lesson evaporates under the **model-swap test** → ML venue.
- Only a specialist could care → AAMAS/KR.
- The value is a deployment, not a mechanism → PAIS.
- You are choosing ECAI over IJCAI in 2026 → they are the same event this year.

## Output format

```text
[Contribution shape] technique/guarantee / empirical understanding / multi-agent / KR theory / deployed system
[Model-swap test] AI lesson survives model swap? yes/no
[Venue] ECAI (main) / ECAI-PAIS / IJCAI / AAAI / AAMAS / KR / ML venue — with the deciding reason
[2026 regime] standalone ECAI or joint IJCAI-ECAI (same event as IJCAI this year)
[Calendar fit] ready for this deadline given no revision round? yes/no
```
