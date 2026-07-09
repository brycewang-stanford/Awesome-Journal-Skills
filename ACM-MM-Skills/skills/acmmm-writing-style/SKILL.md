---
name: acmmm-writing-style
description: Use when revising an ACM MM (ACM Multimedia) paper for house style — putting the cross-modal contribution on the first page, framing media (figures, video, audio) as evidence rather than decoration, making the fusion the visible claim, and compressing the argument into a 6-8 page ACM sigconf body with references-only overflow.
---

# ACM MM Writing Style

Use this to revise an ACM Multimedia draft for the venue's expectations. The reader is a
busy reviewer scanning across sixteen thematic areas; the paper must announce *what is
multimedia about it* before the model diagram.

## The ACM MM first-page arc

Lead the abstract and first paragraph with: **problem → why one modality is insufficient →
the cross-modal method or system → media-grounded evidence → why it matters for
multimedia**. The multimedia contribution belongs on page one; a paper that opens with a
single-modality benchmark reads as a CVPR or ACL paper that wandered in.

- State the **fusion or systems mechanism** as the contribution, not a backbone swap.
- Make every media element *do work*: a teaser figure that shows the cross-modal signal, a
  video that is evidence for a claim, an audio clip that a reader can check.
- Scope claims to what the evidence supports; "improves engagement" needs a measured
  engagement result behind it.

## Media-as-evidence table

| Media element | Weak (decoration) | Strong (evidence) |
|---|---|---|
| Teaser figure | A pretty system diagram | The moment where modalities disagree and the method wins |
| Qualitative grid | Cherry-picked successes | Paired success/failure across modalities with captions that state the point |
| Supplementary video | "See our results" | A clip tied to a specific claim, with the baseline shown alongside |
| Audio sample | An unlabeled waveform | The case the vision-only baseline misses, annotated |

## Compression into the sigconf body

The 6–8 page body is short by ACM standards, and figures compete with text for space.

- Push proofs, full protocols, extra qualitative media, and hyperparameter tables to the
  **supplement**; keep the body's argument self-contained without them.
- Write **self-contained captions** — a reviewer reading only figures and captions should
  grasp the cross-modal claim.
- Budget page space before writing: decide which two or three media elements earn body space
  and which move to the supplement.

## Revision passes

```text
Pass 1 (contribution): Does page one name the cross-modal/systems contribution?
Pass 2 (fusion): Is the mechanism the claim, and is it ablated later?
Pass 3 (media): Does each figure/clip support a specific claim, with a self-contained caption?
Pass 4 (scope): Is every "better/more engaging/higher quality" tied to a measured result?
Pass 5 (budget): Does the body fit 6-8 sigconf pages with overflow holding references only?
```

## Title and abstract for cross-area reviewers

Your reviewers may come from different thematic areas, so the title and abstract have to be
legible to a vision person, an audio person, and a systems person at once.

- Put the **modalities and the mechanism** in the title where natural ("audio-visual," "text-and-
  image," "cross-modal") so area chairs assign the right reviewers.
- Make the abstract's first two sentences carry the whole contribution; a reviewer triaging many
  papers may read little more.
- Avoid single-community jargon in the abstract; define the one term your cross-area readers will
  not share.

## A body-budget worked pass

Treat the 6–8 page limit as a budget you allocate before writing prose:

```text
p1  intro: contribution + why one modality fails + teaser figure
p2  related work (tight) + problem setup
p3-4 method: the fusion/alignment mechanism, one architecture figure
p5-6 experiments: main table, the decisive ablation, failure cases, user-study summary
p7-8 discussion + limitations; references spill onto the overflow pages (references only)
```

If a section will not fit, move detail to the supplement rather than shrinking the font or
margins — template tampering is a desk-reject risk, and a cramped body reads worse than a clean
one with a fuller supplement.

## Common ACM MM style failures

- **Modality as garnish** — audio/text mentioned but never shown to matter; fix by leading
  with the seam and ablating it.
- **Vision-paper voice** — the whole framing is a benchmark race; fix by foregrounding the
  multimedia question.
- **Unbacked perceptual claims** — "more natural," "more engaging" with no user study; fix
  by measuring or softening.
- **Caption starvation** — figures that only make sense from the body text; fix by making
  captions stand alone.
- **Overflow abuse** — method text pushed onto the references pages; those pages are for
  references only, and misuse risks desk reject.

## Output format

```text
[First-page verdict] multimedia contribution up front / buried
[Fusion visibility] mechanism is the claim / hidden behind a backbone
[Media evidence] each element earns its place / decorative elements: <list>
[Scope] claims matched to evidence / overclaims: <list>
[Page budget] fits 6-8 sigconf pages / over by <n>
[Top three fixes] <ordered>
```
