---
name: hri-supplementary
description: Use when planning the supplementary materials for an ACM/IEEE HRI full paper — above all the video figure that shows the embodied interaction, plus study instruments, extended results, and appendices — deciding what a reviewer must see to judge the interaction versus what belongs outside the 8-page body, all anonymized for double-blind review.
---

# HRI Supplementary Materials

HRI is unusual among conferences in how much the **video** matters. The interaction it studies is
temporal and embodied, and prose cannot convey what a robot's timing, motion, and presence do to a
person. A well-made supplementary **video figure** materially changes how reviewers understand the
contribution — and its absence is often read as a gap. This skill plans the video and the rest of
the supplement, and splits content between the body and the supplement by decision-criticality.

## The video figure comes first

Treat the video as a first-class artifact, not an afterthought:

- **Show the interaction**, not just the robot: the person and robot together, the conditions being
  compared, and the behavior your contribution designs or studies. A reviewer should *see* the
  difference your paper claims.
- **Keep it short and legible** — a focused clip (often a couple of minutes; check the current call
  for length/size limits, **待核实** per cycle) beats a long unedited recording. Caption or narrate
  what to look at.
- **Anonymize it for review** — this is the most-missed double-blind leak. Blur or omit identifiable
  faces, mute or remove identifying voices and lab/institution logos, and strip filename/metadata
  that names an author. If participants did not consent to public video, use a review-only,
  de-identified cut (see `hri-reproducibility`).
- **Format for reviewers** — a widely playable codec/container and a size the submission portal
  accepts; a video a reviewer cannot open is a video that does not exist.

## The decision-criticality rule

Ask of every piece of content: **could a reviewer reach the accept/reject decision without seeing
this?**

- **No → it belongs in the 8-page body.** The core design, the study design, the primary results and
  their effect sizes, the main figures, and the central limitation must be *in the paper*. Reviewers
  are not required to read the supplement to judge the paper, and decision-critical material hidden
  in an appendix is effectively invisible.
- **Yes → it can go to the supplement.** Full instrument text, extended tables, additional analyses,
  qualitative excerpts, and implementation detail live outside the body.

The 8-page budget (incl. figures, excl. references) forces this discipline; use it to keep the body
sharp, not to smuggle the argument into an appendix.

## What the supplement typically holds

- **Video figure** (the centerpiece) and, if relevant, a short **demo** clip.
- **Study instruments** — full questionnaires with items and scoring, interview guides, task
  instructions, consent-form summary.
- **Coding schemes and qualitative appendices** — codebooks, extended excerpts, additional themes.
- **Extended results** — full statistical tables, robustness/secondary analyses, per-condition
  breakdowns that would crowd the body.
- **Robot-behavior details** — parameters, WoZ protocol specifics, additional apparatus figures.
- **Reproducibility artifact pointer** — the (anonymized) archive of de-identified data and analysis
  code (see `hri-reproducibility`).

## Keep the body self-sufficient

- Every claim that decides the paper must be **supported in the body**; the supplement *enriches*, it
  does not *carry*.
- Reference supplementary items explicitly ("full scale in the supplement," "see supplementary
  video"), so reviewers know they exist — but never make a core inference depend on following the
  link.
- Do not use the supplement to exceed the page limit by relocating essential text; reviewers and
  chairs notice.

## Anonymization sweep for the supplement

Double-blind covers **everything uploaded**, not just the PDF:

- **Video** — faces, voices, logos, on-screen names, file metadata.
- **Data files** — free-text fields, participant identifiers, embedded author metadata.
- **Code/materials** — author names in headers, institution paths, repository owners.
- **Archive** — host behind an anonymizing view; a personal domain both rots and reveals identity.

See `hri-submission` for the mechanical checklist to run on the final files.

## Anti-patterns HRI reviewers flag

- **No video** for a paper about embodied, temporal interaction.
- **A video that leaks identity** (faces/voices/logos) in double-blind review.
- **Decision-critical results only in the supplement**, leaving the body unable to stand alone.
- **An unplayable or oversized video** the portal or reviewer cannot open.
- **Appendix used to dodge the page limit** by relocating essential argument.

## Output format

```text
[Video] present? shows the interaction/conditions? length/format within limits?
[Video anonymization] faces/voices/logos/metadata clean for double-blind?
[Body sufficiency] all decision-critical content in the 8 pages? yes/no
[Supplement contents] instruments · coding schemes · extended results · artifact pointer
[Anonymization] video + data + code + archive all swept?
[Fix queue] <ordered>
```
