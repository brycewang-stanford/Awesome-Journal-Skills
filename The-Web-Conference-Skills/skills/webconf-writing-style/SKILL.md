---
name: webconf-writing-style
description: Use when drafting or revising a Web Conference (WWW) paper's prose — building the web-native framing that answers "why is this a WWW paper" on page one, writing for a mixed computing/social-science/economics readership, compressing into 8 self-contained pages, and handling scale numbers and platform names with precision.
---

# Web Conference Writing Style

A Web Conference paper is judged by readers who may sit in different disciplines
within the same track panel, under a rule that the first 8 pages must carry the
entire case. The house style that survives this: **lead with the web-native
mechanism, quantify the scale early, and write constructs so an adjacent-field
expert can check them.**

## The page-one obligation: web-nativeness

The venue's most predictable review sentence is a version of "unclear why this is a
WWW paper." Inoculate on page one by naming the property of the Web your
contribution depends on, as a mechanism rather than a backdrop:

| Weak (backdrop) | Strong (mechanism) |
|---|---|
| "We evaluate on web data" | "Anchor text distributes labels across sites, which our method exploits" |
| "Recommendation is important online" | "Feedback loops between ranking and clicks bias naive estimators; we correct for the loop" |
| "Misinformation spreads on platforms" | "Reposting graphs give exposure timestamps that identify the spread model" |
| "We test at web scale" | "At 10^9 edges, quadratic attention is infeasible; our sketch keeps error < ε at linear cost" |

If no such sentence can be written truthfully, the problem is routing, not prose —
go to `webconf-topic-selection`.

## Register for a mixed panel

- **Define constructs at first use** even when your subcommunity finds them
  obvious: "engagement (clicks per impression)," "polarization (as measured by
  ...)." Social-science co-reviewers check construct validity; systems co-reviewers
  check measurability. One parenthetical serves both.
- **Attach every adjective to a number or a mechanism.** "Large-scale" means a
  stated node/edge/user/request count; "efficient" means a complexity bound or a
  measured cost; "real-world" means a named data source with a collection window.
- **Name platforms carefully.** During double-blind review, an identifying platform
  ("our deployment at <company>") must be masked, but mask with *properties*, not
  vagueness: "a shopping platform with ~10^7 daily active users" preserves the
  evidential weight anonymously.
- **Ethics sentences are body text.** One or two sentences on consent, ToS
  compliance, and aggregation level, in Section 3 where the data is introduced —
  not exiled to the appendix (see `webconf-supplementary`).

## An introduction shape that fits this venue

```text
¶1  The web mechanism and the problem it creates or enables   (why the Web)
¶2  Why existing approaches miss it — each named line of prior
    work gets a specific failure tied to the mechanism          (the gap)
¶3  The contribution, typed explicitly: algorithm / system /
    measurement / dataset / theory                              (what's new)
¶4  Evidence preview with scale attached: datasets, platforms,
    windows, headline deltas                                    (why believe)
¶5  Reusability: what transfers beyond this platform/corpus,
    plus artifact availability                                  (why care)
```

Contribution typing (¶3) matters more here than at single-community venues: a
measurement paper judged as a methods paper fails, and vice versa. Say which one
you wrote.

## Compression into 8 self-contained pages

Reviewers may stop at page 8, so compression means *re-homing*, not shrinking
fonts (`acmart` tampering is detectable and sanctioned):

1. One figure that earns its column: replace the architecture-boxes diagram nobody
   quotes with the result figure reviewers screenshot.
2. Prose-to-table conversions for related work contrasts and dataset statistics.
3. Push proof bodies and protocol detail to the appendix, keeping statements and
   sketches in the body; the appendix is verification, not persuasion.
4. Kill roadmap paragraphs ("Section 2 discusses...") — sigconf headers already
   navigate.
5. Cut the second and third examples of every point; web papers over-illustrate.

## Sentence-level habits reviewers reward

- Past tense for what you measured, present tense for what the method does,
  future tense almost never (rebuttal-bait).
- Numbers with uncertainty where runs repeat: "34.2 ± 0.4" or "34.2 (95% CI
  33.9-34.5)," and effect direction in words for the cross-disciplinary reader.
- Limitations stated as scope, in the body's final section: "our identification
  holds for platforms exposing timestamps; feeds without them require..." — this
  venue reads honest scoping as strength, especially in Responsible-Web-adjacent
  tracks.

## Titles and abstracts in this venue's register

Scan any recent WWW proceedings table of contents and two title patterns
dominate: *mechanism-first* ("Correcting X-Bias in Y with Z") and *question-first*
for measurement papers ("Is X a Y or a Z?" — the Kwak et al. Twitter title is the
canonical instance). Patterns to avoid: bare system names with no claim
("WebFooNet"), stacked buzzwords ("Towards Trustworthy LLM-Empowered
Graph-Enhanced..."), and titles promising more generality than the evidence holds
— the title is the first overclaim reviewers can check. For abstracts, the
compression test: a reader should recover mechanism, contribution type, scale of
evidence, and one number from the abstract alone. If the abstract survives having
every adjective deleted, it is ready; if deleting adjectives leaves nothing, it
was decoration all the way down.

## Self-edit gate before submission

- [ ] Page 1 names the web-native mechanism in one sentence a chair could quote.
- [ ] Contribution type declared; every adjective has its number or mechanism.
- [ ] A non-specialist in the track's second discipline could restate your main
      claim after two pages.
- [ ] Nothing claim-bearing lives past page 8; no roadmap padding remains.
- [ ] Ethics and provenance sentences sit beside the data description.

Finally, keep the register stable across sections: a measurement-precise
Section 3 followed by a marketing-voiced Section 6 ("our groundbreaking
framework") reads as two authors who never met. The last pre-submission pass
should be a single-owner voice edit of the whole 8 pages.

## Output format

```text
[Web-native sentence] <quote it, or "missing — routing risk">
[Contribution type] algorithm / system / measurement / dataset / theory
[Register fixes] <constructs undefined, adjectives unattached, platforms named>
[Compression moves] <re-homing applied, pages recovered>
[Remaining risks] <style issues a track panel will still flag>
```
