---
name: imc-camera-ready
description: Use when preparing an accepted ACM IMC paper for the proceedings, covering systematic de-anonymization, finalizing the Ethics and artifact-availability statements, permanentizing dataset and code links to DOI-issuing archives, satisfying the availability shepherd, Community Contribution Award eligibility, and ACM production checks.
---

# IMC Camera-Ready

Use this after an IMC Accept (or a successful One-Shot-Revision). The camera-ready is not just a
de-anonymized PDF: it is where the **availability declaration becomes a real public release**, the
**Ethics statement is finalized**, and the paper enters the ACM Digital Library proceedings. The
shepherd is watching for the artifact you promised, and the **Community Contribution Award** is
judged on what is public **by the camera-ready deadline**.

## De-anonymization sweep (the reverse of submission)

Now the paper carries identity — completely and correctly:

- Restore author names, affiliations, and ORCIDs in the `acmart` metadata.
- Restore acknowledgements: funders, grant numbers, and the operators/providers who granted
  vantage-point or data access.
- Convert third-person references to your own prior work back to first person where appropriate.
- Replace every anonymized dataset/tool link with the **permanent public** URL.
- Restore vantage-point and testbed attributions that were anonymized for review.

## Permanentize the dataset and code

The shepherd checks availability; a link that rots is a failure:

```text
[Archive]   deposit the dataset/tool in a DOI-issuing archive (Zenodo/figshare/Software Heritage)
            or a durable community archive; a personal homepage is not durable
[Version]   tag the exact released version cited by the paper; note how updates will be versioned
[Schema]    ship the documented schema/dictionary and a README with a runnable example
[License]   attach an explicit license (e.g., CC-BY for data, OSI for code)
[Links]     ensure every dataset/figure/tool reference in the PDF resolves to the permanent URL
```

## Finalize the Ethics statement

The Ethics section moves from "what we did to be safe" (review framing) to a complete, citable
record:

- State IRB approval/exemption with the determining body (now de-anonymized).
- Confirm the responsible-disclosure outcome and timeline for any vulnerability/exposure finding.
- Confirm the privacy/anonymization actually applied to the released dataset matches what the
  section claims.

## Satisfy the shepherd

If your paper was assigned an availability shepherd, deliver before the deadline: the public
artifact matching your declaration, the documented schema, and a working link. If your declaration
was **partial** or **none**, ensure the stated justification is intact and, where possible, a
privacy-safe derivative is released.

## Community Contribution Award readiness (if applicable)

To keep eligibility, the dataset/tool/platform must be **public and usable by the camera-ready
deadline**: documented, licensed, DOI-archived, and reusable by a stranger. "Coming soon" forfeits
eligibility.

## ACM production checks

```text
[Template]   final acmart camera-ready format, correct rights/permissions block, DOI, page numbers
[Metadata]   title/authors/affiliations/ORCIDs/keywords/CCS concepts correct
[References]  final bibliography clean; DOIs where available; the BBL matches
[Figures]    vantage-point maps/plots legible in print and grayscale; captions self-contained
[Reproduce]  the PDF's numbers match the released data + scripts (the shepherd may spot-check)
```

## Common camera-ready failures

| Failure | Consequence | Fix |
|---|---|---|
| Anonymized dataset link left in the PDF | Broken/incorrect availability | Replace with the permanent DOI URL |
| Promised artifact never published | Shepherding failure; award ineligible | Publish and archive before the deadline |
| Ethics section still in review framing | Incomplete record | Finalize IRB and disclosure statements |
| Missing rights/permissions block | Production reject | Insert the ACM-provided block |
| Figures illegible in print | Readability loss | Redraw for print/grayscale |

## Calibration

- Camera-ready deadlines are cycle-specific (cycle 1 ~mid-April 2026; cycle 2 ~1 Sep 2026);
  confirm yours and calendar the artifact release before it.
- The exact rights form, template revision, and shepherding process vary by edition — confirm on
  the current camera-ready instructions.

## Output format

```text
[Camera-ready status] ready / blocked
[De-anonymization] names/affiliations/acks/links restored? yes/no
[Artifact] permanent DOI archive live? schema + license + README? yes/no
[Ethics] IRB + disclosure statements finalized? privacy claims match release? yes/no
[Shepherd] availability delivered as declared? yes/no
[Production] acmart + rights block + metadata + BBL correct? yes/no
[Fix queue] <ordered, before the camera-ready deadline>
```
