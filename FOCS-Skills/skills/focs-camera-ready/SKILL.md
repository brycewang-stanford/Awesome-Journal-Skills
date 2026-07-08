---
name: focs-camera-ready
description: Use when converting a FOCS (IEEE Symposium on Foundations of Computer Science) acceptance into its deliverables — the IEEE proceedings version with copyright and de-anonymization steps, the public arXiv/ECCC full version the CFP expects, the New York talk, and award-eligibility hygiene.
---

# FOCS Camera-Ready

Acceptance at FOCS creates two publication duties with different owners of
truth: a proceedings version, produced to IEEE specifications and published
via IEEE Xplore and the IEEE Computer Society Digital Library, and a public
full version with complete proofs that the CFP expects on arXiv, ECCC, or an
equivalent open host by the camera-ready deadline (2026 CFP, checked
2026-07-08; the 2026 camera-ready date and format instructions were not
public at check time — the acceptance packet is the controlling source,
待核实). This skill sequences both.

## The two deliverables

| | Proceedings version | Public full version |
|---|---|---|
| Publisher | IEEE (Xplore + CS Digital Library) | You (arXiv / ECCC) |
| Role | Citable record of the FOCS acceptance | Record of correctness — the document experts actually read |
| Length | Per acceptance packet (待核实) | Unlimited; all proofs |
| Rights | IEEE copyright/publication form (electronic; exact form 待核实) | You retain arXiv license choice |
| Deadline | Camera-ready date (待核实) | CFP expectation: same date |
| Failure cost | Paper dropped from proceedings | Community reads a proofless announcement; reputational, and real |

Treat the full version as the primary deliverable and the proceedings file as
its formatted excerpt — that ordering produces consistent documents; the
reverse ordering produces a proofless PDF and an orphaned preprint.

## De-anonymization, done completely

Reversing double-blind is more than restoring the author block:

- Author names, affiliations, emails, ORCIDs in the packet's required format
  and order (author-order changes after acceptance need chair approval).
- Acknowledgements and grant numbers restored — check funder mandates now,
  since some require specific contract-number phrasing and open-access
  handling of the accepted version.
- Self-citations rewritten out of the third person where it now reads
  absurdly ("Chen et al. [7] — the present authors — showed…" becomes "In
  earlier work [7] we showed…").
- The "full version" pointer made concrete: replace "the full version" with
  the actual arXiv/ECCC identifier on the first page.

## Consistency audit before the deadline

The one camera-ready failure that follows a theory paper forever is
divergence between the proceedings version and the full version. Run the
statement-freeze check across the two sources one last time:

```bash
# same extractor as focs-reproducibility; both sources, post-edits
./extract_statements.sh proceedings-src/ fullversion-src/
# hashes must match: no theorem statement may differ between the
# document people cite and the document people check
# then verify the cross-pointers resolve:
grep -o 'arXiv:[0-9v.]*' proceedings-src/*.tex   # correct ID, correct version
```

If reviewer comments prompted real changes (a repaired lemma, a weakened
claim), apply them to *both* documents and record them in the full version's
changelog ("v3, camera-ready: Lemma 6.2 hypothesis corrected following
committee comments"). Improvements beyond reviewer comments are safe when
they strengthen exposition; new results belong in the journal version, not
in a camera-ready that no longer matches what was refereed.

## The November talk and the awards file

- **Talk:** every accepted FOCS paper gets a program slot in New York
  (November 8–11, 2026); whether the 2026 program runs single-track or
  parallel sessions was unannounced at check time (待核实). Build the talk
  from the ten-page window's narrative — problem, obstacle, one real idea —
  not from the section structure; twenty minutes fits one idea.
- **Registration and attendance duties** for accepted papers (who must
  register, in-person requirements): 待核实 in the acceptance packet; budget
  as if required.
- **Awards:** the PC designates Best Paper and the **Machtey Award** for best
  student paper from the accepted pool — recent Machtey citations (2024: the
  Ising-perceptron capacity paper; papers with all-student author teams) show
  the profile. If your author team's student status matters, confirm the
  packet's eligibility declaration is filled accurately; misdeclared status
  is unfixable after the program is printed.

## Working with IEEE production

Expect the production pipeline of an IEEE Computer Society proceedings —
specific class files, a compliance-checking step, and an electronic
copyright form — with the 2026 specifics (template, page allowance, upload
system) defined only by the acceptance packet (待核实). Two habits that
prevent the classic failures: run the packet's compliance checks on day one
rather than deadline day, because font-embedding and figure-format errors
take iterations to clear; and keep the proceedings source a *generated
projection* of your canonical source (a documented set of cut points and
`\iffull` switches), never a hand-forked copy — hand forks are how the
proceedings version acquires the typo the full version already fixed.

## Endgame sequence

1. Acceptance week: read the packet twice; diary the camera-ready date;
   file the IEEE form early (copyright questions take days, not hours).
2. Week 1: apply reviewer-prompted fixes to the canonical source; regenerate
   both documents from it.
3. Week 2: de-anonymization pass; funder-compliance check; consistency audit
   above; co-author sign-off on the exact PDFs.
4. Submission: upload proceedings files; post/refresh the full version so
   the identifier printed in the proceedings resolves *today*, not at the
   conference.
5. Before travel: talk rehearsed against a mixed-TCS audience; slides carry
   the arXiv/ECCC ID on the final frame.
