---
name: jet-writing-style
description: Use when applying the Journal of Economic Theory (JET) house style to a manuscript — the Elsevier elsarticle theorem-proof format with definition/assumption/proposition/theorem/proof structure, disciplined notation, full references in the abstract, and an Elsevier reference style. For drafting and polishing JET prose; it does not check proofs.
---

# Writing Style (jet-writing-style)

## When to trigger

- Drafting or polishing a JET theory manuscript
- Converting a working paper into JET's elsarticle theorem-proof format
- Tightening notation and statements before submission

## JET house style

- **Typeset in LaTeX, Elsevier `elsarticle` class.** Source must be editable `.tex`; PDF is not
  accepted as a source file. Use proper theorem environments (`amsthm`): Definition, Assumption,
  Proposition, Lemma, Theorem, Corollary, Proof.
- **Theorem-proof structure, not narrative-empirical.** Set up the environment and primitives, state
  assumptions, then results, then proofs (heavy ones to an appendix). The reader should be able to read
  every formal statement without hunting through prose.
- **Notation discipline.** Introduce each symbol once, never reuse a symbol for two objects, keep the
  body and proofs identical. A notation table helps in long papers.
- **References.** Elsevier style — `elsarticle-harv` (name-year) or `elsarticle-num` (numbered); the
  required one is **待核实**, confirm in the live guide. **References cited in the abstract must be given
  in full.** Keep **unpublished results / personal communications out of the reference list.**
- **JEL codes and keywords** are expected per standard Elsevier economics practice (verbatim-rule
  status is **待核实**).
- **Generative-AI disclosure** belongs in the submission, not the prose; reviewers/editors are barred
  from using such tools — write so a human expert can follow every step.

## Prose targets

- State each theorem so it is **self-contained** — readable without the surrounding paragraph.
- Give a **one-line intuition** before a long proof; do not let intuition substitute for rigor.
- Prefer "We prove that …" over hedged "essentially / roughly" phrasing the theorem does not support.

## Notation audit

Before submission, create a notation pass:

- Every primitive is introduced before first use.
- Every assumption label is referenced in at least one theorem or lemma.
- Every theorem statement can be read without searching the previous paragraph.
- Symbols in figures, proofs, and appendices match the body exactly.
- Appendix proof numbering preserves the main theorem dependency order.

Notation consistency is not cosmetic in JET; it is how referees verify the argument.

## amsthm scaffold for a JET manuscript

```latex
% Body carries statements + a sketch; the appendix carries full proofs with restatements.
\begin{assumption}\label{a:sc}
Each type's utility satisfies strict single crossing in (action, type).
\end{assumption}

\begin{theorem}\label{thm:main}
Under Assumptions \ref{a:sc}--\ref{a:compact}, an optimal mechanism exists and is deterministic.
\end{theorem}

\begin{proof}[Sketch] % ≤ 1 paragraph in the body: name the key step, point to the appendix
The allocation is pinned down by Lemma~\ref{lem:mono}; a duality argument then delivers the
transfers. Full details are in Appendix~B.
\end{proof}
```

The pattern to copy: the theorem cites its assumptions by label, the sketch names the key
argument in one sentence, and nothing in the body forces a referee to page-flip mid-statement.

## Sentence-level register for theory prose

- Statements **quantify** ("for every", "there exists") rather than gesture ("in general",
  "typically").
- The body says what each lemma buys economically ("Lemma 2 rules out pooling at the top"); the
  appendix carries the epsilon-management.
- "It is easy to see" is banned wherever a referee could disagree — replace it with the one-line
  reason or a pointer to the appendix step.
- Intuition paragraphs are labeled as intuition and are never load-bearing: deleting them must
  leave the proof intact.

## Hedged-claim rewrite (micro-example)

- **Before:** "Our results show that ambiguity essentially eliminates the gains from screening."
- **After:** "Theorem 3 shows that for maxmin bidders with full-support prior sets, the optimal
  mechanism is a posted price; screening gains are zero in this class — and only in this class
  (Example 4)."

The rewrite replaces "essentially" with the exact class where the claim holds and the example
that bounds it. Run this transformation on every hedge word in the abstract and introduction.

## Anti-patterns

- Submitting PDF source instead of `.tex`
- Mixed reference styles, or abstract citations abbreviated to "et al."
- Symbol reuse and notation drift between statement and proof
- An empirical-paper voice (data-story framing) imposed on a theory result

## Output format

```
【Format】elsarticle .tex, amsthm environments? [Y/N]
【Notation】one symbol ↔ one object, body=proof? [Y/N]
【References】Elsevier style; abstract refs in full; no personal comms? [Y/N]
【Disclosures】JEL+keywords; AI declared at submission? [Y/N]
【Next】jet-tables-figures / jet-submission
```
