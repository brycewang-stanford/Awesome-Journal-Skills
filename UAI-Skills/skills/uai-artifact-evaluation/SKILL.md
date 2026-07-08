---
name: uai-artifact-evaluation
description: Use when packaging code, data, samplers, solvers, and logs for a UAI submission's 50 MB supplementary ZIP or a public post-acceptance release, making probabilistic-inference claims independently runnable while keeping every file double-blind, given that UAI reviewers may open the archive but are not obliged to read it.
---

# UAI Artifact Evaluation

UAI posted no separate artifact-evaluation track or badge system for the 2026 cycle
(existence of one in later cycles: 待核实). What it did post is sharper than a badge: code
and data release is strongly encouraged, a 50 MB anonymous ZIP rides with the submission,
and reviewers judge whether claims are "backed up convincingly." The artifact's job is to
convert a skeptical probabilistic-ML reviewer's spot-check into confirmation.

## Design for the five-minute skeptic

Because reviewers are explicitly not required to consult supplementary material, assume
whoever opens the ZIP gives it five minutes. Optimize for that reader:

- A top-level `README` that states, in its first ten lines, what claim each script
  reproduces and how long it takes.
- One command per headline result, each with a small-scale mode that finishes on a
  laptop: a reviewer who reproduces Figure 2 at n=500 in ninety seconds will extend you
  trust for the n=50,000 version.
- Pinned dependencies and one canonical entry point. A `Makefile` or single driver
  script beats a directory of loose notebooks.
- Expected outputs stored beside the scripts, so "did it work?" needs no judgment.

## What inference artifacts must expose

Probabilistic-modeling papers fail reproduction in venue-specific ways. Package
accordingly:

| Contribution type | Must be in the artifact | Spot-check the reviewer will try |
|---|---|---|
| MCMC / SMC sampler | Seeds, chain configs, convergence diagnostics code | Re-run short chains; compare R-hat and ESS to reported |
| Variational method | ELBO logging, initialization scheme, optimizer settings | Reproduce the ELBO trace shape, not just the endpoint |
| Causal discovery | Graph-generation scripts, SHD/SID evaluation code | Regenerate synthetic graphs; verify metrics on one seed |
| Calibration / conformal | Score functions, split definitions, coverage computation | Recompute empirical coverage at one α |
| Probabilistic programming / PGM inference | Model source, query set, exact-baseline harness | Run the exact baseline on the smallest instance |
| Theory with simulations | Every constant used to instantiate the bound | Check simulation matches theorem conditions |

## Anonymity inside the archive

The double-blind requirement covers all supplementary material explicitly. Archive leaks
are quieter than PDF leaks, so build from a clean export:

```bash
# Build an anonymous artifact from a clean tree, never from the working repo
git archive --format=tar HEAD | tar -x -C /tmp/uai-artifact
cd /tmp/uai-artifact
grep -rniE 'university|\.edu|author|thanks|grant' --include='*.py' --include='*.md' . | head
find . -name '*.ipynb' -exec grep -l '"authors"' {} \;      # notebook metadata
rm -rf .git .github; find . -name '.DS_Store' -delete
zip -r ../supplement.zip . && du -h ../supplement.zip        # must be ≤ 50 MB (2026 cap)
```

Watch for: license headers with names, `pyproject.toml` author fields, conda environment
exports embedding usernames, wandb/MLflow run URLs tied to an account, dataset paths
containing `/home/<name>/`, and model checkpoints whose training config JSON names a
cluster.

## README skeleton for the archive

The archive's README is the artifact's abstract. A shape that fits the five-minute
reader:

```markdown
# Supplementary code for submission #<OpenReview number>

## Claim → command map (small-scale modes; full-scale flags noted)
| Paper claim | Command | Runtime (laptop) |
|---|---|---|
| Fig. 2 (coverage vs n) | `make fig2-small`  | ~2 min |
| Table 1 (SHD, 10 seeds) | `make table1-small` | ~4 min |
| Thm. 3 simulation | `make thm3-check` | ~1 min |

## Environment
- `pip install -r requirements.txt` (pinned versions; Python 3.11)
- No GPU required for small-scale modes.

## Expected outputs
- `expected/` holds reference CSVs; each command prints PASS/FAIL against them.

## Full-scale reproduction
- Flags, hardware used, and total runtime per experiment in `FULL_RUNS.md`.
```

Everything above stays anonymous by construction — no names, no lab conventions in
paths, no acknowledgement of infrastructure that identifies an institution.

## Data that cannot ship

- Under the 50 MB cap, ship generators, not corpora: the script that produces the
  synthetic SCMs or the subsampled benchmark, plus checksums for the full data.
- For licensed or private datasets, include the loader, the preprocessing pipeline, the
  schema, and summary statistics, and state access terms in the README.
- Never bypass a data-use agreement to help reviewers; explain the constraint instead.
  A stated limitation is a clarity point, a violated license is misconduct under the
  AUAI code of conduct.

## Licensing notes

- The review-time ZIP needs no license drama, but the post-acceptance release does:
  choose deliberately between permissive (MIT/BSD/Apache-2.0) and copyleft, and check
  employer policy before the camera-ready deadline forces a rushed default.
- Third-party code vendored into the archive keeps its own license; verify
  compatibility now, since reviewers occasionally notice a GPL file inside an
  "MIT" archive and read it as carelessness.
- Data licensing is separate from code licensing; a permissive code license does not
  launder a restricted dataset.

## After acceptance

Convert the anonymous ZIP into a public artifact worth citing: a tagged repository, an
archival DOI where your institution supports one, a license chosen deliberately, and the
README rewritten from "reviewer instructions" to "user instructions." Link it from the
camera-ready — post-acceptance is when the CFP's release encouragement costs you nothing
and earns citations.

## Output format

```text
[Artifact scope] supplement ZIP / public release / both
[Five-minute path] <command a reviewer runs first, and its runtime>
[Claim coverage] <headline results reproducible / total>
[Anonymity scan] clean / leaks: <files>
[Size] <ZIP size vs current cap>
[Data strategy] shipped / generated / loader-plus-terms
```
