---
name: asplos-camera-ready
description: Use when converting an ASPLOS acceptance or Major Revision decision into a publishable ACM paper within the six-week window — de-anonymization, ACM rights and template obligations, the revision change note, artifact-appendix integration and badge placement, and Digital Library metadata checks.
---

# ASPLOS Camera-Ready

The camera-ready deadline at ASPLOS 2027 sits roughly **six weeks after
notification** — verified indirectly, via the CFP's statement that Major Revisions
are resubmitted "at the camera ready deadline (6 weeks from notification)"
(checked 2026-07-08; the exact date and page allowance for camera-ready are 待核实
and arrive with the acceptance email). The window is shared by two very different
tasks, so the first step is knowing which track you are on.

## Two tracks through the same deadline

| Track | What is due | Judged by |
|---|---|---|
| **Accepted paper** | Final, de-anonymized, ACM-formatted PDF + forms | Publication staff + shepherd if assigned (shepherding for 2027: 待核实) |
| **Major Revision** | The *revised submission* — still a reviewed document | The program committee, as a submission on record |

Do not apply camera-ready instincts to a Major Revision: it stays within submission
rules (anonymity unless told otherwise — confirm in the decision letter),
and its companion document is a **change note keyed to the decision letter**, item
by item, with pointers to where each required change landed. If this revision
follows an earlier revision, the note describes deltas relative to the *previous
revision*, per the CFP's revision-counts-as-submission rule.

## De-anonymization, done as a diff

Reversing double-blind is not just adding an author block. Work from the
submission-time anonymity sweep, inverting each entry:

- Restore author names, affiliations, and emails in the ACM template's format.
- Convert third-person self-citations back to natural first-person where it reads
  better — and check none of them still says "the authors of [12]" about yourself.
- Restore acknowledgments and grant numbers; keep the **GenAI disclosure** placed
  per ACM policy (immediately before References when in Acknowledgments).
- Re-point anonymized supplemental citations to their real, now-citable targets.
- Replace neutralized infrastructure descriptions with the real testbed identity
  where confidentiality allows.

```bash
# residue sweep on the final PDF
pdftotext final.pdf - | grep -niE 'anonym|blind|supplemental material \[|placeholder' | head
pdfinfo final.pdf | grep -iE 'author|creator'   # metadata now SHOULD name you
```

## ACM-specific obligations

- The **rights form** drives the copyright block: complete it early, because the
  generated rights text must be pasted into the paper before the final build, and
  DOI/ISBN metadata follows from it.
- Verify title and author-list **exact match** between the rights form, the PDF,
  and the submission system — mismatches stall Digital Library ingestion and
  corrupt citation records for years.
- ASPLOS proceedings publish in the ACM DL in multiple volumes per edition under
  the multi-cycle model; your cycle determines your volume. Production workflow
  details (TAPS or classic, camera-ready page allowance) for 2027: 待核实 with the
  acceptance instructions.

## Artifact integration

Camera-ready is when artifact evaluation converges with the paper
(`asplos-artifact-evaluation`):

- The **Artifact Appendix** is finalized against the actual archived artifact —
  its dependency list is a promise readers will act on.
- **Badges** earned (Available / Functional / Reproducible) are attached by the
  authors or ACM; confirm placement follows the 2027 instructions rather than
  copying a previous year's badge layout.
- The archival deposit (DOI-issuing repository) must be public before the paper
  claims it; a dead artifact link in the DL is permanent embarrassment.

## Six-week sequence

1. **Day 0-2:** read the decision letter twice; extract every instruction and
   deadline into a checklist; identify track (accept vs revision).
2. **Week 1:** rights form; template migration; de-anonymization diff.
3. **Weeks 2-4:** shepherd/letter-required edits; final artifact deposit; appendix
   sync. For revisions: the required experiments, and nothing speculative.
4. **Week 5:** full residue sweep; metadata check; co-author read of the exact PDF.
5. **Week 6:** upload with margin; confirm the system shows the final version;
   archive the tagged source.

Presentation and registration obligations for 2027 (who must attend Heraklion,
April 11-15, 2027; fees; remote options) were 待核实 at pack-check time — read the
acceptance email's requirements before booking or skipping travel.

## Final-build quality gate

Run on the exact PDF going to production, not the working draft:

- Fonts embedded; figures vector where possible; colors legible in grayscale
  (the DL's print-view and many readers' printers are unforgiving).
- Every cross-reference resolves — a "Figure ??" in the published record is
  permanent, unlike in a submission.
- The bibliography still satisfies the full-name/DOI rules after camera-ready
  additions (new "since submission" citations arrive malformed by default).
- Appendix/artifact pointers updated from submission-time wording ("anonymous
  supplemental material") to their published targets.
- Title capitalization, author ordering, and affiliation strings match what
  co-authors expect to see indexed — this is the last moment ordering disputes
  can be resolved quietly.

## After publication: the unglamorous checklist

- Verify the DL landing page within days of proceedings release: PDF correct,
  authors ordered, badges displayed, artifact link resolving. Ingestion errors
  fixed early are emails; fixed late they are erratum processes.
- Keep the archived artifact's README pointing at the DOI-versioned release,
  and route post-publication fixes to a new tagged version rather than mutating
  the evaluated one — the badge attaches to what the committee evaluated.
- Record the edition's ordinal and volume in your own records; ASPLOS's
  multi-volume-per-edition publishing makes later citation reconstruction
  error-prone without it.

## Output format

```text
[Track] accepted-final / major-revision
[Letter checklist] items: N · addressed: N · pointers recorded: Y/N
[De-anonymization] diff complete · residue sweep clean: Y/N
[ACM forms] rights done · title/author exact-match verified: Y/N
[Artifact] deposit public + DOI minted · appendix synced · badges per instructions
[待核实] camera-ready date / page allowance / shepherding / attendance rules
```
