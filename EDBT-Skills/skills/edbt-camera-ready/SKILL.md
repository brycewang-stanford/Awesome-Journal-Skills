---
name: edbt-camera-ready
description: Use when preparing an accepted EDBT paper for its OpenProceedings camera-ready, covering the host/OpenProceedings LaTeX template, the CC-BY-NC-ND open-access license and copyright form, ISBN/volume metadata, integrating reviewer-required changes without scope creep, permanentizing artifact links, and the presentation obligation.
---

# EDBT Camera Ready

Use this after acceptance. EDBT papers are published **open access on OpenProceedings.org** under a
**CC-BY-NC-ND** license with copyright retained by the authors — this is an open-access production
step, not an ACM/IEEE DL upload. Reopen the current host-site camera-ready instructions, the
OpenProceedings author guidelines, the decision email, and the registration page before advising.

## Camera-ready audit

- **Use the host/OpenProceedings template,** current revision, within the per-shape page budget plus
  any camera-ready allowance the acceptance letter states. Do not switch to `acmart` or `IEEEtran`.
- **Complete the OpenProceedings license and copyright step:** the **CC-BY-NC-ND 4.0** publishing
  license (or the exact license the current volume specifies) with author-retained copyright. This
  is different from an ACM e-rights or IEEE copyright transfer — do not fill in the wrong form.
- **Enter the volume metadata:** title/abstract, author order and affiliations, ORCIDs where asked,
  and the fields OpenProceedings needs for the **ISBN-bearing** volume and the DBLP/Scholar/SCOPUS
  records. Metadata errors in an open-access record are awkward to fix after the volume is frozen.
- **De-anonymize (if the cycle was double-blind):** restore the author block, affiliations,
  acknowledgements, funding, and the real system and repository names.
- **Integrate reviewer-required and revise changes** faithfully — without strengthening claims beyond
  what was evaluated.
- **Permanentize the artifact:** replace any anonymized or temporary link with a public,
  DOI-issuing archive under a compatible license, and update the availability statement to point at
  it.
- **Confirm registration and presentation:** at least one author presents at the edition your cycle
  feeds (recall the last-cycle roll to the next year).

## Open-access metadata and rights checks

```text
[Template]   host/OpenProceedings template, current revision; no manual margin/font edits
[License]    CC-BY-NC-ND publishing license completed; copyright retained by authors (NOT an ACM/IEEE transfer)
[Metadata]   title, abstract, authors + affiliations/ORCID, keywords all entered and matching PDF
[Volume]     ISBN/volume fields as the OpenProceedings volume requires
[References] complete and consistent; DOIs where available (references are unlimited — keep them full)
[Figures]    vector where possible; readable in print and on screen; captions self-contained
[Links]      every artifact / availability link resolves from a logged-out browser
```

## De-anonymization sweep (if the cycle was double-blind)

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the citation |
| System / prototype name | Real name throughout text, figures, artifact | A leftover placeholder in a caption |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Repository / artifact link | Public DOI archive | The old anonymized URL surviving in a footnote |

If the cycle was single-blind, there is nothing to de-anonymize — but still confirm the artifact link
is the permanent, public one.

## Worked example: integrating a revise change

The reviewers required adding a tuned baseline at larger scale and moving an overhead result from the
appendix into the body. Camera-ready move: place the overhead result in the scope/discussion with its
measurement, add the promised scaling table with variance, restore the real system name in the
figures, and point the availability statement at the now-public DOI-archived artifact — without
expanding the claim the reviewers accepted.

## Hedged logistics

- Page allowances, the exact license text and metadata fields, and camera-ready dates change each
  cycle and each host edition; confirm against the decision email and the current OpenProceedings /
  host instructions rather than a prior year.
- The publication month depends on which cycle accepted the paper (the rolling model clusters
  publication across the year); check when your volume goes live.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[Template + budget] host/OpenProceedings template, per-shape budget met? yes/no
[License] CC-BY-NC-ND completed, copyright retained (not ACM/IEEE)? yes/no
[Metadata] authors/affiliations/ORCID/keywords + ISBN volume fields complete? yes/no
[De-anonymization] (if double-blind) author block / system name / links restored? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Open science] artifact link is a permanent DOI archive? yes/no
[Remaining owner] <person -> task>
```
