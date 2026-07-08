---
name: popl-supplementary
description: Use when splitting a POPL paper across the 25-page body, the proof appendix, and anonymous supplementary material — deciding which proofs and auxiliary judgments leave the text, packaging proof scripts without identity leaks under full double-blind, and keeping every artifact self-consistent with the submission PDF.
---

# POPL Supplementary Material

A POPL submission is really three documents: 25 pages of text (bibliography
excluded) that must carry the whole argument, an appendix of full proofs and
auxiliary definitions, and — usually — an anonymized proof development or prototype.
Reviewers are typically expected to judge the paper from the body alone, so the split
is an argumentation decision, not a storage decision. Format and anonymity rules per
the POPL 2027 call, read 2026-07-08; confirm the current cycle's supplement wording
before uploading.

## What lives where

| Content | Body (25 pp) | Appendix | Anonymous artifact |
|---|---|---|---|
| Main definitions, typing/semantics rules actually discussed | yes | mirrored in full | formalized |
| Main theorem statements + proof sketches | yes | full proofs | checked statements |
| Auxiliary lemmas, weakening/substitution boilerplate | no | yes | yes |
| Full figure of every judgment (all rules) | representative rules only | complete figure | source of truth |
| Extended examples, failed design alternatives | one motivating example | yes | test files |
| Proof scripts, build instructions | no | no | yes, with README |

Two disciplines make the split safe:

- **The body must stand alone.** A reviewer who never opens the appendix should
  still believe the theorem plausible from the sketch: state the invariant, the hard
  case, and why it goes through. "Proof in appendix" after an unexplained claim
  reads as a gap.
- **Sketch and proof must not disagree.** The classic incident: the body's sketch
  describes induction on typing derivations while the appendix inducts on evaluation
  steps because the proof changed. Reviewers who notice stop trusting both.

## Anonymizing a proof development

Full double-blind covers everything you upload. Proof repositories are leaky:
`_CoqProject` paths with usernames, `lakefile` package names matching a public
GitHub project, author headers auto-inserted by editors, and `.git` directories with
full commit history. Build the archive from an export, never from a working tree:

```bash
git archive --format=tar.gz -o /tmp/supp.tar.gz HEAD          # no .git, no untracked junk
tar tzf /tmp/supp.tar.gz | grep -iE '\.git|/home/|users/|TODO|AUTHORS' && echo LEAK
grep -rInE '(Copyright|Author|@[a-z]+\.(edu|org|fr|de))' \
  --include='*.v' --include='*.lean' --include='*.agda' extracted/ | head
```

Also rename the development if its public name is googleable to your group, and
strip institutional CI configuration.

## Version-lock the trio

- Tag the exact commit that generated the submitted PDF, appendix, and archive; the
  author response will need to quote them line-precisely months later.
- If the appendix is a separate PDF, give it the same section numbering scheme as
  the body so "App. C.2" resolves unambiguously.
- Late theorem renumbering must propagate to the correspondence table and README —
  do it with a script, not by hand, in deadline week.

## Output format

```text
[Split audit] <claims whose evidence sits only outside the body>
[Sketch-proof consistency] <mismatches found>
[Anonymity scan] clean / leaks listed
[Version lock] <tag/commit for PDF + appendix + archive>
[Upload set] <files, sizes, formats for HotCRP>
```
