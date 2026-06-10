---
name: pom-contribution-framing
description: Use when framing the contribution of a Production and Operations Management (POM) manuscript — stating the managerial insight for practicing operations managers and the advance to OM knowledge, tied to the target Department. Frames the contribution; it does not run the analysis (pom-data-analysis) or polish prose (pom-writing-style).
---

# Contribution Framing (pom-contribution-framing)

## When to trigger

- The paper has technical material but the "so what" is thin
- A reviewer says the contribution is incremental or "not relevant to practice"
- The managerial takeaway is implicit and editors must infer it
- You have results but cannot say in one sentence what a manager does differently

## POM's twin gate: knowledge AND practice

POM's central acceptance question is whether the work is of **significant interest to practicing operations managers** *and* makes a **substantial contribution to knowledge and practice**. Frame both, explicitly — a contribution that advances theory but offers no operational lever, or improves an operational metric with no generalizable insight, sits below the bar.

## Build the contribution in this order

1. **Decision maker & decision.** Name the operations actor (plant manager, supply-chain planner, hospital operations lead, platform operator) and the choice they face under constraints.
2. **Knowledge gap.** What does the target Department's OM literature not yet explain or solve?
3. **Practice gap.** What can managers not currently decide well — and what does it cost them?
4. **The result as a lever.** Give at least one result that **changes practice** (a policy, contract term, staffing rule, sourcing decision) and one that **advances OM theory** (a mechanism, structural property, or empirical regularity).
5. **Department fit.** State explicitly which Department this contributes to, so routing and framing align.

## Translate technique into managerial language

Convert comparative statics, coefficients, or model accuracy into operational consequences: cost saved, fill rate gained, waiting time cut, disruption risk reduced. POM reviewers and the practice-oriented award culture (e.g., the Cheryl Gaimon Best Innovation Paper and Wickham Skinner awards, tied to POMS and the Annual Conference) reward insight that an operations manager can act on.

## Avoid

- "We are the first to model/measure X" with no mechanism or lever.
- Pure performance improvement (faster solver, higher accuracy) with no operations interpretation.
- Practice implications that are vague or not actionable.
- Leaving Department fit implicit for editors to guess.

## Checklist

- [ ] Decision maker and decision named
- [ ] Knowledge gap and practice gap both stated
- [ ] One practice-changing result and one theory-advancing result identified
- [ ] Results expressed as operational levers, not just signs/coefficients
- [ ] Target Department fit stated explicitly


## Contribution pass for Production and Operations Management

Treat this skill as an executable review pass, not a prose hint. First lock the operational decision, the performance metric, and the implementable lever; then judge whether the current manuscript answers the venue's real reader: POM reviewers who want operational insight tied to production, service, supply-chain, or platform decisions.

- **Do the pass:** Translate the result into who learns what, which mechanism changes, and which alternative explanation is ruled out; keep the contribution narrower than the evidence.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Management Science for broader OR/MS theory, Operations Research for method-first optimization, MSOM for manufacturing/service operations depth; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Decision maker】<operations actor>
【Decision】<choice under constraints>
【Knowledge gap】<what OM literature lacks>
【Practice gap】<what managers cannot decide well + cost>
【Practice lever】<decision changed by the result>
【Theory advance】<mechanism / structural / empirical contribution>
【Department fit】<target POM department>
【Next step】pom-tables-figures or pom-writing-style
```
