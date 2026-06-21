---
name: ylj-sources-and-bluebook
description: Use when building and formatting the citation apparatus for a The Yale Law Journal (YLJ) piece — pinpoint cites, Bluebook form, and source support for every assertion. It governs cite construction; the final editorial cite-check and source-pull is ylj-footnotes-and-cite-check.
---

# Sources & Bluebook (ylj-sources-and-bluebook)

Legal scholarship is carried in its **footnotes**, and YLJ formats them in **Bluebook** form (The
Bluebook: A Uniform System of Citation), supplemented by the Journal's own citation requirements. Every
sentence that asserts law or fact carries a footnote with a **pinpoint** cite to authority that actually
supports it. This skill builds correct, supported cites as you draft; the line-by-line editorial verify
happens later in `ylj-footnotes-and-cite-check`.

## When to trigger

- Drafting any sentence that states what the law is, what a court held, or a fact
- Unsure of Bluebook form for a case, statute, regulation, book, or article
- A footnote cites a source generally instead of to the exact page/section
- Preparing the manuscript so student editors can source-pull every footnote

## Core rules YLJ editors enforce

- **A cite for every proposition.** Assertions of law and fact are footnoted; unsupported claims get
  flagged in source-pull.
- **Pinpoint, always.** Cite the exact page (`id. at 412`), section (`§ 1983`), or paragraph — never
  just the first page of a long opinion when you rely on a holding deep inside it.
- **The source must actually say it.** A cite that doesn't support the sentence is the single most
  common source-pull failure; quote or paraphrase only what the page contains.
- **Bluebook form by source type** (typeface, order of authorities, signals, short forms):

| Source | Skeleton (Bluebook) |
|--------|--------------------|
| Case | *Name v. Name*, Vol Reporter Page, pin (Court Year). |
| Statute | Title U.S.C. § X (Year). |
| Regulation | Vol C.F.R. § X (Year). |
| Book | Author, **Title** Page (ed. Year). |
| Law-review article | Author, *Title*, Vol Journal Page, pin (Year). |
| Short forms | *id.*; *supra* note N; hereinafter, used consistently. |

## Signals and explanatory parentheticals

- Use **introductory signals** precisely — `See`, `See also`, `Cf.`, `But see`, `Contra`, `E.g.` —
  each means a different relationship between the cite and the text; misuse signals to a reader (and a
  source-puller) that you misread the source.
- Add **explanatory parentheticals** for any cite whose relevance isn't obvious from the text — they
  prove you read the source and save editors a step.
- Order string cites by the Bluebook hierarchy of authorities; don't list cases alphabetically.

## Quotations and paraphrase

- Verbatim language needs **quotation marks and a pinpoint cite**; paraphrase still needs a cite to the
  Bluebook + the Journal's requirements. Cleaning up another's words without quotation marks is a
  source-pull and integrity failure.
- For altered quotations use the Bluebook conventions (`[ ]`, `. . .`, `(emphasis added)`).

## Checklist

- [ ] Every law/fact assertion has a footnote
- [ ] Every cite is pinpointed to the page/section relied on
- [ ] The cited source actually supports the proposition (spot-check the hardest ones)
- [ ] Bluebook form correct per source type; short forms (`id.`, `supra`) consistent
- [ ] Signals chosen deliberately; explanatory parentheticals where relevance isn't obvious
- [ ] Quotations marked and pinpointed; alterations flagged per Bluebook

## Anti-patterns

- "String of see-cites" with no pinpoints — guarantees source-pull friction
- A cite to the first page of a 40-page opinion for a holding buried at page 38
- Wrong signal (`See` where the source directly states it, or vice versa)
- Paraphrase that tracks the source's wording without quotation marks (integrity flag)
- Deferring all Bluebook formatting to "the editors will fix it" — they cite-check, they don't ghostwrite

## Output format

```
【Apparatus state】% of assertions footnoted; pinpoints present? Y/N
【Bluebook form】case/statute/article skeletons applied consistently? Y/N
【Signals】used deliberately? Y/N
【Quotations】marked + pinpointed + alterations flagged? Y/N
【Next】ylj-writing-style for prose, then ylj-footnotes-and-cite-check for the full verify
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — Bluebook, citation managers, and source-checking tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — YLJ Bluebook / citation-requirement facts
