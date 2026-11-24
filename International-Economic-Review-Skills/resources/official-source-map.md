# International Economic Review Official Source Map

Primary source map for facts used in the IER skill pack. **Access date: 2026-06.** Submission rules, fee,
length and abstract limits, style guidelines, data availability policy and masthead **re-verified
2026-11-24** against the live Penn IER pages (economics.sas.upenn.edu/ier and its submissions,
style-guidelines, data-availability-policy, accepted-manuscript and editorial-information subpages) and the
IER Editorial Express e-submit page, all read directly. The Wiley for-authors page returned HTTP 403 to
automated access on 2026-11-24 and was not re-read. Changes found on 2026-11-24: the Penn pages — not
previously cited in this map — state the **50-page, double-spaced** manuscript limit and an **abstract of not
more than 100 words**, so those two items leave the 待核实 list; the fee (**US$150 / ¥15,000**), portal and
Editor / Co-Editor are **unchanged** (ISER's host is now styled "The University of Osaka"). Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://onlinelibrary.wiley.com/journal/14682354** — official page used to verify or re-check IER scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://onlinelibrary.wiley.com/page/journal/14682354/homepage/forauthors.html** — official page used to verify or re-check IER scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://economics.sas.upenn.edu/ier/submissions** — Penn IER submissions page (read 2026-11-24). Verifies: electronic submission only at **http://editorialexpress.com/ier**; a **submission fee of $150** (¥15,000 via the Japan office) paid after submitting — the manuscript cannot be reviewed until the fee is received; not under consideration elsewhere; must conform to the Review's style guidelines; **single sided, double spaced, and not more than 50 pages**; copyright assignment to Penn Economics and Osaka ISER is a condition of publication.
- **https://economics.sas.upenn.edu/ier/submissions/style-guidelines** — Penn IER style guidelines (read 2026-11-24). Verifies: first page with title, authors, affiliations and an **abstract of not more than 100 words**; sections numbered from the Introduction; single appendix before the references; acknowledgments in Footnote 1; author-date citations with page numbers where applicable; references alphabetical and double spaced at the end.
- **https://economics.sas.upenn.edu/ier/submissions/data-availability-policy** — Penn IER data availability policy (read 2026-11-24). Verifies: IER **adopted the AER data availability policy**; since January 1, 2022 authors acknowledge the data-sharing statement by ticking a box at first submission; data supporting results archived in a public repository as a condition of publication, with a data availability statement and repository link in the final version; exceptions and proprietary-data notices go to the Editor at initial submission; Readme PDF; experimental papers supply original instructions in full as an appendix at submission.
- **https://economics.sas.upenn.edu/ier/submissions/accepted-manuscript** — accepted-manuscript checklist (read 2026-11-24): abstract under 100 words, running head of 35 characters or less, source and PDF files.
- **https://economics.sas.upenn.edu/ier/editorial-information** — editorial information (read 2026-11-24): Editor **Dirk Krueger** (Penn), Co-Editor **Masaki Aoyagi** (ISER, The University of Osaka), editorial board and associate editors.
- **https://editorialexpress.com/cgi-bin/e-editor/e-submit.cgi?dbase=ier** — IER Editorial Express e-submit page (read 2026-11-24): PDF uploads only; notes that a fee is associated with submissions.

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: general-interest economics with a distinctive theory, econometrics, macro, micro, and international reach | Official journal home / author instructions |
| Publisher / owner: Wiley for the Economics Department of the University of Pennsylvania and the Osaka University Institute of Social and Economic Research | Official journal home |
| Submission route: Editorial Express (editorialexpress.com/ier), PDF upload, US$150 fee gate | Penn IER submissions page; Editorial Express e-submit page (re-verified 2026-11-24) |
| Sibling boundary: QJE, JPE, REStud, Econometrica, The Economic Journal, and European Economic Review | Inferred from journal scope and local repository taxonomy |
| general-equilibrium discipline | Official pages above; re-check live before submission |
| structural clarity | Official pages above; re-check live before submission |
| international readership | Official pages above; re-check live before submission |
| theory-empirics balance | Official pages above; re-check live before submission |

## Verified on official pages (2026-06; re-verified 2026-06-22)

- **Editor: Dirk Krueger (University of Pennsylvania); Co-editor: Masaki Aoyagi (Osaka University, ISER).** Re-verified 2026-11-24 on the Penn editorial-information page (and earlier 2026-06-22 on the Penn IER editorial-information page / Wiley editorial board). Roster rotates — re-confirm before naming in a cover letter.
- **Submission fee: US$150** (¥15,000), payable after electronic submission — the manuscript is not reviewed until the fee is received. Re-verified 2026-11-24. Submit at the IER Editorial Express portal **http://editorialexpress.com/ier**. (Penn IER submissions page)
- **Open access (optional):** authors may publish OA under a Creative Commons license for a Wiley Article Publication Charge (exact figure per the Wiley APC list). (Wiley IER for-authors page)

## Unverified / volatile items

- **Resolved 2026-11-24:** length (not more than 50 pages, double spaced) and abstract (not more than 100 words) — Penn submissions and style-guidelines pages.
- **Blinding rules** remain **待核实**: no review model is named on the Penn pages or the Editorial Express page read 2026-11-24, and the Wiley for-authors page was unreachable (HTTP 403).
- Keyword and JEL requirements, and any AI-use policy, are not stated on the Penn pages read 2026-11-24 (待核实; the Wiley page could not be re-read).
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "International Economic Review",
  "verified": "2026-11-24",
  "rules": {
    "main_text_pages_max": {"value": 50, "source": "https://economics.sas.upenn.edu/ier/submissions", "note": "the whole manuscript: single sided, double spaced, not more than 50 pages"},
    "abstract_words_max": {"value": 100, "source": "https://economics.sas.upenn.edu/ier/submissions/style-guidelines"},
    "review_mode": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "submission_fee": {"value": "USD 150 (JPY 15,000 via the Japan office), paid after submitting; no review until received", "source": "https://economics.sas.upenn.edu/ier/submissions"},
    "portal": {"value": "Editorial Express (editorialexpress.com/ier); PDF upload", "source": "https://economics.sas.upenn.edu/ier/submissions"},
    "file_format": {"value": "PDF, single sided, double spaced", "source": "https://economics.sas.upenn.edu/ier/submissions"},
    "reference_style": {"value": "IER house style: author-date citations with page numbers where applicable; alphabetical double-spaced reference list; appendix before references; acknowledgments in Footnote 1", "source": "https://economics.sas.upenn.edu/ier/submissions/style-guidelines"},
    "data_code_policy": {"value": "AER-style data availability policy: acknowledge the data-sharing statement at first submission; deposit data, programs and a Readme PDF in a public repository after conditional acceptance with a data availability statement; exceptions requested at initial submission", "source": "https://economics.sas.upenn.edu/ier/submissions/data-availability-policy"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "keywords_required": {"value": null, "note": "not stated on the official pages as of 2026-11-24"},
    "llm_policy": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
