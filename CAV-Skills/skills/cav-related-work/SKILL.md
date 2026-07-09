---
name: cav-related-work
description: Use when positioning a CAV (Computer Aided Verification) submission against the verification literature across CAV, TACAS, FMCAD, VMCAI, POPL/PLDI, and the journals (FMSD, JAR, TOCL, STTT), writing delta-first contrast rather than a citation catalog, crediting the right benchmark and tool lineages, keeping self-citations double-anonymous for the anonymized categories, and handling concurrent and prior-version overlap.
---

# CAV Related Work

Use this to audit novelty and eligibility. CAV reviewers are close to the verification literature and
expect to see where your paper sits relative to the nearest prior technique or tool — stated as a
**delta**, not a list. Reopen the current CFP for dual-submission, anonymity, and prior-publication
rules before advising authors.

## Positioning checks

- **Separate the verification novelty from the engineering effort.** What is new: an algorithm, a
  decision procedure, an abstraction, a soundness result, a tool capability, or a benchmark regime
  nobody had covered?
- **Cover the verification lanes.** CAV reviewers expect the flagship venues, the tool ecosystems,
  and the journals — not just the papers nearest your method (see the table). A bibliography missing
  the obvious sibling work reads as unaware.
- **Write delta-first.** Each closely related paper gets one sentence naming what it did and one
  naming what you do differently — a technical contrast (what their method cannot do that yours can),
  not a summary.
- **Credit tool and benchmark lineages.** If you extend or compare against a solver/model checker or
  use a standard benchmark set, cite the tool paper and the benchmark/competition to their real
  origin — and to the right venue (Z3 is TACAS, not CAV; see the exemplars guardrails).
- **Preserve double-anonymity where required.** For Regular and Application papers, cite your own
  prior work in the third person and never link reviewers to an identity-revealing preprint,
  repository, or tool homepage. (Tool and Industrial papers are not anonymized.)
- **Declare overlap** with any prior workshop/conference version or concurrent submission; do not
  re-submit archival work as new.

## Verification literature lanes

| Lane | Typical venues | What CAV reviewers check |
|---|---|---|
| Flagship verification | CAV, TACAS | Whether the nearest broad technique/tool is compared or distinguished |
| Hardware / design | FMCAD | Whether hardware-model-checking predecessors are credited |
| Model checking & abstract interpretation | VMCAI | Whether foundational analysis work is engaged |
| Reasoning & proof | IJCAR, LPAR, ITP, CADE | Whether the proof/solver lineage is cited to its origin |
| PL foundations | POPL, PLDI, OOPSLA | Whether borrowed semantics/analysis ideas are credited |
| Journals | FMSD, JAR, TOCL, STTT | Whether deeper journal-length treatments of the topic are engaged |

A bibliography that cites only your own subarea tells a reviewer the delta may be smaller than
claimed; one that reaches the sibling flagships, the tool papers, and the journals signals command of
the field.

## Delta-first positioning vignette

Suppose the paper proposes a new interpolation-based invariant-synthesis technique. Its nearest
neighbors: the foundational interpolation-and-model-checking line (technique, different property
class), a TACAS tool that computes invariants by a different abstraction (tool, no interpolants), and
a journal study of interpolant quality (analysis, no synthesis method). The novelty sentence should
name all three contrasts — synthesis where the study offered only analysis, interpolant-based where
the tool used a different abstraction, and a new property class beyond the foundational line — and
cite each to its correct venue.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the technical difference, avoid unverifiable
                          priority claims; keep the citation anonymous for Regular/Application
[Your workshop version]   often non-archival and citable, but confirm against the current CFP and
                          phrase so anonymity survives (anonymized categories)
[Prior tool-paper version] declare the overlap; state what the new paper adds beyond the tool release
[Archival status unclear]  declare the overlap in the submission form rather than guessing
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" evaluation that re-reports a prior benchmark run without a new technique or question.
- Attributing a technique/tool to the wrong venue (the TACAS/FMCAD/VMCAI-vs-CAV trap) — a reviewer
  who knows the lineage reads it as carelessness.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <flagship / hardware / model-checking-AI / reasoning / PL / journals>
[Nearest 3 works] <work -> one-line technical delta -> correct venue cited?>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <CAV-ready contribution contrast against the nearest prior technique/tool>
```
