---
name: lang-workflow
description: Use when starting or navigating any manuscript aimed at Language (Linguistic Society of America) and unsure which skill applies — it reads your stage and piece type (General Research Article, Research Report, Review Article, Discussion Note, or an online-only section: Perspectives, Phonological Analysis, Language and Public Policy, Teaching Linguistics) and routes you to the matching sub-skill. It dispatches; it does not draft analysis.
---

# Language Workflow Router (lang-workflow)

The orchestrator for a submission to *Language*, the flagship journal of the Linguistic Society of
America (LSA), published continuously since 1925 and, from January 2026, by **Cambridge University
Press** (fully open access from Volume 102). *Language* takes work from **every subfield** — phonology,
phonetics, syntax, semantics, morphology, historical and typological linguistics, sociolinguistics,
psycholinguistics, and computational linguistics — and judges each by the standards of its own
tradition while demanding one thing across the board: a **theoretically grounded claim carried by
rigorous linguistic evidence**, legible to a general linguistics readership, not to one framework's
insiders.

## When to trigger

- Starting a new *Language* manuscript and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding whether the work is a full **General Research Article** or a shorter **Research Report**
- Considering an online-only section (Perspectives / Phonological Analysis / Language and Public
  Policy / Teaching Linguistics)
- Returning with a decision letter (route to `lang-rebuttal`)

## First question: which piece type?

| Situation | Piece type | Route to |
|-----------|-----------|----------|
| In-depth study advancing linguistic theory for a general audience | **General Research Article** (≤18,000 words incl. notes/tables/appendices, excl. references) | full pipeline below |
| Smaller, sharply targeted empirical or analytic contribution | **Research Report** | `lang-topic-selection` → compressed pipeline |
| State-of-the-art synthesis of a research area (≤5,000 words) | **Review Article** | `lang-literature-positioning` → `lang-writing-style` |
| Comment on a published *Language* piece / a focused analytic point | **Discussion Note** | `lang-literature-positioning` + `lang-rebuttal` |
| Field-shaping thesis inviting responses | **Perspectives** (target article + Commentaries + Rejoinder) | `lang-theory-building` + `lang-rebuttal` |
| Pedagogy analysis / policy application | **Teaching Linguistics** / **Language and Public Policy** (online-only) | `lang-topic-selection` |

> A General Research Article over **12,000 words** is held to a more stringent standard — length must
> be earned. Confirm current section rules in `lang-submission`.

## Routing map (stage → skill)

```text
Idea / fit for Language?            → lang-topic-selection
What is the theoretical claim?      → lang-theory-building
In dialogue with which literature?  → lang-literature-positioning
Is the design/data defensible?      → lang-research-design
Are the analyses sound?             → lang-data-analysis
Data + annotation transparent?      → lang-data-and-transparency
Are examples/exhibits clean?        → lang-tables-figures
Does it read across frameworks?     → lang-writing-style
Ready for ScholarOne?               → lang-submission
How will it be judged?              → lang-review-process
Got an R&R / writing a Rejoinder?   → lang-rebuttal
```

## Default order

`topic-selection → theory-building → literature-positioning → research-design → data-analysis →
data-and-transparency → tables-figures → writing-style → submission → review-process → rebuttal`

Iterate: *Language* papers typically loop **theory ↔ data ↔ analysis** several times — the account
that explains the pattern usually sharpens after the data are in hand, not before.

## Calibration anchors (what a Language trajectory feels like)

Orienting heuristics, not editorial guarantees; confirm volatile specifics on the current author pages.

- **Evidence-first, framework-fluent.** The router never rewards a formalism for its own sake. A clean
  analysis in one theory that ignores rival accounts is routed back to `lang-theory-building`; a pile
  of glossed data with no claim is routed to `lang-topic-selection`.
- **Cross-subfield legibility.** Reviewers may sit outside your subfield. The router prioritizes making
  the stakes and the data readable to a syntactician *and* a sociolinguist, not only to specialists.

## Stage-to-symptom dispatch (route on the complaint, not the calendar)

| The author says… | Route to |
|------------------|----------|
| "Reviewer 2 says it's just description." | `lang-theory-building` |
| "It feels too narrow for the flagship." | `lang-topic-selection` |
| "They said I ignored the competing framework." | `lang-literature-positioning` |
| "The data can't bear the generalization." | `lang-research-design` |
| "Reviewer doubts my statistics." | `lang-data-analysis` |
| "Glosses and examples are a mess." | `lang-tables-figures` |
| "Desk-returned before review." | `lang-review-process` then `lang-submission` |

## Worked micro-example (illustrative)

A study of an understudied Bantu tone alternation opens the router unsure where to begin. The glossed
data are rich but the contribution reads as "language X does this," so the router sends it to
`lang-topic-selection`, then `lang-theory-building` to state what the alternation is a *case of* (an
illustrative claim about the phonology–morphology interface), then `lang-research-design` to defend the
elicitation and consultant sampling, looping theory↔data twice. At an illustrative 14,000 words it is a
full General Research Article — but every section must earn its place under the more-stringent bar past
12,000 words.

## Anti-patterns

- Treating *Language* like a subfield venue — the claim must read across linguistics, not one framework
- Submitting a **descriptive data dump** with no theoretical stakes (a classic desk return)
- **Single-framework parochialism** — analyzing only inside one formalism and ignoring rivals
- Assuming a generic style — *Language* uses the **Language Style Sheet** and **Leipzig glossing**
- Quantitative claims with no proper modeling or shared data (route to `lang-data-analysis`)
- Routing as if acceptance were quick; a substantive R&R is the normal first-round outcome

## Output format

```
【Stage】idea / theory / positioning / design / analysis / transparency / exhibits / writing / submit / review / rebut
【Type】General Research Article / Research Report / Review Article / Discussion Note / Perspectives / Teaching Linguistics / Language & Public Policy
【Route to】lang-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — linguistics data + software by subfield
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official LSA/CUP URLs behind every fact in this pack
