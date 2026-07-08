---
name: nsdi-supplementary
description: Use when splitting NSDI material across the 12-page body, the appendix pages the CFP allows beyond references, HotCRP auxiliary-material uploads for critical online content, and the one-shot-revision packet — deciding what reviewers must see in-body versus what merely supports it.
---

# NSDI Supplementary Material

NSDI gives authors four containers with different review status. Misfiling content —
a load-bearing baseline in an appendix, revision evidence missing from the auxiliary
packet — costs more than any phrasing error. Rules below are the NSDI '27 CFP as
rendered on 2026-07-08.

## The four containers

| Container | '27 rule | Review status |
|---|---|---|
| Body | 12 pages incl. footnotes, figures, tables | The paper; judged in full |
| References | extra pages, no stated cap | Checked, uncounted |
| Appendices | extra pages after references permitted | Available context; assume optional reading (obligation 待核实) |
| Auxiliary material (HotCRP form) | for online content critical to the paper; alternative is contacting the co-chairs | Consulted at reviewer discretion; mandatory vehicle for revision packets |

Two contrasts worth internalizing. Against sibling venues that ban submission-time
appendices outright, NSDI *permits* them — the trap here is overuse, not existence.
And the auxiliary-material slot is not a junk drawer: the CFP frames it for content
**critical** to the paper that lives online, plus the structured revision documents
below.

## The placement rule

Ask of every artifact of content: *would a reviewer who skipped this be unable to
judge a claim?*

- **Yes → body.** Key workload description, baseline identity and tuning, the
  mechanism a headline number depends on, the failure regimes. If it does not fit,
  the paper is over-claiming for its budget — cut claims, not their evidence
  (`nsdi-writing-style`).
- **Supports but does not carry → appendix.** Full parameter tables, additional
  workload results consistent with in-body trends, protocol message formats,
  extended proofs of secondary properties.
- **Lives online and matters → auxiliary material,** anonymized. A demo, a dataset
  sample, an interactive visualization. Never a raw GitHub link in the text — repo
  URLs identify authors (`nsdi-submission`).

Self-containment is a hard constraint in both directions: the 12 pages must stand
alone if every appendix page is ignored, and no appendix may quietly introduce a new
claim the body never made.

## Appendix design, when used

- Order appendices by likely reviewer interest; a skeptical reviewer goes to the
  appendix to check one specific thing, not to read linearly.
- Give each appendix a one-line pointer from the body ("full per-workload results:
  App. B") so their existence is discoverable inside the reviewed pages.
- Regenerate appendix tables from the same run ledger as body figures
  (`nsdi-reproducibility`); internal contradictions between body and appendix are a
  reviewer's fastest route to distrust.
- Anonymize appendices to the same standard as the body — leaks hide in config
  listings, hostnames, and dataset paths.

## The one-shot revision packet

NSDI's most distinctive supplementary requirement. A resubmitted one-shot revision
**must** include auxiliary material containing:

1. a version of the paper **highlighting all changes made**, and
2. a **high-level explanation of the major changes**.

Build both as living documents during the revision, not as a deadline-night diff:

```bash
# Maintain the highlighted version continuously with latexdiff
latexdiff submitted/main.tex revised/main.tex > diff/main-diff.tex
pdflatex -output-directory diff diff/main-diff.tex
# Change memo skeleton: one block per required issue
#   R2.3 (baseline tuning): re-ran §6.2 with vendor-recommended config;
#   deltas now 2.1-2.9x (was 2.1-3.4x); text + Fig 7 updated. [diff pp. 8-9]
```

The same reviewers re-read the packet against their issue list; a memo that maps
issue → change → diff location does their verification for them. A revision whose
packet obscures what changed — or that ignores a required issue — is rejected with no
further revision option (`nsdi-author-response`).

## Triage drill for an overfull draft

When the draft runs to 13.5 pages, resist moving the overflow wholesale to an
appendix — demote by evidence role:

1. List every figure/table with the claim it supports; anything supporting no
   in-body claim leaves the paper entirely.
2. Secondary workloads whose trend matches the primary: one summarizing sentence in
   the body + full table in the appendix.
3. Mechanism details needed to *reimplement* but not to *judge* (message formats,
   tuning constants): appendix.
4. Anything a skeptical reviewer needs to *believe* a number: stays in-body, and a
   claim gets cut instead if space still lacks.

## Pre-upload sweep

- [ ] Body stands alone with all appendices deleted.
- [ ] No load-bearing evidence outside the 12 pages.
- [ ] Every appendix pointed to from the body; no orphan claims.
- [ ] Auxiliary uploads anonymized (metadata, paths, owners) and actually critical.
- [ ] Revision packets: highlighted PDF + change memo present, issue-complete.
- [ ] Combined upload sizes within whatever HotCRP enforces this cycle (check the
      form; caps 待核实).

## Cross-container consistency

The containers are read at different times by different people — reviewers now,
revision reviewers months later, artifact evaluators after acceptance — so
consistency is a supply-chain property: numbers quoted in the body match the
appendix tables they summarize; the auxiliary demo shows the same system version
the paper measures; and the revision packet's diff derives from the exact PDF the
reviewers previously read, not an intermediate draft.

## Output format

```text
[Placement audit] item -> body / references / appendix / auxiliary (+ moves needed)
[Self-containment] body survives appendix deletion? orphan claims?
[Appendix hygiene] pointers present / regenerated from ledger / anonymized
[Revision packet] highlighted PDF ok? memo maps all required issues?
[Blocking issues] <ordered before upload>
```
