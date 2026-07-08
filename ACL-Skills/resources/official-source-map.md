# Official Source Map - ACL

Access date: 2026-07-08

This map records the official sources behind every ACL-specific fact in this pack.
ACL runs on ACL Rolling Review (ARR), and both ARR mechanics and per-edition
conference rules change between cycles — reopen the current ARR CFP, the cycle
calendar, and the target conference's calls before giving deadline-sensitive advice.

## Access-method note (read first)

The network gateway used while building this pack returned HTTP 403 for direct
fetches of `2026.aclweb.org`, `aclrollingreview.org`, and `aclanthology.org`.
Facts were therefore verified through two indirect but authoritative channels:

1. **GitHub-source mirrors.** aclrollingreview.org is generated from the public
   repository `github.com/acl-org/aclrollingreview`; its `cfp.md`, `reviewing.md`,
   and `dates.md` were fetched raw from `raw.githubusercontent.com` (which the
   gateway allows) and are the same content the website renders.
2. **Web-search renderings of exact official URLs.** Search-result renderings of
   the ACL 2026 CFP page, the ARR dates page, the Anthology copyright FAQ, and
   OpenReview group pages were used and cross-checked against each other.

Anything that could not be pinned through those channels is marked 待核实 below.
When you have direct access, prefer opening the official URLs themselves.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://2026.aclweb.org/ and https://2026.aclweb.org/calls/main_conference_papers/ | ACL 2026 identity (64th Annual Meeting), San Diego, July 2-7, 2026, hybrid format; ARR-based reviewing with conference-side decisions; eligible cycles (ARR October 2025, January 2026); special theme (explainability) with Thematic Paper Award; commitment/notification/camera-ready dates. | 2026-07-08 (via search renderings) |
| 2 | https://aclrollingreview.org/cfp (repo: acl-org/aclrollingreview, cfp.md) | Long 8 / short 4 content pages; unlimited references; required Limitations section (desk reject if missing); optional ethics statement; anonymized submissions; preprint declaration and incentives; Responsible NLP checklist requirement; AI-assistance policy; dual-submission preclusion; resubmission linking + change-summary rules; meta-review-score-1 resubmission constraint; supplement format (.tgz/.zip, no tracked cloud links); ethics review via Ethics Advisory Committee. | 2026-07-08 (raw GitHub) |
| 3 | https://aclrollingreview.org/reviewing (repo: reviewing.md) | Cycle stage structure (submission → reviews → author response → reviewer discussion → meta-review); ≥3 reviewers per paper; AC writes the meta-review; ARR SACs do not make accept/reject recommendations; commitment defined as sending a complete review package to a venue whose program committee decides. | 2026-07-08 (raw GitHub) |
| 4 | https://aclrollingreview.org/dates (repo: dates.md) | 10-week cycles since May 2025; 2026 cycle calendar: January (submission Jan 5), March (Mar 16), May (May 25 → EMNLP 2026 / AACL 2026, commitment Aug 2), August (Aug 3 → EACL 2027, commitment Oct 11), October (Oct 12, later dates TBA); AoE (UTC-12) deadline convention. | 2026-07-08 (raw GitHub + search rendering) |
| 5 | https://aclrollingreview.org/responsibleNLPresearch/ (repo: responsibleNLPresearch.md) | Responsible NLP checklist sections: A limitations + risks, B scientific artifacts, C computational experiments, D human annotators/participants, E AI assistants; checklist used in review; misleading answers can cause desk rejection; honest limitations protected from penalization. | 2026-07-08 (raw GitHub) |
| 6 | https://aclrollingreview.org/anonymity/ and https://2024.naacl.org/blog/anonimity/ | ACL removed the anonymity (preprint-embargo) period on January 12, 2024, effective from the February 2024 cycles; submissions must still be anonymized; authors declaring "no non-anonymous preprint" gain award eligibility and priority in borderline decisions, enforced until meta-review release. | 2026-07-08 (search renderings) |
| 7 | https://openreview.net/group?id=aclweb.org/ACL/ARR/2026/January | The ARR January 2026 OpenReview group — the author-side submission location for the cycle that fed ACL 2026; confirms the aclweb.org/ACL/ARR/{year}/{month} group-ID pattern. | 2026-07-08 (search listing) |
| 8 | https://acl-org.github.io/pubdocs/camera-ready-faq.html | General \*ACL camera-ready convention: one additional content page for accepted papers (long ≤9, short ≤5) to address reviewer comments. | 2026-07-08 (search rendering) |
| 9 | https://aclanthology.org/faq/copyright/ | ACL Anthology open access; materials published in/after 2016 licensed CC BY 4.0. | 2026-07-08 (search rendering) |
| 10 | https://aclanthology.org/venues/findings/ | Findings of the ACL as an archival, Anthology-published acceptance tier distinct from main-conference proceedings. | 2026-07-08 (search rendering) |

## Verified facts used in the skills

- ACL 2026 was the **64th Annual Meeting**, held **July 2-7, 2026 in San Diego,
  California** (hybrid). As of the pack's access date (2026-07-08) the conference
  had just concluded.
- ACL 2026 reviewing ran through **ARR**, with submissions accepted from the
  **October 2025 and January 2026 cycles**; **commitment deadline March 14, 2026**,
  reviews/meta-reviews to authors by ~March 9-10, **notification April 4, 2026**,
  **camera-ready April 19, 2026**. Final decisions were made by the conference's
  senior area chairs and program chairs, on OpenReview.
- ARR January 2026 cycle submission deadline: **January 5, 2026**; all ARR
  deadlines are 11:59 pm UTC-12 (AoE). ARR moved to **10-week cycles** in May 2025.
- Paper formats: **long = 8 content pages, short = 4**, unlimited references,
  required Limitations section and optional ethics statement outside the count;
  accepted papers traditionally get **one extra content page** (9/5).
- The **Responsible NLP checklist** is mandatory; incorrect/incomplete/misleading
  answers are desk-rejection grounds. Resubmissions must link the prior submission
  and include a change summary with point-by-point responses.
- The **anonymity period was abolished 2024-01-12**; submissions stay anonymized,
  preprints are permitted with declaration, and anonymous-only submissions receive
  award/priority incentives.
- **Findings of ACL** is a real archival acceptance tier published in the ACL
  Anthology; the **Anthology** is open access, CC BY 4.0 for post-2016 materials,
  with no author fees (ACL's cost model is conference registration).
- ACL 2026 ran a special **theme track on explainability** with a Thematic Paper
  Award, plus separate industry, demo, and student-research-workshop tracks with
  their own deadlines (industry: submissions Feb 14, notification Apr 12, 2026).

## Marked 待核实 (could not be pinned through the gateway)

- ACL 2026 registration fees, in-person presentation requirements per track, and
  the Findings presentation options actually offered in San Diego.
- The exact ARR review-form fields and score scales in force for current cycles.
- The ARR October 2025 cycle's exact submission date (the calendar page now
  shows 2026 cycles; the January 5, 2026 date is pinned, the October one is not).
- ACL 2026 award outcomes (best/outstanding/thematic papers) — announced at the
  conference days before this pack's access date.

## Cycle-volatile by construction

Cycle dates and count per year, commitment windows per conference, checklist
wording, review-form structure, preprint-incentive details, page policies, and
theme tracks all change between editions. The 2026 facts above are historical
anchors, not standing rules.
