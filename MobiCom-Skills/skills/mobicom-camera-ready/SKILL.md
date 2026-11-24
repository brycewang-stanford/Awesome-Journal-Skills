---
name: mobicom-camera-ready
description: Use when preparing an accepted MobiCom paper for publication — de-anonymizing into the double-column final version, discharging every rebuttal and revision promise, completing ACM rights and metadata, coordinating the artifact-badge timeline, and planning the in-person presentation for the Austin program.
---

# MobiCom Camera-Ready

Acceptance turns the paper from an anonymous 12-page argument into a published,
attributed ACM record. Camera-ready is where the double-blind wrapper comes off, where every
promise made during review comes due, and where ACM's publishing machinery — rights,
metadata, badges — has to be completed on a fixed clock. Treat it as an audit, not a
formatting pass.

## De-anonymize deliberately

The final version restores what the submission hid:

| Item | Action |
|---|---|
| Author names and affiliations | add in the ACM double-column author block |
| Acknowledgments and funding | restore, with correct grant numbers |
| Self-citations | convert third-person ("prior work [12]") back to first person where appropriate |
| Repository / dataset URLs | make real (they were anonymized or withheld at submission) |
| PDF metadata | set author/title fields correctly |

Do a reverse of the blindness sweep (`mobicom-submission`): confirm nothing that *should* now
be attributed is still anonymized, and nothing that should be a working link is still a
placeholder.

## Discharge every review promise

Continuing reviewers and readers hold you to the record. Before finalizing:

- Clear the **anonymous shepherding** first: MobiCom 2027 accepts are conditional until a TPC
  shepherd, working with the reviewers, signs off a revision — a 4-6-week process that may
  require new experiments or material.
- Fold in every clarification made in the **rebuttal** and every required item from a
  **one-shot revision** (`mobicom-author-response`); a commitment that silently vanishes is a
  credibility loss the community remembers.
- Re-check that headline numbers in the abstract and introduction still match the final
  experiments after any revision re-runs (`mobicom-experiments`).
- Keep the strongest result in the body — camera-ready is not the moment to demote it to an
  appendix to make room.

## Format holds at 12 double-column pages

The final paper keeps the **double-column geometry** and the page discipline (the exact final
page allowance and any extra-page option are 待核实 — confirm on the acceptance instructions).
Figures still count; references and appendices remain outside the body cap
(`mobicom-supplementary`). Do not let de-anonymization (a longer author block, added
acknowledgments) silently push the body over.

## ACM rights, metadata, and badges

```text
Publication checklist (dates on the acceptance instructions; the 2027 camera-ready page was
not yet published on 2026-11-24 — 待核实):
  [ ] ACM eRights form completed; correct copyright/licensing selected
  [ ] title, authors, affiliations, abstract entered to match the PDF exactly
  [ ] ACM classification / keywords set
  [ ] artifact badges coordinated: AEC outcome reflected on the paper (Available /
      Functional / Reproduced) per the artifact timeline (`mobicom-artifact-evaluation`)
  [ ] camera-ready PDF passes the publisher's format validation
  [ ] every author has an ORCID iD
  [ ] 90-second teaser video submitted with the camera-ready (posted up to two weeks
      before the conference)
  [ ] APC settled: ACM publishes open access; authors outside ACM Open institutions pay
      an APC unless waived (2027 subsidized: $500 ACM/SIG members, $750 non-members)
```

The artifact-badge timeline may run separately from the paper deadline; confirm both clocks
so a badge you earned actually appears on the published version.

## Plan the in-person talk

MobiCom 2027 is in **Athens, Greece, October 18-22, 2027**. By submitting, the authors agreed
that **at least one author registers and attends to present**. The TPC picks a subset of papers
for full talks; the rest give shorter **lightning talks followed by posters** — all accepted
papers are equal. Registration fees and remote options are 待核实. Plan early:

- Designate the presenter and confirm travel and registration against the program dates.
- Build the talk around the **mechanism and its measured evidence**, the same arc as the
  paper's first page (`mobicom-writing-style`) — a demo or a short over-the-air video often
  lands harder than a results table.
- Prepare for the wireless-specific questions reviewers raised: channel conditions,
  mobility realism, energy boundary.

## Final checklist

- [ ] De-anonymized fully; reverse blindness sweep passed.
- [ ] Shepherd sign-off received; every rebuttal/revision commitment folded in and consistent.
- [ ] 90-second teaser video ready.
- [ ] Headline numbers match final experiments.
- [ ] Double-column format holds; body within the page allowance.
- [ ] ACM rights + metadata complete; badges coordinated.
- [ ] Presenter designated; talk built on the mechanism→evidence arc.

## Output format

```text
[De-anon] author block / ack / links / metadata restored — gaps flagged
[Promises] rebuttal + revision commitments discharged? each listed
[Format] page/column check after de-anon
[Publishing] rights / metadata / badge status
[Talk] presenter + registration + demo plan
```
