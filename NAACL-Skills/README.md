# NAACL Skills

Twelve agent skills for papers targeting **NAACL — the Annual Conference of
the Nations of the Americas Chapter of the Association for Computational
Linguistics**. The chapter voted in September 2024 to replace "North
American" with "Nations of the Americas" in its name, a change that made
explicit what its recent programs already were: an *ACL flagship whose home
region runs from Canada to Argentina, with theme tracks like "Languages of
Latin America" (Mexico City, 2024) and "NLP in a Multicultural World"
(Albuquerque, 2025) and workshops such as AmericasNLP at its side.

Two structural facts drive everything in this pack:

1. **NAACL owns no reviewing.** Papers are reviewed inside ACL Rolling
   Review (ARR) cycles on OpenReview; authors later *commit* the finished
   review package to a NAACL edition, whose committee sorts commitments
   into the main conference, **Findings of NAACL**, or rejection.
2. **NAACL is not annual.** The chapter stands down when the ACL main
   meeting is hosted in the Americas — there was no NAACL 2023 and no
   NAACL 2026 (ACL 2026 met in San Diego). As of this pack's verification
   date the next edition is **NAACL 2027**, dates and venue unannounced.
   Planning for NAACL therefore means planning ARR timing around a
   conference that sometimes is not there, with explicit fallbacks.

Official basis checked on **2026-07-08**: naacl.org, the NAACL 2024/2025
edition sites and calls, the renaming vote announcements, the 2027 edition
placeholder site, the ARR CFP and dates pages, and the ACL Anthology's
NAACL and Findings listings. The verification gateway blocked direct
fetches of the official domains, so facts were confirmed through
web-search renderings of exact official URLs, cross-checked against ACL
portal announcements — the full trail, access dates, and every item still
marked 待核实 live in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What is distinctly NAACL here

- **The calendar check comes before the style check.** Every skill that
  touches deadlines starts from "does a NAACL edition exist for this cycle
  at all?" — the question authors at annual venues never ask.
- **Commitment is a strategic act.** Reviews are portable across the *ACL
  family; deciding whether a package waits for NAACL, commits to a
  sibling, or re-enters ARR is treated as a first-class decision with a
  decision tree, not an afterthought.
- **The Americas identity is operational, not decorative.** Skills carry
  the consequences: community-owned language data and its release
  constraints, glossing discipline for Nahuatl or Guaraní examples,
  variety-scoped claims (es-MX vs es-AR), accent-correct Anthology
  metadata, and visa lead times for hemispheric host cities.
- **Findings is explained as a capacity mechanism**, so authors triage
  soundness objections (which kill both tiers) differently from
  excitement objections (which often decide only the tier).

## The twelve skills

| Skill | One-line job |
| --- | --- |
| [`naacl-topic-selection`](skills/naacl-topic-selection/SKILL.md) | Decide NAACL vs ACL/EMNLP/EACL/AACL/LREC-COLING/TACL/ML venues by timing, audience, and theme leverage — not imaginary prestige tiers. |
| [`naacl-workflow`](skills/naacl-workflow/SKILL.md) | Run the skipped-year calendar: provisional backward plans, milestone owners, and the commit-vs-wait-vs-reroute decision tree. |
| [`naacl-submission`](skills/naacl-submission/SKILL.md) | Audit the ARR upload: cycle sanity, format/anonymity/checklist gates, and the form declarations that quietly gate everything. |
| [`naacl-writing-style`](skills/naacl-writing-style/SKILL.md) | Scope every claim to tested languages and varieties; make glossed examples carry arguments; write Limitations that pre-empt reviews. |
| [`naacl-related-work`](skills/naacl-related-work/SKILL.md) | Cover five lineages including the regional/community one; cite Findings and workshops correctly; end with a falsifiable delta sentence. |
| [`naacl-experiments`](skills/naacl-experiments/SKILL.md) | Match designs to coverage claims, keep comparisons budget-fair, guard against translationese, and survive the five reviewer probes. |
| [`naacl-reproducibility`](skills/naacl-reproducibility/SKILL.md) | Treat the Responsible NLP checklist as a contract; pin models, prompts, and per-language preprocessing; state an honest release level. |
| [`naacl-artifact-evaluation`](skills/naacl-artifact-evaluation/SKILL.md) | Package data/prompts/guidelines for checklist cross-examination, including community-owned and Indigenous-language data constraints. |
| [`naacl-supplementary`](skills/naacl-supplementary/SKILL.md) | Allocate material across the four review tiers; budget the three-line cost of glossed examples; keep claims out of orphan tiers. |
| [`naacl-review-process`](skills/naacl-review-process/SKILL.md) | Model the ARR-reviews-then-NAACL-decides machine, Main-vs-Findings mechanics, and the deep post-gap commitment pools. |
| [`naacl-author-response`](skills/naacl-author-response/SKILL.md) | Spend the short window on what changes the frozen record NAACL's SACs will read at commitment. |
| [`naacl-camera-ready`](skills/naacl-camera-ready/SKILL.md) | Merge promises + de-anonymization into the Anthology version; restore community credits; protect names with correct diacritics. |

## Resources

| Path | Contents |
| --- | --- |
| [`resources/official-source-map.md`](resources/official-source-map.md) | Twelve sources with URLs and access dates, the verified fact list, the access-method note, and the 待核实 register. |
| [`resources/external_tools.md`](resources/external_tools.md) | Live official surfaces plus five ordered author-side verification passes. |
| [`resources/exemplars/library.md`](resources/exemplars/library.md) | Five Anthology-verified NAACL papers (2013-2022) as writing models, with an anti-misattribution omissions list. |
| [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md) | A fictional code-switched-QA abstract/introduction rebuilt from unscoped to NAACL register. |
| [`resources/code/README.md`](resources/code/README.md) | Adapter to the shared ML-conference reproducibility kit plus four NLP-specific manual checks. |

## Installation and use

This directory is a self-contained Claude Code plugin with its own
marketplace manifest.

```bash
# From a clone of the repository
claude plugin marketplace add ./NAACL-Skills
claude plugin install naacl-skills

# Or reference skills directly in an agent setup by path:
#   NAACL-Skills/skills/<skill-name>/SKILL.md
```

Typical invocations once installed:

- "Is this paper better aimed at NAACL 2027 or EMNLP?" →
  `naacl-topic-selection` + `naacl-workflow`
- "Audit my ARR submission before Friday's deadline" → `naacl-submission`
- "Reviews came back — draft the response" → `naacl-author-response` with
  `naacl-review-process` for triage
- "We got Findings — what now?" → `naacl-review-process` +
  `naacl-camera-ready`

## The moving parts, in one glossary

| Term | What it means in this pack |
| --- | --- |
| **ARR cycle** | A recurring ACL Rolling Review round on OpenReview (identified by month/year) that produces reviews plus a meta-review; not an acceptance. |
| **Commitment** | The author-initiated step of forwarding a completed ARR review package to a specific NAACL edition for a decision. |
| **Findings of NAACL** | The archival, Anthology-indexed acceptance tier for sound papers outside the main program's capacity; presentation arrangements vary by edition. |
| **Skipped year** | An ACL-in-the-Americas year in which no NAACL edition convenes (2023, 2026); packages wait, reroute, or revise. |
| **Limitations section** | The mandatory, uncounted section after the conclusion; its absence is a desk-reject ground under the ARR CFP. |
| **Responsible NLP checklist** | The submission-time questionnaire whose misleading answers are themselves desk-reject grounds; treated in this pack as a contract. |
| **AoE** | Anywhere on Earth (UTC-12), the clock every ARR deadline runs on. |
| **待核实** | "To be verified" — this pack's marker for any statement that could not be pinned to an official rendering by the access date. |

## Sibling packs in this repository

[`ACL-Skills`](../ACL-Skills/), [`EMNLP-Skills`](../EMNLP-Skills/), and this
pack cover three venues that share one review machine but differ in
identity and calendar. The division of labor: venue-generic ARR mechanics
appear in each pack only as far as its own venue's decisions require, and
the NAACL-specific material here — the skipped-year planning, the
commitment pool dynamics after a gap year, the Americas-language data and
writing practices — appears nowhere else. If your paper is venue-undecided,
start with [`naacl-topic-selection`](skills/naacl-topic-selection/SKILL.md),
which routes across the family honestly rather than recruiting for NAACL.

## Honesty and maintenance rules

This pack was built on 2026-07-08, between NAACL editions, and says so
rather than pretending otherwise:

- NAACL 2024/2025 dates and mechanics are **historical anchors** that show
  the machine's shape; they are never presented as the next edition's
  rules.
- Everything unpinned — NAACL 2027 dates, venue, feeding cycles,
  commitment deadline, theme track, presentation policy — is marked
  **待核实** in the source map, and skills route the reader to live pages
  at every deadline-sensitive step.
- ARR mechanics (page budgets, checklist enforcement, preprint policy,
  cycle cadence) change between cycles; the CFP and dates pages govern,
  and this pack defers to them by construction.
- When NAACL 2027 publishes its call, update: the source map's 待核实
  section, the workflow skill's calendar block, the submission skill's
  check-zero example, and this README's second structural fact.

## License

MIT — see [LICENSE](LICENSE). Not affiliated with or endorsed by the NAACL
chapter, the ACL, ACL Rolling Review, or OpenReview; all trademarks belong
to their owners.
