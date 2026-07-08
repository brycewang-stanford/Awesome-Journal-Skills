---
name: naacl-camera-ready
description: Use when converting a paper accepted to NAACL Main or Findings into its final ACL Anthology version — merging promised revisions, restoring identity and community acknowledgements, applying the extra-page allowance, fixing Anthology metadata, and planning presentation logistics for an Americas host city.
---

# NAACL Camera Ready

Acceptance at NAACL produces a permanent object: an open-access paper in the
ACL Anthology under the chapter's proceedings (or under Findings of NAACL).
The camera-ready phase is where the anonymous ARR artifact, the promises made
in your author response, and your public identity get merged into that
object. Historical anchor: NAACL 2025 set a single final-version deadline of
February 8, 2025 covering both Main and Findings; always reconfirm the
current edition's date and instructions.

## The three-source merge

Reconstruct the final paper from three inputs, in this order:

1. **The reviewed PDF** — the text the committee actually accepted.
2. **The promise ledger** — every "we will clarify/add/rescope at
   camera-ready" sentence from your response and the meta-review's requests.
3. **De-anonymization** — author block, acknowledgements, funding, real
   artifact URLs, and first-person self-citation where it reads better.

Work from a diff against the reviewed version. Silent substantive additions
that reviewers never saw are the classic camera-ready foul; the extra page
exists to honor the ledger, not to smuggle in a new experiment.

*ACL convention grants accepted papers one additional content page (long
papers to 9, short to 5) precisely for integrating reviewer-driven changes —
confirm the current edition's instructions rather than assuming.

## De-anonymization with an Americas accent

NAACL papers frequently owe debts that anonymization suppressed: language
consultants, speaker communities, data-sharing agreements with institutions
in Latin America, translation help. Restoring these is not decoration —
data-use agreements often *require* named credit, and omitting it can breach
the terms under which a corpus was shared. Sweep for:

- consultant and community acknowledgements tied to specific datasets;
- grant and agency numbers (including non-U.S. funders) in required formats;
- artifact links flipped from anonymized mirrors to the permanent, licensed
  repository — then click every one from a logged-out session.

## Metadata: the part search engines keep forever

| Field | Checked against | Frequent failure |
|---|---|---|
| Title in submission form | Title in the PDF | Casing drift; math or diacritics mangled |
| Author names | Each author's preferred spelling | Accents stripped (García → Garcia) — especially painful at this venue |
| Author order | The accepted submission | Unagreed reordering at the deadline |
| Abstract | Final PDF abstract | Old-cycle abstract pasted in |
| PDF text layer | Copy-paste of the title and quotes | Ligature/encoding damage from a bad toolchain |

The Anthology renders names with full Unicode; the fix for a stripped accent
takes one minute now and a correction request months later.

## Findings-specific handling

A Findings acceptance publishes identically (Anthology, open access, citable)
but presentation rights differ by edition — some years offer poster slots or
workshop presentation matching. Do not guess: read the decision letter,
answer the presentation-preference form, and update the paper's own footer or
citation guidance to say "Findings of NAACL" so downstream citations land in
the right volume.

## Logistics checklist for the host city

```text
[ ] Registration completed under the presenting author's name
[ ] Visa/ESTA lead time checked for the host country (US, Mexico,
    or elsewhere in the Americas — requirements differ sharply
    by author nationality; start immediately at acceptance)
[ ] Presentation format confirmed: oral / poster / Findings slot
[ ] Travel grants: chapter and conference D&I programs have
    deadlines separate from camera-ready — check both
[ ] Artifact repository public before the talk, not after
```

## Final-week failure catalog

Recurring self-inflicted wounds in the last days before the final-version
deadline, in descending frequency:

- The promise ledger applied from memory instead of from the actual
  response text — reviewers notice the one promised clarification that
  never landed.
- A de-anonymization pass that restores authors but forgets the anonymized
  repository placeholder, shipping `anonymous.4open.science` into the
  permanent record.
- The extra content page treated as license for a new subsection of
  results nobody reviewed.
- Acknowledgements added without checking the data agreement's required
  attribution wording — close is not compliant for partnership credits.
- Rebuilding with the final style switch and never re-reading page breaks,
  so a table straddles the new author block.
- Uploading a PDF whose embedded title metadata still says "Anonymous ACL
  submission."

Each of these is a two-minute check now and a proceedings-correction
request later; the Anthology does process errata, but a corrected PDF
never fully overwrites the copies already downloaded.

## Ordered final pass

1. Apply the promise ledger; diff against the reviewed PDF.
2. Restore identity, acknowledgements, and live artifact links.
3. Verify metadata fields and Unicode rendering one by one.
4. Rebuild with the final-version style switch; recheck page budget.
5. Upload early; keep the confirmation email and the exact final PDF.

## Output format

```text
[Merge status] <ledger items applied / deferred / dropped-with-reason>
[Identity restore] <authors, acks, funding, links — done/pending>
[Metadata audit] <field -> ok/fixed>
[Findings handling] n/a / presentation plan
[Logistics] <registration, visa, travel-grant deadlines>
```
