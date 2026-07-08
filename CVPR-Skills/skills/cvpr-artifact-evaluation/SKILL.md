---
name: cvpr-artifact-evaluation
description: Use when packaging code, models, datasets, or demo videos for a CVPR paper at either review time or release time, covering anonymous supplement packaging under the external-link ban, the dataset-release-by-camera-ready rule, model-weight and license decisions, and making a vision artifact runnable by a skeptical stranger.
---

# CVPR Artifact Evaluation

CVPR has no badge-granting artifact committee; the "evaluation" of your artifacts is
done informally, twice, by two different audiences. At review time, reviewers poke at an
anonymous supplement while deciding whether to trust your tables. After acceptance, the
entire field — 2026 drew 44,011 authors alone — decides whether your method becomes a
baseline or a citation nobody reproduces. Package for both audiences deliberately.

## Review-time artifacts: sealed-box rules

Everything must ride inside the uploaded supplement, because the 2026-verified policy
bans external links that expand content or subvert review. That kills the usual
anonymous-repo-link workflow many venues tolerate. Practical consequences:

- Code goes **in the supplement archive**, scrubbed: no `.git` history, no usernames in
  paths, no institutional cluster hostnames, no wandb entity names in configs.
- Model weights usually exceed sane archive sizes; ship configs + training commands +
  exact dependency pins instead, and say which checkpoints will be released.
- Demo videos are first-class CVPR evidence (see `cvpr-supplementary`) but strip
  container metadata — video files carry author tags more often than PDFs do.
- The 2026 supplementary **size cap was not verifiable** at check time (待核实); design
  the package assuming a strict cap, then confirm on the current page.

```bash
# Build a clean review artifact from a working repo
git archive --format=tar HEAD | tar -x -C /tmp/artifact       # no .git, no untracked junk
cd /tmp/artifact
grep -rniE "$(whoami)|<lab-name>|<cluster-host>|wandb\.(ai|entity)" . | head   # identity scan
pip-compile --quiet requirements.in                            # pin, don't approximate
zip -r ../supplement_code.zip . -x '*.ckpt' '*.pth'            # weights out, recipe in
```

## The runnable-by-a-stranger bar

A reviewer who opens your archive gives it minutes, not an afternoon. One entry point,
one config, one expected number:

| Artifact layer | Minimum viable | Gold standard |
|---|---|---|
| Environment | pinned `requirements.txt` + CUDA/driver note | Dockerfile reproducing the CRF hardware row |
| Inference | script + 5 sample images + expected outputs | notebook rendering figure-quality results |
| Training | full config + command + seed | resumable run with logged curves |
| Evaluation | script that recomputes one main-table row | all-tables harness with dataset download stubs |
| Data | loader + split files + provenance note | checksummed archive or release plan with license |

The single highest-leverage file is `REPRODUCE.md` mapping **each table/figure in the
paper to one command**. It converts a suspicious reviewer into a supportive one faster
than any rebuttal sentence.

## Release-time artifacts: promises come due

Two clocks start at acceptance. First, the verified dataset clause: a dataset claimed as
a contribution must be public by the camera-ready deadline — hosting, license, and
consent scrubbing included. Second, the softer but real credibility clock: the gap
between "code coming soon" in the README and actual code is measured publicly at CVPR
scale.

Release decisions to make explicitly rather than by default:

- **License**: weights and data need one (CC-BY-SA? research-only? non-commercial?);
  "no license" means legally unusable for the industrial half of the CVPR audience.
- **Weights**: which checkpoints — final only, or the ablation grid reviewers saw?
- **Provenance**: for scraped or generated data, document sources and filtering; for
  human data, document consent posture. Vision datasets attract scrutiny years later.
- **Benchmarks**: if you release an evaluation, freeze the metric code and version it —
  silent metric fixes fork the leaderboard.

## Weights and hosting decisions

Model releases have their own failure modes at vision scale:

- **Host durability**: lab web servers die with graduations. Prefer archival or
  platform hosting (institutional repositories, model hubs) with a checksum published
  in the README; the CVF open-access page will outlive your URL, so choose hosts with
  the same life expectancy.
- **Checkpoint provenance**: name each released checkpoint after the paper's table row
  it reproduces (`table2_row4_vitb.pth`), and state which exact code commit evaluates
  it to the printed number.
- **Safety posture for generative models**: decide before release what you ship —
  weights, LoRA deltas, or inference-only API — and write the model card's misuse
  paragraph yourself rather than letting the first misuse write it for you.
- **Version pinning at release**: tag the repo at camera-ready (`v1.0-cvpr`) so later
  refactors don't silently break the commands printed in the paper's supplement.

## Anti-patterns with CVPR-specific cost

- A project-page URL in the submission "for videos" — that is the banned external link,
  not a convenience.
- Supplement code that hard-codes `/home/<name>/data` — an anonymity leak *and* proof
  nobody ran it elsewhere.
- Claiming a dataset contribution, then releasing it months after camera-ready — a
  verified policy breach, not just bad manners.
- Releasing training code without evaluation code: at a benchmark-driven venue the
  evaluation is the artifact people actually reuse.

## After release: the maintenance tail

A used artifact generates issues, and the field reads your issue tracker. Budget a
small maintenance window post-conference: pin the environment against dependency rot,
answer the first wave of "can't reproduce Table 2" issues (usually environment
mismatches — point to the Dockerfile), and keep a `RESULTS.md` of community
reproductions. Six months of light maintenance is what turns a CVPR paper into the
baseline the next cycle's papers must cite.

## Reverify each cycle

- Supplement size/format caps and whether anonymized-repo links are (dis)allowed — the
  external-link wording can shift by year.
- The dataset-release clause wording.
- Any new artifact, checklist, or reproducibility fields on the OpenReview form.

## Output format

```text
[Artifact stage] review-supplement / camera-ready-release
[Identity scan] clean / hits: <files>
[Runnability] entrypoint · pins · expected-output map present?
[Weights & data plan] <ship now / release plan + license>
[Dataset clause] n/a / due at camera-ready: <status>
[Gaps] <ordered fixes>
```
