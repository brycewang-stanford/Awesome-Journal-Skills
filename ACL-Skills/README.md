# ACL Skills

Twelve agent skills for papers targeting the Annual Meeting of the Association
for Computational Linguistics (ACL), the flagship conference of the \*ACL
family for computational linguistics and natural language processing.

The pack is built around the mechanic that makes ACL unlike one-deadline
conferences: **ACL Rolling Review (ARR)**. Papers are submitted to dated ARR
cycles on OpenReview, collect reviews and a meta-review there, and are then
**committed** to a conference, whose senior area chairs and program chairs
make the final call — main conference, Findings of ACL, or reject. Every
deadline-shaped skill in this pack (submission, author response, review
process, workflow) reasons in cycles and commitment windows, not in a single
CFP countdown.

Official basis re-verified on 2026-11-23: the ACL 2027 main-conference call
(65th Annual Meeting, Kyoto, August 17-22, 2027), the ARR CFP, cycle calendar,
sustainable-reviewing policy and Responsible NLP checklist at
aclrollingreview.org. Earlier passes (2026-07-08) covered the ACL 2026 calls
(64th Annual Meeting, San Diego, July 2-7, 2026), reviewer/author guidelines,
OpenReview ARR cycle groups, the \*ACL camera-ready FAQ, and ACL Anthology
policy pages. The exact source list, access methods, and the items still marked
待核实 are in `resources/official-source-map.md`.

## What makes ACL submissions different

- **Cycles, not deadlines.** ARR ran 10-week cycles in 2026 (January 5,
  March 16, May 25, August 3, October 12 submissions); each conference
  announces which cycles it accepts. ACL 2027 takes packages from the ARR
  January 2027 cycle (submission January 4, 2027) or earlier, with its
  commitment date still TBA; ACL 2026 drew from the October 2025 and
  January 2026 cycles, with commitment due March 14, 2026.
- **Each submission brings a reviewer.** From the October 2026 cycle, review
  is guaranteed only to submissions naming a qualified service contributor
  (max 2 submissions each); the rest enter a lottery. Authors are capped at
  20 submissions per cycle, 5 as first or joint-first author.
- **Resubmission is designed-in.** A revised paper returns in a later cycle
  with a mandatory link to the prior submission and a point-by-point revision
  note; unacknowledged resubmission is a desk reject.
- **The Limitations section is mandatory** and sits outside the 8-page (long)
  or 4-page (short) content budget, alongside unlimited references.
- **The Responsible NLP checklist is part of review.** Misleading answers are
  desk-rejection grounds; honest limitations are explicitly protected.
- **No anonymity period since 2024-01-12.** Preprints are allowed with
  declaration; staying preprint-free earns award eligibility and borderline
  priority. Submissions themselves stay fully anonymized.
- **Two acceptance tiers.** Findings of ACL is a real, archival,
  Anthology-published outcome decided at commitment time.
- **Open-access forever.** Accepted papers land in the ACL Anthology
  (CC BY 4.0 for post-2016 material), with no author fees.

## Skills

- `acl-submission` - audit an ARR upload: page budgets, mandatory Limitations,
  Responsible NLP checklist, anonymization, preprint and resubmission
  declarations, dual-submission rules, desk-reject triggers.
- `acl-author-response` - work the in-cycle response window: triage reviews,
  shape the meta-review, handle NLP-reviewer objection patterns, flag
  deficient reviews, decide respond-now versus revise-next-cycle.
- `acl-camera-ready` - spend the extra content page well, de-anonymize,
  disclose AI assistance, satisfy the meta-review, and ship clean ACL
  Anthology metadata under CC BY 4.0.
- `acl-artifact-evaluation` - package code, data, prompts, outputs, and
  annotation materials as anonymized .tgz/.zip supplements aligned with
  checklist Section B, then plan the public release ladder.
- `acl-reproducibility` - run the Responsible NLP checklist as a claims
  audit: hyperparameters, compute, prompt/decoding disclosure, contamination
  stance, variance reporting, checklist-to-paper consistency.
- `acl-supplementary` - split body, Limitations, appendices, and archive so
  nothing decision-critical hides where reviewers are not required to look.
- `acl-review-process` - model the ARR pipeline: reviewers, area-chair
  meta-review, commitment, venue-side decision, ethics escalation, and when
  to shop a package to a sibling conference.
- `acl-writing-style` - revise for task-first framing, page-one examples,
  scoped LLM-era claims, quantified error analysis, anonymity-compatible
  voice, and 8/4-page compression.
- `acl-related-work` - position against fast-moving NLP literature:
  Anthology-first citation, Findings attribution, concurrent preprints,
  freshness sweeps across recent \*ACL rounds.
- `acl-experiments` - design the evidence: tuned LLM baselines, multilingual
  breadth matched to claims, significance and variance floors, human-eval
  agreement, contamination controls, ablations, error taxonomies.
- `acl-workflow` - run the cycle-and-commit calendar: cycle choice, backward
  planning, the resubmission loop, commitment decisions, camera-ready
  through Anthology publication.
- `acl-topic-selection` - route between ACL, EMNLP, NAACL/EACL/AACL, TACL,
  Computational Linguistics, COLM, and ML venues; choose long versus short;
  weigh the theme track and the Findings scenario.

## Resources

| Path | Contents |
| --- | --- |
| `resources/official-source-map.md` | Verified sources with URLs, access dates, the gateway access-method note, and 待核实 items |
| `resources/external_tools.md` | Official ARR/OpenReview/Anthology surfaces plus stage-by-stage author checks |
| `resources/exemplars/library.md` | Six verified ACL main-proceedings exemplars by contribution type, with sibling-venue guards |
| `resources/worked-examples/01-introduction.md` | Fictional before/after abstract + introduction in ACL house style |
| `resources/code/README.md` | Pointer to the shared ML-conference reproducibility kit |

## Using the pack

Typical sequence for a new project: `acl-topic-selection` →
`acl-experiments` (design phase) → `acl-writing-style` + the worked example →
`acl-related-work` → `acl-reproducibility` + `acl-artifact-evaluation` →
`acl-supplementary` → `acl-submission` before the cycle deadline →
`acl-author-response` in the response window → `acl-review-process` +
`acl-workflow` at the commitment decision → `acl-camera-ready` after
acceptance.

Install as a Claude Code plugin from this directory (marketplace manifest in
`.claude-plugin/`), or load individual `skills/*/SKILL.md` files as needed.

## Verified facts snapshot (re-verified 2026-11-23)

| Fact | Value | Source |
| --- | --- | --- |
| Edition anchored | ACL 2027, 65th Annual Meeting | 2027.aclweb.org |
| Dates / place | August 17-22, 2027, Kyoto, Japan | 2027.aclweb.org |
| Reviewing | ACL Rolling Review on OpenReview; venue decides | ACL 2027 call + aclrollingreview.org |
| Eligible cycles for ACL 2027 | ARR January 2027 or earlier | ACL 2027 call |
| Jan 2027 cycle deadline | January 4, 2027 (AoE) | ACL 2027 call |
| Commitment / notification / camera-ready | TBA (as of 2026-11-23) | ACL 2027 call |
| Previous edition | ACL 2026, San Diego, July 2-7, 2026; commitment Mar 14, notification Apr 4, camera-ready Apr 19, 2026 | ACL 2026 CFP |
| Page budgets | long 8, short 4; +1 at camera-ready; refs unlimited | ARR CFP + ACL 2027 call |
| Reviewing obligation | qualified service contributor per submission, else lottery; author caps 20 / 5 | aclrollingreview.org/sustainable-reviewing-2026 |
| Mandatory sections | Limitations (desk reject if absent) | ARR CFP |
| Checklist | Responsible NLP checklist, sections A-E | aclrollingreview.org/responsibleNLPresearch |
| Anonymity | anonymized submissions; no embargo since 2024-01-12 | ARR anonymity update |
| Acceptance tiers | main conference; Findings of ACL (archival) | Anthology venues/findings |
| Proceedings | ACL Anthology, open access, CC BY 4.0 (post-2016) | aclanthology.org/faq/copyright |
| 2027 theme | Homogenization and knowledge collapse in LLMs, Thematic Paper Award anticipated (2026: explainability) | ACL 2027 call |

## FAQ

**Is this pack a substitute for the official calls?** No. It encodes the
verified ACL 2027 call state plus stable mechanics; every deadline-sensitive fact must
be re-checked against the live ARR and conference pages, which win conflicts.

**Why is everything phrased in cycles?** Because ACL acceptance is a
two-stage event (ARR review, then conference commitment), advice framed as
"the ACL deadline" is usually wrong by construction. The pack keeps the two
stages separate the way the venue does.

**Does the pack cover EMNLP or NAACL?** The ARR mechanics are shared across
the \*ACL family, so much of the pipeline reasoning transfers, but calibration,
dates, and edition policies here are ACL's. Use a sibling pack for sibling
venues when one exists.

**What if a fact is marked 待核实?** It could not be pinned through the
network gateway at build time. Treat it as unknown until you open the official
page yourself; the source map lists exactly which facts these are.

## Maintenance notes

- ARR cycle structure has changed repeatedly (monthly → bimonthly → 10-week);
  never project the 2026 calendar forward. Reopen
  aclrollingreview.org/dates and the target edition's site first.
- ACL 2026 facts in this pack (dates, theme, commitment window) are historical
  anchors from a conference that concluded on 2026-07-07, not standing rules.
  ACL 2027's commitment, notification and camera-ready dates were still TBA on
  2026-11-23; fill them in from the official call when posted.
- Checklist wording, preprint incentives, page policies, review forms, and
  Findings presentation options are all cycle-volatile; the official pages
  win any conflict with this pack.
- When adding exemplars, verify the Anthology venue line says the ACL Annual
  Meeting main proceedings — the Anthology hosts every sibling venue too.

## License

MIT (see `LICENSE`). This pack is community documentation and is not
affiliated with or endorsed by the ACL.
