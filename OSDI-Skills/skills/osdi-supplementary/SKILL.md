---
name: osdi-supplementary
description: Use when deciding where OSDI content lives given the no-appendix-in-the-PDF rule and OSDI '27's optional separate supplementary files — triaging material between the 12-page reviewed body, a supplement PC members need not read, the 14-page final paper, and the public artifact, since OSDI judges acceptance on the body alone.
---

# OSDI Supplementary Material

OSDI inverts the supplement habit most authors bring from ML and ACM venues. Rules
below are the OSDI '27 cycle (re-verified 2026-11-24): the submitted PDF gets **12 pages
plus unlimited references and no appendices** — the Requirements for Authors permit extra
pages for references "but not for supplementary material in appendices." New in '27, the
CFP lets authors **upload supplementary material in files separate from the submission**
(formal proofs sketched in the paper, code snippets detailing an algorithm, methodological
detail important for reproducibility), but **PC members are not required to read it**, so
the paper must stand alone. (OSDI '26 allowed no supplement at all.) Accepted papers get
**14 pages plus references**; whether the '27 final paper again allows appendices and the
two-page Artifact Appendix of the '26 rules is 待核实.

## The three destinations

Every piece of material has exactly one correct home:

| Destination | What belongs there | When it exists |
|---|---|---|
| 12-page reviewed body | Everything a reviewer needs to judge correctness and significance | Submission (December) |
| Separate supplementary file (optional, unread by default) | Full proofs only sketched in the body, algorithm code snippets, reproducibility-grade method detail | Submission (December), anonymized |
| Final-paper material (post-acceptance) | Depth for readers: restored detail, extended results, any appendix/Artifact Appendix the '27 final rules allow (待核实) | Final papers (June 3, 2027) |
| Public artifact | Code, traces, configurations, raw data, runbooks | Archived by the May artifact deadline |

The triage question for any candidate paragraph, proof, table, or figure: **"Does a
skeptical reviewer need this to accept the paper?"** Yes → it earns body space, and
something weaker must leave to make room. No → it can go in the supplementary file, wait
for the final paper, or live in the artifact, and the body carries a one-line summary of
what exists. A supplement is corroboration for a curious reviewer, never an argument the
decision depends on.

## Living without an appendix in the PDF

Techniques for material that would be an appendix elsewhere:

- **Proofs and invariants** — state the invariant and the proof's one load-bearing
  step in the body ("safety follows because a lease transfer requires quorum
  acknowledgment of the epoch bump"); the full proof can go in the separate
  supplementary file (the CFP names "formal proofs that are only sketched in the paper"
  as an example) and later into the final paper. If the paper is unacceptable without the full formal argument, OSDI's
  format is telling you something about venue fit (`osdi-topic-selection`).
- **Extended result grids** — the body shows the RQ-answering figure; the sweep
  across every configuration goes to the artifact as data plus plotting scripts,
  referenced in one sentence without a link that breaks anonymity.
- **Protocol/config detail** — compress into a table; systems reviewers extract more
  from a dense parameter table than from two pages of prose.
- **Never** point to an external URL as a de facto appendix. Use the official
  supplementary upload instead; an anonymous link carrying material the paper depends
  on violates the spirit of the rule reviewers enforce, and any non-anonymous link is a
  double-blind breach (`osdi-submission`). Anonymize the supplement like the paper.

## Planning the June expansion in December

Write the submission with a marked expansion plan so the accepted version is an
unfolding, not a rewrite:

```text
% submission-time annotations, kept in comments in the source
% [FINAL-14pp] restore lease-protocol failure cases cut from §4.2
% [SUPPLEMENT] full safety proof (proofs/safety.tex) -> separate upload now
% [FINAL] full workload sweep grid (artifact: plots/sweep/)
% [ARTIFACT-APPENDIX] runbook skeleton -> AE appendix if the '27 rules keep one
% rule: nothing in SUPPLEMENT or FINAL-* may be load-bearing for acceptance
```

The rule in the last comment is the audit: if any `SUPPLEMENT` or `FINAL-*` item is
something a reviewer would have needed, it must be promoted into the body *now* — after
acceptance is too late to have convinced anyone, and OSDI (no response period in '26 or
'27) offers no moment to supply missing material on request.

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
  |                                                  yes -> supplementary file now
  no                                                       + final paper later
  |                                                  no (code/data/runs) -> artifact
  cut entirely (deadline-week sunk cost is not a reason to keep it)
```

Two calibration notes: reviewers differ, so when genuinely unsure whether an item is
acceptance-critical, it goes in the body — the no-response process gives no chance
to supply it on request; and the body must summarize every deferred item in one
sentence ("the full sweep, 240 configurations, accompanies the artifact"), because
an unmentioned deferral is indistinguishable from a gap.

## The Artifact Appendix

Under the OSDI '26 rules (the '27 final-paper rules are 待核实), papers that passed
artifact evaluation could add up to two pages
documenting the artifact in a standard format: what the artifact contains, hardware
and software requirements, how to reproduce which claims. Treat it as the public,
citable interface to the artifact — written from the runbook the AE committee already
exercised (`osdi-artifact-evaluation`), not composed fresh in June.

## Triage failure modes

- Submitting a paper that silently assumes appendix space exists — discovered at
  page 13, two days before the deadline.
- Cutting load-bearing evidence to fit, instead of cutting redundancy
  (`osdi-writing-style`'s compression pass comes first).
- An external "anonymous supplement" link standing in for the official supplementary
  upload — or any appendix pages inside the submitted PDF.
- A body that silently relies on the supplement ("see supplement for the proof that
  makes §4 correct") — reviewers need not open it.
- Deferring so much to the final version that reviewers correctly judge the
  submission incomplete — conditional acceptance mandates fixes, but only for papers
  strong enough to conditionally accept.

## Output format

```text
[No-appendix compliance] PDF = body + refs only? violations: <list>
[Supplement] separate file? anonymized? nothing load-bearing in it?
[Triage table] each deferred item -> destination (supplement / final paper / artifact) + body summary line present?
[Load-bearing audit] any SUPPLEMENT/FINAL-* item a reviewer actually needs? <list or none>
[External links] none that carry evidence / none that break anonymity? yes/no
[June plan] expansion annotations in source? artifact-appendix runbook started?
```
