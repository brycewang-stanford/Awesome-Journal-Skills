# EACL Skills

Twelve agent skills for papers aimed at the **Conference of the European
Chapter of the Association for Computational Linguistics (EACL)** — the
*ACL-family meeting that carries the community's European identity, held in
and around Europe and the Mediterranean (Athens 2027, Rabat 2026, St. Julian's
2024, Dubrovnik 2023) and traditionally the first *ACL conference of the
calendar year, in early spring.

Like its siblings, EACL runs no submission portal of its own. Papers are
reviewed inside **ACL Rolling Review (ARR)** on OpenReview, then **committed**
to an EACL edition, whose senior area chairs and program chairs sort each
commitment into the main conference, **Findings of ACL: EACL**, or reject.
Every deadline-shaped skill here reasons in that two-step rhythm — ARR cycle
first, EACL commitment second — never in a single "conference deadline."

Official basis checked on **2026-07-09**: the EACL 2027 call for papers
(20th Conference, Athens, Greece, March 9-14, 2027), the ARR CFP and cycle
calendar and Responsible NLP checklist at aclrollingreview.org, the ARR
OpenReview groups, the ACL Anthology's EACL and Findings volumes, and the ACL
Member Portal announcements. The verification gateway blocked direct fetches
of `2027.eacl.org`, `aclrollingreview.org`, and `dblp.org`, so those pages
were read through search-engine renderings of exact official URLs and
cross-checked against the ACL Anthology and the ACL Member Portal. The full
source trail, access methods, and every item still marked 待核实 are in
[`resources/official-source-map.md`](resources/official-source-map.md).

## What makes an EACL submission different

- **The European Chapter, not the flagship.** EACL is the ACL's European
  regional meeting, sibling to NAACL (Americas) and AACL (Asia-Pacific) and to
  the flagship ACL. It is the natural home for European and neighbouring-region
  language technology, multilingual and lower-resourced-language work, and a
  strong European reviewing community — but scientific scope is all of CL/NLP,
  not a European-topics-only track.
- **Irregular cadence.** EACL does not run every year and its slot moves; there
  was a gap before 2021, then editions in 2023, 2024, and 2026, and the next is
  2027. Never assume an annual EACL — confirm whether an edition exists before
  planning around it.
- **One viable ARR cycle, no fallback.** Because EACL 2027 sits early in the
  year, the organizers declared the **August 3, 2026 ARR cycle the only viable
  cycle** for it. Unlike ACL (which drew from two cycles) there is no "slip to
  the next cycle" safety net — miss it and the edition is gone. Timing is the
  single highest-leverage decision in this pack.
- **The Limitations section is mandatory** and sits outside the 8-page (long)
  or 4-page (short) content budget, together with unlimited references and
  appendices. Its absence is a desk-reject trigger.
- **The Responsible NLP checklist is part of review.** It is filed at ARR
  submission and misleading answers are desk-rejection grounds; an honest
  Limitations section is explicitly protected, not penalized.
- **Two archival tiers.** Findings of ACL: EACL is a real, Anthology-published
  outcome decided at commitment time, notified simultaneously with the main
  track.
- **Open access, no fees.** Accepted papers land in the ACL Anthology under
  CC BY 4.0 (post-2016 material) with no author charge; the cost model is
  registration, and at least one author registers and presents.

## Skills

- `eacl-submission` - audit an ARR upload aimed at EACL: content-page budgets,
  the mandatory Limitations section, Responsible NLP checklist, anonymization,
  preprint and resubmission declarations, dual-submission rules, and the
  single-cycle timing trap.
- `eacl-author-response` - work the in-cycle rebuttal window: triage reviews,
  address the action editor, answer common NLP-reviewer objections, flag
  deficient reviews, and decide respond-now versus revise-for-a-later-venue.
- `eacl-camera-ready` - spend the extra content page, de-anonymize, disclose AI
  assistance, satisfy the meta-review, and ship clean ACL Anthology metadata
  for an EACL or Findings: EACL record.
- `eacl-artifact-evaluation` - package code, data, prompts, model outputs, and
  annotation materials as anonymized OpenReview supplements aligned with the
  checklist, then plan the public post-acceptance release.
- `eacl-reproducibility` - run the Responsible NLP checklist as a claims audit:
  hyperparameters, compute, prompt and decoding disclosure, contamination
  stance, variance reporting, and checklist-to-paper consistency.
- `eacl-supplementary` - split body, Limitations, appendices, and archive so no
  decision-critical content hides where EACL reviewers are not obliged to read.
- `eacl-review-process` - model the ARR-to-EACL pipeline: reviewers, action
  editor, meta-review, commitment, the venue-side decision, ethics escalation,
  and when to route a package to a sibling meeting.
- `eacl-writing-style` - revise for task-first framing, page-one examples,
  scoped LLM-era claims, quantified error analysis, an anonymity-safe voice,
  and 8/4-page compression.
- `eacl-related-work` - position against fast-moving NLP literature:
  Anthology-first citation, Findings attribution, concurrent preprints, and
  freshness sweeps across recent *ACL rounds and European venues.
- `eacl-experiments` - design the evidence: tuned LLM baselines, multilingual
  breadth matched to claims, significance and variance floors, human-eval
  agreement, contamination controls, ablations, and error taxonomies.
- `eacl-workflow` - run the single-cycle-and-commit calendar: cycle lock,
  backward planning, the rebuttal window, the commitment decision, and
  camera-ready through Anthology publication.
- `eacl-topic-selection` - route between EACL, ACL, EMNLP, NAACL, AACL, TACL,
  Computational Linguistics, LREC-COLING, COLM, and ML venues; choose long
  versus short; weigh the Findings scenario and the single-cycle constraint.

## Resources

| Path | Contents |
| --- | --- |
| `resources/official-source-map.md` | Verified sources with URLs, access dates, the gateway access-method note, and 待核实 items |
| `resources/external_tools.md` | Official ARR/OpenReview/EACL/Anthology surfaces plus stage-by-stage author checks |
| `resources/exemplars/library.md` | Five verified EACL main/Findings exemplars by contribution type, with sibling-venue guards |
| `resources/worked-examples/01-introduction.md` | Fictional before/after abstract + introduction in EACL house style |
| `resources/code/README.md` | Pointer to the shared ML-conference reproducibility kit |

## Using the pack

Typical sequence for a new project: `eacl-topic-selection` →
`eacl-experiments` (design phase) → `eacl-writing-style` + the worked example →
`eacl-related-work` → `eacl-reproducibility` + `eacl-artifact-evaluation` →
`eacl-supplementary` → `eacl-submission` before the single ARR deadline →
`eacl-author-response` in the rebuttal window → `eacl-review-process` +
`eacl-workflow` at the commitment decision → `eacl-camera-ready` after
acceptance.

Install as a Claude Code plugin from this directory (marketplace manifest in
`.claude-plugin/`), or load individual `skills/*/SKILL.md` files as needed.

## Verified facts snapshot (access date 2026-07-09)

| Fact | Value | Source |
| --- | --- | --- |
| Next edition | EACL 2027, 20th Conference of the European Chapter | 2027.eacl.org |
| Dates / place | March 9-14, 2027, Athens, Greece (hybrid) | 2027.eacl.org |
| Reviewing | ACL Rolling Review on OpenReview; EACL commits | EACL 2027 CFP + aclrollingreview.org |
| Viable ARR cycle | August 3, 2026 only (no fallback) | EACL 2027 CFP + @eaclmeeting date-correction |
| Commitment deadline | October 11, 2026 | EACL 2027 CFP |
| Notification / camera-ready | November 12 / November 26, 2026 | EACL 2027 CFP |
| Page budgets | long 8, short 4; +1 at camera-ready; refs/appendices unlimited | ARR CFP + EACL 2027 CFP |
| Mandatory section | Limitations (uncounted; desk reject if absent) | ARR CFP |
| Checklist | Responsible NLP checklist | aclrollingreview.org/responsibleNLPresearch |
| Anonymity | anonymized submissions; no anonymity period since 2024-01-12 | ARR anonymity policy |
| Acceptance tiers | main conference; Findings of ACL: EACL (archival) | ACL Anthology |
| Proceedings | ACL Anthology, open access, CC BY 4.0 (post-2016) | aclanthology.org |
| Prior edition | EACL 2026, 19th, Rabat, Morocco, March 24-29, 2026 | aclanthology.org/2026.eacl-long |

## FAQ

**Is this pack a substitute for the official calls?** No. It encodes the
verified 2027 state plus stable ARR mechanics; every deadline-sensitive fact
must be re-checked against the live ARR and EACL pages, which win conflicts.

**Why the fixation on one cycle?** Because EACL 2027 accepts only the August
2026 ARR cycle, the usual *ACL "just resubmit next cycle" fallback does not
exist for this edition. The pack treats the single cycle as a hard, unrepeatable
gate rather than one of several attempts.

**Does the pack cover ACL, EMNLP, or NAACL?** The ARR machinery is shared
across the *ACL family, so much pipeline reasoning transfers, but the
calibration, dates, cadence, and regional identity here are EACL's. Use a
sibling pack for a sibling venue when one exists.

**Is EACL only for European-language work?** No. EACL welcomes all of CL/NLP.
Its European identity shapes the community and location, and it is a natural
home for multilingual and lower-resourced-language research, but topical scope
is not restricted by region.

**What if a fact is marked 待核实?** It could not be pinned through the network
gateway at build time. Treat it as unknown until you open the official page
yourself; the source map lists exactly which facts these are.

## Maintenance notes

- EACL cadence and calendar slot move between editions; never project the 2027
  timing forward. Reopen the target edition's site and aclrollingreview.org/dates
  before any deadline-sensitive advice.
- EACL 2027 facts here (dates, the single viable cycle, commitment window) are
  current-cycle anchors, not standing rules; the official pages win any conflict.
- Checklist wording, preprint incentives, page policies, review forms, and
  Findings presentation options are all cycle-volatile.
- When adding exemplars, verify the Anthology venue line names an EACL edition
  specifically — the Anthology hosts every sibling venue too, and the shared
  `E`/`eacl` identifiers are easy to confuse.

## License

MIT (see `LICENSE`). This pack is community documentation and is not affiliated
with or endorsed by the ACL or the European Chapter of the ACL.
