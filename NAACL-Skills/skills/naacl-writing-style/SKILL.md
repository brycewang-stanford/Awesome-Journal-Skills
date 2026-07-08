---
name: naacl-writing-style
description: Use when revising the prose of a NAACL submission — scoping every claim to the languages and varieties actually tested, presenting non-English examples with glosses that carry the argument, writing a Limitations section that anticipates reviewers, and cutting to the ARR content-page budget without losing the linguistic substance.
---

# NAACL Writing Style

The house register at NAACL is precise about language and modest about
generality. The chapter's renaming to "Nations of the Americas" sharpened a
tendency its reviewers already had: sentences that quietly equate "language"
with "English" or "text" with "standardized text" get flagged, and claims
are expected to wear their linguistic scope on the surface.

## Scope discipline: say which languages, every time

The most common NAACL-bound prose failure is the unscoped universal:

| Draft sentence | What a reviewer writes | Repaired sentence |
|---|---|---|
| "Our method improves summarization." | "On which languages?" | "improves summarization on English and Brazilian Portuguese news" |
| "LLMs struggle with negation." | "All LLMs? All constructions?" | "the four evaluated models mishandle sentential negation in Spanish" |
| "This transfers to low-resource settings." | "You tested one." | "transfers to Guaraní; other low-resource claims remain untested" |
| "Speakers prefer our outputs." | "Which speakers, recruited how?" | "22 L1 Mexican-Spanish annotators preferred outputs 68% of the time" |

The repair is never hedging for its own sake — it is replacing a category
("low-resource languages") with the sample you measured.

## Examples as argument, not decoration

- Choose examples your quantitative analysis actually turns on: the error
  class that drives the gap, the construction the model misparses.
- Gloss every non-English example in three lines — original, aligned gloss,
  free translation — so a reviewer who reads none of your languages can
  still verify the reasoning.

```text
(3) axolotl  o-  k-  ita   in  siwatl        [Nahuatl]
    axolotl  PST-3SG.OBJ- see DET woman
    'The woman saw the axolotl.'
    -> the model tags 'axolotl' as agent: the error class in §5.2
```

- After each example, one sentence must state what it *demonstrates*; an
  example without a claim attached is a page cost with no return.

## First page architecture

State, in order and within the first column and a half: the phenomenon or
task; the gap in current handling; what you built or measured; the headline
result *with its scope*; why it matters to this community. A NAACL reader
should be able to quote your contribution accurately from the first page
alone — including its language coverage — without meeting a model name
before the problem.

## Limitations as anticipatory prose

Write the Limitations section by simulating the three most likely reviewer
objections and answering them in your own words first. Genuinely useful
NAACL-flavored entries: variety coverage ("results are for Rioplatense
Spanish; peninsular varieties untested"), annotator population limits,
data-governance constraints on release, and evaluation-metric validity for
morphologically rich languages. The section is uncounted; verbosity there
is free, evasiveness is not.

## Compression order for the content-page budget

1. Cut roadmap paragraphs and per-section previews — structure should show,
   not narrate itself.
2. Merge related-work prose into contrastive sentences attached to your
   contributions.
3. Collapse repeated table commentary into one analytical paragraph.
4. Move example galleries and full prompt text to the appendix, keeping the
   load-bearing instances.
5. Only then consider shrinking figures — never below caption legibility.

## Terminology and notation consistency

Multilingual papers accumulate inconsistency faster than monolingual ones
because every concept has more surface forms. Fix a house convention in a
notes file before drafting:

- One term per concept: pick "code-switching" or "code-mixing" and hold
  it; alternating reads as two half-edited drafts merged.
- One romanization/orthography per language throughout, matching what the
  data actually uses; if the corpus mixes orthographies, that fact is
  *content* and belongs in the data description, not in silent
  inconsistency.
- Variety codes stated once and reused (`es-MX`, `pt-BR`, `gn`), never
  informal synonyms ("Mexican", "the Spanish data") drifting through
  sections.
- Metric names with their implementation on first mention, then the bare
  name.

A ten-minute consistency sweep with `grep -c` over the LaTeX source for
each term variant catches most of it mechanically.

## Register calibration

- Prefer measured verbs: *indicates, is consistent with, fails on* — over
  promotional ones: *revolutionizes, unlocks, dramatically*.
- Name languages with their standard names and ISO codes on first mention
  (Guaraní, `gn`); respect community-preferred names for varieties.
- Keep diacritics correct in every language name and citation — misspelling
  *Wixárika* in a paper about it is a credibility wound at this venue.

## Output format

```text
[Scope audit] <unscoped claims found -> repaired versions>
[Example audit] <each example -> claim it carries; gloss ok?>
[First-page test] pass / rewrite needed (what's missing)
[Limitations preview] <predicted objections vs section coverage>
[Compression plan] <cuts in order, estimated page recovery>
```
