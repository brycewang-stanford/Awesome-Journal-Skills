---
name: cikm-artifact-evaluation
description: Use when packaging the code, datasets, knowledge graphs, prompts, and demo systems around a CIKM paper — choosing the artifact form per track (research, applied, resource, demo), meeting the resource track's reuse-and-documentation bar, and staging anonymous review artifacts into citable public releases.
---

# CIKM Artifact Evaluation

CIKM has no verified badge-granting artifact track (2026 lineup: full, short,
applied, resource, demo — source map, 2026-07-08), but artifacts do more work here
than at most venues, because two of the five tracks are *about* artifacts: Resource
papers publish them, and Demonstration papers perform them. This skill covers the
artifact strategy per track and the staging from anonymous review object to public
citable release.

## Artifact role by track

| Track | The artifact is... | Bar it must clear |
|---|---|---|
| Full / Short Research | Supporting evidence, cited anonymously | Regenerates headline results; survives a ten-minute inspection |
| Applied Research | Proof of practice | Substantiates the launch/deployment claim the track requires |
| Resource | **The contribution itself** | Documented, licensed, maintained, adoptable by strangers |
| Demonstration | The thing being demonstrated | Runs live, in front of people, on conference-venue conditions |

## Resource-track packaging bar

A CIKM resource paper is graded on whether others will build on the object. The
verified call names data resources, software, evaluation tasks, and open-source
frameworks. Package accordingly:

- **Provenance and license first**: where the data came from, what consent/terms
  cover it, and a license a university lab and a company can both act on. An
  unlicensed dataset is unadoptable regardless of quality.
- **Schema and statistics**: field-level documentation, size, class balance, known
  gaps — the datasheet discipline, applied without the buzzword.
- **Baselines included**: a resource ships with reference numbers and the scripts
  that produce them, or every adopter re-invents the evaluation differently.
- **Maintenance posture**: versioning scheme, issue channel, and an honest
  statement of how long the hosting is funded. Reviewers of resource papers have
  watched too many datasets rot at dead URLs.
- All of it inside 4 pages (2026) — the paper is the resource's brochure and
  datasheet condensed; depth lives in the repository.

## KG-specific packaging

Knowledge graphs — a CIKM staple — need artifact fields other objects skip: the
dump date of any upstream KG, the extraction queries or rules that produced the
subgraph, entity-resolution decisions (what merged, what split), and per-relation
counts. Two teams "using Wikidata" are usually using different graphs; the artifact
is where that ambiguity dies.

## Demo systems as artifacts

A demo paper's artifact must run where demos actually happen: conference Wi-Fi,
projector resolution, a visitor who types adversarial queries. Package a local
fallback (cached index, canned dataset, offline model), a 90-second scripted tour,
and a reset mechanism that restores clean state between visitors. The 4-page paper
should include the architecture and what a visitor experiences — reviewers accept
demos they can imagine standing in front of.

## Licensing quick guide

License choice is an adoption decision, and CIKM's mixed academic/industry audience
makes it consequential:

| Object | Workable defaults | Watch out for |
|---|---|---|
| Code | MIT/Apache-2.0 for maximum reuse | Copyleft blocks industrial adopters — choose deliberately, not accidentally |
| Original data | CC BY (attribution) or CC BY-NC | NC clauses exclude exactly the applied audience CIKM attracts |
| Derived data (from a KG, a crawl, an API) | Whatever the upstream terms force | Upstream terms propagate: a Wikidata extraction, a scraped corpus, and an API dump each carry different obligations |
| Models/checkpoints | Code license or a stated model license | Base-model license inheritance for fine-tuned checkpoints |

Two failure modes recur in resource-track reviews: no license at all (unadoptable),
and a license the authors had no right to grant because upstream terms forbid
redistribution. Resolve the rights question before the paper claims release.

## Hosting for the decade, not the deadline

CIKM papers become baselines years later (`cikm-reproducibility`), so host on that
horizon: an institutional or platform repository under an organization account
rather than a personal one; an archival deposit with a DOI for the exact
proceedings-version snapshot; dataset hosting with a stated funding horizon rather
than a lab NAS URL. The cheapest insurance is the archival snapshot — it survives
graduations, lab moves, and platform pivots, all of which the venue's older
artifact links have visibly failed to.

## Anonymous-to-public staging

```text
Review stage:  anonymized hosting, no author-resolving URLs/metadata,
               referenced from the PDF where each claim needs it
Acceptance:    real repository public by camera-ready (13-day window in 2026 —
               prepare during the review wait)
Public stage:  license chosen; versioned release tagged to the proceedings
               numbers; archival DOI (e.g., a Zenodo-class deposit) so citation
               outlives the hosting; README linking the ACM DL record
```

The GenAI Usage Disclosure obligation follows the artifact too: generated code,
synthetic data, or AI-produced labels inside the package belong in the paper's
disclosure section (`cikm-reproducibility`).

## Naming and versioning conventions

Give the artifact the paper's short name (the mechanism name from
`cikm-writing-style`), version it semantically with the proceedings snapshot
tagged (e.g., `v1.0-cikm2026`), and keep the README's first line identical to the
paper title so search engines and readers connect the two objects. Post-
publication improvements go in later versions with a changelog; the tagged
snapshot stays frozen because it is what the paper's numbers mean.

## Output format

```text
[Track role] evidence / proof-of-practice / the-contribution / the-performance
[Package state] provenance / license / docs / baselines / maintenance
[KG fields] dump date / extraction / resolution decisions (if applicable)
[Staging] review-anonymous → public-citable, with dates
[Adoption blocker] <the single thing most likely to stop a stranger from using it>
```
