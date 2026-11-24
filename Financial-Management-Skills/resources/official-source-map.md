# Financial Management Official Source Map

Primary source map for facts used in the FM skill pack. **Access date: 2026-06.** Submission fees, masthead, desk-rejection refund, data/code and AI policies **re-verified 2026-11-24** against the live fma.org pages (submissions, editorial board, editorial philosophy, FM Author Toolkit PDF), all read directly. The Wiley For Authors page returned HTTP 403 to automated access on 2026-11-24 and was not re-read. Changes found on 2026-11-24: the PhD-nonmember fee is now **$290** (was $280); the masthead lists **two Editors, Michael Goldstein (Babson) and Kathleen Kahle (Wake Forest University)**, with Shawn Thomas moved to past editors (2022–2025). Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://onlinelibrary.wiley.com/journal/1755053x** — official page used to verify or re-check FM scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://www.fma.org/financial-management** — official page used to verify or re-check FM scope, submission, policy, or author guidance. Access date: 2026-06; **re-verified 2026-11-24** (Editors Michael Goldstein, Babson College, and Kathleen Kahle, Wake Forest University).
- **https://www.fma.org/financial-management-submissions** — **re-verified 2026-11-24.** Submission fees: Professional or PhD Members **$250**; Professional Nonmember **$350**; PhD Nonmember **$290**; all non-member fees include one year of membership; "Click to submit or resubmit a paper" leads to the FMA payment form (fmai.memberclicks.net); editors seek a median turnaround of 6-8 weeks.
- **https://www.fma.org/financial-management-editorial-board** — **re-verified 2026-11-24.** Editors: Michael Goldstein (Babson College), Kathleen Kahle (Wake Forest University); 32 Associate Editors; Past Editors include Shawn Thomas, University of Pittsburgh, 2022-2025.
- **https://www.fma.org/financial-management-editorial-philosophy** — **re-verified 2026-11-24.** Desk rejection: the journal refunds all but **$100** of the submission fee (FMA membership fee nonrefundable); editors "may, in some situations, seek a second reviewer"; AI usage: authors follow Wiley's guidelines on generative-AI tools, and manuscripts under review must not be uploaded to AI technologies; Data and Code Sharing Policy (initial submissions after 1 March 2023): after acceptance authors are *encouraged* to provide programs (and data or pseudo-data) for the Financial Management Dataverse.
- **https://www.fma.org/assets/docs/FM/fmwriterstoolkit.pdf** — FM Author Toolkit (**re-read 2026-11-24**): after the FMA payment process the author is directed to **Wiley ScholarOne** for the upload; gives no abstract word limit and no blinding rule.

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: corporate finance, investments, market institutions, and applied financial decision-making | Official journal home / author instructions |
| Publisher / owner: Wiley for the Financial Management Association | Official journal home |
| Submission route: Wiley online submission | Author instructions or submission portal |
| Sibling boundary: Journal of Corporate Finance, Journal of Banking and Finance, JFQA, and Review of Financial Studies | Inferred from journal scope and local repository taxonomy |
| corporate policy | Official pages above; re-check live before submission |
| capital structure | Official pages above; re-check live before submission |
| payout and investment | Official pages above; re-check live before submission |
| governance channel | Official pages above; re-check live before submission |

## Verified on official pages (2026-06; editors, fee and policies re-verified 2026-11-24)

- **Editors (re-verified 2026-11-24): Michael Goldstein (Babson College) and Kathleen Kahle (Wake Forest University).** Shawn Thomas (University of Pittsburgh) is listed among past editors (2022-2025); the 2026-06-22 three-editor slate and Kahle's Arizona affiliation are superseded. Published by **Wiley** for the **Financial Management Association (FMA)**. (fma.org editorial-board and journal pages)
- **Submission fee (re-verified 2026-11-24 on fma.org/financial-management-submissions):** **$250** for FMA members (Professional or PhD), **$350** for Professional non-members, **$290** for PhD non-members (was $280 on 2026-06-22); the **$350 / $290 non-member fees include one year of FMA membership** for the submitting author. Desk-rejected submissions are refunded all but $100 (editorial-philosophy page). Confirm before submitting. Source: https://www.fma.org/financial-management-submissions ; https://onlinelibrary.wiley.com/page/journal/1755053x/homepage/forauthors.html

## Unverified / volatile items

- **OA APC, word limits, abstract limits, keywords/JEL, and blinding rules** remain **待核实**: none is stated on the fma.org pages or the FM Author Toolkit as of 2026-11-24, and the Wiley For Authors page (https://onlinelibrary.wiley.com/page/journal/1755053x/homepage/forauthors.html) returned HTTP 403 to curl and WebFetch on 2026-11-24; a WebSearch restricted to onlinelibrary.wiley.com and fma.org did not surface FM's own guideline text. Confirm at submission time. (Submission fee, editors, data/code and AI policies are verified above.)
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Financial Management",
  "verified": "2026-11-24",
  "rules": {
    "submission_fee": {"value": "USD 250 FMA member (Professional or PhD) / 350 Professional nonmember / 290 PhD nonmember; nonmember fees include one year of FMA membership; all but USD 100 refunded on desk rejection", "source": "https://www.fma.org/financial-management-submissions"},
    "portal": {"value": "FMA submission/payment form on fma.org, then Wiley ScholarOne for the manuscript upload", "source": "https://www.fma.org/assets/docs/FM/fmwriterstoolkit.pdf"},
    "data_code_policy": {"value": "after acceptance authors are encouraged (not required) to provide replication programs and data or pseudo-data for the Financial Management Dataverse; applies to initial submissions after 1 March 2023", "source": "https://www.fma.org/financial-management-editorial-philosophy"},
    "llm_policy": {"value": "authors follow Wiley's guidelines on generative-AI tools; manuscripts under review must not be uploaded to AI technologies by reviewers or editors", "source": "https://www.fma.org/financial-management-editorial-philosophy"},
    "review_mode": {"value": null, "note": "not stated on the fma.org pages or the FM Author Toolkit as of 2026-11-24; Wiley For Authors page unreachable (HTTP 403)"},
    "abstract_words_max": {"value": null, "note": "not stated on the fma.org pages or the FM Author Toolkit as of 2026-11-24; Wiley For Authors page unreachable (HTTP 403)"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages read as of 2026-11-24"},
    "keywords_required": {"value": null, "note": "not stated on the official pages read as of 2026-11-24 (the Author Toolkit gives keyword advice only)"}
  }
}
```
