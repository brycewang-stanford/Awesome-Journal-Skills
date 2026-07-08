---
name: osdi-artifact-evaluation
description: Use when preparing an OSDI artifact for sysartifacts-run evaluation — the post-acceptance timeline, the 2026 narrowing to a single Artifacts Available badge, Zenodo-grade permanent archiving, the AE-committee runbook, and the two-page Artifact Appendix that documents the result.
---

# OSDI Artifact Evaluation

Package the system for the artifact evaluation committee (AEC). Everything
cycle-specific below is OSDI '26 as verified 2026-07-08 — and 2026 changed the rules,
so check the live Call for Artifacts (`usenix.org/conference/osdi26/call-for-artifacts`
pattern) before optimizing for the wrong target.

## How OSDI AE is wired

- **Who:** an AEC organized with the **sysartifacts** community
  (`sysartifacts.github.io`), which runs artifact evaluation across the systems
  conferences — reviewers are systems students and researchers on machines that are
  not yours.
- **When:** artifacts are submitted **after the paper is (conditionally) accepted** —
  the '26 deadline was **May 8, 2026, 8:59 pm PDT**, about six weeks after the
  March 26 notification. The chairs explicitly encouraged preparing the artifact
  while the paper was still under review; teams that ignored this spent April in a
  panic.
- **Stakes:** badges appear on the published paper. AE is optional but has become an
  expectation for systems papers claiming practical relevance — and it is the
  prerequisite for the final paper's two-page Artifact Appendix.

## The 2026 badge narrowing

| Cycle | Badges evaluated |
|---|---|
| OSDI '21–'25 (sysartifacts calls) | Artifacts Available, Artifacts Functional, Results Reproduced |
| **OSDI '26** | **Artifacts Available only** |

This is the pack's sharpest example of cycle volatility. In 2026 the AEC judged one
thing: that the artifacts have been **made available for retrieval, permanently and
publicly**. Zenodo was the encouraged host; institutional repositories and third-party
archives (FigShare, Dryad, Software Heritage, GitHub, GitLab) were acceptable.

Two disciplined responses:

1. **Meet the letter**: a permanent, resolvable archive — not a personal homepage, not
   a repo you might rename. Mint the DOI/permanent identifier before the deadline and
   put that identifier in the paper.
2. **Build to the historical bar anyway.** Functional/Reproduced may return in later
   cycles, your readers will attempt reproduction regardless (the proceedings are
   open access), and a runnable artifact is what makes the badge worth having. The
   structure below targets reproducibility even when only availability is graded.

## Artifact anatomy

```text
osdi26-artifact/                    # archived as one versioned unit (e.g. Zenodo)
├── README.md                       # THE document: claims map + kick-the-tires + full runs
├── LICENSE                         # explicit; AEC members must be allowed to run it
├── system/                         # source at the paper's commit, build instructions
├── baselines/                      # versions/tags, tuning configs, rebuild notes
├── workloads/                      # traces or regeneration scripts + provenance/licensing
├── experiments/                    # one driver per paper claim: run_fig7.sh, run_tab3.sh
├── expected/                       # reference outputs + tolerance notes (variance!)
├── ledger/                         # provenance records from osdi-reproducibility
└── environment/                    # container/VM image or exact setup script; hw requirements
```

The README's **claims map** is the heart: a table from paper claim (Fig. 7, Table 3,
"recovery under 900 ms") to driver script, expected output, tolerance, and runtime.
An evaluator should reach a first signal — the "kick-the-tires" path — in under 30
minutes on commodity hardware, even if headline experiments need a testbed.

## Systems-specific honesty

- **Hardware walls:** if a claim needs 64 nodes or specific NICs, say so at the top
  and provide a scaled-down mode that exercises every code path with reduced
  magnitudes; state which numbers the small mode can and cannot reproduce.
- **Variance:** publish tolerance windows per claim ("p99 within ±10% across 10
  runs"), sourced from your own ledger — an evaluator who gets 3.1x where the paper
  says 3.2x should find reassurance, not confusion.
- **Licensing traps:** production-derived traces often cannot be redistributed;
  include the generator plus provenance documentation, and say so plainly rather
  than shipping a mystery synthetic substitute.
- **De-anonymization timing:** AE runs post-acceptance, so the artifact need not be
  anonymous in 2026's flow — but verify this against the current call rather than
  assuming it, since submission-time AE exists at other systems venues.

## Working with the AEC

Artifact evaluation is a cooperative review, and the committee's constraints shape
what a good artifact looks like:

- Evaluators are typically graduate students and postdocs handling several artifacts
  in a fixed window — assume **limited time per artifact** and front-load the payoff:
  the fastest path from download to a verifiable signal wins goodwill that carries
  through the harder experiments.
- Expect a **communication channel** (the AE submission system) for questions during
  evaluation; answer fast and patch the README rather than replying inline, so the
  archived artifact ends evaluation better than it started. Where the archive is
  immutable (a minted DOI version), publish a new version rather than editing
  history.
- Provide **fallbacks per failure point**: a prebuilt container beside the
  build-from-source path, a small dataset beside the trace generator, expected logs
  beside every driver so a partial failure is diagnosable from output alone.
- If the badge set is availability-only (as in 2026), evaluators still need to
  *retrieve and inspect* the archive — a 40 GB tarball with no manifest can fail
  even that bar in practice. Ship a top-level manifest with sizes and checksums.

## From badge to Artifact Appendix

Papers passing evaluation may add up to **two pages** of Artifact Appendix to the
final paper (June 9 deadline, `osdi-camera-ready`): a standard-format description of
scope, requirements, and reproduction steps. Write it by condensing the README the
AEC just validated — it is the only reviewed-adjacent supplement OSDI has, and it
outlives the conference as the artifact's citable front door.

## Output format

```text
[Cycle badge set] confirmed from live Call for Artifacts: <list> (待核实 if unread)
[Archive] permanent host + identifier minted? <where / missing>
[Claims map] paper claims covered by drivers: <n/m>; kick-the-tires < 30 min? yes/no
[Hardware honesty] testbed requirements + scaled-down mode documented? yes/no
[Timeline] days to artifact deadline; README/expected-output gaps: <list>
```
