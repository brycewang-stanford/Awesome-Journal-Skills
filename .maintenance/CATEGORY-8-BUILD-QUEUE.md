# Category 8 Build Queue - Computer Science and AI

Created: 2026-06-01

Purpose: turn the category-8 part of `JOURNAL-MASTER-LIST.md` plus the CS breadth inventory into
an executable build queue for complete depth packs. This file is a queue, not a completion claim.

## Current State

- Complete category-8 depth packs: 6 verified pack roots: `NeurIPS-Skills`, `ICML-Skills`,
  `ICLR-Skills`, `AAAI-Skills`, `IJCAI-Skills`, `AISTATS-Skills`.
- Existing category-8 breadth seeds:
  - 155 conference profiles in `Computer-Science-Conference-Skills`.
  - 3 journal profiles in `English-NaturalScience-Journal-Skills`: `nature-machine-intelligence`,
    `ieee-transactions-on-pattern-analysis-and-machine-intelligence`, `journal-of-machine-learning-research`.
- Terminal category-8 quota from `EXPANSION-PLAN.md`: 90 English targets + 10 Chinese targets =
  100 complete packs.

## Complete Pack Template

Use the CS/AI variant from `EXPANSION-PLAN.md`, adapting names to each venue:

- `<slug>-submission`
- `<slug>-author-response`
- `<slug>-camera-ready`
- `<slug>-artifact-evaluation`
- `<slug>-reproducibility`
- `<slug>-supplementary`
- `<slug>-review-process`
- `<slug>-writing-style`
- `<slug>-related-work`
- `<slug>-experiments`
- `<slug>-workflow`
- `<slug>-topic-selection`

Source rule: before creating a complete pack, open the current official CFP, author kit, journal
instructions, artifact policy, and review-process page where available. Conference details are
cycle-volatile; do not hard-code deadlines, locations, page limits, fees, chairs, AI-use rules, or
rebuttal format from memory.

## Wave 25-A - First 24 AI-First Depth Packs

Build these first because the user explicitly prioritized AI conferences and these have high user
value plus existing breadth seeds.

| Order | Target | Type | Existing seed |
|---:|---|---|---|
| 1 | NeurIPS | conference | `neural-information-processing-systems`; depth pack `NeurIPS-Skills` complete |
| 2 | ICML | conference | `international-conference-on-machine-learning`; depth pack `ICML-Skills` complete |
| 3 | ICLR | conference | `international-conference-on-learning-representations`; depth pack `ICLR-Skills` complete |
| 4 | AAAI | conference | `aaai-conference-on-artificial-intelligence`; depth pack `AAAI-Skills` complete |
| 5 | IJCAI | conference | `international-joint-conference-on-artificial-intelligence`; depth pack `IJCAI-Skills` complete |
| 6 | AISTATS | conference | `artificial-intelligence-and-statistics`; depth pack `AISTATS-Skills` complete |
| 7 | UAI | conference | `uncertainty-in-artificial-intelligence` |
| 8 | COLT | conference | `conference-on-learning-theory` |
| 9 | MLSys | conference | `conference-on-machine-learning-and-systems` |
| 10 | KDD | conference | `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining` |
| 11 | The Web Conference | conference | `the-web-conference` |
| 12 | WSDM | conference | `acm-international-conference-on-web-search-and-data-mining` |
| 13 | SIGIR | conference | `acm-sigir-conference-on-research-and-development-in-information-retrieval` |
| 14 | CVPR | conference | `computer-vision-and-pattern-recognition` |
| 15 | ICCV | conference | `international-conference-on-computer-vision` |
| 16 | ACL | conference | `annual-meeting-of-the-association-for-computational-linguistics` |
| 17 | EMNLP | conference | `conference-on-empirical-methods-in-natural-language-processing` |
| 18 | ICRA | conference | `ieee-international-conference-on-robotics-and-automation` |
| 19 | CHI | conference | `acm-chi-conference-on-human-factors-in-computing-systems` |
| 20 | SOSP | conference | `acm-symposium-on-operating-systems-principles` |
| 21 | OSDI | conference | `usenix-symposium-on-operating-systems-design-and-implementation` |
| 22 | IEEE S&P | conference | `ieee-symposium-on-security-and-privacy` |
| 23 | ACM CCS | conference | `acm-conference-on-computer-and-communications-security` |
| 24 | ICSE | conference | `international-conference-on-software-engineering` |

## English 90 Target List

### EN Conferences - Core 61 From Master List

AI / ML:

- NeurIPS
- ICML
- ICLR
- AAAI
- IJCAI
- COLT
- AISTATS
- UAI

Computer vision:

- CVPR
- ICCV
- ECCV

NLP:

- ACL
- EMNLP
- NAACL

Data mining / Web / IR:

- KDD
- The Web Conference
- WSDM
- CIKM
- ICDM
- SIGIR

Multimedia / speech:

- ACM MM
- INTERSPEECH
- ICASSP

Robotics:

- ICRA
- IROS
- RSS
- CoRL

Graphics:

- SIGGRAPH
- SIGGRAPH Asia

HCI:

- CHI
- UIST
- CSCW

Systems:

- OSDI
- SOSP
- NSDI
- EuroSys
- USENIX ATC
- ASPLOS

Architecture:

- ISCA
- MICRO
- HPCA

Databases:

- SIGMOD
- VLDB
- ICDE
- PODS

Theory:

- STOC
- FOCS
- SODA

Security:

- IEEE S&P
- USENIX Security
- ACM CCS
- NDSS

Networking:

- SIGCOMM
- INFOCOM
- MobiCom

Programming languages / software engineering:

- POPL
- PLDI
- OOPSLA
- ICSE
- FSE
- ASE

### EN Journal Targets - 22 From Master List

- Journal of the ACM
- IEEE TPAMI
- JMLR
- Artificial Intelligence
- IJCV
- Nature Machine Intelligence
- IEEE TKDE
- ACM TOG
- IEEE/ACM Transactions on Networking
- IEEE TSE
- ACM TOPLAS
- SIAM Journal on Computing
- Computational Linguistics
- IEEE TVCG
- ACM Computing Surveys
- IEEE TDSC
- IEEE TMC
- IEEE TC
- ACM TOCS
- IEEE TIFS
- ACM TODS
- IEEE TPDS

### EN Fill Slots - 7 Breadth-Seeded Additions

Use these to bring category-8 English targets to 90 while staying conference-first:

- MLSys
- RecSys
- FAccT
- AAMAS
- MICCAI
- ICFP
- CAV

English count: 61 conferences + 22 journals + 7 fill slots = 90.

## Chinese 10 Target List

Use `JOURNAL-MASTER-LIST.md` as the controlling source and verify against the current CCF Chinese
journal list before pack creation:

- 计算机学报
- 软件学报
- 计算机研究与发展
- 自动化学报
- 中国科学:信息科学
- 电子学报
- 模式识别与人工智能
- 计算机辅助设计与图形学学报
- 通信学报
- 计算机科学

## Build Order After Wave 25-A

1. Complete the remaining AI/ML and data/web/IR conference targets: ECCV, CIKM, ICDM, RecSys,
   FAccT, AAMAS, SIGIR-adjacent venues, and venue-specific author-response workflows.
2. Build the vision/NLP/robotics/HCI cluster next because these communities have distinct artifact,
   ethics, anonymity, and supplementary-material norms.
3. Build systems/security/SE/PL/DB/theory clusters as separate subwaves; their artifact evaluation,
   shepherding, claims-of-correctness, benchmark, and proof-exposition conventions should not be
   cloned from AI/ML packs.
4. Build journal targets only after conference template quality is stable; journal packs need
   journal-specific review-cycle, special-issue, revision, and publication-model handling.
5. Build the 10 Chinese targets as a dedicated Chinese-language subwave with source-map verification
   and CCF/CSTPC/CNKI anchor checks.

## Acceptance Gate Per Category-8 Pack

- Complete structure and marketplace metadata.
- 12 CS/AI skills present unless a documented venue exception justifies a different set.
- `resources/official-source-map.md` includes official URL(s), checked date, and unresolved volatile
  facts.
- No annual fact is asserted without a live official source check.
- `python3 tools/run_checks.py --skip-reports` passes.
- Clone audit stays under the 0.90 fail threshold, with venue-specific sections that reflect the
  conference or journal's real review process.
