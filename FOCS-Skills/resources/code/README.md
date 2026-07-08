# FOCS Code Directory — Checkability Tooling for a Theorems Venue

FOCS runs no artifact track, requires no checklist, and asks for no code
(2026 CFP, checked 2026-07-08), so the repository's ML-conference
reproducibility kit answers almost nothing a FOCS author needs. This
directory says precisely which pieces still earn their keep, and gives the
FOCS-native checks that replace the rest.

## From the shared kit, keep only

- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)
  — as a smoke test on a *certificate package* for a computer-assisted proof
  step (README present, no absolute paths, no identity leaks) before it
  ships as arXiv ancillary material.
- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
  — background only. Do **not** import experiment matrices or seed/compute
  reporting into a FOCS paper; that vocabulary signals venue confusion
  (see [`../../skills/focs-experiments/SKILL.md`](../../skills/focs-experiments/SKILL.md)).

## FOCS-native checks

```bash
# (a) CFP compliance: letter paper, and NO copy/print security restrictions
pdfinfo submission.pdf | grep 'Page size'      # expect 612 x 792 pts
qpdf --show-encryption submission.pdf          # expect: not encrypted

# (b) Statement freeze: hash all formal statements in two source trees
#     (submission vs arXiv full version; rerun at camera-ready)
for d in sub-src full-src; do
  awk '/\\begin{(theorem|lemma|corollary|proposition)/,/\\end{/' $d/*.tex \
    | tr -d ' \n' | sha256sum
done

# (c) Blind sweep across ALL pages (appendices leak too)
grep -rn --include='*.tex' -iE 'acknowledg|grant no|our (earlier|previous)' .
exiftool -Author -Creator submission.pdf

# (d) Certificate package for a machine-checked lemma
sha256sum certificate/* > certificate/SHA256SUMS
python3 certificate/check_lemma.py certificate/cases.enum   # stdlib only
```

Mapping: (a) → `focs-submission`; (b) → `focs-reproducibility` and
`focs-camera-ready`; (c) → `focs-submission` / `focs-supplementary`;
(d) → `focs-experiments` and `focs-artifact-evaluation`.

## Scope note

Tooling never decides policy. The controlling sources are the live
`focs.computer.org` CFP and the trail in
[`../official-source-map.md`](../official-source-map.md); the skills in
[`../../skills/`](../../skills/) interpret them for each phase of the cycle.
