---
name: cs-ai-conference-workflow
description: Use when deciding which computer-science or AI conference skill to invoke next, comparing fit across the 155-conference CS roadmap, or routing an AI/ML/CS manuscript before venue-specific re-framing.
---

# CS/AI conference workflow (cs-ai-conference-workflow)

## Purpose

This is the router for the computer-science conference pack. It puts AI conferences first, then routes by contribution type across ML, data mining, vision, NLP, robotics, HCI, systems, security, software engineering, programming languages, databases, and theory. It does not replace a single-conference profile; it selects the right profile and forces an official-cycle check before submission.

## Resources to Load When Needed

- If the target conference family is unclear, read `../../resources/worked-examples/venue-routing.md`.
- If two sibling conferences look plausible, read `../../resources/exemplars/selection-patterns.md`.
  This file now carries the high-confusion sibling contrasts surfaced by clone-audit review
  (robotics, graphics/vision, NLP chapters, systems/networking, security, SE/PL/theory).
- Before submission-ready advice, use `../../resources/conference-roster.md` and
  `../../resources/official-source-map.md` to open the current official CFP,
  author kit, and submission policy for the chosen conference.

## Ask six things first

1. **Contribution type:** algorithm, theory, system, dataset, benchmark, empirical study, user study, security finding, programming-language result, database system, or application.
2. **Evidence shape:** proof, benchmark, ablation, artifact, deployment, user study, field study, exploit/defense, theorem, or system measurement.
3. **Audience:** broad AI, subfield specialists, systems builders, security reviewers, HCI/design researchers, theory community, or domain users.
4. **Review constraints:** double-blind/anonymity, OpenReview visibility, rebuttal length, artifact policy, ethics, AI-use disclosure, and supplementary-material rules.
5. **Cycle risk:** deadline, page limit, author registration, conflict declarations, dual-submission policy, and camera-ready obligations.
6. **Fallback path:** sibling conference, journal, workshop, findings track, or arXiv-only revision.

## Quick routing

| Manuscript signature | Prefer skills |
|---|---|
| AI/ML first | `neural-information-processing-systems` / `international-conference-on-machine-learning` / `international-conference-on-learning-representations` / `aaai-conference-on-artificial-intelligence` / `international-joint-conference-on-artificial-intelligence` |
| Data mining and web AI | `acm-sigkdd-conference-on-knowledge-discovery-and-data-mining` / `the-web-conference` / `acm-international-conference-on-web-search-and-data-mining` / `acm-conference-on-recommender-systems` |
| Vision and multimodal media | `computer-vision-and-pattern-recognition` / `international-conference-on-computer-vision` / `european-conference-on-computer-vision` / `acm-international-conference-on-multimedia` |
| NLP, speech, and IR | `annual-meeting-of-the-association-for-computational-linguistics` / `conference-on-empirical-methods-in-natural-language-processing` / `interspeech` / `acm-sigir-conference-on-research-and-development-in-information-retrieval` |
| Robotics and embodied AI | `ieee-international-conference-on-robotics-and-automation` / `ieee-rsj-international-conference-on-intelligent-robots-and-systems` / `robotics-science-and-systems` / `conference-on-robot-learning` |
| HCI and visualization | `acm-chi-conference-on-human-factors-in-computing-systems` / `acm-symposium-on-user-interface-software-and-technology` / `acm-conference-on-computer-supported-cooperative-work-and-social-computing` / `ieee-visualization-conference` |
| Systems, networking, architecture, and HPC | `acm-symposium-on-operating-systems-principles` / `usenix-symposium-on-operating-systems-design-and-implementation` / `acm-sigcomm` / `international-symposium-on-computer-architecture` |
| Security and privacy | `ieee-symposium-on-security-and-privacy` / `usenix-security-symposium` / `acm-conference-on-computer-and-communications-security` / `network-and-distributed-system-security-symposium` |
| Software engineering, PL, and formal methods | `international-conference-on-software-engineering` / `acm-international-conference-on-the-foundations-of-software-engineering` / `acm-sigplan-conference-on-programming-language-design-and-implementation` / `acm-sigplan-symposium-on-principles-of-programming-languages` |
| Databases and theory | `acm-sigmod-international-conference-on-management-of-data` / `international-conference-on-very-large-data-bases` / `acm-symposium-on-theory-of-computing` / `ieee-symposium-on-foundations-of-computer-science` |

## Sibling-Conference Disambiguation

| Confusable targets | Decision rule |
|---|---|
| NeurIPS vs ICML vs ICLR | Use NeurIPS for broad ML/AI reach, ICML for machine-learning method/theory discipline, and ICLR for representation/deep-learning/open-review fit. |
| KDD vs ICDM vs SDM | KDD leans data-mining impact and applied discovery, ICDM broad IEEE data-mining methods, SDM mathematical/statistical data-mining rigor. |
| CVPR vs ICCV vs ECCV | All require a vision contribution; current cycle, scope, and reviewer community decide, not acronym prestige alone. |
| ACL/EMNLP vs NAACL/EACL | Separate core NLP method, empirical analysis, resource construction, and chapter-cycle fit before choosing. |
| CHI vs UIST vs CSCW vs IUI vs VIS | User study, UI systems, social computing, intelligent-interface, and visualization claims need different evidence. |
| S&P vs USENIX Security vs CCS vs NDSS | Pick by threat model, attack/defense evidence, ethics posture, systems/security community, and current CFP scope. |
| ICSE/FSE vs ASE vs ISSTA vs SANER/ICSME | Broad SE, automation, testing/analysis, reengineering, and maintenance-history papers are not interchangeable. |
| SIGMOD vs VLDB vs ICDE | Data-management systems, PVLDB-style database research, and IEEE data-engineering work have different submission mechanics; verify the current cycle. |

## Decision rules

- **AI first:** if the manuscript is fundamentally about machine learning, language, vision, data mining, agents, or responsible AI, start in the AI/ML rows before considering general CS venues.
- **Contribution type beats prestige:** a theorem paper belongs in COLT/STOC/FOCS/LICS-style venues; a built system belongs in SOSP/OSDI/NSDI/SIGCOMM/ASPLOS-style venues; a user-facing AI interface belongs in CHI/IUI/CSCW rather than only NeurIPS.
- **Evidence must match venue culture:** top AI wants strong baselines and ablations; systems wants artifacts and workloads; security wants threat models and ethics; HCI wants study design and participant context; theory wants complete proofs.
- **Official-cycle requirements are volatile:** always invoke the single-conference skill and re-check the current CFP/author kit before advising submission.
- **These are conferences, not journals (verified 2026-06-22):** no venue here has a standing editor-in-chief — its leadership is the per-edition Program/General Chairs, who rotate yearly, so look them up on the current-cycle committees page rather than assuming a name. None charges an article-processing fee; the cost model is registration plus open-access proceedings (PMLR, OpenReview, ACM/IEEE DL). Treat any "fee" question as a registration or narrow extra-page/submission-volume question, not a journal APC.
- **Rebuttal posture matters:** prepare concise, evidence-based responses and never reveal identity or add new off-policy material during author response.

## Output format

```text
[Top conference skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <venue> (one-line mismatch reason)
[Biggest current gap] novelty / evidence / proof / artifact / user study / ethics / format / official requirements
[Next step] invoke <skill-name> for single-venue fit and current-cycle checks
```
