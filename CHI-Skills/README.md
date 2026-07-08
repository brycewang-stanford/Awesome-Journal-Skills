# CHI Skills

Twelve agent skills for papers targeting **CHI — the ACM CHI Conference on Human
Factors in Computing Systems**, SIGCHI's flagship venue for human-computer
interaction: interaction techniques, user studies, accessibility, social computing,
design research, and human-centered AI. The pack covers the full arc of a CHI cycle:
deciding whether a project is CHI-shaped and which subcommittee should judge it,
building study evidence that survives rubric-based screening, packaging the
single-deadline submission with its video figure, working the two-round
revise-and-resubmit review, and delivering the TAPS camera-ready with its mandatory
accessibility pass.

Official basis checked on **2026-07-08**: the CHI 2027 Papers call and review-process
pages, the CHI 2027 cycle calendar, the CHI 2026 site and its Papers-track outcome
reports, the CHI Steering Committee's assisted-desk-reject rubric, SIGCHI's
accessibility and video guides for authors, and ACM's open-access policy pages.
Direct automated fetches of `chi2027.acm.org` and `chi2026.acm.org` returned 403 in
the verification environment, so official pages were read via search-engine
renderings of the exact URLs and cross-checked against SIGCHI, `chi.acm.org`, and the
ACM Digital Library; the full trail, including everything still marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes CHI different from its siblings

These venue mechanics, verified for the 2026→2027 cycles, drive most of the advice in
the skills — and most of the mistakes made by authors arriving from ML or systems
conferences:

- **PCS, not OpenReview or CMT.** Submission and review run on Precision Conference
  Solutions, and one September deadline collects *everything* — paper, video figure,
  and all supplementary material. There is no later supplement slot.
- **Words, not pages.** No fixed page limit: 5,000–8,000 words are encouraged,
  under 5,000 is a legitimate short paper reviewed to scale, and submissions above
  12,000 words face desk rejection when the length is not justified. Reviewers are
  told to weigh contribution against length.
- **The subcommittee is your jury.** Authors designate up to two reviewing
  subcommittees; that choice determines the 1AC, 2AC, and reviewer pool — the single
  most strategic field on the submission form.
- **Screening has teeth.** Beyond format desk rejects, a rubric-based *assisted*
  desk-reject step (SCs and ACs jointly) can end a submission for grossly
  insufficient contextualization, contribution-per-length, data, or methodological
  transparency — before external review begins.
- **Two rounds, not a rebuttal.** Round 1 accepts nothing; papers with at least one
  RR-or-better recommendation from the 1AC or 2AC get about five weeks to submit a
  tracked-changes revision plus response letter, and the PC meeting decides. At
  CHI 2026: 6,730 submissions, 38.7% invited to revise, 65.5% of resubmissions
  accepted, 25.3% overall.
- **Publication includes accessibility work.** Camera-ready flows through ACM TAPS;
  authors must supply alt text for every figure, tables must be real markup, and
  every video needs closed captions. Since January 1, 2026, all ACM publications are
  open access.

## Skills

| Skill | What it does |
| --- | --- |
| [`chi-topic-selection`](skills/chi-topic-selection/SKILL.md) | Ask who changes what they do because of the paper, type the contribution against CHI's own taxonomy, run the subcommittee fit test, and route honestly between CHI, UIST, CSCW, DIS, IUI, ASSETS, IMWUT, and TOCHI. |
| [`chi-workflow`](skills/chi-workflow/SKILL.md) | Run the one-deadline year: July site opening, September everything-due date, the five-week December revision window, the TAPS/publication-ready/registration chain, and the May conference — with owners and a risk register. |
| [`chi-writing-style`](skills/chi-writing-style/SKILL.md) | Build the typed contribution statement, write for a mixed-methods jury, handle participant voice, calibrate situated claims, and keep prose accessible and word counts defensible. |
| [`chi-related-work`](skills/chi-related-work/SKILL.md) | Cover the five literature lanes CHI checks — including the feeder disciplines — position by fronts rather than inventories, and defuse ADR-Context, the top assisted-desk-reject ground. |
| [`chi-experiments`](skills/chi-experiments/SKILL.md) | Match evidence shape to contribution type, power quantitative studies, make qualitative analysis auditable, and treat the participants-and-ethics section as results-page material. |
| [`chi-reproducibility`](skills/chi-reproducibility/SKILL.md) | Ship protocol-, analysis-, and data-layer transparency "as open as consent allows," with honest availability statements and cold-start verification. |
| [`chi-supplementary`](skills/chi-supplementary/SKILL.md) | Produce the captioned video figure and the anonymous supplement archive for the single September deadline, and the 30-second video preview at camera-ready. |
| [`chi-artifact-evaluation`](skills/chi-artifact-evaluation/SKILL.md) | Package prototypes, instruments, codebooks, and data for the five-minute reviewer and for archival release — in a venue with no badge committee doing it for you. |
| [`chi-submission`](skills/chi-submission/SKILL.md) | Final PCS audit: word-count regime, single-column template, the anonymization channels unique to HCI papers, desk-reject triage, and deadline-week order of operations. |
| [`chi-review-process`](skills/chi-review-process/SKILL.md) | Model the pipeline — 1AC/2AC and externals, the A/ARR/RR/RRX/X scale, DR and rubric-based ADR screening, the revise-and-resubmit threshold, the PC meeting — and read your reviews against the real funnel numbers. |
| [`chi-author-response`](skills/chi-author-response/SKILL.md) | Work the five-week window: triage the reviews, revise with an auditable diff, and write the response letter that carries round 2. |
| [`chi-camera-ready`](skills/chi-camera-ready/SKILL.md) | Convert acceptance into a published, *accessible* paper: TAPS source, alt text everywhere, e-rights and open access, video preview, registration deadlines. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve official sources with URLs and access dates; verified cycle facts; the explicit 待核实 list; the access-method note for the blocked conference domains. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces (CHI 2027, SIGCHI guides, PCS, TAPS, ACM DL) plus six author-side verification passes to run before each milestone. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five DL-metadata-verified CHI papers (2009–2023) across contribution-type × method lanes, with self-check questions and an anti-misattribution recipe. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional smart-speaker deployment abstract and introduction rebuilt against CHI's screening rubric, before → after. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared reproducibility kit, plus the five human-subjects checks (consent scope, participant de-identification, instruments, captions, pinned AI conditions) generic tooling cannot make. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./CHI-Skills
claude plugin install chi-skills
```

Or use the files directly: each `skills/chi-*/SKILL.md` is a standalone instruction
file whose frontmatter `description` tells an agent when to trigger it. Typical
invocations:

- "Is this a CHI paper or a UIST paper, and which subcommittee?" → `chi-topic-selection`
- "Audit my draft and supplement against the CHI submission rules" → `chi-submission`
- "We got a revise-and-resubmit — plan the five weeks" → `chi-author-response`
- "Get the camera-ready through TAPS with the accessibility requirements" → `chi-camera-ready`

## Pack structure

```text
CHI-Skills/
├── .claude-plugin/          # plugin.json + marketplace.json (12 skills declared)
├── README.md                # this file
├── README.zh-CN.md          # 中文说明
├── LICENSE                  # MIT
├── assets/cover.svg         # pack cover
├── skills/
│   └── chi-<topic>/SKILL.md # 12 skills, one directory each
└── resources/
    ├── README.md            # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md       # adapter to the shared repro kit
```

## Suggested use

1. **Before the study** — run `chi-topic-selection`; the contribution type decides
   the evidence plan, and the subcommittee decision decides the audience. Skim the
   exemplars library to see what each contribution type looks like in accepted form.
2. **While building evidence** — keep `chi-experiments` and `chi-reproducibility`
   open next to the study; consent scoped for archival sharing and instruments filed
   as you go are nearly free in April and very expensive in August.
3. **While writing** — `chi-writing-style` for the body, `chi-related-work` for
   positioning (it is now screening-critical), `chi-supplementary` for the video
   figure; compare your opening against the worked example.
4. **Deadline week** — `chi-submission` end to end on the exact files going into
   PCS, including the mechanical anonymity sweeps across PDF, archive, links, and
   audio track.
5. **After submission** — `chi-review-process` to read the round-1 packet,
   `chi-author-response` for the December window, then `chi-camera-ready` or the
   re-route triage in `chi-topic-selection` depending on December 17.

## Cycle anchor facts (historical snapshot, not permanent rules)

- CHI 2026: April 13–17, 2026, Barcelona, Spain. CHI 2027: May 10–14, 2027,
  Pittsburgh, Pennsylvania, USA.
- CHI 2027 Papers: PCS opens July 30, 2026; **everything due September 10, 2026**;
  revised papers due December 3; final notification December 17; TAPS source
  January 14, 2027; publication-ready February 18; registration and presentation
  video March 4.
- Length regime: 5,000–8,000 words encouraged; <5,000 short papers; >12,000
  desk-reject exposure; single-column ACM template for review.
- CHI 2026 funnel: 6,730 completed submissions → 2,603 invited to revise (38.7%) →
  1,705 conditionally accepted (25.3% overall; 65.5% of resubmissions).
- Screening: format desk rejects plus the rubric-based assisted desk reject
  (ADR-Context / ADR-Contribution / ADR-Data / ADR-Method), with ADR-Context the
  most-cited ground in 2026.
- Publication: ACM TAPS; author-supplied alt text mandatory; all ACM publications
  open access since January 1, 2026.

## Fact discipline

This pack separates three classes of statement, and the skills are written to keep
them distinguishable:

1. **Verified cycle facts** — carry dates/thresholds and trace to a numbered source
   in the source map (e.g., the September 10 deadline, the A/ARR/RR/RRX/X scale).
2. **Reported facts** — read only through secondary renderings or inferred from
   posted dates, and labeled as such (e.g., the likely timing of round-1
   notifications).
3. **Unverifiable-at-check-time items** — explicitly marked 待核实 and phrased as
   questions to resolve, never as facts (e.g., the CHI 2027 subcommittee list, PCS
   upload caps, registration rules).

If any statement in the skills presents class 2 or 3 material as class 1, treat it
as a bug and fix it against the live official pages.

## Maintenance notes

- Every date and threshold above is a **2026→2027-cycle snapshot**; reopen the
  current `chi<year>.acm.org` pages before giving deadline-sensitive advice.
- Items that could not be verified live on 2026-07-08 are marked 待核实 in the
  source map — notably the CHI 2027 subcommittee list, PCS file-size caps,
  registration and remote-presentation rules, AI-use policy wording, and the exact
  open-access arrangements for 2027 authors. Do not state these as facts until
  confirmed.
- CHI restructures its review process more often than most venues (the ADR rubric
  arrived for 2026; the word-count wording has shifted across recent cycles); treat
  process continuity assumptions as errors here.
- When adding exemplar papers, follow the verification recipe at the end of
  [`resources/exemplars/library.md`](resources/exemplars/library.md) — a PMLR-style
  shortcut does not exist for CHI; the ACM DL record is the only proof of venue.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
