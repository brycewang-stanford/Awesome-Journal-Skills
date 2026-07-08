> **Illustrative teaching example.** The paper, systems, datasets, and every
> number below are **fictional**, invented solely to demonstrate the writing
> moves this pack teaches. No real result is cited and no venue policy is
> invented. Companion skills:
> [`naacl-writing-style`](../../skills/naacl-writing-style/SKILL.md),
> [`naacl-experiments`](../../skills/naacl-experiments/SKILL.md), and
> [`naacl-topic-selection`](../../skills/naacl-topic-selection/SKILL.md).

# Worked Example: A NAACL-Style Abstract + Introduction (before → after)

The exercise: take a first-draft opening whose claims float free of any
language, and rebuild it so that scope, evidence, and community relevance are
explicit — the register a NAACL reviewer reads as competence.

**Fictional paper:** *"When the Question Switches Language: Code-Switched
Question Answering over Spanish-English Community Forums."* Fictional
contribution: a QA evaluation set built from natively code-switched forum
text, plus an analysis of where monolingual-pipeline assumptions break.

---

## Before (the unscoped draft)

> **Abstract.** Question answering has made enormous progress with large
> language models. However, real-world text is often noisy and multilingual.
> We introduce a new benchmark for code-switched QA and evaluate several
> strong models, finding that performance drops significantly. Our analysis
> reveals interesting patterns and suggests directions for more robust
> multilingual NLP.
>
> **Introduction.** Code-switching is a common phenomenon in multilingual
> communities. Despite recent advances, most QA systems assume monolingual
> input. We collect a dataset of code-switched questions and answers and
> benchmark state-of-the-art models on it. Experiments show that all models
> struggle with code-switched input. We also perform a detailed error
> analysis. Our contributions are: (1) a new dataset; (2) extensive
> experiments; (3) insightful analysis.

### Why this fails the NAACL read

- **No language pair is ever named.** "Multilingual," "code-switched," and
  "real-world" appear; Spanish-English — the paper's actual object — never
  does. The scope probe fails in the abstract's first breath.
- **"Drops significantly" carries no number, no variance, no per-language
  breakdown** — the exact overclaim pattern `naacl-experiments` exists to
  catch.
- **The community is invisible.** Whose forums? Which varieties? Natively
  produced or synthetic switches? For a venue whose identity is the
  hemisphere's language communities, these are first-page facts.
- **Numbered contribution lists** ("extensive," "insightful") assert value
  adjectivally instead of demonstrating it propositionally.

---

## After (the scoped rebuild)

> **Abstract.** Speakers on Latin American community forums routinely ask
> questions that switch between Spanish and English inside a single
> sentence, but QA benchmarks treat the two languages as separate worlds.
> We present **MezclaQA** (fictional), 3,200 natively code-switched
> question-answer pairs drawn from public Mexican and Puerto Rican forum
> threads and annotated by bilingual speakers of the relevant varieties
> (κ = 0.81). Across six open- and closed-weight models, exact-match
> accuracy falls 14-22 points relative to matched monolingual controls
> (mean over 3 runs; per-model results §5), and the gap concentrates in
> questions whose *wh*-word and answer span sit in different languages.
> Attribution: 61% of errors trace to retrieval, not generation. We release
> the data, prompts, and scoring code under community-approved terms.
>
> **Introduction (first paragraph).** A monolingual QA pipeline assumes the
> question's language identifies the answer's. For the estimated tens of
> millions of Spanish-English bilinguals in the Americas, that assumption
> fails at the sentence level: *"¿Dónde encuentro el* deadline *para el* tax
> filing *de este año?"* asks one forum user, mixing determiner phrases
> across languages. We measure what this costs current systems — on text
> produced by the communities themselves, not on synthetically switched
> benchmarks whose distribution flatters monolingual training.

### What changed, move by move

| Draft symptom | Rebuild move | Skill that teaches it |
|---|---|---|
| "multilingual" with no languages | Spanish-English named in sentence one; varieties (Mexican, Puerto Rican) named at the data's introduction | `naacl-writing-style` scope discipline |
| "drops significantly" | "14-22 points, mean over 3 runs," with the breakdown's location cited | `naacl-experiments` variance floor |
| Invisible provenance | Forum source, bilingual annotators, agreement score, community-approved release terms — all on page one | `naacl-artifact-evaluation` |
| Generic motivation | A glossed, load-bearing example carrying the phenomenon | `naacl-writing-style` examples-as-argument |
| "insightful analysis" | One falsifiable analytic claim (retrieval causes 61% of errors) | `naacl-related-work` delta-sentence habit |
| Synthetic-vs-native silence | Explicit contrast with synthetically switched benchmarks | `naacl-experiments` translationese caution |

### The venue-fit sentence this rebuild earns

> "MezclaQA evaluates QA on natively code-switched Spanish-English from
> Latin American forums, showing retrieval — not generation — drives the
> bilingual performance gap."

One sentence; languages, data nativeness, and the mechanism finding all
present. If your own paper's version of this sentence still contains
"multilingual" doing unspecified work, return to
[`naacl-topic-selection`](../../skills/naacl-topic-selection/SKILL.md) and
[`naacl-writing-style`](../../skills/naacl-writing-style/SKILL.md) before
drafting further.

> For real NAACL papers whose first pages execute these moves, see
> [`../exemplars/library.md`](../exemplars/library.md); for the policy facts
> behind the submission itself, see
> [`../official-source-map.md`](../official-source-map.md).
