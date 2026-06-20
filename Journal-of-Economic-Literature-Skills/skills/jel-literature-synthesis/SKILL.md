---
name: jel-literature-synthesis
description: Use when systematically gathering, reading, and synthesizing a large body of economic research for a Journal of Economic Literature (JEL) survey — coverage discipline and avoiding citation gaps. Builds the evidence corpus and synthesis notes; it does not impose the analytical spine (jel-organizing-framework) or write prose.
---

# Literature Synthesis (jel-literature-synthesis)

## When to trigger

- The proposal was encouraged and it is time to read the field thoroughly
- Reading feels unsystematic; you fear missing important contributions
- You have many papers but no way to weigh, compare, or reconcile their findings
- A referee at JEL is likely to ask "why did you omit X / the Y literature?"

## Coverage discipline: read the field, not a convenience sample

A JEL survey's credibility rests on the reader's belief that you read **everything that matters**. Build coverage systematically rather than from memory:

1. **Seed set.** Start from the proposal's key references and the field's canonical pieces.
2. **Forward + backward snowball.** Backward: every paper's reference list. Forward: who cites the seeds (Google Scholar / Scopus citation counts). Iterate until new searches stop turning up unseen important work (*saturation*).
3. **Keyword + JEL-code sweep.** Search EconLit / RePEc / NBER / SSRN by topic keywords **and** by the relevant JEL classification codes (see `jel-classification-system`) to catch work indexed under adjacent labels.
4. **Working papers + adjacent fields.** A current survey must include recent working papers (the frontier) and the bordering literatures the field draws on, or referees will flag staleness and siloing.
5. **Saturation log.** Record when each search stops yielding new must-cite work — this is your evidence of comprehensiveness for `jel-comprehensiveness-and-balance`.

## From reading to synthesis (not summary)

Summarizing is restating each paper; **synthesizing** is making the papers *talk to each other*. Maintain an evidence matrix as you read:

| Column | What to capture |
|--------|-----------------|
| Study | author–year, the result you will cite it for |
| Question/estimand | exactly what it measures (so non-comparable studies are not pooled) |
| Method/data | design and sample (so you can weight credibility) |
| Finding | direction + magnitude (for who-found-what tables) |
| Quality/credibility | identification strength, sample, robustness — your *appraisal*, since JEL does not run new estimates |
| Tension | which other studies it agrees/conflicts with, and why |

This matrix is the raw material for the organizing framework, the summary tables, and the even-handed treatment of controversies. Crucially, you **appraise** primary studies (you are the field's referee-of-record); you do **not** re-estimate them.

## Checklist

- [ ] Seed set drawn from canonical pieces + proposal references
- [ ] Forward and backward snowball iterated to saturation
- [ ] EconLit / RePEc / NBER / SSRN swept by keyword **and** JEL code
- [ ] Recent working papers and adjacent literatures included (no staleness, no silo)
- [ ] Saturation log records where searches stopped yielding new must-cites
- [ ] Evidence matrix captures estimand + method + finding + your credibility appraisal + tensions
- [ ] Non-comparable studies are flagged as such (not pooled into a false consensus)
- [ ] No major author/school whose omission a referee could name

## Anti-patterns

- Citing from memory or from a personal reading list (predictable coverage gaps)
- Summarizing paper-by-paper instead of synthesizing across papers
- Pooling studies that estimate *different* objects into one "the literature finds…" claim
- Ignoring working papers (looks stale) or ignoring adjacent fields (looks siloed)
- Re-running or "correcting" primary studies — a JEL survey appraises, it does not re-estimate
- Leaning on review databases without the JEL-code sweep that catches adjacently-indexed work

## Output format

```
【Seed set】<canonical + proposal references>
【Snowball status】backward/forward iterated to saturation? Y/N
【Databases swept】EconLit / RePEc / NBER / SSRN — by keyword + JEL code? Y/N
【Frontier + adjacency】recent WPs and bordering literatures included? Y/N
【Saturation evidence】<where searches stopped yielding new must-cites>
【Evidence matrix】rows ready with estimand / method / finding / appraisal / tension? Y/N
【Coverage risks】<any author/school an omission referee could name>
【Next step】→ jel-organizing-framework (impose the analytical spine on the matrix)
```
