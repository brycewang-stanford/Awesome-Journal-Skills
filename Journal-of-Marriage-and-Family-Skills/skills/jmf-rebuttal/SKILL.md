---
name: jmf-rebuttal
description: Use when writing the response to a Journal of Marriage and Family (JMF) revise-and-resubmit. JMF reviews are double-blind and most published papers go through at least one R&R, so the response must convert each anonymous reviewer while keeping the editor confident the revision converges. Structures the response letter; it does not fabricate new results.
---

# R&R Rebuttal (jmf-rebuttal)

A JMF **R&R is a real opportunity** — most papers that publish go through one. But you are answering
**anonymous** reviewers (double-blind) plus an editor who adjudicates, so the response letter must move
*every* reviewer toward yes while keeping the editor confident the revision is convergent and the family-
science contribution is intact.

## When to trigger

- An R&R decision arrived and you are planning the revision + response letter
- Reviewers disagree with each other and you must reconcile their demands
- A reviewer requests analyses that would change the paper's claims
- Writing the cover note to the editor summarizing the revision

## Strategy

1. **Read the editor's letter as the rubric.** The editor signals which points are decisive (often
   selection, the framework, or the family-science contribution). Solve those first; the editor
   adjudicates disagreements among reviewers.
2. **One point-by-point response, every comment addressed.** Quote each comment, then respond. Never
   skip one — silence reads as non-compliance.
3. **Concede or rebut explicitly, with evidence.** For each: did what was asked (say where, with the
   new text/table number), or push back **respectfully with a reason** (theory, design, data limits,
   or the unit-of-analysis logic). A well-argued disagreement beats a capitulation that weakens the paper.
4. **Reconcile conflicting reviewers openly.** When R2 wants the opposite of R3, say so, choose a
   principled path, and explain the tradeoff to the editor. Don't silently satisfy one and ignore the
   other.
5. **Answer the recurring family-science objections head-on.** Strengthen the **selection** story,
   confirm models respect **dyadic/family non-independence**, and reaffirm the contribution to families
   — don't dilute it to please a reviewer.
6. **Keep anonymity intact** in the revised manuscript (still double-blind), and **update the
   replication/data materials** so new tables/figures remain reproducible (see
   `jmf-transparency-and-data-policy`).

## Response-letter format

For each reviewer comment:

```
> [Quoted reviewer comment]

Response: [What we did / why we respectfully disagree].
Change: [Section/page/table-figure number where the revision appears].
```

Open with a short **summary of the main changes** to the editor; group by reviewer; end each per-comment
entry with the location of every change so the editor can verify quickly.

## Triage table for a JMF R&R

| Comment type | Default move | Watch-out |
|--------------|--------------|-----------|
| Editor's decisive point | Solve first, lead the letter with it | Often selection, framework, or family-science contribution |
| Reviewer methodological (selection, dyadic dependence) | Concede + add the analysis; report what moved | Don't let a new analysis quietly contradict the headline |
| Reviewer wants a different framework | Engage; adopt or argue from family theory | Switching frameworks can unravel the hypotheses |
| Two reviewers conflict | Choose a principled path, explain the tradeoff to the editor | Silently satisfying one reads as evasive |
| Request that weakens the contribution | Respectful, reasoned pushback | A well-argued "no" beats a damaging "yes" |
| Format/anonymity/data | Comply; keep the revision double-blind and reproducible | New exhibits must stay in sync with deposited code |

Because JMF review is double-blind and most published papers clear at least one R&R, the response letter
is a persuasion document aimed at anonymous referees *and* an adjudicating editor who decides whether the
revision converges — written for the flagship venue of the National Council on Family Relations.

## Worked micro-example (illustrative)

On a dyadic marital-quality-and-health R&R, R2 demands a causal interpretation while R3 calls causal
language unjustified. The fix: state the conflict openly, hold the observational framing, and add within-
couple fixed-effects plus a sensitivity bound. Illustrative letter entry:

> R3: "The authors cannot claim marital strain *causes* health decline from observational panel data."
>
> Response: We agree and removed causal phrasing, reframing the contribution as a within-person association
> net of stable confounders. New couple fixed-effects models (Table 4) attenuate the estimate from −0.15 to
> −0.11 SD but it persists; an E-value of 1.6 (illustrative) shows how strong an unmeasured confounder would
> need to be to explain it. Change: Methods p. 14; Table 4. This also answers R2, to whom we explain why we
> stop short of a causal claim.

## Referee-pushback patterns and the convergence fix

- *"Family theory not engaged" (recurring).* Show how the framework now constrains the revised hypotheses
  and point to the exact paragraphs, not just added citations.
- *"Selection still not handled."* Add the within-unit or sensitivity analysis implied, report the direction
  and size of any change honestly, and align the claim to the new evidence.
- *"You ignored my main point."* Quote every comment verbatim and answer it; the editor scans for coverage,
  and a single skipped comment signals non-compliance.
- *"Revision drifted from the deposited data."* Regenerate the package so new exhibits reproduce, and say so
  (see `jmf-transparency-and-data-policy`).

## Calibration anchors (hedged where uncertain)

- Treating the R&R as a genuine opportunity rather than a soft rejection reflects JMF's norm that most
  publications iterate; NCFR describes reject, revise-and-resubmit, rare near-immediate acceptance, and
  written reconsideration for serious reviewer error. Protecting the family-science contribution while
  answering reviewers is the central balancing act; the editor's letter signals which points are decisive.

## Anti-patterns

- Ignoring or merging away a comment without a visible response
- Capitulating to a request that breaks the paper's logic just to please a reviewer
- Defensive or dismissive tone toward reviewers
- "We thank the reviewer" with no actual change or argued reason
- Adding analyses that quietly contradict the original claim without acknowledging it
- Letting the revised manuscript or new exhibits drift out of sync with the deposited materials

## Output format

```
【Editor's decisive points】addressed first? [list]
【Coverage】every reviewer comment answered? [Y/N]
【Concede vs rebut】each tagged with evidence + change location
【Reviewer conflicts】reconciled and explained to editor? [Y/N]
【Contribution protected】family-science significance not diluted? [Y/N]
【Anonymity + data materials updated】[Y/N]
【Next】resubmit via Wiley Research Exchange
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — review model, editorial process, and decision pathway
