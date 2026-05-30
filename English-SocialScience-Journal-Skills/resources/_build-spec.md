# Build Spec — English-SocialScience-Journal-Skills (per-journal profile skills)

This file is the **single source of truth** for the format, voice, and factual
discipline of every per-journal profile skill in this bundle. It mirrors the
proven design of the sibling `Chinese-SocialScience-Journal-Skills` bundle, but
in English and tuned for international econ / finance / management / accounting /
marketing / operations / information-systems venues.

Each journal ships **one self-contained "fit-and-house-style" profile skill**.
A profile answers four questions for an author:

1. Is my manuscript on-target for this venue?
2. How should it be framed to fit the venue's editorial culture?
3. What method-and-evidence bar does this venue expect?
4. What official submission details must I re-check before submitting?

A profile is a **positioning / venue-selection / re-framing** tool. It is **not**
a substitute for the journal's current official author instructions, and it must
say so.

---

## Canonical template (follow section order and headings exactly)

```markdown
---
name: <slug>
description: Use when targeting <Full Journal Name> (<ABBR>) or deciding whether an economics / finance / management / accounting / marketing / operations / information-systems manuscript fits this venue. Encodes the journal's fit, framing, method-and-evidence bar, house style, official-submission re-check, and desk-reject heuristics.
---

# <Full Journal Name> (<slug>)

## Journal positioning

<2–4 sentences: discipline, tier, what kind of paper wins here, who the readership is. Then one boundary sentence:>
This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the publisher's own site or submission system.

## When to trigger

- The author names <Full Journal Name> / <ABBR> as the target venue.
- A manuscript is near this venue's scope but the author is unsure about contribution level, method bar, or audience fit.
- A general <field> manuscript needs re-framing into the narrative this venue rewards.
- The author needs this venue's high-frequency desk-reject risks and a credible alternative-venue list before submitting.

## Scope & topic fit

- <3–6 bullets of the SPECIFIC topics / questions / paradigms this venue publishes — make it venue-distinctive, not generic.>

## Method & evidence bar

- <3–6 bullets on what this venue demands methodologically: identification standard, theory contribution, modeling rigor, data, replication/pre-registration norms, etc. Be venue-specific.>

## Structure & house style

- <3–6 bullets on framing, contribution statement, intro structure, abstract conventions, length, exhibits, and any venue-specific submission artifacts (e.g., significance statement, structured abstract, online appendix, data/code availability).>

## Official-submission checklist

- Search the live site for "<Full Journal Name> submission guidelines / author instructions / information for authors" and follow the current version, not a third-party broker's copy.
- Re-check <venue-specific items: anonymization/double-blind, word/figure limits, abstract/JEL or keyword codes, reference style, data & code availability policy, pre-registration / registered-report options, ethics/disclosure, submission fees>.
- <1–2 more venue-specific official items.>
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating why this paper belongs to <ABBR>'s core readership.
- [ ] The contribution is stated as <theory / identification / measurement / mechanism>, not as statistical significance.
- [ ] The introduction positions the paper against <2–3 recent papers in this venue or its tier>.
- [ ] Methods, data, exhibits, and references already match the current official guide.
- [ ] <1–2 venue-specific self-checks.>

## Common desk-reject triggers

- <3–5 venue-specific failure modes that get papers desk-rejected or quickly rejected here.>

## Re-routing decision

<2–4 sentences or bullets: if the paper does not fit, name the more appropriate sibling venue(s) and why — use real journal names, ideally other slugs in this bundle.>

## Output format

` ``text
[Fit] High / Medium / Low (one-line reason)
[Target] <Full Journal Name>
[Topic tags] <2–3 closest topics>
[Method/evidence] <does the current method clear this venue's bar?>
[Top risk] <the single most likely reason for rejection>
[Official items to re-check] <submission system / blinding / abstract / exhibits / data-code / etc.>
[Re-route suggestion] <if not a fit, a better-matched venue>
` ``
```

(The triple-backtick fence above is shown escaped; in the real file use a normal
```text fenced block.)

---

## Voice & quality rules

1. **English, opinionated, venue-specific.** Every section must contain content
   that could only be true of *this* venue. If a paragraph would read identically
   for ten journals, it is wrong. The whole value of the bundle is differentiation.
2. **Capture editorial DNA.** State the venue's actual culture: e.g., QJE rewards
   big questions with clean identification; Econometrica wants a theorem or a new
   estimator with proofs; AMR publishes theory papers with no data; Management
   Science is a methods-broad umbrella with department editors; MISQ wants an IS
   theoretical contribution, not just an ML benchmark; JCR wants multi-study
   process evidence for a consumer-behavior theory; TAR/JAR/JAE differ sharply in
   taste even within accounting.
3. **Length:** ~90–150 lines. Dense, scannable, no filler.

## Factual discipline (hard rules — do not break)

- **Do NOT invent volatile facts.** No impact factors, acceptance rates, ISSNs,
  exact word counts, submission fees, editor names, or "ranked #N" claims unless
  they are stable and widely known. When tempted, defer to the official-check
  section ("re-check current word limit") instead of stating a number.
- **Stable, well-known facts are fine:** discipline, that AER/QJE/JPE/Econometrica/
  REStud are the econ "top-5"; that JF/JFE/RFS are the finance "top-3"; that
  AMJ/AMR/ASQ/SMJ/OrgSci/AMA are management's elite; FT50 / UTD24 / ABS 4* set
  membership when widely documented; STAR-Methods-style or significance-statement
  artifacts where they are a permanent venue feature.
- **No fabricated citations.** Do not cite specific articles by title/author/year.
  Refer to literatures and paradigms generically ("the staggered-DiD literature").
- **Defer, don't guess.** Anything that changes year to year goes in the
  official-submission checklist as "re-check," never asserted as current fact.

## Slug / naming

- Slug = kebab-case of the full journal name (frontmatter `name` == folder name).
- When an English slug would collide with a slug already used by the
  `Chinese-SocialScience-Journal-Skills` bundle, suffix `-en` (mirrors that
  bundle's own `-cn` disambiguation convention). The only known collision is
  `journal-of-management` → use `journal-of-management-en` for the SAGE
  *Journal of Management*.
