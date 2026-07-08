# Official Source Map - OOPSLA

Access date: 2026-07-08

Every OOPSLA-specific fact in this pack traces to a source in this file. OOPSLA rules are
re-issued for each yearly volume by that volume's two Review Committee chairs (who serve as
PACMPL Associate Editors), so nothing here should outlive its cycle: reopen the current
OOPSLA track page on the SPLASH site, the HotCRP call, and the PACMPL pages on the ACM
Digital Library before advising on any live deadline or format rule.

**Access-method note (2026-07-08):** the verification environment's gateway returned
HTTP 403 for direct fetches of `2026.splashcon.org`, `conf.researchr.org`,
`oopsla26.hotcrp.com`, `dl.acm.org`, `dblp.org`, and the `lists.seas.upenn.edu` mailing-list
archive. All facts below were therefore established from search-engine renderings of those
exact URLs, triangulated across at least two independent renderings where possible
(SPLASH track page + HotCRP deadlines page + TYPES/announce CFP text; ACM DL front matter +
dblp records for exemplars). Anything resting on a single rendering, or not surfaced at all,
is listed under 待核实. Open the primary URLs yourself before treating any number as final.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://2026.splashcon.org/track/oopsla-2026 (mirror: https://conf.researchr.org/track/splash-2026/oopsla-2026) | OOPSLA 2026 track: two reviewing rounds — Round 1 papers due October 10, 2025 and Round 2 papers due March 17, 2026, both 11:59:59 PM AoE and firm; new papers accepted in either round; per-round outcomes Accept / Minor Revision / Major Revision / Reject, with the note that OOPSLA'25's separate "Conditional Accept" and "Minor Revision" outcomes were merged into a single "Minor Revision" for 2026; an author-response opportunity before decisions are finalized; publication in the 2026 PACMPL(OOPSLA) volume with in-person presentation at SPLASH. | 2026-07-08 |
| 2 | https://oopsla26.hotcrp.com/ and https://oopsla26.hotcrp.com/deadlines | OOPSLA 2026 submission site is HotCRP; both round deadlines restated; the 2026 call uses a 4-day (Tue–Fri) author-response period in each round; OOPSLA1 acceptances published no earlier than April 1, 2026 and OOPSLA2 acceptances no earlier than October 1, 2026. | 2026-07-08 |
| 3 | https://lists.seas.upenn.edu/pipermail/types-announce/2025/012124.html | OOPSLA 2026 Round 1 Call for Papers as circulated on TYPES/announce — cross-check for the round structure, HotCRP address, and PACMPL(OOPSLA) publication promise. | 2026-07-08 |
| 4 | https://2026.splashcon.org/ and https://2026.splashcon.org/dates | SPLASH 2026 umbrella: Oakland Marriott City Center, Oakland, California; main conference Sunday October 4 – Friday October 9, 2026, with workshops and co-located events from Saturday October 3; OOPSLA talks scheduled Monday October 5 – Wednesday October 7; SPLASH 2026 runs jointly with ISSTA 2026 (shared workshops, posters, tool demonstrations, and Student Research Competition under the "SPLASH/ISSTA 2026" label); Onward! Papers and Onward! Essays run as their own SPLASH tracks. | 2026-07-08 |
| 5 | https://2026.splashcon.org/track/splash-2026-artifact-evaluation | SPLASH 2026 artifact evaluation: two-phase process opening with a kick-the-tires integrity check; badge ladder Functional (baseline accepted artifact, documented with an inventory and enough description to exercise it) and Reusable (Functional plus documentation and organization that support reuse); every passing artifact is strongly encouraged to also earn Available by depositing a snapshot on Zenodo for a DOI, absent licensing or privacy constraints. | 2026-07-08 |
| 6 | https://dl.acm.org/journal/pacmpl and https://dl.acm.org/journal/pacmpl/open-access | PACMPL — Proceedings of the ACM on Programming Languages — as the Gold Open Access journal in which OOPSLA papers appear; scope "from design to implementation and from mathematical formalisms to empirical studies." | 2026-07-08 |
| 7 | PACMPL Vol. 10, Issue OOPSLA1 front matter, https://dl.acm.org/action/showFmPdf?doi=10.1145%2F3712440 | The OOPSLA1 2026 issue (April 2026): 75 articles selected from 227 submissions to the October 2025 round through multi-stage double-anonymous reviewing; volume editors (Review Committee chairs) Anders Møller (Aarhus University) and Işıl Dillig (UT Austin) for both 2026 issues. | 2026-07-08 |
| 8 | https://www.sigplan.org/Conferences/SPLASH/ and https://www.sigplan.org/Conferences/OOPSLA/ | SIGPLAN's framing: OOPSLA as the research-paper conference operating inside SPLASH ("Systems, Programming, Languages, and Applications: Software for Humanity"), plus the standing "Objectives of OOPSLA" statement. | 2026-07-08 |
| 9 | https://www.sigplan.org/announce/2023-09-11-oopsla-2024/ | The OOPSLA 2024 Round 1 CFP, which introduced the modern two-round machinery and states that resubmitted (Major Revision) papers keep the same reviewers to the extent possible. | 2026-07-08 |
| 10 | https://www.sigplan.org/Resources/EmpiricalEvaluation/ | The SIGPLAN Empirical Evaluation Guidelines — the checklist OOPSLA reviewers and artifact evaluators apply to measurement-bearing claims. | 2026-07-08 |
| 11 | dblp + ACM DL records for exemplars: https://dblp.org/rec/conf/oopsla/GeorgesBE07.html, https://dl.acm.org/doi/10.1145/1167473.1167488, https://dl.acm.org/doi/10.1145/2983990.2984004, https://dl.acm.org/doi/10.1145/3276490, https://dl.acm.org/doi/10.1145/3428275, https://dl.acm.org/doi/10.1145/2509136.2509515 | Venue attribution for every paper cited in `exemplars/library.md` — each checked to be an OOPSLA proceedings entry or a PACMPL Issue OOPSLA article, never a sibling venue. | 2026-07-08 |

## Verified facts the skills rely on

- OOPSLA today is a yearly *volume* of PACMPL (Proceedings of the ACM on Programming
  Languages, Gold Open Access) fed by **two submission rounds**, with the conference talks
  delivered at SPLASH. For the 2026 volume: Round 1 closed October 10, 2025; Round 2 closed
  March 17, 2026; both AoE and firm; a new paper could enter either round.
- Each round ends in one of four outcomes: **Accept**, **Minor Revision** (fixable concerns,
  handled within the same round — for 2026 this outcome absorbed what OOPSLA'25 called
  "Conditional Accept"), **Major Revision** (an invitation to resubmit to the **next** round
  against an explicit list of expectations), or **Reject**.
- Under the two-round rules as introduced for OOPSLA 2024, a Major-Revision resubmission
  keeps its reviewers to the extent possible, so the revision answers a known audience.
- Authors get a written response opportunity before each round's decisions are finalized;
  the 2026 call scheduled it as a 4-day Tuesday-to-Friday window per round.
- Submissions go through HotCRP (`oopsla26.hotcrp.com` for the 2026 volume), formatted with
  `\documentclass[acmsmall,screen,review,anonymous]{acmart}`: at most **23 pages** for an
  initial submission and up to **25 pages** for an invited revision, in both cases excluding
  references, required statements, and appendices. A **Data-Availability Statement** must
  appear before the references and does not count against the limit.
- Reviewing is **double-anonymous**, described in the PACMPL OOPSLA1 2026 front matter as
  multi-stage.
- Round 1 acceptances of the 2026 volume were published as **PACMPL Vol. 10, Issue OOPSLA1**
  no earlier than April 1, 2026 (75 articles from 227 October-round submissions, roughly a
  third); Round 2 acceptances form **Issue OOPSLA2**, published no earlier than October 1,
  2026. Presentation happens at SPLASH 2026 in Oakland, October 4–9, 2026 (OOPSLA talks
  October 5–7), co-located with ISSTA 2026, alongside the Onward! Papers and Essays tracks.
- Artifact evaluation at SPLASH 2026 is two-phase (kick-the-tires, then full review) and
  awards Functional, Reusable, and — via a Zenodo DOI deposit — Available badges.
- There is no standing editor-in-chief for OOPSLA. The rotating analogue is the pair of
  Review Committee chairs who serve as PACMPL Associate Editors for that year's two issues;
  for 2026 these were Anders Møller and Işıl Dillig. Authors pay through the ACM open-access
  machinery rather than a subscription; SPLASH attendance is funded by registration.

## Cycle position as of 2026-07-08

Both OOPSLA 2026 rounds are closed. The OOPSLA1 issue is published; OOPSLA2 acceptances are
in production for autumn publication; the conference itself (Oakland, October 2026) has not
yet happened. **The next open target for a new paper is OOPSLA 2027 Round 1**, whose CFP had
not been posted at the access date — see 待核实 below before quoting any 2027 date.

## 待核实 (not confirmed as of 2026-07-08 — do not state as fact)

- **OOPSLA 2027 / SPLASH 2027**: no CFP, deadline, venue, or chairs found. The recent
  pattern (Round 1 in early-to-mid October, Round 2 in mid-to-late March) suggests a Round 1
  deadline around October 2026, but that is an extrapolation.
- Exact calendar dates of the 2026 Round 1 and Round 2 **notifications** and of each
  author-response window (only the 4-day Tue–Fri shape was surfaced).
- Whether the "same reviewers on resubmission" sentence appears verbatim in the 2026 call
  (verified in the 2024 CFP; the 2026 renderings describe the same mechanism less fully).
- OOPSLA2 2026 acceptance counts and the OOPSLA 2026 Distinguished Paper policy/awards.
- The current ACM/PACMPL article-processing-charge amount and waiver mechanics as they apply
  to OOPSLA 2026 authors — confirm on the ACM DL open-access page before advising on money.
- Any OOPSLA 2026 policy text on LLM-assisted writing or reviewing.
