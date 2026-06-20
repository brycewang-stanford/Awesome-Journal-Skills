---
name: jop-review-process
description: Use to understand how The Journal of Politics (JOP) evaluates a manuscript — double-blind review, desk screening for fit and general interest, an efficiency-minded review process, and acceptance that is contingent on replicability checked by a JOP replication analyst. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (jop-review-process)

Knowing how JOP screens and decides lets you pre-empt failure modes before submitting. JOP is
**double-blind**, screens for **general interest and fit**, is known for a relatively **efficient**
review process, and ties final acceptance to **replicability** assessed by a **JOP replication analyst**.

## When to trigger

- Before submitting, to stress-test fit and replicability
- Interpreting a decision letter and setting expectations
- Understanding what happens between conditional acceptance and publication
- Deciding whether the paper reads as general-interest enough to clear desk screening

## How JOP review works

1. **Double-blind.** Reviewers do not know the authors and authors do not know reviewers. Upload an
   anonymous version of the manuscript (see `jop-submission`).
2. **Desk screening.** Editors screen for **fit and general interest** — is this political science of
   broad interest, sufficiently novel, and within scope and category limits? Specialist-only or
   incremental papers are at risk here.
3. **External review.** Papers passing the desk go to expert reviewers across the relevant subfield(s).
4. **Decision categories**: typically **reject**, **revise and resubmit**, or **accept** — and JOP is
   reputed for an **efficient** process (treat speed as a qualitative norm, not a guaranteed clock).
5. **Conditional acceptance → replication check.** Acceptance is **contingent on replicability**: a
   **JOP replication analyst** assesses the deposited package before publication, and **non-replicable
   manuscripts are rejected** (see `jop-replication-and-data-policy`).

## Shape the paper to pass

- Make **general interest** explicit early (clears the fit/scope desk screen).
- Lead with the **theoretical innovation** JOP prizes.
- Stay **within the page budget** and category (Research Article ≤ 35 pp / Short Article ≤ 10 pp).
- Engineer **replicability from day one** so the post-acceptance analyst check is routine, not a scramble.
- Clear ethics/IRB and human-subjects compliance up front.

## Anti-patterns

- Submitting a specialist-only paper to a general-interest journal (fit desk screen)
- Over-length or wrong-category submission (page-budget screen)
- Assuming a guaranteed turnaround because JOP is "fast" — speed is a norm, not a promise
- Treating acceptance as final before the replication analyst has signed off

## The gauntlet, stage by stage

Each stage is a separate filter with its own failure mode. Most avoidable rejections happen at the first
two, before a reviewer ever reads the argument.

| Stage | What clears it | What it screens out |
|-------|----------------|---------------------|
| Anonymity / format upload | Anonymous file, correct category, within page budget | Identifying metadata, over-length, wrong category |
| Desk screen (editor) | Explicit general interest, clear non-incremental contribution | Specialist-only or incremental framing |
| External review | Credible identification/logic, theory linked to test | Loose theory-test link, fragile design |
| Conditional accept → analyst | Deposited code regenerates every printed number | Non-replicable package (→ rejected) |

## Referee pushback patterns and the JOP fix

- *"Theory and test are loosely linked."* Make the empirical test follow from the argument's stated
  mechanism or comparative statics, not a loose analogy, so a reviewer sees the prediction is unique.
- *"This is below the journal's bar."* The bar is general interest plus theoretical innovation; lead with
  the portable contribution early so the desk editor sees it without hunting.


## Review-risk pass for Journal of Politics

Treat this skill as an executable review pass, not a prose hint. First lock the political mechanism, evidence design, and scope condition; then judge whether the current manuscript answers the venue's real reader: political-science reviewers who want theory, identification or formal logic, and generalizable political implications in balance.

- **Do the pass:** Turn probable reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against APSR for field-wide political science, AJPS for design-heavy empirical work, World Politics for comparative/international politics; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Desk-screen check】general interest + fit + scope — any red flags?
【Innovation】novel enough to clear "incremental"? [Y/N]
【Category + length】correct category, within page budget? [Y/N]
【Replicability】package ready for the analyst at conditional accept? [Y/N]
【Realistic outcome】reject / R&R / accept
【Next】jop-submission (or jop-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — JOP double-blind review, scope, and replicability-contingent acceptance
