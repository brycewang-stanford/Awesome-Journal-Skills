---
name: soda-supplementary
description: Use when organizing the back matter of a SODA (ACM-SIAM Symposium on Discrete Algorithms) submission — there is no supplementary channel, so appendix architecture inside the single no-page-limit PDF does the supplement's job; covers front/back matter split, appendix ordering, and external-archive references.
---

# SODA Supplementary Material

SODA has **no supplementary upload**: no ZIP slot, no separate appendix deadline,
no reviewer-optional attachments. One PDF on HotCRP, with no page limit, carries
everything (2027 cycle, checked 2026-07-08 via the SIAM SODA27 submission page).
So "supplementary material" at SODA is an *internal layout question*: how to
architect a 40-80 page document so that a triaging PC member, a assigned referee,
and a rebuttal-window author can each navigate it.

## The two-tier document

Think of the submission as front matter (what every reader reads) and back matter
(what the assigned referee verifies), with an explicit contract between them:

| Tier | Typical span | Contents | Reader promise |
|---|---|---|---|
| Front | pages 1-10ish | Title-page abstract, result statements, technique overview, prior-bound comparison, proof roadmap | Self-contained: a PC member can judge significance without back matter |
| Back | the rest | Full proofs in dependency order, deferred cases, calculation appendices, computational-check descriptions | Complete: no step outsourced to "standard arguments" that are not |

The contract fails in both directions: front matter that cannot be judged alone
reads as disorganized; back matter that a referee cannot verify reads as wrong.

## Appendix architecture rules

- **Order by dependency, not by section of first mention.** A referee verifies
  linearly; forward references inside proofs multiply their working memory.
- **Restate before proving.** Use `thm-restate` or manual restatements so each
  appendix proof begins with the exact claim, eliminating page-flipping:

```latex
\usepackage{thm-restate}
% Front matter:
\begin{restatable}{theorem}{maindet}\label{thm:main}
  There is a deterministic $O(m\log^3 n)$-time algorithm for ...
\end{restatable}
% Back matter:
\maindet*   % restates Theorem 1 verbatim, then the full proof follows
\begin{proof} ... \end{proof}
```

- **One notation table, early.** Long documents die by drifting notation; a table
  after the introduction, and a rule that appendices introduce no new symbols
  without it, keeps a 60-page argument navigable.
- **Name the appendices by claim**, not "Omitted Proofs": "Appendix C: Proof of
  the Lower Bound (Theorem 3)" lets the referee jump straight from the rebuttal
  ledger to the page.
- **Case-heavy arguments get a case index**: a small table listing each case, its
  page, and its one-line resolution.

## What lives outside the PDF

Only material that *cannot* be prose belongs elsewhere, referenced from the paper:

- Machine-verification archives (certificates, checkers) at an anonymity-safe
  URL — see `soda-artifact-evaluation` for packaging and the anonymity rules.
- Implementation companions with benchmark data, if any — the paper cites them as
  color, and reviewers owe them nothing.
- The arXiv full version is *not* an external supplement at submission time: what
  you submit to HotCRP must itself be complete. Never write "see the full version"
  in a SODA submission — you are already submitting it.

## Navigation aids for a long reviewed document

An uncapped PDF is read on screens, out of order, by people hunting specific
claims during rebuttal season. Invest in navigability the way capped-venue
authors invest in compression:

```latex
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue]{hyperref}
\usepackage[capitalize,nameinlink]{cleveref}   % "Lemma 4.2" links whole
% After the introduction:
\tableofcontents                                % legitimate in an uncapped venue
% In the appendix preamble, a claim index:
% Theorem 1  -> proved in Appendix B (p. 24)
% Theorem 2  -> proved in Appendix C (p. 31), uses Lemmas C.1-C.4
% Lemma 4.1  -> proved inline (p. 12)
```

- A table of contents is not decoration here — it is the referee's map, and its
  section titles should narrate the argument ("Bounding the recourse of the
  overlay"), not name genres ("Analysis, continued").
- The claim index (theorem → proof location) is the same artifact as the
  claims ledger in `soda-reproducibility`; generate both from one source.
- PDF bookmarks come free with `hyperref`; check they render, since some
  reviewers navigate exclusively through them.

## Habits imported from capped venues that misfire here

| Imported habit | Why it misfires at SODA |
|---|---|
| "Proof deferred to the supplementary material" | There is no supplement; the phrase signals template reuse from another venue |
| Squeezing to 12 pages and dropping proofs | Uncapped submission: dropped proofs read as gaps, not thrift |
| Separate anonymous ZIP with the appendix | No such upload exists; appendix rides in the PDF |
| Supplement written after the deadline | Nothing can be added after July; the PDF is the whole record |
| Appendix as a dumping ground of drafts | Referees read it; unpolished back matter damages the front matter's credibility |

## Pre-upload back-matter audit

1. Grep the PDF text for "full version," "supplementary," and "omitted" — each
   hit is either a broken promise or a leftover from another venue's template.
2. Verify every front-matter theorem has a back-matter proof and vice versa (no
   orphan lemmas proving nothing that is claimed).
3. Check the dependency order: no proof uses a lemma proved later without an
   explicit forward pointer.
4. Compile with links on (`hyperref`) and click every `\ref` in the appendix.
5. Confirm the whole document — appendices included — passes the anonymity sweep.

## Output format

```text
[Back-matter verdict] Navigable / Needs restructuring / Incomplete
[Contract check] <front matter self-contained? back matter complete?>
[Orphans] <claims without proofs; proofs without claims>
[Ordering] <dependency violations found>
[External references] <archives cited; anonymity-safe? necessary?>
```
