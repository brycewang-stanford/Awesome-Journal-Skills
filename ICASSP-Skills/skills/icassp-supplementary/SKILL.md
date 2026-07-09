---
name: icassp-supplementary
description: Use when deciding what goes in the four ICASSP pages versus a public release, given that ICASSP has no reviewed appendix — managing the 4+1 budget, curating optional multimedia (audio, image, video) that reviewers may open, hosting derivations and extra results externally, and keeping the main paper self-contained under single-blind review.
---

# ICASSP Supplementary

Use this when assembling everything around an ICASSP paper that does not fit the four content
pages. The defining constraint: ICASSP has **no reviewed supplement or appendix that decides
acceptance**. The paper must be self-contained in 4+1 pages; anything else is optional material a
reviewer *may* consult but is not obliged to.

## The three shelves

| Shelf | What lives here | Reviewer obligation |
|---|---|---|
| Pages 1-4 | The claim, mechanism, and decision-critical results and figures | Must read |
| Page 5 | References, funding acknowledgements, ethical-standards statement only | Must read (references) |
| Optional release | Extended derivations, extra conditions, demo media, code | May consult, not guaranteed |

If a result decides acceptance, it belongs on pages 1-4. If it merely strengthens or illustrates,
it can live in the optional release — but never assume a reviewer opened it.

## What "supplementary" means at ICASSP

- Unlike double-blind ML venues with a reviewed appendix, ICASSP's optional material is usually a
  **public repository or a demo page**, and because review is single-blind it can carry your
  identity from the start.
- Some cycles allow uploading a **multimedia file** (audio, image, or video) with the submission
  through CMS; confirm the current paper kit for accepted formats and size limits before relying
  on it.
- Long proofs and derivations that will not fit four pages typically go to an **extended
  arXiv/technical-report version** cited from the paper, not to a reviewed appendix.

## Curating multimedia reviewers actually open

For enhancement, separation, synthesis, restoration, or any perceptual result, a short set of
**listenable or viewable examples** is often the most persuasive artifact:

- Provide a small, curated set (roughly five), not a dump; pick cases that show both a strength
  and an honest hard case.
- Label each example with its condition (SNR, corpus, or scene) so a reviewer can interpret it.
- For audio, include the input, the output, and a strong-baseline output side by side.
- Scrub embedded metadata only for privacy/consent reasons, not anonymity — single-blind review
  does not require hiding your identity.

## Keeping the four pages self-contained

- State each main theorem, algorithm, or system so a reviewer can judge it without the external
  material; a paper whose argument only closes in the arXiv version reads as unreviewable in four
  pages.
- Keep one derivation-sketch line in the body for any result whose full proof you exile to the
  technical report.
- Cross-reference the release from the paper at least once; unlinked material is invisible.

## Vignette: splitting an image-restoration paper

A submission proposes a denoiser with a stability argument and a broad evaluation. The body keeps
the method, the key stability statement with a one-line justification, and the two
decision-critical PSNR/SSIM tables; the extended derivation and the full noise-level sweep go to a
cited technical report; a demo page shows five before/after crops with a baseline. Nothing that
decides acceptance lives only off-paper, because ICASSP reviewers are not required to leave the
PDF.

## Consent and licensing checklist

```text
[On-paper] claim, mechanism, decision-critical results all in 4+1
[Off-paper] derivations / extra conditions / media / code (cited from paper)
[Media] curated set, labeled conditions, baseline shown
[Licensing] corpus/data license permits redistribution of any shipped samples
[Consent] speaker/subject consent cleared for any released recordings or images
```

## Output format

```text
[Supplement plan] ready / needs fixes / not ready
[Page budget] 4 content + 1 reference/acks/ethics respected?
[Self-containment] does the paper close without the external material?
[Media] curated / labeled / baseline-anchored
[Release link] present in paper and reachable
```
