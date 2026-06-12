---
name: jpsp-review-process
description: Use to understand how a Journal of Personality and Social Psychology (JPSP) manuscript is judged — per-section editors, masked review, the theoretical-innovation gate, central vs. peripheral limitations, and decision categories. Sets expectations; it does not predict any specific editor's or reviewer's verdict.
---

# Review Process — Per Section (jpsp-review-process)

JPSP is reviewed **inside one of three independently edited sections**, by an editor and reviewers
who are **mutually masked** to the authors. Knowing how *your* section frames decisions helps you
anticipate what reviewers will ask. The IRGP section has published an unusually explicit review model
(below); ASC and PPID share the masked, theory-first culture but set their own specifics (verify).

## When to trigger

- Anticipating how the section will evaluate the paper before submitting
- Interpreting a decision letter's framing (innovation, central vs. peripheral limitations)
- Deciding whether a prospective design should be a Registered Report (Stage 1)

## How the section judges a paper

1. **Section routing.** The paper is handled by the editor of the section you submitted to (ASC, IRGP,
   or PPID); a mis-fit paper can be re-routed or returned. Choose the section deliberately
   (`jpsp-topic-selection`).
2. **Triage.** Papers limited in theoretical scope or methodologically deficient may be **triaged
   (desk-screened)** so authors can move on quickly (IRGP guidance; verify per section).
3. **Innovation gate.** Reviewers first judge whether the **underlying ideas** are sufficiently
   innovative/generative — often *independent* of data strength. A "no" focuses the review on why the
   theoretical bar is unmet; a "yes/probably yes" moves to evaluating the studies.
4. **Central vs. peripheral limitations (IRGP).** Reviewers categorize limitations as **central**
   (must be fixed for the studies to be interpretable) or **peripheral** (could be fixed but the work
   is already compelling), and central ones as addressable with **existing** vs. **new** data.
5. **Decision categories (IRGP, verify per section):**
   - **Accept with revision** — may be offered on the **first round** when the paper is sufficiently
     innovative with **no central limitations**.
   - **Revise and resubmit** — central limitations addressable with **existing** studies/data.
   - **Reject** — central limitations require **new** studies/data (a later resubmission with new data
     is treated as a **new** submission).
   Revised manuscripts are often decided **without further reviews**.
6. **Masked review.** Both directions masked — keep identity out of text, files, and repository links.

## Anti-patterns

- Submitting to the wrong section and hoping the editor re-routes favorably
- Leading with method polish when the **idea** has not cleared the innovation gate
- Treating an R&R as acceptance — central limitations still gate the decision
- Resubmitting a rejected paper with brand-new data and expecting continuity (it is a new submission)
- De-anonymizing yourself via self-references or repository URLs

## Desk-screen patterns the three sections share

Across ASC, IRGP, and PPID the editor-level screen rejects on a small set of recurring failures. Treat these as illustrative of the post-credibility-revolution culture rather than codified rules — confirm current section policy against the journal's submission guidelines (待核实).

| Desk-screen pattern | What it signals to the section editor | Pre-empt by |
|---------------------|----------------------------------------|-------------|
| Single-study submission | Not built to the long-format, multi-study standard | A converging package (`jpsp-study-design`) before submitting |
| Thin theory, clean effect | Fails the innovation gate independent of data | A theoretical advance, not a demonstration (`jpsp-theory-and-hypotheses`) |
| Wrong section | Mis-fit for the editor's masthead and readers | Deliberate section choice (`jpsp-topic-selection`) |
| Under-masked manuscript | Breaks masked review | Strip names, self-refs, metadata, repo URLs (`jpsp-submission`) |
| Missing JARS / TOP disclosures | Transparency floor unmet | Complete JARS + TOP Level 2 statements (`jpsp-open-science-and-transparency`) |
| Underpowered key study | Central interpretability risk | Power against the smallest effect of interest |

## Worked example: tracing a package through the gate

*Illustrative — invented to show the decision sequence, not a real verdict.*

An IRGP submission claims a new group-identity moderator across four studies (illustrative pooled d = 0.29, 95% CI [0.16, 0.42]).

1. **Routing.** Unit of analysis is the group → IRGP, not ASC; a mis-route risks a return.
2. **Innovation gate.** The moderator reconciles two conflicting findings → "probably yes," so review proceeds to the studies.
3. **Central vs. peripheral.** Reviewers flag S3's N = 80 dyads as *central, existing-data* (re-analyzable) but call a missing manipulation check *peripheral*.
4. **Decision.** No central limitation needs new data → **R&R**, often decided **without further review**. Had S3 required a brand-new sample, a later resubmission would count as a **new** submission.

## Output format

```
【Section + editor stream】ASC / IRGP / PPID
【Innovation gate】is the idea a "yes/probably yes"? why
【Likely limitations】central vs peripheral; existing vs new data to fix
【Plausible decision】accept-with-revision / R&R / reject (section-specific)
【Registered Report?】if prospective, Stage 1 considered?
【Next】jpsp-submission (pre-submit) or jpsp-rebuttal (on decision)
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — preregistration / Registered Report tooling
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — IRGP review model, masked-review policy, per-section editors
