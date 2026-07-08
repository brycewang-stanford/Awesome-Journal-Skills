# PLDI Skills

Twelve agent skills for papers targeting **PLDI — the ACM SIGPLAN Conference on
Programming Language Design and Implementation**, the SIGPLAN flagship for
language design, compilers, program analysis, runtimes, synthesis, and
verification tooling. The pack covers a full PLDI campaign: deciding whether the
decisive evidence is really an implementation-and-benchmarks story, building an
evaluation that satisfies SIGPLAN's own Empirical Evaluation Guidelines,
surviving the double-blind HotCRP submission and the short February author
response, publishing the accepted paper as a **PACMPL Issue PLDI** journal
article, and earning the Functional / Reusable / Available badges through
post-acceptance artifact evaluation on Zenodo.

Official basis checked on **2026-07-08**: the PLDI 2026 Call for Papers (47th
edition), the pldi26.sigplan.org research-papers, research-artifacts,
important-dates, and organizing-committee pages, the SIGPLAN "PLDI will join
PACMPL" announcement, the PACMPL pages on the ACM Digital Library, and the
SIGPLAN Empirical Evaluation Guidelines. Direct fetches of `sigplan.org` and
`pldi26.sigplan.org` returned 403 in the verification environment, so official
pages were read via search-engine renderings of the exact URLs and cross-checked
against the ACM DL and dblp; the full trail — including everything still marked
待核实 — is in [`resources/official-source-map.md`](resources/official-source-map.md).

## What makes PLDI structurally unusual

Five verified mechanics drive most of the advice in this pack, and most of the
mistakes made by authors arriving from ML conferences or SE venues:

- **A conference that publishes a journal.** Since PLDI 2023, accepted papers
  appear as PACMPL — Proceedings of the ACM on Programming Languages — Issue
  PLDI (Vol 7 = 2023, Vol 8 = 2024, Vol 9 = 2025), joining POPL, OOPSLA, and
  ICFP in the same Gold Open Access journal. Reviewing stays a conference
  cycle; the output is a journal article, cited in journal form.
- **One November deadline a year.** PLDI 2026 papers were due November 13,
  2025, via HotCRP (`pldi2026.hotcrp.com`), with author response February
  17-21, notification March 5, and the conference in Boulder June 15-19, 2026.
  Miss November and the next chance is next year.
- **A hard format with a stated penalty.** At most 20 pages of text excluding
  bibliography, in single-column `acmsmall` (10 pt / 12 pt), chosen for PACMPL
  compatibility — with **summary rejection** named as the price of deviating.
- **An artifact culture with teeth.** Artifact evaluation runs after
  acceptance; badges are Functional, Reusable, and Available; the Available
  badge requires an archival Zenodo snapshot with a DOI, and Zenodo versioning
  replaces any artifact camera-ready deadline. Badges print on the PACMPL
  article.
- **A published measurement rubric.** SIGPLAN's Empirical Evaluation Guidelines
  (Blackburn, Hauswirth, Berger, Hicks, Krishnamurthi, 2018) give reviewers a
  one-page checklist — clear claims, suitable comparisons, principled benchmark
  choice, adequate data analysis — and this pack teaches evaluations to pass it
  before reviewers apply it.

Also verified: reviewing is double-blind and has been for years; up to 10% of
accepted papers may be named Distinguished Papers (PLDI 2025: 6 of 89); the
PACMPL APC was 400 USD with SIGPLAN covering authors who cannot pay and ACM
fully open access since January 1, 2026; leadership rotates per edition (2026:
General Chair Bor-Yuh Evan Chang, Program Chair Manu Sridharan). The PLDI 2027
site was still a placeholder at the check date — its deadline is 待核实, not
"November 2026."

## The twelve skills

Strategy and framing:

- [`pldi-topic-selection`](skills/pldi-topic-selection/SKILL.md) — test whether
  the claim's evidence is implementation-and-benchmarks shaped, and route
  POPL/OOPSLA/ICFP (same PACMPL journal, different reviewers) or outward to
  ASPLOS, CGO, CAV, ICSE/FSE, and systems venues.
- [`pldi-writing-style`](skills/pldi-writing-style/SKILL.md) — the first-page
  contract (hard case, insight sentence, substrate, headline number), the
  running-example discipline, and the claim ledger.
- [`pldi-related-work`](skills/pldi-related-work/SKILL.md) — delta-per-citation
  discipline, SIGPLAN-family coverage, PACMPL-era journal-form citations, and
  dblp verification against classic venue traps.

Evidence:

- [`pldi-experiments`](skills/pldi-experiments/SKILL.md) — benchmark suites as
  arguments, strongest-configuration baselines, mechanism-isolating ablations,
  and the three currencies: runtime, compile time, memory.
- [`pldi-reproducibility`](skills/pldi-reproducibility/SKILL.md) — the SIGPLAN
  checklist translated to practice: warmup regimes, 30-run variance, pinned
  toolchains, cross-platform scoping, machine-executed protocols.
- [`pldi-supplementary`](skills/pldi-supplementary/SKILL.md) — what lives in
  the 20 pages versus appendix versus anonymized code drop, and the anonymity
  sweep for archives.

Process:

- [`pldi-submission`](skills/pldi-submission/SKILL.md) — HotCRP mechanics, the
  format and page cap, double-blind leak scanning for tool papers, and the
  summary-rejection triage table.
- [`pldi-review-process`](skills/pldi-review-process/SKILL.md) — how an
  implementor PC reads a paper, the stage-by-stage pipeline, and Distinguished
  Paper mechanics.
- [`pldi-author-response`](skills/pldi-author-response/SKILL.md) — the
  four-bucket triage (soundness first), no-new-contributions rules, and a
  working response skeleton for the five-day window.
- [`pldi-workflow`](skills/pldi-workflow/SKILL.md) — backward planning from
  November plus the long tail: February response, March decision, spring
  artifact evaluation, June talk.

After acceptance:

- [`pldi-camera-ready`](skills/pldi-camera-ready/SKILL.md) — de-anonymization
  as a diff, PACMPL metadata and ORCIDs, open-access handling, and the three
  clocks (article, artifact, talk).
- [`pldi-artifact-evaluation`](skills/pldi-artifact-evaluation/SKILL.md) — the
  badge ladder, the ten-minute smoke test, claim-to-script maps, and Zenodo
  archiving.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) —
  twelve dated official sources, the verified-facts list, and the 待核实
  register.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — five
  venue-verified exemplars from DART (2005) to a badged PACMPL-era artifact
  paper (2023), plus the misattribution traps (LLVM, CompCert, RustBelt).
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional compiler paper's first page rewritten into the PLDI arc.
- [`resources/external_tools.md`](resources/external_tools.md) — HotCRP,
  PACMPL, dblp, Zenodo, acmart, and the Empirical Evaluation Guidelines, with
  author-side checks.
- [`resources/code/README.md`](resources/code/README.md) — the shared methods
  kit adapted to badge-ready PL artifacts.

## Suggested route through a PLDI campaign

1. **Twelve-plus weeks out (late summer):** run `pldi-topic-selection`; if the
   claim's verb is "we prove," have the POPL conversation now, not in October.
   Lock the benchmark suite and baselines with `pldi-experiments`.
2. **Eight weeks out:** script the measurement protocol
   (`pldi-reproducibility`) so paper numbers and the eventual artifact cannot
   diverge; start the draft against the first-page contract in
   `pldi-writing-style`.
3. **Final month:** close the claim ledger, run the related-work delta audit,
   assemble the supplement with its anonymity sweep, and clear the
   summary-rejection table in `pldi-submission` before uploading to HotCRP.
4. **February:** execute the response playbook within the five-day window —
   soundness objections first, section-and-line pointers, no new
   contributions.
5. **On acceptance:** start artifact packaging the same week
   (`pldi-artifact-evaluation`), then run the camera-ready diff and PACMPL
   metadata pass (`pldi-camera-ready`), and put the June talk on someone's
   calendar.

## Common misconceptions this pack corrects

- "PLDI publishes conference proceedings" — not since 2023; cite PACMPL
  volume/issue/article, and check the *issue* name before calling a PACMPL
  paper a PLDI paper.
- "The page limit has journal slack" — the 20-text-page cap carries a summary
  rejection penalty despite the journal-format output.
- "Artifacts are optional polish" — badges print on the article, evaluation
  starts immediately after notification, and Available requires a DOI-stamped
  Zenodo archive, not a GitHub link.
- "A big speedup table is an evaluation" — SIGPLAN's published checklist asks
  for claims, comparisons, benchmark justification, and variance; reviewers
  apply it line by line.

## Maintenance notes

- Every dated fact above is a **2026-cycle snapshot**, most of it read through
  search renderings because direct fetches were blocked; open the live pages
  before acting on any deadline, cap, or badge rule.
- PLDI 2027's dates, location, and deadline were unpublished on 2026-07-08.
  Do not extrapolate "mid-November" into advice; check
  https://conf.researchr.org/home/pldi-2027 and the SIGPLAN announcements page.
- Chairs, HotCRP instances, AE mechanics, response-window mechanics, and
  open-access terms rotate or evolve every edition; the source map lists what
  is known to be volatile.
