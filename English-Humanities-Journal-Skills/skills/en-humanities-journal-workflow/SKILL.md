---
name: en-humanities-journal-workflow
description: Use when deciding which English humanities journal skill to invoke next, comparing fit across the 36-journal humanities roadmap, or routing a manuscript before venue-specific re-framing. Routes by sub-field (history / philosophy / literary studies / classics / art history / religion / linguistics / musicology), contribution type (argument, interpretation, theory, edition), and the venue's house style and review norms.
---

# Humanities journal workflow (en-humanities-journal-workflow)

## Purpose

This is the routing skill for the humanities bundle. It does not replace a
single-journal profile; it first classifies the manuscript by **sub-field,
contribution type, and method/approach**, then routes into the matching per-journal
skill for fit and re-framing. It is a sibling to `en-natsci-journal-workflow`,
`en-engtech-journal-workflow`, and `en-journal-workflow`.

## Ask four things first

1. **Sub-field:** history, philosophy, literary studies, classics, art/architectural
   history, religious studies, linguistics, or musicology/aesthetics?
2. **Contribution type:** an original argument or interpretation, a theoretical or
   conceptual intervention, a recovery of new primary sources/evidence, a critical
   edition or attribution, or a methodological/historiographical reframing?
3. **Approach:** archival/empirical, close reading/textual, analytic/formal,
   theoretical/critical, or object-/image-based?
4. **Audience:** the whole field (a generalist flagship), a period/area specialty, or
   a method/theory community?

## Quick routing

| Manuscript signature | Prefer skill |
|---|---|
| Broad, field-defining historical argument | `the-american-historical-review` |
| Society/economy/culture history, problem-driven | `past-and-present` / `journal-of-social-history` |
| Modern European/transnational history | `the-journal-of-modern-history` |
| British/medieval/early-modern, archival | `the-english-historical-review` |
| Early-American / Atlantic history | `the-william-and-mary-quarterly` |
| Philosophy of history / historical method | `history-and-theory` |
| Major analytic philosophy article | `the-philosophical-review` / `nous` / `the-journal-of-philosophy` |
| Moral/political philosophy and ethics | `ethics` / `philosophy-and-public-affairs` |
| Broad philosophy (esp. UK tradition) | `mind` |
| Short, sharp philosophical note | `analysis` |
| Field-defining literary/critical-theory essay | `pmla` / `critical-inquiry` |
| Theory of literature / interpretive method | `new-literary-history` |
| Historicist / material-culture literary study | `representations` |
| Literary history, period-focused | `modern-language-quarterly` |
| Cross-linguistic / world-literature comparison | `comparative-literature` |
| Greek/Latin textual or interpretive scholarship | `the-classical-quarterly` |
| Roman history / archaeology / material culture | `the-journal-of-roman-studies` |
| Major art-historical argument (any period) | `the-art-bulletin` |
| Theoretically engaged art history | `art-history` / `october` |
| Connoisseurship / attribution / object study | `the-burlington-magazine` |
| Religious-studies argument / theory | `the-journal-of-religion` / `history-of-religions` |
| Biblical/theological/early-Christian scholarship | `harvard-theological-review` |
| Core theoretical/empirical linguistics | `language` / `linguistic-inquiry` |
| General linguistics / syntax-semantics theory | `journal-of-linguistics` / `natural-language-and-linguistic-theory` |
| Historical/analytical musicology | `journal-of-the-american-musicological-society` |
| Music theory and analysis | `music-theory-spectrum` |
| Philosophical aesthetics / art criticism | `the-journal-of-aesthetics-and-art-criticism` |

## Sibling-journal disambiguation

| Confusable targets | Decision rule |
|---|---|
| `the-philosophical-review` vs `nous` vs `the-journal-of-philosophy` | All are top generalist analytic venues; route by the article's length, sub-area conventions, and fit, and re-check current scopes — they are close substitutes. |
| `pmla` vs `critical-inquiry` | PMLA is the MLA's broad literary/language flagship; Critical Inquiry foregrounds theory and interdisciplinary critical intervention. |
| `the-art-bulletin` vs `october` vs `art-history` | The Art Bulletin is the CAA generalist flagship; October and Art History foreground critical/theoretical and contemporary engagement. |
| `the-american-historical-review` vs a specialty history journal | AHR wants broad significance across fields/periods; period- and area-specialist arguments often fit a specialty venue better. |
| `language` vs `linguistic-inquiry` | Language (LSA) is the broad disciplinary flagship; Linguistic Inquiry foregrounds generative theory — route by framework and audience. |
| Generalist flagship vs `analysis` | Analysis is for short, focused philosophical notes; a full-length argument belongs at a generalist venue. |

## Decision rules

- **Lead with the argument.** A humanities article is judged on the originality and
  force of its argument or interpretation, its command of sources, and its
  contribution to a scholarly conversation — not on data volume.
- **Sources and evidence.** Primary-source command, archival rigor, accurate
  quotation/translation, and engagement with the relevant scholarship are gating.
- **Field, period, and theory fit.** Match the period/area and the theoretical idiom to
  the journal's actual conversation; a mis-pitched idiom is a common desk reject.
- **House style is substantive.** Citation style (Chicago, MLA, or a discipline style),
  word limit, anonymization for double-blind review, and — for art history and
  musicology — image/example rights and permissions are real gates.
- **Generalist vs specialist.** Generalist flagships need field-wide significance;
  deep specialist work is often better served by a period/area journal.
- Always enter the single-journal skill's official-submission checklist before
  submitting; never rely on a stale template.

## Output format

```text
[Top journal skill] <skill-name>
[Alt 1] <skill-name> (reason)
[Alt 2] <skill-name> (reason)
[Do not submit to] <journal> (one-line mismatch reason)
[Contribution type] argument / interpretation / theory / sources / edition
[Biggest current gap] argument-originality / source-command / field-fit / theory-idiom / house-style / official requirements
[Next step] invoke <skill-name> for single-venue fit and re-framing
```
