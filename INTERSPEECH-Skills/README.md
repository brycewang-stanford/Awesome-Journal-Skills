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

Official basis first checked on **2026-07-08** (the Interspeech 2026 Sydney site,
read via search-engine renderings because the gateway blocked direct fetches) and
**re-verified and moved to Interspeech 2027 on 2026-11-24** by direct fetch of the
Interspeech 2027 (São Paulo) home page, Call for Papers, committees and theme pages,
plus the Interspeech 2026 call, author instructions and submission policy; the ISCA
Archive and ISCA's upcoming-conference and awards pages complete the basis. The
complete trail, including every item still
marked 待核实, is in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes Interspeech unlike its neighbors

These mechanics drive the advice in the skills — and the mistakes made by authors
arriving from NLP or big-ML venues:

- **Four pages, no appendix.** A regular Interspeech 2027 paper is 4 content pages
  plus 2 pages for references and acknowledgments *only* (2026 also allowed the
  AI-use disclosure there; 2025 allowed just one extra page). There is no reviewed
  supplement; whatever decides acceptance must live on the four pages. The **Long
  Paper track** (introduced 2026) continues in 2027: 8 pages + 2, targeted acceptance
  below 30%, and the same work cannot go to both tracks.
- **The paper-update window.** Uniquely among the majors, Interspeech lets authors
  revise the PDF for about a week after the deadline (9 Feb → 16 Feb in 2027; 25 Feb →
  4 Mar in 2026) while metadata stays frozen — a sanctioned proofread pass, not an
  extension.
- **Hard caps on volume and AI.** Interspeech 2027 allows at most two papers per
  author as first author, and desk-rejects papers entirely developed or written by AI
  and papers citing non-existing references.
- **Reviewers listen.** Audio sample pages are consumed as evidence for synthesis,
  conversion, and enhancement papers — and are also the most common anonymity leak.
- **Double-anonymous, but no preprint embargo (2026).** The 2025 anonymity period
  (no non-anonymized posting from one month before the deadline until decisions) was
  dropped in 2026: preprints were allowed as long as the submission itself revealed
  nothing. The 2027 preprint rule is not yet published — reopen the submission policy.
- **Open-access proceedings, no author fee.** Every paper enters the ISCA Archive
  (isca-archive.org) with a `10.21437` DOI; the cost model is registration — at least
  one author must register for the paper to appear, and present it in person.
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
| [`interspeech-submission`](skills/interspeech-submission/SKILL.md) | Final submission audit (CMT in 2025–2026; 2027 portal pending): 4 + 2 format and PDF checker, first-author cap, anonymity sweep including demo pages, area and metadata strategy, and the update-window plan. |
| [`interspeech-review-process`](skills/interspeech-review-process/SKILL.md) | Model the area-based pipeline, what the young rebuttal can move, oral/poster allocation, awards, and how to decode a decision letter. |
| [`interspeech-author-response`](skills/interspeech-author-response/SKILL.md) | Answer a mixed science/engineering review set from the 4-page record, in dialect, within the cap, for the meta-reviewer. |
| [`interspeech-camera-ready`](skills/interspeech-camera-ready/SKILL.md) | Convert acceptance into a correct ISCA Archive entry: de-anonymization order, registration coupling, DOI metadata, and presentation with audio fallbacks. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Thirteen sources with URLs and access dates; the verified Interspeech 2027 fact base; the 2026 history; the 待核实 list; the access-method note; the machine-readable rules block. |
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

## Interspeech 2027 anchor facts (edition snapshot, not permanent rules)

- Interspeech 2027: **São Paulo, Brazil, 29 August – 2 September 2027** — the first
  South American edition; theme **"Speech, Society, and Minorities"**; General Chairs
  Plinio A. Barbosa, Sandra Madureira, Christopher Shulby; Technical Program Chairs
  Khiet Truong, António Teixeira, Theodora Chaspari, Florian Metze.
- 2027 pipeline: portal opens **19 Jan 2027** · paper deadline **9 Feb** · paper-update
  close **16 Feb** · rebuttal **13–20 Apr** · notification **2 Jun** · camera-ready
  **9 Jun 2027**.
- Format: regular papers 4 content pages + 2 pages for references/acknowledgments;
  Long Papers 8 + 2 (targeted acceptance below 30%); double-blind; English; in-person
  presentation; at most two first-author papers per author; AI-written papers and
  non-existing references desk-rejected. Paper kit and portal "available soon"
  (待核实; CMT in 2025 and 2026).
- Proceedings: ISCA Archive, open access, DOI prefix 10.21437, no author fee.
- History — Interspeech 2026: Sydney, 27 September – 1 October 2026, theme
  "Speaking Together"; portal 17 Jan · deadline 25 Feb · update 4 Mar · rebuttal
  24 Apr – 1 May · notification 5 Jun · camera-ready 19 Jun 2026; 4 + up to 2 pages;
  1,000-character abstract; AI-use disclosure section before the references.
- Next edition after 2027: Interspeech 2028, San Antonio, USA.

## Fact discipline

Three statement classes are kept distinguishable throughout the pack:

1. **Verified Interspeech 2027 facts** — traceable to a numbered source in the
   source map (the 9 Feb deadline, the 13–20 Apr rebuttal, the 4 + 2 format).
2. **Reported facts** — found only in secondary renderings and labeled as such
   (none currently load-bearing after the 2026-11-24 direct re-read).
3. **待核实 items** — unresolved at check time and phrased as questions, never as
   facts (the 2027 paper kit and portal, abstract length, preprint rule, attachment
   caps, review-form wording).

If a skill states class-2/3 material as class 1, treat it as a bug and repair it
against the live official pages.

## Maintenance notes

- Every date above is a **São Paulo-cycle snapshot**. ISCA editions are run by
  rotating local committees and Technical Program Chairs; nothing carries to San
  Antonio 2028 automatically — not the tracks, not the rebuttal, not the portal.
- The first maintenance task each cycle is to re-open the primary URLs directly
  (both conference sites answered direct fetches on 2026-11-24) and refresh
  [`resources/official-source-map.md`](resources/official-source-map.md).
- New exemplars must be verified against the ISCA Archive per the recipe at the
  end of [`resources/exemplars/library.md`](resources/exemplars/library.md) —
  speech's famous papers are scattered across ICASSP/NeurIPS/ICML/LREC, and venue
  misattribution is the characteristic error to guard against.

## License

MIT — see [`LICENSE`](LICENSE). 中文版说明见 [`README.zh-CN.md`](README.zh-CN.md)。
