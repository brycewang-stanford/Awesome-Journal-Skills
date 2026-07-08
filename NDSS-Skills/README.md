# NDSS Skills

Twelve agent skills for papers targeting **NDSS — the Network and Distributed System
Security Symposium**, the Internet Society's flagship in the security "big four" alongside
IEEE S&P, USENIX Security, and ACM CCS. The pack runs the full arc of an NDSS cycle:
deciding whether a networked adversary is real, building deployment-grade evidence,
packaging the double-blind HotCRP submission with its ethics record, surviving a two-round
review with an early reject and an interactive rebuttal, handling the **Accept / Minor
Revision / Major Revision** decision set, and delivering an open-access Internet Society
camera-ready plus optional artifact badges.

Official basis checked on **2026-07-08**: the NDSS 2027 Call for Papers and Call for
Artifacts, the live `ndss27-summer.hotcrp.com` cycle site, the Internet Society's June 2026
announcement of the move to Seoul, the NDSS 2026 co-located-events and open-publication
pages, the Test of Time award page, and dblp's `conf/ndss` stream. Direct fetches of
`ndss-symposium.org` and `dblp.org` returned HTTP 403 in the verification environment, so
official pages were read through search-engine renderings of the exact URLs and
cross-checked against HotCRP, Internet Society pages, and dblp records; the full trail,
including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes NDSS different from its siblings

These venue mechanics, verified for the 2027 edition, drive most of the advice in the skills
— and most of the mistakes made by authors arriving from another security venue or from ML
and systems conferences:

- **A fixed identity that just moved.** For decades NDSS *was* San Diego in February. The
  2027 edition deliberately breaks that pattern: **Seoul, Republic of Korea, 22-26 March
  2027**, to grow Asia-Pacific participation. Treat even the host city as a per-edition fact.
- **Two submission cycles into one symposium.** A summer cycle (2027 papers due May 6, 2026)
  and a **fall cycle (papers due August 19, 2026)**, each a complete pipeline. A paper
  rejected in one cycle cannot return with major overlap in the same symposium's other cycle
  — cycle choice is strategic, and a fall deadline may be imminent as you read this.
- **Two-round review with an early reject.** Round 1 filters on a fast read and ejects the
  bottom with no rebuttal; survivors reach Round 2, see reviews, and file a rebuttal into an
  **interactive discussion phase** with the reviewers.
- **A revision-forward decision set.** Beyond Accept and Reject, NDSS issues **Minor
  Revision** and **Major Revision** — the latter carrying an explicit list of reviewer-written
  revision tasks, re-reviewed against that list, at most once per paper.
- **Ethics is structural.** An optional **Ethics Considerations section** (excluded from the
  page count), an **Ethics Review Board** of TPC members that can reject on ethical grounds,
  the **Menlo Report** as the named baseline, and disclosure expectations for high-impact
  vulnerabilities — IRB sign-off alone is not treated as sufficient.
- **13 pages, generous exclusions.** Thirteen body pages in the NDSS template, with the
  ethics section, references, and appendices *outside* the count — but reviewers need not
  read appendices, so the acceptance case must live in the body.
- **Free, open-access proceedings.** The Internet Society publishes papers and talk videos to
  the world with no paywall and no author page charge, and authors may self-archive the
  camera-ready.
- **Opt-in artifact evaluation.** After conditional acceptance, authors may earn **Available /
  Functional / Reproduced** badges on the first page plus a 2-page artifact appendix.

## Skills

| Skill | What it does |
| --- | --- |
| [`ndss-topic-selection`](skills/ndss-topic-selection/SKILL.md) | Apply the wire, deployment-envelope, and adversary-ownership tests, and route among IEEE S&P, USENIX Security, CCS, PETS, IMC, and ACSAC by contribution shape. |
| [`ndss-workflow`](skills/ndss-workflow/SKILL.md) | Run the dual-cycle year: pick summer or fall, backward-plan from the AoE deadline through the disclosure clock, and branch on the decision — told from the NDSS seat in the big-four calendar. |
| [`ndss-writing-style`](skills/ndss-writing-style/SKILL.md) | Build the first-page contract — capability-bounded adversary, evidence-sized claims, woven ethics — and fit 13 template pages for a two-round read. |
| [`ndss-related-work`](skills/ndss-related-work/SKILL.md) | Cover the flagship, specialist, and advisory/RFC literature, write mechanism-level deltas, verify against the open proceedings and dblp, and keep self-citation blind. |
| [`ndss-experiments`](skills/ndss-experiments/SKILL.md) | Match evidence to contribution type across live, testbed, and emulation substrates, evaluate defenses against adaptive adversaries, and keep measurements honest. |
| [`ndss-reproducibility`](skills/ndss-reproducibility/SKILL.md) | Freeze the measured Internet, scrub identity-bearing traces, maintain a claims ledger, and write availability statements that survive open-access scrutiny. |
| [`ndss-supplementary`](skills/ndss-supplementary/SKILL.md) | Split content across the 13-page body, the uncounted ethics section, and appendices by review status — and add the camera-ready artifact appendix. |
| [`ndss-submission`](skills/ndss-submission/SKILL.md) | Final HotCRP audit: AoE clock, template and length, double-blind sweep, ethics readiness, the six-per-author cap and overlap rules, and desk-reject triage. |
| [`ndss-review-process`](skills/ndss-review-process/SKILL.md) | Model the two rounds, the early reject, rebuttal and interactive discussion, the Accept/Minor/Major decision set, and the Ethics Review Board. |
| [`ndss-author-response`](skills/ndss-author-response/SKILL.md) | Triage Round-2 reviews, answer adaptive-attack and ethics objections with pointable evidence, and negotiate toward Accept or a scoped revision. |
| [`ndss-artifact-evaluation`](skills/ndss-artifact-evaluation/SKILL.md) | Target the Available/Functional/Reproduced badges, package exploits and traces responsibly, and write the 2-page artifact appendix. |
| [`ndss-camera-ready`](skills/ndss-camera-ready/SKILL.md) | Discharge revision conditions, de-anonymize, restore disclosure specifics, place earned badges, and meet the Internet Society open-access requirements. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Eleven official sources with URLs and access dates; the access-method note; verified 2027 cycle facts; reported facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus six author-side verification passes for cycle, format, anonymity, ethics, cap, and post-acceptance. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified NDSS papers (two Test of Time winners) across contribution types, with self-checks and a checked misattribution list. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional stale-delegation DNS abstract and introduction rebuilt around adversary model, measurement discipline, and disclosure, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus the NDSS-specific checks (trace scrubbing, live-Internet snapshots, exploit gating) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./NDSS-Skills
claude plugin install ndss-skills
```

Or use the files directly: each `skills/ndss-*/SKILL.md` is a standalone instruction file
whose frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this an NDSS paper or should it go to USENIX Security?" → `ndss-topic-selection`
- "Can I still make the NDSS fall cycle?" → `ndss-workflow`
- "Audit my draft against the NDSS submission rules" → `ndss-submission`
- "Reviews are in and I'm in Round 2 — plan the rebuttal" → `ndss-author-response`
- "We got a Major Revision — what now?" → `ndss-review-process` + `ndss-author-response`

## Pack structure

```text
NDSS-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── ndss-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to the shared repro kit
```

## Fact discipline

The skills keep three classes of statement distinguishable:

1. **Verified cycle facts** — carry dates/caps and trace to a numbered source in the source
   map (the August 19, 2026 fall deadline, the 13-page limit, the Accept/Minor/Major decision
   set, the Seoul move).
2. **Reported facts** — found only in secondary sources and labeled as such (e.g., a named
   Publication Chair found on a personal page).
3. **Unverifiable-at-check-time items** — marked 待核实 and written as questions to resolve,
   never as facts (the fall HotCRP URL, the Major-Revision resubmission window, 2027 chairs,
   any generative-AI policy, the 2027 co-located workshop list, 2027 artifact deadlines).

If any skill presents class 2 or 3 material as class 1, treat it as a bug and fix it against
the live official pages.

## Maintenance notes

- Every date, cap, and city above is a **cycle snapshot** — reopen the current
  `ndss-symposium.org` CFP and the live HotCRP cycle site before deadline-sensitive advice.
- NDSS deadlines are **Anywhere-on-Earth (UTC-12)**; convert deliberately.
- The 2027 Seoul move proves that even NDSS's most fixed attribute — San Diego in February —
  is per-edition. Do not carry any single fact forward as permanent.
- Chairs, the ERB, template versions, HotCRP URLs, and badge definitions rotate or re-set per
  edition; treat journal-style continuity assumptions as errors here.
- When adding exemplar papers, follow the recipe in
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a networked-security
  title does not prove NDSS; USENIX Security, S&P, CCS, and IMC share the subject matter.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
