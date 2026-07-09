---
name: infocom-camera-ready
description: Use when preparing an accepted IEEE INFOCOM paper for its IEEE Xplore camera-ready, covering de-anonymization, the IEEEtran final format and page budget, the IEEE electronic Copyright Form (eCF), PDF eXpress validation, the author-registration requirement, integrating reviewer-required changes without scope creep, and permanentizing any released artifact links.
---

# INFOCOM Camera Ready

Use this after acceptance. INFOCOM papers publish in the **IEEE INFOCOM Proceedings and IEEE
Xplore**, so the camera-ready is an **IEEE production step** with hard mechanical gates: the IEEE
**electronic Copyright Form (eCF)** and **PDF eXpress** validation, plus an **author-registration**
requirement. Reopen the current Final Paper Submission Guidelines, the decision email, and the
registration page before advising (INFOCOM 2026 final paper: 9 Jan 2026, US ET).

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, ORCIDs, acknowledgements,
  funding/grant numbers, and the real tool/testbed/repository names that double-blind forced you to
  hide.
- **Apply the final IEEEtran format** within the page budget (10 pages max, ≤9 of text incl.
  appendices) and any camera-ready page allowance the acceptance letter states — INFOCOM sometimes
  permits a purchased extra page; confirm per cycle.
- **Complete the IEEE eCF:** submit the electronic copyright transfer; EDAS auto-directs you to the
  eCF site. The correct IEEE copyright notice must appear on the first page of the final PDF.
- **Pass PDF eXpress:** run the final PDF through IEEE PDF eXpress to produce an Xplore-compliant
  file, then upload it to EDAS. A PDF that fails PDF eXpress is not published.
- **Meet the author-registration rule:** at least one author must register for the main conference
  as an author; one registration covers up to three main-conference papers (verify the current
  cycle's exact ratio).
- **Integrate reviewer-required changes** from the reviews faithfully — without strengthening claims
  beyond what was evaluated.
- **Permanentize any release:** if you released an artifact, replace any anonymized link with a
  public, licensed, DOI-issuing archive and update the paper to point at it.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong order breaks the Xplore citation |
| Tool / testbed / system name | Real name throughout text, figures, release | A leftover placeholder in a caption |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting into double-citation |
| Anonymized artifact link | Public archive DOI | The old anonymized URL surviving in a footnote |

## IEEE Xplore production checks

```text
[Template]   IEEEtran, correct preamble; no manual margin/font edits; within the page budget
[eCF]        IEEE electronic copyright form completed via EDAS; correct notice on page 1
[PDF eXpress] final PDF validated through IEEE PDF eXpress and uploaded to EDAS
[Registration] at least one author registered; covers this paper (and up to two more)
[Metadata]   title, authors+ORCID, abstract, and indexing terms match the final PDF in EDAS
[References] complete and consistent; DOIs where available; within the reference allowance
[Figures]    vector where possible; readable in print; captions self-contained
[Links]      any artifact/data link resolves from a logged-out browser
```

## Worked example: integrating a required change

The reviewers required tuning a baseline and stating an assumption's limit. Camera-ready move:
report the re-tuned baseline's numbers in the existing results table, add one sentence in the system
model justifying the assumption and one in the limits paragraph bounding it, restore the real
simulator/tool name throughout, and point any released package at its now-public DOI archive —
without expanding the claim the TPC accepted.

## Hedged logistics

- The camera-ready date, any purchased-extra-page allowance, the registration-to-papers ratio, and
  eCF/PDF eXpress mechanics change each cycle; confirm against the decision email and the current
  Final Paper Submission Guidelines rather than a prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / tool name / acks / links restored? yes/no
[IEEE gates] eCF complete? PDF eXpress passed? author registered? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Release] anonymized link replaced by DOI archive? yes/no/na
[Remaining owner] <person -> task before the final-paper deadline>
```
