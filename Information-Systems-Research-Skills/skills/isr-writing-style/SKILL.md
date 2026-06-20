---
name: isr-writing-style
description: Use when polishing the prose, structure, abstract, and notation of an Information Systems Research (ISR) manuscript — front-loading the IS contribution, writing for a sociotechnical and intradisciplinary readership, keeping the 300-word abstract and double-anonymized text, and following INFORMS author-date style. Late-stage polish; do not invoke while the contribution or identification/proof is still unsettled.
---

# Writing Style (isr-writing-style)

## When to trigger

- The argument is sound but the prose buries it, is jargon-heavy, or is passive
- The abstract is over length or does not state the contribution
- Notation is inconsistent (analytical papers) or constructs drift (behavioral papers)
- You need a final pass before `isr-submission`

## Front-load the IS contribution

ISR readers span behavioral, economic, design-science, and organizational backgrounds, so the introduction must make the **contribution to IS** legible to all of them quickly: the phenomenon, why the IT artifact makes it an IS question, the gap/tension in a named IS conversation, what you do, and what you find. Do not make a reviewer reverse-engineer the point from the results. Because ISR is intradisciplinary, name the bridge you build (e.g., an economic lens on a behavioral phenomenon) early and in plain language.

## Write for two audiences without losing either

In an analytical paper, give the **intuition before the algebra** — every key result should have a one-sentence plain-language reading so behavioral readers can follow it. In a behavioral paper, define constructs precisely and avoid undefined formalism. Multimethod papers should signpost transitions between methods and remind the reader how each piece serves the shared argument.

## Abstract, notation, and consistency

- **Abstract: 300 words maximum.** Lead with the phenomenon and contribution, not background.
- **Notation** (analytical): define every symbol on first use; keep a consistent convention; never reuse a symbol for two meanings.
- **Constructs** (behavioral): one name per construct throughout; hypothesis labels stable across text, tables, and figures.

## INFORMS style and double-anonymization

Use the INFORMS **author-date** reference style: references alphabetized by author, with in-text citations
by author name and year. Files are **double-spaced**, **at least 11-point** font, with **one-inch margins**
on all four sides. Keep the text **double-anonymized**: remove names, affiliations, and identifying
acknowledgments, and word self-citations neutrally so the prose does not reveal authorship.

## Checklist

- [ ] Intro front-loads the IS contribution and the intradisciplinary bridge
- [ ] Intuition precedes algebra (analytical); constructs defined (behavioral)
- [ ] Abstract ≤ 300 words and contribution-led
- [ ] Notation/construct names consistent across text and exhibits
- [ ] INFORMS author-date style; double-spaced, ≥11-pt, 1-inch margins
- [ ] Text double-anonymized; self-citations neutral
- [ ] Active voice; jargon minimized for a cross-paradigm readership

## Anti-patterns

- **Buried lede**: the contribution appears only in the discussion.
- **Algebra without intuition** that loses behavioral readers.
- **Construct/notation drift** between text and exhibits.
- **Identity leakage** in acknowledgments or "our prior work" phrasing.


## Style execution pass for Information Systems Research

Run this as a concrete capability pass. First lock the digital artifact or system, user/firm behavior, identification or design evidence, and IS-theory contribution; then test whether the manuscript addresses IS reviewers who expect digital-technology theory, empirical or design leverage, and implications for organizations or markets.

- **Primary move:** Rewrite the opening and transitions so the venue-level claim, evidence object, and contribution are visible before technical detail; keep house-style limits tied to the source map.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against MIS Quarterly for broader IS theory, Management Science for OR/MS generality, Journal of Management Information Systems for applied IS systems; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Intro front-loading】contribution + bridge stated early? [...]
【Two-audience readability】intuition/definitions present? [...]
【Abstract】≤300 words, contribution-led? [...]
【Notation/construct consistency】[...]
【INFORMS style + format】author-date, spacing, margins: pass/fix
【Anonymization】pass/fix
【Next step】isr-submission
```
