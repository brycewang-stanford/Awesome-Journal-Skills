---
name: ipsn-review-process
description: Use when reasoning about how an IPSN-lineage submission is evaluated, covering double-blind review, the per-track (IP / SPOTS) program committees, the rebuttal, Best Paper and Best Research Artifact judging, and how IPSN's process differs from SenSys's revision model, OpenReview venues, and CPS-IoT Week neighbors.
---

# IPSN Review Process

Model the pipeline before interpreting any single review. IPSN's process is **double-blind,
per-track, and conference-style** (not journal-style): a submission is read by a program committee
matched to its track — **IP** or **SPOTS** — and returns an accept/reject decision, usually with a
rebuttal opportunity. Because IPSN merged into **SenSys**, confirm the successor's exact mechanics on
the current call; the structure below is the IPSN-lineage model and what to expect.

## Process model

- Submission and review run on **HotCRP** with **double-blind** anonymity: author identities are
  hidden from reviewers and reviewer identities from authors.
- Papers are matched to reviewers **by track**. An **IP-track** paper is read by method reviewers
  (estimation, signal processing, learning, localization); a **SPOTS-track** paper by
  platform/systems reviewers (hardware, embedded software, tools, deployment). This is why the track
  choice in `ipsn-submission` matters so much.
- Reviewers weigh: the **soundness** of the information-processing method or platform design; whether
  the **evidence is real** (real sensors, ground truth, measured energy/latency, honest deployment
  numbers); **novelty** against the sensing literature; and **reproducibility / artifact** support.
- A **rebuttal** typically lets authors correct factual misreadings before the decision (verify the
  window and format on the current call).
- Accepted papers appeared in **both ACM DL and IEEE Xplore**; the successor publishes regular papers
  in the **ACM** proceedings and demos/posters in the **IEEE** proceedings.

## What each track's reviewers check first

| Track | Reviewer's first question | Common reject trigger |
|---|---|---|
| IP | Is the estimator/inference sound, and is the baseline fair? | Simulation-only, or a proxy metric standing in for the real sensing outcome |
| SPOTS | Is the platform/tool reusable, and are the design trade-offs measured? | A one-off build with a datasheet but no measured power/robustness story |
| Either (deployment) | Are the real-world hardships reported honestly? | Yield, synchronization, and energy numbers missing or idealized |

## Reading a decision against the criteria

| Signal in the reviews | What it means | Author move |
|---|---|---|
| "Only simulated / no real hardware" | Evidence-realism doubt (fatal at IPSN) | If possible add a real-sensor result in rebuttal; otherwise reroute |
| "Baseline is not a real alternative / untuned" | Soundness doubt | Add or justify a fair baseline; report the comparison |
| "Deployment numbers look idealized" | Honesty/realism doubt | Report yield, sync error, energy as measured, with limits |
| "Artifact would strengthen this" | Reproducibility gap | Commit to (and anonymize) a firmware+dataset artifact |
| "Wrong track / out of scope" | Track or venue mismatch | Hard to fix in rebuttal; a `ipsn-topic-selection` lesson for next time |

## How IPSN differs from its neighbors and successor

- **vs. SenSys (pre-merger):** SenSys is the sibling embedded-networked-sensing flagship; IPSN's
  distinctive move was the **IP/SPOTS split** and its **information-processing/estimation** flavor.
  Post-merger the two communities share one venue — but an IP-track *style* paper is still judged on
  its estimation/inference soundness.
- **vs. OpenReview ML venues:** IPSN is not open-review, not score-thread public, and not
  leaderboard-driven. Offline accuracy on a clean dataset does not carry a paper here; on-device or
  in-field evidence does.
- **vs. CPS-IoT Week neighbors (RTAS/HSCC/ICCPS):** those reviewers want timing guarantees, control
  theory, or hybrid-systems verification. An IPSN paper is judged on sensing/information-processing
  soundness and real measurement, not worst-case schedulability.

## Where author leverage actually exists

```text
[Before submission]  track choice + topic tags -> reviewer pool           (largest lever)
[Initial reviews]    factual corrections, a real-hardware number a reviewer said was missing
[Rebuttal]           narrow, evidence-backed answers to soundness/realism doubts
[After reject]       no journal-style guaranteed revision round; reroute or resubmit next cycle
```

A rebuttal moves borderline papers when it corrects a misread table or supplies a measured number a
reviewer flagged; it does not move papers that argue taste or promise experiments not yet run.

## Best Paper and Best Research Artifact judging

IPSN gave a **Best Paper Award** and a **Best Research Artifact Award**. The artifact award is a
distinct incentive: a firmware+dataset package that an evaluator can actually run and reuse is judged
on more than the paper's claims. Target it deliberately (`ipsn-artifact-evaluation`) — verify whether
it persists under the successor (待核实).

## Misreadings to avoid

- **Expecting a journal-style Major Revision** — IPSN is conference-style accept/reject with a
  rebuttal, not a guaranteed revise-and-resubmit round (unlike a journal or a Major-Revision venue).
- **Treating the rebuttal as a debate** — the PC discussion decides; the rebuttal is evidence for an
  advocate, not a closing argument.
- **Assuming the successor keeps IPSN's exact mechanics** — the merged SenSys may differ; confirm.

## Output format

```text
[Process stage] pre-submission / awaiting reviews / rebuttal / decision / accepted
[Track] IP / SPOTS (or successor category)
[Criterion map] each review point -> soundness | evidence-realism | novelty | reproducibility | track-fit
[Leverage plan] the next-stage action that can actually change the outcome
[Forbidden moves] identity leak / unrun experiments promised as done / arguing taste
```
