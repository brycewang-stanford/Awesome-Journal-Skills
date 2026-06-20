# Conference-Selection Patterns

These patterns distinguish sibling venues. They are routing exemplars, not
publication examples.

## AI / ML

- NeurIPS: broad ML/AI contribution, strong evaluation, field-wide interest.
- ICML: machine-learning method or theory with careful baselines and ablations.
- ICLR: representation learning, deep learning, and open-review discourse fit.
- AISTATS/UAI/COLT: statistical, uncertainty, or learning-theory contribution.
- MLSys: ML systems and infrastructure contribution, not merely a large model.
- CoLLAs vs AutoML: CoLLAs needs continual/lifelong adaptation as the research
  object; AutoML needs the automation/search/meta-learning machinery itself to
  be the object. Do not route a generic ML benchmark to either only because the
  model was trained repeatedly.

## Vision, NLP, And Data

- CVPR/ICCV/ECCV: computer-vision contribution; avoid submitting only a generic
  ML method with images as examples.
- WACV vs ACCV vs BMVC vs 3DV: WACV is application-facing vision with a strong
  winter-cycle community; ACCV/BMVC are regional vision venues; 3DV needs the
  three-dimensional geometry, reconstruction, pose, scene, or spatial perception
  claim to be central rather than a visual example.
- ACL/EMNLP/NAACL/EACL: NLP contribution; distinguish method, resource,
  analysis, and regional chapter timing.
- NAACL vs EACL: both are ACL-family regional chapters; choose by cycle,
  community, and empirical setting, not by topic labels alone. Do not sell EACL
  as a fallback NAACL or vice versa without checking the current CFP and
  chapter-specific tracks.
- INLG vs *SEM vs SIGDIAL: INLG needs generation as the object; *SEM needs
  computational semantics; SIGDIAL needs dialogue/discourse interaction. A
  language-model paper must name which of these phenomena is actually advanced.
- KDD/ICDM/SDM: data mining contribution; distinguish applied discovery,
  algorithmic mining, and mathematical/statistical rigor.
- ICDM vs SDM: ICDM can own broad IEEE data-mining methodology and applications;
  SDM expects SIAM-style mathematical, statistical, or algorithmic discipline.
  If the main claim is business impact or deployed discovery, compare KDD too.
- SIGMOD/VLDB/ICDE: database contribution; distinguish data-management systems,
  query processing, and engineering scale.
- SIGMOD vs VLDB: SIGMOD is the ACM database-systems flagship; VLDB/PVLDB has
  its own proceedings-journal mechanics. ICDE is broader IEEE data engineering.
  Submission mechanics can decide the target even when the technical scope is
  similar.

## Robotics, HCI, Systems, Security

- ICRA/IROS/RSS/CoRL: decide whether the main novelty is robotics system,
  embodied learning, experimental result, or research agenda.
- ICRA vs IROS vs RSS: ICRA usually needs robotics/automation breadth with
  task, system, and hardware/simulation credibility; IROS leans intelligent
  robot systems and integrated validation; RSS is narrower and more selective
  around robotics science, abstraction, and deep experimental/theoretical
  insight. Compare CoRL only when robot learning is the main novelty.
- CASE vs RO-MAN vs HRI: CASE owns automation science and engineering systems;
  RO-MAN owns robot-human communication; HRI owns human-robot interaction with
  study design and human evidence. Do not send a human-subjects robot paper to
  CASE unless the automation system is the contribution.
- Humanoids vs RoboCup: Humanoids needs humanoid embodiment, locomotion,
  manipulation, or human-like robot capability. RoboCup needs competition,
  benchmark, multi-agent, soccer/rescue/service-robot, or challenge-driven
  evidence.
- CHI/UIST/CSCW/IUI/VIS: decide whether interaction, user evidence, UI systems,
  social computing, intelligent interface, or visualization is central.
- TEI vs UbiComp vs ASSETS: TEI owns tangible/embodied interaction; UbiComp owns
  pervasive sensing and everyday computing; ASSETS owns accessibility and
  disability-centered computing. The user population and interaction substrate
  should decide, not the presence of a prototype.
- IEEE VIS vs EuroVis vs PacificVis: IEEE VIS is the broad flagship for
  visualization research; EuroVis and PacificVis can be better when the work is
  tuned to those regional communities or cycles. If the claim is graphics
  rendering rather than analytic visualization, compare SIGGRAPH/Eurographics.
- SOSP/OSDI/NSDI/SIGCOMM/ASPLOS/ISCA: systems venue choice follows artifact,
  workload, and architecture/networking scope.
- SOSP/OSDI vs NSDI: SOSP/OSDI own operating systems and systems design;
  NSDI owns networked systems. If the artifact is a distributed service but the
  bottleneck is network protocol behavior, compare NSDI/SIGCOMM before OSDI.
- SIGCOMM vs CoNEXT vs INFOCOM vs EuroSys: SIGCOMM is the networking flagship;
  CoNEXT is networking systems and emerging network research; INFOCOM is IEEE
  networking breadth; EuroSys is systems with European cycle/community fit. A
  routing, transport, or measurement paper must name the community whose
  baselines it beats.
- ISCA vs HPCA vs MICRO vs ASPLOS: ISCA and HPCA own architecture, MICRO owns
  microarchitecture, and ASPLOS needs a systems/architecture/PL intersection.
  Do not route a hardware-performance paper to ASPLOS without a software or
  systems interface.
- MobiCom vs MobiSys: MobiCom owns mobile networking and wireless/mobile
  communication; MobiSys owns mobile systems, sensing platforms, and deployed
  mobile computing artifacts.
- S&P/USENIX Security/CCS/NDSS: security venue choice follows threat model,
  attack/defense evidence, ethics, and community scope.
- S&P vs CCS vs USENIX Security vs NDSS: S&P is the IEEE security flagship,
  CCS is ACM security breadth, USENIX Security often rewards systems artifacts
  and measurement, and NDSS emphasizes network/distributed-system security. The
  threat model and artifact shape should choose the target.
- ESORICS vs PETS vs ACSAC: ESORICS is broad European security research; PETS
  needs privacy-enhancing technology as the core; ACSAC needs applied security
  relevance. Do not route a privacy paper to ESORICS until PETS has been
  considered.

## SE / PL / Theory

- ICSE/FSE: broad software-engineering contribution.
- ASE: automated software engineering and tool automation.
- ISSTA: testing, analysis, and defect-detection evidence.
- SANER/ICSME: software analysis/evolution/reengineering versus maintenance
  history and practice.
- ICSE/FSE vs ASE vs RE: ICSE/FSE own broad software-engineering claims; ASE
  needs automation as the contribution; RE needs requirements engineering,
  stakeholder intent, specification, or requirements process as the object.
- PLDI/POPL/OOPSLA/ICFP/CAV/LICS: programming-language and formal-methods
  target follows theorem, implementation, verification, or language-design
  contribution.
- STOC vs FOCS: both are theory flagships; route by cycle, community, and
  whether the proof speaks to the TCS conversation currently active in that CFP.
  The paper needs theorem novelty and proof architecture, not only algorithmic
  engineering.

## Clone-Audit Triage Notes (2026-06-20)

The clone audit intentionally reports breadth-profile similarities at 0.75+ so
agents can spot routing drift. Treat the following as current triage rules:

- STOC/FOCS and PLDI/POPL are expected high-similarity sibling pairs. Keep the
  shared fit-card skeleton, but require theorem/proof or PL-mechanism language
  in the actual recommendation.
- CHIL is not a generic ML venue: it needs health inference, clinical data,
  health-policy relevance, or patient-care validity. Do not route CHIL-shaped
  language to CPAIOR, KDD, CSCW, FAccT, or ECML PKDD without the corresponding
  constraint-programming, data-mining, social-computing, fairness, or European
  ML community evidence.
- CPAIOR owns constraint programming, AI planning/optimization, and operations
  research integration. If the paper is mainly data mining, human information
  interaction, or statistical ML, compare KDD/CHIIR/AISTATS instead.
- RecSys owns recommender modeling and user-item evaluation. Do not send a
  recommender workload to SOSP, HotNets, MICRO, or other systems venues unless
  the contribution is a deployed system, protocol, hardware mechanism, or
  networked-systems artifact.
- ICDE, K-CAP, ISWC, and ICPR are separate despite shared "data/knowledge"
  vocabulary: ICDE is data engineering, K-CAP is knowledge acquisition, ISWC is
  semantic web, and ICPR is pattern recognition.
- VRST/IEEE VR/ISMAR/I3D/SIGGRAPH should be separated by immersive interaction,
  mixed-reality tracking, interactive 3D systems, and graphics/animation
  contribution. Do not route by "visual" examples alone.
