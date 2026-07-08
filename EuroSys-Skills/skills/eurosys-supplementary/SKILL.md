---
name: eurosys-supplementary
description: Use when deciding what lives outside a EuroSys paper's 12 technical pages — free reference pages, whether the current round permits appendices or supplementary uploads, anonymized artifact repositories linked from the submission, and extended technical reports — without moving decision-critical evidence out of the reviewed pages.
---

# EuroSys Supplementary

Use this when a EuroSys draft overflows its 12 pages of technical content. The
governing fact (EuroSys 2027 CFP, rendered 2026-07-08): the budget is 12 pages
of technical content **plus unlimited reference pages**. Whether the current
round accepts appendices beyond the references, or a separate supplementary
upload in HotCRP, is per-cycle policy that was not verifiable on 2026-07-08 —
待核实 in the live CFP and the HotCRP submission form before relying on either.

## The four shelves

| Shelf | Review status | What belongs there |
|---|---|---|
| 12 technical pages | Fully reviewed, the paper | Design, key mechanisms, headline evaluation, honest limitations |
| Reference pages | Free, always allowed | Bibliography only — never technical content disguised as notes |
| Anonymized artifact repo | Reviewer-optional | Code, configs, full result sets, extra graphs, raw logs |
| Extended tech report / appendix | Only if the round permits (待核实) | Proofs, protocol details, exhaustive parameter sweeps |

The iron rule across all shelves: **a reviewer who reads only the 12 pages must
be able to accept the paper.** Anything reviewer-optional is corroboration, not
argument. If the claim's only support sits on shelf 3 or 4, the claim is
unsupported at decision time.

## What systems reviewers push outward — and what they don't

Safe to externalize:

- Full configuration dumps and tuning grids behind a summarized sensitivity plot.
- Per-benchmark breakdowns when the body shows the aggregate plus the outliers.
- Formal-model details for a mechanism whose intuition the body already conveys.
- Additional workloads that repeat, rather than extend, the body's conclusion.

Dangerous to externalize at EuroSys:

- The baseline-fairness evidence (versions, tuning) — its absence from the body
  reads as concealment, the single most corrosive suspicion in systems review.
- The one experiment that tests the design's stated weakness.
- Failure-handling behavior for a system whose pitch is reliability.

## Anonymized repository mechanics

When linking supporting material from a double-blind submission:

```bash
# Build an identity-clean mirror rather than sanitizing in place
git clone --depth 1 file:///lab/systemX systemX-anon && cd systemX-anon
rm -rf .git && grep -rInE 'university|lab-name|@|githubusercontent' . | less
# fix hits, then publish to an anonymous host (e.g., an anonymized-repo service)
```

- Strip commit history entirely; author fields in old commits are the classic leak.
- Check config files and comments for hostnames, cluster names, and usernames.
- Keep the mirror frozen during review so reviewers see one consistent state.

## Reference-page hygiene

The unlimited reference allowance is generous, not lawless:

- Bibliography pages hold citations — footnote essays, extended tables, or
  "notes" sections smuggled after the references invite a compliance read
  of the whole paper.
- Cite the version that supports the claim: a versioned release or paper,
  not a bare project homepage that will drift.
- Under double-blind, reference entries for your own artifacts must not
  resolve to identifying URLs; cite the anonymized mirror during review.
- Long URLs and dataset citations belong in the bibliography, where they
  are free, rather than inline where they spend technical-page budget.

## Micro-example: a 13.5-page draft

A distributed-tracing paper is 1.5 pages over. The cuts that worked, in
order of pain: the second motivating scenario compressed to two sentences
(0.4 pages); three per-workload latency plots collapsed into one CDF panel
with the full set moved to the artifact repository (0.5 pages); the
formal-consistency argument reduced to its statement plus intuition, full
treatment in the repo's design note (0.4 pages); prose narration of Figure 4
deleted because the caption already said it (0.2 pages). Nothing reviewers
needed for the accept/reject call left the body — that is the test each cut
must pass.

## Overflow triage, in order

1. Compress prose before cutting content — systems drafts carry 10–15% slack in
   restated motivations and figure narration.
2. Merge figures that make one point; delete figures that make none.
3. Move corroborating (not load-bearing) material to the artifact repo with a
   one-line pointer in the body.
4. Only then consider an appendix or tech report, after confirming the round's
   policy (待核实) and remembering reviewers owe it nothing.

## Coordination with the review timeline

- Whatever optional material accompanies the submission must be final at
  the paper gate; there is no mid-review update channel, and a stale repo
  contradicting the PDF is worse than no repo.
- If a rebuttal phase exists, it cannot introduce a new supplement —
  externalized material must already be in place to be pointed at.
- A one-shot revision, by contrast, is a full resubmission: the revised
  round is the moment to promote material inward (e.g., a boundary
  experiment the conditions demanded) rather than to grow the repo.

## Output format

```text
[Page pressure] <current overflow in pages>
[Shelf plan] <item -> body / references / artifact repo / appendix-if-allowed>
[Decision-critical check] <claims whose evidence would leave the body: none / list>
[Anonymity status of repo] <clean / leaks found>
[待核实] <does this round allow appendices or supplementary uploads?>
```
