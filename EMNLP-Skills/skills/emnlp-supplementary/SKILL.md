---
name: emnlp-supplementary
description: Use when dividing an EMNLP paper between content pages, uncounted Limitations and ethics sections, appendices, and ACL Rolling Review supplementary uploads — deciding what reviewers are owed in the body, what belongs in appendix prompts-and-tables territory, and what ships as anonymous code and data archives.
---

# EMNLP Supplementary

Use this when the paper is being carved into layers. Under ARR, an EMNLP submission is a
stack of surfaces with different review guarantees: content pages that reviewers must
read, uncounted mandatory sections they will read, appendices they may read, and
supplementary uploads they are explicitly not obliged to open. Misplacing one artifact
across these boundaries is a quiet way to lose a review.

## The four surfaces and their contracts

| Surface | Counted? | Review contract | Belongs here |
|---|---|---|---|
| Content pages (8 long / 4 short) | Yes | Must-read | Claims, method, headline results, error analysis core |
| Limitations (+ optional ethics) | No | Read and audited | Real boundaries, risks, cultural scope of annotations |
| Appendices | No | Discretionary | Verbatim prompts, full result grids, guidelines, proofs of detail |
| Supplementary upload | No | Explicitly optional | Code, data samples, model outputs, extended logs |

The design rule: **a reviewer who stops at the Limitations section must already be
convinced.** Anything decision-critical placed lower in the stack is a gamble on
reviewer generosity that the venue's own rules tell you not to make.

## What EMNLP appendices are actually for

NLP papers generate a characteristic residue that appendices exist to hold:

- **Prompts, verbatim.** Every template, system message, and few-shot block behind a
  reported number — paraphrased prompts are not reproducible.
- **The full grid.** Body tables show the decision-relevant slice; the appendix holds
  every language × model × metric cell so nobody suspects curation.
- **Annotation materials.** Guidelines, interface screenshots, qualification tests,
  adjudication rules — the things the Responsible NLP checklist swears exist.
- **Example galleries with counts.** Extended model outputs organized by the error
  taxonomy from the body, each category labeled with its frequency.
- **Negative and sanity results.** The prompt variants that didn't work, the metric
  that disagreed — cheap honesty that pre-empts "did you try…" reviews.

Every appendix section needs at least one pointer from the body; unreferenced
appendices are invisible, and reviewers do not spelunk.

## Anonymity holds at every layer

The no-anonymity-period policy frees your preprint, not your uploads. Supplementary
archives leak identity more often than PDFs because they are assembled last, from
working directories:

```bash
# Sweep the supplementary archive before upload
unzip -l supp.zip | grep -Ei '\.git/|\.ipynb_checkpoints|DS_Store'
unzip -p supp.zip '*.py' '*.md' '*.json' 2>/dev/null | \
  grep -nEi 'github\.com/|/home/[a-z]+|@[a-z]+\.(edu|com)|wandb\.ai/[a-z]' | head
# Notebook metadata carries usernames; strip outputs and metadata before packaging
```

Model outputs deserve a special pass: generated text sometimes quotes training data
containing your own lab's names or URLs, and cached API responses may embed account
identifiers in headers you forgot were in the JSON.

## Splitting under the cap: a worked division

A long paper on multilingual toxicity detection with a new annotated corpus, three
model families, and a human evaluation:

- **Body:** task motivation with measured gap; corpus construction summary with
  agreement numbers; main comparison (one table, five languages); error taxonomy with
  frequencies; significance methodology in two sentences.
- **Limitations:** script and dialect coverage boundaries; annotator demographic frame;
  known label ambiguity classes.
- **Appendix:** full guidelines; per-language result grids; all prompts; extended
  examples per error class; annotation interface.
- **Supplementary zip:** corpus sample with license file, scoring scripts, run configs.

The test of the split: could a skeptical reviewer verify the headline claim without
opening the zip? Here, yes — the zip only deepens verification, it never gates it.

## What does not belong in an appendix

The appendix is discretionary reading, which cuts both ways — some material placed
there is effectively deleted, and some actively hurts:

- **The only statement of a core claim's evidence.** If the body says "see App. F for
  the main comparison," the paper has moved its heart into optional territory.
- **The error analysis.** Reviewers treat body-level error analysis as a signal of
  seriousness; an appendix-only error analysis reads as an afterthought filed under
  completeness.
- **Un-discussed contradictions.** An appendix grid quietly showing the method losing
  on two languages the body never mentions is not transparency, it is a landmine — a
  reviewer who finds it will ask why the body didn't.
- **Fresh claims.** Anything argued for the first time in an appendix escapes the
  review contract; ACs are entitled to ignore it, and sharp ones flag it.

The repair in each case is the same: surface the finding in the body in one honest
sentence, and let the appendix hold the detail.

## Size, format, and cycle volatility

Upload caps, accepted formats, and whether appendices ride inside the main PDF or as
separate files are OpenReview-form details that ARR can change between cycles — read
the current form fields rather than assuming last cycle's layout. When in doubt, put
appendices in the main PDF after references (the prevailing ACL-family pattern) and
reserve the separate upload for genuinely non-PDF material.

## Short papers: the compressed stack

A 4-page short paper uses the same four surfaces at higher pressure. The body holds
exactly one claim and its strongest evidence; the Limitations section does double duty
as the honest scope fence that lets the one claim stay sharp; the appendix absorbs the
full grid that proves the claim was not cherry-picked. What short papers cannot do is
use appendices to smuggle a long paper past the format — reviewers calibrate to the
4-page contract and read an appendix three times the body's length as a format dodge,
not thoroughness.

## Output format

```text
[Layer map] <artifact -> body / limitations / appendix / supplementary>
[Must-read completeness] <can review conclude from body + limitations alone: yes/no>
[Orphaned appendices] <sections never referenced from the body>
[Anonymity sweep] <archive findings>
[Form check] <current upload fields and caps confirmed: yes/no>
```
