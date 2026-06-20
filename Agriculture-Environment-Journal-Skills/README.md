# Agriculture & Environment Journal Skills

<p align="center">
  <img src="assets/cover.svg" alt="Agriculture & Environment Journal Skills — 30 flagship agriculture, environment and earth-science journals" width="220">
</p>

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Index](https://img.shields.io/badge/index-Nature%20Food%20%C2%B7%20GCB%20%C2%B7%20WRR%20%C2%B7%20EPSL-1f6feb)](#)
[![Claude Code](https://img.shields.io/badge/agent-Claude%20Code-cc785c)](https://github.com/anthropics/claude-code)

English | [简体中文](README.zh-CN.md)

An opinionated agent skill stack for **30 flagship English-language agriculture, environment, and earth-science journals** — the category the natural-science bundle leaves almost empty. It covers the agriculture / food / plant / soil / crop flagships (Nature Food, Nature Plants, New Phytologist, The Plant Journal, the Annual Review of Plant Biology, Field Crops Research, the soil and agronomy venues, Food Chemistry, Trends in Food Science & Technology); the environment / sustainability / pollution leaders (Global Change Biology, Environment International, Environmental Health Perspectives, Journal of Cleaner Production, Resources Conservation & Recycling, Environmental Pollution); and the earth / atmosphere / hydrology / ocean / climate flagships (Journal of Climate, Water Resources Research, Earth and Planetary Science Letters, Geology, Global Biogeochemical Cycles, Earth System Science Data, and more).

This is the agriculture-and-environment sibling of [`English-NaturalScience-Journal-Skills`](../English-NaturalScience-Journal-Skills/) and [`Engineering-Technology-Journal-Skills`](../Engineering-Technology-Journal-Skills/). Like them, it ships **one self-contained fit-and-house-style skill per journal**, plus `en-agrienv-journal-workflow` for routing. Each journal skill helps answer: *is my manuscript on-target, how should it be framed, what field evidence, data deposition and reporting does this venue expect, and what official submission details must be re-checked?*

## Coverage

| Group | Count |
|---|--:|
| Agriculture · food · plant · soil · crop science | 11 |
| Environment · sustainability · pollution | 7 |
| Earth · atmosphere · hydrology · ocean · climate | 12 |
| **Total journal skills** | **30** |
| Routing workflow (`en-agrienv-journal-workflow`) | 1 |

## How to use

1. **Route first.** Start from `en-agrienv-journal-workflow` to classify your
   manuscript by sub-field (agronomy / plant / soil / food / environment / earth /
   climate), contribution type, and evidence shape, and get a ranked shortlist.
2. **Fit second.** Open the single-journal skill for your top candidate to test
   scope fit, framing, the field-evidence and data-deposition bar, house style, and
   the likely desk-reject triggers.
3. **Re-check official rules last.** Every skill ends with an official-submission
   checklist. Before submitting, open the journal's current author instructions
   (see `resources/official-source-map.md`) — the live page always wins, especially
   for mandatory data/code deposition.

## Design rules (shared with the sibling bundles)

- **No volatile facts.** No impact factors, acceptance rates, ISSNs, exact limits,
  APC amounts, or editor names.
- **No fabricated citations.** Literatures are referred to generically.
- **Stable conventions only.** Durable structural facts (the Nature significance-statement
  system, AGU/AMS/GSA/ASLO society affiliations, the data-journal nature of ESSD, and
  standard FAIR data-deposition expectations) are used where they help fit.
- **Official page wins.** If a live instruction conflicts with a skill, follow the
  official instruction.

## License

MIT © 2026 Bryce Wang. See [LICENSE](LICENSE).
