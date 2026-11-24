# Perspectives on Psychological Science — Official Source Map

Primary source map for facts used in the `ppsych-*` skill pack. **Access date: 2026-06.** Contribution
types, abstract and length rules, proposal rules, data/cover-letter rule, reviewer suggestions, portal,
AI policy and the Editor-in-Chief **re-verified 2026-11-24** against the live APS pages (submission
guidelines, editorial-board page, APS editorial policies), read directly with `curl`; the SAGE
author-instructions and journal pages still return a Cloudflare challenge and could not be read.
**Change found on 2026-11-24:** the APS submission-guidelines page **no longer mentions** the
Research Transparency Statement or the 2024 discontinuation of Open-Practice badges for PoPS, so those
two facts are moved to the unverified list below. Re-check editor names, exact limits, portal forms, data/open-science policy, and style details before relying on them. Items not confirmed from an official page are marked **待核实** in the skills.

## Official pages

- **https://www.psychologicalscience.org/publications/perspectives** — APS journal home (scope, article types, editorial team). Access date: 2026-06.
- **https://www.psychologicalscience.org/publications/perspectives/pps-submissions** — APS Submission Guidelines for PoPS (contribution types, proposal rules, abstract limit, open data, suggested reviewers). Access date: 2026-06.
- **https://journals.sagepub.com/author-instructions/pps** — SAGE author instructions for PoPS (formatting, APA style, production). Access date: 2026-06.
- **https://journals.sagepub.com/home/pps** — SAGE journal home for PoPS. Access date: 2026-06.
- **http://mc.manuscriptcentral.com/pps** — Manuscript Central / ScholarOne submission portal. Access date: 2026-06 (still the portal named on the APS guidelines, 2026-11-24).
- **https://www.psychologicalscience.org/publications/perspectives/editorial-board** — APS editorial board (read 2026-11-24): **Editor-in-Chief Arturo E. Hernandez, University of Houston**.
- **https://www.psychologicalscience.org/publications/aps-editorial-policies** — APS editorial policies (read 2026-11-24): LLMs/generative AI may be used as productivity tools with human oversight; AI bots must not be listed as authors; reviewers must not use AI to write reviews.

**What the submission-guidelines page verifies (re-read 2026-11-24):** "All manuscripts must include an
abstract of **no more than 200 words**"; APA **7th edition** (only four heading levels); tables and
figures embedded; "In principle, there are **no strict page limitations** for stand-alone articles"
except **brief reports (1,000–1,500 words)** of outstanding young scientists' research; an initial
**proposal is required for cooperative and miscellaneous contributions** and optional for stand-alone
articles (positive feedback is not an invitation; all manuscripts get the same review); "When original
data are included in the submission, they should be available in a repository, and the author should
state in a **cover letter** that the data were collected in accordance with ethical guidelines";
authors must name **a minimum of five** objective reviewers (no mentors, colleagues, collaborators);
a submission with a history at another journal should include those reviews and the decision letter;
portal `mc.manuscriptcentral.com/pps`. The page does not state a review mode (masked or not).

## Facts used in the skills (verified 2026-06 where marked)

| Fact area | Status | Source |
|-----------|--------|--------|
| Publisher: SAGE in partnership with APS; bimonthly | verified | SAGE/APS journal home |
| Scope: broad integrative reviews, overviews of research programs, theoretical/metatheoretical statements, methodology + meta-science, philosophy-of-science, opinion, biographical/humor pieces | verified | APS submission guidelines |
| Out of scope: single empirical studies; routine meta-analyses (unless a distinct superordinate theoretical message) | verified | APS submission guidelines |
| Contribution categories: stand-alone (proposal optional) / cooperative (proposal required) / miscellaneous (proposal required) | verified | APS submission guidelines |
| Positive proposal feedback ≠ invitation; identical review for all manuscripts | verified | APS submission guidelines |
| Abstract ≤ 200 words | verified | APS submission guidelines |
| No strict page limit for stand-alone; brief reports 1,000–1,500 words | verified | APS submission guidelines |
| Original data must be available in a repository; cover letter confirms ethical data collection | verified | APS submission guidelines |
| Suggest ≥5 objective reviewers (excluding mentors/colleagues/collaborators) | verified | APS submission guidelines |
| Submission portal: mc.manuscriptcentral.com/pps | verified | APS submission guidelines |
| Editor-in-Chief: Arturo E. Hernandez (University of Houston; from 2024-12-01) | re-verified 2026-11-24 on the APS editorial-board page (start date from the 2026-06-22 check); 以官网为准 (volatile) | APS editorial-board page / EiC editorial |
| APA reference/statistics/exhibit style | **APA 7th edition** (section order, headings/subheadings per APA 7) — verified 2026-06 | APS/SAGE submission guidelines |
| Open-Practice badges for PoPS | Recorded 2026-06 as **discontinued for submissions on/after 2024-01-01** and replaced by required open data/materials and a **Research Transparency Statement** — **待核实 (2026-11-24):** the current PoPS guidelines page no longer says this; it only asks that original data be in a repository | APS submission guidelines (psychologicalscience.org/publications/perspectives/pps-submissions) |
| Sibling boundary: Psychological Science, Psychological Bulletin, Annual Review of Psychology, Current Directions in Psychological Science | inferred from scope + APS journal portfolio | APS journal portfolio |

## Unverified / volatile items

- **Current editor names and board composition** are volatile; re-confirm the EiC and handling-editor structure on the editorial-team page at submission time.
- **Manuscript style is APA 7th edition** (verified 2026-06); the exact figure/color specs and any minor SAGE house deviations remain 待核实 — confirm on the SAGE author instructions.
- **Open-Practice badges / Research Transparency Statement at PoPS** — recorded on 2026-06 from the PoPS guidelines, but **not on the PoPS guidelines page re-read 2026-11-24** (it now says only that original data "should be available in a repository"). The 2024 badge-to-RTS change is still documented for *Psychological Science*; whether it applies to PoPS is 待核实. Tried: the APS PoPS guidelines and editorial-board pages (direct `curl`), the SAGE author instructions (Cloudflare challenge), and a site-restricted web search of psychologicalscience.org (no PoPS-specific hit). The exact **TOP level** is also 待核实.
- **Review mode** (masked vs. unmasked) — not stated on the APS PoPS guidelines page (2026-11-24); SAGE page unreachable. 待核实.
- **Exemplar articles** must be verified in the official archive or DOI page before being cited as real examples (see `exemplars/library.md`).

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Perspectives on Psychological Science",
  "verified": "2026-11-24",
  "rules": {
    "abstract_words_max": {"value": 200, "source": "https://www.psychologicalscience.org/publications/perspectives/pps-submissions"},
    "main_text_words_max": {"value": null, "note": "no strict page limitations for stand-alone articles (official page, 2026-11-24); brief reports of outstanding young scientists' research are 1,000-1,500 words"},
    "review_mode": {"value": null, "note": "not stated on the official pages as of 2026-11-24 (SAGE author instructions unreachable)"},
    "cover_letter": {"value": null, "note": "not stated as a general requirement; only when original data are included must the cover letter confirm ethical data collection, and submissions with a history at another journal should include the prior reviews and decision letter (official page, 2026-11-24)"},
    "conditional_statements": {"value": ["data_availability", "ethics_approval"], "source": "https://www.psychologicalscience.org/publications/perspectives/pps-submissions", "note": "only when original data are included: data available in a repository, ethics confirmation in the cover letter. Cooperative and miscellaneous contributions require an initial proposal"},
    "reference_style": {"value": "APA Publication Manual, 7th edition (four heading levels); tables and figures embedded", "source": "https://www.psychologicalscience.org/publications/perspectives/pps-submissions"},
    "portal": {"value": "http://mc.manuscriptcentral.com/pps", "source": "https://www.psychologicalscience.org/publications/perspectives/pps-submissions"},
    "llm_policy": {"value": "LLMs/generative AI may be used as productivity tools with human oversight; AI bots must not be listed as authors", "source": "https://www.psychologicalscience.org/publications/aps-editorial-policies"},
    "submission_fee": {"value": null, "note": "not stated on the official pages as of 2026-11-24"}
  }
}
```
