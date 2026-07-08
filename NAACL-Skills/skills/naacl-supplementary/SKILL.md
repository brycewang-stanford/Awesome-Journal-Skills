---
name: naacl-supplementary
description: Use when deciding what goes into the content pages, the uncounted sections, the appendix, and the optional uploads of a NAACL-bound ARR submission — allocating material by what reviewers are actually obliged to read, and keeping glossed language examples and long tables from starving the main argument.
---

# NAACL Supplementary

An ARR submission bound for NAACL has four storage tiers with different
review contracts, and misfiling material across them is a self-inflicted
wound. The tiers, from strongest contract to weakest:

| Tier | Counted? | Reviewer obligation | Belongs here |
|---|---|---|---|
| Content pages (8 long / 4 short) | Yes | Must read; sole basis of judgment | Claims, method, main results, decisive analysis |
| Limitations (+ optional ethics) | No | Read and audited | Real scope boundaries, risk discussion |
| Appendix (same PDF, after refs) | No | May consult | Full prompt sets, extra tables, proofs of preprocessing |
| Uploaded supplements (archives) | No | Discretionary | Code, data samples, guidelines, raw outputs |

The operating rule: a reviewer who reads *only* tier 1 must be able to
accept the paper. If a claim's only support lives in tier 3 or 4, the claim
is unsupported for decision purposes.

## The NAACL-specific space pressure: examples in other languages

Papers on Spanish, Portuguese, Haitian Creole, or Indigenous American
languages carry a cost English-only papers never pay: every example needs
the original line, a gloss, and a translation — three lines where a
monolingual paper spends one. Budget for it deliberately:

- Keep two or three *load-bearing* glossed examples in the content pages —
  the ones your error analysis actually turns on.
- Move the example gallery to the appendix, one pointer per phenomenon.
- Never compress by dropping the gloss line; an unglossed example excludes
  every reviewer who does not read the language, which at a
  Nations-of-the-Americas venue is a strange own goal.
- Interlinear-gloss LaTeX packages (`gb4e`, `expex`) interact badly with
  tight column budgets; test early, not the night before.

## Limitations: uncounted but not unread

The Limitations section costs no pages, and reviewers check whether the
weaknesses they found appear in it. Write it as the paper's honest edge:

- which language varieties and domains the claims do not extend to;
- resource asymmetries (a 7B model per language vs. one multilingual run);
- annotation limits — single-dialect annotators, small agreement samples;
- what the community-data terms prevented you from testing or releasing.

A Limitations section that predicts the reviews reads as mastery; one that
lists "compute was limited" reads as filler.

## Appendix construction discipline

1. Every appendix section gets at least one forward reference from the
   content pages; unreferenced appendices are invisible.
2. Order appendix sections by reference order, not by writing order.
3. Tables that exist only to prove thoroughness (per-seed dumps, all-prompt
   grids) go last, clearly labeled as completeness material.
4. Nothing decision-critical enters the appendix after the response window
   — reviewers scored the paper without it.

## Tier migration during revision cycles

Material moves between tiers as the paper evolves, and each direction has
a rule:

- **Promotion (appendix → body):** legitimate any time before upload;
  after reviews, promote only what the response window discussed —
  reviewers scored the body they read.
- **Demotion (body → appendix):** the standard compression move; leave a
  one-line summary plus pointer at the original location so the argument's
  spine stays visible.
- **Resubmission reshuffles:** if a prior cycle's reviewer ignored
  appendix evidence, the fix is usually promotion plus a change-summary
  line saying so — not a complaint that the evidence existed.
- **Never migrate silently between the reviewed version and camera-ready:**
  the tier map of the accepted paper is part of what was accepted.

## Upload-tier packaging check

```bash
# Pre-upload sweep of the supplement archive
unzip -l supp.zip | grep -Ei '\.git/|DS_Store|__pycache__|\.ipynb_checkpoints'
# Anonymity: usernames, lab paths, letterheads
unzip -p supp.zip '*.md' '*.py' '*.txt' | grep -nEi '/(home|Users)/[a-z]+|university|lab\b'
# Size and openability on a clean machine
du -h supp.zip && unzip -t supp.zip > /dev/null && echo OK
```

## Allocation walkthrough

A 9.5-page draft on named-entity recognition for three code-switched pairs:
the per-pair ablation grid (0.7 pages) moves to the appendix behind one
summary row; four of six glossed examples move to an appendix gallery; the
dialect-coverage caveat moves *out* of a footnote into Limitations where it
is free; the annotation guidelines PDF and scoring scripts go to the upload
tier. Result: 8.0 content pages, no claim orphaned outside tier 1.

## Output format

```text
[Tier map] <major item -> tier -> justified?>
[Orphaned claims] <claims supported only outside content pages>
[Gloss budget] <examples kept in body / moved / at risk>
[Limitations audit] <predicted objections covered?>
[Archive sweep] clean / findings
```
