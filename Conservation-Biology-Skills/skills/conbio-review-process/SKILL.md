---
name: conbio-review-process
description: Use to understand how Conservation Biology evaluates a manuscript — double-blind peer review (adopted 2014), editorial screening for scope/novelty/conservation relevance, the editorial-board structure, decision categories, and the Registered Reports route. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (conbio-review-process)

Knowing how *Conservation Biology* screens and decides lets you pre-empt the failure modes before
submitting. The journal is **double-blind** (adopted October 2014) and screens at the desk for scope,
novelty, and conservation relevance before external review.

## When to trigger

- Before submitting, to stress-test against desk-rejection grounds
- Deciding whether to use the **Registered Reports** route (where offered)
- Interpreting a decision letter and setting expectations
- Understanding what reviewers are instructed to weigh

## How review works

1. **Double-blind.** Neither authors nor reviewers know each other's identities; the manuscript and the
   authors' identities are anonymized (see `conbio-submission`). Adopted to reduce intentional and
   unintentional bias and broaden participation.
2. **Editorial screening first.** An editor (and, in the journal's editorial structure, regional/
   handling editors) screens for **fit and conservation relevance**, **novelty/transferability**,
   adequate **English and completeness**, and **ethics**. Papers that are sound but inconsequential, or
   purely local/descriptive, are common desk rejections.
3. **External review.** Papers passing the desk go to expert reviewers, who weigh novelty,
   transferability, methodological soundness, and **direct implications for conservation**.
4. **Decision categories**: typically **reject**, **major/minor revision (revise and resubmit)**, or
   **accept**. Expect revision rather than outright acceptance on a first decision.
5. **Registered Reports** (where offered): a **two-stage** route — Stage 1 (introduction + protocol) is
   reviewed and can receive **in-principle acceptance** before data are collected/analyzed; Stage 2 adds
   Results and Discussion. Choose this **before** you have results.

## Shape the paper to pass

- Make **conservation relevance and transferability explicit** (avoids the "sound but inconsequential"
  desk rejection — see `conbio-conservation-relevance-and-implications`).
- Engage the relevant conservation literatures, including across disciplines.
- Match methods to the question and address detection, scale, and counterfactuals up front.
- Clear ethics, permits, animal-care/IRB, and sensitive-data handling.

## Desk-rejection triage (self-run before upload)

Editors screen at the desk before spending reviewer time, so pre-empt the four recurring grounds:

| Screening ground | Failing manuscript | Fix before submitting |
|------------------|--------------------|-----------------------|
| Conservation relevance | "Sound but inconsequential"; no decision named | Complete the actionability sentence (`conbio-conservation-relevance-and-implications`) |
| Novelty / transferability | A local first-record or single-site description | Generalize the mechanism or decision rule so the lesson travels |
| Scope fit | Belongs in a sibling venue | Re-route (see sibling guard) rather than force the fit |
| Completeness / ethics | Missing permits, data statement, or masking | Clear `conbio-reporting-and-data-policy` and permit declarations first |

**Worked triage.** A clean occupancy study of one reserve, framed as "we document species X at site Y,"
reads as descriptive and local — a likely desk rejection. Reframed as "occupancy declines with edge
density, so managers should buffer reserve edges when expanding," it names a decision and a transferable
rule, and clears the relevance and novelty screens.

## What Conservation Biology reviewers are asked to weigh

Reviewers judge, in roughly this priority: whether the result has **direct implications for conserving
biological diversity**; whether the design matches the ecological question (detection, scale,
counterfactuals, pseudoreplication); whether uncertainty is honestly propagated into any recommendation;
and whether the transferable lesson is stated without over-claiming. A methodologically clean paper that
cannot answer "what conservation decision does this change?" is the modal reject. Anticipate this by
writing the implications paragraph *for the reviewer*, not just the specialist.

## Anti-patterns

- Submitting a local/descriptive study with no transferable conservation lesson
- Ignoring an obvious related literature
- Expecting acceptance without revision on a first decision
- Choosing Registered Reports after results exist
- Leaving author identity detectable in a double-blind submission


## Review-risk pass for Conservation Biology

Treat this skill as an executable review pass, not a prose hint. First lock the species/system threat, conservation decision, and uncertainty relevant to action; then judge whether the current manuscript answers the venue's real reader: conservation-science reviewers who ask whether evidence changes biodiversity, management, or policy action.

- **Do the pass:** Turn probable reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Return a ledger:** give `claim / evidence / risk / manuscript location` rows, so the next agent can edit rather than rediscover the issue.
- **Sibling guard:** compare against Biological Conservation for applied conservation breadth, Global Change Biology for climate/ecosystem process, Ecology Letters for theory-forward ecology; if a sibling owns the contribution, recommend re-routing before polishing format.
- **Submission-ready gate:** do not give final advice until the pack's `resources/official-source-map.md` has been checked for upload-week rules and the manuscript has one concrete fix for the largest venue-specific risk.

## Output format

```
【Desk-rejection check】scope / relevance / novelty / completeness / ethics — red flags?
【Conservation relevance】explicit and transferable? [Y/N]
【Literature engaged】incl. cross-disciplinary? [Y/N]
【Route】standard vs Registered Reports (Stage 1)
【Realistic outcome】reject / major-minor revision / (rare) accept
【Next】conbio-submission (or conbio-revision-and-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind policy, reviewer guidelines, decision categories, Registered Reports
