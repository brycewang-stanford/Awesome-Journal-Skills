# COLT Skills

Twelve agent skills for papers at COLT, the Annual Conference on Learning Theory —
the theorem-first venue for statistical learning, online learning and bandits,
optimization theory, RL theory, and lower bounds, run by the Association for
Computational Learning and published in the Proceedings of Machine Learning Research
(PMLR).

COLT differs structurally from the big empirical ML conferences, and this pack is
built around those differences rather than around a generic conference template:

- **Proofs are the artifact.** There is no artifact-evaluation track, no
  reproducibility checklist, and no experiments requirement; papers are accepted on
  theorems, and the referee's line-by-line proof verification replaces artifact
  review.
- **One PDF, unlimited appendix.** The 2026 cycle allowed a 12-page PMLR-format body
  (excluding references) with no page limit on references and appendices, all in a
  single file — so appendix architecture is a first-class writing problem.
- **Double-anonymous with an informed area chair.** Reviewers do not see author
  names, but the area chair does, and may reveal identities to a reviewer during the
  rebuttal period on request.
- **CMT, not OpenReview.** The 2025 and 2026 cycles ran submissions through Microsoft
  CMT with a single AoE paper deadline (February 4, 2026 for the 39th edition, held
  June 29 - July 3, 2026 in San Diego).
- **An open-problems culture.** COLT publishes short, citable open-problem pieces in
  its proceedings; posing a well-parameterized question is a recognized contribution
  vehicle.

Official basis checked on 2026-07-08: the COLT 2026 Call for Papers and conference
pages at learningtheory.org, the CMT portal link, and PMLR volume pages (v247 = COLT
2024, v291 = COLT 2025). Direct page fetches were gateway-blocked at the access date,
so verification ran through search excerpts of those official pages; everything that
could not be pinned down is flagged 待核实 rather than asserted. See
`resources/official-source-map.md` for the full source map.

## Skills

Submission pipeline:

- `colt-submission` — audit CMT readiness, the 12-page PMLR-format body, single-PDF
  assembly, double-anonymous formatting, the parallel-submission ban, and the
  final-week sequence before the AoE deadline.
- `colt-supplementary` — architect the unlimited in-PDF proof appendix: body/appendix
  splitting, theorem restatement via restatable environments, lemma ordering, and
  referee-verifiable structure.
- `colt-workflow` — plan backward from the single deadline with result-freeze and
  independent proof-verification milestones, then through rebuttal, decision, and
  camera-ready.

Mathematical quality:

- `colt-reproducibility` — enforce re-derivability: complete proofs, quantifier and
  constant hygiene, external-result hypothesis checks, and assumption bookkeeping.
- `colt-artifact-evaluation` — run the verification-ledger discipline that replaces
  artifact review at a venue with no artifact track, plus code-companion norms for
  the rare numerical paper.
- `colt-experiments` — decide whether a COLT paper needs numerics at all, and design
  honest rate plots, separations, and phase-transition illustrations when it does.

Writing and positioning:

- `colt-writing-style` — execute the theorem-first arc: formal setup before results,
  informal/formal theorem pairing, technique paragraphs, and the 12-page budget.
- `colt-related-work` — build the quantitative known-vs-new ledger across the
  COLT/ALT lineage, CS theory, ML theory tracks, statistics literature, and open
  problems, under the current overlap rules.
- `colt-topic-selection` — test whether a result is COLT-shaped versus ALT,
  STOC/FOCS, NeurIPS/ICML/AISTATS, JMLR, or a statistics journal, including the
  open-problem-piece vehicle.

Review and publication:

- `colt-review-process` — model the pipeline: expert-theorist reviewing,
  correctness-first scoring, the informed-AC anonymity design, and single-track
  stakes.
- `colt-author-response` — draft rebuttals for proof-correctness, tightness, and
  novelty-of-technique objections, with self-contained fixes and contained
  concessions.
- `colt-camera-ready` — produce the PMLR proceedings version: de-anonymization,
  rebuttal-promise ledger, numbering stability, arXiv reconciliation, and citation
  metadata.

## Quick start

Install as a Claude Code plugin (this directory is a self-contained plugin with a
marketplace manifest), or use the skills directly by pointing an agent at
`skills/<name>/SKILL.md`.

Typical sequencing for a new project:

1. `colt-topic-selection` → is this a COLT paper, an open-problem piece, or a
   misroute?
2. `colt-workflow` → set the result-freeze and verification dates backward from the
   live deadline.
3. `colt-reproducibility` + `colt-artifact-evaluation` → close the verification
   ledger before polishing prose.
4. `colt-writing-style` + `colt-supplementary` + `colt-related-work` → build the
   document; consult `resources/worked-examples/01-introduction.md` and
   `resources/exemplars/library.md`.
5. `colt-submission` → final audit against the live CFP.
6. `colt-review-process` + `colt-author-response` → rebuttal phase.
7. `colt-camera-ready` → PMLR publication and the talk.

## Pack structure

```text
COLT-Skills/
├── .claude-plugin/           plugin.json + marketplace.json (12 skills declared)
├── assets/cover.svg          pack cover art
├── resources/
│   ├── README.md             resource index and suggested workflow
│   ├── official-source-map.md  verified sources, access dates, 待核实 register
│   ├── external_tools.md     live official links and do-not-infer rules
│   ├── exemplars/library.md  PMLR-verified COLT papers by result type × technique
│   ├── worked-examples/01-introduction.md  fictional before/after first pages
│   └── code/README.md        adapter to the shared ML-conference code kit
└── skills/colt-*/SKILL.md    the twelve skills
```

## Fact discipline

- Facts stated as facts in this pack were verified against official sources on
  2026-07-08 and carry that anchor date; anything unverifiable at that date —
  program-chair names, notification and camera-ready dates, the 2026 open-problems
  track, registration and presentation rules, the 2026 PMLR volume number — is
  explicitly marked 待核实 in the skills and in the source map.
- COLT re-issues every rule annually with the new Call for Papers. Treat the 2026
  facts as historical anchors: reopen learningtheory.org and the current CFP before
  any deadline-sensitive action, and prefer the live text wherever it conflicts with
  this pack.
- Exemplar papers were individually matched to PMLR volume pages; the library
  documents its omissions and the PMLR volume-number traps that cause venue
  misattribution.

## How this pack differs from the sibling conference packs

- Versus **NeurIPS/ICML/ICLR packs:** no reproducibility-checklist, artifact-badge,
  or benchmark-audit workflows — COLT has none of those mechanisms, and this pack's
  `colt-artifact-evaluation`, `colt-reproducibility`, and `colt-experiments` teach
  what actually replaces them (verification ledgers, re-derivability audits, and
  illustration-only numerics).
- Versus the **AISTATS pack:** AISTATS papers balance theorems with experiments under
  a checklist regime; COLT papers stand on theorems alone with unlimited in-PDF
  appendices, so the writing, supplement, and review skills here are built around
  proof architecture rather than theory-experiment pairing.
- Versus the breadth entry in **Computer-Science-Conference-Skills:** that roster
  file answers "is COLT the right venue?" in one page; this pack covers the full
  lifecycle after (or while) that question is answered, with cycle-verified facts.

## Maintenance notes

- Re-verify the portal each cycle (COLT has changed submission systems over its
  history; 2025-2026 used CMT).
- Re-check page arithmetic, anonymity mechanics, rebuttal format, and overlap-policy
  wording in each new CFP before editing any skill.
- When updating exemplars, confirm the PMLR volume landing page names the Conference
  on Learning Theory — volume numbers interleave venues.
