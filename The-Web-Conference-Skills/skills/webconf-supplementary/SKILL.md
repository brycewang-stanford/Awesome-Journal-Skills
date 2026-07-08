---
name: webconf-supplementary
description: Use when deciding what belongs in the Web Conference (WWW) appendix versus the 8 main pages versus an external artifact, under the single-PDF 12-page ceiling where references and appendix share the tail, reviewers need not read past page 8, and no separate supplementary upload exists in the research tracks.
---

# Web Conference Supplementary Material

The Web Conference's 2026 research tracks had **no separate supplementary upload**.
Everything travels in one PDF: 8 pages of main paper, then references, then an
optional appendix, capped at 12 pages total. That design creates a zero-sum tail —
every reference line competes with appendix space — and a hard rhetorical rule:
reviewers are told they need not read past page 8, so the appendix can *support*
belief but never *create* it.

## The three-container model

| Container | Budget | Reviewer contract | Right contents |
|---|---|---|---|
| Main paper | 8 pages | Read and judged | Claims, method, headline evidence, limitations |
| PDF tail | 12 − 8 − |refs| pages | Optional reading | Proofs, pseudo-code, protocol, extra tables |
| External artifact | unlimited | Reached only via link | Code, data manifests, full logs |

The tail is the scarcest resource most teams misbudget. A survey-flavored web paper
with 90 references can eat 2.5+ pages, leaving under 1.5 pages of appendix; a
theory-flavored one with 35 references gets nearly 4. Count your tail *before*
promising appendix sections to co-authors.

## What earns tail space (and what does not)

Earns it:

- Proof details whose theorem statement and proof *sketch* already appear in the
  main text.
- The full crawling/collection protocol backing a one-paragraph summary in Section 3.
- Hyperparameter and search-space tables; per-dataset statistics manifests.
- The pseudo-code for an algorithm described prosaically in the body.
- Secondary robustness tables that repeat a main-text conclusion, not extend it.

Does not earn it:

- Any result cited in the abstract, introduction, or conclusions. If a claim's only
  evidence lives past page 8, the claim is unsupported in the judged document.
- The ethics or data-consent discussion for human-derived web data — reviewers
  weighing harms must find this in the body.
- "Additional experiments" that introduce new claims — reviewers who do read the
  appendix will treat unvetted claims as overreach; those who don't will never see
  them. Either promote to the body or cut.

## Compression order when the PDF is over 12

1. Move executable detail (configs, exact commands) to the artifact and leave a
   pointer line.
2. Collapse per-dataset appendix tables into one table with grouped rows.
3. Trim redundant citations — cite the survey once instead of its 12 members where
   the specific member isn't discussed.
4. Convert appendix prose to structured tables; appendix text is skimmed anyway.
5. Only then touch the main 8 pages, using `webconf-writing-style` compression
   moves rather than spacing hacks — `acmart` tampering is detectable and treated
   as a formatting violation.

## Anonymized linking pattern

External artifacts referenced during review must not identify authors. The stable
pattern:

```text
In the PDF (Section 3, footnote):
  "Code and data manifests: https://anonymous.4open.science/r/webgraph-2F51
   (anonymized for review; will be archived with a DOI upon acceptance)."

Checks before submission:
  - repository has no git history, no institutional paths, no author usernames
  - README written in the same anonymous voice as the paper
  - dataset files carry the crawl manifest, not internal project codenames
  - link actually opens in a logged-out browser session
```

At camera-ready the anonymous mirror is replaced by the DOI-bearing archival
deposit (see `webconf-artifact-evaluation` for the deposit and badge flow).

## Worked budget: one paper, two viable splits

A graph-mining submission has 8.0 main pages locked and must choose its tail. Two
honest allocations of the 4-page tail, for different paper shapes:

| Tail plan | References | Appendix | Fits which paper |
|---|---|---|---|
| Method-heavy | 1.5 pp (42 refs) | 2.5 pp: proof details, pseudo-code, hyperparameter grid | Theory/algorithm claims needing verification depth |
| Measurement-heavy | 2.2 pp (68 refs) | 1.8 pp: collection protocol, per-platform stats, bot-filter rules | Empirical claims needing literature coverage |

What does not exist is the fantasy allocation (2.2 pp of references *and* 2.5 pp
of appendix). Teams discover this on deadline night when BibTeX renders; discover
it two weeks earlier by compiling with the real bibliography and an appendix
skeleton, then assigning the tail like any other scarce budget — explicitly, in
writing, before co-authors draft appendix sections that will not fit.

## Cross-track variation

The single-PDF-with-appendix rule above is the *research tracks* rule for 2026.
Short papers ran at 4 pages **including references** — effectively no tail at all —
and companion-proceedings calls (demos, PhD symposium, workshops) each set their
own limits. Never transplant this page arithmetic across calls; reopen the specific
call's page before formatting.

Note also the asymmetry at camera-ready: the proceedings budget re-labels the
zones (12 pages, 8 *content*) but does not enlarge the content allowance, so an
appendix section promoted during revision must evict something — plan the
appendix as if its contents were permanent residents, not staging.

## Pre-flight audit

- [ ] Total ≤ 12; main ≤ 8; nothing claim-bearing after page 8.
- [ ] Every appendix section is *pointed to* from the body ("full protocol in
      App. B") — orphan appendices signal padding.
- [ ] Every body forward-reference resolves ("App. C" exists and matches).
- [ ] Ethics/consent discussion in the body, not the tail.
- [ ] Anonymous artifact link passes the logged-out test.

## Output format

```text
[Tail budget] refs=<pages> appendix=<pages> total=<n>/12
[Misplaced content] <claims past p.8 / ethics in tail / orphan appendices>
[Compression applied] <moves 1-5 used>
[Artifact link] anonymized + reachable: yes/no
[Cross-references] body->appendix and appendix->body both resolve: yes/no
```
