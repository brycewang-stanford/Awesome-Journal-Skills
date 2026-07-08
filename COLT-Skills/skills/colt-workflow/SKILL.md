---
name: colt-workflow
description: Use when planning a COLT (Conference on Learning Theory) submission calendar backward from the single AoE paper deadline — proof-completion and verification milestones, writing and appendix-assembly passes, CMT logistics, the rebuttal window, decision aftermath, and PMLR camera-ready with conference presentation in early summer.
---

# COLT Workflow

Use this as the project-management layer for a COLT paper. Anchor everything to the
live timetable: for the 39th edition the CFP (checked 2026-07-08) set one submission
deadline — February 4, 2026, Anywhere on Earth, via CMT — for a conference running
June 29 to July 3, 2026 in San Diego. Notification and camera-ready dates were not on
the checked pages (待核实); take them from the CFP and acceptance email of your cycle.

## Stage map

- **Fit decision**: confirm the contribution is a theorem a learning theorist wants
  (see `colt-topic-selection`); if the result is 80% proved, the clock question is
  whether the remaining 20% is verification or invention — only the first is
  schedulable.
- **Result freeze**: theorem statements stop moving. At COLT this is the single most
  important date you control, because every downstream artifact (proof appendix,
  overviews, comparisons) quotes the statements.
- **Verification**: independent re-derivation of every load-bearing proof
  (`colt-reproducibility`). Schedule it as real work with an owner per theorem — it
  finds bugs at a rate authors never want to believe.
- **Writing**: body-first is a mistake here; write the appendix proofs first, then
  distill overviews into the body, so the body never promises what the appendix
  cannot deliver.
- **Submission week**: CMT record early, anonymity sweep, single-PDF assembly
  (`colt-submission`).
- **Rebuttal**: reviews arrive before decisions; block calendar capacity for the
  window even before you know its dates (`colt-author-response`).
- **Aftermath**: acceptance → PMLR camera-ready and talk prep (`colt-camera-ready`);
  rejection → triage between fix-and-resubmit (next COLT / ALT) and re-routing.

## Backward plan from the deadline

| Weeks before deadline | Milestone | Failure smell |
|---|---|---|
| 10+ | All main results proved at whiteboard level | "The lower bound should follow" — it does not, yet |
| 8 | Theorem statements frozen; ledger of claims opened | Statements still absorbing scope changes |
| 6 | Full proofs written in LaTeX, appendix-structured | Proofs alive only in notebooks and heads |
| 4 | Independent verification pass complete; bugs triaged | "We'll verify while writing" (you will not) |
| 3 | Body drafted: setup, results, proof overviews, known-vs-new table | Overview promises diverging from actual proofs |
| 2 | Internal mock review by an uninvolved theorist | No one external has read the model section |
| 1 | Anonymity sweep, notation audit, cross-reference check | Renumbering theorems this late |
| 0 | Upload, re-download, verify the stored PDF; stop editing | Compiling at the AoE boundary |

Weeks are heuristics; the deadline is not. AoE means when it is February 4 anywhere
on Earth — compute your local cutoff and subtract a safety day.

## Verification is the critical path

For a theory paper the long pole is never the writing; it is discovering at week 2
that Lemma 6 is false. Mitigations:

- Verify in dependency order, most-load-bearing first — a bug in the master lemma
  invalidates weeks of downstream polishing.
- When a bug appears, immediately re-derive the *weakest still-true statement* and
  check whether the paper survives with it; many COLT papers ship the weaker constant
  that week-3 debugging forced.
- Maintain the claim ledger (see `colt-artifact-evaluation`) as the single source of
  verification status; standups read the ledger, not vibes.

## Team coordination template

```text
# colt-plan.txt
DEADLINE (AoE):        2026-02-04  -> local cutoff 2026-02-05 11:59 UTC-12
RESULT FREEZE:         2025-12-10  owner: all
PROOF APPENDIX DRAFT:  2025-12-22  owner: A (Thm 1), B (Thm 2, lower bound)
VERIFICATION PASS:     2026-01-09  owner: swap (B checks Thm 1, A checks Thm 2)
BODY + OVERVIEWS:      2026-01-16  owner: A
MOCK REVIEW:           2026-01-21  reader: C (not a coauthor)
ANONYMITY + PDF QA:    2026-01-28  owner: B
UPLOAD TARGET:         2026-02-02  (two days of slack, CMT record made 01-25)
REBUTTAL WINDOW:       dates TBA with reviews -> block capacity on release
```

## Workflow failure modes specific to theory papers

- **The moving theorem:** a coauthor strengthens a statement during the writing
  phase without re-opening its ledger entry; the appendix now proves the old claim.
  Rule: statement edits after freeze require a ledger re-verification, no exceptions.
- **The optimistic lower bound:** upper bound done, lower bound "clearly similar to
  [X]" and scheduled for week 2. Lower bounds are inventions, not chores — either
  prove it before freeze or descope the paper to the upper bound honestly.
- **The single-verifier trap:** the only person who checked Theorem 2 is the person
  who proved it. Swap verification assignments explicitly (the plan file above does).
- **The deadline compile:** first full single-PDF build in the final 48 hours,
  discovering the restatement macros and cross-references were never wired. Build the
  full document skeleton — body, appendix, references — by week 3 even while proofs
  are placeholders.

## After the decision

- Accepted: camera-ready per instructions; book San Diego-style summer logistics
  early (single-track conference, one venue hotel); decide who talks.
- Rejected with deep reviews: the reviews are a free verification report — patch and
  target the next cycle or ALT (deadline typically in autumn; verify).
- Rejected for significance: the mathematics may be sound but mis-framed; rework the
  motivation and known-vs-new ledger before blaming the result.
- Either way, reconcile the arXiv version with what review taught you.
- Debrief the ledger: which claims did reviewers actually verify, and did your
  internal verification pass catch what they caught? Calibrating that gap improves
  the next paper's schedule more than any template.

## Cycle-volatility warnings

- Every date above except the verified 2026 deadline and conference dates is
  cycle-specific; notification, rebuttal window, camera-ready, and registration
  timing are 待核实 until announced.
- Whether an Open Problems track (with its own deadline) runs in your cycle: check
  the CFP; the 2025 edition ran one with a later, non-anonymous, 4-page format.

## Output format

```text
[Stage] proving / freeze / verification / writing / submitted / rebuttal / decision
[Critical path] <the unverified claim or unwritten proof gating everything>
[Calendar] <next official date + source, or 待核实>
[Owner map] <theorem/task -> person>
[Slack] <days between planned upload and AoE cutoff>
```
