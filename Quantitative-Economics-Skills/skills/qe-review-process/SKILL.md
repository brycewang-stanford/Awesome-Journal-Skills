---
name: qe-review-process
description: Use to understand and plan around the Quantitative Economics (QE) editorial timeline — desk-reject risk, external refereeing, ~4-5 month target turnaround, 12-month revise windows, the Econometrica-transfer route, and the pre-acceptance ES Data Editor check. Sets expectations; it does not draft the paper.
---

# Review Process (qe-review-process)

## When to trigger

- You want to calibrate expectations on timeline and desk-reject risk before submitting
- You are deciding whether to use the Econometrica-transfer option
- You need to understand who decides and what gates lie between submission and acceptance
- A long silence has you wondering whether the target turnaround has elapsed

## How QE review works (source map refreshed 2026-06-20; re-confirm on ES pages)

QE runs **editor/coeditor-managed external peer review**. The handling coeditor may **desk-reject without external review** (typically within a couple of weeks); most — but not all — papers that pass desk go to **one or more outside referees**, often including an Associate Editor. The journal targets completing the review process in **about four to five months**. QE is **not double-blind**, and authors must **post the manuscript publicly during review**, so author identity is effectively open on the author side. **Revise offers are normally valid for 12 months.** Wiley product metadata checked on 2026-06-20 lists **Bernard Salanié** as editor; reopen the current official board page before naming the full coeditor or associate-editor roster.

## Gates between submission and acceptance

1. **Membership + fee gate** — at least one author must be an ES member; the submission fee (US$100 / US$50 student) is paid at submission unless transferring from Econometrica or invited (low-income-country exemption applies).
2. **Desk screen** — handling coeditor decides whether to send out; a desk reject is fast and the fee is **not refunded** when rejected without review.
3. **External refereeing** — one or more referees / an AE; the coeditor synthesizes.
4. **Revision rounds** — the coeditor's letter sets binding vs. optional points; revise offers run ~12 months.
5. **Pre-acceptance reproducibility check** — before final acceptance the **ES Data Editor** process runs reproducibility checks; raw data, code, and documentation must already be in hand (see `qe-replication-and-data-policy`).

## The Econometrica-transfer route

A paper previously rejected by *Econometrica* can be submitted to QE with the **option to transfer** the coeditor decision letter, referee reports, and cover letters directly from Econometrica. The QE process is **fully independent** of Econometrica; the transfer **waives the QE submission fee** (other publication fees still apply); the paper needs a cover letter explaining how it differs and how the prior referee comments were addressed. Use this when the Econometrica reports are constructive and the paper's fit is genuinely the empirical/quantitative QE lane.

## Checklist

- [ ] Membership and fee (or transfer/exemption) settled before submitting
- [ ] Realistic timeline noted: ~2 weeks to a desk decision; ~4–5 months to a full review
- [ ] Manuscript posted publicly (review is open on the author side)
- [ ] If transferring: prior Econometrica reports addressed in a cover letter
- [ ] Replication package assembled in advance of the pre-acceptance Data Editor check
- [ ] Revise window (~12 months) tracked if an R&R arrives

## Anti-patterns

- Assuming anonymity — QE is not double-blind and the paper is posted publicly
- Submitting without the replication package, then scrambling at the Data Editor stage
- Treating an Econometrica transfer as automatic acceptance — QE re-decides independently
- Reading too much into silence before the ~4–5 month target has passed

## Desk-reject patterns to screen out before submitting

The handling coeditor screens fast; these are the quantitative-fit failures that draw a no-review rejection at QE.

| Desk-reject pattern | Pre-empt it by |
|---------------------|----------------|
| method-first paper with a toy application | reframe around the economic quantity (`qe-contribution-framing`) |
| no first-order economic question | sharpen fit before submitting (`qe-topic-selection`) |
| identification that cannot clear the ES bar | stress-test it (`qe-identification-strategy`) |
| significance asterisks, exhibits at the end | fix house style (`qe-tables-figures`, `qe-submission`) |
| data so locked the package cannot be built | plan an exemption at submission (`qe-replication-and-data-policy`) |

## Worked vignette: deciding the Econometrica-transfer route (illustrative)

Suppose a structural macro paper was rejected at Econometrica with two constructive reports questioning identification but praising the quantitative contribution. The transfer route fits: the reports are usable, the fee is waived, and the payoff is squarely the QE lane. The cover letter should state point by point how each identification concern was addressed (say, an added sensitivity matrix and Monte Carlo recovery). If instead the reports rejected the *premise*, fresh framing — not a transfer — is the better move. (Scenario illustrative.)

## Output format

```
【Stage】desk screen / out to referees / revision / pre-acceptance check
【Route】fresh submission / Econometrica transfer
【Timeline expectation】~2 wks desk; ~4-5 mo full review; ~12-mo revise window
【Open review noted】manuscript posted publicly? [Y/N]
【Data Editor readiness】package assembled? [Y/N]
【Next step】qe-submission (preflight) or qe-rebuttal (on R&R)
```
