---
name: sigir-camera-ready
description: Use when an accepted SIGIR paper must become the ACM Digital Library version of record — de-anonymizing the sigconf source, CCS concepts and keywords, the e-rights form, TAPS source upload and proof checking, restoring real system and dataset names, and the April camera-ready window before the July conference.
---

# SIGIR Camera Ready

SIGIR publishes through ACM: the version of record is produced by ACM's pipeline
(e-rights, then TAPS) from your **source files**, and it appears in the Digital
Library as both PDF and HTML (SIGIR 2025's volume is DOI 10.1145/3726302). The 2026
camera-ready window sat in late April for the tracks whose dates were verifiable
(April 29, 2026 for Resources / Low Resource Environments); take your own track's
date from the acceptance email, and note the July conference leaves little slack.

## What changes between the reviewed PDF and the record

| Item | Reviewed submission | Version of record |
|---|---|---|
| Document class | `sigconf` + anonymous/review options | `sigconf` with rights commands from TAPS |
| Authors | Hidden | Restored; order frozen **before** e-rights |
| System name | Possibly a review alias | Real name, consistent with the public repo |
| Dataset/log provenance | Genericized for anonymity | As precise as data agreements allow |
| Repository link | Anonymous mirror | Public, licensed, stable (archival DOI best) |
| Acknowledgments | Absent | Restored — and they cost body pages at SIGIR |
| CCS concepts + keywords | Often placeholders | Final; they drive DL search forever |
| Leaderboard references | Scrubbed | Restorable — align run IDs with the paper |

Two SIGIR-specific pressure points hide in that table:

- **Acknowledgments and restored details consume the page budget**, because SIGIR
  counts everything except references inside the limit. If the camera-ready allowance
  for your track is the same as submission (whether acceptance buys an extra page was
  not verifiable for 2026 — 待核实), something you wrote must shrink to make room.
- **The anonymity aliases must be unwound consistently.** A paper that called its
  system "ANON-RANK" in review must not leave one stale alias in a figure caption or
  a run-file name cited in a table. Grep, don't skim.

## The ACM production sequence

1. **e-rights**: the contact author receives ACM's rights form; completing it stamps
   the copyright block, so title and author list must be final first.
2. **TAPS upload**: zip your LaTeX (or Word) source per the instructions in the
   acceptance email. TAPS compiles the DL's PDF and HTML5 — HTML is where homemade
   macros, `\vspace` hacks, and missing figure files fail loudly.
3. **Proofs**: check both renderings. Tables that were hand-tuned for two-column PDF
   are the usual HTML casualties, and IR papers are table-heavy.

```bash
# Sweep before zipping for TAPS
grep -rn "ANON\|anonym" *.tex sections/          # stale review aliases
grep -rn "4open\|anonymous.4open" *.tex          # anonymous mirror still linked?
grep -rn "vspace\|renewcommand{\\\\baselinestretch}" *.tex  # spacing hacks
ls figures/ | wc -l && grep -c includegraphics *.tex        # figure inventory match
```

## Digital Library metadata that outlives the conference

- **CCS concepts**: pick from the ACM taxonomy deliberately (e.g., Information
  systems → Retrieval models and ranking / Evaluation of retrieval results). They are
  the DL's routing layer for your paper's entire life.
- **Keywords**: include the terms IR searchers actually use — task name, collection
  names, method family ("dense retrieval," "learning to rank," "conversational
  search"). Your future citers search the DL and Google Scholar with these.
- **Author name forms**: match each author's existing DL record; inconsistent forms
  split citation identities.
- **ORCID and funding**: attach ORCIDs; format grants the way the funder mandates.
- The abstract in TAPS metadata must equal the PDF abstract — the DL indexes metadata.

## Artifacts at publication time

The camera-ready is the moment review-time artifacts become public commitments:

- Flip the repository public **before** the camera-ready deadline and test it from a
  logged-out browser; the paper will cite it for decades.
- Freeze the exact run files behind every table (`runs/` with a manifest); IR
  replication requests are usually "can you send the run file," and yes should be easy.
- If the paper introduced judgments, topics, or a corpus and it was *not* routed
  through the Resources track, publish it with a license and a datasheet anyway —
  the community treats missing licenses as unusable resources.

## Worked example: absorbing review debts into the budget

An accepted full paper carries two commitments from the review phase: a promised
scope-limitation paragraph and a clarification of the tuning protocol. Camera-ready
also restores acknowledgments (~0.15 pp) and real provenance details (~0.1 pp).
With no verified extra page, the arithmetic forces trades:

1. Review commitments land first — they are quasi-contractual and reviewers of
   record may check.
2. The restored acknowledgments displace the weakest analysis sentence-by-sentence,
   not table-by-table: prose compresses, protocol does not.
3. Nothing *new* enters: results and claims not seen by reviewers do not belong in
   the version of record; they belong in the repository changelog or the next paper.

The heuristic: camera-ready pays debts and restores identity; it does not buy new
real estate.

## Registration and presentation

Author registration by the camera-ready date was confirmed for the Resources track in
2026 (April 29); whether every accepted full/short paper requires a registered,
in-person presenting author — and the fee schedule — was not verifiable at build time
(待核实). Read the acceptance email as the controlling document, and budget for
Melbourne travel early: July is conference high season in the IR calendar.

## Timeline discipline

- Week 0 (decision): settle author order; start e-rights; unwind aliases in source.
- Week 1: TAPS dry run with rights commands stubbed; fix class-file violations.
- Week 2: metadata pass (CCS, keywords, ORCID); repository public; proofs checked.
- Slack: TAPS support queues lengthen as thousands of ACM camera-readies converge —
  finishing a week early is the only reliable mitigation.

## Output format

```text
[Camera-ready status] on-track / blocked-at-rights / blocked-at-TAPS / not started
[Page budget] <pages>/<track allowance> (allowance verified from acceptance email? y/n)
[De-anonymization] aliases unwound y/n, repo public y/n, provenance restored y/n
[Metadata] CCS final / keywords final / ORCIDs attached / abstract == PDF
[Artifacts] run files frozen / license present / archival DOI minted
[Registration] requirement confirmed from acceptance email? y/n (fees 待核实)
```
