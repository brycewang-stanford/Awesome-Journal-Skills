---
name: iccv-supplementary
description: Use when planning or auditing ICCV supplementary material under the same-day paper-plus-supplement deadline, covering what moves out of the 8-page body, parallel production of videos and code from February onward, double-blind hygiene inside the archive, and making depth material navigable for reviewers who choose to open it.
---

# ICCV Supplementary Material

Since the 2025 cycle, ICCV collects the supplement **at the paper deadline** —
one upload event in early March (March 7, 2025, 11:59pm HST; announced as a
deliberate process change that also shortened the decision timeline). That
single scheduling fact rewrites supplement strategy: there is no packaging week
after the paper freezes, so the supplement is a parallel product with its own
owner from February, or it is a casualty.

## What the same-day rule changes in practice

| Old two-deadline habit | Same-day reality |
|---|---|
| "Ship the paper, then render videos next week" | Videos render while the paper is still being edited — reserve machines for both |
| Supplement absorbs deadline-night leftovers | Anything unfinished at the deadline simply does not exist for reviewers |
| Code scrubbed after the PDF freezes | Identity scan runs on paper *and* archive the same night |
| Supplement pointers checked at leisure | "See Suppl. C" written on deadline day points at a section that must already exist |

Practical rule: the supplement's content list is frozen when the paper's section
structure freezes (about two weeks out), and from then on the archive only
*executes* that list.

## Division of labor with the 8 pages

The body must stand alone for a reviewer who never opens the archive; the
supplement rewards the reviewer who does. Sort content by the question it
answers:

- **"Is the claim true?"** → body, always: headline tables, the decisive
  ablation, the honest limitation.
- **"Is it true broadly?"** → supplement: full ablation grids, additional
  datasets, per-class or per-sequence breakdowns, sensitivity sweeps.
- **"Can I see it?"** → supplement, and this is where ICCV differs from
  text-first venues: qualitative galleries, uncurated sample grids, and video
  for anything temporal or 3D. State the selection rule in each caption
  ("validation images 1–12, no curation") — a stated rule is what separates
  evidence from advertising.
- **"Could I rebuild it?"** → supplement: configs, pseudo-code, dataset
  preprocessing detail, plus the code package (`iccv-artifact-evaluation`).
- **"Does the math hold?"** → supplement appendix; vision reviewers spot-check
  derivations rather than read them linearly, so number every step they might
  jump to.

Never exile decision-critical content: a reviewer who must open a zip to learn
how the method works will instead assume the worst and score accordingly.

## Anonymity inside the archive

The archive is reviewed under full double-blind rules, and archives leak
differently than PDFs:

```bash
# Same-night sweep across the whole supplement
unzip -l supplement.zip | grep -viE '^\s*(Archive|Length|----)' | grep -iE 'user|home|<labname>' 
ffprobe -v quiet -show_format videos/main_comparison.mp4 | grep -i 'artist\|author\|comment'
grep -rniE 'wandb|slurm|/nfs/|@(gmail|edu)' code/ --include='*.py' --include='*.yaml' | head
exiftool figures/*.png 2>/dev/null | grep -i 'author\|copyright' | head
```

Video container tags, W&B entity names in configs, cluster paths in logs, and
PNG metadata are the four leaks PDFs never taught you to check. Remember also the
2025 codebase rule: even inside the supplement, do not cite or link your public
repository — include the scrubbed code itself and an availability sentence.

## Structure for a seven-minute visit

Reviewers give supplements minutes. Design entry points, not chapters:

```text
supplement.zip
├── 00_INDEX.pdf         # one page: what is where, mapped to paper claims
├── A_extended_results/  # grids continuing the body's table numbering
├── B_ablations/         # research question restated above each grid
├── C_failure_modes/     # taxonomy first, examples second
├── D_videos/
│   └── INDEX.txt        # clip → claim → timestamp of the money moment
├── E_implementation/    # configs, preprocessing, hyperparameter tables
└── F_code/              # see iccv-artifact-evaluation for packaging bar
```

Two conventions repay their cost every review: continue the paper's numbering
(Suppl. Table 9 follows body Table 8, so discussion-week comments are
unambiguous), and put the single most persuasive qualitative result *first* in
the video index — a reviewer who watches one clip should watch your best.

## Failure gallery: the credibility purchase

An ICCV supplement with zero failure cases reads as curated, and vision
reviewers are the world's most practiced detectors of cherry-picking. Budget a
failure section with a two-level taxonomy (when it fails; why it fails there)
and cross-reference it from the body's limitations paragraph. This is the
cheapest credibility available at the venue: it costs one page of the archive
and no page of the paper.

## Recurring archive defects

1. Dangling body pointers ("Suppl. G") after a late reorganization — grep the
   final PDF for `Suppl` and resolve each against `00_INDEX`.
2. Config dumps contradicting the body's stated hyperparameters because one was
   updated post-freeze — regenerate both from one source of truth.
3. Videos that only play in one player — test the archive on a machine that
   never touched your toolchain.
4. A 300 MB gallery where 30 MB of curated depth would review better — size
   limits for 2025 were not verifiable (待核实), so design for a strict cap.
5. Third-party assets carrying their authors' watermarks into your anonymous
   archive.

## Reverify each cycle

- Whether the unified deadline persists in 2027 or the supplement regains its
  own date.
- Size caps and permitted formats (待核实 even for 2025).
- Any change to the do-not-cite-your-repo wording.

## Output format

```text
[Supplement verdict] ship / fix-first
[Parallel production] owner named · render slots reserved: yes/no
[Placement audit] decision-critical content in archive: none / <move list>
[Leak sweep] paths · video tags · configs · image metadata: clean?
[Navigation] index present · numbering continues body · best clip first
[Pointer resolution] body references resolving: n/m
```
