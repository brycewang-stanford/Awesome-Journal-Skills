# Journal of International Money and Finance Official Source Map

Primary source map for facts used in the JIMF skill pack. **Access date: 2026-06.** Review model, abstract and Highlights rules, AI declaration and APC **re-verified 2026-11-24**. Access method: the live ScienceDirect pages return HTTP 403 (Cloudflare) to curl, WebFetch and a reader proxy, and the Internet Archive holds no Guide-for-Authors capture at all, so the Guide was read via **search-engine rendering restricted to sciencedirect.com / elsevier.com** (three queries); the journal home was read via its newest Internet Archive capture (2025-08-25); the Editorial Manager entry https://www.editorialmanager.com/jimf/ is reachable directly. Findings on 2026-11-24: **single anonymized** review (pays down the blinding 待核实); abstract ≤ **250** words; **Highlights required** (3 to **5** bullets, max **85** characters each); AI use declared in a section before the references; OA **APC USD 3,360** excluding taxes. **Masthead conflict:** the newest readable official home (2025-08-25) names **K.G. Koedijk** as Co-ordinating Editor, not the Aizenman / Chinn / Beirne / Park list below — editors moved to UNVERIFIED. Re-check editor names, fees, exact length limits, portal forms, data policies, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://www.sciencedirect.com/journal/journal-of-international-money-and-finance** — official page used to verify or re-check JIMF scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://www.elsevier.com/journals/journal-of-international-money-and-finance/0261-5606/guide-for-authors** — official page used to verify or re-check JIMF scope, submission, policy, or author guidance. Access date: 2026-06.
- **https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/publish/guide-for-authors** — Guide for Authors (live page HTTP 403 on 2026-11-24; read via search-engine rendering): "This journal follows a single anonymized review process", suitable papers typically sent to at least two reviewers; abstract that does not exceed 250 words; Highlights consisting of 3 to 5 bullet points, each a maximum of 85 characters including spaces, required at submission; AI-use declaration in a new section before the references.
- **https://web.archive.org/web/20250825022911/https://www.sciencedirect.com/journal/journal-of-international-money-and-finance** — newest Internet Archive capture of the official home (2025-08-25): Co-ordinating Editor **K.G. Koedijk** (Utrecht University and CEPR); APC USD 3,360 excluding taxes; editorial policy: refereeing and handling will not exceed thirty (**30**) weeks; authors get a maximum of six months for a major revision and three months for a minor revision, after which a revision counts as a resubmission.
- **https://www.editorialmanager.com/jimf/** — Editorial Manager entry (reachable directly 2026-11-24).

## Facts used in the skills

| Fact area | Source |
|-----------|--------|
| Journal scope: international finance, exchange rates, global banking, capital flows, and open-economy macro-finance | Official journal home / author instructions |
| Publisher / owner: Elsevier | Official journal home |
| Submission route: Editorial Manager / Elsevier submission | Author instructions or submission portal |
| Sibling boundary: Journal of International Economics, Journal of Monetary Economics, JMCB, and Journal of Financial Economics | Inferred from journal scope and local repository taxonomy |
| exchange-rate pass-through | Official pages above; re-check live before submission |
| capital-flow shocks | Official pages above; re-check live before submission |
| global financial cycle | Official pages above; re-check live before submission |
| sovereign risk | Official pages above; re-check live before submission |

## Verified on official pages (2026-06-22; see the 2026-11-24 re-check in the header)

- **Editors (2026-06-22 entry, now UNVERIFIED — see below): Joshua Aizenman, Menzie D. Chinn, John Beirne, and Donghyun Park.** (Elsevier/ScienceDirect editorial-board listings and JIMF special-issue editor credits; accessed 2026-06-22.) **STALE-FIX:** earlier IDEAS-RePEc and some aggregator caches still name **James R. Lothian (Fordham)** as editor — that listing is out of date (RePEc itself flags his editor email as no longer valid), so do not use it. Re-verify the sitting editors on the live Elsevier board before naming one in a cover letter.
  - https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/about/editorial-board
  - https://www.journals.elsevier.com/journal-of-international-money-and-finance/editorial-board/md-chinn
- Published by **Elsevier**; submit via Editorial Manager from the JIMF ScienceDirect page.
- **No society membership and no submission fee** for a standard paper; gold open access is optional at an APC of **USD 3,360** excluding taxes (official home, via search-engine rendering on 2026-11-24 and the 2025-08-25 archive capture). (Elsevier author guidance; accessed 2026-06-22.)

## Unverified / volatile items

- **Editors:** the Aizenman / Chinn / Beirne / Park list (2026-06-22) conflicts with the newest readable official home page (2025-08-25 capture: Co-ordinating Editor K.G. Koedijk); the editorial-board page returned HTTP 403 on 2026-11-24 and search-engine renderings of it were garbled. Do not name an editor until the live board is read.
- **"No submission fee" for regular papers:** not contradicted, but not positively re-confirmed on 2026-11-24 (one special-issue call does require a submission fee).
- **Main-text word/page limits and keyword counts:** not surfaced on 2026-11-24 — confirm at submission time. (APC, abstract limit and blinding rule are now verified above.)
- Exemplar articles must be verified in the official archive or DOI page before being cited as real examples.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of International Money and Finance",
  "verified": "2026-11-24",
  "rules": {
    "review_mode": {"value": "single-blind", "source": "https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/publish/guide-for-authors", "note": "'single anonymized review process'; read via search-engine rendering (live page HTTP 403)"},
    "abstract_words_max": {"value": 250, "source": "https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/publish/guide-for-authors"},
    "required_statements": {"value": ["highlights"], "source": "https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/publish/guide-for-authors", "note": "3 to 5 bullets, each at most 85 characters including spaces"},
    "conditional_statements": {"value": ["ai_use_disclosure"], "source": "https://www.sciencedirect.com/journal/journal-of-international-money-and-finance/publish/guide-for-authors", "note": "only if AI tools were used: statement in a new section before the references"},
    "apc": {"value": "optional open access: USD 3,360 excluding taxes", "source": "https://web.archive.org/web/20250825022911/https://www.sciencedirect.com/journal/journal-of-international-money-and-finance", "note": "same figure on the live home's search-engine rendering, 2026-11-24"},
    "portal": {"value": "Elsevier Editorial Manager (https://www.editorialmanager.com/jimf/)", "source": "https://www.editorialmanager.com/jimf/"},
    "keywords_max": {"value": null, "note": "not surfaced on the official pages as of 2026-11-24"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
