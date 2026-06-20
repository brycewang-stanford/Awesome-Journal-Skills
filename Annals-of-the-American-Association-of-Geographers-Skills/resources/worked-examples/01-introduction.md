> **Illustrative teaching example.** The paper, study area, dataset, and every number below are
> **fictional** and exist only to demonstrate Annals of the AAG house style. No real place, dataset, or
> finding is described. Corresponding skills:
> [`aaag-writing-style`](../../skills/aaag-writing-style/SKILL.md),
> [`aaag-topic-selection`](../../skills/aaag-topic-selection/SKILL.md),
> [`aaag-theory-building`](../../skills/aaag-theory-building/SKILL.md), and
> [`aaag-research-design`](../../skills/aaag-research-design/SKILL.md).

# Worked Example: An Annals-Style Introduction (before → after)

This demonstrates the **Annals introduction bar** from `aaag-writing-style` and `aaag-topic-selection`:
**by the end of the introduction the reader knows the geographic question, the argument, the evidence,
and why it matters to geography broadly** — not just to one area's specialists. The funnel is
**geographic question → the stake of space/scale/environment-society → why it is hard to identify →
setting & design → headline finding with the mechanism → portable geographic contribution → brief
roadmap**, with the Annals' distinctive demands that the **geography be load-bearing** (delete-test),
the **area be clear**, and the **spatial method be defended on its own terms**.

**Illustrative paper (fictional):** *"Cooling Where It Counts: How the Scale of Urban Greening
Determines Who Gets Relief from Extreme Heat."* Fictional setting: a mid-sized metropolitan region whose
municipalities expanded tree-canopy programs at **different spatial scales** (parcel, block, district),
creating within-region variation in greening configuration. (Area: Nature and Society / Geographic
Methods; method: spatial analysis of remotely sensed land-surface temperature with geographically
weighted models. Chosen because the *scale* of an environmental intervention — not just its amount — is
a discipline-wide geographic stake; see the GWR exemplar in [`../exemplars/library.md`](../exemplars/library.md).)

---

## Before (area-insider, buries the geography — typical first draft)

> Urban heat is a growing problem. Many studies have mapped the urban heat island and shown that tree
> canopy lowers land-surface temperature. In this paper, we use Landsat-derived land-surface temperature
> and a geographically weighted regression to study the relationship between tree canopy and temperature
> across our study region. We compiled canopy data from municipal records and ran models at the census-
> tract level. Reducing heat is important for public health. Section 2 reviews the literature on urban
> heat islands, Section 3 describes the study area, Section 4 presents the data, Section 5 presents the
> methods, Section 6 reports results, and Section 7 concludes.

**What's wrong (against `aaag-writing-style` / `aaag-topic-selection`):**

- **Geography is decorative, not load-bearing.** The argument ("canopy lowers temperature") would
  survive deleting every spatial element — it fails the delete-test in `aaag-topic-selection`.
- **No scale argument.** The whole point — that the *scale* of greening matters — is absent; the model
  is run at one arbitrary unit (census tract) with no MAUP/scale reasoning (`aaag-research-design`).
- **Leads with method and study-area description** instead of the geographic question and argument — the
  `aaag-writing-style` anti-pattern of burying the contribution.
- **No portable contribution.** Nothing another area (Methods, Human, Physical) could import; the
  `aaag-theory-building` portability test fails.
- **Over-signposted seven-section roadmap** padding a document whose **11,000-word cap counts captions,
  notes, and tables** (`aaag-writing-style`).

---

## After (Annals arc — geographic stake + scale argument + portable contribution early)

> **Does it matter at what spatial scale a city plants its trees — or only how many it plants?** We show
> that the *configuration* of urban greening, not just its quantity, governs who is relieved from extreme
> heat: when canopy is added in **contiguous, district-scale** patches it lowers land-surface temperature
> roughly **three times** as much for nearby low-income blocks as the same canopy area dispersed parcel by
> parcel. *(geographic question + the scale stake + headline finding in the first breath — this is a claim
> about the spatiality of environmental benefit, not a canopy-temperature correlation.)*
>
> Why this matters across geography: a recurring problem — from political ecology to land-system science
> to spatial analysis — is that we measure environmental interventions by *amount* while their effects are
> set by *spatial configuration and scale*. If the same quantity of greening produces unequal cooling
> depending on how it is arranged in space, then environmental justice is partly a question of spatial
> design, and the unit at which we evaluate programs can manufacture or hide that inequity. *(the stake,
> framed so a Nature-Society reader, a methods specialist, and a physical geographer all see it —
> `aaag-topic-selection` reach test.)*
>
> Identifying this cleanly is hard because municipalities did not choose greening scale at random: a city
> may plant district-scale patches precisely where heat and need are already concentrated, so a naive
> comparison would confound the configuration with the conditions that prompted it — and because results
> can be an artifact of the unit of analysis (the modifiable areal unit problem). *(why it is hard — the
> identification and MAUP problems stated plainly, per `aaag-research-design`.)*
>
> We exploit a region whose municipalities expanded canopy at **different scales** for administrative
> reasons unrelated to local heat trends, pair Landsat-derived land-surface temperature with parcel-level
> canopy, and estimate **geographically weighted** models that let the canopy-temperature relationship
> vary over space. We test the result across **three areal units** to show it is not a unit artifact, and
> validate temperature retrievals against an independent station sample. *(setting & design in one
> paragraph; the spatial method is named as a tool, and scale/MAUP and validation are addressed up front.)*
>
> District-scale greening lowers temperature by **2.1°C** for adjacent low-income blocks against **0.7°C**
> for dispersed greening of equal area, and the gap is stable across areal units. The mechanism is **not**
> simply more trees: contiguous canopy creates connected shade and evapotranspiration corridors that
> dispersed planting cannot, concentrating relief where canopy connectivity is highest. *(headline finding
> with the mechanism and a ruled-out rival — the `aaag-research-design` adjudication move, including the
> scale-artifact check.)*
>
> Our contribution is to show that **the cooling benefit of greening is a property of its spatial
> configuration and scale, not of its quantity** — so programs evaluated by canopy *amount* can be both
> ineffective and inequitable. This reframes a "how much" question as a **"how, and at what scale"**
> question that any geographer studying environmental interventions can carry to their own case. *(portable
> geographic contribution stated early: a methods specialist gets a scale-sensitivity lesson, a
> nature-society scholar gets an environmental-justice mechanism, a physical geographer gets a connectivity
> process — `aaag-theory-building` portability test.)*
>
> The paper proceeds as follows. Section 2 develops the configuration-and-scale argument and its observable
> implications; Section 3 presents the data, design, and the scale-robustness results; Section 4 examines
> the connectivity mechanism and scope conditions. *(brief roadmap — no over-signposting.)*

---

## Why the "after" meets the Annals bar

Mapped to the skill checklists:

- **The geography is load-bearing** — the argument is *about* spatial configuration and scale; deleting
  the geography destroys it (passes the `aaag-topic-selection` delete-test).
- **Scale and MAUP are taken seriously** — the result is tested across areal units and the unit-artifact
  worry is named before the design, per `aaag-research-design` and `aaag-data-analysis`.
- **Portable, cross-area contribution** — the claim ("cooling is a property of configuration and scale,
  not quantity") is framed so Methods, Nature-Society, and Physical readers can each import it
  (`aaag-theory-building` portability test).
- **Identification problem named before the design**, and the **strongest rival is adjudicated** ("the
  mechanism is *not* simply more trees… instead connected shade/ET corridors"), with validation stated —
  the `aaag-research-design` adjudication sentence.
- **Method demoted to a tool** — GWR and Landsat retrievals appear where the design is discussed, never
  as the lead (avoids the `aaag-writing-style` "leading with the method/study-area" anti-pattern).
- **Reads across the discipline and respects the cap** — jargon is defined, the roadmap is three sections
  not seven, and the framing is legible to a generalist geographer within the inclusive 11,000-word limit
  (`aaag-writing-style`: counts include captions/notes/tables).

> Next: hold the maps and remote-sensing figures to cartographic standard with
> [`../../skills/aaag-tables-figures/SKILL.md`](../../skills/aaag-tables-figures/SKILL.md); stress-test
> the spatial design against the venue-neutral
> [`../../../shared-resources/empirical-methods/reviewer-objection-checklist.md`](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md)
> and report results to the shared
> [`../../../shared-resources/empirical-methods/reporting-standards.md`](../../../shared-resources/empirical-methods/reporting-standards.md);
> and benchmark the framing against verified real Annals papers in
> [`../exemplars/library.md`](../exemplars/library.md).
