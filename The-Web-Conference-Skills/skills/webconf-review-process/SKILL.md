---
name: webconf-review-process
description: Use when reasoning about how the Web Conference (WWW) evaluates papers — track-scoped double-blind review, the rebuttal-to-notification pipeline, how the ten research tracks shape reviewer expectations, main versus companion proceedings outcomes, and what authors can and cannot influence at each stage.
---

# Web Conference Review Process

The Web Conference reviews papers **inside topical tracks**, and that single design
choice explains most of what authors experience: who reviews the paper, what
evidence bar applies, and why two similar papers can meet very different fates in
the same year. This skill models the pipeline as verified for the 2026 edition;
per-track reviewer counts, scoring scales, and meta-review mechanics were not
published in verifiable sources and are marked 待核实 where they matter.

## Pipeline with 2026 anchors

| Stage | 2026 date | Author-controllable? |
|---|---|---|
| Abstract registration | Sep 30, 2025 | Fully — track, title, final author list |
| Full paper | Oct 7, 2025 | Fully |
| Track review period | Oct-Nov 2025 | Not at all |
| Rebuttal window | Nov 24 - Dec 1, 2025 | The one mid-process lever |
| Track-chair / PC deliberation | Dec 2025 - Jan 2026 | Not at all |
| Notification | Jan 13, 2026 | — |
| Camera-ready | Jan 25, 2026 | Fully |

Between December 1 and January 13 there is nothing an author can legitimately do.
Emailing chairs with clarifications or new results during deliberation is at best
ignored and at worst remembered.

## What track scoping means for your reviews

Each of the ten research tracks (from "Graph algorithms and modeling for the Web"
to "Responsible Web" to "Systems and infrastructure for Web, mobile, and WoT")
recruits its own expert pool via its track chairs. Consequences worth planning for:

- **The bar is track-local.** "Search and retrieval-augmented AI" reviewers expect
  ablations against current retrieval baselines; "Economics, online markets and
  human computation" reviewers expect incentive or welfare reasoning. The same
  recommendation-systems paper is a methods paper in one track and a measurement
  paper in another.
- **Misrouting is a review-quality event, not just a fit event.** A misrouted paper
  is reviewed by people missing the context to appreciate it, and there is no
  verified mechanism for authors to move a paper between tracks after the deadline.
- **Interdisciplinarity cuts both ways.** The venue's identity is computing plus
  social science plus economics; a track can staff a mixed panel, so a paper should
  be legible to a smart adjacent reader — define constructs, don't lean on
  subcommunity jargon for load-bearing claims.

## The venue's recurring decision logic

Reviews at this venue orbit four recurring questions; strong submissions answer
all four in the first two pages (see `webconf-writing-style`):

1. Is the problem *of the Web* — would it exist without platform structure, open
   hypertext, adversarial content, or live user behavior?
2. Is the evidence at a scale and realism the claim requires?
3. Is the method or finding reusable beyond the studied platform or dataset?
4. Are harms, ethics, and data provenance handled at the standard the "Responsible
   Web" era expects, whatever the track?

A paper failing question 1 collects the venue's signature phrase — "better suited
to a specialized venue" — regardless of technical quality.

## Confidentiality and integrity

Double-blind runs in both directions: authors must not attempt reviewer
identification or contact, and reviewer materials are confidential permanently, not
just until notification. The 2026 CFP's LLM clause also has a review-side face:
policies on machine-generated reviews are set per edition and were not verifiable
for 2026 — if you review, check the current reviewer instructions before using any
AI assistance, and as an author do not assume LLM-written reviews are contestable
on that basis alone.

## Translating review language

Track panels at this venue have recognizable dialect; decode before reacting:

- *"The technical contribution is limited"* from an in-track expert usually means
  "the delta over the sibling-circuit baseline I have in mind is small" — find
  and name that baseline in the rebuttal rather than defending novelty abstractly.
- *"The paper would benefit from evaluation on real-world data"* almost always
  means provenance, not size: the datasets used look synthetic, stale, or
  undocumented (see `webconf-experiments` on freshness as evidence).
- *"The societal implications deserve more discussion"* is rarely a request for a
  philosophy section; it asks for the two concrete sentences on harms, consent,
  and aggregation that belong beside the data description.
- *"Better suited to a specialized venue"* is the web-fit failure; it is nearly
  unrecoverable in rebuttal unless the web-native mechanism genuinely exists in
  the paper and merely went unstated — in which case quote it by page and line.
- *"I am not an expert in this specific area"* in a low-confidence review is
  routing information for *you*: the track pool did not contain your reader, which
  is evidence about track choice for the resubmission.

## Reading the outcome

```text
Accept (research tracks)  -> main proceedings, 12-page/8-content budget,
                             registration + presentation obligations attach
Reject                    -> full re-submission somewhere; reviews travel with
                             you informally (reviewer pools overlap with WSDM/
                             CIKM/SIGIR), so fix rather than re-roll
No verified middle states -> the 2026 sources showed no conditional-accept or
                             revise-and-resubmit lane for research tracks (待核实
                             before assuming one exists in your cycle)
```

After a rejection, the highest-information artifact is the *agreement structure*
across reviews: three reviewers converging on evidence-scale doubts is a
`webconf-experiments` problem; divergent reviews with one champion is often a
framing problem (`webconf-writing-style`), and a routing error is a
`webconf-topic-selection` problem for the next cycle.

One structural note for expectation-setting: the notification is a single
decision on a single date (January 13 in the 2026 cycle) — the sources showed no
staged early-reject or two-phase review for the research tracks, unlike some ML
flagships. Plan emotionally and logistically for one verdict, fifteen weeks
after the abstract.

## Output format

```text
[Stage] <where the paper sits in the pipeline>
[Track lens] <what this track's pool predictably asks>
[Four questions] web-native? / evidence scale? / reusability? / responsibility?
[Actionable now] <the only levers currently open to the authors>
[待核实 items] <per-cycle mechanics to confirm on official pages>
```
