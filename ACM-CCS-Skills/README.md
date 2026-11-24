# ACM CCS Skills

Twelve agent skills for papers targeting **ACM CCS — the ACM Conference on Computer and
Communications Security**, SIGSAC's flagship venue and one of the "big four" of computer
security alongside IEEE S&P, USENIX Security, and NDSS. The pack covers the full arc of a CCS
cycle: deciding whether the security contribution belongs at CCS, building adversary-proof
evidence, packaging the anonymized HotCRP submission, clearing the ethics and disclosure bar,
surviving the two-cycle review and rebuttal, and delivering the ACM camera-ready plus optional
artifact evaluation.

Official basis first checked on 2026-07-08 and **re-verified 2026-11-24** by direct fetch of
the CCS 2026 Call for Papers, the call for artifacts, the CCS 2026 home and organizing-committee
pages, and the CCS 2027 placeholder and HotCRP site. CCS 2026 (The Hague, November 15-19, 2026)
has met; CCS 2027 is announced for Atlanta, October 11-15, 2027, but its call is not out, so the
pack keeps the CCS 2026 rules as its reference edition. The full trail, including everything
still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes CCS different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the skills —
and most of the mistakes made by authors arriving from another security venue or from ML/theory
conferences:

- **Two review cycles, one conference.** CCS runs Cycle A and Cycle B each year on HotCRP. A
  paper enters one cycle; work rejected in the first cycle **cannot be resubmitted the same
  year**. Cycle choice is a strategic decision, not a formality.
- **Abstract registration is mandatory and comes first.** Title, authors, abstract, and topics
  must be registered about a week before the full-paper deadline; no registered abstract, no
  paper.
- **A hard 12-page ACM `sigconf` body.** Twelve pages in the unaltered two-column ACM template,
  excluding bibliography and well-marked appendices. Whitespace or margin tampering is a
  desk-reject trigger.
- **Anonymized submission with third-person self-citation.** Papers not properly anonymized may
  be rejected without review.
- **An "Open Science" appendix is mandatory** (2026): after the body and bibliography, list
  where every artifact needed to evaluate the paper lives (anonymous URLs, also entered on
  HotCRP, live within 3 days of submission) or state that there are none.
- **An "Ethical Considerations" appendix is required** for work touching human subjects, user
  data, or real-world vulnerabilities — in 2026, after the body and bibliography, outside the
  page count. IRB/ERB approval is neither necessary nor sufficient on its own.
- **Generative-AI use must be disclosed** (ACM authorship policy): minor editing in the
  Acknowledgements, substantive use in a "Generative AI Usage" section. CCS 2026 did not
  accept SoK or survey papers.
- **Decisions are not binary.** Accept, minor revision (revise within the cycle), or reject.
- **Optional post-acceptance artifact evaluation** awards ACM badges — Artifacts Available,
  Functional, Reusable, and Results Reproduced — printed on the paper's first page.
- **The reviewers are adversarial.** A SIGSAC PC attacks your threat model, looks for the
  assumption that makes the attack easy, and expects defenses to face an adaptive attacker.

## Skills

| Skill | What it does |
| --- | --- |
| [`ccs-topic-selection`](skills/ccs-topic-selection/SKILL.md) | Route between CCS, IEEE S&P, USENIX Security, NDSS, PETS, and crypto venues by threat model and contribution type — not prestige. |
| [`ccs-workflow`](skills/ccs-workflow/SKILL.md) | Run the dual-cycle year: abstract registration, full paper, rebuttal, notification, artifact evaluation, camera-ready, plus the big-four deadline-hopping calendar. |
| [`ccs-writing-style`](skills/ccs-writing-style/SKILL.md) | Put the threat model on the first page, calibrate attack/defense claims, and compress into 12 two-column `sigconf` pages. |
| [`ccs-related-work`](skills/ccs-related-work/SKILL.md) | Cover the big-four and specialist literature plus the CVE/advisory record, and keep self-citation double-blind. |
| [`ccs-experiments`](skills/ccs-experiments/SKILL.md) | Build the attack demonstration, the adaptive-attack defense evaluation, and validated measurements that survive a skeptic. |
| [`ccs-reproducibility`](skills/ccs-reproducibility/SKILL.md) | Map claims to evidence, pin versions and budgets, and justify withheld artifacts honestly. |
| [`ccs-supplementary`](skills/ccs-supplementary/SKILL.md) | Split content between the 12-page body and appendices — including the ethics section — by review status, not convenience. |
| [`ccs-artifact-evaluation`](skills/ccs-artifact-evaluation/SKILL.md) | Package attacks, defenses, and measurements for the ACM badge ladder with one command per headline result. |
| [`ccs-submission`](skills/ccs-submission/SKILL.md) | Final HotCRP audit: abstract registration, page and template checks, anonymity sweep, ethics section, cap, and dual-submission triage. |
| [`ccs-review-process`](skills/ccs-review-process/SKILL.md) | Model the two-cycle pipeline, the decision categories, the ethics reviewer, and where author leverage exists. |
| [`ccs-author-response`](skills/ccs-author-response/SKILL.md) | Map objections onto threat model, evidence, and ethics, and answer with anonymous, evidence-anchored rebuttals for the meta-reviewer. |
| [`ccs-camera-ready`](skills/ccs-camera-ready/SKILL.md) | Convert acceptance into a correct ACM DL entry: de-anonymization, rights forms, badge placement, disclosure timing, and presentation. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Nine official sources with URLs and access dates; the access-method note; verified 2026 facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Six metadata-verified CCS papers (four Test-of-Time winners) across six contribution types, with self-check questions and an anti-misattribution guide. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional side-channel abstract and introduction rebuilt to the CCS first-page arc, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus the CCS-specific checks the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own marketplace
manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./ACM-CCS-Skills
claude plugin install acm-ccs-skills
```

Or use the files directly: each `skills/ccs-*/SKILL.md` is a standalone instruction file whose
frontmatter `description` tells an agent when to trigger it. Typical invocations:

- "Is this side-channel result a CCS paper or an S&P paper?" → `ccs-topic-selection`
- "Audit my draft against the CCS submission rules" → `ccs-submission`
- "Reviews came in — help me plan the rebuttal" → `ccs-author-response`
- "Package my exploit for artifact evaluation" → `ccs-artifact-evaluation`

## Pack structure

```text
ACM-CCS-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json (12 skills declared)
├── README.md                # this file
├── README.zh-CN.md          # 中文说明
├── LICENSE                  # MIT
├── assets/cover.svg         # pack cover
├── skills/
│   └── ccs-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md            # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # adapter to the shared repro kit
```

## Suggested use

1. **Before writing** — run `ccs-topic-selection`; if the threat model does not fit CCS, this
   pack just saved you a cycle. Skim the exemplars library to see what a durable CCS threat
   model looks like.
2. **While building** — keep `ccs-experiments` and `ccs-reproducibility` open next to the
   codebase; the adaptive-attack triad and version pinning are cheaper to install early than to
   retrofit in deadline week.
3. **While writing** — `ccs-writing-style` for the body, `ccs-supplementary` for the
   body/appendix/ethics split, `ccs-related-work` for positioning against the big four and the
   CVE record; compare against the worked example's before/after.
4. **Deadline week** — register the abstract early, then run `ccs-submission` end to end,
   including the anonymity and template checks and the ethics section.
5. **After submission** — `ccs-review-process` to time expectations, `ccs-author-response` when
   reviews land, then `ccs-camera-ready` and optional `ccs-artifact-evaluation` on acceptance,
   or big-four re-routing on a reject.

## 2026 anchor facts (historical snapshot, not permanent rules)

- CCS 2026: **The Hague, Netherlands, November 15-19, 2026** (has met).
- Cycle A: abstract registration **Jan 7**, full paper **Jan 14**, early reject **Feb 20**,
  rebuttal **Mar 17-20**, notification **Apr 9**, camera-ready **Aug 9, 2026**.
- Cycle B: abstract registration **Apr 22**, full paper **Apr 29**, online artifacts **May 2**,
  early reject **Jun 12**, rebuttal **Jun 29-Jul 1**, notification **Jul 17**, camera-ready
  **Sep 13, 2026**. All deadlines AoE.
- Format: unaltered ACM `sigconf` two-column template · **12-page** main body excluding
  bibliography, well-marked appendices, and supplementary material.
- Anonymized submission · mandatory registration with track and track justification ·
  Open Science appendix · ethics appendix when needed · ORCIDs for all authors ·
  up to **7 papers per author per cycle** · first-cycle rejects cannot return the same year.
- Optional artifact evaluation with ACM badges; accepted papers publish in the ACM Digital
  Library.
- Accepted papers are open access in the ACM DL; authors outside ACM Open institutions paid
  an APC (2026: USD 250 ACM/SIG members, 350 non-members).
- **CCS 2027 is announced for Atlanta, USA, October 11-15, 2027**, but as of 2026-11-24 its
  call is not out; treat the 2026 calendar as a template, not as 2027 dates.

## Fact discipline

This pack separates three classes of statement, and the skills keep them distinguishable:

1. **Verified 2026-cycle facts** — carry dates/caps and trace to a numbered source in the
   source map (e.g., the 12-page body, the two-cycle structure, the ACM badge set).
2. **Reported facts** — found only in secondary sources and labeled as such.
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as questions to
   resolve, never as facts (e.g., the camera-ready page allowance, the CCS 2027 call and
   cycle dates).

If you find any statement in the skills that presents class 2 or 3 material as class 1, treat
it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **2026-cycle snapshot**; reopen the current
  `sigsac.org/ccs/CCS<year>` CFP and the cycle's HotCRP site before deadline-sensitive advice.
- Items that could not be verified live on 2026-11-24 are marked 待核实 in the source map —
  notably every CCS 2027 rule and date, the exact rebuttal format, and the camera-ready page
  allowance. Do not state these as facts until confirmed.
- CCS chairs and policy re-set every edition and can differ between Cycle A and Cycle B; treat
  editor-style continuity assumptions (carried over from journal packs) as errors here.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a famous security result
  is not automatically a CCS paper.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
