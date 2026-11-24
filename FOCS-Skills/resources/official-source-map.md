# Official Source Map - FOCS

Access date: 2026-07-08 (dead links re-checked 2026-11-23). FOCS 2026 call, home page,
organizers, workshop call, HotCRP portal, TCMF news and the FOCS 2026 business-meeting slides
**re-verified 2026-11-24** against the live official pages (direct fetch with `curl`; the
gateway block described below no longer applies).

**Edition status, checked 2026-11-24.** FOCS 2026 (67th, New York, November 8-11, 2026) has
met, and it is still the **latest published FOCS call**. The next edition is announced but
has no call: the FOCS 2026 business-meeting slides, posted by TCMF on November 15, 2026
(https://tc.computer.org/tcmf/2026/11/15/focs-2026-business-meeting-slides/, linking
https://www.cs.columbia.edu/~rocco/FOCS2026-Business-Meeting.pdf), announce **FOCS 2027 in San
Diego, November 8-11, 2027** (Monday-Thursday, Hyatt Regency La Jolla; optional workshops
Friday November 12, 2027), General Chairs **Russell Impagliazzo and Shachar Lovett** (UC San
Diego), Program Committee Chair **Yuval Rabani**, with registration "about $800" for
non-students (tentative). But https://focs.computer.org/2027/ returns HTTP 404,
`focs27.hotcrp.com` does not exist, and https://ieee-focs.org/ still lists FOCS 2026 as the
upcoming conference — **no FOCS 2027 CFP, deadline, format or review rules are published**.
The rules below and in the machine-readable block are therefore the FOCS 2026 rules,
labelled as such. Do not project FOCS 2026's April 1 deadline onto FOCS 2027.

This map records the official sources behind every FOCS-specific fact in this
pack. FOCS policy is re-issued per edition by the program committee appointed
under IEEE Computer Society TCMF sponsorship; reopen the live
`focs.computer.org/<year>/` pages before giving deadline-sensitive advice.

## Access-method note

**Updated 2026-11-24:** every URL in the table below answered a direct `curl` fetch on
2026-11-24 (HTTP 200; dblp 202), so the FOCS 2026 facts are now read first-hand rather
than through search renderings. The paragraph below records the original 2026-07-08 method.

Direct fetches of `focs.computer.org`, `sanjeevkhanna.org`, and several IEEE
pages returned HTTP 403 through this environment's gateway on 2026-07-08. All
facts below were therefore verified through **search-engine renderings of the
exact official URLs**, cross-checked against the IEEE Computer Society TCMF
news pages, the HotCRP portal listing, IEEE Xplore / IEEE CS Digital Library
proceedings records, dblp records, the Windows On Theory community blog, and
university award announcements. Anything not pinned down this way is marked
待核实 below and phrased as a question in the skills, never as a fact.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://focs.computer.org/2026/ | FOCS 2026 identity: 67th Annual Symposium on Foundations of Computer Science, NYU Kimmel Center for University Life, New York, NY, USA, November 8-11, 2026, co-located with TCC 2026; sponsorship by the IEEE Computer Society Technical Committee on Mathematical Foundations of Computing (TCMF). Re-read 2026-11-24: important dates (submission April 1, 2026 5:00 PM EDT; paper notification July 3, 2026; workshop proposals July 31, 2026; camera-ready October 1, 2026; early registration October 25, 2026); organizers — Program Chair Sanjeev Khanna (New York University), Program Co-Chair Sepehr Assadi (University of Waterloo), General Chair Marshall Ball (NYU), General Co-Chairs Benedikt Bünz and Tal Malkin, SafeToC advocates. | 2026-07-08; re-read 2026-11-24 (direct fetch) |
| 2 | https://focs.computer.org/2026/call-for-papers-2/ (mirrored at https://sanjeevkhanna.org/FOCS2026_CFP.html) | FOCS 2026 CFP: submission deadline Wednesday April 1, 2026, 5 PM EDT (21:00 UTC); scope = new and original research on theory of computation, including papers broadening theory's reach; no page limit, full version encouraged as the submission; only abstract + references + first ten pages guaranteed committee reading; 11-point-plus single-column format, 1-inch margins, letter paper; PDF without copying/printing security restrictions; double-blind reviewing; SIGACT prior/simultaneous-publication policy; expectation that accepted authors make full papers with proofs publicly available by camera-ready; PC chair Sanjeev Khanna (chair) and Sepehr Assadi (co-chair). Re-read 2026-11-24, which additionally pinned: proofs must be provided so the main claims can be fully verified; the acknowledgement section must be omitted at submission and own work cited in the third person; SafeToC conflict-of-interest categories; the **LLM / generative-AI policy** (only humans may be authors; substantive use must be disclosed in an "AI Disclosure" statement at the end of the paper; minor copy-editing exempt; authors responsible for hallucinated references); PC-member submissions allowed (except chair and co-chair); citation best practices (avoid "et al.", alphanumeric `alpha` style preferred, optional table of contents not counted toward the first ten pages); Machtey eligibility = all authors full-time students at submission. | 2026-07-08; re-read 2026-11-24 (direct fetch) |
| 3 | https://focs26.hotcrp.com/ | HotCRP as the FOCS 2026 submission system ("The deadline for registering submissions has passed" on 2026-11-24). | 2026-07-08; re-read 2026-11-24 |
| 3a | https://tc.computer.org/tcmf/2026/11/15/focs-2026-business-meeting-slides/ (slides at https://www.cs.columbia.edu/~rocco/FOCS2026-Business-Meeting.pdf) | FOCS 2026 PC chairs' report: 686 submissions, 13 withdrawn, 673 after withdrawals, 174 accepted (25.85%), 172 talk slots; review timeline April 1 deadline → July 3 decisions; 31 submissions judged non-substantive or "AI slop"; 1032 external reviewers. FOCS 2027 announcement: San Diego, November 8-11, 2027 (Hyatt Regency La Jolla, optional workshops November 12, 2027); General Chairs Russell Impagliazzo and Shachar Lovett; PC Chair Yuval Rabani. | 2026-11-24 (direct fetch; PDF linked from the TCMF post) |
| 3b | https://focs.computer.org/2027/ | HTTP 404 on 2026-11-24: no FOCS 2027 site or CFP yet. | 2026-11-24 |
| 4 | https://focs.computer.org/2026/call-for-workshops/ (announced at https://windowsontheory.org/2026/06/16/call-for-workshop-proposals-focs-2026/) | FOCS 2026 workshops: Sunday November 8, 2026; 2.5-hour or 5-hour in-person workshops; two-page proposals emailed to the workshop chairs (Dakshita Khurana and Sam Hopkins) by July 31, 2026 AoE; notification August 14, 2026. | 2026-07-08 |
| 5 | https://ieee-focs.org/ | FOCS series entry point maintained for the symposium, linking editions and papers lists; on 2026-11-24 its "Upcoming Conferences" still lists only FOCS 2026. | 2026-07-08; re-read 2026-11-24 |
| 6 | https://tc.computer.org/tcmf/ and https://www.computer.org/communities/tcmf | The IEEE Computer Society Technical Committee on Mathematical Foundations of Computing as the sponsoring body (chair Ran Canetti, vice chair Rocco Servedio; FOCS steering committee listed); TCMF news posts republish FOCS CFPs and award announcements. | 2026-07-08; re-read 2026-11-24 |
| 7 | https://ieeexplore.ieee.org/xpl/conhome/1000292/all-proceedings and https://www.computer.org/csdl/proceedings/1000292 | The Annual IEEE Symposium on Foundations of Computer Science proceedings series in IEEE Xplore and the IEEE CS Digital Library — the publication channel for accepted papers. | 2026-07-08 |
| 8 | https://focs.computer.org/2025/call-for-papers/ | FOCS 2025 (66th edition): Sydney, Australia, December 14-17, 2025; double-blind reviewing; submissions via focs25.hotcrp.com. | 2026-07-08 |
| 9 | https://focs.computer.org/2024/call-for-papers/ and https://focs.computer.org/2023/call-for-papers/ | FOCS 2024 (65th, Chicago, October 27-30, 2024; deadline April 4, 2024) and FOCS 2023 (64th) both used double-blind reviewing, with purpose language: enabling initial judgment without bias, not making author identification impossible. | 2026-07-08 |
| 10 | https://tc.computer.org/tcmf/2024/11/14/focs-2024-test-of-time-awards-announced/ and https://focs.computer.org/2025/test-of-time-awards/ | FOCS Test of Time Awards: 2024 winners (target years 1994/2004/2014) include Shor's quantum algorithms paper, Simon's quantum power paper, Sipser-Spielman expander codes, Khot-Kindler-Mossel-O'Donnell Max-Cut inapproximability, Micciancio's Gaussian-measures reductions, and Abboud-Vassilevska Williams on popular conjectures; 2025 winners (1995/2005/2015) include Chor-Goldreich-Kushilevitz-Sudan private information retrieval, Auer-Cesa-Bianchi-Freund-Schapire adversarial bandits, and Mehta-Saberi-Vazirani-Vazirani AdWords; 2026 call for nominations posted May 16, 2026 (tc.computer.org/tcmf/2026/05/16/focs-test-of-time-award-call-for-nominations-2026/). | 2026-07-08 |
| 11 | https://www.mit.edu/~lids/news-and-events/news/brice-huang-receives-machtey-award-best-student-paper-focs-2024.html (MIT-hosted copy of the LIDS news item, which no longer resolves on lids.mit.edu; re-read 2026-11-23) and https://news.cs.washington.edu/2026/03/12/allen-school-ph-d-student-er-cheng-tang-earns-best-student-paper-at-focs-2025-for-obfuscating-quantum-programs/ | Machtey Award (FOCS best student paper): 2024 co-winners "Capacity Threshold for the Ising Perceptron" (Brice Huang) and "Optimal Quantile Estimation: Beyond the Comparison Model" (Meghal Gupta, Mihir Singhal, Hongxun Wu); 2025 co-winner Mi-Ying (Miryam) Huang and Er-Cheng Tang for obfuscating unitary quantum programs. | 2026-07-08 |
| 12 | https://dblp.org/rec/conf/focs/Shor94.html | Peter W. Shor, "Algorithms for Quantum Computation: Discrete Logarithms and Factoring," Proceedings of the 35th Annual Symposium on Foundations of Computer Science, Santa Fe, November 20-22, 1994, pp. 124-134 — the exemplar library's dblp anchor. | 2026-07-08 |
| 13 | https://acm-stoc.org/stoc2026/stoc2026-cfp.html | The sibling beat: STOC 2026 deadline November 4, 2025 (4:59pm EST) and conference June 22-26, 2026 — used for the two-flagship calendar advice; also documents that SIGACT policy governs both venues' publication rules. | 2026-07-08 |

## Verified 2026-cycle facts used in the skills

- FOCS 2026 is the 67th edition: New York, NY, November 8-11, 2026, under
  IEEE Computer Society TCMF sponsorship (sources 1, 6).
- Submissions closed Wednesday, April 1, 2026, 5:00 PM EDT (21:00 UTC) on
  HotCRP (`focs26.hotcrp.com`); paper notification July 3, 2026; camera-ready
  October 1, 2026 (sources 1, 2, 3, re-read 2026-11-24 — these two dates were
  待核实 before).
- FOCS 2026 accepted 174 of 673 submissions remaining after 13 withdrawals
  (686 received), 25.85%, per the PC chairs' business-meeting report (source 3a).
- No page limit; the full version is the encouraged submission; committee
  reading is guaranteed only for abstract + references + first ten pages
  (source 2).
- Format floor: 11-point or larger, single column, single-spaced with ample
  spacing, at least 1-inch margins, letter paper; PDF must carry no security
  restrictions on copying or printing (source 2).
- FOCS 2026 used double-blind reviewing; FOCS has used it at least since the
  2023 cycle — several years before STOC's 2026 adoption (sources 2, 8, 9, 13).
- SIGACT's prior/simultaneous-publication policy applies at this IEEE venue;
  different-format prior appearances need pre-submission contact with the PC
  chair (source 2).
- Accepted authors are expected to make full papers with complete proofs
  publicly available by the camera-ready deadline (source 2).
- Anonymity details: no names, affiliations or emails; third-person
  self-citation; the acknowledgement section is omitted at submission
  (source 2, re-read 2026-11-24).
- AI policy (source 2, re-read 2026-11-24): only humans may be authors;
  substantive LLM/generative-AI use must be disclosed in an "AI Disclosure"
  statement at the end of the paper, naming the tool and the affected parts;
  minor copy-editing or grammar help needs no disclosure; authors are
  responsible for fabricated ("hallucinatory") references.
- The FOCS 2026 PC chair is Sanjeev Khanna (New York University; this map said
  University of Pennsylvania before the 2026-11-24 re-read), with co-chair
  Sepehr Assadi (University of Waterloo) — a one-cycle fact (sources 1, 2).
- Workshops run Sunday November 8, 2026; proposals (two pages) due July 31,
  2026 AoE to workshop chairs Dakshita Khurana and Sam Hopkins; decisions
  August 14, 2026 (source 4).
- Award lineage: the Machtey Award honors the best student paper(s) each
  year; the Test of Time Award (annual since 2019) honors FOCS papers from
  roughly 10, 20, and 30 years earlier (sources 10, 11).
- Proceedings are published in IEEE Xplore and the IEEE CS Digital Library
  under the Annual IEEE Symposium on Foundations of Computer Science series
  (source 7).

## Organizers and fee model

FOCS has no standing editor-in-chief; the rotating analogue is the
per-edition PC chair and organizing team appointed under TCMF (2026: PC chair
Sanjeev Khanna, co-chair Sepehr Assadi; 2027: PC chair Yuval Rabani, announced
at the FOCS 2026 business meeting — re-check every cycle). There is no article-processing
charge: IEEE proceedings publication is funded through the conference, and
authors' direct costs are registration and travel. Posting the full version
on arXiv or ECCC is free.

## 待核实 (could not be verified on 2026-07-08 — do not state as fact; list re-checked 2026-11-24)

- Camera-ready format instructions, proceedings page allowance, and the IEEE
  copyright/publication form details for 2026 (acceptance packet controls).
- Registration and in-person presentation obligations for accepted papers.
- Whether the FOCS 2026 program runs single-track or with parallel sessions.
- Whether the 2026 PC initiated any author-contact or clarification round.
- The first FOCS edition to use double-blind reviewing (confirmed 2023-2026;
  earlier cycles unchecked).
- Exact Machtey Award eligibility wording for 2026 (student-authorship
  criteria are applied by the PC; the packet/CFP of the cycle controls).
- FOCS 2027 CFP: venue, dates and chairs are announced (source 3a) but no
  deadline, format, review model or AI policy is published as of 2026-11-24;
  the April-deadline rhythm is a historical pattern only.
- Removed 2026-11-24 (now verified): FOCS 2026 notification and camera-ready
  dates (July 3 / October 1, 2026), FOCS 2026 acceptance statistics, FOCS 2027
  venue and dates.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and
python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "FOCS 2026",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": null, "note": "FOCS 2026 rules (latest published call; FOCS 2027 CFP not out as of 2026-11-24): no page limit, full version encouraged; only the abstract, references and the first ten pages after the title page are guaranteed to be read"},
    "review_mode": {"value": "double-blind", "source": "https://focs.computer.org/2026/call-for-papers-2/", "note": "FOCS 2026; acknowledgements omitted at submission, own work cited in the third person"},
    "template": {"value": "no class file: 11-point or larger, single-column, single-spaced, at least 1-inch margins, letter paper", "source": "https://focs.computer.org/2026/call-for-papers-2/"},
    "file_format": {"value": "PDF without security restrictions on copying or printing", "source": "https://focs.computer.org/2026/call-for-papers-2/"},
    "portal": {"value": "HotCRP (focs26.hotcrp.com for FOCS 2026; no FOCS 2027 site yet)", "source": "https://focs.computer.org/2026/call-for-papers-2/"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://focs.computer.org/2026/call-for-papers-2/", "note": "FOCS 2026: an 'AI Disclosure' statement at the end of the paper if LLMs/generative AI generated or materially affected substantive content; minor copy-editing exempt"},
    "llm_policy": {"value": "humans only as authors; disclose substantive generative-AI use in an end-of-paper AI Disclosure statement; authors responsible for errors and fabricated references", "source": "https://focs.computer.org/2026/call-for-papers-2/"},
    "preprint_policy": {"value": "arXiv/ECCC/ePrint posting and talks encouraged; full paper with proofs expected public by camera-ready; SIGACT prior/simultaneous-submission policy", "source": "https://focs.computer.org/2026/call-for-papers-2/"},
    "reference_style": {"value": "preferably alphanumeric (e.g. BibTeX alpha/alphaurl); avoid 'et al.' in favour of all surnames", "source": "https://focs.computer.org/2026/call-for-papers-2/", "note": "recommended best practice, not a rejection criterion"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
