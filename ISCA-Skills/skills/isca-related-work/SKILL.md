---
name: isca-related-work
description: Use when positioning an ISCA submission against prior art — covering five decades of architecture literature across ACM DL, IEEE Xplore, and dblp, differentiating by mechanism rather than metric, handling self-citations and arXiv preprints under double-blind rules, and exploiting ISCA's unlimited reference pages.
---

# ISCA Related Work

Architecture is an old field with a long memory. ISCA has run since 1973, its
committee members have often worked an area for twenty years, and the fastest way
to lose a reviewer is to present a mechanism they saw under another name in a
proceedings they attended. Positioning at this venue is therefore archaeology
first, differentiation second.

## Search across three catalogs, because ISCA lives in two publishers

ISCA's dual ACM/IEEE sponsorship means its proceedings are split across publisher
libraries by edition (the 52nd, Tokyo 2025, was ACM-published; the 2026 edition
carried IEEE branding — the pattern alternates). Consequences for search:

- **dblp** (`dblp.org/db/conf/isca/`) is the reliable spine: complete, per-edition,
  publisher-neutral. Start every sweep there.
- **ACM DL and IEEE Xplore** each hold only part of the canon; searching one and
  concluding "no prior work" is a classic self-inflicted wound.
- Sweep the sibling venues as first-class citizens — MICRO, HPCA, ASPLOS — plus
  the journals where architecture ideas resurface (TACO, CAL, TC, IEEE Micro
  including its annual Top Picks selections).
- Finish with a recent-window arXiv pass: concurrent preprints will not sink you,
  but a reviewer mentioning one you never saw costs credibility in the rebuttal.

## The lineage paragraph reviewers actually want

For the two or three mechanisms closest to yours, write lineage, not lists:

> Decoupled tracking originates with <A> [x], which <B> [y] extended to
> multi-level hierarchies at the cost of <specific cost>. Both retain <shared
> assumption>. We remove that assumption, which is what enables <consequence §4>.

The differentiation must be **structural** — a different trigger, storage
organization, or contract — and it must be checkable against your design section.
"Unlike prior work, our approach is efficient" differentiates nothing; every
cited author believed the same of theirs.

## Where comparison belongs

| Relationship to your work | Treatment |
|---|---|
| Same problem, mechanism your evaluation can implement | Quantitative baseline in the evaluation (see `isca-experiments`), plus one lineage sentence here |
| Same problem, mechanism impractical to reimplement | Honest qualitative contrast: what it assumes, what yours assumes, why numbers aren't comparable |
| Same mechanism family, different problem | One sentence acknowledging the family; do not manufacture rivalry |
| Classic paper that named the idea space | Cite it — omitting the acknowledged origin insults exactly the senior reviewers most likely to notice |
| Concurrent preprint (recent arXiv) | Cite neutrally as concurrent; differentiate without claiming priority wars |

## Double-blind mechanics, ISCA 2026 wording

The verified 2026 guidelines are specific and slightly unusual:

- References must **not** be omitted or anonymized — the bibliography stays intact.
  Blinding happens in the *prose voice*, not the reference list.
- Your own prior papers are cited in third person: "extends the tracker of Chen et
  al. [7]" — never "our prior design [7]". Audit for possessives near citations.
- Links to your artifacts (repos, project pages) must be **fully anonymized**;
  a github.com/<yourlab> URL anywhere in the paper is an identity leak.

```bash
# Blind-voice audit over the LaTeX source
grep -nEi 'our (prior|previous|earlier|recent) (work|paper|design|study)' *.tex
grep -nEi 'we (previously|earlier) (showed|proposed|presented)' *.tex
grep -nE  'github\.com|gitlab\.com|bitbucket|\.edu/~[a-z]' *.tex *.bib
# Coverage sanity: in-text citation keys that never resolve
grep -oE '\\cite[tp]?\{[^}]*\}' *.tex | tr ',' '\n' | sort -u | wc -l
```

## Building the map before writing the section

Maintain a positioning table in the repo from week one; the section then writes
itself and the rebuttal reuses it:

```text
prior-work-map.tsv
mechanism            venue/year   trigger        storage        differs-from-ours-by
StreamTrack [x]      ISCA'19      miss-driven    per-core CAM   global stall on rollback
LazyMerge  [y]       MICRO'22     epoch-driven   shared SRAM    no cross-level visibility
<ours>               —            demand+decay   per-bank tags  removes rollback entirely
```

Rows come from the dblp sweep; the last column must name a mechanism-level delta.
If you cannot fill that column for a row, that row is your real problem — solve
it in the design or the framing, not in adjectives.

## Using the unlimited reference pages

ISCA 2026 imposed no limit on reference pages, and architecture papers routinely
carry 60-90 citations. Never trim the bibliography for space — trim prose. A thin
bibliography in an old field signals a shallow sweep to reviewers who know the
depth exists. Depth means: the origin paper of each idea family, the strongest
recent representative, and the sibling-venue variants — not twenty near-duplicate
cites of one group.

## Timing and the November reality

The literature moves between your search and the deadline: MICRO's October
program lands weeks before ISCA's November gate, and its papers are fair game for
reviewers to mention. Re-run the sweep in the final two weeks, scoped to the
newest MICRO/HPCA/ASPLOS programs and recent arXiv, and slot any hit into the
lineage paragraphs rather than bolting on a "recent work also..." afterthought.

## Section self-check

- [ ] dblp sweep done for ISCA + MICRO + HPCA + ASPLOS, last five years minimum,
      plus the idea family's origin papers regardless of age.
- [ ] Every close mechanism: lineage sentence + structural delta + evaluation
      treatment decided.
- [ ] Zero first-person self-citations; zero identifying URLs; references intact.
- [ ] Final-fortnight refresh completed against the newest sibling programs.

## Positioning output

```text
[Idea family + origin paper] <family, first-named-at venue/year>
[Closest 3 mechanisms] <name, venue/year, structural delta vs ours>
[Evaluation treatment] quantitative baseline: <which> · qualitative: <which>
[Concurrent-work watch] <arXiv/sibling-program hits from the final sweep>
[Blind-voice audit] first-person self-cites: 0 · identifying URLs: 0
```

Blinding rules and reference policy verified 2026-07-08 against the ISCA 2026
guidelines (`../../resources/official-source-map.md`); reconfirm for 2027 — 待核实.
