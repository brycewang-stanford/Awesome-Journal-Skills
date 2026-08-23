# Worked example — one paper, six steps, real tool output

Every command below was run against the committed index, and the output is pasted
verbatim. The **paper is hypothetical**, deliberately: a real one would make this a
claim about how a named journal treats a named author's work, and it would also let the
example be cherry-picked. Nothing here is a recommendation about any actual manuscript.

> **What is illustrative and what is real.** The matcher output is real. The
> `p_accept` and months-to-decision figures in step 6 are **made up for the arithmetic**
> — the real ones are read from each venue's `resources/official-source-map.md` at the
> moment of use, and this file deliberately stores none of them. That is the same rule
> the whole capability runs on: no volatile fact is ever duplicated out of a source map.

---

## Step 1 — The paper profile

Written once, and read by every later step
([`paper-profile.md`](paper-profile.md)):

```yaml
title: "Paid Family Leave and the Career Trajectories of Low-Wage Mothers"
discipline: economics/labor
method: DiD                       # stacked, with cohort-specific event studies
lane: empirical
contribution: policy-evaluation   # a policy effect, not a new mechanism
setting:
  region: international
  country: US
  data: linked administrative earnings and employer records, 20 years
  proprietary: true               # restricted-access admin data — check disclosure rules
ambition: field                   # a clean policy estimate, not a general-interest result
constraints:
  clock: "tenure file due in 30 months"
  budget_apc: none
  anonymisable: true
history: []
```

The field that does the most work here is `ambition: field`. Calling this
`general-interest` would produce a shortlist of top-5 journals and, on the arithmetic in
step 6, spend most of the tenure clock finding that out.

## Step 2 — Shortlist

```bash
python3 tools/match_venues.py \
  --title "Paid Family Leave and the Career Trajectories of Low-Wage Mothers" \
  --abstract "We study the staggered adoption of state paid family leave mandates using
    linked administrative earnings and employer records covering two decades. A stacked
    difference-in-differences design with cohort-specific event studies estimates effects
    on labor force attachment, employer tenure and wage growth for mothers in the bottom
    third of the earnings distribution. Leave take-up rises sharply, job continuity
    improves, and wage growth is unchanged, implying the policy protects attachment
    without closing the motherhood earnings gap." \
  --discipline economics/labor --lane empirical --top 8
```

```
8 candidates · 95 query terms · scores are relative, not probabilities

  1. Journal of Labor Economics  [journal-of-labor-economics]
     economics/labor · journal · empirical · international · tier: field · depth
     match 1.00 via: earnings, wage, labor, administrative, effects, event
     read: Journal-of-Labor-Economics-Skills/resources/official-source-map.md
  2. Journal of Human Resources  [journal-of-human-resources]
     management · journal · empirical · international · tier: field · depth
     match 0.41 via: estimates, linked, earnings, administrative, records, event
     read: Journal-of-Human-Resources-Skills/resources/official-source-map.md
  3. Journal of Health Economics  [journal-of-health-economics]
     economics/health · journal · empirical · international · tier: field · depth
     match 0.40 via: take-up, mandates, labor, policy, earnings, staggered
     read: Journal-of-Health-Economics-Skills/resources/official-source-map.md
  4. AEJ Economic Policy  [aej-economic-policy]
     economics/policy · journal · empirical · international · tier: field · depth
     match 0.38 via: policy, take-up, estimates, staggered, event, effects
     read: AEJ-Economic-Policy-Skills/resources/official-source-map.md
  5. Journal of Policy Analysis and Management  [journal-of-policy-analysis-and-management]
     public-policy · journal · empirical · international · tier: field · depth
     match 0.36 via: take-up, policy, estimates, effects, distribution, staggered
     read: Journal-of-Policy-Analysis-and-Management-Skills/resources/official-source-map.md
  6. Journal of Banking and Finance  [journal-of-banking-and-finance]
     finance · journal · empirical · international · tier: field · depth
     match 0.26 via: adoption, mandates, paid, staggered, event, growth
     read: Journal-of-Banking-and-Finance-Skills/resources/official-source-map.md
  7. Review of Economics and Statistics  [review-of-economics-and-statistics]
     economics/applied · journal · empirical · international · tier: field · depth
     match 0.24 via: wage, difference-in-differences, estimates, staggered, event, design
     read: Review-of-Economics-and-Statistics-Skills/resources/official-source-map.md
  8. Journal of Public Economics  [journal-of-public-economics]
     economics/public · journal · empirical · international · tier: field · depth
     match 0.21 via: take-up, policy, labor, estimates, design, administrative
     read: Journal-of-Public-Economics-Skills/resources/official-source-map.md
```

**Reading the matched terms is the point of this step.** Row 6, Journal of Banking and
Finance, matched on `adoption, mandates, paid, staggered, event, growth` — six terms,
none of which is about labour or families. It is a design-vocabulary match: staggered
adoption and event studies are how *corporate finance* papers are written too. Drop it,
and note that a shortlist can be wrong in a way that a score alone will not reveal.

Rows 3 and 5 are the informative ones. Neither is a labour journal, and the discipline
prior did not pull them up — it pushed them *down* relative to the run without it, and
they are still here. That is a signal the paper reads as a policy-evaluation paper as
much as a labour paper, which is a real fork in framing, not a retrieval artefact.

## Step 3 — Score, by reading the packs

The matcher is finished. Open each candidate's `source_map` and its
`*-topic-selection` skill, and score Fit × acceptance-odds × turnaround × cost/policy ×
audience. Two things this paper forces:

- **Cost/policy is binding, not cosmetic.** `setting.proprietary: true` means the
  restricted-access data has to clear each venue's data-and-code policy. For an
  economics journal with a data editor, that is a real submission requirement with real
  lead time. Read the policy *before* ranking, not after acceptance.
- **Fit deferred to the pack.** Whether a policy-evaluation contribution with no new
  mechanism clears a given venue's bar is answered by that venue's own
  `*-topic-selection` skill, not by the score in the table above.

## Step 4 — Reach / match / safe

Illustrative, and note that "reach" is a real reach for a `field`-ambition paper:

| Tier | Venue | Why |
|---|---|---|
| Reach | AEJ: Applied Economics | policy evaluation with admin data is squarely its lane; odds are long for a result with no new mechanism |
| Match | Journal of Labor Economics · Journal of Human Resources | the paper's own discipline, and the design is the kind these venues referee well |
| Safe | Journal of Policy Analysis and Management | high fit for the policy framing, faster decision, credible home |

## Step 5 — Anything outside the index?

Nothing plausible here is. If there had been — a specialist family-policy journal this
repository does not cover — the rule is to *say so* rather than force a fit, and hand to
[`rt-venue-integrity`](../../Research-Toolkit-Skills/skills/rt-venue-integrity/SKILL.md)
before submitting anywhere unverified.

## Step 6 — Cost the ladder

The tenure clock in the profile makes this the decisive step. Two sequences, same
venues, different order:

```bash
python3 tools/ladder_ev.py \
  --rung "AEJ: Applied Economics:0.07:5.0" \
  --rung "Journal of Labor Economics:0.12:4.0" \
  --rung "Journal of Human Resources:0.18:4.0" \
  --rung "Journal of Policy Analysis and Management:0.30:3.0"
```

```
  Time until the ladder resolves : 16.1 months (band 16.0-16.2)
  Time to print, if it places    : 16.2 months (band 16.0-16.5)
  P(placed somewhere on it)      : 53% (band 35%-67%)
  P(ladder exhausted, unplaced)  : 47%
```

Dropping the reach rung:

```
  Time until the ladder resolves : 11.7 months (band 11.5-11.8)
  Time to print, if it places    : 12.3 months (band 12.2-12.5)
  P(placed somewhere on it)      : 49% (band 32%-64%)
  P(ladder exhausted, unplaced)  : 51%
```

**What the comparison actually supports.** Trying AEJ: Applied first costs about
4½ months and buys about 4 points of placement probability. Whether that is worth it is
the author's call against a 30-month clock — but notice the honest part: the two
placement bands (35–67% and 32–64%) overlap almost entirely. On these inputs the
*probability* difference is not distinguishable; the **time** difference is, because it
barely moves under the sensitivity band. So the defensible statement is "the reach rung
costs four months and may buy nothing measurable", not "ladder A is better".

**And the warning matters more than either number.** Both ladders exhaust with roughly
even odds. That is the finding: this is not a floor, it is a cliff. Before choosing an
order, go back to step 2 and add a rung that will realistically take the paper.

## What this example is not

It is not evidence that the matcher works. That is what
[`eval/RESULTS.md`](eval/RESULTS.md) is for, on 861 held-out papers, and it reports
R@10 = 41.5% from a bare title — which is to say the shortlist above is a good case, and
a bare-title query on a thinner discipline would not look like this.

---
*Method: [`journal-match.md`](journal-match.md). Entry point:
[`rt-journal-match`](../../Research-Toolkit-Skills/skills/rt-journal-match/SKILL.md) and
[`rt-ladder-ev`](../../Research-Toolkit-Skills/skills/rt-ladder-ev/SKILL.md).*
