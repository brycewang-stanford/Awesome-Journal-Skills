---
name: icdt-camera-ready
description: Use when preparing the final LIPIcs camera-ready for an accepted ICDT (International Conference on Database Theory) paper — the lipics-v2021 final document, mandatory ACM CCS concepts and keywords, author ORCIDs, de-anonymization, complete proofs and the full-version link, CC-BY licensing, and passing the Dagstuhl/DROPS production checks that mint the DOI.
---

# ICDT Camera-Ready

Prepare the final paper for **LIPIcs** (Leibniz International Proceedings in Informatics, Schloss
Dagstuhl). Unlike an ACM/IEEE camera-ready, this is a **LaTeX-only, `lipics-v2021`, open-access,
CC-BY** deliverable that Dagstuhl's production team checks before minting a DOI on **DROPS**. Two
things drive the work: LIPIcs has strict, automatically-checked metadata requirements, and you now
**de-anonymize** and restore everything the anonymous submission removed.

## De-anonymize systematically

The submission was anonymous; the camera-ready is not. Restore, in one pass:

- Author names, affiliations, and ORCIDs in the `lipics-v2021` author macros.
- Acknowledgments — funding sources, grant numbers, colleagues — removed for review.
- First-person self-citations where natural ("in our earlier work [17]"), now that identity is
  public.
- The **full-version link** (arXiv) carrying the complete proofs.

Do a reverse sweep: confirm no leftover "[Anon]" placeholder or anonymized phrasing survives into the
published version.

## LIPIcs metadata (automatically checked)

`lipics-v2021` requires structured metadata that Dagstuhl's toolchain validates; missing or
malformed entries block production:

```latex
\author{Ada Lovelace}{Dept, University, City, Country}{ada@uni.edu}{https://orcid.org/0000-0000-0000-0000}{funding note}
\ccsdesc[500]{Theory of computation~Database theory}   % mandatory ACM CCS concept(s)
\keywords{conjunctive queries, data complexity, dichotomy}  % mandatory
\category{}          % e.g. invited/track, if applicable
\relatedversion{Full version: https://arxiv.org/abs/...}    % the complete-proofs version
\funding{...}        % restored acknowledgment of funding
```

- **ACM CCS concepts** are mandatory — pick the specific "Theory of computation~Database theory" (or
  finer) nodes, not a vague top-level one.
- **Keywords** are mandatory and are how the paper is indexed.
- **ORCIDs** are expected for each author where available.
- Fill `\relatedversion` with the arXiv full version so readers reach the complete proofs.

## Proofs and the full version

- The 15-page camera-ready keeps the same body/appendix split as the submission; ensure the appendix
  proofs are final and correct after any revision.
- Post or update the **full version** (arXiv) with all proofs and link it via `\relatedversion`. The
  LIPIcs paper and the full version must state the same theorems and bounds — a divergence between the
  published bound and the arXiv bound is a citation hazard.
- Incorporate every change promised in the revision letter; the camera-ready is the record of record.

## Licensing and production

- LIPIcs publishes under **CC-BY 4.0**; you retain copyright and grant the open-access license. Do
  not paste in figures or text you cannot license under CC-BY.
- Submit **LaTeX source** (not just a PDF) so Dagstuhl can produce the final; keep the `lipics-v2021`
  class **unmodified** — no custom `\usepackage` hacks that the production check rejects, and no
  reformatting that changes the page geometry.
- Provide the exact page count within budget; the marked appendix is part of the published paper.
- After production, the paper appears open access on **DROPS** with a **DOI**; verify author names,
  affiliations, ORCIDs, and the CCS/keywords render correctly in the DROPS entry.

## Production-check failure modes

| Failure | Cause | Fix |
|---|---|---|
| Metadata rejected | Missing CCS concept, keywords, or malformed author macro | Fill all mandatory `lipics-v2021` fields |
| Class modified | Custom margins/packages altering layout | Revert to stock `lipics-v2021`; move fixes into content |
| Non-CC-BY asset | Figure/text under an incompatible license | Replace or re-license under CC-BY |
| Full-version mismatch | arXiv states a different bound than the LIPIcs paper | Align both to the final result |
| Residual anonymization | "[Anon]"/anonymized prose left in | Restore names, acks, self-citations |

## Reverify each cycle

- The required LIPIcs class revision (`lipics-v2021` as of 2026/2027) and the current metadata
  checklist.
- The camera-ready deadline relative to notification and the event.
- Whether ORCID is mandatory or expected, and the current CC-BY version.

## Output format

```text
[De-anon] names/affiliations/ORCIDs/acks/self-cites restored? yes/no
[Metadata] CCS concepts + keywords + author macros complete? yes/no
[Full version] arXiv linked via \relatedversion and consistent with the paper? yes/no
[License] all assets CC-BY-compatible; LaTeX source submitted? yes/no
[Production] lipics-v2021 unmodified; page budget met; DROPS DOI verified? yes/no
[Fix queue] <ordered before the camera-ready deadline>
```
