---
name: iros-camera-ready
description: Use when preparing an accepted IROS paper for IEEE Xplore camera-ready — de-anonymization from the double-anonymous cycle, integrating the meta-review, the IEEE electronic copyright form (eCF), the July final-paper deadline, registration and in-person presentation, and the public artifact release anonymity had blocked.
---

# IROS Camera Ready

Use this after acceptance. Reopen the current IROS final-submission instructions, the IEEE PDF-eXpress
and copyright pages, the registration page, and the presentation policy before advising authors. For the
2026 cycle the camera-ready (final paper) deadline was **July 10, 2026**, close behind the **June 16**
notification — a short turnaround, so plan it as part of submission, not an afterthought.

## Camera-ready audit

- Convert the anonymous submission to the public version: restore the author block, affiliations,
  acknowledgements, funding, and any code/data links stripped for double-anonymous review.
- Apply the current final-page rules and confirm whether references and any content still fit the budget
  once the author block and acknowledgements are added back.
- Integrate the **meta-review's requested changes** without expanding the contribution beyond what was
  reviewed.
- Run the paper through **IEEE PDF-eXpress** (or the cycle's equivalent) for Xplore compliance, and file
  the **IEEE electronic copyright form (eCF)** — publication in Xplore is gated on it.
- Prepare the **public artifact release** now that anonymity no longer applies: repository, logs, configs,
  datasets, and a citable archive; test every link from a logged-out browser.
- Confirm **registration and in-person presentation** obligations; at least one author typically must
  register and present.

## De-anonymization sweep

- Restore the author list exactly as entered in PaperPlaza metadata; a mismatch between the metadata and
  the camera-ready authorship creates a real dispute vector on the Xplore record.
- Rewrite third-person self-citations ("the XYZ rover [9]") back into natural first-person form where it
  improves clarity.
- Replace anonymized figure and video footage with the real, identified versions if you kept scenery
  blurred for review — and re-check that nothing embarrassing was left cropped.
- Swap anonymized code mirrors for the public, licensed repository.

## Common camera-ready reflow surprises

| Change at camera-ready | Effect | Fix |
|---|---|---|
| Author block + affiliations added | Content reflows; a tight paper may overrun | Trim or budget for it before the flip |
| Acknowledgements/funding restored | Extra lines near the end of the paper | Compress a nearby paragraph |
| Real (unblurred) figures swapped in | Sizes/DPI differ from anonymized placeholders | Re-check figure placement and legibility |
| Public links added | Dead or identity-wrong links | Test each from a logged-out browser |

## Worked example: integrating a meta-review fix

The meta-review asked that failure cases be reported. Camera-ready move: add the failure-taxonomy table
you already logged, one sentence interpreting it, and a pointer from the results discussion — without
strengthening any success claim the reviewers did not evaluate.

```text
Camera-ready gate (do not submit until all true):
  [ ] author block + acknowledgements restored; page budget still met
  [ ] meta-review asks integrated, no scope inflation
  [ ] IEEE eCF filed; PDF-eXpress compliant
  [ ] public artifact + links tested logged-out
  [ ] registration done; presenter assigned
  [ ] final/updated video meets the current spec
```

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF / eCF / metadata / artifact / video>
[Policy checks] <page budget / authors / registration / presentation>
[Meta-review map] <ask -> final edit>
[Remaining owner] <person -> task, before the July deadline>
```
