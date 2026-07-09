# Category 8 Build Queue - Computer Science and AI

Created: 2026-06-01

Purpose: turn the category-8 part of `JOURNAL-MASTER-LIST.md` plus the CS breadth inventory into
an executable build queue for complete depth packs. This file is a queue, not a completion claim.

## Current State

- Complete category-8 depth packs: **100 verified pack roots — TERMINAL QUOTA REACHED**
  (90 English conference depth packs + 10 Chinese-language CS-journal depth packs). The final two
  English conferences (FAccT — responsible AI; ICDT — database theory) closed out the 90-EN quota,
  and the Chinese sub-wave supplied the 10 CN targets. category-8 is complete at 100/100. The
  Chinese-language sub-wave (计算机学报 CJC, 软件学报 JOS, 计算机研究与发展 JCRD, 自动化学报 AAS,
  中国科学:信息科学 SSI, 电子学报 AES, 模式识别与人工智能 PR&AI, 计算机辅助设计与图形学学报 JCAD&CG,
  通信学报 JOC, 计算机科学 CSJ) is complete and each scores 94.0 (built as journal depth packs against
  the 600-substance-unit target, NOT added to CONFERENCE_DEPTH_PACKS). The ENTIRE Wave 25-A launch batch
  (24/24) finished 2026-07-08; EN core-61 tranches two through four
  (NAACL, ECCV, PLDI, SIGMOD, STOC, NSDI, USENIX Security, NDSS; FOCS, SODA, POPL,
  OOPSLA, VLDB, CIKM, EuroSys, ASPLOS; UIST, CSCW, ISCA, MICRO, RSS, CoRL,
  INTERSPEECH, COLM) landed the same day; the fifth tranche
  (HPCA, IROS, ICDE, ICDM, RecSys, MobiCom, ACM MM, ICASSP), the sixth tranche
  (SIGCOMM, EACL, AAMAS, WACV, MobiSys, SenSys, ISSTA, ESEC/FSE), and the seventh
  tranche (ASE, PODS, CoNEXT, IMC, IPSN, VIS, ICSME, ECAI) followed: `NeurIPS-Skills`, `ICML-Skills`, `ICLR-Skills`,
  `AAAI-Skills`, `IJCAI-Skills`, `AISTATS-Skills`, `UAI-Skills`, `COLT-Skills`, `MLSys-Skills`,
  `KDD-Skills`, `The-Web-Conference-Skills`, `WSDM-Skills`, `SIGIR-Skills`, `CVPR-Skills`,
  `ICCV-Skills`, `ACL-Skills`, `EMNLP-Skills`, `ICRA-Skills`, `CHI-Skills`, `SOSP-Skills`,
  `OSDI-Skills`, `IEEE-SP-Skills`, `ACM-CCS-Skills`, `ICSE-Skills`, `NAACL-Skills`, `ECCV-Skills`,
  `PLDI-Skills`, `SIGMOD-Skills`, `STOC-Skills`, `NSDI-Skills`, `USENIX-Security-Skills`,
  `NDSS-Skills`, `FOCS-Skills`, `SODA-Skills`, `POPL-Skills`, `OOPSLA-Skills`, `VLDB-Skills`,
  `CIKM-Skills`, `EuroSys-Skills`, `ASPLOS-Skills`, `UIST-Skills`, `CSCW-Skills`, `ISCA-Skills`,
  `MICRO-Skills`, `RSS-Skills`, `CoRL-Skills`, `INTERSPEECH-Skills`, `COLM-Skills`, `HPCA-Skills`,
  `IROS-Skills`, `ICDE-Skills`, `ICDM-Skills`, `RecSys-Skills`, `MobiCom-Skills`, `ACM-MM-Skills`,
  `ICASSP-Skills`, `SIGCOMM-Skills`, `EACL-Skills`, `AAMAS-Skills`, `WACV-Skills`,
  `MobiSys-Skills`, `SenSys-Skills`, `ISSTA-Skills`, `FSE-Skills`, `ASE-Skills`,
  `PODS-Skills`, `CoNEXT-Skills`, `IMC-Skills`, `IPSN-Skills`, `VIS-Skills`,
  `ICSME-Skills`, `ECAI-Skills`, `ATC-Skills`, `FAST-Skills`, `PPoPP-Skills`,
  `CAV-Skills`, `ICALP-Skills`, `PODC-Skills`, `SIGMETRICS-Skills`, `PerCom-Skills`,
  `SIGGRAPH-Skills`, `INFOCOM-Skills`, `ITCS-Skills`, `HRI-Skills`, `SoCC-Skills`,
  `DAC-Skills`, `EDBT-Skills`, `TACAS-Skills`.
  The eighth tranche (ATC, FAST, PPoPP, CAV, ICALP, PODC, SIGMETRICS, PerCom)
  added systems/storage/parallelism/verification/theory/performance/ubicomp breadth;
  the ninth tranche (SIGGRAPH, INFOCOM, ITCS, HRI, SoCC, DAC, EDBT, TACAS) added
  graphics/large-networking/conceptual-theory/HRI/cloud/EDA/European-DB/verification-tools breadth.
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
| 7 | UAI | conference | `uncertainty-in-artificial-intelligence`; depth pack `UAI-Skills` complete |
| 8 | COLT | conference | `conference-on-learning-theory`; depth pack `COLT-Skills` complete |
| 9 | MLSys | conference | `conference-on-machine-learning-and-systems`; depth pack `MLSys-Skills` complete |
| 10 | KDD | conference | `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining`; depth pack `KDD-Skills` complete |
| 11 | The Web Conference | conference | `the-web-conference`; depth pack `The-Web-Conference-Skills` complete |
| 12 | WSDM | conference | `acm-international-conference-on-web-search-and-data-mining`; depth pack `WSDM-Skills` complete |
| 13 | SIGIR | conference | `acm-sigir-conference-on-research-and-development-in-information-retrieval`; depth pack `SIGIR-Skills` complete |
| 14 | CVPR | conference | `computer-vision-and-pattern-recognition`; depth pack `CVPR-Skills` complete |
| 15 | ICCV | conference | `international-conference-on-computer-vision`; depth pack `ICCV-Skills` complete |
| 16 | ACL | conference | `annual-meeting-of-the-association-for-computational-linguistics`; depth pack `ACL-Skills` complete |
| 17 | EMNLP | conference | `conference-on-empirical-methods-in-natural-language-processing`; depth pack `EMNLP-Skills` complete |
| 18 | ICRA | conference | `ieee-international-conference-on-robotics-and-automation`; depth pack `ICRA-Skills` complete |
| 19 | CHI | conference | `acm-chi-conference-on-human-factors-in-computing-systems`; depth pack `CHI-Skills` complete |
| 20 | SOSP | conference | `acm-symposium-on-operating-systems-principles`; depth pack `SOSP-Skills` complete |
| 21 | OSDI | conference | `usenix-symposium-on-operating-systems-design-and-implementation`; depth pack `OSDI-Skills` complete |
| 22 | IEEE S&P | conference | `ieee-symposium-on-security-and-privacy`; depth pack `IEEE-SP-Skills` complete |
| 23 | ACM CCS | conference | `acm-conference-on-computer-and-communications-security`; depth pack `ACM-CCS-Skills` complete |
| 24 | ICSE | conference | `international-conference-on-software-engineering`; depth pack `ICSE-Skills` complete |

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
