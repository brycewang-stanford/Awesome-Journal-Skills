# Cognitive Psychology Official Source Map

Primary source map for Cognitive Psychology-specific facts encoded in this pack.
Official pages were re-checked on **2026-06-21**. Review model, abstract/keyword/highlights rules, AI
declaration, APC and editor **re-verified 2026-11-24**. ScienceDirect returns a bot challenge (HTTP 403)
to `curl`, WebFetch and reader proxies, so the journal home page was read from its **Internet Archive
snapshot of 2026-10-17** (the newest available) and the Guide for Authors was **read via
search-engine rendering restricted to sciencedirect.com** (no post-2024 archive snapshot exists).
**Change found:** the APC rose from USD 3,460 to **USD 3,730** (excluding taxes), and the journal home
page carries a **"Call for Editor in Chief - Cognitive Psychology"** news item dated 8 September 2026.

## Official journal and author pages

| # | URL | What it verifies | Accessed |
|---|---|---|---|
| 1 | https://www.sciencedirect.com/journal/cognitive-psychology | Elsevier/ScienceDirect journal home; print ISSN 0010-0285, online ISSN 1095-5623; 2026 metrics visible on the page; APC USD 3,730 excluding taxes (re-verified 2026-11-24 via the 2026-10-17 archive snapshot; was USD 3,460 on 2026-06-21); no subscription publication fee; Impact Factor 2.8 and CiteScore 5.4 shown; news item "Call for Editor in Chief - Cognitive Psychology" (8 September 2026); Editor-in-Chief C.M. Rotello, University of Massachusetts Amherst; scope emphasizes longer, integrative, theory-impacting cognition articles and open-science readiness | 2026-06-21 |
| 2 | https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors | Guide for Authors; aims and scope; article types; single-anonymized review; minimum two reviewers for suitable submissions; abstract maximum 250 words; 1-7 keywords; highlights required; Editorial Manager submission; Elsevier Option B research-data policy; APA 7th references; generative-AI disclosure and image-use rules | 2026-06-21 |
| 3 | https://www.editorialmanager.com/cogpsych/ | Editorial Manager submission entry point linked from the ScienceDirect "Submit your article" action | 2026-06-21 |
| 4 | https://www.sciencedirect.com/journal/cognition | Sibling-journal guard: Cognition is a separate Elsevier journal and its article rules must not be imported into Cognitive Psychology | 2026-06-21 |

## Verified facts encoded in the pack

- **Publisher / identity:** Elsevier / ScienceDirect journal, print ISSN 0010-0285 and online ISSN 1095-5623. (#1)
- **Current Editor-in-Chief:** C.M. (Caren) Rotello, PhD, University of Massachusetts Amherst. (#1) (Still listed on the 2026-10-17 home-page snapshot; Elsevier posted a call for a new Editor-in-Chief on 8 September 2026, so a successor may be named — re-confirm before relying.)
- **Scope:** memory, attention, perception, language processing, categorization, thinking, reasoning, and cognition across development/aging. The journal specializes in longer, integrative articles with major theoretical impact. (#1, #2)
- **Article types:** original empirical, theoretical, tutorial, methodological, and critical-review papers in cognitive psychology; related areas are welcome when they directly interest cognitive psychologists and are understandable to that audience. (#2)
- **Review model:** single-anonymized peer review; editor suitability screen first; suitable submissions typically go to at least two reviewers; editors make the accept/reject decision. (#2)
- **Submission system:** Editorial Manager, reached from the ScienceDirect submit link. (#2, #3)
- **Abstract / keywords:** abstract maximum 250 words; 1-7 English keywords. (#2)
- **Highlights:** required at submission, 3-5 bullets, each up to 85 characters including spaces. (#2)
- **Research data:** Elsevier research-data **Option B** applies; authors are encouraged to deposit, cite, and link data, code, models, algorithms, protocols, or state why data cannot be shared. Data availability statements are encouraged at submission. (#2)
- **References:** APA 7th edition style; data and software references have explicit examples in the official guide. (#2)
- **Open access:** hybrid journal; APC displayed on the journal home page as USD 3,730 excluding taxes (2026-10-17 snapshot; USD 3,460 on 2026-06-21); subscription route has no publication fee charged to authors. (#1)
- **AI policy:** authors must declare generative-AI use in manuscript preparation; AI tools cannot be authors; generated or AI-altered manuscript images are not permitted except when the AI use is part of the research design and described reproducibly. (#2)

## Bounded live-check rules

- Do not encode a fixed manuscript word/page ceiling for this pack: the official guide emphasizes longer, integrative work but does not publish a numeric article-length cap in the sections read on 2026-06-21.
- 2026-11-24 access note: the live Guide for Authors could not be fetched directly (HTTP 403 bot challenge); its single-anonymized review, ≥ 2 reviewers, 250-word abstract, 1–7 keywords, 3–5 highlights of ≤ 85 characters and generative-AI declaration were re-confirmed from search-engine renderings of the guide on sciencedirect.com. The research-data Option B wording and the APA 7th reference style were **not** re-confirmed on 2026-11-24 (kept from 2026-06-21).
- **UNVERIFIED (2026-11-24):** the identity and start date of the next Editor-in-Chief after the September-2026 call — not announced on the pages reachable today.
- Treat metrics, APC, and editor listings as volatile. Re-open the ScienceDirect home page before quoting them in submission-ready advice.
- Do not import rules from *Cognition*, *Journal of Experimental Psychology: General*, *Psychological Science*, or *Journal of Memory and Language*.

## Machine-readable submission rules

Compiled from the prose above for tools/preflight.py; the prose is authoritative and python3 tools/venue_rules.py --check fails if the two disagree.

```json
{
  "schema": "ajs-preflight-rules/1",
  "venue": "Cognitive Psychology",
  "verified": "2026-11-24",
  "rules": {
    "abstract_words_max": {"value": 250, "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors", "note": "read via search-engine rendering of the guide on 2026-11-24 (the page returns a bot challenge to automated fetch)"},
    "keywords_min": {"value": 1, "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors"},
    "keywords_max": {"value": 7, "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors", "note": "English keywords"},
    "keywords_required": {"value": true, "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors"},
    "review_mode": {"value": "single-blind", "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors", "note": "single anonymized review; editor suitability screen, then typically at least two reviewers"},
    "main_text_words_max": {"value": null, "note": "no numeric article-length cap on the official pages as of 2026-11-24; the journal favours longer, integrative articles"},
    "required_statements": {"value": ["highlights", "keywords", "conflict_of_interest"], "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors", "note": "highlights: 3-5 bullets, each <= 85 characters including spaces, in a separate editable file; declaration of competing interest ('I have nothing to declare' option)"},
    "conditional_statements": {"value": ["ai_use_disclosure", "data_availability"], "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors", "note": "generative-AI use in manuscript preparation must be declared at submission; data availability statement encouraged under Elsevier research-data Option B (kept from 2026-06-21)"},
    "apc": {"value": "USD 3,730 excluding taxes (hybrid; no fee on the subscription route)", "source": "https://www.sciencedirect.com/journal/cognitive-psychology", "note": "journal home page, Internet Archive snapshot of 2026-10-17"},
    "portal": {"value": "https://www.editorialmanager.com/cogpsych/", "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors"},
    "llm_policy": {"value": "AI tools may support manuscript preparation but their use must be declared at submission; editors and reviewers may not upload manuscripts to generative-AI tools", "source": "https://www.sciencedirect.com/journal/cognitive-psychology/publish/guide-for-authors"}
  }
}
```
