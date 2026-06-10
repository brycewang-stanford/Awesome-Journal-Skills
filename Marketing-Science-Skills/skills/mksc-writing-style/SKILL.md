---
name: mksc-writing-style
description: Use when polishing the prose of a Marketing Science manuscript — front-loading model intuition before notation, managing the formal apparatus for readability, and following INFORMS author-year style and formatting. Late-stage polish; do not invoke while the model or identification is still unsettled.
---

# Writing Style (mksc-writing-style)

## When to trigger

- The paper buries its intuition under notation; an editor cannot grasp the contribution from the first pages
- Notation is dense, inconsistent, or introduced before motivation
- Citations/formatting are not in INFORMS style
- You are doing a final pass before submission (and the model is settled)

## Lead with intuition, then formalize

Marketing Science readers are technical, but the **intuition must come first**. State the marketing question, the mechanism, and the headline counterfactual in words before the model appears. Each major result should be previewed in plain language ("intuitively, because firms re-optimize prices, …") and only then proven. Notation is a tool for precision, not a substitute for an argument.

- Introduce notation **just-in-time**, near where it is used; keep a consistent, minimal symbol set; consider a notation table for heavy models.
- For analytical results, state the proposition in words, give the economic intuition, then the formal claim; push long proofs to an appendix.
- For structural work, motivate each modeling assumption by the marketing institution it captures.

## INFORMS house style

- **Citations**: author-year, e.g., (Norman 1977) or Norman (1977); reference list alphabetical by author in INFORMS reference style.
- **Format**: double-spaced, single column, 11- or 12-point font, one-inch margins; prepared in MS Word or LaTeX (INFORMS LaTeX style files and Style-Instructions.pdf on the Author Portal); uploaded as Word or PDF.
- **Abstract**: not more than 200 words, on the first page; 3–6 keywords describing the theoretical and methodological orientation.
- **Length discipline**: regular articles have no fixed cap but are expected to be written succinctly; **Frontiers** is a strict 6,000-word total cap (including references, tables, graphs, appendices), so for Frontiers, ruthlessly cut and push detail online.
- Keep the manuscript **blinded** for double-anonymous review — no self-identifying phrasing.

## Checklist

- [ ] Question, mechanism, and counterfactual stated in words up front
- [ ] Each result previewed intuitively before being formalized
- [ ] Notation minimal, consistent, introduced just-in-time
- [ ] INFORMS author-year citations; alphabetical reference list
- [ ] Format: double-spaced, 11–12 pt, one-inch margins; Word/LaTeX→Word/PDF
- [ ] Abstract ≤ 200 words; 3–6 keywords
- [ ] Frontiers manuscripts within the 6,000-word total cap
- [ ] Manuscript blinded

## Anti-patterns

- Opening with a wall of notation and no intuition.
- Re-defining symbols or carrying unused notation.
- Numbered/footnote-style citations instead of INFORMS author-year.
- Over-length Frontiers submissions that will be returned.


## Style execution pass for Marketing Science

Treat this skill as an executable review pass, not a prose hint. First lock the demand/supply mechanism, fit evidence, and counterfactual decision margin; then judge whether the current manuscript answers the venue's real reader: quantitative marketing reviewers who read the model through the managerial counterfactual it makes possible.

- **Do the pass:** Rewrite the first two pages so each paragraph starts from the venue-level claim, not from chronology or method inventory; preserve exact source-map limits and move technical overflow to appendix or supplement.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Journal of Marketing Research for empirical marketing breadth, Management Science for wider OR/MS reach, Quantitative Marketing and Economics for specialist modeling; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Intuition-first】question/mechanism/counterfactual stated up front?
【Notation】minimal, consistent, just-in-time?
【Citations/format】INFORMS author-year; double-spaced 11–12pt; Word/LaTeX
【Abstract/keywords】≤200 words; 3–6 keywords
【Length】regular succinct / Frontiers ≤6,000 words total
【Blinding】intact?
【Next step】mksc-submission
```
