---
name: micro-related-work
description: Use when building a MICRO paper's related-work coverage and positioning — sweeping the four-venue architecture literature plus journals and industry disclosures, differentiating by mechanism structure and cost rather than by numbers, obeying MICRO's all-author citation format, and verifying venue attribution via dblp before citing.
---

# MICRO Related Work

At MICRO the related-work section is a *mechanism taxonomy*, not a bibliography
tour. Reviewers — who probably wrote some of the cited papers — check three things:
did you find the nearest mechanisms, do you know how yours differs structurally,
and did you compare against the right one in the evaluation.

## The five lanes to sweep

| Lane | Where it lives | What reviewers check |
|---|---|---|
| Direct ancestors of your mechanism | MICRO/ISCA/HPCA/ASPLOS, last ~5 years first, then classics | The named predecessor is in your evaluation, reimplemented (`micro-experiments`) |
| Same problem, different layer | ASPLOS, OSDI/SOSP, PLDI (software attacks on your bottleneck) | You explain why hardware is still warranted |
| Modeling & methodology you rely on | MICRO/ISCA tool papers (e.g., CACTI @ MICRO 2007, McPAT @ MICRO 2009), TACO/CAL journals | Versions cited match versions used |
| Industry disclosures | Hot Chips talks, ISSCC papers, patents, vendor optimization manuals | A shipped equivalent of your idea would be fatal to novelty — find it before reviewers do |
| Workload/characterization studies | IISWC, SIGMETRICS, arch venues | Your motivating characterization is consistent with published behavior |

The **industry lane is MICRO-distinctive**: commercial cores have shipped
sophisticated predictors and prefetchers for decades, often documented only in
patents and manuals. "Novel versus academia, present in Zen/M-series silicon" is a
real review outcome; a sentence acknowledging and differentiating from disclosed
industrial practice inoculates against it.

## Differentiate on structure and cost, not adjectives

Weak: "Unlike prior work, our approach is more efficient and scalable."
Strong, MICRO-shaped: "Both X [12] and our design track reuse at cache-line grain;
X spends 68KB on per-core tables and trains on evictions, while we piggyback on
existing replacement metadata (3.2KB) and train on fills, which is why we survive
the shared-LLC configs where X thrashes (Fig. 8)."

The pattern: **shared premise → structural difference → cost difference →
consequence shown in your own evaluation**. Every "nearest neighbor" paper deserves
one such sentence; the merely-adjacent get grouped citations.

## Venue attribution: verify before you cite

Architecture's four venues publish look-alike work; misattributing a classic is a
credibility wound with expert reviewers. Verify on dblp (or the ACM DL / IEEE
Xplore record) — MICRO's proceedings are split across both libraries, which makes
guessing extra unreliable:

```bash
# dblp API: confirm venue + year + pages before the entry goes in the .bib
curl -s "https://dblp.org/search/publ/api?q=utility-based+cache+partitioning&format=json" \
  | python3 -c "import json,sys; hits=json.load(sys.stdin)['result']['hits']['hit']; \
  [print(h['info'].get('venue'), h['info'].get('year'), h['info'].get('title')) for h in hits]"
# expect: MICRO 2006 — not ISCA, not HPCA
```

Classics that live *at MICRO* (dblp/ACM-DL verified 2026-07-08, see
`resources/exemplars/library.md`): two-level branch prediction (MICRO 1991),
utility-based cache partitioning (MICRO 2006), CACTI 6.0 (MICRO 2007), McPAT
(MICRO 2009), DaDianNao (MICRO 2014). Rowhammer and Wattch, by contrast, are ISCA
papers — the standard misattribution traps in this space.

## Handling your own preprints and prior papers

- **Your published prior mechanism** is cited in third person and, if it is the
  nearest neighbor, compared in the evaluation like anyone else's — reviewers
  notice a suspicious gap where the obvious predecessor comparison should be.
- **Your own arXiv preprint of this submission:** current-cycle policy on
  preprint coexistence with double-blind review is 待核实 on the live guidelines;
  do not cite it, and do not structure the paper so that finding it is necessary
  to evaluate the work.
- **Extended-abstract or workshop versions** (e.g., an IISWC characterization
  that seeded this mechanism): cite in third person, and be prepared to explain
  the delta in rebuttal if a reviewer connects them.

## Format and anonymity constraints on the section

- MICRO's reference format requires **every author named in every entry — no
  "et al."** — and reference pages are unlimited, so breadth costs no content
  space. There is no page-pressure excuse for a thin section.
- Double-blind: cite your own prior mechanisms in third person, and make the
  comparison genuine — an oddly gentle treatment of one citation is a de-anonymizing
  tell.
- Concurrent-work etiquette for the overlapping April/June cycles (how to treat a
  just-appeared ISCA paper): current-cycle policy 待核实; the safe default is to
  cite and position, since reviewers sit on both PCs and will know it exists.

## Timing the sweep

Run the literature sweep twice: once at project start (it shapes the mechanism —
finding the nearest neighbor early is cheaper than in review), and once in the
final month before the April deadline, because the November ISCA and February
HPCA programs land new neighbors mid-project. The second sweep is diff-only:
new papers in the five lanes since the first pass, each triaged to *cite*,
*differentiate*, or *reimplement-and-compare*.

## Building the section under MICRO's page economics

Because references are unlimited but content pages are scarce and appendix-free,
the winning structure is **dense prose, broad bibliography**:

1. Open with a two-sentence taxonomy of the mechanism space (the axes along which
   designs differ — training signal, storage grain, commitment point).
2. Spend one structural-difference sentence on each of the 3–5 nearest neighbors.
3. Group the rest by lane with clustered citations — ten grouped citations cost
   two lines of body text and zero content-page pressure.
4. Close by naming which neighbors appear in the evaluation and why the others
   cannot (different simulator assumptions, unavailable parameters) — preempting
   the "why didn't you compare against [23]?" review.

Keep a `positioning.md` in the artifact repo mapping each neighbor to its delta
sentence and its evaluation status; rebuttal season reuses it verbatim.

## Output format

```text
[Lane coverage] ancestors / other-layer / tools / industry / workloads: N citations each
[Nearest neighbors] <papers> — structural-difference sentence written: yes/no each
[Eval linkage] neighbors reimplemented in evaluation: list vs excuses
[Industry check] patents/manuals/HotChips swept for shipped equivalents: yes / no
[Attribution] all classics dblp-verified: yes / unverified list
[Format] all-author entries confirmed / et-al violations: N
```
