---
name: jebo-literature-positioning
description: Use when staking a Journal of Economic Behavior & Organization (JEBO) manuscript's contribution against the behavioral, experimental, and organizational literatures. Builds the "what we knew / what was missing / what this adds" frame and a replication/extension stance; it does not invent citations.
---

# Literature Positioning (jebo-literature-positioning)

## When to trigger

- The intro lists prior work but never says what was *missing*
- A referee will ask "how is this different from [the obvious prior experiment]?" and you have no crisp answer
- The paper replicates or extends a known result and you need to position that honestly
- The contribution spans two literatures (e.g., social preferences + organizational design) and the bridge is unclear

## How JEBO referees read a contribution

JEBO referees come from several traditions (behavioral, experimental, evolutionary, organizational), so the positioning must speak to whichever community owns the result while remaining legible to the others. The journal values **cumulative, mechanism-level progress**: a paper earns its place by sharpening, bounding, reconciling, or overturning a *specific behavioral claim*, not by being the first to run a particular task. Because JEBO publishes replications and close extensions more readily than top-5 general-interest journals, an honest "we replicate X and show it breaks under condition Y" is a legitimate, publishable contribution — but only if positioned as such, not disguised as wholly novel.

Build the frame in three moves:

1. **What we knew.** Name the 2–4 anchor results the paper builds on, by mechanism, not by author-name-dropping. ("Other-regarding preferences predict positive giving in dictator games; giving falls under earned endowments and social distance.")
2. **What was missing or contested.** The gap must be a *behavioral* gap — an untested moderator, an unmodeled belief, an unresolved tension between two findings, a mechanism never separated from a confound — not merely "no one used my dataset."
3. **What this adds.** State the increment in one sentence and match it to evidence the paper actually delivers.

## Contribution archetypes JEBO accepts

| Archetype | What positions it well | Failure mode |
|-----------|------------------------|--------------|
| New mechanism / moderator | shows a previously-unidentified driver of a known behavior | "novelty" that is really a re-label of a known effect |
| Reconciliation | resolves a tension between two prior findings with a unifying design | cherry-picking which prior result to cite |
| Bounded replication | replicates and maps the boundary conditions of an influential result | hiding that it is a replication to seem more novel |
| Field test of a lab regularity | takes a lab effect to a consequential field/organizational setting | claiming external validity the design cannot support |
| Theory→prediction→test | derives and tests a sharp behavioral prediction | testing a prediction so loose any result confirms it |

## Positioning the replication/extension stance

If the paper is partly a replication, say so in the intro and frame the *value added* — new population, new incentive scale, new moderator, pre-registered confirmation of a contested result. JEBO referees punish disguised replications far more than honest ones.

## Checklist

- [ ] "What we knew / what was missing / what this adds" stated in three sentences, organized by mechanism
- [ ] The gap is behavioral and specific, not "no prior paper used this data/task"
- [ ] Anchor literature spans the relevant JEBO communities the result must satisfy
- [ ] If a replication/extension, it is labeled as such with the value-added named
- [ ] The claimed increment matches the evidence delivered later in the paper
- [ ] Citations are real; no invented exemplar papers (verify before asserting)

## Anti-patterns

- A literature review that summarizes papers serially instead of building toward the gap
- Inflating novelty by ignoring the closest prior experiment a referee will instantly recall
- A disguised replication presented as wholly new
- Positioning only within one tradition when the result must also satisfy a neighboring JEBO community
- Bridging two literatures with a hand-wave instead of an explicit mechanism-level link

## Output format

```text
【Journal】Journal of Economic Behavior & Organization
【Skill】jebo-literature-positioning
【What we knew】<anchor results by mechanism>
【What was missing】<specific behavioral gap>
【What this adds】<one-sentence increment>
【Archetype】mechanism / reconciliation / replication / field test / theory-test
【Replication stance】novel / honest extension / bounded replication
【Source status】citations verified / 待核实
【Next skill】jebo-identification
```
