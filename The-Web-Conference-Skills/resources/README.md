# The Web Conference Resources

Working materials that back the `skills/` directory. The skills carry the advice;
these files carry the verified sources, the benchmark papers, the style
demonstration, and the reproducibility tooling an agent needs to act on that advice
for a Web Conference (WWW) submission without inventing venue policy.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Check which WWW 2026 facts were verified, from which official URL, on 2026-07-08 — including the access-method note and the 待核实 register. Read this before repeating any deadline, page count, or fee. |
| [`external_tools.md`](external_tools.md) | Jump to the official conference site, calls, ACM DL proceedings, dblp index, and per-cycle author checks. |
| [`exemplars/library.md`](exemplars/library.md) | Position against five verified WWW papers (proceedings-confirmed), with a sibling-venue misattribution guard for the WSDM/SIGIR/KDD circuit. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional abstract+introduction get rewritten into the web-native, mixed-audience first-page arc the venue rewards. |
| [`code/README.md`](code/README.md) | Reach the shared ML-conference reproducibility kit, with Web Conference-specific notes on crawl manifests and decay accounting. |

## Ground rules for this pack

- **Nothing here overrides the current edition's pages.** The venue re-cuts
  tracks, moves deadlines, switches submission platforms (OpenReview ↔ EasyChair
  between 2025 and 2026), and in 2026 moved the conference itself by ten weeks.
- **Web data ages.** Exemplar papers demonstrate positioning and structure; their
  datasets and platform observations describe the Web of their year, not yours.
- **This is a web-research pack.** It shares the repository with economics and
  ML-conference packs; the applicable code kit is the ML-conference one referenced
  in `code/README.md`, extended by the crawl-specific practices in
  `../skills/webconf-reproducibility/SKILL.md`.

## Suggested route through the pack

1. Decide venue, track, and lane with
   [`../skills/webconf-topic-selection`](../skills/webconf-topic-selection/SKILL.md),
   then set the calendar with
   [`../skills/webconf-workflow`](../skills/webconf-workflow/SKILL.md).
2. Build evidence and prose against
   [`../skills/webconf-experiments`](../skills/webconf-experiments/SKILL.md),
   [`../skills/webconf-writing-style`](../skills/webconf-writing-style/SKILL.md),
   and the exemplars library.
3. Package and audit with
   [`../skills/webconf-supplementary`](../skills/webconf-supplementary/SKILL.md) and
   [`../skills/webconf-submission`](../skills/webconf-submission/SKILL.md),
   re-verifying every number in
   [`official-source-map.md`](official-source-map.md).
