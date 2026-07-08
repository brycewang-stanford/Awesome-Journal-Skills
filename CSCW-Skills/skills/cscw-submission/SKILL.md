---
name: cscw-submission
description: Use when readying a CSCW manuscript for upload — confirming the current pathway (rolling via Manuscript Central as of mid-2026), the single-column ACM template, the word-length scrutiny band, anonymization of author and community identifiers, ethics statements, and desk-risk triage.
---

# CSCW Submission

A CSCW submission enters a journal pipeline, and as of the 2026-07-08 check the
pipeline itself is in transition: the **May 14, 2025 PCS deadline was the last fixed
cutoff**, and papers for CSCW 2027 and beyond flow through the rolling pathway on
**Manuscript Central (mc.manuscriptcentral.com/pacmhci)** with no deadline at all.
The first audit item is therefore not the paper — it is the pathway.

## Pathway confirmation (do this first)

- Open https://cscw.acm.org/rolling.html and confirm the live submission venue,
  account requirements, and any transitional instructions.
- If the manuscript is a *revision* from the final fixed cycle, it stays in the
  system and decision vocabulary of that cycle — do not migrate it yourself.
- Record what you verified and when; this venue's lore goes stale in months, and
  colleagues will hand you confident PCS-era instructions that no longer apply.

## Manuscript checks

- **Template:** single-column ACM submission template, per the 2026-cycle CFP.
  Confirm the rolling pathway names the same template before reformatting anything.
- **Length:** no formal cap, but compute the word count (excluding references and
  appendices). Under ~5,000 or over ~12,000 words invites added scrutiny, and
  length disproportionate to contribution is itself a desk-rejection ground — the
  venue's most distinctive gate. Prepare the one-sentence length defense.
- **Ethics visibility:** IRB/ethics status, consent posture per data source, and
  sensitive-data handling stated in the methods section, not implied.
- **Internal completeness:** the paper must stand without the supplement
  (`cscw-supplementary` packages the rest).

## Anonymization: two layers, not one

CSCW review is anonymous, and this venue has a second layer most conferences lack.

**Layer 1 — authors:** names, affiliations, institution and city references, and
identifying grant information removed; self-citations in third person; metadata
scrubbed from PDF and supplement files; acknowledgements withheld until acceptance.

**Layer 2 — the studied setting:** when the paper studies a specific team,
organization, or online community, details that identify *the setting* can also
identify *the authors* (a lab's known field site, a company only insiders could
study, a community the authors visibly moderate). Audit for:

- Named partner organizations or communities whose association with the author
  team is public.
- Screenshots, quoted posts, or platform slugs that reverse-search to a community
  linked to the authors' prior publications.
- Deployment details ("our university's makerspace") that geolocate the team.

Where masking the setting would gut the contribution, mask asymmetrically: keep
analytic detail, coarsen ownership detail.

## Desk-risk triage

| Risk | Mechanism | Standing |
| --- | --- | --- |
| Length incommensurate with contribution | Editor/chairs screening | Explicit desk-reject ground in the 2026-cycle CFP |
| Author identity visible | Anonymity policy | Removal or rejection |
| Setting-based deanonymization | Same policy, subtler leak | Reviewer-reported; damages trust for R&R |
| Wrong-pathway upload | Platform transition confusion | Delay measured in weeks — expensive with no deadline pressure to excuse it |
| Missing ethics account | Reviewer expectation, journal norms | Rarely desk-level, reliably decision-level |
| Concurrent submission elsewhere | Standard ACM/journal policy | Verify current wording on the live CFP before certifying |

## Final pre-upload sequence

```text
1. Pathway verified on cscw.acm.org (date recorded): platform = ______
2. Word count: ______ (defense sentence written if outside 5,000-12,000)
3. Layer-1 anonymity sweep: text, references, PDF metadata, supplement — pass
4. Layer-2 setting sweep: partner names, screenshots, reverse-searchable
   quotes — pass
5. Ethics statement present and specific — pass
6. Supplement inventory matches in-text references (cscw-supplementary) — pass
7. Metadata fields on the platform (title, abstract, authors held privately by
   the system, conflicts) match the PDF exactly
8. Confirmation email/receipt archived with a timestamp
```

Everything above dated 2026-07-08 describes a venue mid-migration. Before any real
upload, re-verify the pathway, template, and policy wording on the live pages —
this skill's job is to tell you *what to verify*, not to spare you the verifying.
