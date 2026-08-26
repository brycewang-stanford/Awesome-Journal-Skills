# Official Source Map - ACL

Access date: 2026-07-08 (ARR calendar, CFP and the next edition re-verified live 2026-08-27)

This map records the official sources behind every ACL-specific fact in this pack.
ACL runs on ACL Rolling Review (ARR), and both ARR mechanics and per-edition
conference rules change between cycles — reopen the current ARR CFP, the cycle
calendar, and the target conference's calls before giving deadline-sensitive advice.

**Edition status, checked 2026-08-27.** ACL 2026 has met (San Diego, July 2-7, 2026), so
every 2026 figure below is a historical anchor. The live edition is **ACL 2027**, and its
official site is up: the 65th Annual Meeting, **Kyoto, Japan, August 17-22, 2027**. What
matters more than the meeting dates is the route to it, because ARR routes by cycle and
not by conference: the **August 2026 cycle closed on August 3** and commits to **EACL
2027**, the **October 2026 cycle** (submission October 12, commitment December 20, 2026)
commits to **NAACL 2027 and COLING 2027**, and the first cycle that commits to **ACL 2027
opens in January 2027**. An author asking today which deadline gets them into ACL 2027 is
asking about a January 2027 ARR submission — not about anything on the 2026 calendar.

## Access-method note (read first)

**Updated 2026-08-27: the block is gone.** `aclrollingreview.org` and `2027.aclweb.org`
now answer direct fetches, and the ARR calendar, the CFP, the ACL 2027 site and its
organising committee were re-read directly on that date. The rest of this map still
carries facts pinned in July 2026 through the channels described below; where a fact has
been re-read directly since, its row says so.

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
| 2 | https://aclrollingreview.org/cfp | Long 8 / short 4 content pages; unlimited references; required Limitations section (desk reject if missing); optional ethics statement; anonymized submissions; preprint declaration and incentives; Responsible NLP checklist requirement; AI-assistance policy; dual-submission preclusion; resubmission linking + change-summary rules; meta-review-score-1 resubmission constraint; supplement format (.tgz/.zip, no tracked cloud links); ethics review via Ethics Advisory Committee. Re-read directly 2026-08-27, which added three rules the July pass predates: the **all-authors reviewing obligation**, the **thin-slicing rule**, and a **48-hour metadata edit window** after each deadline. | 2026-07-08 (raw GitHub); re-read 2026-08-27 (direct fetch) |
| 3 | https://aclrollingreview.org/reviewing (repo: reviewing.md) | Cycle stage structure (submission → reviews → author response → reviewer discussion → meta-review); ≥3 reviewers per paper; AC writes the meta-review; ARR SACs do not make accept/reject recommendations; commitment defined as sending a complete review package to a venue whose program committee decides. | 2026-07-08 (raw GitHub) |
| 4 | https://aclrollingreview.org/dates | 10-week cycles since May 2025; full 2026 cycle calendar and the venue-routing table (which cycle commits to which conference), reproduced below; AoE (UTC-12) deadline convention. | 2026-08-27 (direct fetch) |
| 4a | https://2027.aclweb.org/ | ACL 2027 is the 65th Annual Meeting of the ACL, Kyoto, Japan, August 17-22, 2027; official site launched; all deadlines 11:59 pm UTC-12 (AoE). | 2026-08-27 (direct fetch) |
| 4b | https://2027.aclweb.org/organization/ | ACL 2027 organising committee: General Chair Yusuke Miyao (University of Tokyo); Program Chairs David Adelani (McGill), Arianna Bisazza (Groningen), Jan Buys (Cape Town), Ximena Gutierrez-Vasques (UNAM), David Schlangen (Potsdam). Chairs are appointed per edition and rotate yearly. | 2026-08-27 (direct fetch) |
| 5 | https://aclrollingreview.org/responsibleNLPresearch/ (repo: responsibleNLPresearch.md) | Responsible NLP checklist sections: A limitations + risks, B scientific artifacts, C computational experiments, D human annotators/participants, E AI assistants; checklist used in review; misleading answers can cause desk rejection; honest limitations protected from penalization. | 2026-07-08 (raw GitHub) |
| 6 | https://aclrollingreview.org/anonymity/ and https://2024.naacl.org/blog/anonimity/ | ACL removed the anonymity (preprint-embargo) period on January 12, 2024, effective from the February 2024 cycles; submissions must still be anonymized; authors declaring "no non-anonymous preprint" gain award eligibility and priority in borderline decisions, enforced until meta-review release. | 2026-07-08 (search renderings) |
| 7 | https://openreview.net/group?id=aclweb.org/ACL/ARR/2026/January | The ARR January 2026 OpenReview group — the author-side submission location for the cycle that fed ACL 2026; confirms the aclweb.org/ACL/ARR/{year}/{month} group-ID pattern. | 2026-07-08 (search listing) |
| 8 | https://acl-org.github.io/pubdocs/camera-ready-faq.html | General \*ACL camera-ready convention: one additional content page for accepted papers (long ≤9, short ≤5) to address reviewer comments. | 2026-07-08 (search rendering) |
| 9 | https://aclanthology.org/faq/copyright/ | ACL Anthology open access; materials published in/after 2016 licensed CC BY 4.0. | 2026-07-08 (search rendering) |
| 10 | https://aclanthology.org/venues/findings/ | Findings of the ACL as an archival, Anthology-published acceptance tier distinct from main-conference proceedings. | 2026-07-08 (search rendering) |

## The ARR calendar and what each cycle commits to (re-read 2026-08-27)

ARR is a review pipeline, not a conference deadline. A paper is submitted to a *cycle*,
gets reviews, and is then **committed** to a venue whose own program committee decides.
So "the ACL deadline" is really two dates in different months, and which conference a
cycle can reach is fixed by ARR, not chosen by the author.

| 2026 cycle | Submission | Reviewer registration | Reviews due | Author response | Meta-reviews | Cycle end |
|---|---|---|---|---|---|---|
| March 2026 | March 16 | March 18 | April 20 | April 28 - May 4 | May 21 | May 24 |
| May 2026 | May 25 | May 27 | July 2 | July 8 - 14 | July 30 | August 2 |
| August 2026 | August 3 | August 5 | September 7 | September 14 - 24 | October 8 | October 11 |
| October 2026 | October 12 | TBA | TBA | TBA | TBA | December 20 |

| Venue | Final ARR submission | Commitment |
|---|---|---|
| EMNLP 2026 · AACL 2026 | May 25, 2026 | August 2, 2026 |
| EACL 2027 | August 3, 2026 | October 11, 2026 |
| NAACL 2027 · COLING 2027 | October 12, 2026 | December 20, 2026 |
| **ACL 2027** | **January 2027** | not yet posted (待核实) |

Read together, the two tables answer the question an author actually has. As of
2026-08-27 the August cycle is mid-review (author response ran September 14-24 — note
that this is a *future* date on the published calendar, so the cycle is still open
business), the next submission slot is October 12, and that slot commits to NAACL/COLING
2027. **Nothing on the 2026 calendar reaches ACL 2027**; that route opens with the
January 2027 cycle, whose exact day the ARR page has not yet published.

## Verified facts used in the skills

- **ACL 2027 is the 65th Annual Meeting**, in **Kyoto, Japan, August 17-22, 2027**.
  General Chair **Yusuke Miyao** (University of Tokyo); Program Chairs **David Adelani**
  (McGill), **Arianna Bisazza** (Groningen), **Jan Buys** (Cape Town), **Ximena
  Gutierrez-Vasques** (UNAM), **David Schlangen** (Potsdam). The site publishes no
  detailed program yet ("a detailed schedule will be released closer to the conference
  date") and no track-level calls; the route in is the ARR January 2027 cycle.
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
- **Every author is a reviewer** (re-read 2026-08-27). ACL has adopted a CVPR-style
  policy: after each submission deadline *all* authors must complete the author
  registration form, and assignments are made from their qualifications. Reviewers who
  do not deliver may become **ineligible to commit or (re-)submit in the following ARR
  cycle** — a sanction that lands on the submitting team, not only on the individual, so
  a co-author who ignores an assignment can cost the paper its next cycle. Emergencies go
  through the designated delay form, not silence.
- **Thin-slicing is discouraged, following ICML** (re-read 2026-08-27): concurrently
  submitted papers on a related topic with overlapping stated contributions are treated
  as one contribution split up. There can be **no overlap in stated contributions**, and
  re-used text from the authors' other publications is capped at **10% of total tokens**.
- **Metadata, including the Responsible NLP checklist, stays editable for 48 hours after
  each submission deadline** (re-read 2026-08-27) — the one window in which a checklist
  filed wrong can be fixed before it becomes a desk-rejection ground.
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

- ACL 2027 track-level calls, page policies for its own tracks, registration fees, and
  the commitment date for the January 2027 cycle. The conference site is live but
  publishes only identity, dates, venue and the organising committee; the ARR venue table
  leaves ACL 2027's commitment column blank. Nothing here should be back-filled from the
  2026 edition.
- ACL 2026 registration fees, in-person presentation requirements per track, and
  the Findings presentation options actually offered in San Diego.
- The exact ARR review-form fields and score scales in force for current cycles.
- The ARR October 2025 cycle's exact submission date (the calendar page has since rolled
  forward again and now shows March 2026 onward, so the January 5, 2026 date is also no
  longer on it; both stand on the July 2026 reading).
- The October 2026 cycle's reviewer-registration, review, author-response and meta-review
  dates: the calendar publishes its submission date (October 12) and its cycle end
  (December 20) and prints **TBA** for everything between.
- ACL 2026 award outcomes (best/outstanding/thematic papers) — announced at the
  conference days before this pack's access date.

## Cycle-volatile by construction

Cycle dates and count per year, commitment windows per conference, checklist
wording, review-form structure, preprint-incentive details, page policies, and
theme tracks all change between editions. The 2026 facts above are historical
anchors, not standing rules.
