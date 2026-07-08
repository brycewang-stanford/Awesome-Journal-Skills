---
name: stoc-camera-ready
description: Use when converting a STOC (ACM Symposium on Theory of Computing) acceptance into publishable form — the ACM proceedings version, de-anonymization, rights forms, the CFP-level expectation that the full paper with proofs goes public on arXiv or ECCC by the camera-ready deadline, and TheoryFest talk preparation.
---

# STOC Camera-Ready

Anchor cycle: STOC 2026 required camera-ready copies by **March 31, 2026 (AoE)**
for the conference in Salt Lake City, June 22–26, 2026, with proceedings in the
ACM Digital Library (58th proceedings: `dl.acm.org/doi/proceedings/10.1145/3798129`;
checked 2026-07-08). Two deliverables leave your hands in this phase, and they are
not the same document.

## Deliverable A: the proceedings version

- Reformat from the loose 11-point submission format into the ACM proceedings
  template the acceptance email specifies; exact class file, page allowance, and
  the production vendor's upload flow are per-cycle instructions (待核实 from the
  acceptance packet, not from this file).
- De-anonymize deliberately: author block with canonical name spellings and ORCID,
  restored acknowledgements and grant numbers, self-citations back in first person
  where that reads naturally.
- Complete the ACM rights form before final upload; the copyright block the form
  generates must be pasted into the paper, and the title/author list in the form
  must match the PDF character for character.
- Expect the proceedings version to remain an **extended abstract**: theorem
  statements, overview, and selected proofs. It is the citable record, not the
  complete mathematical record.

## Deliverable B: the public full version

The STOC 2026 CFP stated the expectation that authors of accepted papers make
their **full papers, with proofs, publicly available on arXiv, ECCC, or a similar
preprint service by the camera-ready deadline**. Treat this as a hard milestone
with its own checklist:

- The full version must contain every proof the extended abstract defers, under
  the same theorem numbering or with an explicit correspondence table.
- Title should match the proceedings title (a "(full version)" annotation is
  fine); the abstract page should cite the proceedings version once the DOI
  exists.
- ECCC suits complexity papers seeking community review; arXiv `cs.DS`/`cs.CC`
  etc. is the default. Cross-listing is common and harmless.

```bash
# Package the full version for arXiv from a clean checkout
latexmk -pdf full-version.tex                 # confirm it compiles cold
tar czf stoc-full.tar.gz full-version.tex \
    macros.tex refs.bib sections/ figures/    # sources, not the PDF
# then on arXiv: submit, check the auto-compiled PDF page by page,
# and verify theorem numbering against the proceedings version.
```

## Keeping the two versions coherent

| Check | Proceedings version | Full version |
|---|---|---|
| Theorem statements | Must match full version verbatim | Master copy |
| Proofs | Sketches + pointers allowed | Complete, no deferred steps |
| Bug found after acceptance | Fix if production window allows; else note | Fix and replace; arXiv versions are revisable |
| Long-term citations | DOI of record | Where the community actually reads the math |
| Numbering | May compress; include mapping if so | Canonical |

The failure mode this table exists to prevent: a proceedings version whose
Theorem 3 is the full version's Theorem 5, silently — every later citation and
every reader cross-checking proofs pays for it.

## Conference obligations

- STOC 2026 ran inside a five/six-day **TheoryFest** program (talks, workshops,
  posters, invited events; the extra Saturday hosted a "Can AI do Theory?"
  workshop). Expect a short talk slot; theory talks succeed on one theorem, one
  proof idea, one picture — rehearse to the slot length announced with the
  program.
- Registration and physical-presentation requirements for accepted papers were
  not verifiable from the CFP excerpts at check time: 待核实 in the acceptance
  email before booking decisions.
- Award eligibility is automatic: the PC may designate up to four **STOC Best
  Papers**, and the **Danny Lewin Best Student Paper Award** applies when all
  authors were full-time students at submission (`sigact.org/prizes`).

## Sequence from acceptance email to conference

1. Read the acceptance packet the same day; extract the production vendor's
   instructions, the exact template, and every form deadline into a checklist.
2. Triage the corrections file (`stoc-workflow`): reviewer-caught issues and
   post-submission bug fixes go into both versions now, cosmetic improvements
   into the full version only.
3. Rebuild the paper in the ACM template early — two-column ACM format holds
   far less than the loose submission format, and the compression decisions
   (which proofs stay in the proceedings version) take real editorial time.
4. Freeze theorem numbering across both documents before either is finalized.
5. Submit the ACM rights form, paste the generated block, upload, and then
   post the full version — in that order, so the arXiv abstract can cite the
   final title.
6. Book the talk rehearsal after the program schedule lands.

## Post-publication hygiene

- Update the arXiv/ECCC record with the DOI once the ACM DL entry is live.
- If a journal version follows (JACM, SICOMP, TheoretiCS and TALG are the usual
  homes), note that SIGACT's prior-publication policy runs one way: the journal
  version extending a STOC extended abstract is standard practice, expected by
  editors, and should say "a preliminary version appeared in STOC 2026."
- Archive the exact submitted, accepted, and camera-ready sources; Test of Time
  and prize committees read the proceedings version decades later.

## Failure modes seen at this stage

- The proceedings version compiled from stale submitted sources while all
  fixes went to the full version — the published record now carries known
  bugs (`stoc-reproducibility`'s drift vignette, realized in production).
- Rights-form metadata typed from memory, so the DL entry spells an author
  differently from every other paper they have written.
- The arXiv posting deferred "until after the conference," quietly breaking
  the CFP's camera-ready expectation and leaving five months where the
  community cites a proofless extended abstract.
- A talk built as a proof walkthrough; twenty minutes of lemma dependencies
  loses even the specialists. One theorem, one idea, one picture.

## Output format

```text
[Camera-ready state] not started / ACM version in progress / full version live / both done
[Version-coherence check] <numbering, statements, proof coverage>
[Rights/forms] <ACM form status, copyright block pasted?>
[Full-version location] arXiv/ECCC id or 待核实
[Talk prep] <slot length, one-theorem story chosen?>
```
