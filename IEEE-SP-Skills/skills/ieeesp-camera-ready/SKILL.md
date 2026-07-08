---
name: ieeesp-camera-ready
description: Use when converting an IEEE S&P (Oakland) acceptance into a final paper, including working the shepherd against the draft meta-review's concern list, adding the ethics section, de-anonymizing and restoring disclosure specifics, IEEE compsoc and Xplore requirements, and coordinating artifact submission.
---

# IEEE S&P Camera-Ready

Use this after an Accept decision. S&P's camera-ready is not a formatting
pass: acceptance arrives with a **draft meta-review listing remaining
concerns and a shepherd who strikes each concern only when the revision
resolves it** (2027 CFP, checked 2026-07-08). The camera-ready is the last
reviewed artifact of the cycle.

## Working the shepherding loop

1. Convert the draft meta-review into a numbered concern ledger on day one.
2. For each concern, agree internally on: the change, its location, and the
   one-line evidence the shepherd can check.
3. Ask the shepherd early about any concern you believe is out of scope or
   wrong — negotiation happens at the start, not at the deadline.
4. Submit the revision with a concern → change → location map; make the
   strike-through decision mechanical for the shepherd.
5. Nothing in the shepherding loop authorizes *new* claims: the accepted
   contribution is the contribution.

| Shepherd asks for | Right-sized response |
|---|---|
| Tone down claim X | Rewrite the claim to the evaluated boundary; show old/new text |
| Add limitation discussion | A titled paragraph, referenced from the intro |
| Clarify threat model edge | Amend §2 with the explicit assumption |
| Missing related system | Cite + one-line technical delta, not a new section |
| Ethics wording | Coordinate with the ethics section below |

## The ethics section is added now — and does not count

Accepted papers add a dedicated, well-marked ethics section **without it
counting against page limits** (2026 CFP wording, checked 2026-07-08). Write
it as a record, not a disclaimer:

- What could cause harm, to whom, and what you did about it.
- Responsible disclosure: who was notified, when, what they responded,
  current fix status — with the real names and dates now that anonymity has
  lifted.
- IRB approval or waiver, by institution and protocol ID, where applicable.
- Data handling: what PII existed, minimization, retention, who had access.

## De-anonymization with security-specific restorations

Beyond names, affiliations, acknowledgments, and first-person citations,
restore what anonymity forced you to blur:

- Vendor names and CVE identifiers in the disclosure narrative.
- Artifact URLs (repository, DOI deposit) replacing anonymized placeholders.
- Funding and infrastructure acknowledgments (measurement platforms often
  contractually require attribution).

```bash
# Residue sweep after de-anonymization
pdftotext final.pdf - | grep -inE 'anonym|redacted|omitted for (review|anonymity)|Vendor [A-Z]\b'
pdfinfo final.pdf | grep -iE 'title|author'   # metadata now correct, not blank
grep -rn 'REPLACE-AFTER-ACCEPT' . || true
```

## IEEE mechanics

The proceedings are published by IEEE (Xplore); the compsoc template remains
mandatory. Verify on the current year's author page — all 待核实 at this
pack's check date for 2027: the exact camera-ready deadline, the final page
allowance and any purchasable extra pages, the IEEE copyright/eCF step,
PDF-compliance checking, and whether registration or in-person presentation
by an author is required for publication. Reported by aggregators (unverified
officially): recent S&P papers appear open access in the Computer Society
Digital Library — do not promise open access until confirmed.

## Sequence to the deadline

1. Concern ledger agreed with shepherd (week 1).
2. Content revisions + ethics section drafted (weeks 1–2).
3. De-anonymization and restoration sweep.
4. Artifact evaluation submission if opting in — its schedule runs off the
   acceptance date, in parallel (`ieeesp-artifact-evaluation`).
5. Final compsoc compile, IEEE PDF check, copyright form, upload.
6. Re-download and verify the archived PDF; Xplore keeps what you upload.

## Common failures at this stage

- Treating the meta-review as advisory — an unresolved concern is a
  shepherd-level blocker, not a style note.
- An ethics section written as legal boilerplate; reviewers approved a
  specific record and expect it stated.
- Disclosure narrative updated in the ethics section but not in the
  introduction, leaving contradictory timelines.
- Missing the artifact-evaluation registration window while polishing prose.

## Output format

```text
[Concern ledger] <n> total: resolved <n> · negotiating <n> · open <n>
[Ethics section] disclosure record ✓/✗ · IRB/waiver ✓/✗ · data handling ✓/✗
[De-anon sweep] names/CVEs/URLs restored ✓/✗ · residue found: <items>
[IEEE mechanics 待核实] deadline / page allowance / copyright / attendance
[Artifact track] opted in? deadline <date>; badge targets <list>
```
