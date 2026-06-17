---
name: poq-rebuttal
description: Use when writing the response to a Public Opinion Quarterly (POQ) revise-and-resubmit. POQ referees are survey methodologists who often push on Total Survey Error and AAPOR disclosure, so the response must satisfy each referee on substance and method while keeping the associate editor confident the revision converges. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (poq-rebuttal)

A POQ **R&R is an opportunity** — but the referees are survey scientists, and their comments often turn
on **Total Survey Error** (coverage, nonresponse, wording, mode, weighting) and **AAPOR disclosure**.
The response letter must move *every* referee toward yes on both substance and method, while keeping
the **associate editor** confident the revision is convergent.

## When to trigger

- An R&R decision arrived and you are planning the revision + response letter
- Referees disagree with each other and you must reconcile their demands
- A referee requests new weighting, robustness, or disclosure that touches the claims
- Writing the cover note to the AE summarizing the revision

## Strategy

1. **Read the AE's letter as the rubric.** The associate editor signals which points are decisive.
   Solve those first; the AE adjudicates disagreements among referees.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Answer survey-error objections with evidence, not assertion.** When a referee questions
   nonresponse bias, mode effects, wording, or weighting, respond with an added analysis, a sensitivity
   check, or an explicit disclosure update — point to the revised Appendix A / table / figure.
4. **Concede or rebut explicitly.** For each: did what was asked (say where, with the new
   text/table/figure number), or push back **respectfully with a methodological reason**. Referees
   respect a well-argued disagreement grounded in survey science.
5. **Reconcile conflicting referees openly.** When R2 wants the opposite of R3, say so, choose a
   principled path, and explain the tradeoff to the AE.
6. **Protect the contribution.** Add robustness and disclosure; resist changes that dilute the opinion
   or survey-validity claim that earned the R&R. Defend scope conditions rather than over-claiming.
7. **Keep anonymity intact** in the revised manuscript (still double-blind), and **update the
   replication package and Appendix A** so new tables/figures remain reproducible and disclosed (see
   `poq-transparency-and-data-policy`).

## Response-letter format

For each referee comment:

```
> [Quoted referee comment]

Response: [What we did / why we respectfully disagree, on survey-science grounds].
Change: [Section/page/table-figure/Appendix-A location where the revision appears].
```

Open with a short **summary of the main changes** to the AE; group by referee; end each entry with the
location of every change so the editor can verify quickly.

## Synchronize the revision package

POQ revisions often fail because the manuscript, Appendix A, replication files, and response letter drift apart. Maintain a package ledger:

| Changed item | Manuscript location | Appendix A / supplement | Deposited file |
| --- | --- | --- | --- |
| New weight or variance estimator | Methods/results section and table note | Updated weighting/design-effect disclosure | Analysis script and output |
| Revised response-rate calculation | Methods and disclosure paragraph | Disposition-code table | Calculation worksheet |
| New question wording or split ballot | Survey design section | Exact wording and order | Instrument file |
| New robustness or sensitivity check | Short main-text pointer | Full table/figure | Code and data extract |

Before resubmission, read the response letter against the ledger. Every "we added" sentence needs a manuscript or appendix location, and every new exhibit needs a reproducible source.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Answering a nonresponse/mode/weighting objection with assertion rather than analysis or disclosure
- Capitulating to a request that breaks the design's logic just to please a referee
- Defensive or dismissive tone toward referees
- Letting the revised manuscript, Appendix A, or new exhibits drift out of sync with the deposited package
- Reporting a new robustness result in the letter but leaving Appendix A or replication files unchanged

## Output format

```
【AE's decisive points】addressed first? [list]
【Coverage】every referee comment answered? [Y/N]
【Survey-error objections】each met with analysis/disclosure + change location
【Concede vs rebut】each tagged with evidence + location
【Referee conflicts】reconciled and explained to AE? [Y/N]
【Contribution protected】no dilution of opinion / survey-validity claim? [Y/N]
【Anonymity + package + Appendix A updated】[Y/N]
【Package ledger】manuscript / Appendix A / deposit synchronized? [Y/N]
【Next】resubmit via ScholarOne Manuscripts
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — sensitivity/robustness and disclosure tooling for the revision
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review and AE code/data requests
