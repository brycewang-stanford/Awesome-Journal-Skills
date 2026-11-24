# Human Resource Management Official Source Map

Primary source map for facts used in the HRM skill pack. **Access date: 2026-06.** Length and abstract limits, review mode, required statements, portal, reference style and the co-editors were **re-verified 2026-11-24**. Wiley Online Library answers automated clients with HTTP 403 from this environment (both curl and WebFetch), so the author-guidelines and editorial-board pages were **read via search-engine rendering restricted to onlinelibrary.wiley.com** on 2026-11-24 and corroborated against the Internet Archive snapshot of the author guidelines dated 2024-09-26. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://onlinelibrary.wiley.com/journal/1099050x** — official page used to verify or re-check HRM scope, submission, policy, or author guidance. Access date: 2026-06 (HTTP 403 to automated access on 2026-11-24).
- **https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html** — official page used to verify or re-check HRM scope, submission, policy, or author guidance. Access date: 2026-06; re-read 2026-11-24 via search-engine rendering (live page returns HTTP 403).

## Sources re-read 2026-11-24

| URL | Access method | What it verifies |
|-----|---------------|------------------|
| https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html | search-engine rendering (onlinelibrary.wiley.com only) + Internet Archive snapshot 2024-09-26 | Original Articles approx. **10,000–12,000 words, not including references, tables, figures, and appendices** (the 2024 archive still said "approximately 10,000 words or 35 pages"); **unstructured abstract, 200-word maximum**; required **Data Availability Statement** and **IRB statement**; data transparency table as an additional file when the dataset appears in other studies; **double-blind** review (Editor-in-Chief screens before review); **APA** reference style; new submissions via the **Wiley Research Exchange** portal (authors.wiley.com/journal/HRM); ORCID required; AI tools cannot be authors and any use is described in the Methods or Acknowledgements; preprints considered |
| https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/editorialboard.html | search-engine rendering | Co-Editors-in-Chief Fang Lee Cooke (Monash University) and Shaun Pichler (California State University-Fullerton) |

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: human resource management, talent, compensation, employment systems, workforce analytics, and HR strategy | Official journal home / author instructions |
| Publisher / owner: Wiley | Official journal home |
| Submission route: Wiley online submission | Author instructions or submission portal |
| Sibling boundary: Personnel Psychology, Journal of Management, Human Relations, and Academy of Management Journal | Inferred from journal scope and local repository taxonomy |
| HR system | Official pages above; re-check live before submission |
| talent architecture | Official pages above; re-check live before submission |
| employment relation | Official pages above; re-check live before submission |
| workforce analytics | Official pages above; re-check live before submission |

## Verified on official pages (re-verified 2026-11-24)

- **Co-Editors-in-Chief (Wiley *Human Resource Management*, ISSN 1099-050X): Fang Lee Cooke (Monash University) and Shaun Pichler (California State University, Fullerton; co-EiC from Jan 2025).** Published by **Wiley**. First verified 2026-06-22 and re-verified 2026-11-24 via the Wiley editorial-board page (search-engine rendering). Corrects a prior STALE listing (Cronin/Guthrie/Piening/Snell), which no longer matches the masthead. The author-guidelines text still names Howard Klein as a co-editor in one passage; the editorial-board page is treated as authoritative. Re-verify before submission.
- **Length:** Original Articles approximately 10,000–12,000 words, **excluding** references, tables, figures and appendices.
- **Abstract:** unstructured, at most 200 words.
- **Review:** double-blind; anonymized main file plus a separate title page; the Editor-in-Chief decides whether a paper goes to review.
- **Required statements:** a Data Availability Statement and an IRB statement (ethical treatment of participants and informed consent, as appropriate); a data transparency table as an additional file when the dataset has been used in other studies.
- **Portal:** Wiley **Research Exchange** (authors.wiley.com/journal/HRM). **STALE-FIX (2026-11-24):** earlier versions of this pack said ScholarOne / Manuscript Central.
- **References:** APA style. **ORCID** required. **AI:** cannot be listed as an author; any use is described in the Methods or Acknowledgements.
- **Preprints:** considered for review; posting may compromise anonymity.

## Unverified / volatile items

- **OA APC amount** (hybrid; APC applies only if OA is chosen after acceptance) — **待核实**; Wiley pages unreachable live on 2026-11-24.
- Keyword count and article-type list beyond Original Articles — **待核实**.
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Human Resource Management",
  "verified": "2026-11-24",
  "rules": {
    "main_text_words_max": {"value": 12000, "soft": true, "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html", "note": "Original Articles approx. 10,000-12,000 words, not including references, tables, figures and appendices; read via search-engine rendering (live page returns 403)"},
    "abstract_words_max": {"value": 200, "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "abstract_format": {"value": "unstructured", "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "review_mode": {"value": "double-blind", "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html", "note": "separate title page; Editor-in-Chief screens before review"},
    "required_statements": {"value": ["data_availability"], "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "conditional_statements": {"value": ["ethics_approval", "informed_consent", "ai_use_disclosure"], "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html", "note": "IRB statement for human-participant research (approval, ethical treatment, consent as appropriate); AI use described in Methods or Acknowledgements if used"},
    "reference_style": {"value": "APA", "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "portal": {"value": "Wiley Research Exchange: authors.wiley.com/journal/HRM", "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "preprint_policy": {"value": "preprints considered for review; posting may compromise anonymity", "source": "https://onlinelibrary.wiley.com/page/journal/1099050x/homepage/forauthors.html"},
    "apc": {"value": null, "note": "hybrid OA APC amount not readable as of 2026-11-24"}
  }
}
```
