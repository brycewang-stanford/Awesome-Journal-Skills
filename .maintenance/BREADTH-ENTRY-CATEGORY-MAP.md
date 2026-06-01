# Breadth Entry Category Map

Created: 2026-06-01

Purpose: complete the Wave 1 inventory split for the two breadth bundles that are not root-card
sets: `English-NaturalScience-Journal-Skills` and `Computer-Science-Conference-Skills`.

Counting rule: every line below is an existing breadth profile seed unless explicitly marked as a
router. A breadth seed can support expansion planning, but it is not the same unit as a complete
depth pack in `EXPANSION-PLAN.md`.

## Summary

| Bundle | Profiles | Routers | Primary expansion category split |
|---|---:|---:|---|
| `English-NaturalScience-Journal-Skills` | 100 | 1 | cat 0: 8; cat 4: 25; cat 5: 30; cat 6: 23; cat 7: 6; cat 8: 3; cat 9: 5 |
| `Computer-Science-Conference-Skills` | 155 | 1 | cat 8: 155 |

## English Natural Science Breadth Split

Source roster: `English-NaturalScience-Journal-Skills/resources/journal-roster.md`.

### Category 0 - Multidisciplinary / Cross-Disciplinary (8)

- `nature`
- `science`
- `pnas`
- `nature-communications`
- `science-advances`
- `national-science-review`
- `the-innovation`
- `nature-human-behaviour`

Notes: `nature-human-behaviour` is a cross-disciplinary behavior-science journal. It can also seed
social-science planning, but its primary split here is category 0 because the current natural-science
bundle excludes category 2 from its declared span.

### Category 4 - Mathematics and Physical Sciences (25)

Physics and astronomy:

- `physical-review-letters`
- `reviews-of-modern-physics`
- `physical-review-x`
- `nature-physics`
- `nature-photonics`
- `prx-quantum`
- `physical-review-d`
- `physical-review-b`
- `reports-on-progress-in-physics`
- `nature-astronomy`
- `the-astrophysical-journal`
- `monthly-notices-of-the-royal-astronomical-society`

Chemistry:

- `journal-of-the-american-chemical-society`
- `angewandte-chemie-international-edition`
- `nature-chemistry`
- `chemical-reviews`
- `chemical-society-reviews`
- `nature-catalysis`
- `accounts-of-chemical-research`
- `chem`
- `acs-nano`
- `nature-nanotechnology`

Mathematics:

- `annals-of-mathematics`
- `inventiones-mathematicae`
- `journal-of-the-american-mathematical-society`

### Category 5 - Life Sciences (30)

Cell, molecular, genetics, methods, and biotechnology:

- `cell`
- `molecular-cell`
- `cell-stem-cell`
- `cancer-cell`
- `cell-metabolism`
- `immunity`
- `neuron`
- `developmental-cell`
- `current-biology`
- `nature-genetics`
- `nature-methods`
- `nature-biotechnology`
- `nature-cell-biology`
- `nature-structural-and-molecular-biology`
- `the-embo-journal`
- `nucleic-acids-research`

Ecology, evolution, plant biology, and microbial biology:

- `nature-ecology-and-evolution`
- `molecular-biology-and-evolution`
- `ecology-letters`
- `the-plant-cell`
- `nature-microbiology`

Immunology, host-pathogen biology, and experimental biology:

- `nature-immunology`
- `science-immunology`
- `cell-host-and-microbe`
- `journal-of-experimental-medicine`

Open biology, genomics, neuroscience, and cognitive science:

- `elife`
- `plos-biology`
- `genome-biology`
- `nature-neuroscience`
- `trends-in-cognitive-sciences`

Boundary notes: `elife` can also seed category 0 because of its broad-review model;
`journal-of-experimental-medicine` can also seed category 6, but its current profile DNA is mechanistic and
experimental rather than clinical.

### Category 6 - Medicine and Health (23)

General clinical medicine:

- `nejm`
- `the-lancet`
- `jama`
- `the-bmj`
- `annals-of-internal-medicine`
- `nature-medicine`
- `plos-medicine`

Clinical specialty medicine:

- `the-lancet-oncology`
- `journal-of-clinical-oncology`
- `the-lancet-infectious-diseases`
- `the-lancet-neurology`
- `circulation`
- `journal-of-the-american-college-of-cardiology`
- `european-heart-journal`
- `gastroenterology`
- `gut`
- `blood`
- `diabetes-care`

Translational medicine, oncology, and psychiatry:

- `journal-of-clinical-investigation`
- `science-translational-medicine`
- `cancer-discovery`
- `ca-a-cancer-journal-for-clinicians`
- `molecular-psychiatry`

Boundary notes: `blood` and `cancer-discovery` also seed category 5. Their primary split here is
category 6 because the expansion plan treats specialty clinical and translational journals as a
medicine-and-health lane.

### Category 7 - Engineering and Technology (6)

Materials, energy, and robotics:

- `nature-materials`
- `advanced-materials`
- `nature-energy`
- `joule`
- `energy-and-environmental-science`
- `science-robotics`

Boundary notes: `science-robotics` can also seed category 8 when treated as a CS/AI venue, but its
primary expansion-home here is engineering and robotics.

### Category 8 - Computer Science and AI (3)

- `nature-machine-intelligence`
- `ieee-transactions-on-pattern-analysis-and-machine-intelligence`
- `journal-of-machine-learning-research`

### Category 9 - Agriculture and Environment (5)

- `nature-geoscience`
- `nature-climate-change`
- `nature-sustainability`
- `environmental-science-and-technology`
- `one-earth`

### Router

- `en-natsci-journal-workflow` - infrastructure, not counted as a venue profile or depth-pack seed.

## Computer Science Conference Breadth Split

Source roster: `Computer-Science-Conference-Skills/resources/conference-roster.md`.

All 155 conference profiles map to category 8. The subarea split below is for sequencing later
one-conference-one-depth-pack work. It preserves the AI-first ordering requested for the CS lane.

### AI / ML Core, Learning Theory, ML Systems, Health AI, Regional AI (16)

- `neural-information-processing-systems`
- `international-conference-on-machine-learning`
- `international-conference-on-learning-representations`
- `aaai-conference-on-artificial-intelligence`
- `international-joint-conference-on-artificial-intelligence`
- `artificial-intelligence-and-statistics`
- `uncertainty-in-artificial-intelligence`
- `conference-on-learning-theory`
- `conference-on-machine-learning-and-systems`
- `conference-on-lifelong-learning-agents`
- `international-conference-on-automated-machine-learning`
- `conference-on-health-inference-and-learning`
- `machine-learning-for-health`
- `asian-conference-on-machine-learning`
- `international-conference-on-discovery-science`
- `european-conference-on-artificial-intelligence`

### Data Mining, Web, Knowledge, Recommenders, and IR (16)

- `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining`
- `ieee-international-conference-on-data-mining`
- `siam-international-conference-on-data-mining`
- `european-conference-on-machine-learning-and-principles-and-practice-of-knowledge-discovery`
- `acm-conference-on-recommender-systems`
- `the-web-conference`
- `acm-international-conference-on-web-search-and-data-mining`
- `acm-international-conference-on-information-and-knowledge-management`
- `international-semantic-web-conference`
- `international-conference-on-knowledge-capture`
- `acm-sigir-conference-on-research-and-development-in-information-retrieval`
- `european-conference-on-information-retrieval`
- `acm-sigir-conference-on-human-information-interaction-and-retrieval`
- `acm-ieee-joint-conference-on-digital-libraries`
- `conference-and-labs-of-the-evaluation-forum`
- `text-retrieval-conference`

### Planning, Reasoning, Agents, Constraints, and Responsible AI (9)

- `international-conference-on-automated-planning-and-scheduling`
- `international-conference-on-principles-of-knowledge-representation-and-reasoning`
- `international-conference-on-autonomous-agents-and-multiagent-systems`
- `international-conference-on-principles-and-practice-of-constraint-programming`
- `international-conference-on-theory-and-applications-of-satisfiability-testing`
- `integration-of-constraint-programming-artificial-intelligence-and-operations-research`
- `aaai-acm-conference-on-ai-ethics-and-society`
- `acm-conference-on-fairness-accountability-and-transparency`
- `aaai-conference-on-human-computation-and-crowdsourcing`

### Computer Vision, Medical Imaging, Multimedia, Graphics, and XR (20)

- `computer-vision-and-pattern-recognition`
- `international-conference-on-computer-vision`
- `european-conference-on-computer-vision`
- `winter-conference-on-applications-of-computer-vision`
- `asian-conference-on-computer-vision`
- `british-machine-vision-conference`
- `international-conference-on-pattern-recognition`
- `international-conference-on-3d-vision`
- `medical-image-computing-and-computer-assisted-intervention`
- `ieee-international-symposium-on-biomedical-imaging`
- `acm-international-conference-on-multimedia`
- `acm-international-conference-on-multimedia-retrieval`
- `acm-siggraph`
- `acm-siggraph-asia`
- `eurographics`
- `acm-siggraph-eurographics-symposium-on-computer-animation`
- `ieee-international-symposium-on-mixed-and-augmented-reality`
- `ieee-conference-on-virtual-reality-and-3d-user-interfaces`
- `pacific-graphics`
- `acm-siggraph-symposium-on-interactive-3d-graphics-and-games`

### NLP and Speech (14)

- `annual-meeting-of-the-association-for-computational-linguistics`
- `conference-on-empirical-methods-in-natural-language-processing`
- `north-american-chapter-of-the-association-for-computational-linguistics`
- `european-chapter-of-the-association-for-computational-linguistics`
- `international-conference-on-computational-linguistics`
- `conference-on-computational-natural-language-learning`
- `international-natural-language-generation-conference`
- `sigdial-conference-on-discourse-and-dialogue`
- `joint-international-conference-on-computational-linguistics-language-resources-and-evaluation`
- `starsem-conference-on-computational-semantics`
- `interspeech`
- `ieee-international-conference-on-acoustics-speech-and-signal-processing`
- `ieee-automatic-speech-recognition-and-understanding-workshop`
- `ieee-spoken-language-technology-workshop`

### Robotics and Automation (12)

- `ieee-international-conference-on-robotics-and-automation`
- `ieee-rsj-international-conference-on-intelligent-robots-and-systems`
- `robotics-science-and-systems`
- `conference-on-robot-learning`
- `acm-ieee-international-conference-on-human-robot-interaction`
- `ieee-international-conference-on-robot-and-human-interactive-communication`
- `ieee-international-conference-on-automation-science-and-engineering`
- `international-symposium-on-robotics-research`
- `international-symposium-on-experimental-robotics`
- `robocup`
- `ieee-ras-international-conference-on-humanoid-robots`
- `international-symposium-on-distributed-autonomous-robotic-systems`

### HCI, Visualization, Accessibility, and Interactive Systems (15)

- `acm-chi-conference-on-human-factors-in-computing-systems`
- `acm-symposium-on-user-interface-software-and-technology`
- `acm-conference-on-computer-supported-cooperative-work-and-social-computing`
- `acm-conference-on-designing-interactive-systems`
- `acm-conference-on-intelligent-user-interfaces`
- `acm-international-joint-conference-on-pervasive-and-ubiquitous-computing`
- `acm-international-conference-on-mobile-human-computer-interaction`
- `acm-international-conference-on-tangible-embedded-and-embodied-interaction`
- `acm-sigaccess-conference-on-computers-and-accessibility`
- `international-conference-on-advanced-visual-interfaces`
- `ieee-visualization-conference`
- `eurovis`
- `ieee-pacific-visualization-symposium`
- `acm-interactive-surfaces-and-spaces`
- `acm-symposium-on-virtual-reality-software-and-technology`

### Systems, Networking, Architecture, HPC, and Performance (20)

- `acm-symposium-on-operating-systems-principles`
- `usenix-symposium-on-operating-systems-design-and-implementation`
- `usenix-symposium-on-networked-systems-design-and-implementation`
- `acm-sigcomm`
- `acm-mobicom`
- `acm-mobisys`
- `acm-conext`
- `ieee-infocom`
- `eurosys`
- `usenix-annual-technical-conference`
- `usenix-conference-on-file-and-storage-technologies`
- `architectural-support-for-programming-languages-and-operating-systems`
- `international-symposium-on-computer-architecture`
- `ieee-acm-international-symposium-on-microarchitecture`
- `ieee-international-symposium-on-high-performance-computer-architecture`
- `international-conference-for-high-performance-computing-networking-storage-and-analysis`
- `acm-sigplan-symposium-on-principles-and-practice-of-parallel-programming`
- `acm-international-symposium-on-high-performance-parallel-and-distributed-computing`
- `acm-sigmetrics`
- `acm-workshop-on-hot-topics-in-networks`

### Security, Privacy, and Cryptography (12)

- `ieee-symposium-on-security-and-privacy`
- `usenix-security-symposium`
- `acm-conference-on-computer-and-communications-security`
- `network-and-distributed-system-security-symposium`
- `privacy-enhancing-technologies-symposium`
- `international-symposium-on-research-in-attacks-intrusions-and-defenses`
- `annual-computer-security-applications-conference`
- `european-symposium-on-research-in-computer-security`
- `acm-asia-conference-on-computer-and-communications-security`
- `acm-conference-on-security-and-privacy-in-wireless-and-mobile-networks`
- `iacr-conference-on-cryptographic-hardware-and-embedded-systems`
- `financial-cryptography-and-data-security`

### Software Engineering, Programming Languages, and Formal Methods (16)

- `international-conference-on-software-engineering`
- `acm-international-conference-on-the-foundations-of-software-engineering`
- `ieee-acm-international-conference-on-automated-software-engineering`
- `acm-sigsoft-international-symposium-on-software-testing-and-analysis`
- `mining-software-repositories`
- `ieee-international-conference-on-software-maintenance-and-evolution`
- `ieee-international-conference-on-software-analysis-evolution-and-reengineering`
- `international-symposium-on-empirical-software-engineering-and-measurement`
- `ieee-international-requirements-engineering-conference`
- `acm-ieee-international-conference-on-model-driven-engineering-languages-and-systems`
- `acm-sigplan-conference-on-programming-language-design-and-implementation`
- `acm-sigplan-symposium-on-principles-of-programming-languages`
- `acm-sigplan-conference-on-object-oriented-programming-systems-languages-and-applications`
- `acm-sigplan-international-conference-on-functional-programming`
- `international-conference-on-computer-aided-verification`
- `acm-ieee-symposium-on-logic-in-computer-science`

### Databases (3)

- `acm-sigmod-international-conference-on-management-of-data`
- `international-conference-on-very-large-data-bases`
- `ieee-international-conference-on-data-engineering`

### Theory (2)

- `acm-symposium-on-theory-of-computing`
- `ieee-symposium-on-foundations-of-computer-science`

### Router

- `cs-ai-conference-workflow` - infrastructure, not counted as a venue profile or depth-pack seed.

## Follow-up For Build Queues

- `JOURNAL-MASTER-LIST.md` now reserves `[A-depth]` for complete reusable depth assets.
- Natural-science breadth seeds above should not be counted as complete packs unless a matching
  depth pack root already exists.
- CS conference breadth seeds above should drive the category-8 build sequence, with NeurIPS,
  ICML, ICLR, AAAI, IJCAI, AISTATS, UAI, COLT, MLSys, KDD, CVPR, ACL, EMNLP, SIGIR, ICRA, CHI,
  SOSP/OSDI, S&P, CCS, ICSE, PLDI, SIGMOD, STOC, and FOCS treated as early depth-pack candidates.
