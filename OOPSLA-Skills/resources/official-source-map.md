# Official Source Map - OOPSLA

Access date: 2026-07-08. OOPSLA 2027 call, SPLASH 2027 home/dates/organizing committee, SPLASH 2027
artifact-evaluation call and the `oopsla27.hotcrp.com` front and deadlines pages **re-verified
2026-11-24** against the live pages (direct fetch with `curl`; the 403 seen on 2026-07-08 no longer
occurs), and the pack moved from the OOPSLA 2026 volume to OOPSLA 2027.

**Edition status, checked 2026-11-24.** The live edition is **OOPSLA 2027** (the 2027 volume of
PACMPL(OOPSLA)), presented at **SPLASH 2027, Prague, Czechia, October 10-15, 2027** (Diplomat Hotel
Prague). Its call is published on `2027.splashcon.org/track/splashoopsla2027`. **Round 1 closed on
October 14, 2026** (HotCRP: "The deadline for registering submissions has passed"); Round 1 is in
review, with author response **December 1-5, 2026**. The next open door for a new paper is
**Round 2, April 7, 2027** (AoE, firm). OOPSLA 2026 (SPLASH 2026, Oakland, October 4-9, 2026) has
met; its rows below are kept as labelled history.

Every OOPSLA-specific fact in this pack traces to a source in this file. OOPSLA rules are
re-issued for each yearly volume by that volume's two Review Committee chairs (who serve as
PACMPL Associate Editors), so nothing here should outlive its cycle: reopen the current
OOPSLA track page on the SPLASH site, the HotCRP call, and the PACMPL pages on the ACM
Digital Library before advising on any live deadline or format rule.

**Access-method note.** On 2026-07-08 the verification gateway returned HTTP 403 for direct
fetches of `2026.splashcon.org`, `conf.researchr.org`, `oopsla26.hotcrp.com`, `dl.acm.org`,
`dblp.org` and the `lists.seas.upenn.edu` archive, so the 2026 facts (sources 7-15) were
established from search-engine renderings of those exact URLs, triangulated where possible. On
**2026-11-24** sources 1-6 were fetched **directly** and read in full. Anything resting on a single
rendering, or not surfaced at all, is listed under 待核实.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://2027.splashcon.org/track/splashoopsla2027 | OOPSLA 2027 call: two reviewing rounds, **Round 1 deadline October 14, 2026** and **Round 2 deadline April 7, 2027** (AoE), all deadlines firm; new papers in either round; acceptances published in the 2027 PACMPL(OOPSLA) volume and presented **in person** at SPLASH 2027 ("Remote presentations will not be possible"); RC Chairs **Nadia Polikarpova** (UC San Diego) and **Ilya Sergey** (National University of Singapore), contact `oopsla-2027-rc-chairs@googlegroups.com`; at least three reviews and an author response for papers going to full review, but a paper may first get two reviewers and be rejected without a third review or response if both judge it clearly below the bar; outcomes **Accept / Minor Revision / Major Revision / Reject** (Conditional Accept and Minor Revision merged "as in OOPSLA'26"); Round 1 rejects may not resubmit to Round 2, but OOPSLA 2026 rejects are welcome; Minor Revision may revise within the round or wait; Major Revision must wait for the next round; revisions need an explanation of changes and (unless impossible) a PDF diff, same reviewers to the extent possible; only Accepted and Minor Revision papers submit artifacts; **new desk-rejection policy** (policy violations or clearly below bar) and abuse-of-process rule; reviewers may not upload submissions to third-party AI services; **reserve reviewer policy** (one senior author per paper registers on TPMS, with exemptions); **new submission limits**: at most **5** submissions per individual per round, at most **2** with no senior author, excess desk-rejected; template `\documentclass[acmsmall,screen,review,anonymous]{acmart}`; initial submissions at most **23 pages** excluding required statements, references and supplementary material (appendices); revisions up to **25 pages**; camera-ready at most 25 pages plus at most **1** page for data-availability, funding and acknowledgments, plus unlimited references, no page purchase; **double-blind** reviewing with anonymized supplementary material; COI declaration rules (over-declaring forbidden); no concurrent submission, related submissions must be disclosed; **Data-Availability Statement** section just before the references in the initial submission, not counted; HotCRP https://oopsla27.hotcrp.com/; **generative AI**: ACM Policy on Authorship and its FAQ, citations to non-existent work or non-existent results/artifacts are grounds for desk rejection, automated reference checks; OOPSLA1 published no earlier than April 1, 2027 and OOPSLA2 no earlier than October 1, 2027; ACM 100% Open Access with ACM Open or an APC, subsidized 2027 APC **$500** for ACM/SIG members and **$750** for non-members; ACM human-participants policy and ORCID; FAQ criteria (Novelty, Importance, Evidence, Clarity) and LLM/AI-paper scope guidance; preprints on arXiv/home pages allowed, no broad identifiable publicity. | 2026-11-24 |
| 2 | https://2027.splashcon.org/dates | SPLASH 2027 dates (AoE): OOPSLA Round 1 author response Dec 1-5, 2026; Round 1 notification Dec 18, 2026; Round 1 revision submission Jan 22, 2027; Round 1 final notification Feb 12, 2027; Round 1 camera ready Mar 5, 2027; Round 2 submission Apr 7, 2027; Round 2 author response Jun 15-19, 2027; Round 2 notification Jul 2, 2027; Round 2 revision Jul 30, 2027; Round 2 final notification Aug 13, 2027; Round 2 camera ready Aug 27, 2027; artifact submission Jan 26, 2027 (R1) and Aug 3, 2027 (R2); kick-the-tires Feb 1-7, 2027 and Aug 9-15, 2027; artifact notification Mar 9, 2027 and Sep 15, 2027. | 2026-11-24 |
| 3 | https://2027.splashcon.org/ | SPLASH 2027: Prague, Czechia, Sun 10 - Fri 15 October 2027, Diplomat Hotel Prague; tracks OOPSLA and Artifact evaluation; co-located MPLR and SAS (Static Analysis Symposium); keynotes TBA. | 2026-11-24 |
| 4 | https://2027.splashcon.org/committee/splash-2027-organizing-committee | SPLASH 2027 General Chair Filip Křikava (Czech Technical University); OOPSLA Review Committee Co-Chairs Nadia Polikarpova and Ilya Sergey; Artifact Evaluation Co-Chair Satyajit Gokhale (AWS). | 2026-11-24 |
| 5 | https://2027.splashcon.org/track/splash-2027-artifact-evaluation | SPLASH 2027 artifact evaluation: only Accepted and Minor Revision OOPSLA papers; badges **Artifact Available** (DOI, publisher-controlled), **Artifact Evaluated - Functional or Reusable**, and **Results Reproduced**; optional; artifact submitted as a stable DOI URL (Zenodo recommended); single-blind; kick-the-tires phase; VM/Docker packaging guidance; AE chairs Chengpeng Wang, Satyajit Gokhale and Simon Oddershede Gregersen; AEC nominations by December 15, 2026; AE HotCRP link "soon available". | 2026-11-24 |
| 6 | https://oopsla27.hotcrp.com/ and https://oopsla27.hotcrp.com/deadlines | OOPSLA 2027 HotCRP: "Submission deadline: Wednesday Oct 14, 2026, 11:59:59 PM AoE" (past); "The deadline for registering submissions has passed". | 2026-11-24 |
| 7 | https://2026.splashcon.org/track/oopsla-2026 (mirror: https://conf.researchr.org/track/splash-2026/oopsla-2026) | OOPSLA 2026 (history): Round 1 October 10, 2025 and Round 2 March 17, 2026; Accept / Minor Revision / Major Revision / Reject, with Conditional Accept (an OOPSLA'25 outcome) now part of Minor Revision; publication in the 2026 PACMPL(OOPSLA) volume, presentation at SPLASH 2026. | 2026-07-08 |
| 8 | https://oopsla26.hotcrp.com/ and https://oopsla26.hotcrp.com/deadlines | OOPSLA 2026 HotCRP (history); 4-day (Tue-Fri) author response per round. | 2026-07-08 |
| 9 | https://lists.seas.upenn.edu/pipermail/types-announce/2025/012124.html | OOPSLA 2026 Round 1 CFP on TYPES/announce (history). | 2026-07-08 |
| 10 | https://2026.splashcon.org/ and https://2026.splashcon.org/dates | SPLASH 2026 (history): Oakland Marriott City Center, Oakland, California, October 4-9, 2026; OOPSLA talks October 5-7; run jointly with ISSTA 2026; Onward! Papers and Essays tracks. | 2026-07-08 |
| 11 | https://2026.splashcon.org/track/splash-2026-artifact-evaluation | SPLASH 2026 artifact evaluation (history): two-phase with kick-the-tires; Functional and Reusable badges; Available via a Zenodo DOI. | 2026-07-08 |
| 12 | https://dl.acm.org/journal/pacmpl and https://dl.acm.org/journal/pacmpl/open-access | PACMPL — Proceedings of the ACM on Programming Languages — the Gold Open Access journal in which OOPSLA papers appear; scope "from design to implementation and from mathematical formalisms to empirical studies." | 2026-07-08 |
| 13 | PACMPL Vol. 10, Issue OOPSLA1 front matter, https://dl.acm.org/action/showFmPdf?doi=10.1145%2F3712440 | OOPSLA1 2026 issue (April 2026): 75 articles from 227 October-2025 submissions through multi-stage double-anonymous reviewing; volume editors Anders Møller (Aarhus University) and Işıl Dillig (UT Austin) for the 2026 issues. | 2026-07-08 |
| 14 | https://www.sigplan.org/Conferences/SPLASH/ and https://www.sigplan.org/Conferences/OOPSLA/ ; https://www.sigplan.org/announce/2023-09-11-oopsla-2024/ ; https://www.sigplan.org/Resources/EmpiricalEvaluation/ | SIGPLAN's framing of OOPSLA inside SPLASH; the OOPSLA 2024 Round 1 CFP that introduced the two-round machinery; the SIGPLAN Empirical Evaluation Guidelines. | 2026-07-08 |
| 15 | dblp + ACM DL records for exemplars: https://dblp.org/rec/conf/oopsla/GeorgesBE07.html, https://dl.acm.org/doi/10.1145/1167473.1167488, https://dl.acm.org/doi/10.1145/2983990.2984004, https://dl.acm.org/doi/10.1145/3276490, https://dl.acm.org/doi/10.1145/3428275, https://dl.acm.org/doi/10.1145/2509136.2509515 | Venue attribution for every paper cited in `exemplars/library.md`. | 2026-07-08 |

## Verified facts the skills rely on (OOPSLA 2027 volume)

- OOPSLA is a yearly *volume* of PACMPL (Gold Open Access) fed by **two submission rounds**, with
  the talks delivered at SPLASH. For the 2027 volume: **Round 1 closed October 14, 2026**;
  **Round 2 closes April 7, 2027**; both AoE and firm; a new paper may enter either round (source 1).
- Each round ends in **Accept**, **Minor Revision** (revise within the round by its revision
  deadline, or wait for the next round; absorbs the old "Conditional Accept" as in OOPSLA'26),
  **Major Revision** (must wait for the next round), or **Reject**. A Round 1 reject cannot be
  resubmitted to Round 2; the rule is per year, so OOPSLA 2026 rejects may come to OOPSLA 2027 and
  Round 2 rejects may go to the next volume's Round 1. Revisions need an explanation of changes and
  (unless impossible) a PDF diff; the same reviewers are kept to the extent possible (source 1).
- **Two-reviewer early rejection and desk rejection (new for 2027):** a paper may start with two
  reviewers and be rejected without a third review or author response if both judge it clearly
  below the bar with high confidence; the Chairs may desk-reject policy violations or clearly
  below-bar papers, and a desk reject counts for the no-resubmission rule (source 1).
- **Submission limits (new for 2027):** at most **5** submissions per individual per round,
  including at most **2** with no senior author; excess papers desk-rejected, most recent first
  (source 1).
- **Reserve reviewer policy:** for each paper at least one senior author (PhD ≥ 5 years ago or a
  faculty-equivalent role) registers as a reserve reviewer on TPMS, unless exempt (source 1).
- **Format:** `\documentclass[acmsmall,screen,review,anonymous]{acmart}`; at most **23 pages** for an
  initial submission and **25 pages** for a revision (including 2026 minor/major revisions), both
  excluding required statements, references and supplementary material such as appendices; papers
  must be self-contained. Camera-ready: at most 25 pages plus at most 1 page for data-availability,
  funding and acknowledgments, plus references; no page purchase (source 1).
- **Data-Availability Statement** just before the references in the initial submission, not counted
  toward the limit; explain any missing artifact (source 1).
- **Double-blind** reviewing: omit names and institutions, third-person self-citation, anonymized
  supplementary material; preprints allowed, no broad identifiable publicity (source 1).
- **Generative AI:** ACM Policy on Authorship and FAQ; references to non-existent work, or claimed
  results/artifacts that do not exist, are grounds for desk rejection, and references are checked
  automatically (source 1).
- **Publication and APC:** OOPSLA1 no earlier than April 1, 2027; OOPSLA2 no earlier than October 1,
  2027. ACM is 100% Open Access: no APC for authors at ACM Open institutions; otherwise the
  subsidized 2027 APC is $500 (ACM/SIG members) or $750 (non-members) (source 1).
- **Presentation:** in person at SPLASH 2027, Prague, October 10-15, 2027; remote presentation not
  possible (sources 1, 3).
- **Artifact evaluation (SPLASH 2027):** Accepted and Minor Revision papers only; badges Available,
  Functional / Reusable, and Results Reproduced; kick-the-tires phase; Round 1 artifacts due
  January 26, 2027 (sources 2, 5).
- **No standing editor-in-chief.** The rotating analogue is the pair of Review Committee chairs
  (PACMPL Associate Editors): 2027 Nadia Polikarpova and Ilya Sergey; 2026 Anders Møller and Işıl
  Dillig (sources 1, 4, 13).
- **History (2026 volume):** Round 1 October 10, 2025, Round 2 March 17, 2026; OOPSLA1 2026 = 75 of
  227 October-round submissions; SPLASH 2026 in Oakland, October 4-9, 2026, co-located with ISSTA
  2026 (sources 7-13).

## 待核实 (not confirmed as of 2026-11-24 — do not state as fact)

- Whether Onward! Papers/Essays run at SPLASH 2027 (only OOPSLA, artifact evaluation, MPLR and SAS
  are listed on the SPLASH 2027 site as of 2026-11-24), and whether ISSTA co-locates again.
- The SPLASH 2027 artifact-evaluation HotCRP address ("soon available").
- OOPSLA2 2026 acceptance counts and the OOPSLA Distinguished Paper policy/awards.
- Registration fees for SPLASH 2027.

Removed from this list on 2026-11-24 (now confirmed on sources 1-2): the OOPSLA 2027 / SPLASH 2027
call, deadlines, venue and chairs; the round notification and author-response dates (for 2027);
the "same reviewers on resubmission" sentence (present in the 2027 call); the ACM APC amounts
(2027 subsidy stated in the call); and the generative-AI policy text.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "OOPSLA 2027 (PACMPL)",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 23, "source": "https://2027.splashcon.org/track/splashoopsla2027", "note": "OOPSLA 2027 initial submission; excludes required statements, references and appendices/supplementary material; revisions up to 25; camera-ready 25 + 1 page of statements"},
    "page_limit_includes_references": {"value": false, "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "review_mode": {"value": "double-blind", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "anonymized_supplement_required": {"value": true, "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "required_statements": {"value": ["data_availability"], "source": "https://2027.splashcon.org/track/splashoopsla2027", "note": "Data-Availability Statement section just before the references in the initial submission, not counted toward the page limit"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://2027.splashcon.org/track/splashoopsla2027", "note": "ACM Policy on Authorship: generative-AI use to create content must be disclosed in the paper"},
    "template": {"value": "ACM acmart: \\documentclass[acmsmall,screen,review,anonymous]{acmart}", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "portal": {"value": "HotCRP (oopsla27.hotcrp.com); Round 2 deadline April 7, 2027 AoE", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "apc": {"value": "ACM Open institutions: none; otherwise subsidized 2027 APC USD 500 (ACM/SIG members) / 750 (non-members)", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "preprint_policy": {"value": "arXiv/home-page preprints and talks allowed; no broad identifiable publicity during review", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "llm_policy": {"value": "ACM Policy on Authorship and generative-AI FAQ; non-existent references or claimed results/artifacts are grounds for desk rejection (automated reference checks)", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "data_code_policy": {"value": "artifacts not required, but missing artifacts must be explained in the Data-Availability Statement; optional artifact evaluation for Accepted and Minor Revision papers (Available, Functional/Reusable, Results Reproduced)", "source": "https://2027.splashcon.org/track/splash-2027-artifact-evaluation"},
    "supplement_policy": {"value": "appendices as anonymized supplementary material, not counted; reviewers need not read it, so the paper must be self-contained", "source": "https://2027.splashcon.org/track/splashoopsla2027"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
