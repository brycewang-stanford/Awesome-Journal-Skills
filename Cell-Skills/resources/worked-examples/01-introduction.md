> **Illustrative teaching example.** The paper, molecule, system, and every number below are
> **fictional** and exist only to demonstrate Cell house style. No real-paper facts are stated, and
> no policy is invented. Corresponding skills: [`cell-framing`](../../skills/cell-framing/SKILL.md),
> [`cell-summary`](../../skills/cell-summary/SKILL.md), and
> [`cell-highlights`](../../skills/cell-highlights/SKILL.md).

# Worked Example: A Cell-Style Summary + Opening (before → after)

This demonstrates the **Cell single-narrative arc** from `cell-framing`:
**broad problem → gap / hypothesis → why now (tractable) → the mechanism we found → broad significance** —
and the Cell front-matter conventions from `cell-summary` (one unstructured ≤150-word Summary that
*names the mechanism* and *quantifies*) and `cell-highlights` (Highlights ≤85 chars, an ~50-word
third-person eTOC blurb, and a single-panel Graphical Abstract). The Cell rule that governs all of it:
the manuscript tells **one mechanistic story**, and the reader knows the mechanism before Results.

**Illustrative paper (fictional):** *"Mitochondrial protease LONP2 clears oxidized aconitase to license
the integrated stress response."* Fictional system: a mouse hepatocyte model plus reconstituted
biochemistry, in which loss of a matrix protease (the invented "LONP2") couples oxidative damage to a
cytosolic stress program.

---

## Before (a list of experiments — typical first-draft Summary + opening)

> **Summary.** Here we report several findings on LONP2, a mitochondrial protease. LONP2 was knocked
> down in hepatocytes and we performed RNA-seq, proteomics, and metabolomics. Many pathways were
> changed. We also did co-immunoprecipitation and found interacting partners. The integrated stress
> response (ISR) was affected. These results provide insights into mitochondrial proteostasis and may
> have implications for disease. Further studies are needed to clarify the mechanism.
>
> **Introduction.** Mitochondria are essential organelles that have been studied extensively. Many
> proteases exist in the matrix. The ISR is an important pathway. In this study, we characterize LONP2
> using multiple approaches and present a number of results relating to mitochondrial function.

**What's wrong (against `cell-fit` / `cell-framing` / `cell-summary` / `cell-highlights`):**

- **No mechanism named.** It says the ISR "was affected," never *how* — the top `cell-summary` failure
  (states *that*, not *how*). A descriptive, mechanism-free story is a `cell-fit` desk-reject trigger.
- **No quantification.** "Many pathways," "a number of results" — `cell-summary` requires a quantified
  headline effect.
- **A list of techniques, not one arc.** RNA-seq + proteomics + metabolomics + co-IP are presented as
  parallel mini-projects, exactly the anti-frame `cell-framing` rewrites.
- **Throat-clearing intro** ("studied extensively," "important pathway") that buries the advance — the
  reader reaches Results without knowing the mechanism.
- **Jargon/filler on the blacklist** ("Here we report," "provide insights," "Further studies are
  needed") flagged by `cell-summary`.
- **Over-length-prone, label-style verbs** ("characterize") instead of a declarative claim.

---

## After (Cell arc — one mechanism, named and quantified, significance-forward)

> **Summary.** Cells must couple mitochondrial oxidative damage to the cytosolic programs that defend
> the proteome, yet how a matrix-localized injury is read out across the organelle boundary is unknown.
> *(context + gap, for a general life-scientist.)* We show that the mitochondrial protease LONP2
> degrades oxidized aconitase, and that when LONP2 is lost, undegraded oxidized aconitase accumulates
> and triggers the integrated stress response through the kinase HRI. *(approach + the mechanism, named
> explicitly.)* LONP2 deletion raised ISR target ATF4 **4.2-fold** and reduced hepatocyte survival under
> oxidative stress by **60%**; re-expressing catalytically active — but not protease-dead — LONP2 fully
> restored both. *(quantified headline result + a loss/gain causality pair that makes it a complete
> story.)* Thus LONP2 is a proteostatic sensor that converts mitochondrial oxidation into an adaptive
> cytosolic response, defining a mechanism linking organelle damage to cell-fate decisions in
> oxidative disease. *(significance for a broad community.)*
>
> *(Word count ≈ 135 — under the ~150 ceiling; single unstructured paragraph; no citations, no
> subheadings.)*

> **Introduction (opening, ≈3–4 short paragraphs — skeleton).**
>
> *(¶1 broad problem.)* A cell's proteostasis network must sense damage wherever it arises, but
> mitochondria are topologically sealed: oxidative injury inside the matrix must somehow be communicated
> to the cytosolic stress machinery. How that signal crosses the boundary is a central unsolved problem
> in organelle quality control.
>
> *(¶2 specific gap / hypothesis.)* The integrated stress response can be activated by mitochondrial
> dysfunction, but the molecular event that *initiates* it from inside the matrix is unknown. We
> hypothesized that a matrix protease reads out a specific oxidized substrate, and that the substrate —
> not the protease activity per se — is the signal.
>
> *(¶3 why now / why tractable.)* Reconstituting LONP2 with defined oxidized substrates, combined with a
> hepatocyte system in which we can delete and re-express catalytic variants, finally lets us separate
> *sensing* from *degradation* and test causality both ways.
>
> *(¶4 what we found + implication.)* We find that LONP2 clears oxidized aconitase, and that failure to
> clear it — not loss of the protein itself — triggers the HRI-dependent ISR. This identifies a
> defined molecular sensor coupling mitochondrial oxidation to cell fate, and reframes matrix proteases
> as signaling nodes, not just housekeeping enzymes. *(the reader now knows the mechanism before
> Results.)*

---

## The Cell front-matter artifacts (from `cell-highlights`)

**Highlights** (3–4 telegraphic bullets, each ≤85 characters incl. spaces; phenomenon → mechanism →
causality → significance):

```
- LONP2 degrades oxidized aconitase in the mitochondrial matrix            (61 chars)
- Loss of LONP2 lets oxidized aconitase trigger the ISR via HRI            (61 chars)
- Protease-dead LONP2 fails to rescue ISR activation and cell death        (65 chars)
- A matrix protease couples mitochondrial oxidation to cell fate           (62 chars)
```

**eTOC / "In Brief" blurb** (~50 words, third-person, lay — about the paper, never "we"):

> Zhang et al. show that the mitochondrial protease LONP2 acts as a damage sensor: it clears oxidized
> aconitase, and when it cannot, the unremoved protein switches on a cytosolic stress program through
> the kinase HRI. The work reframes matrix proteases as signaling hubs linking organelle damage to cell
> survival.

**Graphical Abstract** (single panel, top→bottom cause→effect, minimal text): one image, two states.
*Top:* healthy mitochondrion, LONP2 (scissors icon) degrading oxidized aconitase → cytosol calm, ISR
off. *Bottom:* LONP2 absent → oxidized aconitase accumulates → arrow crosses to cytosol → HRI → ATF4 →
reduced survival. No A/B/C sub-panels, no legend paragraph, colorblind-safe.

---

## Why the "after" meets the Cell bar

Mapped to the skill checklists:

- **Mechanism named, not just a phenotype** — "LONP2 degrades oxidized aconitase … triggers the ISR
  through HRI" (`cell-summary`: names the molecular cause; `cell-fit`: a worked-out mechanism, not a
  description).
- **Quantified headline result** — 4.2-fold ATF4; 60% survival drop (`cell-summary`: at least one
  quantified effect in the Summary).
- **Causality both ways** — loss (deletion) *and* gain (catalytically active vs. protease-dead
  re-expression) make it a *complete* story (`cell-fit` loss-of-function + gain-of-function pair).
- **One arc, not a technique list** — Summary and intro carry a single hypothesis → mechanism →
  significance line; orthogonal assays are evidence *for the arc*, demoted from the headline
  (`cell-framing`).
- **Significance-forward, general-reader framing** — first sentence is legible outside the subfield and
  ends on what it means for oxidative disease (`cell-framing` intro shape; `cell-summary` move 1 + 5).
- **Constraints respected** — Summary ≈135 words, single unstructured paragraph, no citations;
  Highlights ≤85 chars; eTOC ~50 words third-person; Graphical Abstract single-panel (`cell-summary`,
  `cell-highlights`).
- **Blacklist cleared** — no "Here we report," "provide insights," or "Further studies are needed"; the
  declarative title names actor + effect (`cell-framing` title discipline).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified Cell papers**
> whose Summaries and openings execute this arc, and
> [`../external_tools.md`](../external_tools.md) for the deposition, STAR Methods, and Cell Press author
> resources this pack references.
