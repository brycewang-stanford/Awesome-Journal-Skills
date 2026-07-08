---
name: cscw-supplementary
description: Use when assembling supplementary materials for a CSCW submission — appendices, codebooks, interview guides, survey instruments, analysis code, and data extracts — deciding what accompanies a journal-model paper, anonymized end to end and consistent across R&R rounds.
---

# CSCW Supplementary Materials

Supplements at CSCW serve a journal-style review: they let reviewers *verify* the
methods section without bloating a paper already policed by the contribution-vs-
length standard. Because Revise and Resubmit sends the paper back to the same
reviewers, the supplement is also a **versioned record** — round-two reviewers can
and do compare it against round one.

## What goes where

| Material | Main paper | Appendix | Separate supplement file |
| --- | --- | --- | --- |
| Method summary + key instrument excerpts | ✓ | | |
| Full interview guide / survey instrument | | ✓ | ✓ if long |
| Codebook (definitions + paraphrased exemplars) | | ✓ | ✓ |
| Trace-pipeline ledger and attrition table | summary | ✓ | code as archive |
| Analysis scripts | | | ✓ (archive) |
| Additional tables/robustness checks | | ✓ | ✓ |
| Consent forms / recruitment text | | | ✓ |
| Raw transcripts, identifiable data | never | never | never |

Decision rule: **anything a reviewer needs to evaluate a claim belongs in the paper
or appendix; anything a reviewer needs to *trust* the method belongs in the
supplement; anything participants did not consent to share belongs nowhere.**

## Anonymization is deeper than the PDF

The supplement is the classic identity leak at this venue, because it aggregates
exactly the artifacts teams forget to scrub:

- **Documents:** consent forms carry institution letterhead and IRB protocol
  numbers tied to a university; recruitment emails carry names. Redact, and check
  PDF/Office metadata (author fields, tracked changes, comments).
- **Code archives:** repository paths (`/home/username/`), git history, package
  lockfiles with private registry URLs, notebook execution metadata. Export clean
  archives, never a cloned `.git`.
- **Data extracts:** usernames, community names, timestamps precise enough to
  reverse-search, URL slugs. For small communities, the *combination* of quoted
  text and date can identify the community even with names removed.
- **Media:** screenshots showing account handles, browser profiles, or platform
  locale details.

Mechanical sweep before upload:

```bash
# strings that must not appear anywhere in the supplement tree
grep -ri -l -E "(surname|firstname|university-name|lab-name|grant-no|protocol-no)" supplement/
# metadata in every PDF
for f in supplement/**/*.pdf; do exiftool "$f" | grep -iE "author|creator|company"; done
# accidental git history or user paths in code archives
find supplement/ -name ".git" -o -path "*Users*" -o -path "*home*" | head
```

Adapt the string list per project; run it on the *packed* archive, since packing
often reintroduces metadata.

## R&R versioning discipline

- Keep every round's supplement frozen; name uploads by round
  (`supplement-r2.zip`), never overwrite.
- If the response letter cites the supplement ("the revised codebook now includes
  ..."), the cited file must exist under that name — reviewers check.
- New supplementary material added at R&R must be flagged in the change summary;
  silently appearing files read as scope creep or, worse, as identity leaks made
  under revision pressure.

## Pre-upload checklist

```text
[Inventory]   every supplement file listed in the paper or response letter? y/n
[Consent]     each artifact within participants' consent scope? y/n
[Sweep]       mechanical anonymity sweep run on the packed archive? y/n
[Size/format] platform limits confirmed on the live submission system? 待核实 per
              regime (PCS legacy vs Manuscript Central) — do not assume
[Round label] files named by round; prior rounds preserved? y/n
```

Platform-specific size and format caps were not verifiable at 2026-07-08; check the
live Manuscript Central instructions for the rolling pathway before packaging.
