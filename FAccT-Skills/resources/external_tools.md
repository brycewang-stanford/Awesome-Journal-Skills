# External Tools - ACM FAccT

Access date: 2026-11-24 (first compiled 2026-07-09)

Use these surfaces after reopening the current FAccT cycle pages. FAccT mechanics — deadlines,
page budget, endmatter statements, the Revise round, and the submission platform — are decided per
edition. 2026 introduced OpenReview, the Revise-and-resubmit decision, and the required Generative
AI Usage Statement; 2027 moved the deadline to the autumn (27 October / 3 November 2026), merged
the rebuttal into the revision, added Senior Area Chairs, and replaced the AI-writing prohibition
with a disclosure rule. On 2026-11-24 `facctconference.org`, the FAccT Blog, and the OpenReview API
were readable directly; `dl.acm.org` still blocks automated fetches (cross-check via Crossref and
dblp). Note the naming history: the venue was **FAT\*** in 2018-2020 and **FAccT** since 2021; the
dblp key is `db/conf/fat`.

## Official workflow

- FAccT conference hub (FAccT 2027: Porto, Portugal): https://facctconference.org/
- FAccT 2027 Call for Papers (dates, page limit, focus areas, Program Chairs): https://facctconference.org/2027/cfp.html
- FAccT 2027 Author Guide (template, endmatter, anonymity, AI policy, APCs): https://facctconference.org/2027/authorguide.html
- FAccT 2027 Reviewer Guide (criteria, reviewer timeline): https://facctconference.org/2027/rguide.html
- FAccT 2027 Area Chair Guide: https://facctconference.org/2027/acguide.html
- FAccT 2027 submission + review platform (OpenReview): https://openreview.net/group?id=ACM.org/FAccT/2027/Conference
- FAccT Blog (timeline and process announcements): https://facct-blog.github.io/
- ACM TAPS workflow (LaTeX / Word templates): https://www.acm.org/publications/taps/word-template-workflow
- ACM LaTeX template package (`sample-sigconf-authordraft.tex`): https://www.acm.org/publications/authors/submissions
- ACM Open participating institutions (does an APC apply?): https://libraries.acm.org/acmopen/open-participants
- History — FAccT 2026 (Montréal, Jun 25-28, 2026): https://facctconference.org/2026/index.html,
  CFP https://facctconference.org/2026/cfp.html, committees https://facctconference.org/2026/committees.html,
  CRAFT call https://facctconference.org/2026/cfpcraft.html
- FAccT 2026 proceedings (ACM DL): https://dl.acm.org/doi/proceedings/10.1145/3805689

## Cross-check surfaces (when a primary page is blocked)

- OpenReview API (`api2.openreview.net/groups?id=ACM.org/FAccT/2027/Conference`) for the edition
  title, location, and start date.
- Crossref (`api.crossref.org/works/<DOI>`) for ACM DL proceedings records when `dl.acm.org`
  returns 403.
- ACM DL FAccT proceedings (2019 onward) for accepted-paper verification.
- PMLR vol 81 for the FAT* 2018 proceedings (the inaugural edition was published in PMLR, not ACM DL).
- dblp FAccT/FAT* stream: https://dblp.org/db/conf/fat/index.html

## Author-side checks

- OpenReview profile (unaffiliated authors: weeks ahead), conflicts, coauthor emails, and the
  mandatory **abstract-registration** step (with **focus-area** selection and the archival choice)
  that precedes the paper deadline; the author list freezes there.
- **Every author signs up to review** (FAccT 2027 requirement).
- ACM TAPS compliance — LaTeX `acmart` built anonymized for review (e.g.
  `manuscript,screen,review,anonymous`), single-column, or the ACM Word template; the page budget
  (14 pages + 1 endmatter page; references and appendices unlimited); PDF export.
- Mutual-anonymity sweep: anonymize the PDF, released links, system and field-site names, and —
  critically — **withhold the Positionality / Acknowledgements / Author-Contributions / Competing-
  Interests statements** from the anonymous submission.
- The **required Generative AI Usage Statement** (even if no AI was used) and the **Ethical
  Considerations** statement (with adverse impacts).
- Accountability documentation where relevant: datasheet, model card, data statement, impact
  assessment (see [`../skills/facct-artifact-evaluation`](../skills/facct-artifact-evaluation/SKILL.md)).
- The **archival vs non-archival** choice, and the presentation requirement (in person expected,
  virtual option available).

## Do not infer

- Do not assume the process carries over between editions: the pre-decision rebuttal existed in
  2026 but not 2027, and the AI policy flipped from prohibition (2026) to disclosure (2027).
  Confirm on the current CFP/Author Guide.
- Do not import a SIGSOFT-style ACM artifact **badging** track; FAccT centers documentation and
  release, and the FAccT 2027 Author Guide describes no badge scheme.
- Do not assume FAccT covers APCs. ACM went 100% Open Access on 1 Jan 2026: authors at ACM Open
  institutions pay nothing; others pay an APC (2026 subsidy $250 ACM/SIG members / $350
  non-members; 2027 subsidy not yet announced) unless granted one of ACM's rare waivers.
- If pages disagree, treat the newest CFP, Author Guide, or OpenReview deadline as controlling, and
  record the conflict (e.g., the two different 2027 Program Chair lists on the CFP and a blog byline).
