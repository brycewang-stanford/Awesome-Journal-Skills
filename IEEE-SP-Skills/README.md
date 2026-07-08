# IEEE S&P Skills

Twelve agent skills for papers targeting **IEEE S&P — the IEEE Symposium on
Security and Privacy**, held since 1980 and known across the field as
"**Oakland**" for its original venue in the Oakland hills. The pack covers the
full arc of an S&P cycle: deciding whether there is a real adversary,
building adversary-grade evidence, packaging the anonymous HotCRP submission
with its ethics record, surviving a round-based review with early rejects and
a short rebuttal, handling the three-way **Accept / Revise / Reject**
decision, and delivering a shepherded IEEE camera-ready plus artifact badges.

Official basis checked on **2026-07-08**: the S&P 2027 Call for Papers and
per-cycle deadline pages, the S&P 2026 CFP and artifact-evaluation pages, the
IEEE Computer Society Technical Committee on Security and Privacy index, and
dblp's `conf/sp` proceedings stream. Direct fetches of
`sp<year>.ieee-security.org` were blocked in the verification environment, so
official pages were read via search-engine renderings of the exact URLs and
cross-checked against dblp and IEEE Xplore; the full trail, including
everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes IEEE S&P different from its siblings

These venue mechanics, verified for the 2026/2027 cycles, drive most of the
advice in the skills — and most of the mistakes made by authors arriving from
USENIX Security, CCS, or NDSS, let alone from ML or systems venues:

- **Multiple submission cycles per symposium.** Each S&P symposium accepts
  papers through more than one cycle (June and November for the 2027
  symposium), and each cycle is a self-contained mini-conference with its own
  HotCRP site, binding registration freeze, review rounds, and decision date.
  You choose a cycle, not "the deadline."
- **A binding registration a week before the paper.** Title, full abstract,
  complete author list with **ORCIDs**, and conflicts freeze at registration;
  ORCID name/email must match HotCRP or the paper is desk rejected.
- **Rounds with an early reject and no rebuttal for the cut.** Weak papers
  exit in the first round without a chance to respond; survivors see reviews
  and file a short (~5-day) rebuttal.
- **A three-way decision, and the Revise pathway is the signature.**
  **Accept** comes with a draft meta-review and a **shepherd**; **Revise** is
  a structured major revision against a written expectations summary,
  re-reviewed; **Reject** starts a one-year embargo (from the original
  submission date), with ~40% overlap counting as a resubmission.
- **Ethics is structural, not decorative.** An Ethics Considerations field at
  registration, a Research Ethics Committee that can reject on ethical
  grounds, the **Menlo Report** as the named baseline, IRB disclosure, and
  harm mitigation for any PII.
- **13 + ≤5 pages in the IEEE compsoc template**, 18 total, with reviewers
  **not required to read appendices** — the acceptance case must live in the
  body.
- **SoK is a first-class lane** (the `SoK:` title prefix plus a checkbox), and
  **artifact evaluation** is a post-acceptance opt-in with Available,
  Functional, and Results Reproduced badges.

## Skills

| Skill | What it does |
| --- | --- |
| [`ieeesp-topic-selection`](skills/ieeesp-topic-selection/SKILL.md) | Apply the real-adversary test, decide research vs SoK, and route among USENIX Security, CCS, NDSS, PETS, and CRYPTO under the one-year embargo. |
| [`ieeesp-workflow`](skills/ieeesp-workflow/SKILL.md) | Run the multi-cycle year: pick a cycle, plan backward from its registration week, and branch for Accept / Revise / Reject with named owners. |
| [`ieeesp-writing-style`](skills/ieeesp-writing-style/SKILL.md) | Pass the first-round survival test — adversary, bounded claim, evidence map, why-now, ethics signal — and compress into 13 compsoc pages. |
| [`ieeesp-related-work`](skills/ieeesp-related-work/SKILL.md) | Cover the four-flagship literature window, write security-delta sentences, verify dblp/Xplore attribution, and keep self-citation anonymous. |
| [`ieeesp-experiments`](skills/ieeesp-experiments/SKILL.md) | Match evaluation to contribution type, evaluate defenses against adaptive adversaries, and report attack success with trials and dispersion. |
| [`ieeesp-reproducibility`](skills/ieeesp-reproducibility/SKILL.md) | Freeze the measured world — target snapshots, hardware pinning, disclosure timing — and write honest availability statements under ethical limits. |
| [`ieeesp-supplementary`](skills/ieeesp-supplementary/SKILL.md) | Split content across the 13-page body and the shared 5-page refs/appendix so nothing the acceptance case needs sits where reviewers may not read. |
| [`ieeesp-artifact-evaluation`](skills/ieeesp-artifact-evaluation/SKILL.md) | Choose Available / Functional / Reproduced badges, deposit with a DOI, and package exploits and malware-adjacent code responsibly. |
| [`ieeesp-submission`](skills/ieeesp-submission/SKILL.md) | Final HotCRP audit: registration freeze, ORCID matching, compsoc format, anonymization with disclosure-trail sweeps, and desk-reject triage. |
| [`ieeesp-review-process`](skills/ieeesp-review-process/SKILL.md) | Model the rounds, the early reject, the rebuttal, the REC track, the shepherd, and where author leverage actually exists. |
| [`ieeesp-author-response`](skills/ieeesp-author-response/SKILL.md) | Triage reviews for the 5-day rebuttal, answer adaptive-attack and ethics objections, and treat a Revise summary as a contract. |
| [`ieeesp-camera-ready`](skills/ieeesp-camera-ready/SKILL.md) | Work the shepherd's concern ledger, add the ethics section, de-anonymize and restore disclosure specifics, and meet IEEE compsoc/Xplore requirements. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen official sources with URLs and access dates; verified cycle facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus author-side verification passes for registration week, the format gate, anonymity, ethics, and post-acceptance. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified S&P papers across attack and SoK lanes, with self-check questions and an anti-misattribution guide. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional serverless side-channel abstract and introduction rebuilt to survive the first-round, no-rebuttal read, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus the S&P-specific checks (target snapshots, disclosure timing, dangerous-material handling) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its
own marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./IEEE-SP-Skills
claude plugin install ieee-sp-skills
```

Or use the files directly: each `skills/ieeesp-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to
trigger it. Typical invocations:

- "Is this a real S&P paper or should it go to USENIX Security?" → `ieeesp-topic-selection`
- "Which S&P 2027 cycle can I realistically hit?" → `ieeesp-workflow`
- "Audit my draft against the S&P submission rules" → `ieeesp-submission`
- "Reviews are in and I have five days — plan the rebuttal" → `ieeesp-author-response`
- "We got a Revise — how do I handle it?" → `ieeesp-review-process` + `ieeesp-author-response`

## Pack structure

```text
IEEE-SP-Skills/
├── .claude-plugin/            # plugin.json + marketplace.json (12 skills declared)
├── README.md                  # this file
├── README.zh-CN.md            # 中文说明
├── LICENSE                    # MIT
├── assets/cover.svg           # pack cover
├── skills/
│   └── ieeesp-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md              # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md         # adapter to the shared repro kit
```

## Suggested use

1. **Before writing** — run `ieeesp-topic-selection`; if there is no defensible
   adversary, this pack just saved you a cycle and the one-year embargo. Skim
   the exemplars library to see what "a real adversary and an end-to-end
   demonstration" looks like in accepted form.
2. **Plan the cycle** — `ieeesp-workflow`, working backward from a specific
   registration week; the ethics latency (disclosure, IRB) is the item teams
   misplace.
3. **While building** — keep `ieeesp-experiments` and `ieeesp-reproducibility`
   open next to the codebase; adaptive-adversary evaluation and target
   snapshots are cheaper to install early than to retrofit.
4. **While writing** — `ieeesp-writing-style` for the body,
   `ieeesp-supplementary` for the body/appendix split, `ieeesp-related-work`
   for positioning; compare against the worked example's before/after.
5. **Deadline week** — `ieeesp-submission` end to end, including the ORCID and
   disclosure-trail anonymity checks, and treat registration week as its own
   deadline.
6. **After submission** — `ieeesp-review-process` to time expectations,
   `ieeesp-author-response` when reviews land, then `ieeesp-camera-ready` (with
   the shepherd) or the Revise / rejection branch depending on the decision.

## Fact discipline

This pack separates three classes of statement, and the skills are written to
keep them distinguishable:

1. **Verified cycle facts** — carry dates/caps and trace to a numbered source
   in the source map (e.g., the 13-page body limit, the November 17, 2026
   Cycle 2 paper deadline, the Accept/Revise/Reject decision set).
2. **Reported facts** — found only in secondary sources and labeled as such
   (e.g., S&P 2025 submission/acceptance counts from institutional award
   announcements).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased
   as questions to resolve, never as facts (e.g., 2027 Cycle 1's review
   timetable, the Revise resubmission target cycle, the 2027 camera-ready and
   artifact schedules).

If you find any statement in the skills that presents class 2 or 3 material as
class 1, treat it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **cycle snapshot**; reopen the current
  `sp<year>.ieee-security.org` CFP and the live per-cycle deadline pages before
  giving deadline-sensitive advice.
- S&P deadlines are stated in a **fixed clock time** (e.g., 7:59:59 AM EDT),
  not Anywhere-on-Earth — convert to your timezone rather than assuming AoE.
- Items that could not be verified live on 2026-07-08 are marked 待核实 in the
  source map — notably 2027 Cycle 1's review dates, the Revise resubmission
  mechanics, the 2027 camera-ready and artifact-evaluation schedules, the PC
  chairs and REC membership, and the exact wording of the generative-AI
  policy. Do not state these as facts until confirmed.
- PC chairs and the REC rotate per edition and policy is re-set annually;
  treat editor-style continuity assumptions (carried over from journal packs)
  as errors here.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a "SP"
  string does not prove main-conference S&P (EuroS&P and SPW workshops are
  distinct venues).

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
