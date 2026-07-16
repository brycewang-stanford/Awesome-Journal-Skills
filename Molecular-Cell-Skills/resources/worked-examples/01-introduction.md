> **Illustrative teaching example.** The protein, structure, system, and every number below are
> **fictional** and exist only to demonstrate Molecular Cell house style. No real-paper facts are stated,
> and no policy is invented. Corresponding skills:
> [`molcell-framing`](../../skills/molcell-framing/SKILL.md),
> [`molcell-summary`](../../skills/molcell-summary/SKILL.md), and
> [`molcell-highlights`](../../skills/molcell-highlights/SKILL.md).

# Worked Example: A Molecular Cell Summary + Opening (before → after)

This demonstrates the **Molecular Cell single-mechanism arc** from `molcell-framing`:
**molecular problem → gap / hypothesis → why now (the step is now visible) → the mechanism we proved →
physiological consequence** — and the Cell Press front-matter conventions from `molcell-summary` (one
unstructured Summary that *names the molecular mechanism* and *quantifies*) and `molcell-highlights`
(Highlights ≤85 chars, an ~50-word third-person eTOC blurb, and a single-panel Graphical Abstract). The
governing rule: the manuscript proves **one molecular mechanism**, and the reader knows it before Results.

**Illustrative paper (fictional):** *"The replicative helicase XYZ couples single-subunit ATP hydrolysis to
strand-selective unwinding."* Fictional system: a reconstituted helicase plus a human cell model, in which
a conserved β-hairpin grips the lagging strand and one subunit's hydrolysis paces translocation.

---

## Before (a technique list — typical first-draft Summary + opening)

> **Summary.** Here we studied the helicase XYZ, an important replication protein. We solved cryo-EM
> structures, performed unwinding assays, and did cell-based experiments. XYZ was found to bind DNA and
> hydrolyze ATP. Knockdown affected replication. These results provide insights into DNA replication and
> may have implications for genome stability. Further studies are needed to clarify the mechanism.
>
> **Introduction.** DNA replication is a fundamental process that has been studied extensively. Helicases
> are essential enzymes. Many questions remain. In this study, we characterize XYZ using multiple
> approaches and present a number of results relating to its function.

**What's wrong (against `molcell-fit` / `molcell-framing` / `molcell-summary` / `molcell-highlights`):**

- **No molecular mechanism named.** "Binds DNA and hydrolyzes ATP" is not a *step* — the top
  `molcell-summary` failure (states *that*, not *how*). A mechanism-free story is a `molcell-fit`
  desk-reject trigger.
- **No quantification.** "A number of results," "affected replication" — `molcell-summary` requires a
  quantified headline (a rate, a resolution, a fold-change).
- **A list of techniques, not one mechanism.** Cryo-EM + assays + knockdown are presented as parallel
  activities, exactly the anti-frame `molcell-framing` rewrites.
- **Throat-clearing intro** ("studied extensively," "essential enzymes") that buries the mechanism — the
  reader reaches Results not knowing what was proven.
- **Jargon/filler on the blacklist** ("Here we studied," "provide insights," "Further studies are needed").
- **Label-style verb** ("characterize") instead of a declarative molecular claim.

---

## After (Molecular Cell arc — one mechanism, named, quantified, physiologically anchored)

> **Summary.** How replicative helicases couple ATP hydrolysis to strand separation at a stalled fork is
> unclear. *(molecular context + gap, for a molecular-biology reader.)* Combining a 2.9 Å cryo-EM structure
> with single-molecule unwinding and reconstitution, we show that the helicase XYZ grips the lagging strand
> through a conserved β-hairpin and that hydrolysis at a single subunit ratchets the enzyme one nucleotide
> per step. *(orthogonal approaches + the mechanism, named at the molecular level.)* A β-hairpin point
> mutant uncouples ATPase from unwinding, slows fork progression **12-fold**, and sensitizes cells to
> replication stress; wild-type but not the mutant rescues. *(quantified headline + separation-of-function
> that makes the mechanism airtight.)* XYZ thus converts nucleotide hydrolysis into processive,
> strand-selective translocation that safeguards genome duplication. *(physiological consequence.)*
>
> *(Word count ≈ 110 — under the ~150 ceiling; single unstructured paragraph; no citations, no
> subheadings.)*

> **Introduction (opening, ~3 short paragraphs — skeleton).**
>
> *(¶1 molecular problem.)* Replicative helicases must convert ATP hydrolysis into directional, strand-
> selective unwinding, yet how the chemical step is mechanically coupled to strand separation — and how the
> enzyme chooses which strand to translocate on — is not understood at the level of a defined contact.
>
> *(¶2 gap / hypothesis.)* Prior work localized unwinding activity to XYZ but could not separate DNA
> gripping from ATP hydrolysis, leaving the coupling mechanism unresolved. We hypothesized that a specific
> structural element grips one strand and that hydrolysis at a single subunit — not all subunits — sets the
> step size.
>
> *(¶3 why now + what we found.)* A 2.9 Å structure of XYZ trapped on a forked substrate, combined with a
> reconstituted single-molecule assay that resolves individual steps, finally lets us separate gripping
> from hydrolysis and test causality with point mutants. We find that a conserved β-hairpin grips the
> lagging strand and that single-subunit hydrolysis paces one-nucleotide steps; a mutant that breaks only
> the grip uncouples ATPase from unwinding and destabilizes forks in cells. *(the reader now knows the
> mechanism before Results.)*

---

## The Cell Press front-matter artifacts (from `molcell-highlights`)

**Highlights** (3–4 telegraphic bullets, each ≤85 characters incl. spaces; phenomenon → mechanism →
causality → consequence):

```
- Cryo-EM captures helicase XYZ gripping the lagging strand           (66 chars)
- A conserved beta-hairpin couples ATP hydrolysis to unwinding        (61 chars)
- A hairpin mutant uncouples ATPase from strand separation            (57 chars)
- Single-subunit hydrolysis paces processive fork unwinding           (58 chars)
```

**eTOC / "In Brief" blurb** (~50 words, third-person, accessible — about the paper, never "we"):

> Zhang et al. show how a replicative helicase turns chemical energy into motion. The enzyme grips one DNA
> strand with a small conserved loop and burns ATP one subunit at a time to pry the strands apart, a
> stepwise mechanism that keeps DNA replication moving through obstacles and protects genome stability.

**Graphical Abstract** (single panel, left→right cause→effect, minimal text): one image, two states.
*Left:* XYZ engaged, β-hairpin gripping the lagging strand, ATP → one-nucleotide step → fork advances.
*Right:* β-hairpin mutant, hydrolysis uncoupled → no translocation → fork stalls. No A/B/C sub-panels, no
legend paragraph, colorblind-safe.

---

## Why the "after" meets the Molecular Cell bar

Mapped to the skill checklists:

- **Mechanism named at the molecular level** — "β-hairpin grips the lagging strand … single-subunit
  hydrolysis ratchets one nucleotide per step" (`molcell-summary`: names the molecular cause; `molcell-fit`:
  a worked-out step, not a description).
- **Quantified headline** — 2.9 Å; 12-fold slower (`molcell-summary`: at least one quantified effect).
- **Orthogonal validation** — structure + single-molecule + reconstitution converge, and a point mutant
  ties the mechanism to the phenotype (`molcell-fit` orthogonality + separation-of-function).
- **One mechanism, not a technique list** — Summary and intro carry a single question → mechanism →
  consequence line; the assays are converging evidence, demoted from the headline (`molcell-framing`).
- **Physiologically anchored** — the in-vitro mechanism is shown to matter in cells (fork stability under
  replication stress) (`molcell-fit` physiological relevance).
- **Constraints respected** — Summary ≈110 words, single unstructured paragraph, no citations; Highlights
  ≤85 chars; eTOC ~50 words third-person; Graphical Abstract single-panel (`molcell-summary`,
  `molcell-highlights`).
- **Blacklist cleared** — no "Here we studied," "provide insights," or "Further studies are needed"; the
  declarative title names the molecular actor + action (`molcell-framing` title discipline).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **method × topic** positioning of
> Molecular Cell mechanistic stories, and [`../external_tools.md`](../external_tools.md) for the deposition,
> STAR Methods, and Cell Press author resources this pack references.
