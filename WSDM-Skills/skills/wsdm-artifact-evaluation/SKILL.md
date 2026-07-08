---
name: wsdm-artifact-evaluation
description: Use when packaging code, data, and models as evidence for a WSDM paper - anonymous repositories cited in the PDF, the proprietary-log dilemma of web-scale research, public-benchmark substitution tiers, WSDM Cup datasets, and what credible artifact release looks like at a venue without a formal badge process.
---

# WSDM Artifact Evaluation

Package artifacts for a venue where they are persuasion, not process. The pack
found no formal artifact-evaluation track or badge system for current WSDM
editions (待核实 each cycle) - the CFP-level expectation is the community norm of
"practical yet principled": reviewers reward submissions whose claims a skeptic
could re-derive. That means the artifact's job is to be *inspectable during
review* and *usable after publication*, with no committee to certify it.

## The reviewer-facing artifact

Because appendices count against WSDM's page budget and there is no rebuttal in
which to hand over materials later, the anonymous repository referenced in the
PDF is the only expansion space you get. Build it to be skimmed in ten minutes:

```text
anon-artifact/
├── README.md            # 1 screen: claim -> script -> expected output table
├── LICENSE              # anonymized placeholder license during review
├── env/                 # lockfile or container spec, exact versions
├── data/
│   ├── public/          # download scripts for public benchmarks
│   └── PROPRIETARY.md   # honest statement of what cannot be shared and why
├── src/                 # training/ranking/mining code, no company paths
├── configs/             # one config per reported table row
└── results/
    └── seeds_1-5/       # raw metric dumps behind every table in the paper
```

Anonymity requirements are stricter than habit: fresh remote with no commit
history, no author handles in configs or notebook metadata, no internal package
registries, no dataset paths like `/nfs/companyname/...`. An Associate Chair
can see who you are; your reviewers must not.

## The proprietary-log dilemma

WSDM's core subject matter - query logs, click data, user graphs, ad
interactions - is often legally unshareable. The venue's reviewers know this;
what they punish is *unverifiable* work, not *industrial* work. Choose a rung
and state it explicitly in the paper:

| Rung | What is released | What the paper must then carry |
|---|---|---|
| Full release | Data + code + configs | Just the pointers |
| Sampled/anonymized release | A privacy-scrubbed sample + full code | The scrubbing procedure and how sample results track full-data results |
| Public-benchmark mirror | Code + experiments re-run on public datasets | Both result sets, with the deltas discussed, not hidden |
| Code-only | Pipeline code, no data | Enough dataset statistics that a platform-holder could replicate |
| Nothing sharable | - | A candid limitation; expect a proportional credibility discount |

The public-benchmark mirror rung is the WSDM workhorse: pair the proprietary
result with the same method on public data so at least one full row of the
evidence is end-to-end reproducible by anyone.

## Public substitutes worth knowing

- Standard IR/rec benchmarks with public tooling (MS MARCO, TREC collections,
  MovieLens/Amazon review dumps, KuaiRec-style log releases) - verify current
  licensing before citing a release plan.
- **WSDM Cup datasets**: the conference's own annual challenge (the 2027 site
  already carries a WSDM Cup call) periodically produces real industrial
  datasets; using one signals community alignment. Check the specific cup's
  redistribution terms.
- Graph/social benchmarks (SNAP collections and successors) for the network
  side of the venue.

Anything here can go stale or change license - re-verify at packaging time.

## Model and prompt artifacts

Foundation-model-era WSDM papers ("Search with Foundation Models" is in-scope
per the 2026 CFP) add artifact surfaces older guidance misses:

- Pin model identity precisely: provider, model string, version/date, and
  decoding parameters; an unpinned API model makes results unreproducible by
  construction - say what you did about that (snapshotting outputs, local
  checkpoints, fixed eval windows).
- Ship prompts verbatim in the repository even when the page budget forces the
  paper to summarize them.
- Cache and release model *outputs* used in evaluation when terms permit; that
  lets others audit the judgment layer without paying for inference.

## Credibility signals at a badge-free venue

With no committee stamping artifacts, reviewers use fast proxies to decide
whether the repository is real or decorative. Engineer the proxies:

| Signal | Reads as | Cost to provide |
|---|---|---|
| Config file per reported table row | The numbers came from these runs | Minutes |
| Raw seed-level metric dumps | Variance claims are checkable | Minutes |
| A `make reproduce-table2` entry point | Someone actually reran this | An hour |
| Download script for each public dataset | The pipeline is end-to-end | An hour |
| Honest `PROPRIETARY.md` | The authors know what they cannot prove | Minutes |
| Commit dated one hour before deadline as the only commit | Decorative repo | - avoid |

The last row is about the squeeze: a repository assembled on deadline night
tends to mismatch the paper's numbers, and one mismatch found by a reviewer
discounts the entire artifact. Freeze the repo when experiments freeze
(`wsdm-workflow` sets this at one week out), not when the PDF does.

## Post-acceptance conversion

At camera-ready time the anonymous mirror becomes the citable artifact: move to
the real organization/account, add the actual license, tag the release that
matches the camera-ready numbers, and archive a snapshot (e.g., a DOI-issuing
archive) so the URL in the ACM DL version outlives your CI. Update the README's
claim-to-script table against final camera-ready table numbers - drift between
repo and proceedings is the most common post-publication complaint.

One more conversion detail: if the paper used the public-benchmark-mirror
rung, keep both pipelines in the public repo permanently - the mirror is what
future papers will actually build on, and its issues page becomes your
citation engine.

## Output format

```text
[Artifact tier] full / sampled / public-mirror / code-only / none + stated in paper? 
[Ten-minute test] README claim->script->output table present: yes / no
[Anonymity sweep] history / handles / paths / registries: clean or leaks listed
[FM pins] model string+date+decoding params recorded: yes / no / n-a
[Post-acceptance plan] public home, license, tagged release, archival snapshot
```
