---
name: mobisys-related-work
description: Use when positioning a MobiSys submission against the mobile-systems literature — offload, on-device ML, mobile OS and runtimes, sensing services, and energy — covering the right lanes, handling concurrent work, verifying that cited "MobiSys papers" are MobiSys rather than MobiCom/SenSys/OSDI, and self-citing without breaking double-blind.
---

# MobiSys Related Work

Use this to audit novelty and coverage. Reopen the current CFP for dual-submission,
anonymity, and prior-publication rules before advising authors. At MobiSys the failure mode is
usually a **too-narrow** related-work section that misses a sibling-venue predecessor.

## Positioning checks

- Separate the **system contribution** from an engineering improvement: a new runtime
  mechanism, scheduling policy, on-device inference system, sensing service, or platform.
- Cover the mobile-systems lanes below; a bibliography that cites only machine-learning papers
  tells a systems reviewer that known mobile-systems work may be getting rediscovered.
- Treat ACM DL, USENIX, and IEEE proceedings as archival unless current rules say otherwise.
- Cite arXiv and workshop versions in a way that preserves double-blind review; do not point
  reviewers to identity-revealing pages.
- Use related work to sharpen what is new: a tighter energy budget, a lower latency tail, an
  on-device capability that previously required the cloud, or a deployment others only
  simulated.

## Literature lanes to sweep

| Lane | Typical venues | What MobiSys reviewers check |
|---|---|---|
| Computation offload / edge | MobiSys, MobiCom, NSDI, EuroSys | Whether the nearest offload system is compared or distinguished |
| On-device ML systems | MobiSys, SenSys, MLSys, ASPLOS | Whether prior on-device runtimes/schedulers are acknowledged |
| Mobile OS / runtime | MobiSys, OSDI, SOSP, EuroSys | Whether the platform mechanism has an OS-systems predecessor |
| Mobile sensing / ubicomp | MobiSys, SenSys, IMWUT | Whether the sensing-service line is covered without misfiling |
| Energy / measurement | MobiSys, SenSys, IMC | Whether energy methodology follows established practice |

A related-work section that ignores the SenSys or OSDI predecessor of a mobile-systems idea is
a recognizable MobiSys reject pattern that no amount of on-device polish repairs.

## Venue-verification discipline

The mobile-systems canon is easy to misattribute because MobiSys, MobiCom, and SenSys share
the SIGMOBILE umbrella:

- Verify each cited "MobiSys paper" on the **ACM DL** and **dblp** by matching the
  `conf/mobisys` record; TaintDroid is OSDI, CenceMe is SenSys, RF-sensing classics are
  MobiCom/SIGCOMM (see [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md)).
- Do not cite a paper as MobiSys from memory; a misattributed venue signals careless
  scholarship to a specialist reviewer.

## Concurrent-work judgment calls

- Independently concurrent arXiv work: cite neutrally, state the technical difference, and
  avoid priority claims reviewers cannot verify.
- Your own workshop (e.g., HotMobile) version: typically non-archival and citable, but verify
  against the current CFP and phrase the citation so double-blind review survives.
- When in doubt about the archival status of a venue, declare the overlap in the submission
  form rather than gambling on a chair's interpretation.

## Positioning vignette

Imagine the paper proposes a thermal-aware on-device inference runtime. Its nearest neighbors:
an on-device DNN scheduler at MobiSys with no thermal model, a mobile-GPU inference framework
at MobiSys tuned for peak not sustained load, and an OS-level DVFS mechanism at OSDI. The
novelty sentence should name all three contrasts — thermal-awareness where the scheduler had
none, sustained-load stability where the GPU framework optimized peak, and application-level
control where the OS mechanism was generic.

## Output format

```text
[Eligibility] clear / needs declaration / risky
[Closest lanes] <offload / on-device ML / mobile OS / sensing / energy>
[Nearest 3 works] <work -> distinction>
[Venue-verification risk] <none / misattribution issues>
[Novelty sentence] <MobiSys-ready contribution contrast>
```
