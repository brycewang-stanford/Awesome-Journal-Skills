---
name: joap-review-process
description: Use when you need to understand how the Journal of Applied Psychology (JAP) evaluates a manuscript — masked (anonymized) peer review, the action-editor model, the dual gate of theoretical contribution and measurement/design rigor, and common desk-reject patterns. Use when stress-testing a paper before submission or interpreting a decision letter. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (joap-review-process)

JAP is selective and exacting. Reviewers and the action editor weigh **theoretical contribution** and
**methodological rigor together** — an interesting finding with weak measurement, and a flawless design
with no theory advance, are both common rejections. Review is **masked (anonymized)**. Knowing how the
gate works lets you pre-empt the standard rejection reasons.

## When to trigger

- Before submitting, to stress-test the manuscript
- Deciding how to frame the contribution and rigor for masked reviewers
- Interpreting a decision letter and setting expectations

## How review works

1. **Masked review.** Author identities are withheld throughout consideration; keep names out of the
   manuscript and out of repository/preregistration links (see `joap-submission`).
2. **Editorial triage.** The editor / action editor screens for fit, theoretical contribution, and
   rigor; weak-fit or atheoretical papers are frequently **desk rejected** without full review.
3. **Action-editor model.** An associate/action editor manages the manuscript and several reviewers and
   writes the decision; the editor's letter is the rubric you must satisfy on revision.
4. **External review** assesses the theoretical contribution, construct validity and measurement,
   design and causal warrant, analysis (SEM/HLM/mediation/meta-analysis), and transparency.
5. **Transparency is weighed.** TOP-aligned data/materials/code sharing and preregistration factor into
   evaluation; opacity is a mark against the paper.
6. **Decisions.** Reject, major/minor revise-and-resubmit, or accept; expect a demanding R&R, often
   across multiple rounds, before acceptance.

## The dual gate (what gets papers in)

| Gate | What reviewers ask | Where to fix it |
|------|--------------------|-----------------|
| Theoretical contribution | Is there a new mechanism/boundary/integration? | `joap-theory-and-hypotheses`, `joap-literature-positioning` |
| Construct validity / measurement | Are the constructs validly measured? | `joap-study-design` |
| Causal / inferential warrant | Does the design support the claim (CMV, nesting)? | `joap-study-design`, `joap-data-analysis` |
| Analytic rigor | SEM fit, indirect-effect CIs, multilevel done right? | `joap-data-analysis` |
| Transparency | Data/materials/code shared under TOP? | `joap-open-science-and-transparency` |

## Desk-reject and decline-without-review patterns

The dual gate means many manuscripts never reach external review. Confirm current categories on the
official page, but recognize these shapes:

| Pattern an editor sees | Likely outcome | Pre-empt it by |
|------------------------|----------------|----------------|
| Rigorous study, no theoretical advance | desk reject | state the new mechanism/boundary/integration up front |
| Cross-sectional single-source self-report | desk reject (rigor) | add temporal/source separation or an experimental leg |
| Better fit for a sibling venue | desk reject (fit) | make the I-O micro/measurement contribution explicit |
| Mediation by Sobel/steps; OLS on nested data | thin-method flag | modern indirect-effect CIs; multilevel models |
| "Data available on request," no DOIs | returned for compliance | deposit with persistent IDs before submitting |

## Worked micro-example (illustrative triage)

```
Manuscript: two-wave multilevel field study (612 in 74 teams) + lab experiment,
            servant leadership → safety → performance, open data/materials/code,
            experiment preregistered, indirect-effect CI reported.
Editor read: contribution (cross-level mechanism + boundary), rigor (temporal +
            multilevel + experimental leg), transparency (TOP-aligned — strong).
Likely route: external review, probable major R&R (added robustness/alternative
            models, sharper boundary theory).
Counter-case: same finding, one cross-sectional single-source survey, no prereg,
            request-only data → likely desk reject.
```

## How reviewers weigh the evidence (calibration anchors)

- The single strongest signal is **theory + rigor together**: a clear mechanism *and* a design that can
  bear the causal/cumulative claim. Either alone usually loses.
- A causal leg (experiment or field experiment) attached to a field study converts "interesting
  correlation" into "credible mechanism."
- Transparency is weighed, not pass/fail — a candid exemption with an access path reads better than
  silent opacity; preregistration *quality* matters more than mere presence.
- Expect multiple R&R rounds; reviewers test alternative explanations and measurement rivals hard.

## Anti-patterns

- A rigorous but atheoretical paper (the venue's most common rejection)
- Cross-sectional single-source self-report as the whole evidentiary base
- Exploratory results dressed as confirmatory
- Weak or absent transparency (counts against the paper)
- Expecting acceptance without a demanding, multi-round R&R

## Output format

```
【Theoretical contribution】clear + new? [Y/N]
【Construct validity / measurement】adequate? [Y/N]
【Causal / inferential warrant】CMV + nesting handled? [Y/N]
【Analytic rigor】SEM fit / indirect CIs / multilevel correct? [Y/N]
【Transparency】data/materials/code + preregistration strong? [Y/N]
【Realistic outcome】desk reject / R&R / accept
【Next】joap-submission (or joap-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — masked review model, TOP weighting, action-editor process
