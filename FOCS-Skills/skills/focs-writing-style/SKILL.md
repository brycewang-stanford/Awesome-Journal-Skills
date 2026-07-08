---
name: focs-writing-style
description: Use when drafting or revising a FOCS (IEEE Symposium on Foundations of Computer Science) paper — making the first ten pages carry the whole case to a broad theory committee, pairing informal and formal theorem statements, keeping single-column 11-point prose readable, and writing double-blind-safe self-references.
---

# FOCS Writing Style

FOCS submissions carry no length cap, and the CFP encourages submitting the
full version of the paper — but everything outside the abstract, the
references, and the **first ten pages** is read only at the committee's
discretion (FOCS 2026 CFP, checked 2026-07-08). Style at this venue is
therefore an exercise in front-loading: the opening ten pages must let a
committee member from a different corner of TCS decide the paper's fate
fairly, even if they never turn to page eleven.

## Budgeting the guaranteed pages

A budget that survives contact with real papers:

| Pages | Content | Failure mode it prevents |
|---|---|---|
| 1–1.5 | Problem, headline theorem(s) informally, why they matter | Reviewer cannot state your result after page 2 |
| 1.5–3 | Context: prior bounds, the obstacle, your delta stated precisely | "Novelty unclear" from a non-specialist |
| 3–6 | Technical overview: the proof's actual ideas, with real definitions | "Contribution may be incremental" — ideas were invisible |
| 6–9.5 | Formal statements of all results; proof of one representative lemma in full | Committee cannot check that formality matches the informal claims |
| 9.5–10 | Organization note pointing into the body | Diligent reviewer gets lost after the window |

Every theorem you want credit for must be *stated* by page ten. A result whose
first appearance is page 23 does not exist for most of the committee.

## The informal/formal pairing

State each headline result twice: once in the introduction in plain language
with all quantifiers honest, once formally with every hypothesis. Keep the two
mechanically linked so they cannot drift apart across revisions:

```latex
% preamble: restatable theorems, one source of truth
\usepackage{thmtools, thm-restate}
\declaretheorem[name=Theorem]{theorem}

% introduction (inside the ten-page window)
\begin{restatable}[Main]{theorem}{mainthm}\label{thm:main}
  For every $\varepsilon>0$ there is a deterministic
  $O(m^{1+\varepsilon})$-time algorithm that ...
\end{restatable}

% body or appendix, before the proof
\mainthm*
\begin{proof} ... \end{proof}
```

The `thm-restate` discipline is the cheapest insurance against the classic
FOCS embarrassment: an introduction promising a bound the formal theorem
quietly weakens.

## Prose calibration for a cross-area committee

- **Quantify hedges.** "Nearly linear" must resolve to $O(m\,\mathrm{polylog}\,m)$
  or $O(m^{1+o(1)})$ within a sentence; the two are different claims and
  committees notice.
- **One new notion per section opening.** Single-column 11-point pages hold a
  lot of math; the reader's constraint is working memory, not ink. Introduce a
  definition, use it twice, then build on it.
- **Confession phrases are debts.** Every "it is standard that", "one can
  verify", and "similarly" in the guaranteed pages will be audited by someone;
  each must either point at a numbered reference or be provable by a reader in
  under a minute.
- **Name your techniques.** A committee remembers "the lazy-recoloring
  argument" and forgets "our second technical contribution". Naming is not
  vanity; it is compression for the PC discussion.
- **Write the obstacle paragraph.** The single highest-leverage paragraph in a
  FOCS submission explains why the previous best approach could not give your
  result. It converts "difficult" from an adjective into an argument.

## Double-blind prose

FOCS has used double-blind review for several cycles (2023–2026 CFPs all
require it), with the stated purpose of enabling an unbiased first judgment —
not making authorship undiscoverable. The prose consequences:

- Self-citations in the third person: "Chen et al. showed", never "we
  previously showed" — even when the antecedent is your own arXiv posting.
- No acknowledgements, grant numbers, or lab-specific phrasing ("our group's
  earlier framework") at submission time.
- Citing your own public full version is normal in this community; what is
  banned is prose that *asserts* the identity, not literature that permits a
  determined guess.

## Abstract anatomy

The abstract is guaranteed reading and often the only text a non-assigned PC
member sees before the discussion. A FOCS abstract that does its job contains,
in order: the problem in one sentence; the main bound or theorem with honest
quantifiers; the one-line comparison to the previous best; the technique named
in a phrase; and, when the paper has them, the downstream consequences. What
it omits: motivation boilerplate ("X is a fundamental problem"), citations,
and any claim the formal theorems do not support. Write it last, from the
restatable statements, so the abstract inherits their honesty.

## Notation economy

Single-column pages at 11 point invite dense macro-heavy notation; committees
across subareas punish it. Working rules:

- Prefer words to fresh symbols for anything used fewer than three times; a
  fourth-order tensor of indexed families needs a name, an ad-hoc set does not.
- Keep one notational convention per object class through the whole paper —
  a graph that is $G$ on page 2 must not become $\mathcal{G}$ on page 30 of
  the full version (statement-freeze tooling in `focs-reproducibility`
  catches drift in theorems, not prose; only discipline catches this).
- Standard objects get standard symbols; novelty budget is spent on results,
  not on renaming expansion constants.

## Revision pass order

1. Ten-page audit: print pages 1–10 alone; have a colleague reconstruct all
   claimed results from them.
2. Quantifier audit: every informal statement checked against its restatable
   twin.
3. Confession audit: grep the LaTeX for hedge phrases and discharge each.
4. Blind audit: third-person self-references, metadata, acknowledgements.

Do the passes in that order — narrative surgery invalidates later audits, so
anonymity always goes last.
