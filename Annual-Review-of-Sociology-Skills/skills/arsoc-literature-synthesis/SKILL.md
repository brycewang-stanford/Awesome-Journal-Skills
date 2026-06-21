---
name: arsoc-literature-synthesis
description: Use when systematically gathering, reading, and synthesizing a large body of sociological research for an Annual Review of Sociology (ARSoc) review — coverage discipline and avoiding citation gaps across theoretical traditions. Builds the evidence corpus and synthesis notes; it does not impose the analytical spine (arsoc-organizing-framework) or write prose (arsoc-writing-style).
---

# Literature Synthesis (arsoc-literature-synthesis)

## When to trigger

- The topic was commissioned and it is time to read the subfield thoroughly
- Reading feels unsystematic; you fear missing important contributions or a whole tradition
- You have many studies but no way to weigh, compare, or reconcile their findings
- A Committee/referee at ARSoc is likely to ask "why did you omit X / the Y literature / the qualitative work?"

## Coverage discipline: read the subfield, not a convenience sample

An ARSoc review's credibility rests on the reader's belief that you read **everything that matters** across methods and schools. Sociology spans quantitative, qualitative, computational, and theoretical work, and reviewers notice when one mode is slighted. Build coverage systematically rather than from memory:

1. **Seed set.** Start from the field's canonical pieces and the references behind the commissioned topic.
2. **Forward + backward snowball.** Backward: every study's reference list. Forward: who cites the seeds (Google Scholar / Web of Science / Scopus). Iterate until new searches stop turning up unseen important work (*saturation*).
3. **Database + keyword sweep.** Search **Sociological Abstracts**, Web of Science, Scopus, JSTOR, and Google Scholar by topic keywords *and* by the names of the rival theoretical traditions, to catch work indexed under adjacent labels.
4. **Mind-the-modes coverage.** Deliberately sweep for **qualitative and ethnographic** work, **computational / big-data** studies, **demographic** analyses, and the **theoretical** statements, not only the quantitative articles you know best — siloing by method is a recurring ARSoc referee complaint.
5. **Recent + adjacent.** Include recent papers and forthcoming work (the frontier) and the bordering literatures the subfield draws on, or referees will flag staleness and siloing.
6. **Saturation log.** Record when each search stops yielding new must-cite work — this is your documented evidence of comprehensiveness for `arsoc-comprehensiveness-and-balance` and `arsoc-transparency-and-reproducibility`.

## From reading to synthesis (not summary)

Summarizing is restating each study; **synthesizing** is making the studies *talk to each other*. Maintain an evidence matrix as you read:

| Column | What to capture |
|--------|-----------------|
| Study | author–year, the result you will cite it for |
| Question/claim | exactly what it argues or measures (so non-comparable studies are not pooled) |
| Method/data | design, sample, mode (quant / qual / computational / theoretical) — so you can weight credibility |
| Finding | direction + magnitude, or the central claim (for who-found-what tables) |
| Tradition | which theoretical school / school it speaks for |
| Credibility | identification strength, sample, analytic transparency — your *appraisal*, since ARSoc runs no new analysis |
| Tension | which other studies it agrees/conflicts with, and why |

This matrix is the raw material for the organizing framework, the summary tables, and the even-handed treatment of debates. Crucially, you **appraise** primary studies (you are the subfield's referee-of-record for the wider discipline); you do **not** re-analyze them.

## Checklist

- [ ] Seed set drawn from canonical pieces + the commissioned topic's references
- [ ] Forward and backward snowball iterated to saturation
- [ ] Sociological Abstracts / Web of Science / Scopus / JSTOR / Scholar swept by keyword **and** by tradition
- [ ] Qualitative, computational, demographic, and theoretical modes all deliberately covered (no method silo)
- [ ] Recent/forthcoming work and adjacent literatures included (no staleness, no silo)
- [ ] Saturation log records where searches stopped yielding new must-cites
- [ ] Evidence matrix captures claim + method/mode + finding + tradition + credibility appraisal + tensions
- [ ] Non-comparable studies flagged as such (not pooled into a false consensus)
- [ ] No major author/school/method whose omission a referee could name

## Anti-patterns

- Citing from memory or from a personal reading list (predictable coverage gaps)
- Summarizing study-by-study instead of synthesizing across studies
- Covering only the quantitative literature and ignoring the qualitative/theoretical work (method silo)
- Pooling studies that measure *different* objects into one "the literature finds…" claim
- Ignoring forthcoming work (looks stale) or ignoring adjacent subfields (looks siloed)
- Re-analyzing or "correcting" primary studies — an ARSoc review appraises, it does not re-estimate

## Output format

```text
【Seed set】<canonical + commissioned-topic references>
【Snowball status】backward/forward iterated to saturation? Y/N
【Databases swept】Sociological Abstracts / WoS / Scopus / JSTOR / Scholar — by keyword + tradition? Y/N
【Mode coverage】quant + qual + computational + demographic + theoretical all swept? Y/N
【Frontier + adjacency】recent/forthcoming work and bordering literatures included? Y/N
【Saturation evidence】<where searches stopped yielding new must-cites>
【Evidence matrix】rows ready with claim / method / finding / tradition / appraisal / tension? Y/N
【Coverage risks】<any author/school/method an omission referee could name>
【Next step】→ arsoc-organizing-framework (impose the analytical spine on the matrix)
```
