---
name: isca-camera-ready
description: Use when converting an accepted ISCA paper into its published form — de-anonymizing authors, acknowledgments, and artifact links; satisfying the edition's publisher workflow under the alternating ACM/IEEE arrangement; integrating shepherd requirements and badges; and preparing the June talk and attendance logistics.
---

# ISCA Camera-Ready

Acceptance starts a second, administrative project with real failure modes:
papers have appeared with anonymization stubs intact, dead artifact links, and
acknowledgments naming the wrong grant. The 2026 edition maintained a dedicated
camera-ready guidelines page (`iscaconf.org/isca2026/submit/cameraready.php` —
its detailed contents were not directly fetchable at verification time, so the
specific instructions below marked *practice* are community-standard rather than
quoted rules; the page itself is the authority — 待核实 per edition).

## The publisher variable unique to ISCA

ISCA's ACM SIGARCH + IEEE-CS TCCA co-sponsorship shows up concretely at
camera-ready: the publishing arrangement varies by edition (the 52nd
edition's proceedings were ACM-published; the 2026 edition carried IEEE
branding and pointed LaTeX users at an IEEE template). Everything downstream —
rights forms, copyright blocks, final template, DOI issuer, submission portal
for finals — follows the edition's publisher. Rule one of ISCA camera-ready:
**identify this edition's publisher workflow before touching the LaTeX**, and
expect it to differ from the last ISCA you published at.

## De-anonymization is a checklist, not a mood

Work from the submission's blinding actions and invert each one deliberately:

| Was blinded at submission | Camera-ready action |
|---|---|
| Author block absent | Full names, affiliations, emails — order confirmed by *all* coauthors in writing before upload |
| PDF metadata scrubbed | Regenerate with true metadata; verify with `pdfinfo` |
| Artifact links anonymized | Swap in canonical repo + archival DOI (`isca-artifact-evaluation`); click every link from the final PDF |
| Third-person self-citations | Recast where the prose reads absurdly; keep where fine |
| Acknowledgments omitted | Add funders with exact grant numbers, contributors, and any disclosure the publisher's policy requires |
| Neutralized cluster/trace names | Restore real names where licenses permit |

```bash
# Final-PDF de-anonymization verification (inverse of the submission sweep)
pdfinfo final.pdf | grep -i author            # now SHOULD list authors
pdftotext final.pdf - | grep -ci 'anonym'     # expect 0
pdftotext final.pdf - | grep -nE 'blind review|under submission' # expect none
pdftotext final.pdf - | grep -oE 'https?://[^ )]+' | sort -u > links.txt
while read -r u; do curl -s -o /dev/null -w '%{http_code} %s\n' "$u" "$u"; \
  done < links.txt | grep -v '^200'           # every link in the paper resolves
```

## Shepherds and required changes

If the acceptance carries a shepherd or a mandatory-revisions list, that list is
a condition, not a suggestion. Practice that keeps this smooth: send the
shepherd a change memo (item → what changed → where) with the revised draft,
early enough for one round of disagreement; where you believe a requested change
is wrong, negotiate in the memo — never silently skip an item and hope.

## Content changes: repair, don't remodel

Camera-ready is for review-driven repairs and accuracy fixes. If numbers
changed (a bug found post-acceptance, a rerun under the fixed seed), correct
them and ensure abstract/intro claims still match the tables — publishing known-
stale numbers because "it was accepted with them" is how errata happen. Do not
add new contributions; the version of record should be the reviewed paper,
healed. Any camera-ready page allowance beyond the submission's 11 text pages is
edition-specific and was not verified — 待核实 before planning to grow.

## Badges, statements, and the artifact block

Coordinate with the AE track (`isca-artifact-evaluation`): earned badges are
applied to the published paper under the ACM badging framework, and the
camera-ready typically carries an artifact-availability statement with the
archival DOI. Get the DOI *before* the camera-ready deadline by depositing the
evaluated snapshot early; retrofitting a DOI after the proceedings freeze is
somewhere between painful and impossible.

## The June obligations

The 2026 conference ran June 27 - July 1 in Raleigh. Between camera-ready and
the conference, in rough order of deadline pressure:

1. **Registration** — whether a specific author-registration category is
   mandatory per paper was not verified (待核实, and commonly true at flagship
   venues); resolve it the week of acceptance, with visa lead times in mind for
   international authors.
2. **Talk** — the community's norm is mechanism-forward: motivate with your
   measured data, spend the middle on how the design works (the walk-through
   from `isca-writing-style` translates directly to slides), end on the honest
   limits. Rehearse against the session's time slot, not a guess at it.
3. **Poster/lightning collateral** if the edition uses them — 待核实.
4. **Publicity** — once the proceedings version exists: update the arXiv record
   if one exists, the lab page, and the repo README to cite the canonical DOI,
   so the version of record accretes the citations.

## Sequence for the six-or-so weeks

```text
Week 0   Read THIS edition's camera-ready page top to bottom; identify
         publisher, template, rights form, portal, true deadline (AoE?).
Week 1   Shepherd memo (if any) + content repairs; coauthor sign-off on
         author order and affiliations.
Week 2   De-anonymization checklist; acknowledgments with grant numbers;
         artifact DOI deposited.
Week 3   Publisher template pass; rights form executed by the authorized
         author; metadata (title case, abstract, keywords) entered exactly.
Week 4   Link check + verification script above on the actual final PDF;
         upload; download back and re-verify what the portal stored.
Buffer   Publisher back-and-forth (format rejections are routine, not
         emergencies) + registration + talk drafting.
```

## Final gate before upload

- [ ] Publisher, template, and rights form identified from THIS edition's pages
- [ ] Author block, order, and affiliations signed off by every coauthor
- [ ] De-anonymization checklist fully inverted; verification script clean
- [ ] Shepherd/mandatory items all addressed with a change memo
- [ ] Artifact DOI live; badge coordination confirmed with AE chairs
- [ ] Acknowledgments carry exact grant numbers and required disclosures
- [ ] Portal's stored PDF downloaded back and re-verified
- [ ] Registration done; talk slot known; travel and visa in motion

Verified anchors (dates, sponsorship, AE arrangement, 2026 template flavor):
`../../resources/official-source-map.md`, checked 2026-07-08. The camera-ready
page contents, page allowance, rights workflow, and attendance rules for the
target edition are the controlling sources once posted.
