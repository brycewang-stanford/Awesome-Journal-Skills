---
name: nsdi-reproducibility
description: Use when making an NSDI paper's results reconstructible — capturing testbed topology, trace provenance, and configuration while experiments run, planning which datasets can ship publicly, and keeping the paper and artifact from drifting apart so badge evaluation and the Community Award stay reachable.
---

# NSDI Reproducibility

A networked-systems result is a function of topology, traffic, timing, and code — and
three of those four are absent from the PDF unless deliberately recorded. NSDI
rewards the discipline institutionally: artifact badges after acceptance and a
**Community Award** for the best paper whose code and/or dataset is public by the
final-papers deadline. But the work happens during the experiments, not after the
decision email.

## The four provenance ledgers

Keep each as a versioned file next to the results it explains:

| Ledger | Contents | Loss mode it prevents |
|---|---|---|
| Topology | node specs, NIC/switch models, link speeds, RTT matrix, kernel + NIC settings | "worked on our cluster," unreproducible knee points |
| Traffic | trace source + collection context, scaling/anonymization transforms, synthetic-generator parameters + seeds | headline numbers tied to data nobody can regenerate |
| Configuration | every config diff from defaults, per system **and per baseline** | untuned-baseline accusations you cannot rebut |
| Run | per-experiment: commit hash, config snapshot, fault schedule, raw-log location, analysis-script hash | figures that cannot be regenerated at revision time |

The run ledger has a second life NSDI makes unusually likely: a **one-shot revision**
letter can demand new measurements on the same setup, 3-4 months after submission,
at a subsequent deadline. Teams with ledgers rerun in days; teams without them
rebuild the testbed from memory.

## Determinism is different here

Unlike ML reproducibility, networked-systems results are legitimately
non-deterministic — background load, timer jitter, and cross-traffic vary. The honest
posture is not "identical numbers" but **characterized variance**:

- Fix what can be fixed: seeds for generators and fault schedules, pinned software
  versions, isolated or documented-shared testbeds.
- Measure what cannot: repeat headline experiments across days/trace slices; publish
  the spread with the artifact so an evaluator knows a 7% delta is noise, not
  failure.
- Timestamp everything; time-of-day and neighbor effects are real explanations, but
  only if recorded.

## What can actually ship?

Decide per data item *before* the camera-ready crunch, because the answer shapes the
paper's claims:

1. **Public now** — code, synthetic generators, testbed configs, analysis scripts.
   Default to shipping.
2. **Public after transformation** — production-derived traces that can be
   anonymized/aggregated. Document the transform and what properties it preserves;
   state in the paper that released traces differ from raw ones.
3. **Never public** — proprietary traces, customer data. Plan the fallback: a
   synthetic workload with matched characteristics, shipped alongside a fidelity
   note. Do not let a never-public trace be the *only* support for a headline claim
   if a shippable proxy can corroborate it.

Anonymize the artifact itself for review-time supplements (repo owners, hostnames,
paths, company strings in configs); de-anonymize only at final-paper time.

## Wiring it into the repo

```bash
# Layout that keeps paper and artifact from drifting
experiments/
  <exp-id>/run.sh          # topology + config + fault schedule, self-describing
  <exp-id>/provenance.json # commit, trace id, seeds, dates, operator
figures/
  Makefile                 # every paper figure regenerated from raw logs:
                           #   make fig6 -> pulls exp logs, runs analysis, emits PDF
paper/
  claims.md                # claim -> exp-id -> figure mapping, reviewed at freeze
```

The `claims.md` cross-map is the cheapest anti-drift device: at submission freeze,
walk it once; any claim whose exp-id is stale gets rerun or reworded. The shared
smoke-checker
([`../../resources/code/README.md`](../../resources/code/README.md)) covers package
hygiene but not topology/trace fidelity — those checks are yours.

## Blind now, open later

Reproducibility material crosses the double-blind boundary twice, and each crossing
has a checklist:

- **At submission** (if any package is uploaded as auxiliary material): scrub
  repository owners, commit-author emails, hostnames that embed the institution,
  and license files naming the organization; keep the scrubbed and true versions as
  separate branches so de-anonymization is a merge, not a rewrite.
- **At final papers**: flip to the public, attributed release — DOI'd archive,
  real repository, institutional acknowledgment — dated **before** the final-papers
  deadline if the Community Award matters (`nsdi-camera-ready`).

## Cheap wins ordered by payoff

1. `provenance.json` per experiment, written by the runner script (an hour to
   automate).
2. Figure Makefile with raw-log inputs (removes an entire class of revision pain).
3. Baseline config diffs recorded (rebuts the most common reviewer attack).
4. Variance characterization for the two headline results.
5. Early legal check on trace release — licensing takes longer than deadline gaps.

## Signs the discipline is slipping

- A figure in the draft that nobody can regenerate this week.
- "The good run" language — selecting runs by outcome rather than by protocol.
- Baseline numbers copied forward from an earlier paper draft instead of re-measured
  on the current topology.
- Testbed changes (kernel upgrade, NIC swap) mid-campaign without a ledger entry
  splitting before/after results.

Any one of these, found at submission freeze, costs days; found by an artifact
evaluator or a revision reviewer, it costs the result's credibility.

## Output format

```text
[Ledger status] topology / traffic / configuration / run — each present/partial/absent
[Variance] headline results with characterized spread? which lack repeats?
[Shippability] data items -> public / transformable / never (fallback named)
[Drift check] claims.md walked? stale claim list
[Award posture] on track for public code+data by final-papers deadline? 
[Next actions] ordered by payoff-per-hour
```
