---
name: webconf-artifact-evaluation
description: Use when packaging datasets, models, or code for the Web Conference (WWW) Artifacts Available badge or for reviewer scrutiny, covering archival-repository choice, the light-verification bar, web-data licensing and takedown realities, anonymized artifacts during review, and what the badge does and does not certify.
---

# Web Conference Artifact Evaluation

The Web Conference's 2026 artifact program was an **availability badge, not a
reproducibility audit**: a volunteer committee performed a light verification that
the artifact exists, is downloadable from a publicly accessible *archival*
repository, and carries minimal instructions. Accepted papers from all tracks of
the main or companion proceedings — except workshop papers — could apply, with the
artifact submitted at camera-ready time. Design the artifact to clear that bar
first, then exceed it for your actual readers.

## What the badge checks vs. what readers need

| Dimension | Badge bar (2026) | Reader bar |
|---|---|---|
| Location | Public archival repository | Same, plus a mirror for big files |
| Persistence | Link resolves at check time | DOI/versioned, survives repo moves |
| Instructions | "Minimal" access instructions | Environment, run commands, expected output |
| Completeness | Artifact "exists" | Enough to regenerate headline tables |
| Legality | Not assessed | Licenses and platform ToS actually permit sharing |

"Archival" is the operative word: a personal GitHub repository can be deleted or
rewritten and historically has *not* counted as archival for ACM badging purposes.
Deposit a release snapshot in Zenodo, figshare, or an institutional repository that
mints DOIs, and let GitHub be the development mirror the README points to.

## Web-data artifacts are legally different

This venue's artifacts are dominated by crawls, platform datasets, interaction
logs, and derived embeddings — objects with third-party rights attached. Decide the
sharing tier per component *before* promising anything in the paper:

1. **Freely shareable**: your code, your synthetic data, aggregate statistics.
2. **Shareable as derivatives**: URL lists, item IDs, hydration scripts — release
   the *pointers* plus the pipeline, not the content, when platform terms forbid
   redistribution (the standard pattern for social-media datasets).
3. **Shareable on request / gated**: user-level data behind a data-use agreement;
   document the request path in the README so the artifact is still "available."
4. **Not shareable**: proprietary logs. Say so in the paper's availability
   statement and ship the measurement code anyway.

A takedown-resilient design states the crawl window, preserves checksums of the
original corpus, and includes the re-crawl script — so when 15% of URLs die (they
will), a later user can quantify exactly what changed.

## Minimum viable package

```text
artifact-v1.0/  (deposited at Zenodo, DOI 10.5281/zenodo.XXXXXXX)
├── README.md          # what this is, paper title, 3-command quickstart
├── LICENSE            # code license + per-dataset terms table
├── environment.yml    # or Dockerfile / requirements.txt with pins
├── data/
│   ├── MANIFEST.md    # per-file: source, crawl window, row counts, sha256
│   └── ids/           # hydration pointers where content can't ship
├── src/               # training/analysis code, seeds surfaced as flags
├── scripts/
│   ├── reproduce_table2.sh
│   └── recrawl.py     # dead-link accounting for future users
└── CITATION.cff
```

The single highest-leverage file is `reproduce_table2.sh` — one command per
headline result. Badge reviewers may not run it; the citing researcher eighteen
months later definitely will.

## During review vs. after acceptance

Review at this venue is double-blind and the appendix is the sanctioned home for
reproducibility detail, so during review the artifact appears as an *anonymized*
link (if at all) with no author-identifying paths, git history, or platform account
names. After acceptance, the flow inverts: mint the DOI first, cite it in the
camera-ready, then file the badge application alongside the final files — the
badge's availability check needs the link that will live in the published paper.
Sequence details sit in `webconf-camera-ready`; content standards for what the
package proves sit in `webconf-reproducibility`.

## Vignette: the crawl that got a takedown notice

A team releases a 40M-page news crawl with their WWW paper. Eight months later, a
publisher demands removal of its articles. Because the artifact followed the
tiered design, the response costs an afternoon, not the artifact: the Zenodo
deposit v1.1 removes the publisher's content files, the manifest documents the
removal (URLs retained as pointers, checksums preserved), the hydration script
still lets rights-holding users rebuild the full corpus, and the paper's DOI
citation now resolves to a version history that explains itself. The
counterfactual design — one monolithic tarball with raw content — would have
forced a full withdrawal and orphaned every downstream citation. Design for the
takedown on day one; on the Web it is a *when*, not an *if*.

## Badge application dry run

Before filing with the camera-ready, simulate the committee's light check from a
clean machine and a logged-out browser:

1. The link in the paper resolves to the archival record (not a login page, not a
   personal homepage redirect).
2. The record shows a version, a license, and a README visible without download.
3. One file downloads successfully and matches its manifest checksum.
4. The README's first screen states what the artifact is and which paper it
   accompanies — the committee volunteer decides in minutes.

## Honest labeling

The Artifacts Available badge certifies existence, not correctness. Do not write
"our results are independently verified" on the strength of it. Conversely, an
artifact too encumbered to badge (tier 3-4 data) does not bar publication — the
paper just needs an availability statement that says precisely what is released,
what is gated and why, and what a reader can still verify with the released parts.

## Output format

```text
[Artifact tiering] code=<tier> data=<tiers per set> models=<tier>
[Badge eligibility] track eligible? archival deposit? DOI minted?
[Legal check] platform ToS / license conflicts found: <list or none>
[Decay plan] crawl window stated? checksums? recrawl script?
[One-command repro] present for headline tables: yes/no
[Availability statement] drafted for the paper: yes/no
```
