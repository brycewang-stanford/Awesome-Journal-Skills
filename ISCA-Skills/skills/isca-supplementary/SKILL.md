---
name: isca-supplementary
description: Use when deciding what accompanies an ISCA submission beyond the 11 reviewed pages — what must live inside the page budget because reviewers see nothing else, how to use fully anonymized artifact links under the double-blind rules, staging material for the revision window, and planning post-acceptance release.
---

# ISCA Supplementary Strategy

ISCA's verified 2026 format was spare: a printable PDF of at most 11 pages of
text plus unlimited references, uploaded to HotCRP. The public guidelines
described no separate supplementary-file channel and no appendix regime — the
only sanctioned overflow surface they mention is a **fully anonymized artifact
link** inside the paper. Strategy at this venue is therefore not "what goes in
the supplement" but **"what earns a place in the only document reviewers are
given"** — and what waits, staged, for the revision window and the camera-ready.

## Triage: the four destinations for every piece of material

| Material | Destination | Why |
|---|---|---|
| Anything a claim depends on (mechanism detail, methodology, headline evidence, overheads) | The 11 pages | Reviewers judge the submission PDF; content elsewhere is invisible at decision time |
| Full config dumps, per-workload result tables, extra sweeps | Anonymized artifact repo, referenced once | Available to the curious without spending pages; not assumed read |
| Experiments anticipating likely objections | Staged, unpublished — ready for the rebuttal/revision window | The 2026 process let authors add evidence in February (`isca-author-response`) |
| Tutorials, extended lineage, code documentation | Post-acceptance artifact and camera-ready pointers | Serves readers and evaluators, not reviewers |

The discipline mirrors tape-out: the submission PDF is the mask set. Everything
else is either supporting collateral or inventory for a later window.

## What the anonymized link may carry — and what it may not

The 2026 guidelines explicitly required artifact links (e.g., repositories) to
be fully anonymized. Practical protocol:

- Host on an anonymization-friendly mirror (anonymous review services or a
  scrubbed repo under a neutral account), never the lab's GitHub organization.
- Scrub the *contents*, not just the URL: commit author fields, README
  affiliations, hardcoded home-directory paths, cluster hostnames, license
  headers with names, CI badges pointing at the real org.
- Reference it once, matter-of-factly ("configurations and per-workload data:
  <link>"), and assume it is **optional** reading — no reviewer obligation to
  open it exists in any verified rule. A claim proved only in the repo is a
  claim the committee never saw.

```bash
# Identity scrub of the anonymous artifact mirror before submission
git -C mirror log --format='%an %ae' | sort -u          # commit identities
grep -rniE 'university|institute|\.edu|corp|@[a-z-]+\.(com|org)' \
     mirror/ --include='*.md' --include='*.txt' | head
grep -rn '/home/\|/Users/\|hostname\|slurm' mirror/ | head
zip -r artifact-mirror.zip mirror/ -x '*.git*'          # if a file drop is used
```

## Fitting evidence into 11 pages without hiding it

When the draft overflows, resist the instinct to exile results tables to the
repo. Compression moves that keep evidence reviewable:

- Collapse per-workload bars into a compact table + one distribution figure;
  keep the outliers visible and named (per `isca-experiments`, outlier honesty
  is credibility).
- Replace a second mechanism diagram with a walk-through that reuses the first.
- Cut background prose before cutting any measurement — architecture reviewers
  forgive terseness; they do not forgive invisible evidence.
- Summarize a sweep with its break points ("benefit holds for T ∈ [4K, 32K],
  collapses below") and put the full curve in the repo.

## The staging shelf: supplementary material in time, not space

ISCA's process gives material a second entry point: the rebuttal/revision window
(three weeks in the 2026 cycle). Maintain a staging shelf from day one:

```text
staging/
  obj-baseline-storage/    # equal-storage comparison vs <rival>, ready to run
  obj-threshold-sweep/     # sensitivity sweep, plotted, unpublished
  obj-os-effects/          # full-system spot-check, half-built
  notes.md                 # for each: trigger objection, cost to finish, owner
```

Rules for the shelf: each item names the objection that would trigger it; each
is runnable inside a week (window math); none contains new-contribution
material — window additions must repair the submitted claim set, not extend it
(`isca-author-response` explains why extension backfires).

## After acceptance: the release ladder

Camera-ready (`isca-camera-ready`) de-anonymizes the artifact link and the AE
process (`isca-artifact-evaluation`) formalizes the package. Sequence the
release: swap the anonymous mirror for the canonical repo; add an archival
snapshot (DOI-issuing service) for the version evaluated; move the shelf's
run-but-unpublished sweeps into the repo's extended-results directory, clearly
versioned against the paper.

## Failure modes specific to this venue's spareness

- **The phantom appendix:** authors trained at appendix-friendly venues put the
  proof-of-overhead in "Appendix A" past page 11 — at ISCA that page either
  violates the format or does not exist; the overhead analysis must be *in*
  the 11 (or its space earned by cuts elsewhere).
- **The revealing repo:** an immaculate PDF and a mirror whose commit log names
  the lab. Sweep contents, not just URLs.
- **The overloaded link:** a reference like "see repository for evaluation
  details" attached to a headline claim — reads as evidence dodging and draws
  exactly the review it fears.
- **The empty promise:** "code will be released upon acceptance" with no link
  at all is weaker than either a clean anonymous mirror or silence; write only
  what is true and checkable.

## Quick triage output

Record the decision for every displaced item so deadline week doesn't relitigate:

```text
[Item] <table/figure/analysis/derivation>
[Claim it supports] <claim id, or "none">
[Destination] 11-pages / anonymized-repo / staging-shelf / post-acceptance
[If repo] identity-swept? yes/no   [If shelf] trigger objection + cost-to-run
[Reviewer impact if invisible] fatal / weakens / none
```

Any item marked "fatal if invisible" that is not in the 11 pages is a layout
bug — fix the budget, not the claim.

Verified format and blinding facts: `../../resources/official-source-map.md`
(2026-07-08). Whether 2027 adds an appendix allowance, a supplement upload, or
different link rules is 待核实 — reread the new guidelines before triaging.
