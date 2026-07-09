---
name: pods-camera-ready
description: Use when preparing an accepted ACM PODS paper for its PACMMOD-track camera-ready, covering de-anonymization, the final acmsmall format and PACMMOD journal metadata (DOI, ORCID, CCS concepts), integrating shepherd-required revision items without overclaiming, posting and DOI-linking the arXiv full version, and confirming registration and presentation.
---

# PODS Camera Ready

Use this after acceptance. PODS research papers are published in the **PACMMOD PODS track**
(Proceedings of the ACM on Management of Data), so the camera-ready is a journal-style production step,
not just a formatting pass. Reopen the current PACMMOD/PODS author instructions, the decision/shepherd
email, and the registration page before advising.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, ORCIDs, acknowledgements,
  funding, and any real system name that lightweight double-anonymity forced you to hide — in the body
  *and* the appendix.
- **Apply the final format:** the `acmart` class in the PACMMOD/`acmsmall` production variant the
  instructions name (drop the `review,anonymous` options), within the stated page allowance.
- **Complete PACMMOD journal metadata:** title/abstract, author order, ORCIDs, ACM CCS concepts and
  keywords, and the DOI-bearing citation once assigned. Journal-style metadata errors are harder to fix
  after publication than conference ones.
- **Integrate the shepherd's required revision items** faithfully — every item from a minor/major
  revision made and reflected — without strengthening a theorem beyond what the proofs establish.
- **Post the full version on arXiv** and DOI-link it: the community norm is a complete full version;
  ensure its theorem statements match the PACMMOD version exactly.
- **Confirm registration and presentation** obligations; at least one author presents at the PODS
  symposium.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing your own work |
| A prototype/system name | Real name throughout body, appendix, figures | A leftover anonymized placeholder in a proof or caption |
| arXiv full-version link | Public arXiv URL + DOI cross-link | An anonymized/withheld link surviving in a footnote |

## PACMMOD production checks

```text
[Template]   acmart in the PACMMOD/acmsmall production variant; review+anonymous options removed
[Metadata]   title, abstract, authors+ORCID, CCS concepts, keywords entered and matching the PDF
[References] complete and consistent; DOIs where available (references are unlimited, not page-counted)
[Proofs]     the shepherd-required proof fixes integrated; appendix consistent with the body
[Rights]     ACM e-rights/copyright form completed; correct rights statement on the first page
[arXiv]      full version posted, de-anonymized, theorem statements matching, DOI cross-linked
```

## Worked example: integrating a shepherd-required fix

The shepherd required completing the complexity accounting in a theorem and labeling a lower bound as
conditional on OMv. Camera-ready move: expand the accounting in the body with the deferred steps in the
appendix, add the "conditional on OMv" qualifier at the theorem's point of statement, restore the real
system name used in the running example, and post the arXiv full version whose Theorem 4 reads
identically — without widening the claim the reviewers accepted.

## arXiv full-version handoff

The PACMMOD paper is the extended abstract of record; the arXiv full version is the community's
complete reference. Keep them consistent: the same theorem numbers and statements, the same
assumptions, and a DOI cross-link in both directions. This is the PODS analogue of releasing an
artifact — a readable, permanent full proof, not a badge.

## Hedged logistics

- Page allowances, metadata fields, rights-form mechanics, the exact `acmart` production variant, and
  camera-ready dates change each cycle; confirm against the decision email and current PACMMOD/PODS
  instructions rather than a prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / acks / system name / links restored in body + appendix? yes/no
[PACMMOD metadata] ORCID / CCS / keywords / rights form complete? yes/no
[Shepherd-item map] <required revision item -> final edit, no overclaim>
[arXiv full version] posted, de-anonymized, statements matching, DOI cross-linked? yes/no
[Remaining owner] <person -> task>
```
