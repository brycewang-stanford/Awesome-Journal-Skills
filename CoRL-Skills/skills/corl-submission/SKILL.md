---
name: corl-submission
description: Use when preparing or auditing a CoRL OpenReview submission — the corl_2026 LaTeX template, the 8-page main text with a mandatory Limitations section counted inside it, uncounted references and appendix, the supplementary file and 250 MB video, double-anonymous rules, abstract registration, and dual-submission checks.
---

# CoRL Submission

This is the pre-upload audit for a CoRL paper. The numbers below are the CoRL 2026
requirements as read on 2026-07-08 and re-verified on 2026-11-24 from the official
Instruction for Authors and Call for Papers (corl.org); the 2026 cycle is over and
CoRL 2027 was not yet announced on 2026-11-24, so apply this skill to a 2027-cycle
draft after re-opening the new year's pages — CoRL re-issues its
instructions annually and has changed page accounting between cycles.

## The 2026 package, itemized

| Element | 2026 rule | Notes |
|---|---|---|
| Platform | OpenReview, group `robot-learning.org/CoRL/2026/Conference` | Profile + conflicts needed for every author |
| Abstract registration | May 25, 2026, 23:59 AoE | Separate, earlier than the paper; authors frozen after it |
| Paper deadline | May 28, 2026, 23:59 AoE (a Thursday) | Supplementary zip due June 4, 2026 |
| Main text | 8 pages, **including a mandatory Limitations section** | Limitations counts toward the limit — budget for it |
| Not counted | Acknowledgments, references, optional appendix | Appendix rides in the same PDF |
| Template | `corl_2026` LaTeX class | Camera-ready later flips to `[final]` mode |
| Review model | Double-anonymous | Applies to paper, supplementary, and any linked site |
| Supplementary | Encouraged; single zip; video ≤ 250 MB (strict), ~3 min suggested | See `corl-supplementary` for content strategy |
| Reciprocal reviewing | At least one qualified author per paper; authors with 3+ submissions must review | Non-compliance can desk-reject |
| Generative AI | Disclose use briefly in the submission form; no AI authors; nonexistent citations desk-rejected | GPTZero screening in 2026 |

## What makes the CoRL audit different

Two venue-specific traps dominate desk problems here, and neither exists in the
same form at neighboring conferences:

1. **The Limitations section is not optional and not free.** The 2026 instructions
   require every submission to include a Limitations section — limiting
   assumptions, failure modes, and how they might be addressed — and it counts
   inside the 8 pages. Drafts imported from NeurIPS-style templates (where such
   sections often sit outside the limit) silently overflow. Audit the page budget
   with Limitations present, not as an afterthought.
2. **Project pages leak identity.** Robot-learning papers habitually ship a
   project website with videos. During review, any link that identifies an author,
   lab, or institution is an anonymity violation under the 2026 instructions —
   this includes the URL itself (`lab-name.github.io` fails even if the page is
   scrubbed). Use an anonymous hosting pattern or put the video in the
   supplementary upload instead.

## Anonymity sweep for a robot-learning paper

Beyond the standard items (author block, acknowledgments, metadata, third-person
self-citation), sweep the modalities specific to this field:

- **Video frames**: lab signage, whiteboards, badge lanyards, reflections in glossy
  robot shells, distinctive lab furniture that appears in your prior papers.
- **Robot livery**: stickers, hostnames on monitors, custom end-effectors already
  associated with your group.
- **Dataset paths** burned into figures or config listings (`/home/<user>/...`).
- **Repository and W&B links** in code snippets or appendix listings.

```bash
# Mechanical pre-upload pass on the submission PDF and supplementary bundle
pdftotext main.pdf - | grep -nEi 'github\.io|github\.com|wandb|acknowledg|our (lab|group|university)' | head
pdfinfo main.pdf | grep -Ei 'author|creator|producer'
grep -RnEi 'hostname|/home/|api_key' supplementary/code/ | head
stat -c '%n %s' supplementary/video.mp4      # must be <= 250 MB (2026 strict cap)
pdftotext main.pdf - | grep -ci 'limitation' # 0 hits => missing mandatory section
```

## Page-budget strategy under the 8+Limitations rule

- Write the Limitations section early and hold it at a fixed budget (half a page is
  a common shape); do not let it become the compression victim of deadline week.
- Overflow goes to the appendix — reviewers are not obligated to read it, so only
  non-load-bearing detail (full hyperparameter tables, extra rollouts, per-task
  breakdowns beyond the headline) may live there.
- Do not fight the template: class-file modifications, margin edits, and squeezed
  float spacing are detectable and read as rule-testing to ACs.

## Form fields and policy checks

- **Abstract registration first.** The 2026 cycle separated abstract (May 25) and
  paper (May 28); a missed abstract registration forecloses the submission
  entirely, and authors cannot be added or removed after it. Register with a
  stable title and author list.
- **Dual submission**: the paper must not be under review elsewhere; the
  fast-moving robot-learning arXiv culture makes this an easy accident when a
  workshop version is circulating — check the current CFP's exact scope wording
  each cycle.
- **GenAI policy** (added April 17, 2026): LLMs cannot be authors; the submission
  form asks for a brief disclosure of how generative AI was used for research and
  writing; papers citing references that do not exist are desk-rejected (CoRL 2026
  screened every submission with GPTZero, with chairs confirming flags); several
  near-duplicate submissions by the same authors are all desk-rejected. Resolve
  every reference against a real record before upload.
- **Dual-submission exceptions**: for a venue whose decision overlaps the review
  period (ICML decisions, for example), notify the Publication Chair before
  submitting; undisclosed overlap may be reported to both venues.
- Subject areas / keywords on the form drive reviewer assignment in a small,
  specialized pool; pick the subfield your harshest competent critic works in.

## Pre-upload checklist

```text
[ ] Abstract registered by the abstract deadline (title/authors stable)
[ ] Main text <= 8 pages WITH Limitations section included and substantive
[ ] References + appendix after main text, same PDF, uncounted
[ ] corl_2026 template unmodified; compiles with no page-limit tricks
[ ] Anonymity sweep passed: text, figures, video frames, links, metadata
[ ] Supplementary video <= 250 MB, ~3 min, anonymized end to end
[ ] Code/data (if included) scrubbed of identities, paths, and keys
[ ] OpenReview form: authors, conflicts, keywords, abstract synced with PDF
[ ] Dual-submission status confirmed with every coauthor in writing
[ ] GenAI-policy disclosure handled per the current instructions [待核实]
```

## Re-verify each cycle

Page accounting (the 2026 camera-ready got a 9th page; earlier cycles differed),
the Limitations rule, video caps, the GenAI policy, and deadline clock conventions
are all chair-set and cycle-volatile. The controlling sources are
https://www.corl.org/contributions/call-for-papers and
https://www.corl.org/contributions/instruction-for-authors for the live year —
open both before trusting any number in this file.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue corl-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.
