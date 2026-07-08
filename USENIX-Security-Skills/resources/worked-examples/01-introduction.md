> **Illustrative teaching example.** The paper, system, datasets, vulnerability, vendor,
> and every number in this file are **invented** to demonstrate USENIX Security first-page
> craft. No real paper is paraphrased, no real flaw is described, and no venue policy is
> stated here beyond what [`../official-source-map.md`](../official-source-map.md) verifies.
> Companion skills: [`usenixsec-writing-style`](../../skills/usenixsec-writing-style/SKILL.md),
> [`usenixsec-topic-selection`](../../skills/usenixsec-topic-selection/SKILL.md),
> [`usenixsec-experiments`](../../skills/usenixsec-experiments/SKILL.md).

# Worked Example: A USENIX Security Abstract + Introduction (before → after)

The exercise: take a first-draft opening for a security-measurement paper and rebuild
it to the USENIX Security bar — the threat model or vantage stated up front, claims
calibrated with populations and dispersion, the responsible-conduct thread visible, and
every claim wired to an experiment a reviewer can locate. The venue's instincts
(threat-model realism, measurement validity, ethics as a gate, auditable evidence) are
the grading rubric throughout.

**Fictional paper:** *"AnchorScan: Measuring Certificate-Pinning Bypass Exposure Across
the Mobile App Ecosystem."* Invented study: an internet-scale measurement of how many
mobile apps ship certificate-pinning configurations that a network adversary can
silently disable, combined with a disclosure campaign to the affected developers.

---

## Before (a typical first draft)

> **Abstract.** Certificate pinning is an important security mechanism. However, many
> apps implement it incorrectly. We present AnchorScan, a novel framework for detecting
> pinning bypass vulnerabilities at scale. Using AnchorScan, we scanned a large number
> of apps and found that a significant fraction are vulnerable. Our results show that
> pinning bypass is a widespread problem that urgently needs to be addressed.
>
> **Introduction.** Mobile security is a critical concern in today's world. Certificate
> pinning is widely used to prevent man-in-the-middle attacks. Unfortunately, developers
> often make mistakes. In this paper, we build a powerful tool to automatically find
> these mistakes across many apps. Our contributions are threefold: (1) a novel
> detection framework; (2) a large-scale measurement; (3) extensive analysis showing the
> problem is severe.

**Why this fails the USENIX Security rubric:**

- **No threat model.** "Man-in-the-middle" is named but never scoped — which adversary,
  what network position, what capability? A security reviewer cannot judge the finding
  without it (`usenixsec-writing-style`).
- **No vantage or validity statement.** "Scanned a large number of apps" hides the
  population, the time window, and what the measurement cannot see — the first thing
  measurement reviewers probe (`usenixsec-experiments`).
- **Uncalibrated superlatives** ("significant fraction", "widespread", "severe") with no
  number, no base rate, no dispersion — fails the backing bar in the abstract itself.
- **No ethics thread.** A scan-and-disclose study with zero mention of scan conduct or
  disclosure signals the Ethical Considerations appendix will be an afterthought — a
  review-visible risk at this venue (`usenixsec-topic-selection`).
- **Marketing vocabulary** ("powerful tool", "novel framework") where the auditable
  measurement, not the framework, should be the protagonist.

---

## After (rebuilt to the USENIX Security bar)

> **Abstract.** We measure how many Android apps ship certificate-pinning configurations
> that a **local network adversary** (Section 3 threat model: on-path, no device
> compromise, holds a CA trusted by the OS store) can silently disable. AnchorScan
> statically extracts pinning configurations and confirms bypassability dynamically
> against an instrumented proxy. Applied to the 41,000 most-installed free apps on a
> single store snapshot (March 2026; Section 4 states what this vantage excludes), 12.4%
> (5,084 apps; 95% CI 11.9-12.9% over 5 re-runs) accept our substituted certificate;
> 3.1% do so despite declaring pinning, indicating a config that is present but
> ineffective. We disclosed to all 5,084 developers 90 days before submission
> (Section 8); 41% had responded and 18% shipped a fix by the camera-ready date. Code,
> the (de-identified) app-hash list, and the proxy harness are available (Open Science
> appendix).
>
> **Introduction.** *(¶1 — problem and adversary.)* Certificate pinning is only a defense
> against the adversary it is configured to stop; we ask, at ecosystem scale, against a
> concretely specified local network adversary, how often shipped pinning actually holds.
> *(¶2 — gap, named per prior approach.)* Prior app-security scans report the *presence*
> of pinning APIs; presence is not efficacy, and dynamic confirmation at scale has been
> limited to hundreds of apps (Section 2). *(¶3 — contribution and vantage.)* AnchorScan
> combines static extraction with dynamic confirmation, and we report results with the
> vantage stated: one store, one region, one snapshot, free apps only — Section 4
> quantifies each restriction's effect on the estimate. *(¶4 — evidence map.)* The
> detection pipeline is validated against a 200-app hand-labeled ground truth (Section 5,
> precision/recall reported); the ecosystem measurement is Section 6; a base-rate and
> false-positive analysis is Section 6.3. *(¶5 — ethics and scope.)* Section 8 documents
> scan rate limits, the coordinated 90-day disclosure, and IRB consultation; we claim
> nothing about iOS or paid apps, and we do not release exploit tooling.

---

## What changed, instinct by instinct

| Reviewer instinct | Before | After |
|---|---|---|
| Threat-model realism | "man-in-the-middle" | On-path local adversary, capabilities and non-goals stated (Section 3) |
| Measurement validity | "a large number of apps" | 41,000 apps, one snapshot, vantage restrictions quantified (Section 4) |
| Backing | "significant fraction" | 12.4% with CI over re-runs, plus the presence-vs-efficacy split |
| Ethics as a gate | absent | Rate limits, 90-day disclosure with outcomes, IRB — in the abstract and body |
| Auditable evidence | "powerful tool" | Ground-truth validation + released code, hash list, and harness |

Three transferable moves: (1) the **efficacy-not-presence reframing** — measuring
whether the defense *works*, not whether the API is *called*, is what turns a scan into
a security finding; (2) the **vantage confession** — naming exactly what one snapshot
cannot see disarms the measurement reviewer's strongest objection in advance; (3) the
**disclosure narrative in the abstract** — putting the 90-day timeline and response
rates on page 1 shows the ethics gate was cleared before a reviewer has to ask.

> Next: benchmark against the real, verified USENIX Security papers in
> [`../exemplars/library.md`](../exemplars/library.md), and re-check current submission
> mechanics in [`../official-source-map.md`](../official-source-map.md) before acting.
