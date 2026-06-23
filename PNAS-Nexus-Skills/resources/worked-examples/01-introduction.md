> **Illustrative teaching example.** The paper, setting, numbers, and every claim below are
> **fictional** and exist only to demonstrate PNAS Nexus house style. No real-paper facts are stated, and
> **no policy or societal recommendation is invented** beyond what a result of this shape could plainly
> support. Corresponding skills:
> [`pnasnexus-significance`](../../skills/pnasnexus-significance/SKILL.md),
> [`pnasnexus-abstract`](../../skills/pnasnexus-abstract/SKILL.md),
> [`pnasnexus-fit`](../../skills/pnasnexus-fit/SKILL.md), and
> [`pnasnexus-writing`](../../skills/pnasnexus-writing/SKILL.md).

# Worked Example: A PNAS Nexus Significance Statement + Abstract (before → after)

PNAS Nexus Research Reports carry **two distinct front-matter artifacts** — a mandatory
**Significance Statement of 50–120 words** written for a broad, cross-disciplinary reader (answers
*"so what, and who cares?"*), and a **≤250-word single-paragraph Abstract** with **no headings** written
for scientists (answers *"what did you do and find?"*). They must not read the same. Note the two
PNAS-Nexus-specific traps this example highlights: the Significance Statement has a **50-word floor** (not
just a 120-word ceiling), and the abstract must be a **single paragraph with no subheadings**.

**Illustrative paper (fictional):** *"Low-cost street sensors reveal how extreme heat reshapes when and
where city residents move."* Fictional setting: a year of block-level temperature and pedestrian-flow data
from a network of inexpensive sensors in one large city, linked to anonymized mobility counts. The work
straddles **engineering** (the sensor network), **physical/environmental science** (urban heat), and
**social science** (human mobility and exposure) — a natural PNAS Nexus cross-division fit.

The genre rules being demonstrated:

- **Significance Statement** (`pnasnexus-significance`): **50–120 words**; gap → plain-language advance →
  why it matters → optional concrete application; no jargon, no acronyms, no citations; genuinely broader
  and plainer than the abstract.
- **Abstract** (`pnasnexus-abstract`): **≤250 words; one paragraph, no subheadings**, no
  citations/figure callouts; five moves (context → gap → approach → quantified result → implication);
  ≥1 quantified result with uncertainty; distinct in register from the Significance Statement.
- **Fit** (`pnasnexus-fit`): a reader from another division must say "I understand why this matters" — and
  the broad implication must be *demonstrated*, not asserted.

---

## Before (the two artifacts are nearly identical, both too technical, and the statement is too short)

**Significance Statement (draft — 36 words, under the 50-word floor, and just a compressed abstract):**

> Using a low-cost IoT sensor network and anonymized CDR-derived mobility traces, we quantify
> heat-induced spatiotemporal redistribution of pedestrian flux, finding a statistically significant
> negative association between wet-bulb globe temperature and midday ambulatory volume across census
> blocks.

**Abstract (draft):**

> Using a low-cost IoT sensor network and anonymized CDR-derived mobility traces, we quantify
> heat-induced redistribution of pedestrian flux. We deployed sensors and ran regressions. Midday flux
> decreased with temperature. This has implications for urban planning, public health, climate
> adaptation, transportation policy, and environmental justice in cities worldwide.

**What's wrong (against `pnasnexus-significance` / `pnasnexus-abstract` / `pnasnexus-fit`):**

- **The Significance Statement is below the 50-word floor** — PNAS Nexus enforces a **minimum** of 50
  words as well as the 120-word ceiling; 36 words is non-compliant.
- **It is a compressed abstract** — same content, same register; the skill's most-flagged failure. It
  must be genuinely broader and plainer.
- **Jargon and undefined acronyms** ("IoT", "CDR-derived", "wet-bulb globe temperature", "ambulatory
  volume") — a reader from another division cannot follow it.
- **The abstract is too short and under-quantified** — it states a direction ("decreased") with no
  magnitude, no uncertainty; the skill requires ≥1 quantified result (magnitude + unit + CI/P).
- **The abstract opens with method, not stake**, and ends on a **scattershot list of implications**
  asserted, not earned (a `pnasnexus-fit` over-claiming trigger).

---

## After — Significance Statement (plain, within 50–120 words, distinct from the abstract)

> *(103 words. No acronyms, no instrument names, no citations — the four moves: gap → plain advance →
> why it matters → concrete application.)*
>
> As cities get hotter, people change not just whether they go outside but when and where — yet most heat
> studies rely on a few official weather stations that miss how conditions vary street by street. We used
> a dense network of inexpensive sensors, paired with anonymized counts of foot traffic, to map this at
> the scale of individual blocks. On the hottest afternoons, movement did not simply fall; it shifted
> away from the most exposed streets and into shaded ones, and toward cooler hours. Knowing which blocks
> empty out, and when, lets cities target shade, water, and cooling where residents actually go.

---

## After — Abstract (~235 words, five moves, quantified, single paragraph, no headings, scientist register)

> *(235 words. One paragraph; context → gap → approach → quantified results → implication; acronyms
> defined on first use; quantified headline with uncertainty.)*
>
> Extreme urban heat is a growing driver of illness and death, but its effect on human behavior is
> usually studied with sparse official weather stations that cannot resolve the large temperature
> differences that exist between one street and the next. Whether residents respond to heat by reducing
> movement overall, or by redistributing it across space and time, has therefore been difficult to
> establish at the scale at which people actually make decisions. Here we paired a year of measurements
> from a dense network of low-cost street-level temperature sensors with anonymized, block-level counts
> of pedestrian activity in one large city, and modeled how local heat related to where and when people
> moved. Total midday pedestrian activity on the hottest afternoons was lower than on mild afternoons,
> but the dominant response was spatial and temporal redistribution rather than simple withdrawal:
> activity on the most sun-exposed blocks fell substantially more than on nearby shaded blocks, and a
> measurable share of afternoon activity shifted into the cooler early morning and evening. The
> block-level sensor data explained more of this variation than the city's official station network
> alone. These results show that residents adapt to extreme heat by reorganizing their use of urban space
> and time, not only by staying indoors, and that inexpensive, dense sensing can reveal exposure patterns
> invisible to conventional monitoring — information cities can use to place cooling resources where and
> when people are most exposed.

---

## Why the "after" pair meets the PNAS Nexus bar

Mapped to the skill checklists:

- **Within both bounds** — the Significance Statement is **103 words (≥ 50 and ≤ 120)**; the draft's
  36-word version would have been rejected on the floor alone (`pnasnexus-significance`).
- **Two distinct artifacts, not one written twice** — the Significance Statement is plain and answers
  "why does a non-specialist care?"; the abstract is technical and answers "what did you do and find?"
  (`pnasnexus-abstract` / `pnasnexus-significance`: "if the two read the same, the Significance Statement
  is wrong").
- **The Significance Statement passes the cross-division test** — every term a reader in another field
  would not know is gone: "wet-bulb globe temperature" becomes "the hottest afternoons", "CDR-derived
  ambulatory volume" becomes "anonymized counts of foot traffic" (`pnasnexus-significance` rewrite drill).
- **Single paragraph, no headings, within the cap** — the abstract is 235 ≤ 250 words, one unstructured
  paragraph with no citations or figure callouts (`pnasnexus-writing` order; `pnasnexus-abstract` hard
  constraints).
- **Quantified, with the headline earned** — the abstract reports a *direction plus a structured pattern*
  (exposed vs shaded blocks; midday vs morning/evening) rather than "decreased", and ends on an
  implication the data support, not a scattershot list (`pnasnexus-abstract`; `pnasnexus-fit`
  over-claiming triggers). *In a real submission, replace the qualitative magnitudes with exact effect
  sizes and confidence intervals.*
- **Cross-division significance demonstrated, not asserted** — an engineer (the sensing), an environmental
  scientist (urban heat), and a social scientist or planner (mobility, exposure) can each state why it
  matters, satisfying the `pnasnexus-fit` cross-division test for a genuinely interdisciplinary paper.

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified PNAS Nexus
> articles** whose front matter executes this two-artifact discipline, and [`../README.md`](../README.md)
> for how these resources fit the rest of the pack.
