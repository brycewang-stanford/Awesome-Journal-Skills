# STOC Code Adapter — What Applies at a Proofs-First Venue

This directory adapts the repository's shared tooling to STOC, and it starts
with a warning: STOC has no artifact track, no reproducibility checklist, and no
code-upload channel, so most conference-reproducibility tooling answers questions
this venue never asks. Use the shared ML-conference kit **only** for the narrow
cases below, and use the STOC-native checks for everything else.

## Shared kit (use selectively)

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

Legitimate uses for a STOC paper: sanity-checking a post-acceptance public
repository of illustration scripts, or packaging the checker for a
computer-assisted proof step. Do **not** import its experiment-matrix or
seed/compute reporting framing into the paper itself — that is venue confusion
(`../../skills/stoc-experiments/SKILL.md`).

## STOC-native checks (no dependencies)

```bash
# 1. Anonymity: metadata and self-reference sweep (double-blind cycles)
pdfinfo submission.pdf | grep -i author
grep -rn --include='*.tex' -iE 'our (paper|previous|earlier)|acknowledg' src/

# 2. Statement drift: extended abstract vs full version share statement files?
diff <(grep -h '\\begin{theorem}' -A4 abstract/*.tex) \
     <(grep -h '\\begin{theorem}' -A4 full/*.tex)

# 3. Confession grep: expand or justify every hit before submission
grep -rn --include='*.tex' -iE 'clearly|it is easy to see|standard argument|similarly' src/

# 4. arXiv full-version tarball with ancillary checker files
mkdir -p anc && cp verify_certificate.py anc/ 2>/dev/null
tar czf stoc-full.tar.gz full-version.tex macros.tex refs.bib sections/ anc/
```

Each check corresponds to a skill: 1 → `stoc-submission`, 2 →
`stoc-reproducibility`, 3 → `stoc-writing-style`, 4 → `stoc-artifact-evaluation`
and `stoc-camera-ready`.

## Scope note

Venue policy never comes from tooling. The controlling sources are the live CFP
and the trail in [`../official-source-map.md`](../official-source-map.md); the
skills in [`../../skills/`](../../skills/) interpret them.
