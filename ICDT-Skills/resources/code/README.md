# ICDT "Code" / Proof-Artifact Adapter

ICDT is a **pure database-theory** venue: for almost every paper there is **no code artifact and no
artifact-evaluation track**. The deliverable that plays the role code plays elsewhere is the
**complete-proofs full version** — the marked appendix in the reviewed PDF and the archived arXiv
version. This directory therefore stays deliberately thin, and points reusable checks at the shared
tooling only where they genuinely transfer.

ICDT-specific *policy* (the two-cycle calendar, the Cycle-1 revision, anonymous review since 2024,
the `lipics-v2021` 15-page format, the no-online-appendix rule, LIPIcs/CC-BY publication) lives in
the skills and in [`../official-source-map.md`](../official-source-map.md).

## Shared kits (use only what transfers to a theory paper)

- [`../../../shared-resources/submission-readiness/readiness-checklist.md`](../../../shared-resources/submission-readiness/readiness-checklist.md)
  — generic pre-submission checklist; adapt it to the ICDT proof-completeness and anonymity items
  rather than to code packaging.
- [`../../../shared-resources/submission-readiness/response-to-referees.md`](../../../shared-resources/submission-readiness/response-to-referees.md)
  — response scaffolding; adapt it to the **Cycle-1 revision letter** in
  [`../../skills/icdt-author-response/SKILL.md`](../../skills/icdt-author-response/SKILL.md).

Do **not** import the ML-conference reproducibility kit, Docker/`check_repro_package.py` layout
checks, or the econometrics/Stata tooling used by other packs in this repository. An ICDT submission
is a LaTeX document with proofs, not a runnable package, and "reproducibility" here means
**verifiability of theorems** (`../../skills/icdt-reproducibility/SKILL.md`).

## The ICDT proof-artifact checklist (what the generic tooling cannot check)

- **Every theorem has a complete, in-PDF proof.** The body proves or sketches each result; the marked
  appendix holds the full details, read at the PC's discretion. There is **no online appendix** and no
  "proofs available on request."
- **The single PDF is self-contained.** Nothing acceptance-critical depends on an external link during
  review (`../../skills/icdt-supplementary/SKILL.md`).
- **Bounds match and are labeled.** If tightness is claimed, both the upper and the lower bound are
  proved and identified (`../../skills/icdt-experiments/SKILL.md`).
- **The full version exists and agrees with the paper.** Maintain an arXiv full version with all
  proofs; it must state the same theorems and bounds as the LIPIcs paper, and it is linked from the
  camera-ready via `\relatedversion` (`../../skills/icdt-camera-ready/SKILL.md`).
- **Any optional code is not the contribution.** For the rare algorithmic paper with an experiment,
  archive code in a DOI-issuing repository and link it from the full version — but if the code is the
  point, the paper belongs at EDBT/SIGMOD, not ICDT (`../../skills/icdt-topic-selection/SKILL.md`).

## Minimal, dependency-free self-check for a LaTeX submission

```bash
# Sanity checks on an ICDT submission source tree (no venue policy encoded — just hygiene)
grep -rIl '\\documentclass' . | head                      # confirm lipics-v2021 is the class in use
grep -RIn 'lipics-v2021'  *.tex | head                     # class actually referenced
grep -RInE 'thebibliography|\\bibliography' *.tex | head    # references present (do not count to 15pp)
grep -RInE 'appendix' *.tex | head                          # a marked appendix exists for full proofs
# Anonymity smoke test on the built PDF:
pdftotext paper.pdf - | grep -nEi 'acknowledg|funded by|grant no|our (earlier|previous) (paper|work)' | head
```

Treat the script as hygiene only. The real bar — proof completeness, matching bounds, the right model
of computation — is a human reading task the ICDT skills describe.
