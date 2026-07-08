---
name: colm-artifact-evaluation
description: Use when packaging the artifacts of a COLM paper — model weights, training data, prompts, evaluation sets, and cached model outputs — for anonymous review and public post-acceptance release, navigating licenses, API terms-of-service limits, and the absence of a formal COLM artifact track.
---

# COLM Artifact Evaluation

COLM had no formal artifact-evaluation track verifiable for the 2026 cycle (checked
2026-07-08; 待核实 each edition). That absence does not lower the bar — it moves the
audit into ordinary review, where artifact quality influences scores without a
rubric to appeal to. Package as if a skeptical reviewer will spend ten minutes with
your materials, because at this venue one usually will.

## The COLM artifact taxonomy

LM papers produce artifact types with very different release mechanics; inventory
yours before deciding anything:

| Artifact | Review-time form | Release-time form | Blocking question |
|---|---|---|---|
| Code (training/eval) | Anonymized repo or supplement ZIP | Public repo, tagged release | Does one command reproduce one table? |
| Prompts | Verbatim appendix + files in package | Same, public | Exact strings, incl. system prompts? |
| Fine-tuned weights | Usually described, not uploaded (size) | Model hub upload with model card | Does the *base* model's license permit derivative release? |
| Training/eval data you built | Anonymized sample + datasheet | Full release with license | Any personal data, scraped ToS conflicts, or annotator-privacy issues? |
| Cached model outputs | Sample in supplement | Full archive | Does the provider's ToS permit publishing outputs at this scale? |
| Human-eval materials | Instructions + interface in appendix | Same | IRB/consent status stated? |

The two questions authors most often skip are in the right-hand column: derivative
weight licensing and output-publication ToS. Both can void a promised release after
acceptance — resolve them *before* the paper commits to anything.

## One-command reproduction

The credibility core of the package is a single entry point per headline result:

```makefile
# Makefile at package root — one target per main-text table/figure
table2:            ## headline comparison, ~40 GPU-min or ~$8 API spend
	python run_eval.py --config eval/run-042.yaml --out results/table2.csv
figure3:           ## scaling curve from cached outputs (no model access needed)
	python plots/scaling.py --cache outputs/cache.jsonl --out figs/figure3.pdf
verify:            ## regenerate all numbers from cached outputs only
	python verify_from_cache.py --tolerance 0.1
```

The `verify`-from-cache target is the LM-specific trick: reviewers without GPUs or
API budgets can still confirm that your published numbers follow from your recorded
model responses. It converts "trust me" into "check me" at zero compute cost, and it
keeps working after API models drift or deprecate (`colm-reproducibility`).

## Anonymous review packaging

- Build from a clean export and grep for identity leaks — the commands and channel
  list live in `colm-supplementary`; org-scoped model-hub IDs are the leak class
  unique to LM work.
- If weights must be inspectable at review time, an anonymized hub account or a
  size-reduced distilled checkpoint are the workable options; a link to your lab's
  account is a double-blind violation under COLM's no-identifying-links rule.
- Include a `MANIFEST.md`: inventory, license per item, compute needed per target,
  and what is deliberately absent with the reason ("training corpus omitted:
  contains licensed text; filtering scripts included instead").

## Datasheets for anything you release

For each dataset or evaluation set: how items were created (author population,
LLM-generated fraction — disclosable under the 2026 LLM policy), collection dates
(this doubles as contamination documentation for future users), license and source
licenses, known biases and coverage gaps, and a contamination canary if you want
future training runs to be detectable. For model releases: intended use, evaluation
scope, and known failure modes. These documents are cheap at packaging time and
impossible to reconstruct honestly later.

## Post-acceptance release sequence

1. De-anonymize the repository; restore real hub org names and W&B links.
2. Upload weights/data with cards and licenses; tag the exact code release cited in
   the camera-ready.
3. Add the paper's OpenReview URL to every artifact so provenance points both ways.
4. Freeze a `colm2026` git tag — the paper cites a snapshot, not a moving `main`.
5. Update the paper's availability statement to match what actually shipped
   (`colm-camera-ready` owns the deadline: August 7, 2026 this cycle).

## The ten-minute reviewer walkthrough

Dry-run the package as the busiest plausible reviewer before every upload. The
sequence they follow is predictable, so optimize for it in order:

1. **Minute 1-2: open `MANIFEST.md`.** If there is no manifest, they grep for a
   README and form their opinion from whatever half-stale file they find. The
   manifest is the cheapest score you will ever buy.
2. **Minute 3-4: look for the entry point.** `make table2` or an equivalent single
   command. If the first thing they see is a 400-line setup guide with cluster
   assumptions, the walkthrough ends here.
3. **Minute 5-7: run `verify` from cache.** No GPUs, no keys, under a minute of
   compute — this is the step that actually gets executed in practice, which is
   why the cached-outputs archive earns its place in the package.
4. **Minute 8-9: spot-check a prompt file against the paper's appendix.** Any
   mismatch between packaged prompts and printed prompts contaminates trust in
   both.
5. **Minute 10: skim the code for identity leaks and hardcoded secrets** — partly
   ethics-duty, partly curiosity. This is where an org-scoped `from_pretrained`
   string ends your anonymity.

Sizing note: keep the review package lean — cached outputs can be sampled down to
what `verify` needs, with the full archive promised for release. No supplementary
size cap was verifiable for COLM 2026 (待核实), but a multi-gigabyte upload fails
socially even where it succeeds technically.

## Longevity: the two-year test

A COLM artifact's real audience arrives later — the group in two years trying to
compare against you. Two cheap investments serve them: freeze an environment
manifest (exact package versions; a container digest if you can), and write the
`MANIFEST.md` assuming every external URL in it will eventually rot — name
artifacts by content hash where possible so mirrors stay verifiable. The venue
publishes on OpenReview, where your artifact links are permanently attached to the
paper's public page; links that die quietly are the failure mode, so prefer
archival hosts for anything you would want cited.

## Output format

```text
[Inventory] code ▢ prompts ▢ weights ▢ data ▢ cached-outputs ▢ human-eval ▢
[Legal gates] base-model license: <ok/blocks release>  output-ToS: <ok/limits>
[One-command check] targets exist for: <tables/figures>  verify-from-cache: ▢
[Anonymity] package clean / leaks: <items>
[Manifest + datasheets] present / missing: <which>
[Release plan] <ordered steps with dates>
```
