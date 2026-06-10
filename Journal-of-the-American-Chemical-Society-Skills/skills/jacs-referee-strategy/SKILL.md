---
name: jacs-referee-strategy
description: Use when suggesting/excluding reviewers and pre-empting likely referee objections for a Journal of the American Chemical Society (JACS) manuscript. Plans the review-facing strategy — it does not run experiments or write the paper.
---

# Referee Strategy (jacs-referee-strategy)

## When to trigger

- You are choosing suggested and excluded reviewers for Paragon Plus
- You want to anticipate and disarm objections before submission
- You are stress-testing the manuscript as a skeptical referee would
- A revision is coming and you want to predict reviewer concerns

## Choosing reviewers

- **Suggested:** independent experts who can judge the chemistry — across the
  relevant subfields (e.g., a synthesis expert *and* a mechanism/spectroscopy
  expert for a catalysis paper). No collaborators, advisors, or same-institution.
- **Breadth coverage:** because JACS is broad-scope, include at least one
  reviewer who can speak to the general-interest claim, not only the niche.
- **Excluded:** only with a brief, professional reason (direct competitor with a
  conflict, prior dispute). Keep the list short and credible.

## Pre-empting the standard JACS objections

Referees at JACS predictably probe rigor and significance. Address each before
they raise it:

| Likely objection | Pre-empt by |
|------------------|-------------|
| "Not broad enough for JACS" | Lead with the breadth driver; cite cross-field relevance |
| "Compound X is not fully characterized" | Complete SI characterization + purity for every compound |
| "Purity not demonstrated" | EA or HPLC/GC trace + clean NMR for key compounds |
| "Mechanism is speculative" | Add controls, kinetics, KIE, or labeling; soften unproven steps |
| "Scope is cherry-picked" | Report failed substrates; show functional-group tolerance |
| "Selectivity claim unsupported" | Provide ee/dr with method and racemate/standard traces |
| "Crystal structure not deposited" | CCDC number + checkCIF-clean CIF |
| "Yields/conditions not reproducible" | Procedures with scale/equiv; replicate key results |
| "Over-claimed novelty" | State closest prior art and the specific delta |

## Reviewer-simulation pass

Read the manuscript once as a hostile referee and write the three harshest
defensible criticisms. For each, decide: (a) fix now with data, (b) soften the
claim, or (c) prepare a rebuttal point. Carry these into `jacs-revision`.

## Checklist

- [ ] Suggested reviewers are independent and cover the needed expertise + breadth
- [ ] Excluded reviewers (if any) have a brief, professional justification
- [ ] Each standard objection above is addressed or has a planned response
- [ ] The three harshest defensible criticisms are written down
- [ ] Unproven claims are softened in language before submission
- [ ] Prior-art delta is explicit, pre-empting "incremental" charges

## Anti-patterns

- Suggesting friends/collaborators as reviewers (editors notice)
- Excluding everyone competent under vague "competitor" claims
- Ignoring an obvious rigor gap and hoping a referee misses it
- Leaving an over-claim in place that a referee will seize on
- No breadth-competent reviewer for a paper whose pitch is broad interest


## Operating pass for Journal of the American Chemical Society

Treat this skill as an executable review pass, not a prose hint. First lock the chemical novelty, characterization chain, controls, and scope or mechanism evidence; then judge whether the current manuscript answers the venue's real reader: chemistry reviewers who expect a molecule/material/reaction claim to be supported by rigorous characterization and mechanistic insight.

- **Do the pass:** Return a claim-evidence-risk ledger rather than a prose-only diagnosis; every recommendation must point to a manuscript location or missing artifact.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against ACS Central Science for broad conceptual reach, Angewandte for communication style, specialized ACS journals for narrower chemistry; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Stop condition:** do not give submission-ready advice until the pack's `resources/official-source-map.md` has been checked for volatile rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Suggested】names/areas: synthesis [..], mechanism [..], breadth [..]
【Excluded】name — reason (brief)
【Objections pre-empted】[...]; planned rebuttals: [...]
【Top-3 hostile criticisms】1) ... 2) ... 3) ...
【Actions】fix-now: [...]; soften: [...]
【Next】jacs-submission (suggestions) → jacs-revision (after decision)
```

## Related resources

- [`jacs-cover-letter`](../jacs-cover-letter/SKILL.md) — where suggested/excluded reviewers are noted
- [`jacs-methods`](../jacs-methods/SKILL.md) — closing the rigor gaps referees probe
