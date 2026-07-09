---
name: socc-camera-ready
description: Use when preparing an accepted ACM SoCC paper for its camera-ready, covering de-anonymization, the acmart/sigconf final format and ACM metadata (DOI, ORCID, CCS concepts), integrating reviewer-required changes without scope creep, permanentizing released code and traces, the ACM rights/e-copyright form, and the presentation obligation in Singapore.
---

# SoCC Camera Ready

Use this after acceptance in a SoCC round. The camera-ready turns the anonymized `acmart`
submission into the final ACM Digital Library version of your ACM Symposium on Cloud Computing
paper. Reopen the current SoCC author instructions, the acceptance email, and the ACM rights page
before advising — SoCC is jointly SIGMOD+SIGOPS, and its camera-ready is an ACM production step,
not just a formatting pass.

## Camera-ready audit

- **De-anonymize completely:** restore the author block, affiliations, acknowledgements, funding,
  and the real system, cluster, provider, and trace names that dual anonymity forced you to hide.
- **Apply the final format:** the ACM Primary Article Template, `sigconf`, within the 12-page (full)
  or 6-page (short) budget, with any camera-ready page allowance the acceptance letter grants;
  references remain unlimited.
- **Complete ACM metadata:** title/abstract, author order, ORCIDs, ACM **CCS concepts** and
  keywords, and the DOI-bearing citation once assigned. Metadata errors are harder to fix after
  publication than formatting ones.
- **Integrate reviewer-required changes** from the reviews and rebuttal faithfully — add the tail or
  cost breakdown you promised, fix the misread workload — **without strengthening claims beyond what
  was evaluated**.
- **Permanentize reproducibility:** replace anonymized artifact links with a public, licensed,
  DOI-issuing archive, and make released code, workload generators, and traces available (or
  document why a trace cannot be released).
- **Confirm registration and presentation:** SoCC 2026 is in person in Singapore (Nov 18-20, 2026);
  at least one author presents.

## De-anonymization sweep

| Anonymized at submission | Restore at camera-ready | Watch for |
|---|---|---|
| Author block, affiliations, ORCID | Full, correctly ordered | Wrong author order breaks the DOI citation |
| System / cluster / trace name | Real name throughout text, figures, artifact | A leftover anonymized placeholder in a caption |
| Cloud provider / deployment identity | Restored where disclosable | Confidentiality limits on naming a provider |
| Acknowledgements, funding | Restored | Grant numbers required by funders |
| Self-citations (third person) | Natural first-person where it aids clarity | Over-correcting and double-citing |
| Artifact / trace link | Public archive DOI | The old anonymized URL surviving in a footnote |

## ACM production checks

```text
[Template]   acmart sigconf, current revision; no manual margin/font edits; correct page budget
[Metadata]   title, abstract, authors+ORCID, CCS concepts, keywords entered and matching the PDF
[References] complete, consistent, DOIs where available; unlimited allowance, but keep it clean
[Figures]    vector where possible; tail/cost plots readable in print; captions self-contained
[Rights]     ACM e-rights/copyright form completed; correct rights block on the first page
[Links]      every released-code and trace link resolves from a logged-out browser
```

## Worked example: integrating a rebuttal promise

The reviewers accepted the paper on the condition that the p99.9 breakdown and the pricing model
behind the cost claim appear in the final version. Camera-ready move: add the p99.9 figure from the
existing logs beside the p99 result, add one paragraph stating the pricing model and the resulting
saving, restore the real system and testbed names in those figures, and point the availability
statement at the now-public trace-replay archive — **without** expanding the cost claim beyond the
regimes measured.

## Artifact and badge handoff

If the edition runs artifact evaluation, the camera-ready and the artifact process may be separate
deadlines. Do not wait for the artifact result to finalize the paper, but make the paper's
availability statement consistent with the ACM badges you are pursuing (Available at minimum;
Functional / Reusable / Reproduced if the track grants them). Add any badge acknowledgement only per
the current instructions. Whether SoCC offers evaluation for a given edition is **待核实** — confirm
on the current call (`socc-artifact-evaluation`).

## Hedged logistics

- Page allowances, metadata fields, rights-form mechanics, and exact camera-ready dates change each
  cycle and per round; confirm against the acceptance email and current SoCC instructions rather
  than a prior year.

## Output format

```text
[Camera-ready status] ready / needs fixes / blocked
[De-anonymization] author block / system+trace names / acks / links restored? yes/no
[ACM metadata] ORCID / CCS / keywords / rights form complete? yes/no
[Reviewer-change map] <required change -> final edit, no scope creep>
[Reproducibility] anonymized links replaced by DOI archive? trace released or exception documented?
[Remaining owner] <person -> task>
```
