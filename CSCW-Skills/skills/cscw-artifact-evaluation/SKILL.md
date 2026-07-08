---
name: cscw-artifact-evaluation
description: Use when packaging what stands behind a CSCW paper — systems, analysis pipelines, codebooks, instruments, datasets from real communities — for review-time scrutiny and post-acceptance release, where community-data ethics constrain release more than any badge checklist.
---

# CSCW Artifact Packaging

CSCW has no artifact-evaluation committee stamping badges; the "evaluators" of your
artifacts are the reviewers deciding whether to trust your methods, and later the
researchers and *the studied communities themselves* who encounter the released
materials. That second audience is the venue's distinctive constraint: a CSCW
artifact release is an act with consequences for real people who never signed your
consent form.

## Artifact classes and their release logic

| Artifact | Review-time form | Post-acceptance form | Governing constraint |
| --- | --- | --- | --- |
| Study instruments (guides, surveys) | Anonymized in supplement | Public archive | Institution redaction only |
| Codebooks | Anonymized in supplement | Public archive | Paraphrased exemplars only |
| Analysis code | Anonymized archive | Public repository + DOI archive | Strip identity from history |
| Built systems / prototypes | Screenshots/video + code where feasible | Open source if maintainable | Third-party assets, API keys |
| Trace datasets | Aggregates or synthetic sample | Aggregates; raw only if terms + ethics allow | Platform ToS + re-identification risk |
| Interview/field data | Never | Almost never | Consent scope is absolute |

## The community re-identification test

Before releasing any dataset or exemplar text derived from an online community, run
the adversary exercise — assume a motivated actor (a journalist, a harasser, a
platform admin, a community member with a grudge):

1. **Quote search:** can any released text snippet be pasted into a search engine
   and land on the original post? If yes, paraphrase or drop it.
2. **Join attack:** can released fields (timestamps + community + activity counts)
   be joined against public APIs or archives to recover usernames? Coarsen until
   the join fails.
3. **Small-population exposure:** would identifying *the community* (not any
   member) expose it to raids, deplatforming, or press attention it has not chosen?
   If the community is small or marginalized, community-level anonymity is part of
   the ethical contract — name it only with its agreement.
4. **Future-context check:** platforms change hands and moderation regimes change;
   would this release be safe under a hostile future owner of the platform's data?

Document the outcome in a short release memo; it becomes the honest core of the
paper's data-availability statement (`cscw-reproducibility`).

## Minimum viable released package

```text
release/
├── README.md            # what claims each artifact supports; setup in ≤ 5 steps
├── LICENSE              # code license + data terms, which may differ
├── instruments/         # guides, surveys, recruitment text (redacted)
├── codebook/            # definitions + paraphrased exemplars
├── pipeline/            # collection + analysis code, config, environment spec
├── data/
│   ├── aggregates/      # tables behind each figure
│   └── synthetic/       # optional: structure-preserving fake sample
└── ETHICS.md            # consent scope, what is withheld and WHY, contact path
```

`ETHICS.md` is the CSCW-specific file: it tells reusers what they may *not* do
(re-identify, recontact, join against other datasets) and why the withheld parts
are withheld. A release that explains its own limits earns more trust than a
maximal dump.

## Review-time discipline

- Everything reviewers can open must be anonymous — including git metadata,
  archive paths, and hosting URLs (use anonymized repository services, not a lab
  server whose domain resolves the institution).
- Never put decision-critical evidence *only* in the artifact; the paper must
  stand if a reviewer opens nothing.
- Keep the review package and the eventual public release as separate builds from
  one source tree; the deanonymization diff at acceptance should be mechanical
  (`cscw-camera-ready`).

## Release audit

```text
[Claims map]     each artifact → the claim it supports (no orphan uploads)
[Adversary test] quote-search / join / community-exposure / future-context: pass?
[Consent gate]   every released item inside consent + ToS scope? y/n
[Two builds]     review build anonymous; release build attributed; same tree? y/n
[ETHICS.md]      withholdings explained, reuse limits stated? y/n
```

No CSCW badge program existed at the 2026-07-08 check; if one appears in a future
cycle, its checklist supplements — never replaces — the community-protection tests
above.
