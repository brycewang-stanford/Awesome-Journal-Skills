---
name: jmis-writing-style
description: Use when the prose is the bottleneck for a Journal of Management Information Systems (JMIS) manuscript — an abstract and introduction that land the IS-management contribution, and a body that reads for a method-literate but management-minded IS audience. Late-stage polish; do not invoke before the mechanism, identification, and contribution are settled.
---

# Writing Style (jmis-writing-style)

## When to trigger

- The mechanism, identification, and contribution are settled and the prose is the remaining gap
- The abstract or introduction buries the contribution under setup or method
- The paper reads like a reference-discipline manuscript (pure econ/CS) wearing an IS label
- The abstract exceeds **150 words** or quietly slips in citations

## Lead with the IS-management contribution

A JMIS reader is method-literate but management-minded. The introduction should reach the contribution fast: the technology, the managerial/economic question, what was not known, and what you show — stated for an IS audience, not buried under literature. The recurring failure is an intro that spends pages on background before the "we show that…" sentences. Get the IT artifact and the managerial stake on the first page.

## Write the 150-word, citation-free abstract last and tight

JMIS requires an abstract of **up to 150 words** with **no citations**, plus a set of **keywords** indicating the paper's content. Draft it after the intro is stable. It should name the technology/setting, the question, the method and data, the headline result *with magnitude*, and the contribution — in plain sentences a busy editor can scan. Do not pad it with background or cite prior work. (检索于 2026-06；以官网为准.)

## Keep the technology and the managerial payoff visible throughout

Because JMIS sits at the technology–organization–economics nexus, the prose should keep the **IT artifact load-bearing** and surface the **managerial/economic implication** as a first-class thread, not an afterthought paragraph. Translate statistical findings into managerial language where it helps (what a firm/platform should do), without overclaiming past the evidence. Define IS constructs precisely and use them consistently; explain reference-discipline machinery for an IS reader rather than assuming it.

## Match prose to JMIS's numbered-reference house style

JMIS uses **numbered bracketed citations [9] with an alphabetized reference list**, not author-date. Write so the argument reads cleanly with numeric cites (avoid "as Author (2020) argued" constructions that assume author-date), and confirm references are formatted to JMIS's numbered style before submission. (检索于 2026-06；以官网为准.)

## Tighten the prose

- Prefer the active voice and concrete subjects ("the platform redesign raised…") over nominalized passives.
- Cut hedging stacks ("it may possibly suggest") to a single calibrated claim.
- One idea per paragraph; topic sentence carries the point.
- Make every "implications for practice" sentence say something a manager could act on.

## A first-page test for the introduction

Read only page one and ask: can a JMIS editor name the technology, the managerial/economic question, the gap, and what you show? If any is missing, the intro is too slow. A reliable JMIS opening moves in four beats: (1) a concrete IT/management phenomenon a reader cares about; (2) the tension or gap in the IS conversation; (3) "in this paper we show that…" with the contribution and its magnitude; (4) why it matters for IS theory and for managers/firms/platforms. Save the extended literature for the positioning section — do not make the reader earn the contribution.

## Worked fix: an abstract that overruns and under-delivers (illustrative)

Before: a 190-word abstract that spends three sentences on background, cites two papers, and ends "implications are discussed." After: a 140-word, citation-free abstract — "Using the staggered redesign of a marketplace's ranking algorithm, we show that personalization reduced marginal-seller retention by 6 percentage points, shrinking buyer-side variety; the effect is concentrated among supply-constrained categories, implying platforms should temper personalization where seller supply is thin" — plus four keywords. It states setting, method, result *with magnitude*, and the managerial contribution, and it obeys the ≤150-word, no-citation rule.

## Checklist

- [ ] Intro reaches the IT artifact, managerial question, and contribution on the first page
- [ ] "We show that…" sentences are explicit and match the discussion
- [ ] Abstract ≤150 words, citation-free, names result + magnitude; keywords present
- [ ] IT artifact stays load-bearing; managerial/economic payoff is a visible thread
- [ ] IS constructs defined and used consistently; reference-discipline machinery explained
- [ ] Prose reads cleanly with numbered citations; references in JMIS numbered style
- [ ] Active voice; hedging trimmed; one idea per paragraph
- [ ] One term per construct, defined at first use and held stable throughout
- [ ] Prose contains no first-person self-citation or detail that breaks double-blind

## Write so the double-blind file stays blind

JMIS prose goes into a fully anonymized file, so the writing itself must not leak authorship. Phrase self-citations in the third person ("Prior work [12] shows…", not "In our earlier study we showed…"); avoid "as we have argued elsewhere"; keep acknowledgments, grant numbers, and institution names out of the draft; and do not name a proprietary dataset or platform in a way that fingerprints the author. These are stylistic habits, not just submission mechanics — building them into the prose now means the `jmis-submission` anonymization check finds nothing to fix.

## Anti-patterns

- An intro that withholds the contribution until after pages of background
- An abstract over 150 words, or with citations, or with no magnitude
- Prose written for an econ/CS audience that never surfaces the IS-management takeaway
- Author-date phrasings that fight JMIS's numbered-reference style
- "Implications for practice" that no manager could act on
- Polishing prose while the mechanism or identification is still moving
- Drifting between synonyms for one construct, so reviewers doubt the measurement
- First-person self-citations ("in our earlier study") that break double-blind anonymization
- Importing reference-discipline jargon without glossing it for an IS reader

## Keep the IS vocabulary precise and consistent

IS readers are unforgiving about loose construct language. Decide on one term per construct and use it everywhere — do not drift between "IT capability," "digital capability," and "technology resource" for the same thing, or between "platform openness" and "API accessibility" if you mean one concept. Define each construct at first use and keep the definition stable through theory, measurement, and discussion. When you import a reference-discipline term (e.g., a specific elasticity, a game-theoretic equilibrium concept), gloss it for the IS reader rather than assuming fluency. Precision here is not pedantry: a referee who sees a construct shift names mid-paper will doubt the measurement and the theory.

## Polish last, and only once

Writing-style is the final pass, so run it only after the mechanism, identification, contribution, and exhibits are settled — polishing prose around a moving argument wastes effort and risks locking in sentences you will have to cut. When you do polish, make one full pass for argument flow (does each section advance the claim?), one for construct and citation consistency, and one for sentence-level economy. Then write the abstract last, against the finished intro.

## Output format

```text
【Intro】contribution on page 1? "we show that…" explicit? [Y/N]
【Abstract】≤150 words, citation-free, magnitude + keywords? [Y/N]
【IS-management thread】artifact load-bearing; managerial payoff visible? [Y/N]
【Citation style】reads with numbered cites; refs in JMIS numbered format? [Y/N]
【Next step】jmis-submission
```
