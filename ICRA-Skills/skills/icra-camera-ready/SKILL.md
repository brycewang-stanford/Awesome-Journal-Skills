---
name: icra-camera-ready
description: Use when converting an accepted ICRA paper into its final form — the 8-page total limit including references, de-anonymization after double-anonymous review, PaperPlaza final upload and PDF compliance, IEEE electronic copyright transfer, final video, author registration requirements, and IEEE Xplore publication.
---

# ICRA Camera-Ready

Acceptance email to Xplore entry is a five-week administrative gauntlet (2026
cycle: notification Jan 31, final upload Mar 6). Errors here are permanent —
the camera-ready is what IEEE Xplore archives forever — and some steps
(copyright, registration) can block publication outright. Work the checklist,
not vibes; and reverify every number on the current year's final-submission
instructions page.

## The page-geometry surprise

The 2026 final limit was **8 pages total, including references and everything
else** — a different shape from the submission's 6-content + 2-reference split.
Consequences:

- A submission using its full 6+2 arrives at camera-ready already at the
  ceiling; every reviewer-requested addition must displace something.
- Long bibliographies now compete with content — prune duplicate ICRA/RA-L
  citations (`icra-related-work`) before cutting analysis.
- No overlength purchase was offered in the 2026 ICRA instructions; do not
  assume the RA-L extra-page fee model (USD 175/page there) applies to the
  conference — different rules, verify each.

## Submission vs final: what changes shape

| Dimension | At submission (2026) | At camera-ready (2026) |
|---|---|---|
| Page rule | 6 content + 2 reference-only | 8 total, references included |
| Authors | stripped from PDF (double-anonymous) | restored, must match metadata |
| Acknowledgements | removed | restored with grant numbers |
| Artifact links | anonymized or omitted | permanent public URLs |
| Video | anonymized footage, review windows | de-anonymized, final upload |
| Legal state | none | eCF copyright transfer required |
| Registration | not required | required and linked to paper |

## De-anonymization pass

Reversing the double-anonymous preparation is itself error-prone:

1. Restore the author block exactly matching PaperPlaza metadata — names,
   order, affiliations; the proceedings index is built from metadata, and a
   PDF/metadata mismatch propagates to Xplore.
2. Restore acknowledgements: grants, fellowships, equipment donors — funding
   agencies audit for these lines.
3. Reverse the anonymity grammar: "the platform of [7]" may become "our
   previously developed platform [7]" where it aids clarity.
4. De-anonymize artifact links to their permanent public homes
   (`icra-artifact-evaluation` staging pays off here).
5. Check ORCID/author spelling against IEEE Xplore's existing records to avoid
   splitting your publication profile.

## PaperPlaza final upload and compliance

- The final PDF goes through PaperPlaza's compliance check (embedded fonts,
  page size, page count). IEEE-sponsored conferences commonly require an
  IEEE-compatible PDF (PDF eXpress or equivalent validation) — follow whichever
  path the year's instructions specify.
- Rebuild from the untouched IEEE template; a class file hacked in September
  to squeeze a line will fail compliance in March.
- Verify the title and abstract fields in PaperPlaza match the PDF verbatim —
  these fields, not the PDF, feed the program booklet and Xplore metadata.

## IEEE copyright transfer

Publication requires completing the IEEE electronic copyright form (eCF),
typically launched from within PaperPlaza by the submitting author:

- The signer must be authorized — employer-owned work (many industry labs,
  government employees) has special eCF paths; find out *before* deadline day
  whose signature is legally valid.
- IEEE's posted policies govern what authors may self-archive (accepted-version
  posting, institutional repositories, arXiv updates); read the current policy
  rather than folklore before updating the preprint with the final PDF.
- No copyright form, no proceedings — this is a hard blocker, unlike most
  camera-ready sloppiness.

## Registration and presentation obligations

IEEE RAS conferences tie publication to registration and presentation:

- Expect a requirement that at least one author register (typically at the
  full/member rate, not student rate) per paper by a stated deadline, and
  present at the conference; papers not presented risk exclusion from Xplore
  ("no-show" policies). The exact 2027 wording and fees were unpublished at
  check time — treat as 待核实 and verify on the year-site.
- Budget realities: Seoul 2027 (COEX, May 24-28) means flights, visas, and
  ~10,000-attendee-scale hotel demand; registration opens around early
  February 2027 per the conference site.

## Final video and multimedia

The accepted paper's video attachment can usually be refreshed at final
submission — de-anonymized (lab names allowed back), with the paper's final
title card. Keep the evidence discipline from `icra-supplementary`; the video
ships to Xplore alongside the paper and outlives the conference week.

## Five-week schedule

```text
Week 1  triage reviewer comments (icra-author-response ledger);
        freeze the addition list against the 8-page total budget
Week 2  execute text changes; de-anonymization pass; restore acks
Week 3  rebuild PDF on clean template; PaperPlaza/PDF-compliance dry run;
        start eCF signature chain (industry co-authors take longest)
Week 4  final video re-edit + de-anonymize; artifact links flipped public;
        one author registered; metadata/PDF verbatim check
Week 5  upload final PDF + video; complete eCF; archive confirmations;
        update arXiv per IEEE posting policy
```

## Terminal checklist

1. 8-page total limit met; no compliance warnings.
2. Author block ≡ PaperPlaza metadata ≡ intended Xplore record.
3. Acknowledgements and grant numbers restored.
4. eCF completed by an authorized signer.
5. Registration made and linked to the paper number.
6. Video final, de-anonymized, within spec, uploaded.
7. Public artifact URL live and printed in the paper.
8. Confirmations archived; preprint updated within policy.

## Output format

```text
[Camera-ready status] on-track / blocked: <item>
[Page budget] <n>/8 total — displaced content: <what>
[De-anonymization] authors/acks/links restored: y/n each
[Compliance] PaperPlaza check + IEEE PDF validation: pass/pending
[Legal] eCF signer identified/signed: <status>
[Registration] paid + linked: <status>
[Days to deadline] <n> vs plan week <n>
```
