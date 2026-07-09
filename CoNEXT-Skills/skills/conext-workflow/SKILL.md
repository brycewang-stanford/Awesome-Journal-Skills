---
name: conext-workflow
description: Use when planning an ACM CoNEXT campaign backward from a deadline, covering the choice between the December and June submission cycles, the mandatory registration step, the one-shot major-revision window, the reproducibility badge opt-in due at submission, PACMNET camera-ready, and presentation — all on CoNEXT's distinctive two-cycles-per-year calendar.
---

# CoNEXT Workflow

Plan the whole campaign backward from the cutoff. CoNEXT's defining feature is **two submission
cycles a year** — a **December** deadline and a **June** deadline — both feeding one annual program
and one rolling PACMNET volume. The first decision is therefore not "when do I write?" but "which
cycle am I targeting, and is my evidence ready for it?" Every date below is the CoNEXT 2026 snapshot
read on 2026-07-09 (see [`../../resources/official-source-map.md`](../../resources/official-source-map.md));
reopen the live Important Dates page before committing.

## Choose the cycle

```text
[December cycle]  register 5 Dec 2025 -> submit 12 Dec 2025 -> early-reject Feb 2026
                  -> notify 31 Mar 2026 -> camera-ready 30 Apr 2026 -> June 2026 PACMNET issue
   (major revision path) revision due 29 May 2026 -> resubmit 5 Jun 2026 -> camera-ready 31 Jul 2026
[June cycle]      submit 5 Jun 2026 -> (its own review round, notification, and later PACMNET issue)
```

- Target the **nearer honest deadline** your evidence is actually ready for. A half-finished testbed
  campaign rushed into December scores worse than a complete one in June.
- If you earn a one-shot major revision in the December cycle, the resubmission lands in the spring —
  so the two cycles are two entry points into the same program, not two separate conferences.
- Both cycles publish in **PACMNET**; the issue you land in depends on your cycle and revision path.

## Backward plan from a chosen cutoff (T = submission day)

```text
T minus 12-16 weeks  Lock the contribution and the evaluation platform (testbed/deployment/trace).
                     Run conext-topic-selection: CoNEXT vs SIGCOMM/NSDI/IMC, and December vs June.
T minus 8-12 weeks   Build evidence with conext-experiments + conext-reproducibility. Pin traces,
                     configs, firmware/OS versions NOW — they cannot be reconstructed later.
T minus 4-8 weeks    Draft against conext-writing-style and the worked example. Positioning with
                     conext-related-work. Decide the body/appendix/artifact split (conext-supplementary).
T minus 2 weeks      Freeze the body. Build the anonymized artifact. Decide badging.
T minus 1 week       REGISTER (title/abstract/authors/conflicts). OPT IN for the reproducibility
                     badge before the submission deadline if you want it.
T minus 1-2 days     conext-submission end to end: acmart budget, double-anonymous sweep, HotCRP
                     fields, conflicts.
T                    Submit; re-download and read the uploaded PDF cold.
```

## After submission

```text
[Early-reject window]   Some cycles notify clearly-below-bar papers partway through. No action but
                        to plan the next cycle or a sibling venue if it comes.
[Reviews / discussion]  Two rounds + TPC meeting. Prepare an initial rebuttal if the cycle offers one
                        (conext-author-response, Turn 1).
[Decision]              Accept / Reject / one-shot major revision.
[One-shot revision]     ~2 months to address the minimum-necessary changes; same reviewers re-read
                        once; a shepherd checks the changes (conext-author-response, Turn 2).
[Accept]                Camera-ready to acmart + PACMNET metadata (conext-camera-ready). If you opted
                        in, send the one-page artifact description within a week (conext-artifact-evaluation).
[Reject]                No appeal. Reroute via conext-topic-selection to a sibling venue or the other
                        CoNEXT cycle, revised.
```

## Roles and hand-offs

- **Registration owner** — one author confirms title/abstract/authors/conflicts before the earlier
  registration cutoff; a missed registration means no submission slot.
- **Artifact owner** — pins traces/configs and stages the anonymized artifact; owns the badge opt-in
  before submission and the one-page description after acceptance.
- **Anonymity owner** — runs the double-anonymous sweep on the final PDF, figures (topologies!), and
  archive, and on the major-revision response letter.
- **Shepherd liaison** — after a revision or conditional accept, the corresponding author tracks each
  required change to a tracked edit for the shepherd.

## Calendar hygiene

- Confirm **both** cycles' exact dates and time zones each year; CoNEXT re-posts them per edition.
- Do not assume the December and June cycles share every rule (page budget, revision window); verify
  the one you are in.
- Watch the co-located **Student Workshop** and any workshops if a shorter or student-facing venue
  fits ongoing work better (see [`conext-topic-selection`](../conext-topic-selection/SKILL.md)).

## Output format

```text
[Target] CoNEXT <year>, <December | June> cycle, submission <date + time zone>
[Backward plan] <milestones with dates: platform freeze, evidence, draft, register, opt-in, submit>
[Risk] <the milestone most likely to slip, and the fallback cycle/venue>
[Post-submission] <decision-contingent branches: revision window, camera-ready, badge>
```
