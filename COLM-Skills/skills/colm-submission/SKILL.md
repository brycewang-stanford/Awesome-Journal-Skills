---
name: colm-submission
description: Use when preparing or auditing a COLM submission on OpenReview — the late-March abstract and full-paper deadlines, the strict 9-page main text, double-blind rules banning acknowledgments and identity links, the Code of Ethics acknowledgment, LLM-usage disclosure, reciprocal-reviewer nomination, and pre-upload risk triage.
---

# COLM Submission

Everything below is the COLM 2026 cycle as read from `colmweb.org` on 2026-07-08.
COLM re-issues its instructions each edition and has already changed details between
2024, 2025, and 2026 — reopen the current submission-instructions page before acting
on any number here.

## The 2026 mechanics

- **Two deadlines a week apart:** abstract March 26, 2026; full paper March 31,
  2026. The abstract is not decorative — it routes reviewer bidding — so submit the
  real abstract, not a stub you plan to overwrite.
- **Platform:** OpenReview, group `colmweb.org/COLM/2026/Conference`, opened
  February 2026. Every author needs an OpenReview profile with current affiliation
  and publication history *before* the deadline; profile gaps break conflict
  detection and can strand the submission.
- **Format:** a **strict 9-page upper limit on main text**, with unlimited
  additional pages for citations. An optional acknowledgments section (≤ 1 page)
  sits outside the limit — but in the *submitted* version there must be no
  acknowledgments at all, because review is double-blind.
- **Anonymity:** no author names, no acknowledgments, and no links that resolve to
  you — the instructions call out GitHub links explicitly. LM papers leak identity
  through unusual channels; sweep them (next section).
- **Code of Ethics:** every author must read it and explicitly acknowledge it in the
  submission form. Reviewers are encouraged to flag violations, so treat the
  acknowledgment as a real audit, not a checkbox.
- **LLM-usage disclosure:** COLM 2026 adopted the ICLR 2026 LLM policy *minus* minor
  writing/code assistance. Disclose LLM-originated ideas, LLM-written content
  (including references), LLM-generated data or plots, and LLM-based evaluation.
  Fill this in truthfully; a judge-model evaluation pipeline is disclosable use.
- **Reciprocal reviewing:** there is a per-submission and a per-reviewer
  requirement; an author with 4+ submissions enters the reviewer pool
  automatically, and two submissions cannot lean on the same reciprocal reviewer
  unless nobody else qualifies. Decide the nominee per paper *before* deadline
  night — group-wide, this is a constraint-satisfaction problem, not a form field.

## Where LM papers leak identity

Beyond the obvious author block: Hugging Face model and dataset URLs under your org,
Weights & Biases dashboard links, API keys or org IDs left in config listings, model
names that only your lab uses internally, "our previously released model X"
phrasing, dataset cards naming maintainers, and PDF metadata from your LaTeX
toolchain. Grep before upload:

```bash
# Anonymity + hygiene sweep over the built PDF and the source tree
pdftotext main.pdf - | grep -niE 'huggingface\.co/[a-z0-9-]+|wandb\.ai|github\.com|we (previously|earlier) released|acknowledg' | head
pdfinfo main.pdf | grep -iE 'author|creator|producer'
grep -rniE 'api[_-]?key|org-[A-Za-z0-9]{6,}|hf_[A-Za-z0-9]{20,}' paper-src/ | head
```

Every hit is either a required anonymization fix or a leaked credential — both are
blocking.

## Risk triage before upload

| Finding | Weight at COLM 2026 | Fix path |
|---|---|---|
| Main text spills past page 9 | Strict-limit violation; assume fatal | Move eval configs and extra tables to appendices, never shrink the template |
| GitHub / HF / W&B link resolving to authors | Explicit anonymity breach | Anonymized mirror (e.g., an anonymous repo) or remove until camera-ready |
| Missing or false LLM-usage disclosure | Policy violation with integrity flavor | Disclose accurately; the policy exempts minor assistance, so honesty is cheap |
| Code of Ethics not acknowledged by a co-author | Form incompleteness | Chase co-author acknowledgments days early — you cannot click for them |
| Reciprocal reviewer double-booked across your group's papers | Requirement violation | Reassign nominees across the submission set |
| Placeholder abstract at the March 26 deadline | Misrouted bidding, weak reviewer match | Submit the genuine abstract; edits before the paper deadline are the escape hatch |
| Same work under review elsewhere | Dual-submission exposure | Withdraw one venue before March 31 |

## Deadline-week order of operations

1. **T-7 days:** freeze the claim set; anything unverified by now gets cut or
   hedged, not rushed.
2. **T-5:** submit the real abstract (March 26 in 2026). Confirm all OpenReview
   profiles and the reciprocal-reviewer assignment.
3. **T-3:** assemble the full PDF on the official COLM template; run the sweep
   commands above on the *built* PDF.
4. **T-2:** collect every co-author's Code of Ethics acknowledgment and LLM-usage
   disclosure input; these require other humans, so they cannot be T-0 tasks.
5. **T-0 (March 31):** upload, then re-download your own submission and read it
   cold — what you download is what reviewers receive.

## The abstract week is a strategy window

The five days between abstract (March 26) and paper (March 31) in 2026 were not
slack — they are the last point where cheap decisions are still available:

- **Title and abstract drive reviewer bidding.** Include the load-bearing nouns a
  matching system and a bidding human need: the phenomenon, the method family, the
  model classes studied. A cute title with no searchable terms buys you the wrong
  reviewers for four months.
- **Subject-area selections route the paper.** Choose the lane where your weakest
  section will be judged most fairly — an evaluation-critique paper mis-filed
  under "training methods" gets reviewers who ask for training contributions.
- **The withdraw option is real.** If the claims ledger still has red entries at
  the abstract deadline, submitting the abstract costs nothing, and withdrawing
  before March 31 costs only pride. Submitting a paper whose headline experiment
  finished an hour before upload costs a year at this venue.

```text
Abstract-week triage:
  all claims verified            -> proceed; polish
  1-2 claims at risk             -> submit abstract; cut/hedge at-risk claims now
  core claim unverified          -> submit abstract; decide by T-2, not T-0
  core claim failed              -> withdraw; COLM 2027 or the autumn venue
```

## Cycle-volatile items — recheck each edition

- All dates (the March 26 / March 31 pair is a 2026 fact, not a pattern; 2024's
  deadline was in late March too, but COLM has not promised stability).
- The 9-page cap, acknowledgment allowance, and template version.
- LLM-policy wording — 2026's is one edition old and explicitly adapted from
  another venue's; expect revision.
- Reciprocal-reviewing thresholds and mechanics.
- 待核实: any supplementary-material size caps and any abstract-edit grace rules;
  neither was verifiable on 2026-07-08.

## Output format

```text
[COLM submission status] ready / blocked / at risk
[Format] page count vs 9-page cap; template OK?
[Anonymity] clean / leaks: <channel list>
[Policy items] ethics-ack ▢  llm-disclosure ▢  reciprocal-reviewer ▢
[Fix queue] <ordered, with owners — co-author items first>
```
