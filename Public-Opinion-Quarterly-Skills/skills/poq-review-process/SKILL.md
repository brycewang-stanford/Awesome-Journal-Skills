---
name: poq-review-process
description: Use to understand how Public Opinion Quarterly (POQ) evaluates a manuscript — double-blind review via ScholarOne Manuscripts, typically two to three referees, the survey-methodology and AAPOR-disclosure bar reviewers apply, and how associate editors may request code/data during review. Sets expectations and shapes the paper to survive review; it does not contact editors.
---

# Review Process (poq-review-process)

Knowing how POQ screens and decides lets you pre-empt the failure modes before submitting. POQ runs a
**double-blind** process via **ScholarOne Manuscripts**, with manuscripts typically evaluated by **at
least two (most often three) referees** who are survey scientists. They will scrutinize survey error
and **AAPOR-standard disclosure** as hard as the substantive claim.

## When to trigger

- Before submitting, to stress-test against the failure modes POQ reviewers catch
- Choosing the submission type and anticipating reviewer expectations for it
- Interpreting a decision letter and setting expectations
- Understanding what associate editors may request (code/data) during review

## How POQ review works

1. **Double-blind.** Reviewers do not know the authors and authors do not know reviewers. Anonymize the
   manuscript accordingly (see `poq-submission`).
2. **Editorial handling.** An associate editor manages the paper; the **AE may request code and data as
   a necessary part of peer review** — have your replication materials ready, not just at acceptance.
3. **Referees.** Typically **two to three** expert referees evaluate the work.
4. **What referees weigh** (POQ-specific):
   - **Contribution** — to opinion/communication theory, current opinion, or survey validity.
   - **Survey design & Total Survey Error** — coverage, sampling, nonresponse, measurement, mode, weighting.
   - **AAPOR disclosure** — is **Appendix A** complete? Is the **response rate computed per AAPOR
     Standard Definitions**? Are sampling and weighting documented?
   - **Analysis** — design-based inference; reproducibility.
5. **Decision categories** — reject, revise-and-resubmit, or accept (typical journal practice; confirm
   current wording — 待核实). Acceptance generally needs the referees persuaded on both substance and
   method.

## Shape the paper to pass

- Make the contribution type explicit (opinion vs. methods) so referees judge it on the right terms.
- Complete **Appendix A** and report the response rate per AAPOR definitions before submitting — a
  missing disclosure element is an easy, avoidable strike.
- Use design-based inference; weights/strata/clusters in the variance, not just the estimate.
- Have replication materials ready in case the AE requests them during review.
- Anticipate the artifact-vs-effect objection and answer it in the design (see
  `poq-survey-design-and-measurement`).

## Anti-patterns

- An incomplete or missing Appendix A (disclosure failure reviewers flag immediately)
- A response rate with no AAPOR definition; undocumented weighting
- Naive IID inference on a complex sample
- Assuming code/data are only needed at acceptance — the AE may ask during review
- Sending an under-anonymized manuscript into a double-blind process


## Review-risk pass for Public Opinion Quarterly

Run this as a concrete capability pass. First lock the public-opinion construct, sampling frame, mode effects, weighting/nonresponse plan, and trend or causal interpretation; then test whether the manuscript addresses survey and public-opinion reviewers who inspect measurement, sampling, mode, nonresponse, and inference about attitudes or behavior.

- **Primary move:** Turn likely reviewer objections into a ledger with response evidence, manuscript location, and the decision-maker who must be convinced first.
- **Decision ledger:** return `claim / evidence / blocker / next edit` rows so the next pass can patch the manuscript directly.
- **Sibling comparison:** compare against Political Analysis for methods-first work, Journal of Politics for political-science theory, Communication Research for media-effects framing; if the neighboring outlet has the stronger audience claim, recommend re-routing before polishing.
- **Verification floor:** before submission-ready advice, re-open `resources/official-source-map.md` for volatile rules and name the one unresolved fact that could change the recommendation.

## Output format

```
【Contribution clear】opinion / current-opinion / survey-validity? [Y/N]
【TSE addressed】coverage/sampling/nonresponse/measurement/mode/weighting? [Y/N]
【Appendix A + AAPOR response rate】complete? [Y/N]
【Design-based inference】weights/strata/clusters in variance? [Y/N]
【Replication ready for AE request】[Y/N]
【Realistic outcome】reject / R&R / (rare) accept
【Next】poq-submission (or poq-rebuttal if decided)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — disclosure checklist and design-based analysis tools
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — double-blind review, referee count, AE code/data requests
