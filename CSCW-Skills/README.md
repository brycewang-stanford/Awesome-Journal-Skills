# CSCW Skills

Twelve agent skills for papers targeting **CSCW — the ACM SIGCHI Conference on
Computer-Supported Cooperative Work and Social Computing**, the field's home for
research on how technology shapes and supports groups, communities, organizations,
and cooperative work. The pack covers the full life of a CSCW paper: deciding
whether the group is genuinely the unit of analysis, building methods-pluralist
evidence, submitting into a journal-model pipeline, surviving Revise-and-Resubmit
rounds with the same reviewers, and landing a PACMHCI article plus a conference
talk.

Official basis re-checked on **2026-11-24**: the CSCW 2027 site, Submit and
organizing-committee pages, the rolling CFP and track guidelines for CSCW 2027 and
beyond, the CSCW 2026 Call for Papers, review-process FAQ and decision blog posts,
the ACM Digital Library PACMHCI CSCW track, and dblp. `cscw.acm.org` was read
directly; `dl.acm.org`, Manuscript Central and the ACM CSCW Medium blog refused
automated access, so the detailed July 2026 rolling CFP was read from an Internet
Archive capture; the full trail, including every item marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes CSCW different from its siblings

CSCW looks like a conference and reviews like a journal — and it is mid-transition
to being one structurally. These verified mechanics drive the advice in the skills:

- **Papers are journal articles.** Accepted work is published in **PACMHCI
  (Proceedings of the ACM on Human-Computer Interaction)**, in dedicated CSCW
  issues (e.g., Vol. 8: CSCW1 April 2024 with 209 papers, CSCW2 November 2024 with
  171), not in a standalone proceedings volume.
- **Revise-and-Resubmit is the main sequence.** In the last fixed cycle, 66.2% of
  papers surviving external review received R&R, and revised papers return to the
  **same reviewers**. The response letter, not a rebuttal box, is the venue's
  persuasion instrument.
- **The deadline is gone.** The May 14, 2025 deadline (PCS) was the last fixed
  cutoff. CSCW 2027 (Philadelphia, October 16-20, 2027) and beyond run **rolling
  submissions to PACM HCI/CSCW** (ToCHI acceptances in CSCW scope also earn a
  slot) — via Manuscript Central (mc.manuscriptcentral.com/pacmhci) under an
  editorial board with EiCs Amy Bruckman and Eric Gilbert and decisions in roughly
  3-4 months, per the July 2026 rolling CFP.
- **Length is a claim, not a limit.** No page cap; instead a scrutiny band
  (roughly 5,000-12,000 words) and an explicit desk-reject ground for length
  incommensurate with contribution.
- **Methods pluralism is real.** Interviews, ethnography, trace analysis, surveys,
  deployments, and theory all publish here, each held to its own tradition's rigor
  — the venue's own Lasting Impact Award list spans all of them.
- **The studied community is a stakeholder.** Anonymization runs two layers deep
  (authors *and* settings), and data release is governed by consent scope and
  community exposure, not by reproducibility maximalism.

## Skills

| Skill | What it does |
| --- | --- |
| [`cscw-topic-selection`](skills/cscw-topic-selection/SKILL.md) | Apply the unit-of-analysis test and run the routing decision against CHI, ICWSM, DIS, GROUP, TOCHI, and FAccT. |
| [`cscw-workflow`](skills/cscw-workflow/SKILL.md) | Plan the journal-model campaign: rolling submission timing, R&R capacity budgeting, and conference-year back-planning. |
| [`cscw-writing-style`](skills/cscw-writing-style/SKILL.md) | Keep every claim at the group level, name a reusable concept, handle participant voice, and defend the word count. |
| [`cscw-related-work`](skills/cscw-related-work/SKILL.md) | Braid four literatures, cite CSCW era-correctly (proceedings vs. PACMHCI), and survive same-reviewer re-reads. |
| [`cscw-experiments`](skills/cscw-experiments/SKILL.md) | Design methods-pluralist evidence — interview, ethnographic, trace, survey, deployment — each rigorous by its own tradition. |
| [`cscw-reproducibility`](skills/cscw-reproducibility/SKILL.md) | Build auditability where sharing is impossible: codebooks, decision logs, trace-pipeline ledgers, honest availability statements. |
| [`cscw-supplementary`](skills/cscw-supplementary/SKILL.md) | Split material across paper, appendix, and supplement; scrub identity from documents, archives, and extracts; version by round. |
| [`cscw-artifact-evaluation`](skills/cscw-artifact-evaluation/SKILL.md) | Package artifacts under community-protection tests: quote-search, join attacks, community exposure, ETHICS.md. |
| [`cscw-submission`](skills/cscw-submission/SKILL.md) | Verify the live pathway, audit the two anonymity layers, check the length band, and run the pre-upload sequence. |
| [`cscw-review-process`](skills/cscw-review-process/SKILL.md) | Decode the decision ladder, the R&R base rates, the rolling editorial board, and what silence at each month means. |
| [`cscw-author-response`](skills/cscw-author-response/SKILL.md) | Triage reviewer requests across method traditions and write the point-by-point response letter the same reviewers reread. |
| [`cscw-camera-ready`](skills/cscw-camera-ready/SKILL.md) | Run the two acceptance tracks: PACMHCI production (conditions, deanonymization, TAPS) and the conference presentation. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates, verified facts, and the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five verified CSCW papers — four Lasting Impact Award winners plus a PACMHCI-era anchor — spanning the venue's methods registers. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional moderation-team study's abstract and introduction rebuilt from individual-user to group-level framing. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, scoped to the computational slice with pointers for what it cannot check. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./CSCW-Skills
claude plugin install cscw-skills
```

Or use the files directly: each `skills/cscw-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to trigger it.
Typical invocations:

- "Is this collaboration study a CSCW paper or a CHI paper?" → `cscw-topic-selection`
- "We got Revise and Resubmit — plan the revision" → `cscw-author-response`
- "Audit my interview study's methods section" → `cscw-experiments`
- "Can we release this community dataset?" → `cscw-artifact-evaluation`

## Pack structure

```text
CSCW-Skills/
├── .claude-plugin/           # plugin.json + marketplace.json (12 skills declared)
├── README.md                 # this file
├── README.zh-CN.md           # 中文说明
├── LICENSE                   # MIT
├── assets/cover.svg          # pack cover
├── skills/
│   └── cscw-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md             # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md        # adapter to the shared repro kit
```

## Suggested use

1. **Before the study** — run `cscw-topic-selection` on the project's core claim;
   if no collective completes "we show that ___", the pack just saved you a year.
   Design evidence with `cscw-experiments`, including ethics and quote policy.
2. **While writing** — `cscw-writing-style` for group-level prose and the length
   defense, `cscw-related-work` for era-correct positioning, and the worked
   example as a before/after mirror.
3. **Before upload** — `cscw-submission` end to end, starting with the pathway
   check (the platform changed in 2026), plus `cscw-supplementary` for the
   package.
4. **In the pipeline** — `cscw-review-process` to read decisions and silences;
   `cscw-author-response` when the R&R lands (it probably will: 66.2% base rate
   in the last verified cycle).
5. **After acceptance** — `cscw-camera-ready` for the two tracks, and
   `cscw-artifact-evaluation` for the public release.

## Anchor facts (snapshot of 2026-11-24, not permanent rules)

- **CSCW 2027:** Philadelphia, PA, USA, **October 16-20, 2027** (Loews Philadelphia
  Hotel); General Chairs Louise Barkhuus and Andrew Miller, Technical Program Chairs
  Jed Brubaker and Elizabeth Churchill. No paper deadline: a paper accepted before
  the program is set is invited to CSCW 2027; later acceptances go to the following
  year.
- **CSCW 2026:** Salt Lake City, Utah, USA, **October 10-14, 2026** (met).
  CSCW 2025 was Bergen, Norway, October 18-22, 2025.
- **Final fixed cycle (feeds CSCW 2026):** submissions May 14, 2025, 12:00 EDT on
  PCS → Revise-for-External-Review resubmissions September 16, 2025 → external-review
  decisions November 11, 2025 (33.8% final, 66.2% R&R) → R&R due January 13, 2026 →
  final decisions late March 2026 (152 accepted, 44 rejected).
- **Rolling model (CSCW 2027+):** no deadlines; five tracks (Design/Theory, Mixed
  Methods, Qualitative, Quantitative, Systems); per the July 2026 rolling CFP,
  Manuscript Central (mc.manuscriptcentral.com/pacmhci), EiCs Amy Bruckman and Eric
  Gilbert, ~3-4 months to decision; publication in PACMHCI; presentation optional.
- **Format:** single-column ACM Small (acmsmall) template; no length cap;
  5,000-12,000 word scrutiny band; anonymous review with author names,
  affiliations, and identifying grant details removed; LLM-generated text must be
  clearly marked where used beyond editing.

## Fact discipline

Three classes of statement are kept distinguishable throughout the pack:

1. **Verified facts** — carry dates and trace to a numbered source in the source
   map (e.g., the May 2025 cycle statistics, the rolling platform).
2. **Reported facts** — found in secondary renderings and labeled as such.
3. **Unverifiable-at-check-time items** — marked 待核实 and phrased as questions
   to resolve (e.g., the date the conference program is set, live confirmation of
   the Manuscript Central portal and EiCs, TAPS specifics, registration rules).

If any skill statement presents class 2 or 3 material as class 1, treat it as a
bug and fix it against the live official pages.

## Maintenance notes

- CSCW's rolling model is explicitly a **soft launch**; its mechanics (platforms,
  pace, track structure, issue assignment) may be tuned within months. Reopen
  cscw.acm.org/rolling.html before any deadline-sensitive advice.
- The fixed-cycle facts in this pack are **historical anchors** for calibration,
  not live rules — the May 2025 cycle will not recur.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md); era-correct
  citation (proceedings vs. PACMHCI) is part of the check.
- Editors-in-Chief and board composition can change; re-verify names before citing
  them.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
