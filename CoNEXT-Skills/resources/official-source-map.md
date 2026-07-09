# Official Source Map - ACM CoNEXT

Access date: 2026-07-09

This map records the official and cross-check sources used for CoNEXT-specific facts in this
pack. **CoNEXT** is the ACM SIGCOMM International Conference on emerging Networking EXperiments
and Technologies, whose research papers are published as journal articles in **PACMNET
(Proceedings of the ACM on Networking)**. What makes CoNEXT distinctive drives most of this
pack: **two submission cycles per year** (a December deadline and a June deadline) both feeding
one annual program, a journal-style **one-shot "major" revision** decision, **double-anonymous**
review, and a separate **reproducibility committee** awarding optional ACM badges. Reopen the
current-cycle CFP, the Important Dates page, the PACMNET journal pages, and the reproducibility
instructions before giving submission-ready advice.

## Access method note

Direct fetches of `conferences.sigcomm.org`, `dl.acm.org`, `mailman.ripe.net`, and the CFP-mirror
blogs returned **HTTP 403** from the verification gateway on 2026-07-09 (the same egress block
seen when verifying other ACM/SIGCOMM venues). Official pages were therefore read through
**search-engine renderings of the exact URLs** and cross-checked against the ACM Digital Library
PACMNET editorials, the PACMNET tables of contents, dblp CoNEXT proceedings, the CoNEXT HotCRP
sites, and the RIPE RACI mailing-list re-posting of the CFP. Facts that could not be pinned to at
least two independent surfaces are labeled **待核实**. Do not confuse ACM CoNEXT with unrelated
"Conext" trademarks (e.g., Schneider Electric Conext inverters); no fact here derives from them.

## Primary official sources

| # | Source URL | What it verifies | Access date |
|---|---|---|---|
| 1 | https://conferences.sigcomm.org/co-next/2026/ | CoNEXT 2026 (22nd edition) home: Utrecht, The Netherlands, December 7-11, 2026; PACMNET publication; two submission cycles | 2026-07-09 |
| 2 | https://conferences.sigcomm.org/co-next/2026/#!/cfp | CoNEXT 2026 call for papers: December and June cycles, double-anonymous review, one-shot major revision, reproducibility badging | 2026-07-09 |
| 3 | https://conferences.sigcomm.org/co-next/2025/#!/cfp | CoNEXT 2025 CFP (used to confirm page limits, review rounds, revision mechanics, badge opt-in wording carried into 2026) | 2026-07-09 |
| 4 | https://dl.acm.org/journal/pacmnet | PACMNET journal home: open-access ACM journal, backed by SIGCOMM, publishing CoNEXT (and SIGMETRICS) research papers | 2026-07-09 |
| 5 | https://dl.acm.org/journal/pacmnet/how-to-submit | PACMNET submission model: new CoNEXT submissions considered through the CoNEXT CFP; papers scheduled to the closest PACMNET issue | 2026-07-09 |
| 6 | https://dl.acm.org/doi/10.1145/3786284 | PACMNET V4, CoNEXT1, March 2026 Editorial (the spring/June-cycle issue mapping) | 2026-07-09 |
| 7 | https://dl.acm.org/doi/10.1145/3768969 | PACMNET V3, CoNEXT4, December 2025 Editorial (issue/volume cadence and article counts) | 2026-07-09 |
| 8 | https://mailman.ripe.net/archives/list/raci-list@ripe.net/thread/4PYW4UYGT27NL3LABVDMQN6XHSPXAQGI/ | RIPE RACI re-posting of the ACM CoNEXT 2026 CFP (December + June important dates, major-revision path) | 2026-07-09 |
| 9 | https://dl.acm.org/doi/proceedings/10.1145/3765515 | CoNEXT '25 proceedings (21st edition) on ACM DL; cross-check for acceptance counts and paper types | 2026-07-09 |
| 10 | https://www.sigcomm.org/events/conext-conference + https://www.sigcomm.org/events/conext-conference/conext-best-paper-award | CoNEXT series identity (created 2005), SIGCOMM sponsorship, and the annual CoNEXT Best Paper Award | 2026-07-09 |

## Verified 2026-cycle facts used in skills

- **CoNEXT 2026 is the 22nd edition**, held in **Utrecht, The Netherlands, December 7-11, 2026**,
  sponsored by ACM SIGCOMM, with research papers published in **PACMNET** (sources 1, 4).
- **Two submission cycles feed the 2026 program.** The **December cycle**: paper registration
  **5 December 2025**, paper submission **12 December 2025**; early-reject notification February
  2026; notification of acceptance **31 March 2026**; camera-ready **30 April 2026**; publication
  in the **June 2026 PACMNET issue**. Papers given the one-shot major revision: revision due
  **29 May 2026**, resubmission **5 June 2026**, camera-ready **31 July 2026**. The **June cycle**
  submission is **5 June 2026** (sources 2, 8). These two annual deadlines are CoNEXT's defining
  cadence — verify each date on the live Important Dates page before advising.
- **Publication venue is PACMNET**, the open-access *Proceedings of the ACM on Networking*, backed
  by SIGCOMM. Accepted long and short papers are scheduled into the **closest PACMNET issue**;
  issues are labeled by cycle (e.g., PACMNET Vol 4, CoNEXT1, March 2026; Vol 3, CoNEXT4, December
  2025). PACMNET Vol 3 published ~50 articles (a ~56% increase over Vol 2's ~32) (sources 4-7).
- **Review is double-anonymous:** authors and reviewers are mutually hidden. The process runs
  **two rounds of reviews** by TPC members, **online discussion**, and a **TPC meeting**
  (sources 2, 3).
- **Decisions are Accept / Reject / one-shot "major" revision.** A major revision comes with a
  summary of merits and a list of **minimum necessary changes**; authors get roughly **two
  months** to submit the revised version, which the **same reviewers** re-review for a final
  accept/reject (sources 2, 3). This is the journal-style, PACMNET-driven mechanic.
- **Paper types and budgets (verified for 2025; carried into 2026, 待核实 on exact 2026 numbers):**
  **long papers ≤16 pages** plus **unlimited references** and up to **4 pages of appendices**;
  **short papers ≤10 pages** plus unlimited references and up to **2 pages of appendices**. Format
  is the **ACM `acmart` template** (source 3).
- **A reproducibility committee awards optional ACM badges.** To be eligible authors must
  **opt in for ACM badging before the paper submission deadline** and send a **one-page** artifact
  description with pointers to code/artifacts **within a week after acceptance** (sources 2, 3).
- **Submission is on HotCRP**, one site per cycle (e.g., `conext25-june.hotcrp.com` for the
  CoNEXT 2025 June cycle); the CoNEXT 2026 per-cycle HotCRP URLs are on the CFP (sources 3, 5;
  exact 2026 URLs **待核实**).
- **CoNEXT runs a Student Workshop** for graduate students (1-2 page abstracts, poster session,
  published in the CoNEXT Companion proceedings) and recognizes an annual **CoNEXT Best Paper
  Award** (sources 9, 10).
- **Acceptance is competitive:** the June 2025 cycle drew **181 new submissions** with **32
  accepted (27 long + 5 short)**, roughly an **18% rate** for that cycle (source 3; combine with
  the December cycle for the full-year rate — **待核实**).

## The PACMNET journal-style model (honest reading of the cycle question)

CoNEXT's move into **PACMNET** reframed the research track as a **journal**: accepted papers are
PACMNET articles scheduled to the nearest issue, and the process carries a genuine **one-shot
major revision** round re-read by the original reviewers. The **two deadlines per year** are the
operational heart of this model — a paper submitted in December that earns a major revision is
resubmitted in the spring and lands in a later PACMNET issue, so the two cycles are not two
separate conferences but two entry points into **one** annual program and one rolling journal
volume. This differs from single-deadline networking flagships (SIGCOMM, NSDI's cycles) and is
exactly the kind of structure that is re-decided per edition — **verify the two-cycle calendar on
the current Important Dates page before advising**, and never carry a previous year's dates
forward.

## The public-review and shepherding culture

CoNEXT inherits the **SIGCOMM reviewing tradition**: substantive text reviews weighing strengths
and weaknesses, a **TPC meeting**, and **shepherding** of conditionally accepted or revised papers
by a designated TPC member who confirms the required changes were made. SIGCOMM-family venues have
historically published a **public review** (a signed reviewer's framing) alongside some papers;
whether CoNEXT 2026 publishes public reviews with PACMNET articles, and the exact shepherding
mechanics for the one-shot revision, are **待核实** on the live CFP.

## No editor-in-chief of the conference; open access

CoNEXT has **no standing conference editor-in-chief**; the rotating analogue is the per-edition
General Chairs and TPC (Program) Co-Chairs, appointed under ACM SIGCOMM. PACMNET does have a
journal Editorial Board, but per-edition conference leadership rotates. PACMNET is **open access**;
at least one author presents each accepted paper at CoNEXT.

## Still cycle-volatile (verify every year)

- Both cycles' exact dates, registration/abstract cutoffs, and time zones (AoE vs. local).
- Page budgets and which `acmart` variant/format the CFP mandates (2026 numbers **待核实**).
- One-shot major-revision mechanics: revision window length, re-review assignment, and page delta.
- Reproducibility-committee badge set offered, the opt-in deadline, and whether evaluation is
  mandatory or optional.
- Whether public reviews are published with PACMNET articles and the shepherding procedure
  (**待核实**).
- Per-cycle HotCRP URLs and the CoNEXT 2026 organizing-committee roster (General Chairs, TPC
  Co-Chairs) — reported names circulate but are **待核实** beyond the live committee page.
