---
name: cikm-supplementary
description: Use when deciding what supporting material accompanies a CIKM submission given budgets that count appendices inside the page limit, structuring the in-PDF appendix versus the anonymously cited artifact, keeping both double-blind, and handling the uncounted GenAI-disclosure and reference sections correctly.
---

# CIKM Supplementary

CIKM 2026 gives supporting material no free rider: every track's budget counts the
appendix **inside** the page limit — 10 pages for full papers, 4/7/4/4 for
short/applied/resource/demo — and only the references (full track: up to 2 pages)
plus the GenAI Usage Disclosure section sit outside it (source map, 2026-07-08).
There is no separate supplementary-upload channel in the verified 2026 calls. The
design question is therefore three-way: costed appendix pages, the anonymously
cited artifact, or cut.

## The three containers

| Container | Costs | Right contents |
|---|---|---|
| Main body | Budget pages | Everything needed to evaluate the claim unaided |
| In-PDF appendix | **Budget pages too** | Only material reviewers must see *during* review that the body cannot hold: a proof, a prompt set, a schema diagram |
| Cited anonymous artifact | Zero pages, but discretionary attention | Configs, full hyperparameter grids, extra per-dataset tables, code, data cards |

Decision rule per candidate item: *must a reviewer see this to score the paper?* If
yes and it is short, appendix — knowing it displaces body content one-for-one. If
yes and it is long, restructure the body so a summary suffices, and put the whole in
the artifact. If no, artifact or delete.

## Building the anonymous artifact

- Host with an anonymity-preserving service (anonymized repository links of the
  usual kind); the URL, commit history, issue templates, CI badges, and README
  must not resolve to authors or institutions.
- Strip notebook metadata, license headers naming people, internal hostnames, and
  data paths like `/home/username/` — the classic leak channels.
- Structure for a ten-minute reviewer visit: a top-level README mapping paper
  section → directory, and one script per headline table. Reviewers sample; make
  the sample they take be the strongest material.
- Reference the artifact from the PDF at the point of relevance ("full grids:
  artifact §3"), not only in a final availability statement, so the pointer is
  found when the question arises.

## What the uncounted sections may and may not carry

The GenAI Usage Disclosure section and the references are outside the budget — and
they are not overflow space. Substantive results, extra experiments, or method
details placed there violate the sections' declared purposes and read as budget
gaming to a panel that sees the trick every year. The disclosure section carries
disclosure; references carry references; nothing else.

## Appendix design rules (for the pages you do spend)

When appendix pages are budget pages, they must earn their cost like body pages:

- Order appendix sections by reference order from the body, and give each a
  one-line purpose header ("A. Prompt templates used in §4.3") — a reviewer
  arriving from a citation should land exactly where sent.
- No orphans: appendix content never referenced from the body is invisible at
  best and budget-waste at worst; either reference it or move it to the artifact.
- Keep appendix tables to the same caption standard as body tables (protocol,
  variance, source); reviewers do not lower standards past the references.
- Never let the appendix complete an incomplete body argument. The body must
  stand alone; the appendix substantiates, it does not continue.

## Reviewer-attention economics

Plan the material split around how attention actually distributes:

| Material location | Realistic reviewer attention | Design consequence |
|---|---|---|
| Body pages 1-2 | Everyone, carefully | The whole argument, compressed |
| Body middle | Everyone, once | Protocol and headline evidence |
| In-PDF appendix | Sometimes, when following a specific doubt | Doubt-resolving material only |
| Artifact README | A minority, for ~10 minutes | Orientation + strongest single script |
| Artifact internals | Rarely, and only if the README earned trust | Completeness, not persuasion |

The split fails when persuasion-critical material sits below its audience's
attention line — which is why "nothing decision-critical lives only in the
artifact" recurs across this pack.

## Worked split: a 13-page full-paper draft

A draft holds 9 pages of core, 2 pages of extra per-dataset tables, 1 page of
prompts, 1 page of proofs. Target: 10 including appendix. Moves: per-dataset tables
→ artifact, keeping one summary row per dataset in the body (saves ~1.7 pages);
prompts → appendix at half a page by showing one template plus deltas, full set →
artifact; proof → appendix, compressed to the lemma statements with the full
derivation in the artifact. Result: 10 pages with the review-critical material
still in the PDF, and nothing decision-relevant living solely in the artifact —
because artifact inspection is at reviewer discretion, never guaranteed.

## Version-consistency discipline

Body, appendix, and artifact are three copies of one experimental truth, and they
drift independently under deadline pressure. Locks that prevent it: generate
paper tables from the same logged results the artifact ships (one source of
numbers, two renderings); when a result updates, update body summary, appendix
table, and artifact data in the same commit; and record in the artifact README
which commit corresponds to the submitted PDF, so a reviewer comparing the two
sees agreement, not archaeology. A number that differs between the PDF and the
artifact is read as sloppiness at best — and at a venue that reserves automated
compliance checking, consistency across submitted surfaces is the cheap kind of
integrity to maintain.

## Pre-upload verification

```text
[ ] Page count with appendix ≤ track budget (measure, don't estimate)
[ ] Artifact URL anonymous end-to-end (open it logged out; check git log)
[ ] Every artifact pointer in the PDF resolves to real content
[ ] GenAI/reference sections carry only their declared content
[ ] Body survives a reviewer who never opens the artifact
```

## Output format

```text
[Budget state] <measured pages incl. appendix vs. track limit>
[Split map] <item → body / appendix / artifact / cut>
[Artifact health] anonymity / README / per-table scripts
[Gaming check] uncounted sections clean?
[Residual risk] <what a no-artifact reviewer would still miss>
```
