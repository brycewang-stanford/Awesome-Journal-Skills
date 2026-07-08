---
name: ccs-camera-ready
description: Use when preparing an accepted ACM CCS paper for the ACM Digital Library proceedings, covering de-anonymization, the ACM sigconf final format, ACM rights and eRights forms, badge placement from artifact evaluation, incorporation of shepherd and minor-revision requirements, disclosure-timing coordination, registration, and in-person presentation.
---

# CCS Camera Ready

Use this after acceptance or after clearing a minor revision. Reopen the current CCS
camera-ready instructions, the ACM rights form, the registration page, and the notification
or shepherd email before advising authors.

## Camera-ready audit

- Convert the anonymous submission to the public proceedings version: author names,
  affiliations, acknowledgements, funding, and artifact links restored.
- Apply the ACM `sigconf` final template and the ACM rights-management block; the DOI, the
  conference reference string, and the copyright notice come from the ACM eRights system.
- Incorporate exactly what the shepherd or the minor-revision decision required, without
  expanding the contribution beyond what was reviewed.
- Place any artifact-evaluation badges earned (Available, Functional, Reusable, Results
  Reproduced) as instructed; badge placement is part of the ACM camera-ready workflow.
- Confirm the final title and abstract match the HotCRP-registered title and abstract if the
  cycle froze them at registration.
- Coordinate disclosure timing: the public proceedings version and any released exploit or
  advisory should not appear before the agreed vendor-disclosure date.

## Badge placement map

| Badge earned in artifact evaluation | Where it goes | What to confirm |
|---|---|---|
| Artifacts Available | First page, with the archival DOI/URL | The archive is public and permanent before camera-ready |
| Artifacts Evaluated - Functional | First page | The committee's functional result is final |
| Artifacts Evaluated - Reusable | First page | Documentation matches the reusable claim |
| Results Reproduced | First page | The reproduced results match the camera-ready numbers |

## De-anonymization sweep

- Restore the author block, acknowledgements, grants, and contribution statements the
  anonymous version stripped.
- Rewrite third-person self-citations into natural first person where it improves clarity.
- Replace anonymized repository placeholders with the public, licensed, archived artifact and
  test every link from a logged-out browser.
- Re-check that de-anonymizing did not silently reveal an embargoed vendor before its patch.

## ACM proceedings reflow

- Switching from the submission build to the final `sigconf` build changes spacing; recheck
  every page break, protocol figure, and wide result table after adding the author block.
- Material that fit the 12-page anonymous body can overflow once affiliations,
  acknowledgements, and the rights block are added; confirm the final length against the
  camera-ready page instruction rather than assuming.
- Keep theorem, protocol, and section numbering identical to the reviewed version so the
  meta-review and shepherd record stay traceable.

## Worked example: integrating a shepherd requirement

The shepherd asked that the adaptive-attack results move from the appendix into the main
evaluation. Camera-ready move: promote the adaptive table into Section 6, add one sentence
interpreting the degraded defense numbers honestly, and leave the full attack derivation in
the appendix — without strengthening any claim the reviewers did not see.

## Hedged logistics

- Registration pricing, the exact camera-ready and rights-form deadlines, and badge-placement
  mechanics change every cycle; confirm against the notification email and current instructions.

## Output format

```text
[Camera-ready status] Ready / Needs fixes / Blocked
[Final package] <PDF / source / bib / ACM rights form / badges / artifacts>
[Policy checks] <format / authors / disclosure timing / registration / presentation>
[Reviewer-change map] <shepherd/revision requirement -> final edit>
[Remaining owner] <person -> task>
```
