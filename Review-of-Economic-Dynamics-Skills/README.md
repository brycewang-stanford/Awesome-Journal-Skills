# Review of Economic Dynamics — Agent Skill Pack (`red-skills`)

An opinionated, venue-specific stack of twelve Claude agent skills for authors targeting the
**Review of Economic Dynamics (RED)** — the journal of the **Society for Economic Dynamics (SED)**,
published by **Elsevier** (ISSN 1094-2025, quarterly, since 1998).

RED's scope is defined by **method and lens rather than subfield**: dynamic, quantitative economics —
dynamic general-equilibrium models, growth, business cycles, labor, monetary and fiscal policy, and
international macro — studied through **theoretical, computational, or empirical dynamic models**.
Heavily computational quantitative-macro work is squarely in scope. These skills encode RED's actual
norms so a manuscript clears the desk screen and respects the journal's code-first replication culture.

## What makes RED distinctive (and why this pack exists)

- **A real per-submission fee.** The current Elsevier Guide lists USD **195** standard; USD **100** if
  all coauthors are full-time students at submission; **waived for second-and-later resubmissions**. The
  review process does not begin until the fee is received — unusual versus most top general-interest
  economics journals.
- **Run by a scholarly community, not a generalist masthead.** The SED — the macro/dynamics community
  behind the SED Annual Meetings — owns the journal.
- **Code-first replication.** A dedicated *Availability of Data and Computer Code* policy covers
  **computational as well as empirical** papers; archives are posted on the RED site and indexed as a
  citable **RePEc "Computer Codes"** series. README requirements are specific (software/OS, execution
  order, expected runtime, random seeds).
- **Fast-review orientation.** The current reviewer page asks reviewers to notify the editor if they
  cannot act within six weeks, and older SED newsletters report fast first-decision performance; treat
  timing as guidance, not a promised clock.
- **Single-anonymized review** (not double-blind), with a **minimum of two referees** after an editor desk screen.
- Coordinating Editor: **Loukas Karabarbounis** (University of Minnesota / Minneapolis Fed).

## The twelve skills

| Skill | Role |
| --- | --- |
| `red-workflow` | End-to-end map of the RED manuscript lifecycle |
| `red-topic-selection` | Is the question dynamic/quantitative and in-scope for RED? |
| `red-literature-positioning` | Position against the dynamic-economics and SED literature |
| `red-identification-strategy` | Model assumptions / regularity conditions / causal design per paper type |
| `red-data-analysis` | Calibration, moment-matching, estimation, numerical solution discipline |
| `red-contribution-framing` | Frame the marginal quantitative/dynamic contribution |
| `red-tables-figures` | IRFs, moment tables, calibration tables, model-vs-data exhibits |
| `red-writing-style` | RED house style; author-year references; ≤250-word abstract |
| `red-replication-and-data-policy` | The Data/Code archive, readme.txt, .zip/.gz to the code editor, RePEc indexing |
| `red-review-process` | Desk screen, single-anonymized refereeing, live timing expectations |
| `red-submission` | Pre-submission preflight: fee, ScienceDirect/Editorial Manager, keywords, AI declaration |
| `red-rebuttal` | Response-to-referees strategy after a revise-and-resubmit |

## Install / use

This repository is a Claude Code plugin. The skills live under `skills/red-<role>/SKILL.md` and are
declared in `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`. Point your Claude Code
marketplace at this directory and enable the `red-skills` plugin, then invoke a skill by name.

## Sourcing & honesty

Every venue-specific fact traces to an official SED/Elsevier page in
[`resources/official-source-map.md`](resources/official-source-map.md) (accessed 2026-06-20). The source
map records the active Elsevier Guide fee, the older SED fee text, the optional OA APC price-list entry,
the single-anonymized review model, and the overlapping SED/Elsevier data-policy requirements so the
skills do not rely on stale scraper notes.

## License

MIT — see [`LICENSE`](LICENSE).
