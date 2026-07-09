---
name: icalp-camera-ready
description: Use when preparing an accepted ICALP (EATCS) paper for the LIPIcs open-access camera-ready — converting to the lipics-v2021 document class, de-anonymizing (restoring authors, affiliations, ORCIDs, acknowledgements, and funding), completing LIPIcs metadata (ACM CCS, keywords, DOI cross-references), reconciling the body with the public full version, and passing Dagstuhl production checks.
---

# ICALP Camera-Ready

Use this after acceptance. The ICALP camera-ready is a **LIPIcs** (Leibniz International Proceedings in
Informatics, Schloss Dagstuhl) production, so it has requirements a generic "final version" pass
misses: the **`lipics-v2021` document class is mandatory**, the paper must be **de-anonymized**, and
LIPIcs metadata (author ORCIDs, ACM CCS classification, keywords, funding) must be complete for the
open-access record. Confirm the exact deadline and the current LIPIcs author instructions before
starting (camera-ready date **待核实** per cycle).

## Convert to LIPIcs

- Compile in the **`lipics-v2021`** class from the official LIPIcs bundle. If you drafted in a
  different class, port early — the LIPIcs style constrains title/author blocks, theorem environments,
  and the bibliography, and last-minute conversion breaks cross-references.
- Respect the LIPIcs page policy for the proceedings version (the style targets a compact page count;
  the **full version stays on arXiv/ECCC** and is cited, not inlined).
- Do not modify the class's margins, fonts, or spacing — Dagstuhl production will bounce a tampered
  style.

## De-anonymize systematically

The submission was lightweight double-blind; the camera-ready is **not**. Restore everything you
removed:

```text
[ ] Author names, affiliations, and ORCIDs in the LIPIcs author block
[ ] Acknowledgements (advisors, discussions, anonymous-referee thanks)
[ ] Funding / grant numbers (required by many funders; LIPIcs has a funding field)
[ ] First-person self-citation restored where natural ("in our earlier work [12]")
[ ] The public full-version link (arXiv/ECCC/HAL) now openly referenced
```

Sweep for **leftover anonymization**: "[anonymized]" placeholders, blanked acknowledgements, and
"the full version" phrasing that should now name the arXiv handle.

## Complete LIPIcs metadata

LIPIcs records are richly indexed; fill every field:

- **ACM 2012 CCS** concepts (the classification LIPIcs requires) and **keywords**.
- **ORCID** for each author.
- **Category / related version** fields linking the LIPIcs paper to the arXiv/ECCC **full version**
  (LIPIcs supports an explicit "related version" for this).
- Funding statements per author.
- Correct **track** designation (A or B) if the proceedings distinguish them.

## Reconcile body and full version

- Ensure the **theorem statements and numbering** in the LIPIcs body match the public full version so
  citations to "Theorem 3" resolve the same way in both.
- If reviews prompted a fix, apply it in **both** the LIPIcs version and the arXiv full version, and
  refresh arXiv around publication.
- The proceedings version may again defer full proofs to the full version — but every claim in the
  LIPIcs paper must still be either proved or precisely referenced (`icalp-supplementary`).

## Production and logistics

- Run the **LIPIcs/Dagstuhl checklist** (metadata completeness, class compliance, PDF/A-friendly
  fonts, no overfull hboxes in the final).
- Confirm the **copyright/consent** step (LIPIcs is open access under a Creative Commons license —
  authors retain copyright; verify the current license wording).
- Arrange for **at least one author to register and present** — presentation is expected for the paper
  to appear.
- Meet the camera-ready deadline; LIPIcs volumes are produced on a fixed schedule and late files risk
  exclusion.

## Common camera-ready misses

- Leaving the paper in a non-LIPIcs class and scrambling at the deadline.
- Forgetting **ORCIDs / CCS / funding** metadata (holds up production).
- A dangling "[anonymized]" or blanked acknowledgement.
- Body and arXiv full version drifting out of sync on theorem numbering.
- Assuming the full proofs must now be inlined — the full version still carries them; the LIPIcs paper
  references it.

## Output format

```text
[Class] lipics-v2021 compiles clean? yes/no
[De-anonymized] authors/affil/ORCID/acks/funding restored? leftover [anonymized]? 
[Metadata] ACM CCS + keywords + ORCIDs + related-version (full version) complete? yes/no
[Body/full-version] theorem numbering consistent; both updated for review fixes? yes/no
[Production] LIPIcs checklist + license + presenter arranged? yes/no
[Fix queue] <ordered, with the camera-ready deadline>
```
