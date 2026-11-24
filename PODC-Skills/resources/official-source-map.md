# Official Source Map - ACM PODC

Access date: 2026-07-09 (whole call, committee, awards and next edition re-read **directly**
2026-08-27, after the gateway block described below lifted). PODC 2026 call, programme
committee, DMANET call, front-page outcomes and the new PODC 2027 edition pages
**re-verified 2026-11-24** against the live podc.org pages (direct fetch with `curl`).

**Edition status, checked 2026-11-24.** PODC has now opened its 2027 edition site,
https://www.podc.org/podc2027/, and the podc.org front page leads with it: **PODC 2027, the
46th ACM Symposium on Principles of Distributed Computing, June 21-25, 2027, Reykjavik
University, Iceland**. The conference committee is published
(https://www.podc.org/podc2027/conference-committee/): **General Chair Michal Dory**
(University of Haifa), **Local Chair Magnús M. Halldórsson** (Reykjavik University),
**Program Chair Seth Gilbert** (National University of Singapore). But the **PODC 2027 call for
papers is not published**: https://www.podc.org/podc2027/call-for-papers/ and the 2027
program-committee page both say only "Watch this space for more information." — no
deadlines, no page budget, no review model, no HotCRP site. The only 2027 call that is out is
the call for workshops and tutorials (first proposal deadline December 15, 2026; second
February 28, 2027; workshop days June 21 and June 25, 2027). So the **latest published paper
call is still PODC 2026** (Egham, July 6-10, 2026, now met), and the rules below and in the
machine-readable block are the PODC 2026 rules, labelled as such. Do not project PODC 2026's
February deadlines onto PODC 2027; re-read the 2027 call when it appears.

This map records the official and cross-check sources used for PODC-specific facts in this pack.
PODC is the **ACM SIGACT-SIGOPS Symposium on Principles of Distributed Computing**, the flagship
for the *theory* of distributed computing; its calendar, page budget, and review model are decided
per edition. Reopen the current-cycle call for papers, the Important Dates page, and the HotCRP
site before giving submission-ready advice.

## Access method note

**Updated 2026-08-27: `podc.org` answers direct fetches again.** The call for papers, the
program-committee roster, the award announcements and the next-edition page were all read
from the official site on that date, and the facts they carry are no longer second-hand.
`dl.acm.org` is still blocked, so anything resting on the ACM Digital Library (source 6)
still stands on a rendering.

Direct fetches of `podc.org` and `dl.acm.org` failed from the verification gateway on 2026-07-09
(the same block seen when verifying other ACM venues). Official pages were therefore read through
**search-engine renderings of the exact URLs** and cross-checked against dblp, the ACM Digital
Library PODC proceedings, the **DMANET** call-for-papers announcement, wikicfp, and confsearch.
Facts that could not be pinned to a primary rendering are labeled **待核实**.

Two naming/attribution guards:

- **PODC is not PODS.** `PODS` (`Principles of Database Systems`) is the SIGMOD-week database-theory
  venue. No fact here derives from PODS. Search hits mentioning "PoDC / Proof of Double Committee"
  (a blockchain consensus product) are also unrelated and were discarded.
- **PODC is not DISC.** DISC (the EATCS International Symposium on DIStributed Computing) is the
  *other* distributed-theory flagship; PODC and DISC **share** the Dijkstra Prize and the Doctoral
  Dissertation Award but are distinct conferences with distinct calendars and proceedings (DISC uses
  LIPIcs; PODC uses the ACM proceedings). A famous result may have appeared at DISC, not PODC.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://www.podc.org/podc2026/call-for-papers/ | PODC 2026 call: scope, lightweight double-blind review, ACM Master template, 10-page-merits budget with unbounded full version, Brief Announcements track (≤5-page submission), arXiv freedom. Read directly 2026-08-27, which additionally pinned the **AI-tools disclosure rule**, the **typesetting alternative to `acmart`**, the **conflict-of-interest definition** and its ToC advocates, the **award-splitting clause**, the **full-version requirement**, and the **cite-all-authors practice** — every one of them previously unread or 待核实. | 2026-07-09; re-read 2026-08-27 (direct fetch) |
| 1a | https://www.podc.org/podc2026/call-for-papers/ (re-read) | Re-read 2026-11-24 (direct fetch): calendar abstract February 11 / full paper February 16 / notification April 29, 2026 (23:59 AoE); regular papers no page limit, merits within the first 10 pages after the title page; Brief Announcements at most 5 pages; accepted regular papers up to 10 pages and brief announcements up to 3 pages in two-column ACM proceedings format (`\documentclass[sigconf]{acmart}`); lightweight double-blind; AI-use disclosure; conflict-of-interest list of **five** categories (family member or close friend; Ph.D. advisor/advisee or postdoc/undergraduate mentor/mentee within five years; same affiliation; alleged harassment; frequent or recent collaborators within two years); in-person presentation expected and a paid registration required; **ACM Open Access from January 1, 2026: no APC if the corresponding author's institution is in ACM Open, otherwise an APC of $250 (ACM/SIG members) or $350 (non-members)** unless waived. | 2026-11-24 (direct fetch) |
| 2 | https://www.podc.org/podc2026/ | PODC 2026 (45th) home: Royal Holloway, University of London, Egham, England; July 6-10, 2026; co-located with SPAA 2026 | 2026-07-09; re-read 2026-11-24 |
| 3 | http://dmatheorynet.blogspot.com/2026/01/dmanet-podc-2026-second-call-for-papers.html | PODC 2026 second CFP (DMANET): abstract 11 Feb 2026, full paper 16 Feb 2026, notification 29 Apr 2026 (all 23:59 AoE). The camera-ready date of 20 May 2026 recorded on 2026-07-09 does **not** appear in the post as re-read on 2026-11-24 (see 待核实). | 2026-07-09; re-read 2026-11-24 |
| 4 | https://podc26.hotcrp.com/ | PODC 2026 submission site (HotCRP) | 2026-07-09 |
| 5 | https://www.podc.org/podc2026/program-committee/ | PODC 2026 program committee: Chair **Eric Ruppert** (York University) plus 37 named members. Roster read in full 2026-08-27; the 待核实 on it is discharged. | 2026-07-09; read in full 2026-08-27 (direct fetch) |
| 5a | https://www.podc.org/ | PODC 2026 outcomes announced on the front page: **Best Paper** to Kahbod Aeini, Dante Bencivenga, George Giakkoupis and Philipp Woelfel, "Simple and Efficient Randomized Wait-Free Locks"; **Best Student Paper** to Haoran Zhou for "Efficient Counting and Simulation in Content-Oblivious Rings" (with Jérémie Chalopin, Yi-Jun Chang, Giuseppe Antonio Di Luna); **2026 Dijkstra Prize** to Das Sarma, Holzer, Kor, Korman, Nanongkai, Pandurangan, Peleg and Wattenhofer for "Distributed Verification and Hardness of Distributed Approximation". | 2026-08-27 (direct fetch) |
| 5b | https://www.podc.org/podc2026/next-podc/ | Tentative PODC 2027 information: Reykjavik University, Iceland; tentative dates June 21 to 25, 2027; local organisation Magnús M. Halldórsson, Maxime Flin, Alexandre Nolin. | 2026-08-27; re-read 2026-11-24 (direct fetch) |
| 5c | https://www.podc.org/podc2027/ | PODC 2027 edition home: June 21-25, 2027 at Reykjavik University, Iceland; "Watch this page for more information." | 2026-11-24 (direct fetch) |
| 5d | https://www.podc.org/podc2027/call-for-papers/ | PODC 2027 call page: "The 46th ACM Symposium on Principles of Distributed Computing, June 21-25, 2027, Reykjavik University, Iceland. Watch this space for more information." — no paper call yet. | 2026-11-24 (direct fetch) |
| 5e | https://www.podc.org/podc2027/conference-committee/ | PODC 2027 committee: Michal Dory (General Chair), Magnús M. Halldórsson (Local Chair), Seth Gilbert (Program Chair), Naama Ben-David (Treasurer), Ajay Singh and Diana Ghinea (Publicity), Quanquan Liu and Alexandre Nolin (Workshops). The 2027 program-committee page is still a placeholder. | 2026-11-24 (direct fetch) |
| 5f | https://www.podc.org/podc2027/call-for-workshops-and-tutorials/ | PODC 2027 workshops and tutorials: days Monday June 21 and Friday June 25, 2027; double deadline, first proposals December 15, 2026 (AoE), notification January 15, 2027; second proposals February 28, 2027 (AoE), final notification March 14, 2027. | 2026-11-24 (direct fetch) |
| 6 | https://dl.acm.org/doi/proceedings/10.1145/3732772 | ACM DL PODC 2025 proceedings (used to confirm the ACM two-column proceedings publication model and the conference series). Still HTTP 403 to `curl` on 2026-11-24. | 2026-07-09 |
| 7 | https://dblp.org/db/conf/podc/podc2026.html | dblp PODC 2026 record (accepted-paper cross-check) and the PODC proceedings series for exemplar verification | 2026-07-09 |
| 8 | https://www.podc.org/dijkstra/ | Edsger W. Dijkstra Prize in Distributed Computing: joint PODC/DISC, decade-of-impact, presented alternately at PODC and DISC | 2026-07-09 |
| 9 | https://www.podc.org/dissertation/ | Principles of Distributed Computing Doctoral Dissertation Award (created 2012; joint PODC/DISC) | 2026-07-09 |
| 10 | https://spaa.acm.org/ | SPAA 2026 co-location at Royal Holloway, July 6-10, 2026 (confirms the shared venue/dates) | 2026-07-09 |

## Verified 2026 facts used in skills

- **PODC 2026 is the 45th ACM Symposium on Principles of Distributed Computing**, jointly sponsored
  by **ACM SIGACT and SIGOPS**, held at **Royal Holloway, University of London, Egham, England**,
  **July 6-10, 2026**, co-located with **SPAA 2026** (sources 1, 2, 10).
- **Calendar (all 23:59 AoE):** abstract registration **11 February 2026**, full-paper submission
  **16 February 2026**, notification **29 April 2026**, camera-ready **20 May 2026**; submission via
  `podc26.hotcrp.com` (sources 3, 4).
- **Review is lightweight double-blind:** submissions must not reveal author identity — no names,
  affiliations, or email addresses anywhere in the submission (source 1). This is a change from
  PODC's historically single-blind practice; verify the exact wording each cycle.
- **Format is the ACM Master template (`acmart`), two-column proceedings.** Regular submissions have
  **no page limit**, but only the abstract and the **first 10 pages after the title page** are
  guaranteed to be read; material beyond is read at the committee's discretion. Authors are
  encouraged to submit the **full version** (with proofs). Accepted regular papers appear in **≤10
  pages** in two-column ACM proceedings format (source 1).
- **Brief Announcements** are a distinct track: the **submission is at most 5 pages** (including
  title, abstract, and references); accepted Brief Announcements are published at **up to 3 pages**
  in the proceedings (source 1).
- **arXiv/preprint freedom:** authors may post drafts on the web, submit to arXiv, and give talks
  about the work; a preprint is not treated as a dual-submission problem (source 1).
- **Journal invitations:** selected papers are invited to the **Journal of the ACM (JACM)** and to a
  special issue of **Distributed Computing** (reported on the call/series pages).
- **Awards:** every regular paper is eligible for **Best Paper** and **Best Presentation**;
  student-authored papers (full-time students principally responsible) are eligible for **Best
  Student Paper** (source 1, historical CFPs). The **Dijkstra Prize** and the **Doctoral Dissertation
  Award** are held **jointly with DISC** (sources 8, 9).
- **Program Chair: Eric Ruppert** (York University, Canada). The committee is **38 members
  including the chair** (source 5, read in full 2026-08-27) — small enough that conflict
  declarations matter, which is why the call defines them precisely (below).
- **Conflicts of interest are defined, narrowly, in the call** (source 1, read 2026-08-27;
  re-read 2026-11-24): a **family member or close friend**; a Ph.D. advisor or advisee (**no
  time limit**), or a postdoctoral or undergraduate mentor or mentee **within the past five
  years**; a **person with the same affiliation**; a person involved in an alleged harassment
  incident (**the incident need not have been reported**); and frequent collaborators or
  co-authors of a joint publication **within the last two years**. (The family/close-friend
  and same-affiliation categories were omitted from this list before the 2026-11-24 re-read.) Anything outside that list goes to the PC
  chair or to the conference's **Theory of Computing Advocates, Faith Ellen and Idit Keidar**,
  who may be asked to verify a reason confidentially. Do not declare a conflict that is not on
  this list without raising it first — the list is exhaustive by design.
- **AI-tool use must be disclosed in the submission** (source 1, read 2026-08-27): any use
  beyond copyediting or internet search has to have "the nature of the usage" stated, and
  authors remain accountable for the content, including plagiarism and citation. This is a
  disclosure rule, not a prohibition, and it lives in the call rather than in a separate
  policy page.
- **Two typesetting routes, not one** (source 1, read 2026-08-27). Either 11-point-or-larger
  type, single-column, single-spaced, 1-inch margins, letter-size paper; **or** the ACM Master
  template `acmart.cls` **version 1.80 or greater**, declared exactly as
  `\documentclass[acmsmall,nonacm,anonymous]{acmart}`. The `nonacm` and `anonymous` options
  are part of the requirement, not a suggestion — the submission is single-column and
  anonymous, and it is only the *accepted* version that becomes two-column ACM proceedings.
- **If the accepted paper does not fit the 10 proceedings pages, a public full version is
  mandatory** (source 1, read 2026-08-27): it must be available (e.g. on arXiv) **by the
  proceedings due date**, and the proceedings version must refer to it. This is the venue's
  answer to a 10-page cap on a proofs paper, and it is an obligation with a deadline, not an
  option.
- **Cite every author by name.** The call asks authors to avoid "et al." because alphabetical
  author ordering — the norm in this field — turns the abbreviation into a systematic bias
  against everyone after the first name (source 1, read 2026-08-27).
- **The committee may decline or split either award** (source 1, read 2026-08-27). PODC 2026
  did award both: **Best Paper** to Kahbod Aeini, Dante Bencivenga, George Giakkoupis and
  Philipp Woelfel, "Simple and Efficient Randomized Wait-Free Locks"; **Best Student Paper**
  to Haoran Zhou, "Efficient Counting and Simulation in Content-Oblivious Rings", co-authored
  with Jérémie Chalopin, Yi-Jun Chang and Giuseppe Antonio Di Luna (source 5a).

## The proofs-venue model (why there is no artifact track)

PODC evaluates a **model, a theorem, and a proof**. There is **no artifact-evaluation track and no
ACM badge program** at PODC — the analogue of "does the code run" is "does the proof close and are
the model, timing, and failure assumptions stated precisely and honestly." The `podc-experiments`,
`podc-reproducibility`, and `podc-artifact-evaluation` skills are therefore written for a proofs
venue: tight/matching bounds, self-contained proof appendices, checkable assumptions, and — only
where a paper includes them — transparent optional simulations. Do not import an ACM
Available/Functional/Reusable/Reproduced badge workflow; it does not exist here.

## No editor-in-chief; ACM Open Access APC

Like every conference in this collection, PODC has **no standing editor-in-chief**; the rotating
analogue is the per-edition **Program Chair** and program committee, appointed under ACM
SIGACT/SIGOPS (PODC 2027: Program Chair **Seth Gilbert**, source 5e). Proceedings are published by
ACM, and **since January 1, 2026 they are fully Open Access** (source 1a, re-read 2026-11-24):
there is **no APC if the corresponding author's institution participates in ACM Open**; otherwise
each paper owes an **APC of $250 for ACM/SIG members or $350 for non-members**, unless the authors
qualify for an ACM waiver or geographic discount. (Before the 2026-11-24 re-read this map said
"there is no APC"; that was wrong for the 2026 call.) A paid conference registration by one author
is required in any case, and papers are expected to be presented in person (exceptions only in
exceptional circumstances, approved by the PC chair).

## Still cycle-volatile (verify every year)

- All dates and AoE cutoffs, and whether abstract registration precedes the full-paper deadline
  (2026 splits them: 11 Feb / 16 Feb).
- The exact double-blind wording and how strictly it is enforced (**recently changed**, so do not
  carry a prior year's single-blind assumption forward).
- Whether the cycle runs an **author-response / rebuttal** phase. The 2026 call, read in full
  on 2026-08-27, **describes none**, and its calendar leaves no window for one (full paper
  16 Feb, notification 29 Apr, nothing between). Absence from a call is weaker evidence than
  a statement, so this is recorded as *not offered in 2026* rather than *ruled out*: plan for
  no rebuttal, and re-read the call before assuming a later cycle behaves the same way.
- The page-budget wording (the 10-page-merits rule and the ≤10 / ≤3 published limits). The
  `acmart` revision and option string are no longer volatile-unknown — the 2026 call names
  them (≥1.80, `[acmsmall,nonacm,anonymous]`) — but they are still per-edition.
- **Best Presentation** award mechanics and eligibility. Best Paper and Best Student Paper are
  now pinned to the call's own wording and to the 2026 outcomes; the presentation award is
  named in historical calls but not in the 2026 one.
- PODC 2027's paper call: dates (June 21-25, 2027), venue and Program Chair (Seth Gilbert) are
  now published (sources 5c-5e, 2026-11-24), but deadlines, page budget, review model and
  HotCRP site are not.

## 待核实 (could not be confirmed on 2026-11-24)

- **PODC 2026 camera-ready date of 20 May 2026.** Recorded from the DMANET post on 2026-07-09,
  but neither the DMANET post (source 3) nor the PODC 2026 call (source 1) shows a camera-ready
  date when re-read on 2026-11-24, and a web search found no official page stating it. Kept as
  a historical figure; do not cite it as verified.
- The ACM DL PODC proceedings record (source 6): `dl.acm.org` still refuses automated fetches
  (HTTP 403) on 2026-11-24.
- Every PODC 2027 paper-call rule (deadlines, page budget, review model, AI-use wording, APC
  treatment) — the 2027 call page is a placeholder as of 2026-11-24.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "ACM PODC 2026",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": null, "note": "PODC 2026 rules (latest published call; PODC 2027 call not yet out as of 2026-11-24): regular submissions have no page limit, but the merits must be presented within the first 10 pages after the title page and the rest is read at the committee's discretion; accepted regular papers up to 10 two-column proceedings pages"},
    "review_mode": {"value": "double-blind", "source": "https://www.podc.org/podc2026/call-for-papers/", "note": "PODC 2026 lightweight double-blind: no author names, affiliations or emails anywhere in the submission"},
    "template": {"value": "11-point or larger, single-column, single-spaced, 1-inch margins, letter paper; or acmart.cls version 1.80+ with \\documentclass[acmsmall,nonacm,anonymous]{acmart} (accepted papers: [sigconf])", "source": "https://www.podc.org/podc2026/call-for-papers/", "note": "PODC 2026 call"},
    "portal": {"value": "HotCRP (podc26.hotcrp.com for PODC 2026; PODC 2027 site not yet announced)", "source": "https://www.podc.org/podc2026/call-for-papers/"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.podc.org/podc2026/call-for-papers/", "note": "PODC 2026: if AI tools were used beyond copyediting or internet search, the nature of the usage must be disclosed in the submission"},
    "llm_policy": {"value": "disclose any AI-tool use beyond copyediting or internet search in the submission; authors remain accountable for content, plagiarism and citations", "source": "https://www.podc.org/podc2026/call-for-papers/"},
    "preprint_policy": {"value": "drafts may be posted on the web or arXiv and presented in talks; important references must not be omitted or anonymized", "source": "https://www.podc.org/podc2026/call-for-papers/"},
    "supplement_policy": {"value": "no separate supplement: submit the full version (full proofs) as one submission; if an accepted paper exceeds 10 proceedings pages, a public full version (e.g. arXiv) is required by the proceedings due date", "source": "https://www.podc.org/podc2026/call-for-papers/"},
    "apc": {"value": "ACM Open Access: none if the corresponding author's institution is in ACM Open; otherwise $250 (ACM/SIG members) or $350 (non-members), waivers possible", "source": "https://www.podc.org/podc2026/call-for-papers/"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24 (call asks only for a brief abstract on the title page)"}
  }
}
```
