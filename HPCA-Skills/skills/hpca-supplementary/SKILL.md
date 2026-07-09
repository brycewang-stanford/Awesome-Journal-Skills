---
name: hpca-supplementary
description: Use when deciding where HPCA material belongs across the four destinations the venue offers — the 11-page body, the anonymized artifact mirror, the staging shelf for the rebuttal/revision window, and the post-acceptance public release — while keeping anonymity intact and every reference author-complete.
---

# HPCA Supplementary

Use this to triage material across the destinations HPCA actually provides. HPCA has
no open-ended supplementary upload culture: material lives in one of four places, and
putting it in the wrong one either wastes body pages or leaks anonymity.

## The four destinations

1. **The 11-page body.** Only what the argument needs to stand: the characterization,
   the mechanism, and the headline evidence. Everything a reviewer must read to
   believe the claim.
2. **The appendix (within the submitted PDF's allowance).** Extended methodology,
   additional sensitivity studies, proofs of any modeled bounds — material a reviewer
   *may* consult, kept out of the core argument.
3. **The anonymized artifact mirror.** Code, configs, scripts, and reduced-input
   runs, with all identity scrubbed and links anonymized, so a reviewer can inspect
   during the window.
4. **The post-acceptance public release.** The de-anonymized, badge-ready artifact on
   the AE HotCRP after acceptance, plus any licensed-workload recipes.

## Where does each thing go?

| Material | Destination | Note |
|---|---|---|
| Mechanism description, headline results | Body | The paper's core |
| Extra sensitivity sweeps, extended methodology | Appendix | Referenced from the body |
| Simulator, configs, regen scripts | Anonymized mirror | Fully scrubbed for review |
| Machine-state logs, raw output | Anonymized mirror / appendix | Provenance for silicon |
| Licensed-workload recipes + checksums | Post-acceptance release | Cannot ship the suite itself |
| De-anonymized artifact + README | Post-acceptance release | Badge round on AE HotCRP |

## Keep anonymity intact across destinations

The most dangerous leaks happen in the material *around* the paper:

- Scrub author names, institution paths, and repo owners from the mirror; anonymize
  every artifact URL in the PDF.
- Strip identifying metadata from config files, commit authorship, and notebook
  fields.
- Keep acknowledgments, funding, and any AI-use disclosure phrased so they do not
  de-anonymize (the disclosure stays anonymous until camera-ready).
- Never blind the bibliography or drop a reference's authors to save space — that is
  a reject trigger, not an anonymity fix.

## Stage for the window

Between submission and the rebuttal/revision window, keep a **staging shelf**: extra
experiments a reviewer might request, pre-run and ready to fold in. The window is
short and combined (respond *and* revise), so material assembled in advance is the
difference between answering an objection and deferring it.

## Triage pass

```text
1. Body carries only what the claim needs — move the rest to appendix/mirror
2. Appendix holds referenced extras, not orphan material
3. Mirror is fully anonymized (names, paths, URLs, metadata)
4. Licensed workloads reduced to recipes+checksums for later release
5. Staging shelf holds pre-run likely-requested experiments
6. Bibliography intact: no blinding, all authors listed
```

## Output format

```text
[Body discipline] core-only? (Y/N)
[Mirror anonymity] fully scrubbed? (Y/N)
[Destination errors] <material in the wrong place>
[Window readiness] staging shelf populated? (Y/N)
[Bibliography] intact and author-complete? (Y/N)
[Fixes] <ordered>
```

Reopen the current CFP and AE page for the submitted-PDF appendix allowance and the
release mechanics — both are per-edition.
