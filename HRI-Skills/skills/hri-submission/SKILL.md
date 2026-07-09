---
name: hri-submission
description: Use when auditing an ACM/IEEE HRI full-paper submission for PCS readiness — the mandatory abstract-then-paper two-step deadline, choosing the correct one of the five tracks, the 8-page acmart anonymous format, the double-blind sweep across PDF and video, the human-participants ethics acknowledgment, and desk-reject triage before the AoE cutoff.
---

# HRI Submission

Run this audit before uploading to **PCS** (Precision Conference Solutions), HRI's submission
portal. HRI full papers are highly selective, double-blind, and reviewed by a track-specific
subcommittee, so the submission mechanics — track choice, the two-step deadline, anonymization
across the PDF *and the video* — decide whether the paper is even reviewed. Every number below was
read from the HRI 2026 full-papers call on 2026-07-09 (see `resources/official-source-map.md`);
treat it as a one-cycle snapshot and reopen the live call first.

## The two-step deadline

HRI separates **abstract registration** from **paper submission**, and both are AoE:

- **Abstract deadline (HRI 2026: 22 September 2025)** — required for *every* full paper, about a week
  early. It locks title, authors, and the **track**, and drives reviewer/AC assignment. Miss it and
  the system will not accept the PDF later.
- **Paper deadline (HRI 2026: 30 September 2025)** — upload the anonymized PDF, supplement, and video.

Register the *real* title and abstract and the *right* track — the abstract and track drive who
reviews you, and a mismatch weakens your subcommittee fit before anyone reads the paper.

## Choose the correct track

Full papers enter **exactly one** of five tracks, each a distinct contribution type reviewed by its
own subcommittee: **User Studies · Technical · Design · Theory and Methods · Systems** (User Studies
is typically largest and may be split). Pick by your **primary contribution**, not your topic;
reproducibility studies go to **User Studies**. A design paper judged as a user study (or vice
versa) is marked down for a study it never claimed. See `hri-topic-selection` for the routing.

## Format and page budget

- **ACM Primary Article Template (`acmart`)** in **anonymous review** mode. The exact class options
  and template revision for the current cycle are **待核实** — a secondary rendering also referenced
  "IEEE Proceedings specifications," consistent with the ACM/IEEE dual sponsorship; confirm the
  current author kit before compiling.
- **Page budget: up to 8 pages**, including figures, **excluding references**. Over-length
  (excluding references) is a stated desk-reject ground.
- Margins, fonts, and spacing are fixed by the template; recover space by **editorial compression**,
  not template tampering (a formatting alteration is itself a desk-reject risk).

## Double-blind sweep (PDF *and* video)

HRI review is **double-blind**, and every aspect of the submission must be anonymized —
**including the video and data**, the leak surface authors most often forget:

```bash
# PDF metadata and identity leaks
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'our (lab|group|university)|@[a-z0-9.]*\.edu|acknowledg|grant #' | head
# Supplement / artifact archive
unzip -l supplement.zip | grep -Ei '/home/|/Users/|\.git/|\.DS_Store' | head
# Video: check container metadata for author/tool/location tags
ffprobe -hide_banner video.mp4 2>&1 | grep -Ei 'title|author|comment|location' | head
```

HRI-specific leaks to hunt manually: **faces and voices** in the video, **lab logos** or a
recognizable **robot/lab space** on screen, an **institution name** in an IRB statement, a
first-person self-citation, a personal-domain data link, and named acknowledgments/grants. Blur or
mute the video and use an anonymizing archive view *before* upload (see `hri-supplementary`,
`hri-reproducibility`).

## Human-participants acknowledgment

By submitting you accept ACM's **Policy on Research Involving Human Participants and Subjects**:

- State **IRB/ethics approval** (anonymized) or a documented exemption; report **informed consent**;
  justify and debrief any **deception** (common with Wizard-of-Oz or staged failures).
- A study with participants but no ethics statement is a scored weakness and a policy exposure (see
  `hri-experiments`).

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 8 pages (excl. refs) | Desk-reject-grade | Cut or move to supplement; references do not absorb body text |
| Template altered (margins/font) | Desk-reject risk | Recompile clean `acmart`, recover space editorially |
| Identity leak in PDF, video, data, or archive | Anonymity violation | Re-anonymize and re-host; blur/mute the video |
| Abstract/track not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Wrong track for the contribution | Weak subcommittee fit | Re-declare track at abstract time; write to the contribution type |
| Participants but no IRB/consent statement | Ethics exposure + scored down | Add the (anonymized) ethics + consent statement |
| No video for an embodied-interaction study | Read as a gap | Produce an anonymized video figure |

## Final-week order of operations

1. Freeze the study and results early; only the writing should churn near the deadline.
2. Register the abstract, authors, and **track** well before the abstract cutoff.
3. Produce and **anonymize the video** and supplement; host any archive behind an anonymizing view.
4. Run the mechanical anonymity checks on the **final** PDF, video, data, and archive — not drafts.
5. Fill every PCS field (track, subject areas, conflicts for every coauthor's institution and recent
   collaborators) a day early; late conflicts are the classic midnight failure.
6. Re-download the uploaded PDF and re-open the uploaded video cold to confirm they are the files you
   meant and that the video plays.

## Reverify each cycle

- The abstract/paper two-step and its dates; the exact `acmart` class options and template revision.
- The track list and how User Studies is split; the page budget.
- Video length/format/size limits; any generative-AI use/disclosure policy (**待核实**).

## Output format

```text
[HRI submission status] ready / blocked / needs work
[Abstract+track] title/authors/track locked by the earlier deadline? yes/no · track: <one of five>
[Format] pages (body incl. figures / refs) · acmart anonymous compliance
[Anonymity] PDF/video/data/archive clean / leaks: <where>
[Ethics] IRB/consent statement present (anonymized)?
[Video] anonymized video figure present + playable?
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
