---
name: sigcomm-camera-ready
description: Use when preparing an accepted ACM SIGCOMM paper for the TAPS proceedings — clearing shepherd sign-off in HotCRP, uploading the final PDF plus source under acmart, de-anonymizing author and deployment identity, keeping the 12-page body under ACM two-column reflow, appendix-necessity approval, and releasing the public artifact by the badge deadline.
---

# SIGCOMM Camera Ready

Use this after acceptance. Reopen the current camera-ready instructions, the ACM TAPS
requirements, and your shepherd's HotCRP thread before finalizing; the 2026 cycle set the
camera-ready deadline at **July 3, 2026, 23:59 UTC**, with the final version approved by the
shepherd via a HotCRP comment.

## Clear the shepherd first

At SIGCOMM the shepherd gates the final version. Before you polish anything:

- Map each review and meta-review concern to a concrete edit and confirm the mapping with the
  shepherd through HotCRP comments — do not assume silence is approval.
- The shepherd also **approves whether any appendix is necessary**; be ready to justify each
  appendix or fold it into the body, and expect to remove one that is not load-bearing.
- Do not strengthen the accepted contribution into something reviewers never evaluated;
  camera-ready is clarification and integration, not a new result.

## De-anonymization sweep

| Anonymized in submission | Restored for camera-ready |
|---|---|
| Author names, affiliations, ORCIDs | Full author block in ACM metadata and PDF |
| Acknowledgments and funding | Restored, spelled out |
| Deployment / system / company names | Real names where the paper's honesty needs them |
| Anonymized artifact links | Public, licensed, citable archive with a DOI |
| Third-person self-citation | Natural first-person where it improves clarity |

Test every restored link from a logged-out browser, and confirm the artifact archive is the
one the paper actually points to.

## ACM two-column reflow

Switching `acmart` from the review to the final mode changes spacing, and adding the author
block, acknowledgments, and funding lines consumes room the anonymous draft did not use.
Recheck every page break, figure placement, and wide table after the flip; multi-panel
measurement plots and full-width topology figures are the usual overflow culprits. Keep
section, theorem-if-any, and equation numbering stable so the review record stays traceable
to the final text.

## The TAPS pipeline

SIGCOMM finals go through the ACM Publishing System, which regenerates the PDF from your
source, so local-only PDF tweaks will not survive:

```text
# TAPS-facing checklist
[ ] Upload BOTH the final PDF and the complete LaTeX/Word source to HotCRP
[ ] acmart.cls (or ACM Word template), unmodified class options
[ ] Correct ACM rights/CCS concepts and keywords entered
[ ] All fonts embedded; figures at publication resolution
[ ] References complete with DOIs; artifact/DOI links live
[ ] Shepherd HotCRP comment recording final-version approval
```

Fix problems in the **source**, recompile, and re-check the TAPS-produced PDF rather than
editing the PDF by hand.

## Release the artifact on its own clock

Artifact evaluation and badge assignment run on a separate schedule from the paper deadline.
Once anonymity no longer applies, publish the code, traces, topologies, and configuration to
a permanent archive with a DOI, and submit to the artifact-evaluation committee for the
badges you can honestly support (see `sigcomm-artifact-evaluation`). A public artifact by the
badge deadline is also what makes a paper eligible for the reproducibility recognition the
venue prizes.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Shepherd] concerns mapped, appendix necessity, HotCRP approval — status
[Final package] TAPS PDF + source / acmart / rights / fonts / references
[De-anonymization] authors / funding / deployment names / artifact links
[Artifact] public archive + DOI + AEC submission — status
[Remaining owner] <person -> task>
```
