---
name: rss-camera-ready
description: Use when converting an accepted RSS (Robotics: Science and Systems) paper into its public form — de-anonymization and platform-attribution restoration, adding the external links the CFP reserves for this stage, publication in the free roboticsproceedings.org archive with a 10.15607 DOI, and single-track presentation preparation.
---

# RSS Camera Ready

Turn the anonymous accepted version into the archival one. The 2026 camera-ready
deadline was never publicly surfaced (待核实 — take it from the acceptance email);
everything else below is verified venue mechanics as of 2026-07-08.

## What changes at this stage, specifically at RSS

| Submission state | Camera-ready state |
|---|---|
| Anonymous authors | Full author block, affiliations, funding |
| Generic hardware provenance | Restored platform attribution and lab lineage |
| No external links (CFP rule) | Project page, repo, video links welcome |
| Anonymized supplement archive | Public artifact release (`rss-artifact-evaluation`) |
| Reviewed claims | Same claims + accepted clarifications only |

The links row is the venue-specific one: RSS 2026 explicitly deferred all external
linking to the camera-ready, so this is the moment the project page, code repository,
and hosted video enter the paper. Test every link logged-out before submitting the
final PDF.

## Edits that are — and are not — in scope

- **In scope:** corrections promised in the rebuttal, scope-sentence adjustments the
  AC asked for, fixed typos, restored acknowledgements, added links.
- **Out of scope:** new experiments upgrading the claims, retitled contributions, or
  quietly strengthened numbers. The accepted paper is what the AC meeting endorsed;
  divergence beyond clarification is an integrity problem, not a formatting one.
- Keep section, table, and figure numbering stable where possible so the review
  record still maps onto the final text.

## Publication mechanics

- RSS proceedings appear at **roboticsproceedings.org** — free to read, no author
  fee, no paywall — with DOIs of the form `10.15607/RSS.<year>.<vol>.<paper>`. Verify
  your final metadata (title capitalization, author order, affiliations) exactly as
  it should be archived; the volume page is what dblp and citation indices ingest.
- There is no APC anywhere in this pipeline; the cost model is conference
  registration. Whether at least one author must register/present in person was not
  publicly verified for 2026 (待核实 against the acceptance email).

## The single-track presentation

Acceptance at RSS means presenting to the *entire* conference, not a parallel-session
slice — the preparation bar is accordingly higher:

1. Build the talk for the distant-subfield attendee: one slide establishing why your
   problem matters outside your niche, before any method detail.
2. Show real footage early; a single uncut clip buys more belief than an
   architecture diagram.
3. Rehearse the failure question — "when does it break?" is the most common
   single-track question, and your failure table is the prepared answer.
4. Poster/spotlight mechanics vary per edition (待核实 in author instructions);
   prepare the poster to carry the trial evidence the talk compresses away.

## Archive-metadata proof pass

The roboticsproceedings.org volume page is the record dblp, Google Scholar, and
citation managers will ingest — proof it like a legal document:

- Author name forms consistent with each author's existing publication record
  (initials vs full names decide whether citation graphs merge or fork).
- Title capitalization and any math/Unicode rendered as intended.
- Affiliations current at publication time, not at submission time.
- Funding acknowledgements exactly as grant terms require.
- The `10.15607/RSS.*` DOI, once minted, is what belongs in your CV and repo
  citation file — point the repository's citation entry at the proceedings page,
  not at the arXiv mirror.

## Between acceptance and Sydney: an ordered runway

Eleven weeks separated the 2026 decision (April 27) from conference week (July
13-17). A workable ordering:

| Weeks after decision | Action |
|---|---|
| 0-1 | Extract acceptance-email requirements; calendar the camera-ready date |
| 1-3 | Final PDF edits (clarifications only) + de-anonymization sweep |
| 1-4 | Visa and travel booking — the long pole for many teams |
| 3-6 | Public artifact release built and tested (`rss-artifact-evaluation`) |
| 6-9 | Talk drafted and rehearsed against the whole-audience test |
| 9-11 | Poster printed; footage loaded locally; links re-tested logged-out |

## Final-pass checklist

```text
[ ] Acceptance-email requirements extracted (deadline, format, forms) — sole source
[ ] Author block, funding, acknowledgements restored
[ ] Platform attribution un-anonymized; self-citations re-personalized
[ ] Links added and tested logged-out: repo / project page / video
[ ] Claims diff vs accepted version = clarifications only
[ ] Metadata proofread as-it-will-be-archived
[ ] Public artifact release live before the conference talk drives traffic to it
```

## Hedged logistics (all 待核实 per cycle)

- Camera-ready deadline, template version, and any form uploads: sole source is the
  acceptance email plus the author-instructions page it links.
- Registration classes, pricing, and whether a paper requires a specific class or
  in-person presenter: verify on the current registration page.
- Copyright/consent mechanics for the proceedings: RSS's open-access model differs
  from IEEE-style transfer flows — do not assume either shape; read the form sent.
- Talk length, spotlight-vs-poster split, and session assignment: published with
  the program, not the acceptance email; recheck close to conference week.

## Output format

```text
[Camera-ready status] blocked / in progress / submitted
[Sole-source items] <from acceptance email: deadline, forms>
[Diff audit] clarifications only / out-of-scope edits found
[Link check] <url -> ok/broken>
[Presentation prep] whole-audience slide / footage / failure answer
```
