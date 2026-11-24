# JBES Official Source Map

Primary and authoritative sources behind the JBES-specific facts injected into this
skill pack. **Policy refresh date: 2026-06-20; editor/fee live-check 2026-06-22; editors and ASA data policy re-verified 2026-11-24 (T&F submission rules still unreachable).**
Taylor & Francis pages are the canonical source for JBES, but the T&F journal and
author-instruction pages did not render directly in this environment during this
refresh. Official T&F search-index snippets were used only for scope, Open Select
status, and the current editorial board. Submission-only details that require the
live author-instruction page are not hard-coded here.

**Live-check 2026-06-22:** Joint Editors **Yingying Fan** (USC), **Michael Kolesár**
(Princeton), and **Dacheng Xiu** (Chicago) re-confirmed as current via the T&F journal
"about" page snippets. JBES is **hybrid Open Select** (OA optional, no APC if you
publish non-OA). A single T&F search snippet this session quoted an Open Select APC of
**~USD 2,500**, but that figure could **not** be re-confirmed on a second authoritative
source or a live-rendered T&F page — treat it as **unconfirmed** and have authors read
the exact APC off the live T&F author-instruction / open-access cost-finder page rather
than budgeting from this number.

**Re-check 2026-11-24:** every tandfonline.com page (journal home, about-this-journal, author
instructions) and the ScholarOne host returned HTTP 403 to curl and WebFetch, and the Internet Archive
holds no usable capture of the JBES author instructions; search-engine queries restricted to
tandfonline.com / amstat.org did not surface the instructions text either. The submission-only details
below therefore **remain unencoded**. What was re-verified 2026-11-24: the Joint Editors **Yingying Fan,
Michael Kolesár and Dacheng Xiu** and the hybrid **Open Select** status, via search-engine rendering of
the T&F about-this-journal page (no change); and the **ASA data-sharing policy page**, re-read directly
(unchanged: ASA strongly encourages data and code as supplementary material; editors may set
journal-level policies; waivers for confidentiality or security; authors encouraged to cite data and
include a data availability statement).

## Official journal / society pages

- **https://www.tandfonline.com/journals/ubes20** — JBES homepage on Taylor &
  Francis Online. Official search snippets verify: journal title; Taylor & Francis
  Open Select / hybrid open-access status; high-level aims and scope.
- **https://www.tandfonline.com/journals/ubes20/about-this-journal** — T&F
  "About this journal" page. Official search snippets verify current editorial
  board names and the hybrid Open Select program.
- **https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ubes20**
  — T&F author-instruction entry point for JBES. This remains the live source that
  must be opened before submission-ready advice on platform, file requirements,
  abstract/page limits, review model, citation style, and fee/APC specifics.
- **https://www.amstat.org/publications/q-and-as/asa-journal-policies-on-data-sharing-and-reproducibility**
  — ASA journal policies on data sharing and reproducibility (re-read directly 2026-11-24). Directly verifies
  the ASA-wide policy for ASA-owned journals published with Taylor & Francis.
- **https://as.vanderbilt.edu/economics/atsushi-inoue-appointed-co-editor-of-prestigious-journal/**
  — Vanderbilt announcement verifying the 2022-2024 JBES Co-Editor term held by
  Atsushi Inoue and Ivan Canay, useful as a historical note on the rotating
  Co-Editor model.

## Checked facts

| Fact used in skills | Source |
| --- | --- |
| Published by Taylor & Francis on behalf of the **American Statistical Association (ASA)** | T&F journal page; ASA context |
| Scope = high-quality methodological contributions oriented toward applications in microeconomics, macroeconomics, business, and finance | T&F official search snippet |
| Innovations include developing/improving statistical methods, adapting methods from other fields including **machine learning and data science**, and computational improvements | T&F official search snippet |
| Theoretical contributions should have clear empirical relevance; JBES articles often include a substantive empirical application | T&F official search snippet |
| Hybrid open-access / **Open Select** status | T&F official search snippet |
| Current Joint Editors: **Yingying Fan** (USC), **Michael Kolesár** (Princeton), and **Dacheng Xiu** (Chicago) | T&F official search snippet |
| ASA strongly encourages authors to include data sets and code as supplementary material demonstrating final-article results | ASA policy |
| ASA encourages underlying data to be publicly available when privacy/confidentiality constraints allow | ASA policy |
| ASA encourages citing referenced datasets in the reference list and including a data availability statement | ASA policy |
| ASA journal editors may set journal-specific policies under the broad ASA principle; waiver requests are possible for confidentiality or security reasons | ASA policy |
| Historical JBES Co-Editor model: Atsushi Inoue and Ivan Canay held the 2022-2024 term | Vanderbilt announcement |
| JBES does not use the Journal of Applied Econometrics Data Archive; that archive belongs to a separate Wiley journal | Cross-journal negative check |

## Submission-only details not encoded

Do not hard-code the following for JBES until the live T&F author-instruction page
has been opened in a normal browser session (still UNVERIFIED / 待核实 after the 2026-11-24 re-check:
HTTP 403 on tandfonline.com and mc.manuscriptcentral.com, no archive capture, no search rendering):

- submission platform;
- submission fee, if any, and exact open-access APC;
- manuscript length, page, or abstract limits;
- peer-review anonymity model and expected timeline;
- required reference style or template;
- whether JBES adds stricter code/data enforcement beyond the ASA-wide policy.

## Operational notes for this pack

- Keep the core JBES identity firm: methods-with-empirics, ASA-owned, T&F-published,
  hybrid Open Select, rotating Joint Editors, and strong reproducibility norms.
- For submission advice, route users to the live T&F author instructions before
  asserting platform, length, review model, fees, or formatting requirements.
- Treat data/code sharing as an ASA expectation: prepare a reproducible supplement
  and a data availability statement, while documenting any confidentiality or
  security constraints.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Journal of Business & Economic Statistics",
  "verified": "2026-11-24",
  "rules": {
    "data_code_policy": {"value": "ASA policy: data sets and code demonstrating the final results strongly encouraged as supplementary material; data availability statement and data citations encouraged; waivers for confidentiality or security", "source": "https://www.amstat.org/publications/q-and-as/asa-journal-policies-on-data-sharing-and-reproducibility", "note": "ASA-wide; JBES-specific enforcement not confirmed"},
    "main_text_pages_max": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24 (T&F author instructions unreachable)"},
    "abstract_words_max": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24 (T&F author instructions unreachable)"},
    "review_mode": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24 (T&F author instructions unreachable)"},
    "keywords_required": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24"},
    "jel_codes_required": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24"},
    "submission_fee": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24"},
    "portal": {"value": null, "note": "not confirmed on the official pages as of 2026-11-24"}
  }
}
```
