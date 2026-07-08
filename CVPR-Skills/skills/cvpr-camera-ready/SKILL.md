---
name: cvpr-camera-ready
description: Use when preparing the final version of an accepted CVPR paper, covering de-anonymization, the dataset-release-by-camera-ready obligation, CVF open access versus the IEEE Xplore version of record, oral/highlight/poster preparation at conference scale, and arXiv/preprint synchronization after acceptance.
---

# CVPR Camera-Ready

Use this after a CVPR acceptance (decisions landed February 20 in the 2026 cycle,
conference in early June). The verified 2026 publication pipeline is described below;
the *mechanical* camera-ready details for any given year — exact deadline, page
allowance, IEEE forms — were not fetchable at check time and are 待核实: read the
instructions email and the current Author Guidelines before building the final PDF.

## Where the paper actually ends up

Accepted CVPR papers are published twice, and the two copies serve different audiences:

- **CVF open access** (`openaccess.thecvf.com`): free to everyone, posted around the
  conference; the file is the accepted version apart from a watermark. This is the copy
  the field reads and the one bibliography tools usually find first.
- **IEEE Xplore**: the version of record, under IEEE Computer Society co-sponsorship.
  Institutional reporting and some citation databases key off this one.

There is no author-side publication fee; costs ride on registration. Consequence for
you: the PDF you upload at camera-ready *is* the artifact of record in both channels —
there is no copy-editing pass to catch your mistakes.

## De-anonymization without breakage

Reversing double-blind is edit work, not a switch:

1. Restore authors, affiliations, and emails in the final class-file mode.
2. Write real acknowledgements (grants, compute donors) — banned during review, expected
   now.
3. Convert third-person self-citations back where the prose became misleading ("[12]
   showed" → "we showed in [12]" only where it clarifies lineage).
4. Replace every "anonymous supplementary" pointer with live URLs: code repo, project
   page, dataset host. Links were banned at submission; the camera-ready is where they
   belong.
5. Rebuild and re-read — de-anonymization routinely reflows line breaks and can push a
   tight page over whatever the final-version limit is that year.

## The dataset clause has a deadline

Verified 2026 policy: if the paper claims a **dataset release as a scientific
contribution**, the dataset must be publicly available **no later than the camera-ready
deadline**. "Available upon request" or a landing page with a form does not meet the
bar you promised reviewers. Licensing, hosting bandwidth, and consent/PII scrubbing all
have to be finished on the paper's schedule, not the lab's.

```bash
# Release-readiness probe, run from a machine outside your institution
curl -sIL https://<dataset-host>/<archive> | grep -Ei 'HTTP|content-length'
sha256sum downloaded_archive.tar.gz          # matches the checksum printed in the repo?
python3 - <<'EOF'
import json; m = json.load(open("meta/license.json"))
assert m["license"] and m["contact"], "license/contact missing from release metadata"
EOF
```

## Oral, highlight, or poster: what changes

In 2026 the program split acceptances into tiers (program trackers reported 141 orals in
four parallel tracks and 578 highlights among 4,090 acceptances — cross-check the
official program before quoting). What each tier means for preparation:

| Outcome | Extra deliverables | Preparation reality |
|---|---|---|
| Oral | Talk + poster | A few minutes on a big stage; rehearse to time, design slides for the back row |
| Highlight | Poster, flagged in the program | Extra foot traffic; the poster must carry the paper alone |
| Poster | Poster | Thousands of attendees walk the halls; a legible headline result beats density |
| Award candidate | Talk logistics vary | Committee re-reads the paper — camera-ready polish matters twice |

Every tier presents at a venue with five-digit attendance (about 12,200 registrants in
2026), so print deadlines, poster-size specs, and the video/teaser uploads requested by
the virtual platform belong on the same checklist as the PDF.

## Final-PDF quality assurance

The version of record gets no editorial pass, so run your own. Faults found in
published CVPR PDFs year after year, all preventable in an afternoon:

1. Rebuttal-promised changes never applied — diff the rebuttal's commitments ("we
   will cite [Foo]", "we will clarify the protocol") against the final text, item by
   item.
2. Reviewer-visible numbers silently changed. If a table improved after acceptance
   (bug fix, longer training), say so in a footnote; unexplained deltas between the
   reviewed and published versions are the stuff of integrity threads.
3. Camera-ready line numbers left on, draft watermarks, or `\usepackage{review}`-mode
   artifacts from the author kit.
4. Broken cross-references from late figure surgery (`Fig. ??`), and citations still
   pointing to arXiv versions of papers that have since been published (fix per
   `cvpr-related-work`).
5. Author metadata: the OpenReview record, the PDF author block, and the form you
   file with the publisher must agree on names, order, and affiliations — mismatches
   propagate to IEEE Xplore and are painful to correct later.

## Synchronizing the public record

After acceptance, converge the copies: update the arXiv version to match the
camera-ready (arXiv posting was already legal during review), point the repo README at
the CVF page once it exists, and use one canonical BibTeX everywhere — mixed
arXiv/proceedings citations fragment your citation count for years. Keep the media
embargo in mind in reverse: it lifted at acceptance, so coordinated publicity is now
allowed.

## Reverify each cycle (all 待核实 for the current year)

- Camera-ready deadline, final page allowance, and whether an extra page is granted.
- Whether the final template differs from the submission template (line numbers off,
  copyright block on).
- IEEE copyright/e-forms and PDF validation requirements.
- Registration-per-paper and in-person presentation obligations.
- Poster dimensions, talk lengths, and virtual-platform upload list.

## Output format

```text
[Camera-ready status] on-track / blocked
[Version-of-record checks] deanonymized · acknowledgements · live links · page fit
[Dataset clause] not-claimed / released-and-probed / BLOCKED: <gap>
[Tier prep] oral/highlight/poster deliverables and dates
[Public sync] arXiv updated · repo pointed · canonical BibTeX chosen
[待核实 items] <forms, deadline, page allowance for this year>
```
