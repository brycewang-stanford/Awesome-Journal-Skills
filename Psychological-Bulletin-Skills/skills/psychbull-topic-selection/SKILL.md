---
name: psychbull-topic-selection
description: Use when deciding whether a question is review-worthy and meta-analyzable for Psychological Bulletin and which synthesis type fits (meta-analysis, systematic review, meta-review/meta-synthesis, qualitative review). Tests fit for an APA research-synthesis flagship; it does not write the review.
---

# Topic Selection & Synthesis Fit (psychbull-topic-selection)

Psychological Bulletin publishes **syntheses of research in scientific psychology**, not original
studies. The first question is therefore not "is my result interesting?" but **"is there a body of
existing studies worth synthesizing, and what synthesis does it support?"** This skill tests fit and
chooses the synthesis type; it does not draft content.

## When to trigger

- You have an idea for a review/meta-analysis and want to know if it fits Psychological Bulletin
- Deciding between a meta-analysis, a systematic review, or a qualitative review
- Worried the topic is too narrow, already reviewed, or actually a primary study in disguise

## Fit test for Psychological Bulletin

1. **It synthesizes existing research.** The contribution is integrating *prior* studies, not
   reporting new data (primary studies → other journals) and not pure theory (→ *Psychological Review*).
2. **There is a sufficient, locatable literature.** Enough comparable studies exist that a systematic
   search can plausibly recover them; a handful of papers is a narrative essay, not a Bulletin review.
3. **General psychological significance.** The question matters across psychology, resolves a debate,
   reconciles conflicting findings, or estimates the size and moderators of a much-studied effect.
4. **It adds beyond prior reviews.** If a recent meta-analysis exists, justify a new one (new studies,
   better methods, an unresolved moderator, a correction).

## Choosing the synthesis type

| If the literature… | Choose |
|--------------------|--------|
| Has many studies reporting **extractable, comparable effect sizes** | **Meta-analysis** |
| Is large but **heterogeneous / not cleanly poolable**, yet needs systematic appraisal | **Systematic review** (PRISMA) |
| Consists largely of **prior reviews or meta-analyses** | **Meta-review / meta-synthesis** |
| Is **qualitative or too varied to pool** but worth integrating | **Qualitative / narrative review** |

## Scoping the question

- Frame the question with an explicit structure (e.g., **PICO**-style: population, exposure/predictor,
  comparison/outcome) so eligibility can be operationalized later.
- Define the **outcome / effect** precisely — the same construct must be recoverable across studies.
- Anticipate the **moderators** you will test, so coding and search are designed for them.
- Sanity-check feasibility: a quick scoping search to estimate how many studies exist.

## Anti-patterns

- A "review" that is really an original empirical study with a literature section
- A topic with too few studies to synthesize (write a primary paper or a theory piece instead)
- Re-doing a recent meta-analysis with no added value
- Submitting original theory here instead of to *Psychological Review*
- A vague question that cannot be turned into eligibility criteria

## Output format

```
【Fit】synthesis of existing work? [Y/N — if N, which journal]
【Synthesis type】meta-analysis / systematic / meta-review / qualitative
【Question】structured (population / predictor / outcome)
【Why now】adds beyond prior reviews? [reason]
【Feasibility】rough study count from scoping search
【Next】psychbull-literature-search-strategy
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — scoping-search databases and reporting standards
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — Psychological Bulletin scope (syntheses, not primary studies)
