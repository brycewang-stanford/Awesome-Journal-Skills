---
name: conext-camera-ready
description: Use when preparing the camera-ready of an accepted ACM CoNEXT paper for its assigned PACMNET issue — systematically de-anonymizing, completing PACMNET journal metadata and ACM rights/CCS/keywords, permanentizing artifact and DOI links, applying any shepherd-required changes, and passing ACM production checks.
---

# CoNEXT Camera-Ready

Deliver the camera-ready for the **PACMNET** issue your paper was scheduled into. This is the step
where the double-anonymous manuscript becomes a citable ACM journal article, so two things dominate:
**systematic de-anonymization** and **complete journal metadata**. If your paper went through a
one-shot revision or a shepherd, this is also where you confirm every required change actually
landed before the deadline (December cycle: camera-ready 30 Apr 2026; major-revision path 31 Jul
2026 — verify your cycle's date).

## De-anonymize systematically

The review copy was scrubbed of identity; the camera-ready must restore it *completely and only
where appropriate*:

```text
[Authors + affiliations]  add the real author block and affiliations
[Acknowledgments]         restore funding, grants, and collaborators
[Self-citation]           switch "prior work [12]" back to first person only where accurate
[System/testbed names]    restore real names of systems, testbeds, deployments
[Artifact links]          swap anonymized URLs for the permanent DOI-issuing archive
[Repository]              point to the real, public repository (not the anon service)
```

Do a dedicated pass: a leftover "Anonymous" or a dead anon-service link in the published article is a
visible production error.

## Complete PACMNET journal metadata

Because CoNEXT publishes in PACMNET, the camera-ready carries **journal** metadata, not just
conference proceedings fields:

- **ACM CCS concepts** and **author keywords** (required for ACM DL indexing).
- The **ACM rights/licensing** block (the e-rights form output) — CoNEXT/PACMNET is open access;
  confirm the exact license and copyright string from your rights form.
- **Author ORCIDs** and correct affiliations.
- The **PACMNET volume/issue** assignment (e.g., the cycle-named issue your paper landed in) and any
  article-number/DOI fields the production kit requests.

## Permanentize availability

- Move the artifact from the anonymizing service to a **DOI-issuing archive** (Zenodo/figshare/
  Software Heritage) and cite that DOI in the paper.
- If you earned or are pursuing **ACM reproducibility badges**, ensure the badge and the artifact DOI
  are correctly associated (coordinate with the reproducibility committee; see
  [`conext-artifact-evaluation`](../conext-artifact-evaluation/SKILL.md)).
- Replace any placeholder or personal-GitHub link; the published record should point to permanent
  locations.

## Apply shepherd / revision-required changes

- If a **shepherd** was assigned or the paper came through a one-shot revision, re-check the list of
  **minimum necessary changes** against the final PDF; the shepherd signs off before publication.
- Do not use camera-ready to quietly expand scope or add claims the reviewers did not see — restrict
  edits to the required changes, de-anonymization, and polish.

## Pass ACM production checks

- Compile with the **required `acmart` version/options** for PACMNET; do not alter margins or fonts.
- Run the **ACM PDF checks** (embedded fonts, no broken references, valid metadata) that the
  production/TAPS pipeline enforces.
- Confirm the paper fits the **final page allowance** (the camera-ready limit may differ from the
  review limit — verify).
- Check figures, especially topology diagrams and CDFs, render correctly in the final PDF.

## Camera-ready checklist

```text
[De-anon]      authors, acks, system/testbed names, artifact links all restored? yes/no
[No leftovers] no "Anonymous", no dead anon-service links? yes/no
[Metadata]     CCS + keywords + rights block + ORCIDs + PACMNET issue/DOI complete? yes/no
[Availability] artifact on a DOI archive; badge association correct? yes/no
[Shepherd]     required changes confirmed in the final PDF? yes/no/n-a
[Production]   acmart version, ACM PDF checks, page allowance, figures? pass/fail
```

## Output format

```text
[Camera-ready status] ready / blocked
[Cycle + issue] <December | June> cycle -> PACMNET <volume/issue>
[De-anonymization] complete / leftovers: <where>
[Metadata] CCS/keywords/rights/ORCID/DOI status
[Availability] permanent artifact DOI + badge association
[Production] acmart + ACM checks pass? outstanding items with the deadline
```
