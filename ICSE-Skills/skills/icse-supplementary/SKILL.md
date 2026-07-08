---
name: icse-supplementary
description: Use when deciding what goes into the 10-page body versus the replication package of an ICSE research-track submission, covering the no-unlimited-appendix page model, anonymized supplementary links and HotCRP uploads, package organization for reviewer navigation, and content-placement rules that protect the review.
---

# ICSE Supplementary Material

ICSE's page model is stricter than most authors coming from ML venues expect,
and it inverts their packing instincts. The 2027 research-track format (read
2026-07-08): main text ≤ 10 pages **inclusive of all figures, tables, and
appendices**, plus up to 2 pages of references only. There is no unlimited
in-PDF appendix. Everything else travels as supplementary material — an
anonymized link in the paper or an upload via HotCRP — and must be assumed
optional reading.

## The placement rule

One question decides placement: **must a reviewer see it to score the paper?**

| Content | Placement | Why |
|---|---|---|
| Anything a criterion score depends on: RQ answers, key tables, protocol essentials, the threat analysis | The 10 pages | Optional material cannot carry mandatory weight |
| Full prompt templates, extended proofs, extra result tables, per-subject breakdowns | Package, *summarized* in-body | Body states the finding + pointer; package holds the mass |
| Tool source, benchmark, scripts, raw outputs | Replication package | This is the verifiability substrate (`icse-reproducibility`) |
| Interview guides, codebooks, instruments | Package, named in the availability statement | Reviewers audit method through them when they choose to |
| Demo video, screenshots gallery | Package, only if genuinely clarifying | Never as a substitute for a precise in-body description |

The failure mode is *load-bearing supplement*: "due to space, the evaluation
methodology is described in the supplementary material" invites the reviewer
to score what the body shows — an unevidenced claim. Compress into the body
instead: a protocol table instead of two prose pages, a summary row instead
of the full matrix.

## Summarize-and-point discipline

Every relocation leaves a residue in the body — the conclusion plus a precise
pointer:

> Patches for all 214 bugs, with per-bug generation logs, are in the package
> (`results/patches/`); Table 5 reports the aggregate. The full 41-item
> codebook is in `codebook.pdf`; Table 2 shows the 6 categories with ≥10%
> prevalence.

Precise pointers (directory, file, section of the package README) also pay
forward: they become the artifact-evaluation roadmap after acceptance.

## Package layout reviewers can navigate in five minutes

```text
replication-package/
├── README.md            # map: claim/table/figure -> command -> output
├── REQUIREMENTS.md      # env: versions, container digest, hardware, runtime
├── LICENSE              # open license even at review time (anonymized holder)
├── code/                # tool source, pinned dependencies
├── benchmark/           # subjects or fetch-scripts with SHAs + mining date
├── scripts/             # one entry point per paper table/figure:
│   ├── run_rq1.sh       #   names match the RQs, not internal jargon
│   └── make_table3.py
├── results/             # raw outputs the paper's numbers derive from
└── appendix.pdf         # extended tables/proofs that did not fit the body
```

The README's first section is a **claims map**: each headline claim, the
command that regenerates its evidence, expected runtime, and expected output.
A reviewer who checks one row and succeeds extends trust to the rest; one who
hits a broken path on the first try generalizes that, too.

## Anonymity of the archive

The supplement must hold the same double-anonymous line as the paper:
`git archive` exports (no history), scrubbed notebook metadata, no
`/home/username/` paths in configs or logs, no institutional hostnames, no
author names in `LICENSE`/`setup.py`/`CITATION` files, hosting through an
anonymizing service rather than a personal account. Scrub, then *re-run the
entry-point scripts* — anonymization that breaks paths converts your evidence
into a liability.

## What must stay out of the package

Screening for exclusions is as important as packing inclusions: third-party
code or datasets whose licenses forbid redistribution (link with pinned
fetch-scripts instead); human-subjects raw data beyond what consent covers
— transcripts, recordings, un-aggregated survey rows; credentials, API
keys, and internal hostnames hiding in config files and CI logs; and
proprietary industrial code shown to you under NDA, even in fragments
quoted in comments. A replication package is a publication: it gets the
same legal and ethical review as the paper, and a leak in the supplement is
harder to retract than a sentence.

## Size and dependency realism

No supplement size cap was verifiable for 2027 (待核实 on the live HotCRP
form), so engineer for reviewer patience instead: keep the download small
(fetch-scripts for large corpora, with checksums), keep the smoke test under
minutes on a laptop, and never require credentials, cluster schedulers, or
paid API keys for at least a reduced-scale verification path. Provide cached
outputs beside every expensive step so the analysis chain can be verified
without the compute.

## Reverify each cycle

The 10+2 model, the HotCRP supplementary option, and the availability-
statement placement are 2027-cycle facts; page models have changed across
ICSE editions before. Confirm the current call before deciding any placement
that would be expensive to reverse in deadline week.

## Output format

```text
[Body/package split] each relocated item -> residue sentence + pointer present?
[Load-bearing check] any criterion-relevant content living only in the package? (must be none)
[Package audit] layout roles present; claims map covers every headline number
[Anonymity + runnability] scrub done; entry points re-run post-scrub
[Reviewer path] smoke test minutes, laptop-feasible, credential-free
```
