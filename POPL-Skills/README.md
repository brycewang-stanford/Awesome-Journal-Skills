# POPL Skills

Twelve agent skills for papers targeting **POPL — the ACM SIGPLAN Symposium on
Principles of Programming Languages**, the theory-leaning flagship of the SIGPLAN
family: semantics, type systems, program logics, verification principles, and the
proof techniques that carry them. The pack walks the full arc of a POPL campaign —
testing whether a project's decisive evidence is a theorem rather than a benchmark,
building the informal-to-formal ramp reviewers expect, surviving the single July
HotCRP deadline under full double-blind review, converting an October *conditional*
acceptance into a satisfactory revision, getting a mechanized proof development
through artifact evaluation with zero `admit`s, and publishing the result as a
**PACMPL Issue POPL** journal article presented at the January symposium.

Official basis checked on **2026-07-08**: the POPL 2027 research-papers call and
important-dates pages (popl27.sigplan.org), the POPL 2027 and POPL 2026 conference
sites, the POPL 2025/2026 artifact-evaluation tracks, the PACMPL journal and issue
pages on the ACM Digital Library, and dblp records for every exemplar. Direct
fetches of the sigplan.org and conf.researchr.org sites returned HTTP 403 in the
verification environment, so official pages were read via search-engine renderings
of the exact URLs and cross-checked against the ACM DL and dblp. The full trail —
including everything still marked 待核实 — is in
[`resources/official-source-map.md`](resources/official-source-map.md).

**A timing warning baked into this pack:** the POPL 2027 submission deadline was
**July 9, 2026, 11:59 PM AoE — one day after the verification date above**. Any
agent using these skills near that date must check the live pages before telling an
author the window is open.

## What makes POPL structurally distinctive

Six verified mechanics drive the advice in this pack:

- **A July deadline for a January conference.** POPL 2027 (the 54th edition):
  papers due July 9, 2026 via `popl27.hotcrp.com` with **no abstract deadline**,
  notification October 5, 2026, symposium January 10-16, 2027 at the Hilton Mexico
  City Reforma. One deadline per year; the fall belongs to revision, artifacts, and
  travel.
- **Full double-blind, by explicit contrast with its own past.** Since POPL 2023
  the venue uses *full* double-blind — author identities are revealed only after
  conditional-acceptance decisions, and only for the papers that crossed —
  replacing the lightweight double-blind process POPL used before then.
- **Nobody is accepted, only conditionally accepted.** Every positive decision
  carries conditions, and the call is blunt: submit a satisfactory revision to the
  Review Committee by the requested deadline "or risk rejection."
- **A 25-page text budget with a stated penalty.** At most 25 pages of text
  excluding bibliography, in the single-column acmart/`acmsmall` PACMPL layout
  (10 pt / 12 pt); deviating formats are grounds for **summary rejection**, and
  Word is not accepted.
- **Proof artifacts are the native artifact.** Artifact evaluation is by invitation
  for conditionally accepted papers; badges are Artifacts Evaluated - Functional,
  Artifacts Evaluated - Reusable, and Artifacts Available (archival Zenodo/ACM DL
  snapshot). The AE pages name Coq/Isabelle proof libraries as their examples of
  reusable artifacts and require completeness for reusable proof claims — **no
  `admit` in Coq/Rocq, no `sorry` in Lean or Isabelle**.
- **A conference that publishes a journal.** Accepted papers appear as PACMPL —
  Proceedings of the ACM on Programming Languages — Issue POPL: Vol 2 = 2018,
  Vol 7 = 2023, Vol 10 = 2026 (published January 8, 2026, 2675 pages). PACMPL is
  Gold Open Access; the APC was 400 USD with SIGPLAN covering authors who cannot
  pay, and ACM has been fully open access since January 1, 2026.

Also verified: at most 10% of accepted papers are designated Distinguished Papers;
POPL 2026 (the 53rd edition) ran January 11-17, 2026 in Rennes, France, with CPP
co-located — as it is again in 2027; and POPL is sponsored by SIGPLAN in
cooperation with SIGACT and SIGLOG. The POPL 2027 author-response window, revision
deadline, and chair names had not rendered at check time and are logged as 待核实.

## The twelve skills

Strategy and framing:

- [`popl-topic-selection`](skills/popl-topic-selection/SKILL.md) — the "principles"
  fit test: does the decisive evidence live in a proof? Routing across the PACMPL
  family (PLDI, OOPSLA, ICFP) and outward to LICS, CAV, CPP, ESOP, and journals.
- [`popl-writing-style`](skills/popl-writing-style/SKILL.md) — the
  informal-to-formal ramp, notation as load-bearing infrastructure, proof sketches
  that name the hard case, and transferability framing.
- [`popl-related-work`](skills/popl-related-work/SKILL.md) — theorem-level delta
  sentences, the LICS/CAV/TOPLAS neighborhood map, PACMPL journal-form citations,
  and dblp verification against misattributed classics.

Evidence:

- [`popl-reproducibility`](skills/popl-reproducibility/SKILL.md) — what
  "reproducible" means per claim type at a theory venue, the mechanize-vs-hand-prove
  decision, and the paper-to-proof correspondence table.
- [`popl-experiments`](skills/popl-experiments/SKILL.md) — evidence that supports
  rather than carries the claim: case-study discipline, proof-effort accounting,
  and honest bad-news reporting.
- [`popl-supplementary`](skills/popl-supplementary/SKILL.md) — the body / proof
  appendix / anonymous artifact split, sketch-proof consistency, and the anonymity
  sweep for proof repositories.

Process:

- [`popl-submission`](skills/popl-submission/SKILL.md) — HotCRP mechanics, the
  25-page cap and summary-rejection rules, theory-specific identity leaks, and the
  last-72-hours order of operations.
- [`popl-review-process`](skills/popl-review-process/SKILL.md) — how a POPL
  committee probes correctness by counterexample, what conditional acceptance
  actually decides, and Distinguished Paper mechanics.
- [`popl-author-response`](skills/popl-author-response/SKILL.md) — the four-bin
  triage with soundness doubts first, concession craft, and a concise-response
  skeleton.
- [`popl-workflow`](skills/popl-workflow/SKILL.md) — backward planning from July
  ("theorems do not compress"), the fall gauntlet after notification, and the
  PACMPL deadline wheel for retargeting.

After the decision:

- [`popl-camera-ready`](skills/popl-camera-ready/SKILL.md) — the two gates:
  committee revision, then PACMPL production; de-anonymization as a reviewed diff;
  the January visa clock.
- [`popl-artifact-evaluation`](skills/popl-artifact-evaluation/SKILL.md) — the
  badge criteria proof-flavored, the axiom audit, toolchain pinning, and Zenodo
  archiving.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) — twelve
  dated sources, the verified-fact list, the 待核实 register, and the access-method
  note for the 403-blocked official sites.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) — six
  dblp/ACM-DL-verified landmarks from Cousot & Cousot 1977 to RustBelt in PACMPL
  2(POPL), plus the LICS/JCSS/FPCA/CGO misattribution traps.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  — a fictional gradual-session-types paper's opening rewritten into the POPL arc.
- [`resources/external_tools.md`](resources/external_tools.md) — HotCRP, PACMPL,
  dblp, Zenodo, and author-side checks, with the do-not-infer list.
- [`resources/code/README.md`](resources/code/README.md) — the shared artifact kit
  translated to proof developments (seeds → toolchain pins, experiment matrix →
  correspondence table).

## Suggested route through a POPL campaign

1. **Sixteen weeks out (winter/spring):** run `popl-topic-selection` honestly — if
   the claim needs benchmarks to matter, have the PLDI/OOPSLA conversation before
   investing in metatheory. Conjecture the main theorem precisely.
2. **Twelve to eight weeks out:** prove the hard lemmas, start the kernel
   mechanization, and open the correspondence table (`popl-reproducibility`).
   Freeze the formal core early — broken lemmas do not fix on deadline adrenaline.
3. **Final month:** draft against the ramp in `popl-writing-style`, lock case
   studies (`popl-experiments`), assemble appendix and anonymous artifact with the
   sweep in `popl-supplementary`, and clear `popl-submission`'s severity table
   before the AoE cutoff.
4. **Response window:** run the four-bin triage in `popl-author-response` —
   soundness first, definitions quoted, no new theorems.
5. **On conditional acceptance (early October):** open three tracks the same week —
   the condition ledger (`popl-camera-ready`), the artifact completeness and axiom
   audits (`popl-artifact-evaluation`), and January visa logistics.

## Common misconceptions this pack corrects

- **"POPL is lightweight double-blind."** Not since 2023 — the current process is
  full double-blind, with identities revealed only after conditional-acceptance
  decisions.
- **"Acceptance means done."** POPL acceptances are conditional; the revision gate
  is real and the call names rejection as the failure price.
- **"There is no page limit at POPL."** The 2027 call caps text at 25 pages
  excluding bibliography, under summary-rejection enforcement.
- **"An admitted lemma is fine if disclosed."** For the Reusable badge the AE
  criteria require completeness — no `admit`, no `sorry`; disclosure belongs in the
  axiom audit, not in place of it.
- **"POPL 2018 has proceedings."** PACMPL-era POPL papers are journal articles —
  cite volume, issue POPL, article number.

## Maintenance notes

- Every dated fact here is a **single-cycle snapshot read on 2026-07-08**, much of
  it through search renderings because direct fetches were blocked. Reopen the live
  call before acting on any deadline, cap, or badge rule.
- The July 9, 2026 deadline is POPL 2027's, not a law of nature; do not project it
  onto later cycles, and treat the unrendered response window and revision deadline
  as unknown until the dates page is opened directly.
- Chair identities, HotCRP instances, badge wording, and double-blind mechanics are
  per-edition decisions; the source map's volatility list says what to recheck.
