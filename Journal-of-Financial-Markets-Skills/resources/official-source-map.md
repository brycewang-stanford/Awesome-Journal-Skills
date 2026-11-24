# Journal of Financial Markets Official Source Map

Primary source map for facts used in the JFM skill pack. **Access date: 2026-06.** Masthead, APC and submission route **re-verified 2026-11-24**. Access method: the live ScienceDirect pages return HTTP 403 (Cloudflare) to curl, WebFetch and a reader proxy, so the journal home was read via an **Internet Archive capture dated 2026-10-17** and the Guide for Authors via search-engine rendering restricted to sciencedirect.com / elsevier.com (no Internet Archive capture of the Guide newer than January 2024). **Changes found on 2026-11-24:** the journal home names **Paolo Pasquariello (University of Michigan) as Managing Editor** — the Lehmann / Seppi / Subrahmanyam slate below came from aggregator listings (RePEc, Research.com) and is stale; the open-access **APC is USD 3,230** (was USD 3,040). Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://www.sciencedirect.com/journal/journal-of-financial-markets** — official page used to verify or re-check JFM scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://www.elsevier.com/journals/journal-of-financial-markets/1386-4181/guide-for-authors** — official page used to verify or re-check JFM scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://web.archive.org/web/20261017113912/https://www.sciencedirect.com/journal/journal-of-financial-markets** — Internet Archive capture (2026-10-17) of the official home, read 2026-11-24: Managing Editor **Paolo Pasquariello, PhD, University of Michigan**; APC **USD 3,230** excluding taxes; subscription route has no publication fee; 3 days submission to first decision, 63 days to decision after review; "Submit your article" links to https://submit.elsevier.com/JFM.
- **https://www.sciencedirect.com/journal/journal-of-financial-markets/publish/guide-for-authors** — Guide for Authors (live page HTTP 403 on 2026-11-24). A search-engine rendering on 2026-11-24 quotes "a submission fee of US$ 275 for new submissions" with half refunded on a desk rejection, double-anonymized review, a 250-word abstract and mandatory Highlights, but the search tool dated the indexed copy to roughly 2023, so none of these is treated as verified (see UNVERIFIED below).

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: market microstructure, asset pricing, liquidity, trading, and financial-market design | Official journal home / author instructions |
| Publisher / owner: Elsevier | Official journal home |
| Submission route: Editorial Manager / Elsevier submission | Author instructions or submission portal |
| Sibling boundary: Journal of Finance, Journal of Financial Economics, Review of Financial Studies, and Management Science | Inferred from journal scope and local repository taxonomy |
| microstructure mechanism | Official pages above; re-check live before submission |
| liquidity measurement | Official pages above; re-check live before submission |
| trading venue design | Official pages above; re-check live before submission |
| price discovery | Official pages above; re-check live before submission |

## Verified on official pages (2026-06; re-verified 2026-06-22; masthead and APC re-verified 2026-11-24)

- **Managing Editor (re-verified 2026-11-24): Paolo Pasquariello (University of Michigan)**, per the official journal home (Internet Archive capture of 2026-10-17); his University of Michigan CV (https://www.bus.umich.edu/FacultyBios/CV/ppasquar.pdf, corroboration only) gives Managing Editor 2022-present. **Superseded:** the 2026-06-22 entry "Editors: Bruce N. Lehmann, Duane J. Seppi, and Avanidhar Subrahmanyam" relied on RePEc / Research.com aggregator fields, which are out of date. Published by **Elsevier**.
- **Submission fee: US$170** for original and revised submissions; the manuscript is only considered after the fee is paid. Source: Elsevier JFM Guide for Authors, via WebSearch snippets 2026-06-22 (>=2 corroborating results). **Not re-confirmed on 2026-11-24** — see UNVERIFIED (a rendering of the guide quotes US$275). Re-confirm on the live guide before submitting.
- **Open-access APC: USD 3,230 excluding taxes** (subscription route has no APC). Source: official JFM home, Internet Archive capture of 2026-10-17, read 2026-11-24 (was USD 3,040 per a 2026-06-22 search snippet).

## Unverified / volatile items

- Exact **word limits, abstract limits, JEL/structured-abstract, and blinding rules** remain **待核实**: on 2026-11-24 the live Guide returned HTTP 403, no Internet Archive capture newer than 2024-01-21 exists, and the search-engine rendering (double-anonymized review, 250-word abstract, mandatory Highlights) was dated by the search tool to roughly 2023 — confirm at submission time.
- **Submission fee amount 待核实:** US$170 (2026-06-22 snippets, original and revised submissions) vs **US$275 for new submissions, half refunded on desk rejection** (2026-11-24 rendering of the official Guide, index date uncertain). The pack keeps both figures visible until the live guide can be read.
- Associate-editor / co-editor roster: not re-read on 2026-11-24 (editorial-board page HTTP 403; no archive capture).
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Financial Markets",
  "verified": "2026-11-24",
  "rules": {
    "apc": {"value": "optional open access: USD 3,230 excluding taxes; no publication fee on the subscription route", "source": "https://web.archive.org/web/20261017113912/https://www.sciencedirect.com/journal/journal-of-financial-markets", "note": "Internet Archive capture of the official journal home, 2026-10-17"},
    "portal": {"value": "Elsevier submission system via the journal's 'Submit your article' link (https://submit.elsevier.com/JFM)", "source": "https://web.archive.org/web/20261017113912/https://www.sciencedirect.com/journal/journal-of-financial-markets"},
    "submission_fee": {"value": null, "note": "a fee applies, but the amount is unconfirmed as of 2026-11-24 (US$170 in 2026-06 snippets vs US$275 in an older-dated rendering of the guide)"},
    "review_mode": {"value": null, "note": "not verifiable on the official pages as of 2026-11-24 (live guide HTTP 403; only a ~2023-dated rendering says double-anonymized)"},
    "abstract_words_max": {"value": null, "note": "not verifiable on the official pages as of 2026-11-24"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages read as of 2026-11-24"}
  }
}
```
