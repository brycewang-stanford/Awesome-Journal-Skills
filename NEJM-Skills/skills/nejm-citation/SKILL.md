---
name: nejm-citation
description: Use to convert references to NEJM's Vancouver / ICMJE numbered style — numbered in order of appearance, limited author lists then et al., NLM journal abbreviations, and a capped reference count. Late-stage style pass.
---

# Reference Style (nejm-citation)

## When to trigger

- References are in author–date (APA/Harvard) or another numbered convention and must become Vancouver/ICMJE.
- The reference list is alphabetical instead of ordered by citation appearance.
- Author lists are not handled per the "list N then et al." convention.
- The reference count exceeds the article-type cap.

## Vancouver / ICMJE mechanics (NEJM)

- **Numbered, in order of appearance** in the text; in-text citations are superscript numbers (e.g., text.¹ or text.²,³).
- A **single reference list** numbered in citation order — not alphabetical.
- **Author lists**: the Vancouver/ICMJE convention lists the first **six authors then "et al."** when there are more than six. NEJM uses a limited author list of this kind — confirm the exact cutoff in the current author guidelines.
- **Journal titles abbreviated** per **NLM / Index Medicus** abbreviations.
- Include volume, issue/pages (or article identifier), and year; include the **DOI** where available.
- Keep the reference list within the article-type cap (an Original Article runs a **limited list, on the order of ~40**).

## Reference formats (shape)

- **Journal article:**
  `Author AB, Author CD, Author EF, et al. Title of the article. Journal Abbrev Year;Volume:first-last.`
- **Book:**
  `Author AB. Book title. Edition. City: Publisher; Year.`
- **Chapter:**
  `Author AB. Chapter title. In: Editor CD, ed. Book title. City: Publisher; Year:pp-pp.`
- **Online / dataset:**
  `Author/Org. Title. URL (accessed date).` — include DOI when present.

> Surname precedes initials (no periods between initials in Vancouver); article title in sentence case; journal abbreviated and not italicized in the classic style. Use a reference manager's NEJM/Vancouver style and verify mechanically.

## Conversion from author–date

| From                              | To (Vancouver / NEJM)                          |
|-----------------------------------|------------------------------------------------|
| "(Smith et al., 2021)"            | superscript number, e.g., "…outcome.¹²"        |
| "Smith, J. (2021)."               | "Smith J. … 2021;…"                            |
| Alphabetical reference list       | ordered by first appearance                    |
| ">6 authors all listed"           | first six authors, then **et al.**             |
| Full journal name                 | NLM abbreviation                               |

## Tooling

- Use Zotero/EndNote with an **NEJM / Vancouver (ICMJE)** style; do a final manual pass on the author cutoff and NLM abbreviations.
- Verify every superscript number resolves to a list entry, with no gaps or duplicates, and that the count is within the cap.


## Citation pass for New England Journal of Medicine

Use this as a second-pass capability check. First lock the clinical question, population, endpoint, effect size, safety signal, and practice implication; then test whether the manuscript addresses clinical-medicine reviewers who expect practice-changing evidence, patient relevance, safety, and exact reporting discipline.

- **Primary move:** Audit references and notes as evidence discipline: each source should position, document, or delimit a claim.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Neighbor test:** compare against JAMA for broad clinical medicine, Lancet for global-health/public-health reach, specialty journals for narrower disease domains; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Style detected】 author-date / other-numbered → Vancouver/ICMJE
【Numbering】 by appearance? single list, not alphabetical? yes/no
【Author lists】 first six then et al. (confirm cutoff)? yes/no
【Journal abbreviations】 NLM/Index Medicus applied? yes/no
【Reference count】 N vs ~40 cap (article-type) → ok / over
【Unresolved/duplicate refs】 [...]
【Next】 nejm-submission
```

## Anti-patterns

- **Do not** leave author–date citations anywhere in an NEJM manuscript.
- **Do not** alphabetize the reference list — order is by appearance.
- **Do not** spell out full journal names — use NLM abbreviations.
- **Do not** list all authors when there are more than six — use "et al." per the convention.
