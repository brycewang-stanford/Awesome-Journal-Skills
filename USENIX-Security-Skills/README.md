# USENIX Security Skills

Twelve agent skills for papers targeting the **USENIX Security Symposium** — one of the
"Big Four" computer-security venues and, since USENIX ATC was discontinued after 2025,
USENIX's flagship summer event. The pack covers the full arc of a USENIX Security cycle:
deciding whether the work is an auditable security contribution, building
threat-model-faithful evidence, assembling the 13-page-plus-appendices submission,
surviving the two-cycle HotCRP review and shepherding process, and delivering the
open-access camera-ready plus the two-phase artifact evaluation.

Official basis first checked on 2026-07-08 and **re-verified 2026-11-24** by direct fetch
of the USENIX Security '27 Call for Papers, the '27 Preliminary Call for Artifacts, the '27
symposium page and the '26 Call for Papers. The pack now describes **USENIX Security '27**
(Denver, August 11–13, 2027); its Cycle 2 is the open door (registration Jan 19, papers
Jan 26, 2027, AoE). The full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes USENIX Security different from its siblings

These venue mechanics, verified for the '27 cycles, drive most of the advice in the
skills — and most of the mistakes made by authors arriving from other conferences:

- **Two submission cycles a year, each a full HotCRP pipeline.** Every cycle opens with a
  mandatory paper **registration** a week before the paper deadline (fixed title, authors
  with ORCIDs, topics); an unregistered paper cannot be uploaded. Each author may submit at
  most **seven papers per cycle**, and a '27 Cycle-1 reject may not enter '27 Cycle 2. "When do we submit?" is a strategic choice, not
  a fixed date.
- **Major Revision is gone.** Beginning '26 the venue retired the Invited-Major-Revision
  outcome, and '27 keeps it that way. Papers are Accepted, **Accepted on Shepherd
  Approval** (a short shepherding pass — about 12 days in '27; prose fixes, not new
  experiments), or rejected. The old
  submit-at-85%-and-revise safety net no longer exists.
- **Open Science is mandatory and acceptance-conditional.** Every submission carries an
  **Open Science appendix** stating where its artifacts live (anonymous links, a 3-day
  upload grace period, then frozen), and paper acceptance is conditioned on a **Phase-1
  artifact-availability check** passing before finals are due.
- **Ethics is a gate, not a score.** The **Ethical Considerations appendix** is no longer
  mandatory in '27 but is strongly encouraged; reviewers judge every paper's ethics and may
  reject on ethical grounds, so disclosure expectations and IRB/human-subjects documentation
  for live-system work can still sink a technically sound paper.
- **AI tools are allowed, fabrication is misconduct.** The '27 CFP permits AI assistance
  but treats hallucinated references or invented results as grounds for desk rejection.
- **Two-phase artifact evaluation with three independent badges** — Artifacts Available
  (mandatory), Artifacts Functional, and Results Reproduced (both optional, after finals).
- **Open access, no author fee.** USENIX publishes proceedings and talk recordings freely
  on usenix.org; the author-side obligation is one full-price registration per paper and
  presentation at the symposium.
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
| [`usenixsec-supplementary`](skills/usenixsec-supplementary/SKILL.md) | Route material across the 13-page body, the Open Science and Ethics appendices, optional appendices, and external artifacts by reading guarantee. |
| [`usenixsec-artifact-evaluation`](skills/usenixsec-artifact-evaluation/SKILL.md) | Pass the mandatory Phase-1 availability check and package hazardous security artifacts safely for optional Phase-2 badges. |
| [`usenixsec-submission`](skills/usenixsec-submission/SKILL.md) | Final HotCRP audit: registration with ORCIDs, 13-page geometry, the named appendices, mechanical anonymity sweeps, early-reject exposure. |
| [`usenixsec-review-process`](skills/usenixsec-review-process/SKILL.md) | Model the two-cycle pipeline, the retired Major Revision, shepherd-approval, and the resubmission restrictions between cycles. |
| [`usenixsec-author-response`](skills/usenixsec-author-response/SKILL.md) | Write the mid-review response that survives online discussion, handle required ethics revisions, and work with a shepherd after acceptance. |
| [`usenixsec-camera-ready`](skills/usenixsec-camera-ready/SKILL.md) | Convert acceptance into a correct open-access entry: de-anonymization, artifact-URL swap, Phase-1 sign-off, presenter obligations. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates; the access-method note; verified '27 facts and '26 history; the explicit 待核实 list. |
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

## USENIX Security '27 anchor facts (cycle snapshot, not permanent rules)

- **USENIX Security '27** is the 36th Symposium: **Hyatt Regency Denver at Colorado
  Convention Center, August 11–13, 2027**. Program co-chairs: Adam Doupé (Arizona State)
  and Andrei Sabelfeld (Chalmers).
- **Sec '27 Cycle 1**: registration Aug 18, 2026 · submission Aug 25, 2026 · artifacts
  Aug 28 · early reject Oct 6 · rebuttal Nov 5–12 · notification Dec 3 · shepherded approval
  Dec 15, 2026 · finals Jan 14, 2027.
- **Sec '27 Cycle 2**: registration Jan 19, 2027 · submission Jan 26, 2027 · artifacts
  Jan 29 · early reject Mar 9 · rebuttal Apr 8–15 · notification May 6 · shepherded approval
  May 18 · finals Jun 3, 2027. All deadlines AoE.
- **Format**: unaltered USENIX Security LaTeX template · ≤ 13-page body excluding references
  and appendices · mandatory "Open Science" appendix · "Ethical Considerations" appendix
  strongly encouraged · unlimited appendices at submission · **20 pages total** at
  camera-ready.
- **Policies**: at most 7 papers per author per cycle · SoK papers solicited ("SoK: "
  prefix), no Replication submissions in '27 · AI tools allowed, fabrication is misconduct.
- **History**: USENIX Security '26 (35th) met at the Baltimore Marriott Waterfront,
  August 12–14, 2026, under Elissa Redmiles and Ben Stock; its Ethics appendix was mandatory.
- **Proceedings**: USENIX open access, no author fee.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep them
distinguishable:

1. **Verified '27-cycle facts** — carry dates/caps and trace to a numbered source in
   the source map (e.g., the 13-page body, the Jan 26, 2027 Cycle-2 deadline).
2. **Reported facts** — found in secondary sources and labeled as such.
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as questions
   to resolve, never as facts (e.g., the '27 rebuttal format, the '27 presentation format,
   the '27 Cycle-2 HotCRP URL).

If you find any statement in the skills that presents class 2 or 3 material as class 1,
treat it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **cycle snapshot**; reopen the current
  `usenix.org/conference/usenixsecurity<NN>` pages and the per-cycle HotCRP site before
  giving deadline-sensitive advice.
- Items that could not be verified live on 2026-11-24 are marked 待核实 in the source map —
  notably the '27 rebuttal format, the '27 presentation format, and the '27 Cycle-2 HotCRP
  URL. Do not state these as facts until confirmed.
- USENIX Security chairs rotate per edition and policy is re-set annually; treat
  editor-style continuity assumptions (carried over from journal packs) as errors here.
- **Major Revision was retired for '26 and stays retired in '27** — if a skill or a memory
  says otherwise, it is stale. The current intermediate outcome is shepherd approval.
- **The Ethics appendix became optional (strongly encouraged) in '27** — skills that call
  it mandatory describe '26.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a matching title in
  a CVE or a talk does not prove the academic paper or the venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
