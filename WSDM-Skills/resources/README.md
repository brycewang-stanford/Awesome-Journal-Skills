# WSDM Resources

Working materials behind the WSDM skill pack. The `skills/` directory holds the
advice; this directory holds what the advice stands on - verified sources, real
exemplar papers, a worked style rewrite, official links, and the shared
reproducibility tooling adapter.

## Contents

| File | Purpose |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Every official URL used to ground the pack, access-dated 2026-07-08, with the access-method disclosure (gateway-blocked domains verified via search renderings and cross-checks) and the full 待核实 register. |
| [`external_tools.md`](external_tools.md) | Live links an author needs during a WSDM cycle: conference sites, EasyChair, ACM DL, dblp, plus the per-cycle re-check list. |
| [`exemplars/library.md`](exemplars/library.md) | Five DOI-verified WSDM papers spanning the venue's lineages (click models, unbiased LTR, sequential recommendation, off-policy RL for recommendation, community detection), with self-check questions and a venue-misattribution guard list. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | A fictional before/after abstract+introduction rewrite into the WSDM register: behavior-first framing, bias-aware evaluation claims, self-containment for a no-rebuttal review. |
| [`code/README.md`](code/README.md) | Adapter to the repo-shared ML-conference reproducibility kit, with the WSDM-specific caveats (appendix-inclusive budget, log-data manifests). |

## Ground rules

- Nothing in this directory overrides a live official page. WSDM policies are
  edition-specific; the source map records what was true for which edition and
  when it was checked.
- The exemplar library is deliberately short and verified rather than long and
  guessed; add rows only with an ACM DL DOI or dblp record in hand.
- The worked example is fictional teaching material. Do not quote it in a
  manuscript.

## Suggested path through the pack

1. Fit first: [`../skills/wsdm-topic-selection`](../skills/wsdm-topic-selection/SKILL.md),
   sanity-checked against real venue output in [`exemplars/library.md`](exemplars/library.md).
2. Build evidence with [`../skills/wsdm-experiments`](../skills/wsdm-experiments/SKILL.md)
   and [`../skills/wsdm-reproducibility`](../skills/wsdm-reproducibility/SKILL.md),
   using [`code/README.md`](code/README.md) for the artifact smoke check.
3. Write with [`../skills/wsdm-writing-style`](../skills/wsdm-writing-style/SKILL.md)
   against the rewrite in [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
4. Before the August deadline, re-open every link in
   [`official-source-map.md`](official-source-map.md) and run
   [`../skills/wsdm-submission`](../skills/wsdm-submission/SKILL.md).
