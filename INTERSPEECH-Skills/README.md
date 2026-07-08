# INTERSPEECH Skills

Twelve agent skills for papers targeting **Interspeech — the annual conference of
ISCA, the International Speech Communication Association** (carefully not the
computer-architecture symposium sharing the acronym). Interspeech is the broadest
speech venue in existence: automatic speech recognition, synthesis and voice
conversion, speaker and language recognition, phonetics and prosody, spoken
dialogue, speech health, and speech resources all review under one roof. The pack
walks the full annual arc — venue fit, the brutal 4-page format, CMT submission and
the post-deadline paper-update window, rebuttal, ISCA Archive camera-ready, audio
artifacts, and the conference itself.

Official basis checked on **2026-07-08**: the Interspeech 2026 (Sydney) site — call
for papers, submission policy, registration — plus the Interspeech 2025 policy
pages as immediate precedent, the ISCA Archive, ISCA's upcoming-conference and
awards pages, and the ASSTA mirror of the 2026 CFP. Direct fetches of the ISCA and
conference domains were blocked by the verification environment's gateway, so
official pages were read via search-engine renderings of exact URLs and
cross-checked against one another; the complete trail, including every item still
marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes Interspeech unlike its neighbors

These mechanics drive the advice in the skills — and the mistakes made by authors
arriving from NLP or big-ML venues:

- **Four pages, no appendix.** A regular paper is 4 content pages plus one page for
  references and acknowledgments *only*. There is no reviewed supplement; whatever
  decides acceptance must live on the four pages. A **Long Paper track** debuted in
  2026 (reported: 8 pages + 2 reference pages, target acceptance below 30%).
- **The paper-update window.** Uniquely among the majors, Interspeech lets authors
  revise the PDF for about a week after the deadline (25 Feb → 4 Mar in 2026) while
  metadata stays frozen — a sanctioned proofread pass, not an extension.
- **Reviewers listen.** Audio sample pages are consumed as evidence for synthesis,
  conversion, and enhancement papers — and are also the most common anonymity leak.
- **Double-anonymous with an anonymity period.** Since 2025, non-anonymized
  postings (arXiv included) are forbidden from one month before the deadline until
  decisions.
- **Open-access proceedings, no author fee.** Every paper enters the ISCA Archive
  (isca-archive.org) with a `10.21437` DOI; the cost model is registration — and at
  least one author must register for the paper to appear at all.
- **A mixed jury.** Phoneticians and engineers review in adjacent areas; papers
  must survive both the "where is the significance test?" reader and the "where is
  the error analysis?" reader.

## Skills

| Skill | What it does |
| --- | --- |
| [`interspeech-topic-selection`](skills/interspeech-topic-selection/SKILL.md) | Apply the modality test (does the claim survive transcript-only?) and route between Interspeech, ICASSP, ASRU/SLT, Odyssey, SSW, ACL-family, and speech journals. |
| [`interspeech-workflow`](skills/interspeech-workflow/SKILL.md) | Run the annual clock — winter deadline, update window, spring rebuttal, June verdict, registration coupling, September conference — with owners per phase. |
| [`interspeech-writing-style`](skills/interspeech-writing-style/SKILL.md) | Achieve the one-pass property in 4 pages: numeric abstracts, diff-based method description, protocol one-liners, and the honest compression order. |
| [`interspeech-related-work`](skills/interspeech-related-work/SKILL.md) | Cover the five lanes (ISCA Archive lineage, IEEE siblings, challenge canon, ML/NLP crossover, corpus papers) and dodge the venue-misattribution traps. |
| [`interspeech-experiments`](skills/interspeech-experiments/SKILL.md) | Match metrics to task law (WER, MOS/CMOS, EER/minDCF, PESQ/STOI), anchor baselines to public recipes, and test significance over the right randomness. |
| [`interspeech-reproducibility`](skills/interspeech-reproducibility/SKILL.md) | Pin the five decay channels: corpus versions, text normalization, trial lists, subjective protocols, and seeds — and ship the scoring ruler, not just the model. |
| [`interspeech-supplementary`](skills/interspeech-supplementary/SKILL.md) | Manage the three shelves — 4 pages, references page, optional accompaniment — and curate audio sample pages reviewers actually open. |
| [`interspeech-artifact-evaluation`](skills/interspeech-artifact-evaluation/SKILL.md) | Package audio demos, recipes, and checkpoints: anonymous during review, permanent after, with corpus-license chains and speaker-consent hygiene. |
| [`interspeech-submission`](skills/interspeech-submission/SKILL.md) | Final CMT audit: 4+1 format and PDF checker, anonymity sweep including demo pages, area and metadata strategy, and the update-window plan. |
| [`interspeech-review-process`](skills/interspeech-review-process/SKILL.md) | Model the area-based pipeline, what the young rebuttal can move, oral/poster allocation, awards, and how to decode a decision letter. |
| [`interspeech-author-response`](skills/interspeech-author-response/SKILL.md) | Answer a mixed science/engineering review set from the 4-page record, in dialect, within the cap, for the meta-reviewer. |
| [`interspeech-camera-ready`](skills/interspeech-camera-ready/SKILL.md) | Convert acceptance into a correct ISCA Archive entry: de-anonymization order, registration coupling, DOI metadata, and presentation with audio fallbacks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Ten sources with URLs and access dates; the verified 2026 fact base; reported-only items; the 待核实 list; the gateway access-method note. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five author-side verification passes and a conflict rule. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five ISCA-Archive-verified exemplars (Conformer, SpecAugment, ECAPA-TDNN, Tacotron, SUPERB) with DOIs, self-checks, and a misattribution guard. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional streaming-ASR first page rewritten from NLP-flavored draft into the Interspeech one-pass shape. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus five speech-specific manual checks. |

## Installation and use

As a Claude Code plugin (this directory is a self-contained plugin with its own
marketplace manifest):

```bash
# From a clone of the repository
claude plugin marketplace add ./INTERSPEECH-Skills
claude plugin install interspeech-skills
```

Or use the files directly — each `skills/interspeech-*/SKILL.md` is a standalone
instruction file whose frontmatter `description` tells an agent when to fire.
Typical invocations:

- "Is this speech-LLM paper Interspeech or EMNLP?" → `interspeech-topic-selection`
- "Get my draft down to four pages without losing the claim" → `interspeech-writing-style`
- "Audit the demo page before I submit" → `interspeech-artifact-evaluation`
- "We got accepted — what happens before Sydney?" → `interspeech-camera-ready`

## Pack structure

```text
INTERSPEECH-Skills/
├── .claude-plugin/                 # plugin.json + marketplace.json (12 skills)
├── README.md                       # this file
├── README.zh-CN.md                 # 中文说明
├── LICENSE                         # MIT
├── assets/cover.svg                # pack cover (waveform)
├── skills/
│   └── interspeech-<topic>/SKILL.md  # 12 skills, one directory each
└── resources/
    ├── README.md                   # resource guide + suggested route
    ├── official-source-map.md
    ├── external_tools.md
    ├── exemplars/library.md
    ├── worked-examples/01-introduction.md
    └── code/README.md              # shared repro-kit adapter
```

## 2026 anchor facts (snapshot, not permanent rules)

- Interspeech 2026: **Sydney, Australia, 27 September – 1 October 2026**, hosted
  with ASSTA; theme **"Speaking Together"**.
- 2026 pipeline: portal open 17 Jan · paper deadline **25 Feb** · paper-update
  close **4 Mar** · rebuttal reported 24 Apr – 1 May (待核实) · notification
  **5 Jun** · camera-ready **19 Jun** · early-bird registration closes **15 Jul** ·
  standard closes 16 Aug.
- Format: regular papers 4 content pages + 1 references/acknowledgments page;
  Long Paper track new in 2026 (parameters reported, 待核实).
- Proceedings: ISCA Archive, open access, DOI prefix 10.21437, no author fee.
- Next editions: **Interspeech 2027, São Paulo, Brazil, 29 Aug – 2 Sep 2027**
  (first South American edition); Interspeech 2028, San Antonio, USA.

## Fact discipline

Three statement classes are kept distinguishable throughout the pack:

1. **Verified 2026-cycle facts** — traceable to a numbered source in the source
   map (the 25 Feb deadline, the 19 Jun camera-ready, the Sydney dates).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (the rebuttal window, Long Paper parameters, the 2026 committee names).
3. **待核实 items** — unresolved at check time and phrased as questions, never as
   facts (attachment caps, review-form wording, any AI-use policy, all 2027 rules).

If a skill states class-2/3 material as class 1, treat it as a bug and repair it
against the live official pages.

## Maintenance notes

- Every date above is a **Sydney-cycle snapshot**. ISCA editions are run by
  rotating local committees and Technical Program Chairs; nothing carries to
  São Paulo 2027 automatically — not the tracks, not the rebuttal, not the portal.
- The pack was verified through gateway-limited access (renderings, not direct
  fetches); the first maintenance task each cycle is to re-open the primary URLs
  directly and refresh
  [`resources/official-source-map.md`](resources/official-source-map.md).
- New exemplars must be verified against the ISCA Archive per the recipe at the
  end of [`resources/exemplars/library.md`](resources/exemplars/library.md) —
  speech's famous papers are scattered across ICASSP/NeurIPS/ICML/LREC, and venue
  misattribution is the characteristic error to guard against.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
