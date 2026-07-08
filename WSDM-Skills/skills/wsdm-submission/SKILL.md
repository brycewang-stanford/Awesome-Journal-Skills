---
name: wsdm-submission
description: Use when auditing a WSDM submission before the August deadlines - EasyChair setup, the abstract-then-paper week, the appendix-inclusive page budget, the required ethical-considerations section, anonymization that survives Associate-Chair metadata visibility, and desk-reject exposure at a no-rebuttal venue.
---

# WSDM Submission

Audit a paper headed for WSDM's single annual deadline. The stakes are unusual:
WSDM historically runs **no rebuttal**, so whatever enters EasyChair in August is
the entire case reviewers will ever see. A fixable-in-rebuttal weakness at other
venues is a terminal weakness here. Every number below is a 2026-edition anchor
(19th WSDM, Boise); reopen the current edition's CFP before quoting any of it.

## The two-deadline week

WSDM pairs an abstract registration with a full-paper deadline one week later
(2026: abstracts August 7, papers August 14, 2025, both 23:59 AoE, EasyChair).
Use the gap deliberately:

- The abstract you register steers bidding at a venue with a compact, expert PC.
  A vague abstract lands the paper with the wrong specialists; at a no-rebuttal
  venue you cannot later explain what the paper "really" meant.
- Placeholder titles or abstracts ("TBD") were an explicit desk-reject trigger in
  the 2026 short-paper call - assume the same hygiene standard everywhere.
- Author lists and orderings should be final at abstract time. Confirm every
  coauthor's EasyChair account and conflict declarations that week, not on
  deadline night.

## Page-budget arithmetic: appendices live inside the cap

The 2026 long-paper rule: **9 pages including diagrams, tables, and appendices**,
with unrestricted space only for references and the ethical-considerations
section. The 2025 rule was 8 pages plus at most 2 shared by references and
ethics. Two consequences that surprise people arriving from KDD or NeurIPS:

1. There is no unlimited appendix to absorb overflow. A proof, a prompt listing,
   or a hyperparameter table "moved to the appendix" still spends the same budget.
2. The only uncounted prose you control is the ethics section - and chairs read
   it as ethics, not as a smuggling route for extra experiments. Abusing it is a
   credibility hit in front of the same SPC who writes your meta-review.

```latex
% WSDM 2025-cycle documented setting - verify options against the current CFP
\documentclass[sigconf,anonymous,review]{acmart}
% sigconf   : ACM two-column conference layout (WSDM is an ACM conference)
% anonymous : suppresses the author block for double-blind review
% review    : line numbers for reviewer reference
% Never patch \baselineskip, margins, or fonts: a tampered acmart is visible
% to any chair who compiles the reference template next to your PDF.
```

Budget the 9 pages backwards: fix the space for the evaluation section first
(WSDM reviewers weigh it heaviest), then the method, then shrink the
introduction to what remains. Cutting evaluation to preserve a long method
narrative is the classic losing trade at this venue.

## Anonymization under hybrid blinding

WSDM's CFP describes "a combination of single-blind reviewing and double-blind
reviewing": the PDF must be fully anonymized for PC and senior PC members, while
Associate Chairs can see submission metadata (including authorship) to check
conflicts. Practical readings:

- Do not treat AC metadata visibility as permission to be sloppy - the people
  scoring the paper still must not be able to guess the authors.
- Industry papers leak identity through infrastructure nouns: an internal system
  name, a proprietary metric, a "our platform serves X million queries" figure
  that uniquely identifies one company. Rewrite to role descriptions ("a large
  commercial search engine") and round figures that fingerprint you.
- Self-citations go in third person; a cited anonymous repository must have a
  history-free remote, no institutional paths, and no author handles in configs.
- WSDM's anonymization seriousness is not folklore: the venue hosted the 2017
  controlled experiment showing single-blind reviewers favor famous affiliations,
  and its policy is written in that shadow.

## Desk-level exposure table

| Failure | Why it is severe at WSDM | Recoverable? |
|---|---|---|
| Over the 9-page inclusive cap | Explicit CFP bound; appendices count | No, after AoE |
| Missing ethical-considerations section | Required element of the submission | No |
| Identity leak in PDF or linked repo | Hybrid-blind policy with an experimental rationale | No |
| Wrong or "TBD" registered abstract | Bad bidding + placeholder desk-reject rule | Only in the abstract-paper gap |
| Claim answerable only "in rebuttal" | There is no rebuttal to answer it in | Only by rewriting before the deadline |
| Ethics section used as overflow appendix | Read by SPC as bad faith | Only before the deadline |

## Vignette: the platform paper that fingerprinted itself

A search-quality team anonymizes diligently - author block gone, citations in
third person, repository scrubbed - and still gets flagged. The leak chain:
the paper reports "our engine's 2.3 billion daily queries in 41 languages,"
names an internal experiment platform in a figure caption, and evaluates on a
locale mix only one company serves. No single item names the employer; the
conjunction does. The repair pass that would have caught it:

- Read the paper asking "how many organizations could have written this
  sentence?" - any sentence with answer "one" gets generalized or rounded.
- Rename internal systems to functional labels ("the interleaving platform").
- Report locale/scale details in buckets wide enough to cover several
  plausible platforms, with exact values deferred to the camera-ready.

This is also why the audit below schedules the anonymity sweep *after* the
content freeze: anonymity is a property of the final text, and every late
paragraph reopens it.

## Final-week order of operations

1. Freeze scope: anything not already in the evaluation cannot be promised later.
   Delete forward-looking claims ("we will additionally verify...").
2. Recompile from a clean `acmart` checkout; check the page count with references
   and ethics excluded from the 9, everything else included.
3. Run the self-containment pass: for each likely reviewer objection, verify the
   answer is physically in the PDF (see `wsdm-author-response` for the objection
   inventory method).
4. Sweep metadata: PDF author fields, figure-embedded usernames, dataset paths,
   acknowledgements, grant numbers, repository history.
5. Submit the PDF with hours of AoE margin. EasyChair accepts resubmissions until
   the deadline - upload early, replace often.

## Output format

```text
[WSDM submission audit] Ready / Needs fixes / Blocked
[Budget] 9-page-inclusive check: pass / over by N (appendices counted?)
[Ethics section] present and substantive: yes / no
[Anonymity] PDF / repo / metadata / infrastructure-noun leaks found: <list>
[Self-containment] objections lacking in-PDF answers: <list>
[Abstract-week actions] <items only fixable before the paper deadline>
```
