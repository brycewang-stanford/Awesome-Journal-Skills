---
name: fast-camera-ready
description: Use when preparing an accepted USENIX FAST paper for its open-access camera-ready, covering de-anonymization, the USENIX two-column template and the larger camera-ready page allowance, integrating shepherd- or revision-required changes without scope creep, permanentizing trace and code availability, adding the artifact appendix and USENIX badges, and meeting the final-files deadline.
---

# FAST Camera Ready

Use this after acceptance. FAST papers are published **open access by USENIX**, free to the public,
so the camera-ready is a production step with no APC and no paywall — but with firm final-files dates
(FAST '27 Spring: 28 Jul 2026; Fall: 26 Jan 2027) and USENIX formatting requirements. Reopen the
current instructions-for-authors, the decision/shepherd email, and the Call for Artifacts before
advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding, and
  the real system/tool and repository names that double-blind forced you to hide.
- **Apply the final format:** the USENIX two-column template within the current camera-ready
  allowance (reported larger than submission — e.g. 13 pages long / 7 short, references excluded).
  Use the extra space for shepherd-required additions, not scope creep.
- **Integrate the required changes** from the reviews, the shepherd, or the one-shot revision
  faithfully — without strengthening claims beyond what was evaluated.
- **Permanentize availability:** replace every anonymized artifact/trace link with a public,
  licensed, DOI-issuing archive, and update the availability statement to point at it.
- **Add the artifact appendix and badges** if you went through artifact evaluation: badges appear on
  the first page and the appendix details the artifact (`fast-artifact-evaluation`).
- **Confirm registration and presentation** obligations; at least one author presents.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations | Full, correctly ordered | Wrong order breaks the citation |
| System / tool name | Real name throughout text, figures, artifact | A leftover placeholder in a caption or a config |
| Acknowledgements, funding, hardware donors | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Device dumps / hostnames redacted for review | Real values only where safe; keep serials out | Re-introducing a serial number needlessly |
| Artifact / trace link | Public archive DOI | The old anonymized URL surviving in a footnote |

## USENIX production checks

```text
[Template]   USENIX two-column template, current revision; no manual margin/font edits; 10pt/12pt
[Metadata]   title, authors, affiliations match HotCRP and the PDF; abstract consistent
[Testbed]    the device/firmware table is complete and final; device-state caveats intact
[References] complete, consistent; DOIs where available; references excluded from the page count
[Figures]    vector where possible; latency distributions and plots readable in print; captions self-contained
[Rights]     USENIX publication agreement completed; correct notice on the first page
[Links]      every availability, trace, and artifact link resolves from a logged-out browser
[Appendix]   artifact appendix + earned badges added per the current instructions
```

## Worked example: integrating a one-shot-revision result

The revision required adding a steady-state write-amplification comparison and a crash-consistency
test. Camera-ready move: keep the added §5.3 table and §6 crash-test exactly as evaluated, restore
the real system name in those sections and the artifact, point the availability statement at the
now-public DOI archive, and — using the larger camera-ready budget — expand the device-state caveat
into a clear paragraph rather than inflating the claim the AEC and reviewers accepted.

## Hedged logistics

- Page allowances, metadata fields, the rights agreement, and exact final-files dates change each
  cycle; confirm against the decision email and current USENIX author instructions rather than a
  prior year. The two deadlines have different final-files dates — use the one for *your* cycle.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / system name / acks / device dumps / links restored? yes/no
[Format] USENIX template, within camera-ready page allowance? yes/no
[Required-change map] <shepherd/revision item -> final edit, no scope creep>
[Availability] anonymized links replaced by DOI archive? artifact appendix + badges added? yes/no
[Remaining owner] <person -> task, against the final-files date>
```
