---
name: osdi-supplementary
description: Use when deciding where OSDI content lives given the no-appendix submission rule — triaging material between the 12-page reviewed body, the 14-page-plus-appendices final paper, and the public artifact, since OSDI (unlike appendix-friendly venues) reviews nothing outside the body.
---

# OSDI Supplementary Material

OSDI inverts the supplement habit most authors bring from ML and ACM venues. Rules
below are the OSDI '26 cycle (verified 2026-07-08): submissions get **12 pages plus
unlimited references and nothing else** — the CFP permits extra pages for references
"but not for supplementary material in appendices." There is no supplement upload, no
appendix, no ZIP. Accepted papers later expand to **14 pages plus references and
appendices**, plus an optional **two-page Artifact Appendix** for papers passing
artifact evaluation.

## The three destinations

Every piece of material has exactly one correct home:

| Destination | What belongs there | When it exists |
|---|---|---|
| 12-page reviewed body | Everything a reviewer needs to judge correctness and significance | Submission (December) |
| Final-paper appendix (post-acceptance) | Depth for readers: full protocol details, extended results, proofs written out, the Artifact Appendix | Final papers (June) |
| Public artifact | Code, traces, configurations, raw data, runbooks | Archived by the May artifact deadline |

The triage question for any candidate paragraph, proof, table, or figure: **"Does a
skeptical reviewer need this to accept the paper?"** Yes → it earns body space, and
something weaker must leave to make room. No → it waits for the final-paper appendix
or the artifact, and the body carries a one-line summary of what exists.

## Living without an appendix at submission

Techniques for material that would be an appendix elsewhere:

- **Proofs and invariants** — state the invariant and the proof's one load-bearing
  step in the body ("safety follows because a lease transfer requires quorum
  acknowledgment of the epoch bump"); the full proof is final-paper appendix
  material. If the paper is unacceptable without the full formal argument, OSDI's
  format is telling you something about venue fit (`osdi-topic-selection`).
- **Extended result grids** — the body shows the RQ-answering figure; the sweep
  across every configuration goes to the artifact as data plus plotting scripts,
  referenced in one sentence without a link that breaks anonymity.
- **Protocol/config detail** — compress into a table; systems reviewers extract more
  from a dense parameter table than from two pages of prose.
- **Never** point to an external URL as a de facto appendix. An anonymous link
  carrying material the paper depends on violates the spirit of the rule reviewers
  enforce, and any non-anonymous link is a double-blind breach (`osdi-submission`).

## Planning the June expansion in December

Write the submission with a marked expansion plan so the accepted version is an
unfolding, not a rewrite:

```text
% submission-time annotations, kept in comments in the source
% [FINAL-14pp] restore lease-protocol failure cases cut from §4.2
% [FINAL-APPENDIX-A] full safety proof (draft in proofs/safety.tex)
% [FINAL-APPENDIX-B] full workload sweep grid (artifact: plots/sweep/)
% [ARTIFACT-APPENDIX] runbook skeleton -> becomes the 2-page AE appendix
% rule: nothing in FINAL-* may be load-bearing for acceptance
```

The rule in the last comment is the audit: if any `FINAL-*` item is something a
reviewer would have needed, it must be promoted into the body *now* — after
acceptance is too late to have convinced anyone, and OSDI '26 offered no response
period in which to supply missing material on request.

## Triage decision flow

Run each candidate item through this flow when the draft first crosses 12 pages —
not on deadline night:

```text
item: proof / table / protocol detail / extra experiment / config dump
  |
  needed by a skeptical reviewer to ACCEPT? --yes--> body (cut something weaker;
  |                                                  osdi-writing-style compression
  no                                                 pass runs first)
  |
  needed by a READER or REPRODUCER later? --yes--> is it prose/math?
  |                                                  yes -> final-paper appendix
  no                                                 no (code/data/runs)
  |                                                       -> artifact
  cut entirely (deadline-week sunk cost is not a reason to keep it)
```

Two calibration notes: reviewers differ, so when genuinely unsure whether an item is
acceptance-critical, it goes in the body — the no-response process gives no chance
to supply it on request; and the body must summarize every deferred item in one
sentence ("the full sweep, 240 configurations, accompanies the artifact"), because
an unmentioned deferral is indistinguishable from a gap.

## The Artifact Appendix (the one supplement OSDI formalizes)

For papers that pass artifact evaluation, the final paper may add up to two pages
documenting the artifact in a standard format: what the artifact contains, hardware
and software requirements, how to reproduce which claims. Treat it as the public,
citable interface to the artifact — written from the runbook the AE committee already
exercised (`osdi-artifact-evaluation`), not composed fresh in June.

## Triage failure modes

- Submitting a paper that silently assumes appendix space exists — discovered at
  page 13, two days before the deadline.
- Cutting load-bearing evidence to fit, instead of cutting redundancy
  (`osdi-writing-style`'s compression pass comes first).
- An external "anonymous supplement" link standing in for the forbidden appendix.
- Deferring so much to the final version that reviewers correctly judge the
  submission incomplete — conditional acceptance mandates fixes, but only for papers
  strong enough to conditionally accept.

## Output format

```text
[No-appendix compliance] submission = body + refs only? violations: <list>
[Triage table] each deferred item -> destination (final-appendix / artifact) + body summary line present?
[Load-bearing audit] any FINAL-* item a reviewer actually needs? <list or none>
[External links] none that carry evidence / none that break anonymity? yes/no
[June plan] expansion annotations in source? artifact-appendix runbook started?
```
