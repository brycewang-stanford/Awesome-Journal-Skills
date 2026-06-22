---
name: hlr-workflow
description: Use when starting or navigating any Harvard Law Review (HLR) article, essay, or book review and you need the right next sub-skill. Routes by lifecycle stage and the distinctive student-edited, multi-submit/expedite law-review process. It dispatches; it does not draft content.
---

# HLR Workflow Router (hlr-workflow)

The orchestrator for a Harvard Law Review submission. HLR is **student-edited, not peer-reviewed**, and
generalist across all of law. The router's first job is to set the right mental model: you write a
**near-final** article, run a **preemption check** before drafting, submit broadly across peer journals
via **Scholastica** (but to **HLR through its own submission system**, not Scholastica), leverage offers
with **expedite** requests, and then survive an intensive
student-editor edit plus a full **cite-check / source-pull**. Figure out the stage, then dispatch.

## When to trigger

- Starting a new HLR piece and unsure where to begin
- Mid-project and unsure which skill applies next
- Deciding the piece type (Article, Essay, Book Review, or a Supreme Court Foreword/Comment by invitation)
- Holding an offer and deciding whether/how to expedite (route to `hlr-placement-strategy`)
- An editor sent edits or a source-pull request (route to `hlr-student-editor-review`)

## First question: which piece type?

| Situation | Type | Route to |
|-----------|------|----------|
| Full original legal argument, novel normative claim | **Article** (long, heavily footnoted) | normal pipeline below |
| Shorter, focused intervention or provocation | **Essay** | normal pipeline, tighter scope |
| Engaging a recent book to make an independent claim | **Book Review** | `hlr-thesis-and-contribution` + `hlr-argument-structure` |
| Invited Supreme Court **Foreword** / Comment / Term piece | **Supreme Court issue** | `hlr-argument-structure` + `hlr-sources-and-bluebook` (invitation-driven) |

> Notes are **student-written and unsigned** by HLR editors — not an outside-author track. If you are
> not an HLR editor, you are writing an Article, Essay, or Book Review.

## Routing map (stage → skill)

```text
Is the topic timely and placeable?   → hlr-topic-selection
What is the legal claim / payoff?     → hlr-thesis-and-contribution
Has this argument been made already?  → hlr-preemption-check
How is the argument built?            → hlr-argument-structure
Are authorities cited correctly?      → hlr-sources-and-bluebook
Is the footnote apparatus sound?      → hlr-footnotes-and-cite-check
Does the prose read like a law review?→ hlr-writing-style
Where and when do I submit/expedite?  → hlr-placement-strategy
Ready to upload (HLR's own system)?   → hlr-submission
Editor sent edits / source-pull?      → hlr-student-editor-review
Working through the edit cycle?        → hlr-revision-and-editing
```

## Default order

`topic-selection → thesis-and-contribution → preemption-check → argument-structure →
sources-and-bluebook → footnotes-and-cite-check → writing-style → placement-strategy → submission →
student-editor-review → revision-and-editing`

> Run the **preemption check early** — discovering your claim was already made *after* drafting is the
> classic wasted-summer failure. Iterate thesis ↔ argument ↔ sources before polishing prose.

## Law-review reality check (force this before routing)

| Check | Pass condition | Route if weak |
|-------|----------------|---------------|
| Student-edited model | You expect a generalist student audience, not a subfield peer panel | `hlr-writing-style` |
| Preemption | You have searched SSRN / Westlaw / HeinOnline and your claim is genuinely new | `hlr-preemption-check` |
| Normative payoff | The piece does more than describe doctrine — it argues for something | `hlr-thesis-and-contribution` |
| Source-pull readiness | Every proposition is pin-cited and pullable to a real source | `hlr-footnotes-and-cite-check` |
| Placement plan | You know the seasons and the expedite mechanics before you submit | `hlr-placement-strategy` |

## Anti-patterns

- Treating HLR like a peer-reviewed journal — it is **student-edited**; pitch and process differ
- Skipping the preemption check and discovering the claim was published last year
- Submitting outside the seasons, or single-submitting when the norm is multi-submit + expedite
- A descriptive doctrinal survey with no normative thesis (generalist editors reject "no payoff")
- Loose, un-pinpointed citations that cannot survive the source-pull

## Output format

```
【Stage】topic / thesis / preemption / argument / sources / footnotes / writing / placement / submit / edit / revise
【Type】Article / Essay / Book Review / Supreme Court (invited)
【Route to】hlr-<skill>
【Why】one line
【Then】the next skill after that
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — legal research databases + Bluebook/citation tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official HLR URLs behind every fact in this pack
