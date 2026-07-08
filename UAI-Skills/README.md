# UAI Skills

Twelve agent skills for papers targeting **UAI — the Conference on Uncertainty in
Artificial Intelligence**, the AUAI's annual venue for probabilistic reasoning,
graphical models, causal inference, Bayesian methods, and decision making under
uncertainty. The pack covers the full arc of a UAI cycle: deciding whether uncertainty
is genuinely the contribution, building inference-grade evidence, packaging the
single-PDF submission, surviving OpenReview review and author response, and delivering
the PMLR camera-ready plus poster and spotlight.

Official basis checked on **2026-07-08**: the UAI 2026 Call for Papers, submission
instructions, important-dates page, reviewer/AC instructions, the UAI 2026 OpenReview
group, the AUAI code of conduct, and the PMLR proceedings volumes for UAI 2020–2025.
Direct fetches of `auai.org` were blocked in the verification environment, so official
pages were read via search-engine renderings of the exact URLs and cross-checked
against OpenReview, PMLR volume pages, and the `mlresearch` metadata repositories; the
full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes UAI different from its siblings

These venue mechanics, verified for the 2026 cycle, drive most of the advice in the
skills — and most of the mistakes made by authors arriving from other conferences:

- **One PDF carries everything reviewed.** The 8-page main part is followed by
  unlimited references and appendices *in the same file* (≤ 15 MB). There is no
  separate supplement deadline; proofs are always on the reviewed record.
- **The ZIP is optional reading.** A supplementary archive (≤ 50 MB, code/data) may
  accompany the PDF, but reviewers are explicitly not required to consult it — so
  nothing decision-critical may live only there.
- **Four posted criteria.** Reviews assess technical correctness, novelty, whether
  claims are backed up convincingly, and clarity of writing.
- **A reviewer-volunteer clause.** Submitting authors agree that at least one author
  will review if the Program Chairs ask.
- **All accepted papers get posters plus spotlights** (physically or remotely in the
  2026 wording), with longer talks for selected papers, and all are published
  open-access in a PMLR volume with no author fee.
- **Uncertainty is the subject.** The reviewer pool concentrates on probabilistic
  inference, graphical models, causality, and Bayesian statistics; papers where the
  probability is decorative get re-routed by reviewers even when technically solid.

## Skills

| Skill | What it does |
| --- | --- |
| [`uai-topic-selection`](skills/uai-topic-selection/SKILL.md) | Apply the deletion test — does anything remain if the probability is removed? — and route between UAI, AISTATS, NeurIPS/ICML, COLT, CLeaR, and journals. |
| [`uai-workflow`](skills/uai-workflow/SKILL.md) | Run the one-deadline year: February submission, spring review phases, June decision, July camera-ready, August conference, with named owners per risk. |
| [`uai-writing-style`](skills/uai-writing-style/SKILL.md) | Enforce notation discipline (conditioning vs `do(·)`), labeled assumption ledgers, an 8-page argument spine, and calibrated claims. |
| [`uai-related-work`](skills/uai-related-work/SKILL.md) | Cover the five literature lanes UAI reviewers check, verify PMLR volume ↔ venue attribution, and keep self-citations double-blind. |
| [`uai-experiments`](skills/uai-experiments/SKILL.md) | Design the exact-truth / stress / real-data ladder, pick metrics that measure the claimed probabilistic object, and report dispersion over seeds. |
| [`uai-reproducibility`](skills/uai-reproducibility/SKILL.md) | Build determinism ledgers, sampler diagnostics, ELBO and coverage traces, and honest availability statements. |
| [`uai-supplementary`](skills/uai-supplementary/SKILL.md) | Split content across the three tiers — 8-page body, in-PDF appendix, optional ZIP — by review status, not by convenience. |
| [`uai-artifact-evaluation`](skills/uai-artifact-evaluation/SKILL.md) | Package code and data for the five-minute skeptic: one command per claim, anonymous end to end, under the size cap. |
| [`uai-submission`](skills/uai-submission/SKILL.md) | Final OpenReview audit: caps, template, anonymity sweep with mechanical checks, dual-submission and volunteer-reviewer items, desk-risk triage. |
| [`uai-review-process`](skills/uai-review-process/SKILL.md) | Model the pipeline — bidding, reviews, author response, reviewer-AC discussion, decision — and where author leverage actually exists. |
| [`uai-author-response`](skills/uai-author-response/SKILL.md) | Map objections onto the four criteria and answer with numbered, evidence-anchored, anonymous replies built for the AC discussion. |
| [`uai-camera-ready`](skills/uai-camera-ready/SKILL.md) | Convert acceptance into a correct PMLR entry: de-anonymization, forms, public artifacts, poster and spotlight preparation. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten official sources with URLs and access dates; verified 2026 facts; the explicit 待核实 list. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes to run before upload. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five metadata-verified UAI papers (PMLR v161/v216/v244) across five topic × method lanes, with self-check questions and an anti-misattribution guide. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional causal-discovery abstract and introduction rebuilt to the four review criteria, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit, plus the UAI-specific checks the generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./UAI-Skills
claude plugin install uai-skills
```

Or use the files directly: each `skills/uai-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this identifiability result a UAI paper or an AISTATS paper?" → `uai-topic-selection`
- "Audit my draft against the UAI submission rules" → `uai-submission`
- "Reviews came in — help me plan the response" → `uai-author-response`
- "Package my sampler experiments for the supplement" → `uai-artifact-evaluation`

## Pack structure

```text
UAI-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json (12 skills declared)
├── README.md                # this file
├── README.zh-CN.md          # 中文说明
├── LICENSE                  # MIT
├── assets/cover.svg         # pack cover
├── skills/
│   └── uai-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md            # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # adapter to the shared repro kit
```

## Suggested use

1. **Before writing** — run `uai-topic-selection`; if the deletion test fails, this
   pack just saved you a cycle. Skim the exemplars library to see what "uncertainty as
   the contribution" looks like in accepted form.
2. **While building** — keep `uai-experiments` and `uai-reproducibility` open next to
   the codebase; the three-regime ladder and determinism ledger are cheaper to install
   early than to retrofit in deadline week.
3. **While writing** — `uai-writing-style` for the body, `uai-supplementary` for the
   body/appendix/ZIP split, `uai-related-work` for positioning; compare against the
   worked example's before/after.
4. **Deadline week** — `uai-submission` end to end, including the mechanical anonymity
   and size checks on the merged PDF.
5. **After submission** — `uai-review-process` to time expectations,
   `uai-author-response` when reviews land, then `uai-camera-ready` or the rejection
   triage depending on June's email.

## 2026 anchor facts (historical snapshot, not permanent rules)

- UAI 2026 is the **42nd** edition: Amsterdam, Netherlands, **August 17–21, 2026**
  (tutorials Monday, main conference Tuesday–Thursday, workshops Friday).
- Submission window: **January 25 – February 25, 2026, 23:59 AoE**, on OpenReview.
- 2026 pipeline: bidding Mar 2–9 · reviews Mar 21–Apr 11 · author response
  Apr 23–May 2 · reviewer-AC discussion May 2–8 · notification Jun 1 ·
  camera-ready Jul 27.
- Format: UAI LaTeX template · main part ≤ 8 pages · unlimited references/appendices in
  the same PDF · PDF ≤ 15 MB · optional ZIP ≤ 50 MB.
- Proceedings: PMLR (open access, no author fee). Volume anchors: v124 = 2020,
  v161 = 2021, v180 = 2022, v216 = 2023, v244 = 2024, v286 = 2025.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep
them distinguishable:

1. **Verified 2026-cycle facts** — carry dates/caps and trace to a numbered source in
   the source map (e.g., the 8-page main part, the February 25 deadline).
2. **Reported facts** — found only in secondary sources and labeled as such (e.g.,
   the 2026 general chairs, sourced from an organizer's homepage).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as
   questions to resolve, never as facts (e.g., registration rules, LLM policy).

If you find any statement in the skills that presents class 2 or 3 material as
class 1, treat it as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and cap above is a **2026-cycle snapshot**; reopen the current
  `auai.org/uai<year>/` pages before giving deadline-sensitive advice.
- Items that could not be verified live on 2026-07-08 are marked 待核实 in the source
  map — notably the 2026 Program Chairs, camera-ready page allowance, registration and
  remote-presentation rules, any LLM/AI-use policy, and the 2026 PMLR volume number.
  Do not state these as facts until confirmed.
- UAI chairs rotate per edition and policy is re-set annually; treat editor-style
  continuity assumptions (carried over from journal packs) as errors here.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — PMLR volume
  numbers alone do not prove the venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
