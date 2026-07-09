---
name: hri-writing-style
description: Use when drafting or revising an ACM/IEEE HRI full paper's structure and prose for an interdisciplinary audience — leading with the human-robot contribution and research questions, making hypotheses and measures explicit, describing the robot embodiment, keeping claims proportional to the study within the 8-page acmart budget, and writing so the chosen track's contribution type is unmistakable.
---

# HRI Writing Style

HRI reviewers come from robotics, HCI, psychology, and design at once. A sentence that a roboticist
finds obvious may be opaque to a psychologist and vice versa, so HRI prose must be **legible across
disciplines** while making a **rigorous** contribution its home track can judge. You have **8 pages**
(including figures, excluding references) in the ACM `acmart` template — a tight budget that rewards
a clear arc and punishes throat-clearing. This skill builds the paper for that audience and budget.

## The HRI first-page arc

Lead with the interaction, not the machinery:

1. **The interaction problem** — a question about what happens *between a person and a robot*, in
   one or two sentences, in the first breath.
2. **Why we do not yet know** — the gap: what prior work measured, and why it does not answer this
   question (often: stated attitudes measured where behavior matters, or systems evaluated without
   people).
3. **The contribution, stated for your track** — a designed behavior/system/interface, a finding
   about people, a method, or a concept — named as the *kind* of contribution your track reviews.
4. **The study** — an embodied robot, real participants, a design a reviewer can judge, evidence
   proportional to the claim.
5. **What it means for designing interactive robots** — the implication, concrete.

See `resources/worked-examples/01-introduction.md` for a fictional before→after that executes this
arc.

## Make the study legible: state design, hypotheses, and measures

HRI's empirical reviewers expect the scaffolding to be explicit, ideally by the end of the
introduction or the top of the method:

- **Design** — between-subjects, within-subjects, or mixed; conditions and what is manipulated.
- **Hypotheses or research questions** — stated as predictions (H1, H2...) for confirmatory work, or
  as RQs for exploratory/qualitative work. Do not disguise an exploratory study as confirmatory.
- **Measures** — which construct each dependent variable operationalizes, and whether the instrument
  is validated (e.g., a named trust/anthropomorphism scale) or bespoke (justify it).
- **Robot and task** — enough that a reader pictures the embodiment and the interaction (and point
  to the video).

A paper that hides its design until Section 4 forces reviewers to reverse-engineer it, which reads
as evasion.

## Describe the robot embodiment (and lean on the video)

HRI is about embodied interaction, so the robot is not a detail:

- Name the platform and the relevant capabilities/behaviors; show it in a figure and the **video**.
- Distinguish what was **autonomous** from what was **teleoperated / Wizard-of-Oz** — reviewers will
  look for this, and hiding it is a credibility risk (see `hri-experiments`).
- Describe the interaction as it unfolds in *time*; static prose under-serves a temporal phenomenon,
  which is exactly what the video is for (see `hri-supplementary`).

## Claims proportional to the study

The fastest way to lose an HRI reviewer is a claim the study cannot support:

- A single lab study with one robot and short exposure supports a **bounded** claim, not a universal
  law about "robots." Say "in this task, with this robot," and frame generality as future work.
- Report **effect sizes and confidence intervals**, not just p-values; "significant" without a
  magnitude is uninformative about whether the effect matters for design.
- For qualitative work, claim **insight and transferability**, not frequency; report your analysis
  method (e.g., thematic analysis) and reflexivity, not a fake sample size.
- Match the verb to the evidence: "suggests," "indicates," "in our study" — not "proves."

## Write for the interdisciplinary reader

- **Define discipline-specific terms once.** A roboticist's "policy," a psychologist's "valence,"
  and a designer's "probe" each need a gloss for the other two-thirds of the room.
- **Justify constructs, don't assume them.** Explain why the measured construct (trust, warmth,
  competence, mind perception) is the right one for the interaction you study.
- **Prefer plain figures.** A clear condition diagram and a results plot with error bars communicate
  across fields better than dense tables.

## Budget discipline (8 pages, acmart)

- The template is fixed; recover space by **cutting**, not by shrinking margins or fonts (a
  formatting violation is a desk-reject risk — see `hri-submission`).
- Move detailed instruments, full model tables, and extended qualitative excerpts to the
  **supplement**, keeping in the body only what a reviewer must read to judge the paper (see
  `hri-supplementary`).
- References do **not** count against the 8 pages — but the body does, including figures. Budget
  figure space deliberately.

## Anti-patterns HRI reviewers flag

- **System-first framing** — leading with a capability and accuracy, burying the human question
  (route-signal that this may be an ICRA/IROS paper; see `hri-topic-selection`).
- **Scale dump** — administering many questionnaires and reporting whatever turned out significant,
  with no pre-registration and no correction.
- **Undisclosed Wizard-of-Oz** — presenting teleoperated behavior as autonomous.
- **Liking as outcome** — using a vague "users liked it" in place of the behavioral or theory-linked
  outcome the claim needs.
- **Over-signposting** — a paragraph of "Section 2 does X" standing in for an argument.

## Output format

```text
[First-page arc] problem → gap → contribution(track) → embodied study → design implication: present?
[Study legibility] design / hypotheses-or-RQs / measures stated early? yes/no
[Embodiment] robot described + video referenced? autonomy vs WoZ clear?
[Claim proportionality] claims bounded to the study? effect sizes reported?
[Budget] pages used (body incl. figures / refs) · formatting clean?
[Revisions] <ordered edits with section pointers>
```
