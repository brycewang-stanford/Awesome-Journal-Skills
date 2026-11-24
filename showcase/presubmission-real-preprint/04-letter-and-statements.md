# Stage 4 — Cover-letter decision and statements

Method: `shared-resources/submission-readiness/cover-letter-and-disclosures.md`. Policy comes from the compiled rules (`00-preflight.json` → AER-Insights rules, verified 2026-11-23) and `AER-Insights-Skills/resources/official-source-map.md` + `skills/aeri-submission`.

**Hard rule observed:** no grant number, conflict, IRB number, registry ID, or editor/reviewer name is invented. A few facts are prefilled from the authors' own public source, and each is marked with where it came from:
- the grants in the title footnote (tex l. 80);
- the commented-out AI declaration (tex l. 275–277).

The authors must confirm those. Everything else is **[AUTHOR TO SUPPLY]**.

---

## 1 · Cover letter: decision

| Rule | Value (source) | Action |
|---|---|---|
| `cover_letter` | **optional**. "A cover letter is not required"; when used, preferably entered in the portal **form field** (submissions page, re-verified 2026-11-23) | **No standalone cover letter.** Put two short notes in the ScholarOne form field: the preprint and the restricted data. |

Why the notes are worth including: the editor needs to know about (i) the public arXiv preprint (relevant under the anonymization RCT), (ii) the confidential platform data, which the AEA Data Editor will assess, and (iii) any coeditor conflict. No other content is needed. Do not repeat the abstract.

**Form-field note (≤ 120 words):**

> This manuscript has been posted as a preprint (arXiv:2611.21070); it is not under review elsewhere. The labor-market data are confidential posting- and contract-level records provided by a private spot-work platform under [AUTHOR TO SUPPLY: agreement type / terms]. Replicators can obtain access by [AUTHOR TO SUPPLY: access route, contact, expected conditions and timeline], and all code and the public tourism inputs (JNTO arrivals; Japan Tourism Agency Overnight Travel Statistics Survey) will be deposited in the AEA Data and Code Repository. [ONLY IF TRUE — AUTHOR TO SUPPLY: Conflict with coeditor <name from the live editors page> because <one-line reason>.]

Notes:
- The coeditor roster changed in 2026: editor Larry Samuelson from September 2026, per the source map. Re-check the live editors page before naming anyone.
- Whether to name the platform in the form field (it already appears in the manuscript's data footnote) is the authors' call. It does not identify the authors.

---

## 2 · Required statements

The rules list exactly one required statement, `disclosure_statement`. The rest are conditional or package items.

| Statement | Status at AER: Insights | Where it goes | Drafted below |
|---|---|---|---|
| Disclosure statement (one per coauthor) | **Required**. A missing statement means the submission is incomplete and is not reviewed | Separate PDF per author. **Not** in the anonymized manuscript | §2.1 |
| AI-use description | **Required if AI was used** in preparing the manuscript | Portal field at submission | §2.2 |
| "Title page" PDF | **Required** under the anonymization RCT | Separate PDF | §2.3 |
| Data availability statement | Required before acceptance (AEA Data and Code Availability Policy); recommended now | README / manuscript at acceptance; brief version in the form field | §2.4 |
| RCT registration | **Not applicable**. Observational design, no field experiment | — | — |
| JEL codes / keywords | Not required by the submissions or style pages (2026-11-23); prepare them if the portal prompts | Portal metadata | §2.5 |
| Ethics / IRB | No requirement stated for secondary aggregated data; [AUTHOR TO SUPPLY: whether an institutional review or exemption applies] | Title page, if applicable | — |

### 2.1 Disclosure statement: template (one per coauthor; repeat for each author)

> **Disclosure Statement — [AUTHOR TO SUPPLY: author name]**
> Manuscript: "Trade Tensions Meet the Gig Economy: Evidence from the 2025 Halving of Chinese Travel to Japan"
>
> 1. Sources of financial support relevant to this paper: [AUTHOR TO SUPPLY. The manuscript's title footnote names JST ERATO JPMJER2301 and JSPS KAKENHI 25K16620; confirm which applies to this author, and list any others within the AEA policy's look-back window.]
> 2. Paid or unpaid positions (officer, director, board member, consultant, employee) with any organization with an interest in the paper's subject or results: [AUTHOR TO SUPPLY. In particular, any paid or unpaid relationship with the data-providing platform, or "None".]
> 3. Data access: The data were provided by Timee, Inc. [AUTHOR TO SUPPLY: whether the provider had the right to review the paper before circulation and whether it requested changes.]
> 4. Other relevant relationships or interests: [AUTHOR TO SUPPLY, or "None".]
>
> Signed: [AUTHOR TO SUPPLY] Date: [AUTHOR TO SUPPLY]

Check the live AEA Disclosure Policy page for the exact items and look-back window before finalizing. The items above are the policy's usual headings, not a substitute for it.

### 2.2 AI-use description (portal field)

The authors' own source contains a commented-out declaration (tex l. 275–277). Draft based on it, **for the authors to confirm as current and complete**:

> During the preparation of this work, the authors used [AUTHOR TO CONFIRM: Claude Code and Codex — as stated in the source's commented-out declaration] to debug code for data construction, estimation, and production of tables and figures, and to improve the language of the manuscript. The authors reviewed and edited all output and take full responsibility for the content. No AI tool is an author.

### 2.3 "Title page" PDF: template

> **Trade Tensions Meet the Gig Economy: Evidence from the 2025 Halving of Chinese Travel to Japan**
> Suguru Otani — Market Design Center, Department of Economics, The University of Tokyo — [email as in the preprint]
> Chang Yang — Graduate School of Economics, The University of Tokyo — [email as in the preprint]
> *Acknowledgements:* [move the current title footnote here verbatim: thanks, the two grant numbers, and the data-provider and platform-staff thanks.] [AUTHOR TO SUPPLY: author-order statement if not alphabetical; corresponding author.]

At the same time, remove from the manuscript: the `\author{…}` block (tex l. 81–84), the title footnote (l. 80), and the PDF `Author` metadata. Also clear `pdfauthor`, for example with `\hypersetup{pdfauthor={}}`, or strip the PDF properties.

Self-citations are already in third person and by name (Kanayama, Miyaji and Otani 2026; Kanayama and Otani 2026; Sekiya et al. 2026). That is consistent with the AEA instructions; keep them that way.

### 2.4 Data availability statement: draft

> The tourism data are public: monthly visitor arrivals by origin from the Japan National Tourism Organization, and overnight stays by prefecture and guest origin from the Japan Tourism Agency's Overnight Travel Statistics Survey [AUTHOR TO SUPPLY: table IDs, URLs, access dates]. The labor-market data are confidential posting- and contract-level records from Timee, Inc., used under [AUTHOR TO SUPPLY: agreement]. They cannot be redistributed by the authors. Researchers may request access by [AUTHOR TO SUPPLY: contact, procedure, conditions, expected time and cost]. [AUTHOR TO SUPPLY, if permitted: The aggregated prefecture-by-week panel used for the main estimates is included in the replication package.] All code is deposited at [openICPSR DOI, at acceptance].

### 2.5 Classification (optional metadata)

The current JEL codes are F14, F16 and J21; keywords are as in the manuscript. Candidates for the authors to consider (their choice; check the AEA JEL guide):
- J23 (labor demand);
- J31 (wage level and structure);
- Z32 (tourism and development).

---

## 3 · Check before upload

Rerun `python3 tools/preflight.py <anonymized.pdf> --venue "AER: Insights"`. Expected result: no `ANON-*` findings. `STMT-MISSING disclosure_statement` will still appear; it is a known false positive, because the statement is a separate upload (see REPORT.md).

Then confirm in the portal:
- the fee band;
- one disclosure PDF per author;
- the title-page PDF;
- the separate, anonymized Supplemental Appendix PDF;
- the AEA word-count PDF.
