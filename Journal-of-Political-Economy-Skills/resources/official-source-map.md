# Official Source Map — Journal of Political Economy (JPE)

Sources used to verify the JPE-specific facts injected into this skill pack.
Access date for all entries: **2026-05-30**. Submission rules, fee, review model, portal, data
policy and masthead **re-verified 2026-11-23**: `journals.uchicago.edu` still returns HTTP 403 to
direct fetches (WebFetch and curl), so the University of Chicago Press pages were read via
search-engine rendering of the exact official pages (instructions, data policy, issue mastheads);
the JPE Data Editor policy page was fetched directly. One correction: the submission portal is
**Editorial Manager** (editorialmanager.com/jpolec), not Editorial Express — the pack has been fixed.

Note on access: at access time the University of Chicago Press / Atypon site
(`journals.uchicago.edu`) returned HTTP 403 behind a Cloudflare bot challenge and
could not be machine-fetched directly. The facts below were confirmed via web
search result snippets that quote those official pages, plus open authoritative
mirrors (Wikipedia, RePEc/IDEAS, the Crossref REST API, the JPE Data Editor
site, and the Social Science Data Editors / DCAS site). Where only the gated
official page can confirm a precise current figure (e.g., exact word/abstract
limits), the skills say "verify on the official page" rather than inventing it.

## Primary / official (University of Chicago Press, gated at access time)

- <https://www.journals.uchicago.edu/journals/jpe/about> — JPE homepage, aims/scope, history (HTTP 403 at access time; quoted via search).
- <https://www.journals.uchicago.edu/journals/jpe/instruct> — Instructions for Authors: Chicago author-date references, PDF/Word/LaTeX formats, manuscript preparation, the $250/$125 submission fee, single-blind review (gated; quoted via search). **Re-verified 2026-11-23 via search rendering:** "Manuscripts should be submitted via the JPE Editorial Manager (EM) site"; "Manuscripts must be in English and must begin with a title page that includes the names, e-mail addresses, and affiliations of all authors"; PDF preferred (EM also accepts Word and LaTeX); $250 nonsubscriber / $125 individual-subscriber fee, non-refundable even on desk rejection, decisions not released until paid or waived; waiver for 3 or more JPE referee reports in the prior 12 months; "The Journal of Political Economy uses a single-blind system of peer review." No abstract or length limit surfaced. (An archived 2025-07-25 Wayback copy of the page, read only as a cross-check, carries the same wording.)
- <https://www.journals.uchicago.edu/journals/jpe/board> — editorial board: lead editor Esteban Rossi-Hansberg (University of Chicago) plus co-editors (gated; quoted via search). Re-verified **2026-06-22**: Rossi-Hansberg became an Editor in 2021 and Lead Editor in 2024 and remains the sitting Lead Editor (confirmed via uchicago board-page and CV/CEPR/AmAcad search snippets). **Re-verified 2026-11-23** via search rendering of the JPE journal pages and a recent issue masthead: Lead Editor Esteban Rossi-Hansberg; Editors John Asker, Andrew Atkeson, Leonardo Bursztyn, Gabriel Carroll, Melissa Dell, David Lagakos, Guido Lorenzoni, Francesca Molinari, Luigi Pistaferri, Nicholas Ryan, Bruno Strulovici, Christopher Taber, Christopher Walters; Managing Editor Connie Fritsche. Co-editor roster rotates — re-check the board page before naming a handling editor.
- <https://www.journals.uchicago.edu/journals/jpe/datapolicy> — JPE data policy: publishes only if data/code documented and available; endorses DCAS v1.0; deposit to the JPE Dataverse; exemption requested at first submission; 5-year preservation for exempted data; license allowing unrestricted access for replication (gated; quoted via search).
- <https://www.editorialmanager.com/jpolec/> — JPE submission system: **Editorial Manager (EM)** (re-verified 2026-11-23 against the Instructions for Authors wording quoted above; "Editorial Express" was an error).
- <https://www.journals.uchicago.edu/journals/jpemi/pr/220517> — 2022 launch announcement of JPE Microeconomics (lead editor John List); first issue March 2023.
- <https://www.journals.uchicago.edu/journals/jpema/pr/220517> — 2022 launch announcement of JPE Macroeconomics (lead editor Greg Kaplan); first issue March 2023. **Re-verified 2026-11-23** (search rendering of the 2026 JPE Micro and JPE Macro issue pages): John List and Greg Kaplan remain the lead editors; each companion charges its own $100 submission fee.
- <https://economics.uchicago.edu/news/journal-of-political-economy-updates-and-announcements-2022> — University of Chicago Dept. of Economics announcement of the JPE Micro / JPE Macro companions and their Chicago lead editors.

## Submission fee and review model (quoted from the Instructions for Authors via search)

- $250 submission fee for nonsubscribers; $125 for individual JPE subscribers; non-refundable even if desk-rejected; waiver for authors who completed 3+ JPE referee reports in the prior 12 months. Source: JPE Instructions for Authors (<https://www.journals.uchicago.edu/journals/jpe/instruct>), quoted in search results 2026-05-30; **fee re-confirmed 2026-06-22** via the same Instructions page search snippets (the $250/$125 split and the 3-report waiver are unchanged).
- Review model: single-blind (referees see authors). Same source.

## JPE Data Editor (open)

- <https://jpedataeditor.github.io/> — JPE runs its own Data Editor who checks reproducibility at conditional accept before deposit to the JPE Dataverse (distinct from the AEA Data Editor).
- <https://jpedataeditor.github.io/policy> — JPE Data and Code Policy, Version 1 (dated October 17, 2026), fetched directly **2026-11-23**. Verifies: DCAS v1.0 endorsement; conditionally accepted papers provide data, programs and computation details before publication and must pass reproducibility checks; deposit to the JPE Dataverse; exemption requests must be stated clearly at first submission and are not considered later; exempted data and code preserved for no less than five years after publication; license allowing unrestricted access for replication.

## Data and Code Availability Standard (open)

- <https://social-science-data-editors.github.io/> — DCAS v1.0 and the README template that JPE's policy is compatible with.
- <https://datacodestandard.org/> — the Data and Code Availability Standard endorsed by JPE and other leading journals.

## Open authoritative mirrors actually machine-read

- <https://en.wikipedia.org/wiki/Journal_of_Political_Economy> — founded 1892 by James Laurence Laughlin; published by University of Chicago Press for the UChicago Dept. of Economics and Booth School of Business; monthly (quarterly 1892–1905, ten/yr 1906–1921, bimonthly 1922–2019); editor-in-chief Esteban Rossi-Hansberg (University of Chicago); ISSN 0022-3808 (print) / 1537-534X (web); 2023 establishment of JPE Micro and JPE Macro.
- <https://ideas.repec.org/s/ucp/jpolec.html> — publisher University of Chicago Press; ISSN 0022-3808.
- <https://api.crossref.org/journals/0022-3808> — canonical title "Journal of Political Economy"; publisher "The University of Chicago Press"; ISSN 0022-3808 / 1537-534X.
- <https://api.crossref.org/journals/0022-3808/works> — bibliographic data for landmark JPE papers cited in the skills: Becker, "Crime and Punishment: An Economic Approach," JPE vol. 76, 1968, pp. 169–217; Stigler, "The Economics of Information," JPE vol. 69, 1961, pp. 213–225; Black & Scholes, "The Pricing of Options and Corporate Liabilities," JPE vol. 81, 1973, pp. 637–654. (Note: Becker's "A Theory of the Allocation of Time" is in *The Economic Journal* 75(299):493–517, 1965 — not JPE — and was removed here after web verification on 2026-06-07.)

## Not verified

- Exact abstract word limit and main-text length/word limits: only the gated official Instructions for Authors page is authoritative; not confirmed here. (2026-11-23: search renderings of the instructions surfaced no limit; a third-party guide's "250 words" contradicts itself and is not used.)
- JEL-code / keyword requirements and any AI/LLM-use policy: not surfaced from the official pages on 2026-11-23.
- Current acceptance rate: JPE does not publish an official figure (confirmed by multiple secondary sources that it is not disclosed).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Political Economy",
  "verified": "2026-11-23",
  "rules": {
    "review_mode": {"value": "single-blind", "source": "https://www.journals.uchicago.edu/journals/jpe/instruct", "note": "read via search-engine rendering (site returns 403 to direct fetches); manuscript must begin with a title page naming all authors"},
    "submission_fee": {"value": "USD 250 nonsubscribers / USD 125 individual JPE subscribers; non-refundable; waiver for 3+ JPE referee reports in the prior 12 months", "source": "https://www.journals.uchicago.edu/journals/jpe/instruct"},
    "portal": {"value": "Editorial Manager (editorialmanager.com/jpolec)", "source": "https://www.journals.uchicago.edu/journals/jpe/instruct"},
    "language": {"value": "English", "source": "https://www.journals.uchicago.edu/journals/jpe/instruct"},
    "file_format": {"value": "PDF preferred; Editorial Manager also accepts Word and LaTeX; title page with names, e-mail addresses and affiliations of all authors", "source": "https://www.journals.uchicago.edu/journals/jpe/instruct"},
    "data_code_policy": {"value": "JPE Data and Code Policy (DCAS v1.0): data, programs and computation details before publication; JPE Data Editor reproducibility check; JPE Dataverse deposit; exemptions only if requested at first submission", "source": "https://jpedataeditor.github.io/policy"},
    "abstract_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-23"},
    "main_text_words_max": {"value": null, "note": "not stated on the official pages as of 2026-11-23"},
    "jel_codes_required": {"value": null, "note": "not stated on the official pages as of 2026-11-23"},
    "llm_policy": {"value": null, "note": "not stated on the official pages as of 2026-11-23"}
  }
}
```
