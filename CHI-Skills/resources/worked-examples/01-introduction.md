> **Illustrative teaching example.** The paper, system, participants, and every
> number in this file are **invented** to demonstrate CHI first-page craft. No real
> paper is paraphrased, and no venue policy is asserted here beyond what
> [`../official-source-map.md`](../official-source-map.md) verifies. Companion
> skills: [`chi-writing-style`](../../skills/chi-writing-style/SKILL.md),
> [`chi-topic-selection`](../../skills/chi-topic-selection/SKILL.md),
> [`chi-experiments`](../../skills/chi-experiments/SKILL.md),
> [`chi-related-work`](../../skills/chi-related-work/SKILL.md).

# Worked Example: A CHI-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening for a mixed-methods interaction paper and
rebuild it to the CHI bar — contribution type declared, evidence named with its
population and setting, claims scoped in the sentence that makes them, and the
literature gap stated as a front rather than a coverage list. The screening rubric
CHI now applies before full review (ADR-Context, ADR-Contribution, ADR-Data,
ADR-Method) is the grading standard throughout.

**Fictional paper:** *"Whose Turn Is It? Addressee Ambiguity in Shared Voice
Assistants for Multigenerational Households."* Invented study: a four-week
deployment of a commercial smart speaker augmented with a researcher-built addressee-light
prototype in 14 multigenerational homes, with interviews and interaction logs.

---

## Before (a typical first draft)

> **Abstract.** Voice assistants are becoming increasingly popular in homes around
> the world. However, most research has focused on single users. In this paper, we
> present a novel system and a study of voice assistants in multigenerational
> households. Our results show that our system significantly improves the user
> experience. We conclude with design implications for future voice assistants.
>
> **Introduction.** Smart speakers have seen massive adoption in recent years.
> Companies like Amazon and Google have sold millions of devices. Many researchers
> have studied voice interaction, including [long list of citations]. However,
> there is a lack of research on multigenerational households. We built a system
> called TurnLight and evaluated it with users. The results were very positive.
> Our contributions are: (1) a novel system; (2) a user study; (3) design
> implications.

**Why this fails the CHI screening rubric:**

- **ADR-Context exposure.** The literature appears as an undifferentiated citation
  list ("many researchers have studied...") with no front: what is known about
  shared voice use, and where exactly does it stop? (`chi-related-work`)
- **ADR-Data exposure.** "Results were very positive" and "significantly improves
  the user experience" attach no participants, no duration, no measures — the
  evidence is invisible on page 1. (`chi-experiments`)
- **Untyped contributions.** "A novel system; a user study; design implications"
  names no contribution type doing the work — is this an artifact paper validated
  by a deployment, or an empirical paper with a probe? The subcommittee cannot even
  be chosen from this. (`chi-topic-selection`)
- **Unscoped claims.** "Improves the user experience" is a universal claim; the
  study can at most support a claim about these households, this task family, this
  four-week window. (`chi-writing-style`)

---

## After (rebuilt to the CHI bar)

> **Abstract.** In multigenerational households, a shared voice assistant must
> decide *who is being addressed* — and its failures fall unevenly on the oldest
> and youngest speakers. We report a four-week deployment in 14 multigenerational
> homes (41 residents, ages 9–84) of a commercial smart speaker paired with
> TurnLight, a peripheral display that externalizes the assistant's addressee
> inference. Interaction logs (6,120 exchanges) show misaddressed commands
> clustered on older adults' speech, and interviews reveal households developing
> compensatory "speaking-for" routines that concentrated interactional labor on
> one family broker. With TurnLight present, households repaired misaddressing
> in situ more often and reported redistributed initiation. We contribute (1) an
> empirical account of addressee ambiguity as a household-level accessibility
> problem, (2) TurnLight as an open-sourced probe embodying inference
> transparency, and (3) four design implications for shared conversational
> devices.
>
> **Introduction (opening moves).** Deployments of home voice assistants have
> documented adoption and appropriation in single-adult and nuclear-family homes
> [x, y], and lab studies have measured recognition disparities for older and
> younger voices [z, w]. What happens when both conditions hold at once — shared
> devices, mixed-age speakers, sustained real use — has not been studied in the
> field. This matters because the failure is interactional, not merely technical:
> when the device routinely serves the "easiest" voice, households reorganize
> around that bias... [gap → stake → study → contributions list as in the
> abstract, each bullet typed and pointed at its evidence section.]

**What changed, move by move:**

1. **The human stake leads.** The first sentence names who is affected and how —
   the "who changes what they do" test from `chi-topic-selection`.
2. **Evidence carries its own passport.** n=14 households, 41 residents, age range,
   four weeks, 6,120 logged exchanges: an AC triaging against ADR-Data can see the
   data's shape without leaving the abstract.
3. **The gap is an intersection, not an absence.** "No one studied X" invites a
   counterexample; "these two literatures each hold one piece, and the
   intersection is unexamined in the field" is a checkable front.
4. **Findings are stated as findings.** Misaddressing clustered on older adults;
   households developed brokerage routines; repair increased with the probe — each
   is scoped to the deployment and owns a results section.
5. **Contributions are typed** (empirical account / artifact-as-probe / design
   implications), which also settles the subcommittee conversation and the
   supplement plan (logs schema, interview guide, probe firmware —
   `chi-supplementary`).

---

## Transfer checklist for your own opening

- [ ] First paragraph names the humans and the stake, not the industry trend.
- [ ] Abstract states population, n, method, and duration for every study invoked.
- [ ] The gap sentence would survive a reviewer who knows both literatures.
- [ ] Every contribution bullet is typed and maps to a section and an artifact.
- [ ] No claim in the opening exceeds what the limitations section will later admit.
