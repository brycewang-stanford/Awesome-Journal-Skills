---
name: facct-related-work
description: Use when positioning an ACM FAccT submission across its many disciplinary lanes — algorithmic fairness/ML, HCI, law and policy, STS and critical theory, and prior FAccT/FAT* proceedings — writing delta-first contrast that a mixed reviewer pool will accept, citing borrowed constructs to their real origin, keeping self-citations mutually anonymous, and declaring overlap with workshops, preprints, and prior versions.
---

# FAccT Related Work

Use this to audit novelty and disciplinary reach. FAccT reviewers come from **different fields**,
and each expects to see the nearest work **in their lane** engaged. A fairness-metrics reviewer
wants the ML fairness literature; a legal reviewer wants the relevant law and governance work; an
STS/critical reviewer wants the theory you are (often implicitly) drawing on. The fastest way to
lose a mixed panel is a bibliography that is deep in one field and blank in the others. Reopen the
current CFP for anonymity, dual-submission, and prior-publication rules before advising.

## Positioning checks

- **Name the FAccT novelty precisely.** What is new: a fairness/transparency method, an empirical
  harm nobody had measured, an accountability framework, a reframing of a taken-for-granted
  construct, a qualitative account of an affected community, or a legal-technical synthesis?
- **Cover the disciplinary lanes** (see table). A paper that cites only its home field reads as
  unaware of the interdisciplinary conversation FAccT exists to host.
- **Write delta-first.** Each closely related work gets one sentence naming what it did and one
  naming what you do differently — across the divide where relevant ("the ML work optimized the
  metric; the legal work named the right; we connect them by...").
- **Cite borrowed constructs to their real origin.** If you use "disparate impact," "contestability,"
  "situated knowledge," or "the right to explanation," cite the field that coined it, not a
  second-hand ML paper — mixed reviewers notice mis-attribution instantly.
- **Preserve mutual anonymity.** Cite your own prior work in the third person; never link reviewers
  to an identity-revealing preprint, repository, project page, or the arXiv version of this paper.
- **Declare overlap** with a prior workshop/CRAFT version or concurrent submission; do not re-submit
  archival work as new.

## FAccT literature lanes

| Lane | Typical venues / bodies | What FAccT reviewers check |
|---|---|---|
| Algorithmic fairness & ML | FAccT, NeurIPS/ICML/ICLR, JMLR | Whether the nearest fairness measure/method is compared or distinguished |
| HCI & human factors | CHI, CSCW | Whether prior work on how people use/contest the system is credited |
| Law, policy & governance | Law reviews, policy journals, regulation | Whether the relevant legal doctrine or regulatory instrument is engaged correctly |
| STS & critical theory | STS venues, critical data/algorithm studies | Whether the theoretical lineage of your critique is named, not just gestured at |
| Documentation & accountability infra | Prior FAccT (datasheets, model cards, audits) | Whether existing documentation/audit frameworks are built on rather than reinvented |
| Domain literature (health, credit, hiring...) | The applied field | Whether you understand the real decision context you study |

A bibliography that reaches across at least the lanes your claim touches signals command of the
interdisciplinary field; one confined to a single lane invites the "unaware of the neighbor
discipline" critique that a mixed panel is unusually well-positioned to make.

## Delta-first positioning vignette

Suppose the paper proposes a **contestability mechanism** for automated benefit decisions. Its
neighbors span lanes: an ML paper on algorithmic recourse (technique, no institutional grounding),
an HCI study of how claimants experience appeals (experience, no mechanism), and legal scholarship
on due-process rights in automated administration (the right, no system). The novelty sentence names
all three contrasts — a *mechanism* where recourse gave only a technique, grounded in the *appeal
experience* HCI documented, realizing the *due-process right* the law names — which is exactly the
cross-lane synthesis FAccT rewards.

## Concurrent and prior-version judgment calls

```text
[Concurrent arXiv work]   cite neutrally, state the difference, avoid unverifiable priority claims;
                          keep the citation mutually anonymous
[Your workshop/CRAFT version]  usually non-archival and citable, but confirm against the current CFP
                          and phrase so anonymity survives
[Prior short/position version] declare the overlap and state what the full paper adds beyond it
[Archival status unclear]  declare the overlap in the submission form rather than guessing
```

## Eligibility red flags

- Substantial text overlap with a published paper by the same authors (self-plagiarism risk).
- A "new" audit that re-reports a prior dataset's disparities without a new question or population.
- Citations confined to one discipline while the paper claims interdisciplinary contribution — the
  clearest signal that the interdisciplinarity is a label, not a method.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Lanes covered] <ML-fairness / HCI / law-policy / STS-critical / documentation / domain>
[Nearest 3 works] <work -> one-line cross-lane delta>
[Construct attribution] <borrowed term -> cited to its real origin? yes/no>
[Archival-overlap risk] <none / declare: what>
[Novelty sentence] <FAccT-ready contribution contrast across the relevant lanes>
```
