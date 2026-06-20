---
name: arecon-literature-synthesis
description: Use when systematically gathering, reading, and synthesizing a body of economic research for an Annual Review of Economics (ARE) review — coverage discipline and avoiding citation gaps. Builds the evidence corpus and synthesis notes; it does not impose the analytical spine (arecon-organizing-framework) or appraise study credibility (arecon-evidence-standards).
---

# Literature Synthesis (arecon-literature-synthesis)

## When to trigger

- The invitation is secured and it is time to read the field thoroughly
- Reading feels unsystematic; you fear missing important contributions an adjacent economist would expect
- You have many papers but no way to weigh, compare, or reconcile their findings
- A Committee referee is likely to ask "why did you omit X / the Y literature?"

## Coverage discipline: read the field, not a convenience sample

An ARE review's credibility rests on the reader's belief that you read **everything that matters** — and ARE referees are often the very authors whose work is being weighed, so gaps are noticed. Build coverage systematically rather than from memory:

1. **Seed set.** Start from the pitch's key references and the field's canonical pieces.
2. **Forward + backward snowball.** Backward: every paper's reference list. Forward: who cites the seeds (Google Scholar / Scopus). Iterate until new searches stop turning up unseen important work (*saturation*).
3. **Keyword + JEL-code sweep.** Search EconLit / RePEc / NBER / SSRN by topic keywords **and** by the relevant JEL classification codes, to catch work indexed under adjacent labels.
4. **Working papers + adjacent fields.** A current review must include recent working papers (the frontier) and the bordering literatures the field draws on, or referees flag staleness and siloing. ARE's annual cadence makes frontier coverage especially visible — a review that stops at last year's published work reads as dated on arrival.
5. **Saturation log.** Record when each search stops yielding new must-cite work — this is your evidence of comprehensiveness for the balance audit in `arecon-evidence-standards`.

## From reading to synthesis (not summary)

Summarizing is restating each paper; **synthesizing** is making the papers *talk to each other*. Maintain an evidence matrix as you read:

| Column | What to capture |
|--------|-----------------|
| Study | author–year, the result you will cite it for |
| Question/estimand | exactly what it measures (so non-comparable studies are not pooled) |
| Method/data | design and sample (so you can weight credibility) |
| Finding | direction + magnitude (for who-found-what tables) |
| Credibility | identification strength, sample, robustness — your *appraisal*, since ARE runs no new estimates |
| Tension | which other studies it agrees/conflicts with, and why |

This matrix is the raw material for the organizing framework, the summary tables, and the even-handed treatment of controversies. Crucially, you **appraise** primary studies — you are the field's referee-of-record for adjacent readers — you do **not** re-estimate them.

## Synthesis depth vs. ARE's accessibility mandate

Unlike a Handbook chapter (exhaustive) or a JEL survey (deeper and longer), an ARE review must stay **readable by an outsider in ~25–40 pages** (检索于 2026-06；以官网为准). So the matrix serves a second purpose: it lets you cite the confirmatory tier in clusters while reserving prose for the field-defining work. Read exhaustively; *write* selectively. Coverage is proven by the citation set; accessibility is exercised in the prose.

## Checklist

- [ ] Seed set drawn from canonical pieces + pitch references
- [ ] Forward and backward snowball iterated to saturation
- [ ] EconLit / RePEc / NBER / SSRN swept by keyword **and** JEL code
- [ ] Recent working papers and adjacent literatures included (no staleness, no silo)
- [ ] Saturation log records where searches stopped yielding new must-cites
- [ ] Evidence matrix captures estimand + method + finding + credibility appraisal + tensions
- [ ] Non-comparable studies flagged as such (not pooled into a false consensus)
- [ ] No major author/school whose omission a Committee referee could name

## Anti-patterns

- Citing from memory or from a personal reading list (predictable coverage gaps the surveyed authors will spot)
- Summarizing paper-by-paper instead of synthesizing across papers
- Pooling studies that estimate *different* objects into one "the literature finds…" claim
- Ignoring working papers (looks stale at an annual cadence) or ignoring adjacent fields (looks siloed)
- Re-running or "correcting" primary studies — an ARE review appraises, it does not re-estimate
- Leaning on review databases without the JEL-code sweep that catches adjacently-indexed work

## Output format

```text
【Seed set】<canonical + pitch references>
【Snowball status】backward/forward iterated to saturation? Y/N
【Databases swept】EconLit / RePEc / NBER / SSRN — by keyword + JEL code? Y/N
【Frontier + adjacency】recent WPs and bordering literatures included? Y/N
【Saturation evidence】<where searches stopped yielding new must-cites>
【Evidence matrix】rows ready with estimand / method / finding / appraisal / tension? Y/N
【Coverage risks】<any author/school an omission referee could name>
【Next step】→ arecon-organizing-framework (impose the analytical spine on the matrix)
```
