---
name: icdt-artifact-evaluation
description: Use when preparing the "artifact" of an ICDT (International Conference on Database Theory) paper, which at a pure-theory venue is the complete-proofs full version rather than a code package — covering why ICDT has no ACM-style artifact-badging or code-artifact track, what the marked appendix and the archived arXiv full version must contain, and (only for the rare algorithmic paper) how any code should be handled.
---

# ICDT Artifact Evaluation

Read this to set expectations correctly: **ICDT is a pure database-theory venue with no code-artifact
track and no ACM-style artifact badges.** The role an artifact plays at a systems or empirical venue
— letting an evaluator re-run your result — is played at ICDT by the **complete, checkable proof**:
the marked appendix that a referee reads, and the **archived full version** that carries every proof
for readers after publication. This skill is about making that proof-artifact airtight, not about
Docker images.

> If you arrived expecting the ACM "Available / Functional / Reusable / Reproduced" badges, note that
> those belong to venues like the co-located **EDBT** (systems) or SIGMOD/PODS's ACM track. ICDT
> publishes in **LIPIcs** and evaluates *proofs*. Whether a given EDBT/ICDT edition offers any
> optional artifact/reproducibility recognition for ICDT papers is **待核实** — check the current
> call; the default is none.

## The ICDT "artifact" is the proof

| Systems-venue artifact | ICDT analogue |
|---|---|
| Runnable code + README | Complete proofs in the marked appendix, self-contained in the PDF |
| Reproducibility of numbers | Verifiability of theorems by a competent referee |
| DOI-issued code archive | The LIPIcs paper (DOI on DROPS) + the arXiv full version |
| "Works on a clean machine" | "Checks out under a careful reading" |

Design the proof-artifact so a referee can certify correctness in a bounded reading budget, exactly
as a systems evaluator wants a package that runs in the first ten minutes.

## The marked appendix (the reviewed artifact)

- Contains the **full proofs** for every theorem stated in the body, read at the PC's discretion.
- Is **inside the single submission PDF** — ICDT does not allow online/external appendices, so there
  is no separate artifact upload for review (see `icdt-supplementary`).
- Is **signposted per theorem** so a referee checking one result finds its proof immediately.
- Is **navigable, not a dump** — a 40-page unstructured appendix is as unpersuasive as no proof.

## The full version (the archived artifact)

After acceptance, the enduring "artifact" is the **full version**, typically on **arXiv**:

```text
[Contents]   every theorem with its complete proof; all lemmas, all cases; the constructions in full
[Consistency] identical theorem statements and bounds to the LIPIcs paper — no silent divergence
[Link]        referenced from the camera-ready via \relatedversion (icdt-camera-ready)
[Openness]    arXiv is open access, matching LIPIcs's CC-BY spirit; both are permanent, citable
[Timing]      post/refresh it around camera-ready, after the revision's fixes are folded in
```

The full version is what the community actually reads and builds on; a conference paper whose full
proofs never appear anywhere weakens the result's standing even after acceptance.

## The rare algorithmic paper with code

If your ICDT paper contributes an *algorithm* and you ran an experiment (`icdt-experiments`), you may
choose to share code — but this is optional and not badged:

- Deposit it in a DOI-issuing archive (Zenodo / Software Heritage) for permanence, link it from the
  full version, and license it openly.
- Keep it anonymized for review if you reference it at all; the reviewed object is still the PDF.
- Do not present the code as the contribution — if it were, the paper likely belongs at EDBT/SIGMOD.

## Output format

```text
[Artifact type] proof-artifact (default) / optional code (algorithmic paper)
[Marked appendix] full proofs present, in-PDF, signposted per theorem? yes/no
[Full version] complete-proofs arXiv version, consistent with the paper, linked? yes/no
[Badges] none at ICDT (confirm current call); EDBT/systems path if code is the point
[Fix queue] <complete missing proofs / signpost appendix / post full version>
```
