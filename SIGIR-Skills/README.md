# SIGIR Skills

Twelve agent skills for papers targeting **SIGIR — the International ACM SIGIR
Conference on Research and Development in Information Retrieval** — the flagship
venue for search, ranking, recommendation, and retrieval evaluation. The pack is
organized around four structural facts that make SIGIR strategy different from
generic ML-conference advice:

1. **A multi-track submission system, not one CFP.** SIGIR 2026 fields Full, Short,
   Perspectives, Resources, Reproducibility, Industry, and Low Resource Environments
   tracks, each with its own page (and in the Resources case, its own
   *single-anonymous* review regime). Routing a contribution to the right track is a
   first-class decision.
2. **No appendix escape hatch.** Full papers get 9 pages and short papers 4, with
   only references excluded — appendices count inside the budget, so overflow lives
   in the cited repository or dies.
3. **TREC-lineage evaluation culture.** Reviewers audit collection choice, baseline
   tuning symmetry, metric-cutoff discipline, and paired significance testing before
   they weigh novelty; "significantly" is a reserved word.
4. **ACM production.** Proceedings go through e-rights and TAPS into the ACM Digital
   Library (SIGIR 2025 volume: DOI 10.1145/3726302), with CCS concepts and metadata
   that outlive the conference.

Official basis checked on **2026-07-08**: the SIGIR 2026 site (49th edition, July
20-24, 2026, Melbourne | Naarm, Australia), its per-track submission pages and
cross-track policy page, the SIGIR OpenReview venue groups, the ACM DL proceedings
record, sigir.org, and the SIGIR 2025 CFP as the previous-cycle anchor. The exact
source list — including the access-method note (several official domains were only
reachable through search renderings) and every fact left 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## Verified 2026-cycle anchors

| Fact | 2026 value | Volatility |
|---|---|---|
| Edition | 49th International ACM SIGIR Conference, July 20-24, 2026, Melbourne \| Naarm, Australia | Per edition |
| Full papers | ≤ 9 pages excluding references; appendices inside the budget; double-blind | Per cycle |
| Short papers | ≤ 4 pages excluding references; separate OpenReview group | Per cycle |
| Resources track | ≤ 6 pages + refs; **single-anonymous**; abstract Feb 5 → notify Apr 2 → camera-ready Apr 29, 2026 | Per cycle |
| Reproducibility | Own track in 2026 (split from the former combined track) | Per cycle |
| Template | ACM Primary Article Template (`sigconf` LaTeX / Word Interim) | Per cycle |
| PC duty | Full-paper submissions nominate one author as a PC member | Per cycle |
| Platform | OpenReview, per-track venue groups | Per cycle |
| Policy | ACM authorship + AI-use disclosure; parallel submission desk-rejected; cross-track double submission banned | Per cycle |
| Publication | ACM Digital Library via e-rights + TAPS | Per year |

Full/short submission deadlines for 2026 (trackers reported abstract Jan 15 / paper
Jan 22, 2026 AoE, matching the 2025 pattern), rebuttal mechanics, camera-ready page
allowances, chair names, and fees could not be verified live and are flagged 待核实
in the source map rather than asserted.

## Skills

Routing and planning:

- [`sigir-topic-selection`](skills/sigir-topic-selection/SKILL.md) — the two tests:
  does the contribution survive an oracle-retrieval swap (if yes, it isn't IR), and
  which track owns the strongest honest claim; neighbor routing to ECIR, CIKM, WSDM,
  CHIIR, ICTIR, RecSys, TheWebConf, and NLP/ML venues.
- [`sigir-workflow`](skills/sigir-workflow/SKILL.md) — the January-deadline annual
  rhythm, backward planning to the two-stage abstract/paper gate, multi-track
  coordination under the cross-track ban, and the SIGIR→CIKM→SIGIR-AP→WSDM→ECIR
  fallback ring.

Building the paper:

- [`sigir-writing-style`](skills/sigir-writing-style/SKILL.md) — the IR register:
  task-and-regime-first openings, mechanism-stated failures, calibrated evidence
  previews, reserved-word discipline, table-centric argumentation.
- [`sigir-related-work`](skills/sigir-related-work/SKILL.md) — lineage fluency from
  Ponte & Croft to ColBERT, the mechanized delta sentence, venue-misattribution
  guards, and arXiv-era concurrent-work handling.
- [`sigir-experiments`](skills/sigir-experiments/SKILL.md) — claim-to-collection
  matching, metric-cutoff discipline, the paired-test-with-correction house
  protocol, baseline tuning symmetry, ablations, and LLM-era pitfalls
  (contamination, LLM-as-judge validation, prompt variance).
- [`sigir-reproducibility`](skills/sigir-reproducibility/SKILL.md) — the seven
  drift sources of IR results and how to pin each with an artifact; plus how to
  write a Reproducibility-track study whose contribution is the divergence analysis.

Packaging and submitting:

- [`sigir-artifact-evaluation`](skills/sigir-artifact-evaluation/SKILL.md) — the
  run-file + qrels + index-recipe artifact standard, the Resources-vs-in-paper
  routing decision, judgment documentation, and dual anonymity packaging.
- [`sigir-supplementary`](skills/sigir-supplementary/SKILL.md) — the three-container
  model (budget pages / free references / cited repository) under SIGIR's
  no-appendix rule, and the review-criticality ranking that decides what stays.
- [`sigir-submission`](skills/sigir-submission/SKILL.md) — the pre-upload audit:
  full-vs-short format table, IR-specific anonymization (system names, leaderboards,
  query logs), policy gates, desk-reject triage, final-week sequence.

Review phase and after:

- [`sigir-review-process`](skills/sigir-review-process/SKILL.md) — per-track
  machinery, what IR reviewers score (evaluation validity above novelty), the four
  reviewer archetypes, and decision-packet triage.
- [`sigir-author-response`](skills/sigir-author-response/SKILL.md) — responding when
  a channel exists, pre-empting when it doesn't, and the post-rejection routing
  playbook including SIGIR-AP's advertised revise-and-resubmit route.
- [`sigir-camera-ready`](skills/sigir-camera-ready/SKILL.md) — e-rights, TAPS,
  alias-unwinding, CCS concepts and DL metadata, artifact publication, and the
  April-to-July production runway.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — every
  source URL with access date, verified facts, the access-method disclosure, and
  the 待核实 register.
- [`resources/external_tools.md`](resources/external_tools.md) — per-track pages,
  OpenReview groups, ACM authoring pipeline, and the IR tooling stack.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — six
  DOI-verified SIGIR exemplars spanning 1998-2020 plus the misattribution guard list.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional before/after rewrite into the SIGIR first-page arc.
- [`resources/code/README.md`](resources/code/README.md) — IR-specific adapter over
  the shared ML-conference reproducibility kit.

## Suggested sequence

1. **Route**: `sigir-topic-selection` (track fork), then `sigir-workflow` (calendar).
2. **Build**: `sigir-experiments` + `sigir-reproducibility` while writing with
   `sigir-writing-style` and `sigir-related-work`.
3. **Package**: `sigir-artifact-evaluation` and `sigir-supplementary` well before
   deadline week; then the `sigir-submission` audit.
4. **Review phase**: `sigir-review-process` to read the machine,
   `sigir-author-response` to answer it (or to pre-empt it at writing time).
5. **Publish**: `sigir-camera-ready` on acceptance; on rejection, back to
   `sigir-workflow`'s fallback ring.

## Installation

The pack ships as a Claude Code plugin. From this repository:

```bash
claude plugin marketplace add ./SIGIR-Skills
claude plugin install sigir-skills
```

Or point an agent at individual `skills/sigir-*/SKILL.md` files — each is
self-contained, declares its scope in the frontmatter, and ends with a structured
output block so results compose.

## Scope and disclaimers

- The pack advises on strategy, structure, and evidence for SIGIR submissions. It is
  not the CFP: where anything here conflicts with the current track pages, the
  official pages win, always.
- Facts are dated 2026-07-08 and phrased as cycle anchors. SIGIR restructured its
  own track lineup between 2025 and 2026 (Resource & Reproducibility split) — assume
  it can again.
- Facts marked 待核实 (deadlines, rebuttal mechanics, fees, chairs, camera-ready
  allowances) must be verified live before being stated to an author as fact.
- No text here should be pasted into a paper; the worked example is fictional by
  design and the exemplar library records positioning patterns, not reusable prose.

## Maintenance notes

- Reopen the per-track pages (not a remembered "SIGIR CFP") before deadline-sensitive
  advice; SIGIR's rules are track-scoped by construction.
- After each edition, refresh: edition number/venue, track lineup, page budgets,
  anonymity regimes per track, OpenReview group ids, and the ACM Open status note.
- SIGIR 2027 is the 50th edition and an Americas year per the SIG's rotation —
  expect anniversary-cycle changes and verify everything.
