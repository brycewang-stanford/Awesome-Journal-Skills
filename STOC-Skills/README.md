# STOC Skills

Twelve agent skills for papers targeting **STOC — the ACM Symposium on Theory of
Computing**, SIGACT's flagship venue for algorithms, computational complexity,
cryptography, quantum computing, learning theory, and the rest of the theory of
computation. The pack covers the whole arc of a STOC cycle: deciding whether a
result is flagship-general or belongs at a specialized theory venue, writing an
extended abstract that survives the guaranteed-read window, clearing the HotCRP
submission audit, modeling a no-rebuttal review process, and converting an
acceptance into both an ACM proceedings entry and the public arXiv/ECCC full
version the community actually reads.

Official basis checked on **2026-07-08**: the STOC 2026 Call for Papers and
conference pages at `acm-stoc.org`, the STOC 2026 HotCRP portal, SIGACT prize
and policy pages, the ACM Digital Library proceedings record, and dblp entries
for the exemplar papers. Direct fetches of the official domains were
gateway-blocked in the verification environment, so pages were read via
search-engine renderings of the exact URLs and cross-checked against the ACM DL,
dblp, and the SIGACT community blog; the full trail, including everything still
marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes STOC unlike its neighbors

These venue mechanics, verified for the 2026 cycle, drive the advice in the
skills — and the mistakes of authors arriving from ML conferences or journals:

- **A reading contract instead of a page limit.** Submissions have no length
  bound, but only the abstract, the **table of contents**, and the first twelve
  pages are guaranteed committee attention; the rest is discretionary. The ToC
  is a reviewed object, and every theorem must be stated inside the window.
- **The full version is the artifact.** The CFP expects accepted authors to
  post complete papers, with all proofs, on arXiv or ECCC by camera-ready. The
  ACM proceedings entry is an extended abstract — the advertisement, not the
  record — so keeping the two documents consistent is a first-class task.
- **Newly double-blind.** STOC 2026 used double-blind reviewing, a departure
  from the venue's long non-anonymous tradition; old lab templates are now the
  main identity-leak source.
- **No rebuttal.** The arc runs from the November deadline straight to a
  February decision. Every anticipated objection must be answered inside the
  submission, because there is no second conversation.
- **A two-beat year with FOCS.** STOC (November deadline, June conference) and
  FOCS (April deadline, fall conference) share a community and scope; theory
  groups plan around the pair, and rejected papers reappear at the other beat.
- **Theorems only.** No experiments axis, no artifact track, no checklist.
  Computation appears legitimately as a certified proof step, a discovery
  instrument, or a labeled illustration — never as benchmarking.
- **TheoryFest.** STOC 2026 ran as a five/six-day program in Salt Lake City
  (June 22–26, plus a Saturday "Can AI do Theory?" workshop), with talks for
  all accepted papers and up to four PC-designated Best Papers.

## Skills

| Skill | What it does |
| --- | --- |
| [`stoc-topic-selection`](skills/stoc-topic-selection/SKILL.md) | Run the breadth tests (corridor, lineage, technique) and route between STOC/FOCS, SODA, CCC, ITCS, COLT, CRYPTO, PODC, SoCG, EC, QIP, or a direct journal submission. |
| [`stoc-workflow`](skills/stoc-workflow/SKILL.md) | Plan the two-beat theory year: backward planning to the November deadline, the FOCS fallback, the corrections file, and the camera-ready double deliverable. |
| [`stoc-writing-style`](skills/stoc-writing-style/SKILL.md) | Build the theorem-forward first page, informal/formal statement pairs, the technical-overview section, and notation economy for a cross-area committee. |
| [`stoc-related-work`](skills/stoc-related-work/SKILL.md) | Cover the five lanes theory reviewers check — lineage, barriers, neighboring models, technique ancestry, concurrent preprints — with version-aware citation. |
| [`stoc-supplementary`](skills/stoc-supplementary/SKILL.md) | Architect everything past page twelve: the reviewed ToC, placement decisions, pointer discipline, and the appendix/full-version division of labor. |
| [`stoc-reproducibility`](skills/stoc-reproducibility/SKILL.md) | Make theorems independently checkable: single-source statements against drift, hypothesis visibility, external-result audits, deterministic proof computation. |
| [`stoc-experiments`](skills/stoc-experiments/SKILL.md) | Classify any computation as certified proof step, discovery instrument, or illustration — and re-route benchmark-shaped evidence to the venues that reward it. |
| [`stoc-artifact-evaluation`](skills/stoc-artifact-evaluation/SKILL.md) | Manage the evidence stack at a no-artifact-track venue: the full version as object of record, certificates with independent checkers, honest mechanization claims. |
| [`stoc-submission`](skills/stoc-submission/SKILL.md) | Final HotCRP audit: the guaranteed-read rule, format floor, double-blind sweep, SIGACT prior/simultaneous-publication policy, deadline-week sequence. |
| [`stoc-review-process`](skills/stoc-review-process/SKILL.md) | Model the SIGACT PC with external subreviewers, the committee's evaluation axes, the November-to-February arc, and what each outcome means. |
| [`stoc-author-response`](skills/stoc-author-response/SKILL.md) | Work the three real channels at a no-rebuttal venue: pre-emptive objection discharge, chair-mediated clarifications, and the FOCS resubmission memo. |
| [`stoc-camera-ready`](skills/stoc-camera-ready/SKILL.md) | Deliver both March 31 artifacts — the ACM proceedings version and the public full version — keep them coherent, and prepare the TheoryFest talk. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve official sources with URLs and access dates, the verified 2026-cycle fact list, the access-method note, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus six author-side verification passes keyed to the skills. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five dblp/ACM-verified STOC papers across five decades and contribution types, with a STOC-vs-FOCS misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional dynamic-connectivity opening rebuilt from journal style into the STOC arc: result, lineage, barrier, technique, consequences. |
| [`resources/code/README.md`](resources/code/README.md) | The few shared-kit tools that apply at a proofs-first venue, plus STOC-native anonymity, drift, and packaging checks. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./STOC-Skills
claude plugin install stoc-skills
```

Or use the files directly: each `skills/stoc-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger
it. Typical invocations:

- "Is this result STOC material or should it go to SODA?" → `stoc-topic-selection`
- "Audit my draft against the STOC reading rule before I upload" → `stoc-submission`
- "The proofs live at page 30 — how do I structure the appendix?" → `stoc-supplementary`
- "We got in; what do the March deadlines require?" → `stoc-camera-ready`

## Pack structure

```text
STOC-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── stoc-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared kit, mostly declined
```

## 2026 anchor facts (historical snapshot, not permanent rules)

- STOC 2026 was the **58th** edition: Salt Lake City, Utah, USA,
  **June 22–26, 2026**, inside an expanded TheoryFest week (Saturday June 27:
  "Can AI do Theory?" workshop).
- Submission deadline: **November 4, 2025, 4:59pm EST** (a US-Eastern clock, not
  AoE), on HotCRP; no separate abstract deadline. Notification by
  **February 1, 2026**; camera-ready **March 31, 2026 (AoE)**.
- Reading rule: no length bound; abstract + table of contents + first **twelve
  pages** guaranteed; 11-point-plus, single-column, 1-inch margins, letter paper.
- **Double-blind** reviewing; SIGACT prior/simultaneous-publication policy with
  the Science/Nature exception; arXiv/ECCC posting is not prior publication.
- Full papers with proofs expected on **arXiv/ECCC by camera-ready**;
  proceedings in the ACM Digital Library (58th: DOI 10.1145/3798129).
- PC chair: Artur Czumaj (Warwick). Experimental opt-in **LLM pre-submission
  feedback** (Gemini-based; full paper due November 1; authors-only output).
- Sibling beat: FOCS 2026 deadline April 1, 2026 (21:00 UTC), conference
  November 8–11, 2026, New York.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — carry dates and trace to a numbered source in
   the source map (the twelve-page window, the November 4 deadline).
2. **Community customs** — practices documented only in how the venue behaves
   (chair-mediated clarification questions, subreviewer delegation), labeled as
   customs rather than rules.
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions
   (the entire STOC 2027 cycle, registration obligations, camera-ready format
   specifics, the first double-blind year).

Any statement presenting class 2 or 3 material as class 1 is a bug; fix it
against the live official pages.

## Maintenance notes

- Every date and rule above is a **2026-cycle snapshot**. STOC's reading window
  has already changed size across cycles (10 → 12 pages), and double-blind is
  new; reopen `acm-stoc.org/stoc<year>/` each fall before deadline advice.
- **STOC 2027 was entirely 待核实 at 2026-07-08** — no official CFP was
  locatable, and aggregator listings carried recycled 2026 data. The historical
  pattern (CFP late summer, deadline early November) is a pattern, not a fact.
- PC chairs and committees rotate annually; every name in this pack is a
  one-cycle fact.
- When adding exemplars, follow the dblp verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — and
  never attribute between STOC and FOCS from memory.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
