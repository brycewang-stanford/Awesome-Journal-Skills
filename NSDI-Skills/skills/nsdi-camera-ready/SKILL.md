---
name: nsdi-camera-ready
description: Use when converting an NSDI acceptance into a published, presented paper — de-anonymizing within the same 12-page cap, meeting the final-papers deadline that also gates Community Award eligibility, designating the presenter, and landing in USENIX's open-access proceedings for the May symposium.
---

# NSDI Camera-Ready

Acceptance starts a production pipeline with several deliverables owned by different
people — the final PDF, the public artifact, the presenter designation, and the trip
to the symposium. Facts below reflect the NSDI '26/'27 pages rendered on 2026-07-08;
the '27 final-paper dates were not yet posted (待核实), so anchor every date to the
notification email and the authors' instructions it links.

## Deliverables and owners

| Deliverable | Owner to assign | Hard constraint |
|---|---|---|
| Final PDF | writing lead | same 12-page cap as submission |
| Public artifact release | artifact lead | before final-papers date for award eligibility |
| Production/copyright forms | corresponding author | per the authors' instructions |
| Presenter designation | presenting co-author | via the co-chairs' Presenter Information form |
| Travel, visa, registration | presenter | May 11-13, 2027, Providence, RI |

Assign these on notification day. Cohort timing matters here: a spring acceptance
(notified July) has months of runway before the May symposium, while a fall
acceptance (notified December) runs its production pipeline much closer to the
event — same deliverables, tighter interleaving.

## The final PDF

NSDI's cap is symmetric: **final papers, like submissions, are limited to 12 pages
including footnotes, figures, and tables**, references and appendices beyond. There
is no accepted-paper page bonus to spend, so camera-ready editing is substitution,
not addition:

- **De-anonymize:** real names, affiliations, acknowledgments, funding — all inside
  the same 12 pages the anonymous version used, which usually costs a few lines;
  reclaim them from prose, not from evidence.
- **Restore what blinding distorted:** research-track papers that neutralized
  deployment context ("a large provider") may now name it — verify employer/legal
  sign-off on every restored detail, since this step is where confidentiality
  incidents happen.
- **Real links replace anonymized ones:** repository, DOI'd archive, dataset pages —
  consistent with what the artifact ships (`nsdi-artifact-evaluation`).
- **Honor the revision record:** for papers accepted via one-shot revision, confirm
  every change promised in the change memo survived into the final text; shipping a
  final that quietly reverts a required fix betrays the reviewers who accepted on
  those terms.
- Then re-verify the page count — de-anonymization and shepherd-requested edits both
  nudge layout.

## One deadline, two prizes

The **final-papers deadline** carries double weight at NSDI: it is the production
cutoff, and it is the **Community Award eligibility line** — the award goes to the
best paper whose code and/or dataset is public by that date. Sequence accordingly:

1. Public release of the artifact repository/archive (with license and DOI) *before*
   the final-papers date.
2. Final PDF cites those live, permanent URLs.
3. Artifact-badge evaluation proceeds on its own schedule; badge outcomes do not
   retroactively fix a missed release date.

## Presenter and symposium duties

- Accepted papers **designate one co-author as presenter** via the Presenter
  Information form the program co-chairs distribute. Decide early — visa timelines
  for a US venue (Providence, RI for May 11-13, 2027) run months, and the presenter
  should ideally be the person who can answer testbed questions.
- Registration requirements, speaker discounts, and remote-presentation options for
  '27 are 待核实 — read the instructions-for-presenters page of the current edition
  rather than assuming either flexibility or rigidity.
- Spring-cohort papers surface on the public accepted-papers list well before the
  event; coordinate any press/blog timing with your institution against the venue's
  publication schedule, not against the symposium date alone.

## Open access, and what it changes

USENIX proceedings are open access: the final PDF becomes a permanently free
download on `usenix.org`, joining a record where every prior NSDI paper is equally
free. Practical consequences:

- No paywalled-version hedging — the `usenix.org` PDF is the canonical citation
  target; sync any arXiv/preprint copy to the final text or clearly mark it stale.
- The paper will be read far outside the reviewing community (operators, OSS users,
  hiring committees); the abstract and figure captions carry more weight than at
  paywalled venues.
- Slides and talk materials commonly join the presentation page; treat them as part
  of the paper's permanent public footprint.

## Production checklist

```text
[ ] Authors/affiliations restored; ORCID/name spellings confirmed by each coauthor
[ ] Acknowledgments + funding numbers complete (grant offices care)
[ ] 12-page cap re-verified after de-anonymization
[ ] Employer/legal sign-off on restored deployment details
[ ] Revision-memo promises intact in final text
[ ] Artifact public with license + DOI before final-papers date (award clock)
[ ] All URLs in the PDF resolve and are permanent
[ ] Copyright/production forms submitted per authors' instructions
[ ] Presenter designated via the form; travel/visa started
[ ] Metadata (title/abstract) identical across HotCRP, PDF, and artifact README
```

## After the symposium

The paper's public life is just beginning: keep the artifact's pinned dependencies
buildable for at least the horizon on which one-shot-revision reviewers and
follow-up work will consult it; route errata through the venue's published
correction channel rather than silently editing preprint copies; and archive the
talk recording/slides link alongside the repository README so the three public
faces of the work — PDF, artifact, talk — reference each other.

## Output format

```text
[Deadline map] final-papers date + form dates (from notification email)
[PDF status] de-anonymized / cap verified / links live / memo honored
[Award clock] artifact public before final-papers date? y/n + date
[Presenter] designated? visa/travel risk level
[Open-access sync] preprint copies reconciled with canonical PDF
[Open items] owner -> item -> due date
```
