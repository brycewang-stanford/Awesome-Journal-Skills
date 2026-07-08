# USENIX Security Skills

Twelve agent skills for papers targeting the **USENIX Security Symposium** — one of the
"Big Four" computer-security venues and, since USENIX ATC was discontinued after 2025,
USENIX's flagship summer event. The pack covers the full arc of a USENIX Security cycle:
deciding whether the work is an auditable security contribution, building
threat-model-faithful evidence, assembling the 13-page-plus-appendices submission,
surviving the two-cycle HotCRP review and shepherding process, and delivering the
open-access camera-ready plus the two-phase artifact evaluation.

Official basis checked on **2026-07-08**: the USENIX Security '26 Call for Papers and
Call for Artifacts, the per-cycle HotCRP deadline pages, the community artifact-evaluation
instructions, the USENIX Security ethics guidelines, the '25 reviewing-model page (used as
documented history), and the '27 conference page. Direct fetches of `usenix.org`,
`*.usenix.hotcrp.com`, and `dblp.org` returned HTTP 403 in the verification environment,
so official pages were read via search-engine renderings of the exact URLs and
cross-checked against multiple renderings, USENIX accepted-paper listings, and secondary
deadline trackers; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes USENIX Security different from its siblings

These venue mechanics, verified for the '26 cycle, drive most of the advice in the
skills — and most of the mistakes made by authors arriving from other conferences:

- **Two submission cycles a year, each a full HotCRP pipeline.** Every cycle opens with a
  mandatory paper **registration** roughly a week before the paper deadline; an
  unregistered paper cannot be uploaded. "When do we submit?" is a strategic choice, not
  a fixed date.
- **Major Revision is gone.** Beginning '26 the venue retired the Invited-Major-Revision
  outcome. Papers are now Accepted, **Accepted on Shepherd Approval** (at most a two-week
  shepherding pass — prose fixes, not new experiments), or rejected. The old
  submit-at-85%-and-revise safety net no longer exists.
- **Open Science is mandatory and acceptance-conditional.** Every submission carries an
  **Open Science appendix** stating where its artifacts live, and paper acceptance is
  conditioned on a **Phase-1 artifact-availability check** passing before finals are due.
- **Ethics is a gate, not a score.** A mandatory **Ethical Considerations appendix**,
  vulnerability-disclosure expectations, and IRB/human-subjects documentation for
  live-system work can sink a technically sound paper on their own.
- **Two-phase artifact evaluation with three independent badges** — Artifacts Available
  (mandatory), Artifacts Functional, and Results Reproduced (both optional, after finals).
- **Open access, no author fee.** USENIX publishes proceedings and talk recordings freely
  on usenix.org; the author-side obligation is presentation at the symposium.
- **Auditable evidence is the house style.** The reviewer pool prizes reproducible attacks,
  measured populations with stated vantage, and defenses tested against adaptive attackers.

## Skills

| Skill | What it does |
| --- | --- |
| [`usenixsec-topic-selection`](skills/usenixsec-topic-selection/SKILL.md) | Apply the remove-the-adversary test and route among USENIX Security, IEEE S&P, CCS, NDSS, and specialty venues (PETS, SOUPS, WOOT) by reviewer fit. |
| [`usenixsec-workflow`](skills/usenixsec-workflow/SKILL.md) | Choose between the two annual cycles, backward-plan from the registration wall, and assign the venue-specific risks to owners. |
| [`usenixsec-writing-style`](skills/usenixsec-writing-style/SKILL.md) | Put the threat model up front, calibrate security claims with populations and dispersion, and weave the disclosure narrative into the prose. |
| [`usenixsec-related-work`](skills/usenixsec-related-work/SKILL.md) | Cover the Big-Four and specialty lanes, handle concurrent work across the multi-cycle calendar, and cite your own work double-blind. |
| [`usenixsec-experiments`](skills/usenixsec-experiments/SKILL.md) | Match experiments to claim type — adaptive attackers for defenses, base rates for detection, vantage validity for measurement, ethics for live systems. |
| [`usenixsec-reproducibility`](skills/usenixsec-reproducibility/SKILL.md) | Write the Open Science appendix, decide what can and cannot be shared, and fingerprint time- and environment-coupled security experiments. |
| [`usenixsec-supplementary`](skills/usenixsec-supplementary/SKILL.md) | Route material across the 13-page body, the two mandatory appendices, optional appendices, and external artifacts by reading guarantee. |
| [`usenixsec-artifact-evaluation`](skills/usenixsec-artifact-evaluation/SKILL.md) | Pass the mandatory Phase-1 availability check and package hazardous security artifacts safely for optional Phase-2 badges. |
| [`usenixsec-submission`](skills/usenixsec-submission/SKILL.md) | Final HotCRP audit: registration, 13-page geometry, the two named appendices, mechanical anonymity sweeps, early-reject exposure. |
| [`usenixsec-review-process`](skills/usenixsec-review-process/SKILL.md) | Model the two-cycle pipeline, the retired Major Revision, shepherd-approval, and the resubmission restrictions between cycles. |
| [`usenixsec-author-response`](skills/usenixsec-author-response/SKILL.md) | Write the mid-review response that survives online discussion, handle required ethics revisions, and work with a shepherd after acceptance. |
| [`usenixsec-camera-ready`](skills/usenixsec-camera-ready/SKILL.md) | Convert acceptance into a correct open-access entry: de-anonymization, artifact-URL swap, Phase-1 sign-off, presenter obligations. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates; the access-method note; verified '26/'27 facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (HotCRP, CFP, Call for Artifacts, ethics, proceedings) plus the author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five verified USENIX Security '24 Distinguished Paper Award winners across five topic × evidence-shape lanes, with self-check questions and an anti-misattribution guide. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional certificate-pinning measurement abstract and introduction rebuilt to the USENIX Security bar, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared conference reproducibility kit, plus the USENIX Security-specific checks (hazards, Open Science, double-blind) the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./USENIX-Security-Skills
claude plugin install usenix-security-skills
```

Or use the files directly: each `skills/usenixsec-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this measurement study a USENIX Security paper or an IMC paper?" → `usenixsec-topic-selection`
- "Audit my draft against the USENIX Security submission rules" → `usenixsec-submission`
- "Reviews came in — help me plan the response" → `usenixsec-author-response`
- "Package my scanner for artifact evaluation" → `usenixsec-artifact-evaluation`

## Pack structure

```text
USENIX-Security-Skills/
├── .claude-plugin/              # plugin.json + marketplace.json (12 skills declared)
├── README.md                    # this file
├── README.zh-CN.md              # 中文说明
├── LICENSE                      # MIT
├── assets/cover.svg             # pack cover
├── skills/
│   └── usenixsec-<topic>/SKILL.md   # 12 skills, one directory each
└── resources/
    ├── README.md                # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md           # adapter to the shared repro kit
```

## Suggested use

1. **Before writing** — run `usenixsec-topic-selection`; if the remove-the-adversary test
   fails, this pack just saved you a cycle. Skim the exemplars library to see what an
   auditable security contribution looks like in award-winning form.
2. **While building** — keep `usenixsec-experiments` and `usenixsec-reproducibility` open
   next to the codebase; the adaptive-attacker experiment and the disclosure clock are
   cheaper to start early than to retrofit in deadline week.
3. **While writing** — `usenixsec-writing-style` for the body, `usenixsec-supplementary`
   for the body/appendix/artifact split, `usenixsec-related-work` for positioning;
   compare against the worked example's before/after.
4. **Deadline week** — `usenixsec-submission` end to end, including registration and the
   mechanical anonymity checks; mind the registration wall a week ahead of the paper
   deadline.
5. **After submission** — `usenixsec-review-process` to time expectations,
   `usenixsec-author-response` when reviews land, then `usenixsec-camera-ready` (with the
   Phase-1 artifact clock) or the rejection triage depending on the notification email.

## 2026/2027 anchor facts (historical snapshot, not permanent rules)

- **USENIX Security '26** is the 35th Symposium: **Baltimore Marriott Waterfront,
  August 12–14, 2026**. Program co-chairs: Elissa Redmiles (Georgetown) and Ben Stock
  (CISPA).
- **Sec '26 Cycle 1**: registration Aug 19, 2025 · submission Aug 26, 2025 · early reject
  Oct 7, 2025 · notification Dec 4, 2025 · finals Jan 15, 2026.
- **Sec '26 Cycle 2**: registration Jan 29, 2026 · submission Feb 5, 2026 · early reject
  Mar 17, 2026 · notification May 14, 2026 · finals Jun 11, 2026. All deadlines 11:59 pm AoE.
- **Format**: unaltered USENIX Security LaTeX template · ≤ 13-page body · mandatory
  "Ethical Considerations" and "Open Science" appendices (≤ 1 page each) before references.
- **USENIX Security '27** is the 36th Symposium: **Denver, August 11–13, 2027**, chairs
  Adam Doupé (Arizona State) and Andrei Sabelfeld (Chalmers); Cycle 1 registration
  Aug 18, 2026 / submission Aug 25, 2026; Cycle 2 registration Jan 19, 2027 / submission
  Jan 26, 2027.
- **Proceedings**: USENIX open access, no author fee.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified 2026/2027-cycle facts** — carry dates/caps and trace to a numbered source in
   the source map (e.g., the 13-page body, the Feb 5 Cycle-2 deadline).
2. **Reported facts** — found in secondary sources and labeled as such (e.g., the '27
   program co-chairs, sourced from conference-tracker renderings).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as questions
   to resolve, never as facts (e.g., the '27 notification dates, resubmission restrictions,
   any AI-use policy).

If you find any statement in the skills that presents class 2 or 3 material as class 1,
treat it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **cycle snapshot**; reopen the current
  `usenix.org/conference/usenixsecurity<NN>` pages and the per-cycle HotCRP site before
  giving deadline-sensitive advice.
- Items that could not be verified live on 2026-07-08 are marked 待核实 in the source map —
  notably the '27 early-reject/notification/finals dates, the '27 AoE convention,
  cross-cycle resubmission restrictions, and any AI-assistance policy. Do not state these
  as facts until confirmed.
- USENIX Security chairs rotate per edition and policy is re-set annually; treat
  editor-style continuity assumptions (carried over from journal packs) as errors here.
- **Major Revision was retired for '26** — if a skill or a memory says otherwise, it is
  stale. The current intermediate outcome is shepherd approval.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a matching title in
  a CVE or a talk does not prove the academic paper or the venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
