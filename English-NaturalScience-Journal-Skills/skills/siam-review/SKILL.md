---
name: siam-review
description: Use when targeting SIAM Review (SIAM Rev.) or deciding whether an applied- or computational-mathematics manuscript fits this expository, broad-readership SIAM venue. Encodes the journal's fit, framing, expository-and-rigor bar, house style, official-submission re-check, and desk-reject heuristics.
---

# SIAM Review (siam-review)

## Journal positioning

SIAM Review, published by the Society for Industrial and Applied Mathematics, is the flagship general-readership journal of the applied- and computational-mathematics community. Its defining character is expository excellence for a broad audience: it does not exist primarily to publish narrow primary results, but to survey, contextualize, and illuminate. The journal is organized into distinct sections — Survey and Review (authoritative surveys of active areas), Research Spotlights (accessible accounts of a focused new result), SIGEST (revised reprints of outstanding papers from specialized SIAM journals, made accessible to the wider community), and Education (material of pedagogical value). The common thread is that articles must be readable, significant, and valuable to applied mathematicians, scientists, and engineers well beyond the immediate specialty.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the SIAM Review site and confirm the requirements for the specific section you are targeting.

## When to trigger

- The author wants to write an authoritative survey or an accessible account of applied/computational mathematics for a broad readership.
- A focused new result has wide appeal and could be presented as a Research Spotlight rather than a specialized primary paper.
- The author has a topic of strong pedagogical value suited to the Education section, or is considering nominating/preparing a SIGEST reprint.
- The author needs to understand which SIAM Review section fits, the expository bar, and common rejection reasons before submission.

## Scope & topic fit

- Survey and Review: authoritative, balanced surveys of an active applied- or computational-mathematics area, accessible to non-specialists and useful as an entry point.
- Research Spotlights: a single significant new result of broad interest, presented clearly and accessibly with the technical core intact but the exposition foregrounded.
- SIGEST: revised, accessible versions of outstanding papers selected from specialized SIAM journals (by invitation/selection).
- Education: expository material, novel pedagogical treatments, or case studies valuable for teaching applied and computational mathematics.
- Topics span numerical analysis, optimization, dynamical systems, scientific computing, mathematical modeling, applied probability, and the mathematics of data and applications.
- Narrow primary research without broad expository value belongs in a specialized SIAM journal, not SIAM Review.

## Method & evidence bar

- Exposition is the primary evaluation axis: clarity, balance, accessibility, and the ability to orient a broad reader are weighted as heavily as technical content.
- Surveys must be authoritative and even-handed: comprehensive coverage of the area, fair treatment of competing approaches, and an accurate, current bibliography.
- Mathematical content must still be correct and rigorous; results stated must be precise and either proved or correctly attributed, even when full proofs are deferred to references.
- Research Spotlights must convey genuine significance and broad interest, not merely a competent specialized result.
- MSC (Mathematics Subject Classification) codes should be assigned to signal scope; for applied work, note relevant computational or application domains.
- Reproducibility is valued where computational results are presented: code and data supporting figures should be available, consistent with current SIAM reproducibility expectations; arXiv posting is common and generally compatible.

## Structure & house style

- Structure follows the chosen section: surveys are organized for navigability (clear sectioning, summary tables, well-chosen figures); Research Spotlights are short and tightly focused; Education pieces foreground motivation and pedagogy.
- Writing must be accessible: define specialized terms, motivate before formalizing, and keep a broad applied-mathematics reader oriented throughout.
- Figures, schematics, and worked examples are encouraged and expected to carry expository weight.
- LaTeX with the current SIAM style/macros is standard — re-check the section-specific length and formatting requirements on the submission site.
- References must be complete, current, and balanced across the relevant literature; an out-of-date or one-sided bibliography is a serious weakness for a survey.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current SIAM Review submission instructions and confirm the requirements and length expectations for your target section (Survey and Review, Research Spotlights, SIGEST, Education).
- Assign MSC codes and note relevant application/computational domains.
- If computational results are presented, prepare supporting code/data per current SIAM reproducibility expectations; post to arXiv if appropriate with the identifier ready.
- Prepare a cover letter identifying the section, the intended broad audience, and why the article is significant and accessible to them.
- Confirm all co-authors have approved the submission and re-check current open-access/APC options under SIAM.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence naming the target section and why the article is significant and accessible to a broad applied-mathematics readership.
- [ ] The exposition orients a non-specialist: terms defined, motivation given, structure navigable.
- [ ] For a survey: coverage is authoritative and balanced, and the bibliography is current and even-handed.
- [ ] Mathematical statements are correct and precise; results are proved or correctly attributed.
- [ ] Figures, tables, and examples carry real expository weight; computational results have supporting code/data where applicable.
- [ ] An honest assessment: is this an expository contribution for a broad audience, or a narrow primary result better suited to a specialized SIAM journal?

## Common desk-reject triggers

- A narrow primary research paper submitted as if it were a survey or spotlight, without broad expository value.
- A survey that is unbalanced, out of date, or merely a reference list without synthesis and perspective.
- An article written for specialists that does not orient a broad applied-mathematics reader.
- A Research Spotlight whose result lacks genuine breadth of interest.
- A submission that ignores the section structure or grossly exceeds the section's expected length.

## Re-routing decision

Primary machine-learning research → `journal-of-machine-learning-research`. Narrow primary applied/computational results → the appropriate specialized SIAM journal (SIAM Journal on Numerical Analysis, Optimization, Scientific Computing, Applied Mathematics, etc.). Deep applied-analysis or PDE theory with substantial theorem content → `communications-on-pure-and-applied-mathematics`. Broad pure-mathematics results → `advances-in-mathematics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] SIAM Review
[Section] Survey and Review / Research Spotlights / SIGEST / Education
[Topic tags] <2–3 areas/domains>
[Method/evidence] <is the exposition broad and authoritative, and is the content correct, significant, and accessible?>
[Top risk] <the single most likely reason for rejection — usually breadth/exposition fit>
[Official items to re-check] <section requirements / length / MSC / reproducibility / open-access>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
