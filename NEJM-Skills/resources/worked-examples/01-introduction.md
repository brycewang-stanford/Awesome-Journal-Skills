> **Illustrative teaching example.** The trial, setting, and every number below are **fictional** and
> exist only to demonstrate NEJM house style for a clinical-trial abstract and introduction. No real-trial
> facts are stated and no clinical recommendation is implied. Corresponding skills:
> [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md), [`nejm-writing`](../../skills/nejm-writing/SKILL.md),
> [`nejm-study-design`](../../skills/nejm-study-design/SKILL.md), [`nejm-reporting`](../../skills/nejm-reporting/SKILL.md),
> [`nejm-statistics`](../../skills/nejm-statistics/SKILL.md), and [`nejm-ethics`](../../skills/nejm-ethics/SKILL.md).

# Worked Example: An NEJM-Style Abstract + Introduction (before → after)

This demonstrates two things at once, drawn **only** from this pack's own skill files:

1. The **structured abstract** required by [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md) — four headed
   sections (**Background / Methods / Results / Conclusions**), ≤250 words, primary outcome led with an
   **effect size + 95% CI** (not a bare P value), the **intention-to-treat** population and per-group n stated,
   ending with the **trial registration number** and **funding source**.
2. The **terse IMRAD Introduction** required by [`nejm-writing`](../../skills/nejm-writing/SKILL.md) — the
   clinical problem, the gap, the specific question, ending with the objective; no mini-review.

It also shows the **CONSORT-aligned** reporting expectations from
[`nejm-reporting`](../../skills/nejm-reporting/SKILL.md) (participant flow that reconciles with the analysis
population), the **prospective registration** non-negotiable from
[`nejm-study-design`](../../skills/nejm-study-design/SKILL.md), and the statistical reporting discipline from
[`nejm-statistics`](../../skills/nejm-statistics/SKILL.md) (CI over bare P, ITT primary, absolute risk + NNT
alongside relative measures).

**Illustrative trial (fictional):** *"Early High-Flow Oxygen versus Standard Oxygen in Adults Hospitalized
with Community-Acquired Pneumonia (the FICTIONAL OXYGEN-CAP Trial)."* Every figure is invented for teaching.

---

## Before (an unstructured abstract that buries the result)

> Community-acquired pneumonia remains a major cause of hospitalization worldwide and has been studied
> extensively. Oxygen therapy is a cornerstone of management, and there has been much interest in whether
> more aggressive oxygenation strategies are beneficial. We performed a study using high-flow oxygen and
> found interesting and robust results suggesting that this novel approach may be helpful. Patients did
> better on the new treatment, which was statistically significant (P<0.05). High-flow oxygen could
> represent a promising new standard of care for pneumonia and should be widely adopted. Further work is
> needed.

**What's wrong (against this pack's skills):**

- **Not a structured abstract.** [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md) requires four headed
  sections (Background / Methods / Results / Conclusions); this is one unheaded paragraph.
- **No effect size and no 95% CI** for the primary outcome — only "P<0.05," which
  [`nejm-statistics`](../../skills/nejm-statistics/SKILL.md) explicitly forbids as the sole result.
- **No design, no population, no per-group n, no ITT** — the Methods content
  [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md) and [`nejm-study-design`](../../skills/nejm-study-design/SKILL.md) require is absent.
- **No registration number and no funding source** in the Conclusions, both mandated by
  [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md) and [`nejm-study-design`](../../skills/nejm-study-design/SKILL.md).
- **Over-claiming** ("should be widely adopted," "new standard of care") — exactly the over-reach
  [`nejm-writing`](../../skills/nejm-writing/SKILL.md) flags as a top rejection reason.
- **Filler adjectives** ("interesting," "robust," "novel," "promising") that
  [`nejm-writing`](../../skills/nejm-writing/SKILL.md) bans; "numbers, not adjectives."

---

## After — the structured abstract (NEJM house style)

> **BACKGROUND**
> Hospitalized adults with community-acquired pneumonia commonly receive supplemental oxygen, but the
> standard low-flow approach may not relieve hypoxemia quickly. It is unknown whether early high-flow nasal
> oxygen, as compared with standard oxygen, reduces the need for escalation to mechanical ventilation.
>
> **METHODS**
> We conducted a multicenter, randomized, open-label trial. We randomly assigned 1,200 adults hospitalized
> with community-acquired pneumonia and hypoxemia (oxygen saturation <92%) in a 1:1 ratio to early high-flow
> nasal oxygen (600 patients) or standard oxygen (600 patients), with randomization in permuted blocks
> stratified by site. The pre-specified primary outcome was escalation to invasive mechanical ventilation
> within 14 days. The secondary outcome was 28-day all-cause mortality. Analyses followed the
> intention-to-treat principle; outcome assessors were blinded.
>
> **RESULTS**
> The primary outcome occurred in 66 of 600 patients (11.0%) in the high-flow group and in 108 of 600
> (18.0%) in the standard-oxygen group (absolute difference, −7.0 percentage points; 95% CI, −11.1 to −2.9;
> relative risk, 0.61; 95% CI, 0.46 to 0.81; P=0.001), corresponding to a number needed to treat of 15.
> At 28 days, all-cause mortality was 7.5% versus 9.0% (absolute difference, −1.5 percentage points; 95% CI,
> −4.5 to 1.5). Serious adverse events occurred in 4.2% versus 3.8% of patients.
>
> **CONCLUSIONS**
> Among adults hospitalized with community-acquired pneumonia and hypoxemia, early high-flow nasal oxygen
> reduced escalation to mechanical ventilation within 14 days as compared with standard oxygen. (Funded by
> the Fictional National Institute for Respiratory Research; OXYGEN-CAP ClinicalTrials.gov number,
> NCT00000000.)

**Why this clears the bar (mapped to the skills):**

| Requirement | Skill | How the rewrite satisfies it |
| --- | --- | --- |
| Four headed sections, ≤250 words | [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md) | Background / Methods / Results / Conclusions present; tight prose. |
| Primary outcome led with effect + 95% CI | [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md), [`nejm-statistics`](../../skills/nejm-statistics/SKILL.md) | Absolute difference **and** relative risk, each with a 95% CI, plus exact P. |
| ITT + per-group n | [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md), [`nejm-statistics`](../../skills/nejm-statistics/SKILL.md) | "intention-to-treat"; 600 vs 600 stated. |
| Absolute risk + NNT alongside relative | [`nejm-statistics`](../../skills/nejm-statistics/SKILL.md) | Absolute difference and NNT (15) given, not relative risk alone. |
| Registration number + funding source in Conclusions | [`nejm-abstract`](../../skills/nejm-abstract/SKILL.md), [`nejm-study-design`](../../skills/nejm-study-design/SKILL.md) | NCT number and funder named in the final sentence. |
| Conclusion calibrated, names the comparator | [`nejm-writing`](../../skills/nejm-writing/SKILL.md) | "as compared with standard oxygen"; no "new standard of care" over-reach. |

> Note: the registered primary outcome must match the reported one
> ([`nejm-study-design`](../../skills/nejm-study-design/SKILL.md)). In a real submission, the open-label design
> would carry a justification and a blinded-outcome-assessment note in the Methods
> ([`nejm-study-design`](../../skills/nejm-study-design/SKILL.md)).

---

## After — the Introduction (terse IMRAD, NEJM house style)

> Community-acquired pneumonia is among the most frequent reasons for hospital admission, and hypoxemia at
> presentation marks patients at risk for clinical deterioration. Supplemental oxygen is standard care, but
> the conventional low-flow approach can be slow to correct hypoxemia, and some patients progress to invasive
> mechanical ventilation.
>
> High-flow nasal oxygen delivers heated, humidified oxygen at high flow rates and can be started early on the
> ward. Whether beginning high-flow oxygen early — rather than after deterioration — reduces the need for
> mechanical ventilation in this population is not established; prior data come largely from intensive-care
> settings and other diagnoses.
>
> We therefore conducted the OXYGEN-CAP trial to determine whether early high-flow nasal oxygen, as compared
> with standard oxygen, reduces escalation to invasive mechanical ventilation within 14 days among adults
> hospitalized with community-acquired pneumonia and hypoxemia.

**Why this is NEJM-shaped (mapped to [`nejm-writing`](../../skills/nejm-writing/SKILL.md)):**

- **Two to three short paragraphs**: the clinical problem, the gap, then the specific question — ending on the
  objective. No exhaustive background; detail would move to references and the protocol.
- **Question, not method, leads.** It opens with the clinical problem, not the apparatus.
- **Plain, terse sentences; past tense for what was done** ("We therefore conducted…"); present tense for
  established facts ("Supplemental oxygen is standard care").
- **No over-claim and no filler.** No "novel," "robust," or practice recommendation — the Discussion, not the
  Introduction, weighs implications soberly.

---

## CONSORT and ethics reminders this example assumes (not shown above)

Per [`nejm-reporting`](../../skills/nejm-reporting/SKILL.md) and
[`nejm-ethics`](../../skills/nejm-ethics/SKILL.md), a real OXYGEN-CAP write-up would also carry:

- A **CONSORT 25-item checklist** and a **participant flow diagram** (Enrollment → Allocation → Follow-up →
  Analysis) whose denominators reconcile with the 600-vs-600 ITT populations and Table 1.
- **Prospective registration before first enrollment**, with the registered primary outcome matching the
  reported one; the **protocol and statistical analysis plan** submitted as a supplement.
- **IRB/ethics approval and informed consent** per the Declaration of Helsinki, **ICMJE COI disclosures**, a
  **role-of-the-funding-source** statement, and a **data-sharing statement** — all stated in the Methods/end
  matter, not the abstract.

> **All numbers above are fictional teaching values. Do not cite them. To benchmark against real NEJM trials
> by design, see [`../exemplars/library.md`](../exemplars/library.md).**
