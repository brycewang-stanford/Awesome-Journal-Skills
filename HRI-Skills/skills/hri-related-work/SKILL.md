---
name: hri-related-work
description: Use when writing or auditing the related-work and positioning of an ACM/IEEE HRI full paper — covering HRI's crossing literatures (robotics, HCI, psychology, design), writing a delta-first argument that credits each community, and keeping self-citation compatible with double-blind review.
---

# HRI Related Work

An HRI related-work section has a harder job than most: it must place the paper in **several
literatures at once** — robotics, HCI, psychology/cognitive science, and design — because HRI
reviewers are drawn from all of them, and each expects to see their field cited correctly. A section
that reads as an ICRA lit review to a psychologist (or vice versa) signals the authors do not
understand the interdisciplinary conversation they are joining. This skill covers coverage,
positioning, and double-blind hygiene.

## Cover the crossing literatures

Map your paper to the lanes it actually touches, and cite each in that community's terms:

- **HRI conference and journal core** — the directly adjacent HRI work (prior HRI/THRI/JHRI studies
  on your construct or interaction). This is where reviewers look first; missing the nearest HRI
  neighbor is the classic fatal gap.
- **Robotics** — the technical substrate (perception, control, behavior generation, autonomy) your
  robot relies on, if the contribution is technical/systems.
- **HCI** — interaction design, evaluation methods, and any general-HCI phenomenon your interaction
  instantiates.
- **Psychology / cognitive & social science** — the theory behind your constructs (trust, mind
  perception, social presence, warmth/competence, persuasion), cited to its origin, not only to its
  HRI re-uses.
- **Design** — if yours is a design contribution, the design methods and precedents (probes,
  research-through-design, participatory design) it builds on.

You do not need every lane — you need the lanes your contribution genuinely engages, covered well
enough that a reviewer from each field trusts you.

## Delta-first positioning

HRI reviewers reward a crisp statement of what is **new**:

- For each closest prior work, state in one sentence **what they did** and **what you do
  differently** — a different robot, a different measured outcome (behavior vs. attitude), a
  different population, a causal manipulation where they had correlation, a design where they had a
  study.
- Prefer a **short, sharp delta** over an exhaustive survey. Eight pages do not allow a textbook
  review; they allow a targeted argument for why your contribution is needed.
- Avoid the "no one has studied X with a robot" claim unless it is true and load-bearing — novelty
  of *combination* is fine, but say why the combination matters, not merely that it is unclaimed.

## Credit theory correctly (the interdisciplinary trap)

The most common HRI positioning error is citing a psychological or design construct only through its
HRI re-uses:

- If you measure **trust**, **anthropomorphism**, **social presence**, or **persuasion**, cite the
  originating theory and the validated instrument, not just the last three HRI papers that used the
  word. A psychology reviewer notices immediately.
- If you borrow a **method** (thematic analysis, mixed methods, a specific experimental paradigm),
  cite its methodological source so a methods reviewer trusts you are using it correctly.
- Do not rename an existing construct; align your terminology with the field that owns it.

## Double-blind self-citation

HRI full-paper review is **double-blind**; positioning must not de-anonymize you:

- Cite your own prior work in the **third person** ("Prior work [X] found...", never "our previous
  work [X]"), and keep those citations in the normal reference list.
- If a new submission builds directly on your unpublished or under-review work, describe the
  relationship without identifying the authors; do not attach an identifying tech report.
- Do not remove necessary self-citations to avoid detection — a missing obvious reference is itself
  a signal. Anonymize the *phrasing*, not the *scholarship*.
- Watch acknowledgments, grant numbers, and platform/lab names elsewhere in the paper that a
  related-work reviewer might connect to an author (see `hri-submission`).

## Placement and length

- A **related-work section** works when the paper needs to survey a landscape; **inline positioning**
  (delta stated where each idea is introduced) often serves better under the 8-page budget. Choose
  one primary strategy; do not both survey at length and re-argue inline.
- Keep related work proportional — it exists to justify the contribution, not to prove reading. If it
  crowds out the method or results, cut it.

## Anti-patterns HRI reviewers flag

- **Single-field tunnel vision** — a robotics-only or psychology-only reference list for a paper that
  claims to be interdisciplinary.
- **Construct laundering** — using a theoretical term (e.g., "trust") while citing only its HRI
  buzzword uses, not its theoretical source or validated measure.
- **Survey-as-substitute** — a long neutral catalogue with no delta, leaving reviewers to guess the
  contribution.
- **First-person self-citation** — an anonymity break hiding in the related work.

## Output format

```text
[Literature lanes covered] HRI-core / robotics / HCI / psychology / design — which apply, which cited well
[Nearest HRI neighbor] identified and delta stated? yes/no
[Delta-first] each key prior work paired with an explicit difference? yes/no
[Theory credited] constructs/methods cited to origin + validated instrument? yes/no
[Double-blind] self-citations third-person; no identifying acknowledgments/labs? yes/no
[Fix queue] <ordered edits>
```
