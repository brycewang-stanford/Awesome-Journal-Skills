---
name: itcs-artifact-evaluation
description: Use to adapt the idea of an "artifact" to a pure-theory venue — at ITCS there is no artifact-evaluation track, no code, and no badges; the analogue is making every claim independently verifiable through complete proofs in the submitted PDF and a matching public full version, plus checkable finite objects for any computational content.
---

# ITCS Artifact Evaluation

**ITCS has no artifact-evaluation track.** There are no ACM/IEEE artifact badges, no
Available/Functional/Reusable/Reproduced tiers, no code submission, and no evaluation committee
inspecting a package. It is a **pure-theory** venue: the thing that must be independently
verifiable is the **mathematics**. This skill exists because authors arriving from empirical CS
(where "artifact evaluation" is a real post-acceptance track) need to know what plays that role at
ITCS — and what does *not* apply.

## The ITCS "artifact" is the proof

The artifact that a reviewer inspects is the **argument itself**. Making it "evaluatable" means:

- **Complete proofs of every central claim, inside the submitted PDF** (body sketch + appendix
  full proof). This is the single most important "artifact" obligation and it is enforced at
  submission, not post-acceptance (see [`itcs-submission`](../itcs-submission/SKILL.md) and
  [`itcs-reproducibility`](../itcs-reproducibility/SKILL.md)).
- **Self-contained definitions** so the claims can be verified without your other papers open.
- **Pinned dependencies** — every borrowed theorem cited to a precise statement, so a reviewer can
  audit what you assume versus prove.

There is nothing to "install," nothing to "run," and no badge to earn. The equivalent of a
reproduced result is a reviewer following the proof to the end and agreeing.

## The public full version as the durable, verifiable record

The closest thing ITCS has to an "available artifact" is the **full version on arXiv / ECCC /
IACR ePrint**, which authors are encouraged to post under lightweight double-blind:

- It is the **permanent open record** of the complete argument — the analogue of an archived,
  DOI-bearing artifact, except it is the paper itself, open access, mirrored by LIPIcs on
  acceptance.
- **It does not substitute for proofs in the submitted PDF.** During review the PC judges the
  submission; a central proof that lives only in the preprint counts as absent (see
  [`itcs-supplementary`](../itcs-supplementary/SKILL.md)).
- Keep the preprint and submission **in sync** so the "artifact" a later reader verifies matches
  the one the PC accepted.

## When a paper does have computational content

Occasionally an ITCS paper leans on a small computation — a search that found a gadget, a solver
certifying a finite separation. Make *that* checkable, in the spirit of an artifact but without a
track to submit it to:

- **Include the finite object** (the graph, code, certificate) so verification is a static check,
  not a re-run. A reviewer confirming that a supplied 12-vertex graph has the claimed property is
  the theory analogue of "reproduced."
- **State the search space and the tool/version** so the computation is auditable in principle.
- **Do not host it on a personal repository during review** — that is a lightweight-double-blind
  leak; fold small objects into an appendix (see [`itcs-experiments`](../itcs-experiments/SKILL.md)).

## What does NOT transfer from empirical-CS artifact tracks

| Empirical-CS artifact concept | ITCS reality |
|---|---|
| Available / Functional / Reusable / Reproduced badges | None — no badges exist at ITCS |
| A separate artifact-evaluation committee & deadline | None — the PC judges the proofs at review time |
| Docker image / build script / environment pinning | Irrelevant — there is no code to build |
| "Reproduce the numbers" | Replaced by "follow the proof and agree" |
| Post-acceptance artifact submission | The post-acceptance task is the LIPIcs camera-ready (see itcs-camera-ready) |

## Verifiability checklist (the ITCS "artifact" pass)

```text
[Proofs-in-PDF]   every central claim fully proved inside the submitted PDF? yes/no
[Self-contained]  claims verifiable without the authors' other papers? yes/no
[Dependencies]    borrowed results pinned to precise statements? yes/no
[Full version]    posted (arXiv/ECCC/ePrint) and consistent with the submission? yes/no
[Compute objects] any finite computational witness included and statically checkable? yes/no/NA
[Anonymity]       no personal-repo link exposing identity during review? yes/no
```

## Output format

```text
[ITCS verifiability status] independently-checkable / gaps
[Proof artifact] central claims proved in-PDF? self-contained? dependencies pinned? (yes/no)
[Durable record] full version posted and in sync? yes/no
[Computational witness] finite object included & checkable? yes/no/NA
[Note] there is no badge/track — the deliverable is a checkable proof, not a package
[Fix queue] <ordered; unproved central claims first>
```
