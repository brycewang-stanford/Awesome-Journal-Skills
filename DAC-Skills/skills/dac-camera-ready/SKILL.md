---
name: dac-camera-ready
description: Use when preparing the final ACM/IEEE Design Automation Conference (DAC) Research-Manuscript camera-ready after acceptance, covering de-anonymization, restoring author/affiliation/acknowledgement/funding blocks, the ACM copyright form and rights stamp, the April proceedings deadline, ACM Digital Library metadata and archival-flow checks, and the still-fixed 6+1 page budget.
---

# DAC Camera-Ready

Use this after an accept decision to produce the archival version. The DAC camera-ready is an
**ACM Digital Library** deliverable: ACM is the 2026 copyright holder, and the final manuscript plus
copyright form are due at the April proceedings deadline (DAC 2026: ~14 April 2026, after the
~9 March notification). The camera-ready is a controlled edit of the accepted paper, not a rewrite —
scope, claims, and QoR numbers are fixed by what was reviewed.

## De-anonymize systematically

The review version was double-blind; the camera-ready restores identity. Do it as a checklist so
nothing is missed and nothing new leaks in:

- **Author block** — full author list, affiliations, and contact, in the order and form you want
  cited for years.
- **Self-citations** — convert third-person references to your own prior work back to first person
  where natural ("in our earlier work [7]"), now that identity is public.
- **Acknowledgements and funding** — restore the acknowledgements and **grant numbers** you stripped
  for review; funders often require exact wording.
- **Tool/repository names** — restore the real tool name and any public artifact/OpenROAD-flow link
  you anonymized.

## ACM copyright and rights stamp

- Complete the **ACM copyright/e-rights form** when it arrives; it returns the **rights text and DOI
  stamp** that must appear on the first page.
- Insert the rights block exactly as ACM specifies using the current ACM template; a missing or
  wrong rights stamp is a common production bounce.
- Confirm the **conference/proceedings string** and volume ACM assigns for the 63rd DAC so the
  citation and DOI resolve correctly on ACM DL.

## The page budget still binds

- The final version keeps the **6-page body + 1 references-only page** budget; de-anonymization adds
  the author block and acknowledgements, which can push the body over — reclaim space editorially,
  do **not** shrink fonts or alter the template.
- The seventh page remains **references only**; acknowledgements belong in the body, not on the
  reference page.
- Re-check every figure is legible at final column width after any reflow.

## ACM DL metadata and archival flow

- **Title and author metadata** must match the PDF exactly — mismatches break indexing and citation.
- Supply **ACM CCS concepts** and **keywords** if the template/portal requests them; they drive
  discoverability in the ACM DL.
- Verify **references resolve** (DOIs where available) — the archival version is what the field will
  cite.
- If your paper is a Best-Paper candidate or in a special session, confirm any additional
  presentation or final-version requirements the track adds.

## Production checklist

```text
[De-anon]     authors/affiliations/acks/funding restored; tool + artifact links de-anonymized
[Rights]      ACM copyright form submitted; rights text + DOI stamp on page 1
[Template]    current ACM double-column; 6+1 budget still met after reflow
[Figures]     legible at final size; grayscale/color-blind safe
[Metadata]    title/authors match PDF; CCS + keywords supplied; references resolve
[Fonts]       all fonts embedded; PDF passes the portal's readability check
[Deadline]    final manuscript + copyright by the April proceedings cutoff
```

## Reverify each cycle

- The exact proceedings/copyright deadline and which ACM template revision is required.
- Whether DAC 2026 also deposits to **IEEE Xplore** (**待核实**) in addition to ACM DL, which can
  add a second rights/metadata step.
- Any AI-authorship/disclosure statement required on the final version.

## Output format

```text
[Camera-ready status] ready / blocked
[De-anonymization]    authors/acks/funding/tool links restored? yes/no
[Rights]              ACM copyright form + first-page stamp done? yes/no
[Budget]              6-page body + references-only page still met? yes/no
[Metadata]            ACM DL title/authors/CCS/keywords/DOIs correct? yes/no
[Fix queue]           <ordered items before the April proceedings deadline>
```
