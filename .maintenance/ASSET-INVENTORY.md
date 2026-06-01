# AJS Wave 1 Asset Inventory

Created: 2026-06-01

Purpose: bootstrap Wave 1 of `EXPANSION-PLAN.md` by mapping the current repository assets into the
10-category expansion frame. This is an inventory, not a completion claim for the 1000 complete-pack
target.

## Current Hard Counts

Verified by `python3 tools/audit_repo.py` on 2026-06-01 after the ICLR category-8 depth pack:

- Canonical `SKILL.md`: 1036
- Curated pack roots: 48
- Root journal entry cards: 200

Counting distinction: a current AJS "pack root" is not always a terminal expansion-plan package.
Depth packs are closest to the final "complete skill package" unit. Breadth bundles, routers, and
toolkits are infrastructure or coverage layers that can seed later depth-pack work.

## Pack Root Map

| Pack root | Kind | Expansion category | Wave 1 status |
|---|---|---|---|
| `AER-Skills` | imported depth pack | 1 Econ & Management | reusable / upgrade only if needed |
| `Academy-of-Management-Journal-Skills` | depth pack | 1 Econ & Management | reusable |
| `Academy-of-Management-Review-Skills` | depth pack | 1 Econ & Management | reusable |
| `Accounting-Research-Skills` | depth pack | 1 Econ & Management | reusable |
| `Administrative-Science-Quarterly-Skills` | depth pack | 1 Econ & Management | reusable |
| `Annals-of-Mathematics-Skills` | depth pack | 4 Math & Physical | reusable |
| `Cancer-Cell-Skills` | depth pack | 5 Life Sciences | reusable |
| `Cell-Skills` | depth pack | 5 Life Sciences | reusable |
| `China-Economic-Quarterly-Skills` | depth pack | 1 Econ & Management | reusable |
| `China-Industrial-Economics-Skills` | depth pack | 1 Econ & Management | reusable |
| `China-Rural-Economy-Skills` | depth pack | 1 Econ & Management | reusable |
| `Chinese-Public-Administration-Skills` | depth pack | 2 Social Sciences | reusable |
| `Chinese-SocialScience-Journal-Skills` | breadth bundle | spans 0 / 1 / 2 / 7 | seed bundle; per-entry root-card split recorded |
| `Computer-Science-Conference-Skills` | breadth bundle | 8 CS & AI | seed bundle; not a substitute for 100 CS depth packs |
| `Econometrica-Skills` | depth pack | 1 Econ & Management | reusable |
| `Economic-Research-Journal-Skills` | depth pack | 1 Econ & Management | reusable |
| `English-NaturalScience-Journal-Skills` | breadth bundle | spans 0 / 4 / 5 / 6 / 7 / 8 / 9 | seed bundle; per-entry split recorded |
| `English-SocialScience-Journal-Skills` | breadth bundle | mostly 1 Econ & Management | seed bundle |
| `ICML-Skills` | depth pack | 8 CS & AI | reusable; second category-8 Wave 25-A depth pack |
| `ICLR-Skills` | depth pack | 8 CS & AI | reusable; third category-8 Wave 25-A depth pack |
| `JAMA-Skills` | depth pack | 6 Medicine & Health | reusable |
| `Journal-of-Finance-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Finance-and-Economics-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Financial-Economics-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Financial-Research-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Management-Sciences-in-China-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Management-World-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Political-Economy-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-Quantitative-and-Technological-Economics-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-World-Economy-Skills` | depth pack | 1 Econ & Management | reusable |
| `Journal-of-the-American-Chemical-Society-Skills` | depth pack | 4 Math & Physical | reusable |
| `Lancet-Skills` | depth pack | 6 Medicine & Health | reusable |
| `NEJM-Skills` | depth pack | 6 Medicine & Health | reusable |
| `Nankai-Business-Review-Skills` | depth pack | 1 Econ & Management | reusable |
| `Nature-Skills` | imported depth/toolkit pack | 0 Multidisciplinary | reusable / imported |
| `NeurIPS-Skills` | depth pack | 8 CS & AI | reusable; first category-8 Wave 25-A depth pack |
| `PNAS-Skills` | depth pack | 0 Multidisciplinary | reusable |
| `Physical-Review-Letters-Skills` | depth pack | 4 Math & Physical | reusable |
| `Quarterly-Journal-of-Economics-Skills` | depth pack | 1 Econ & Management | reusable |
| `Review-of-Economic-Studies-Skills` | depth pack | 1 Econ & Management | reusable |
| `Review-of-Financial-Studies-Skills` | depth pack | 1 Econ & Management | reusable |
| `Science-Skills` | depth pack | 0 Multidisciplinary | reusable |
| `Social-Sciences-in-China-Skills` | depth pack | 2 Social Sciences | reusable |
| `Sociological-Studies-Skills` | depth pack | 2 Social Sciences | reusable |
| `Strategic-Management-Journal-Skills` | depth pack | 1 Econ & Management | reusable |
| `claude-scholar` | imported toolkit | cross-cutting toolkit | keep out of 1000 venue-pack quota |
| `codex-claude-academic-skills` | imported toolkit | cross-cutting toolkit | keep out of 1000 venue-pack quota |
| `nature-paper-skills` | imported toolkit/depth support | 0 Multidisciplinary / cross-cutting | reusable / imported |

## Category Coverage Snapshot

| Category | Current strong assets | Main gap |
|---|---|---|
| 0 Multidisciplinary | Science, PNAS, Nature imported assets, natural-science breadth seeds | complete depth packs for additional multidisciplinary/interdisciplinary venues |
| 1 Econ & Management | strongest current coverage: English and Chinese depth packs + EN social breadth | expand selected breadth entries into complete depth packs |
| 2 Social Sciences | Social Sciences in China, Sociological Studies, Chinese Public Administration, CN breadth seeds | English social-science depth packs and more CN social-science depth packs |
| 3 Humanities | CN breadth contains some adjacent roots | almost all complete packs still missing |
| 4 Math & Physical | Annals, PRL, JACS, natural-science breadth seeds | more math/physics/chemistry depth packs |
| 5 Life Sciences | Cell, Cancer Cell, natural-science breadth seeds | more life-science depth packs |
| 6 Medicine & Health | NEJM, Lancet, JAMA, natural-science breadth seeds | specialty medical depth packs |
| 7 Engineering & Tech | natural-science breadth seeds | complete engineering depth packs mostly missing |
| 8 CS & AI | NeurIPS + ICML + ICLR depth packs + CS conference breadth seed + JMLR/TPAMI/NMI journal seeds in natural-science breadth | complete CS/AI conference and journal depth packs mostly missing |
| 9 Agriculture & Env | natural-science breadth seeds | complete agriculture/environment depth packs mostly missing |

## Root Card Map

Current root cards are validated navigation entries, not separate installable skills:

- 100 root cards point into `English-SocialScience-Journal-Skills` and map primarily to category 1.
- 100 root cards point into `Chinese-SocialScience-Journal-Skills`; their working per-entry split
  is recorded in `.maintenance/ROOT-CARD-CATEGORY-MAP.md`.
- 100 natural-science breadth cards and 155 CS conference breadth cards are split in
  `.maintenance/BREADTH-ENTRY-CATEGORY-MAP.md`.

Wave 1 inventory status: current pack roots, root cards, and breadth cards now have a working
category split. `JOURNAL-MASTER-LIST.md` uses `[A-depth]` for complete reusable depth assets, while
breadth-only seeds stay documented in the category-map files until upgraded into depth packs.

Category 8 now has an executable queue in `.maintenance/CATEGORY-8-BUILD-QUEUE.md`: 90 English
targets, 10 Chinese targets, a first 24-pack AI-first launch batch, and CS/AI pack acceptance gates.
`NeurIPS-Skills`, `ICML-Skills`, and `ICLR-Skills` are the first three completed depth packs from
that launch batch.

Next task: continue Wave 25-A depth-pack production with AAAI, IJCAI, AISTATS, and UAI, preserving
official-source checks and clone-audit gates per pack.
