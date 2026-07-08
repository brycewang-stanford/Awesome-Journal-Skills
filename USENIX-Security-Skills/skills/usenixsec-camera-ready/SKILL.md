---
name: usenixsec-camera-ready
description: Use when preparing final papers for the USENIX Security Symposium after acceptance — de-anonymizing, keeping the Ethical Considerations and Open Science appendices current, clearing the mandatory Phase-1 artifact availability check before finals are due, and meeting USENIX's open-access publication and presentation obligations.
---

# USENIX Security Camera-Ready

Acceptance at USENIX Security starts a short, condition-laden runway: in the '26
cycles, final papers were due about six weeks after notification (Cycle 1: notified
Dec 4, 2025, finals Jan 15, 2026; Cycle 2: notified May 14, 2026, finals Jun 11,
2026), and during that same window the **mandatory artifact-availability check had
to pass**. The camera-ready is therefore not a formatting chore — part of the
acceptance itself is still pending.

## What is actually conditional

Under the '26 Open Science policy, acceptance is conditional on the artifact
evaluation committee verifying, before finals are due, that the artifacts named in
the paper's Open Science appendix are genuinely available — or that the appendix
carries a justified explanation for withholding them. Plan the runway backwards
from that:

| Week after notification | Camera-ready lane | Artifact lane |
|---|---|---|
| 1 | Ingest decision + shepherd requests | Move artifacts from anonymous mirror to permanent home |
| 2–3 | Apply required edits; shepherd sign-off | Submit availability materials; respond to AE contact |
| 4 | De-anonymize; final template pass | Availability verified (Phase-1 complete) |
| 5–6 | Upload finals + metadata; presenter forms | Decide on optional Phase-2 (Functional / Reproduced) |

## De-anonymization done in the right order

Restore identity everywhere it was stripped, and keep the pieces consistent:

- Author block and affiliations, matching the HotCRP metadata exactly — the
  proceedings entry is generated from what USENIX has on file.
- Acknowledgements and funding, which double-blind rules forced out of the
  submission.
- Self-citations rewritten back to natural first-person where that reads better.
- **Artifact URLs**: replace every anonymized mirror with the permanent, named
  location. A camera-ready pointing at a dead anonymous repository is the classic
  post-acceptance defect at this venue, because reviewers checked the anonymous one
  and nobody rechecks the swap.

The two named appendices — "Ethical Considerations" and "Open Science" — remain in
the final paper, updated: disclosure timelines that were "in progress" at submission
should state their current status (vendor response, CVE assignment, patch release).

## Mechanical pass before upload

```bash
# Final-paper checks
pdftotext final.pdf - | grep -nEi 'anonym|under submission|double.blind' | head
pdftotext final.pdf - | grep -noE 'https?://[^ ]+' | sort -u > urls.txt
while read -r n url; do curl -sIL --max-time 10 "${url#*:}" -o /dev/null \
  -w "%{http_code} ${url}\n"; done < <(tr ':' ' ' < urls.txt | head -40)
pdffonts final.pdf | awk 'NR>2 && $4!="yes"'   # any non-embedded font lines = fix
```

Follow the current "Instructions for Presenters and Authors of Accepted Papers"
page for the cycle — title formatting, copyright/consent forms, and slide or poster
requirements are set there, not in the CFP.

## Publication model: open access, no author fee

USENIX publishes Security proceedings open access; papers (and later, talk
recordings) are freely available on usenix.org. There is no article charge. The
author-side obligations run through the conference instead: presentation at the
symposium in Baltimore (Aug 12–14, 2026 for the '26 program) per the current
presenter instructions. Registration mechanics, speaker-registration rules, and any
remote-presentation allowance are per-year decisions — 待核实 against the
instructions page for your cycle before booking anything.

Cycle-1 authors get a bonus decision: finals are locked ~7 months before the
symposium, so plan whether to post an extended version (arXiv or tech report) in
the gap, and make the proceedings version state clearly which version is canonical.

## Badge and visibility follow-through

- Optional Phase-2 artifact evaluation (Functional / Results Reproduced badges)
  happens **after** finals are due — the camera-ready must not overstate badge
  status it does not yet hold.
- Distinguished Paper Awards and the Internet Defense Prize are selected from the
  final program; nothing to do except have the final PDF be the strongest version.
- Add the paper's usenix.org proceedings URL to the artifact README once live, so
  artifact users land on the canonical version.

## Reverify each cycle

- Final-paper deadline for your cycle and the shepherd-approval interaction.
- Whether Phase-1 availability verification remains a condition of acceptance.
- Presenter/registration requirements and any remote option (待核实 for '27).
- Formatting and form requirements on the current instructions page.

## Output format

```text
[Runway] notification → finals dates; days remaining
[Conditions open] shepherd sign-off / Phase-1 availability / forms
[De-anonymization] identity restored + artifact URLs swapped and re-tested
[Appendices] Ethical Considerations + Open Science updated to current status
[Presentation] presenter, registration status, travel constraints
```
