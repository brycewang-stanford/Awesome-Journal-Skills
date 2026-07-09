> **Illustrative teaching example.** The study, dataset, vantage points, and every number below
> are **fictional** and exist only to demonstrate IMC house style. No real-paper facts, networks,
> or results are stated, and no policy is invented. Corresponding skills:
> [`imc-writing-style`](../../skills/imc-writing-style/SKILL.md),
> [`imc-topic-selection`](../../skills/imc-topic-selection/SKILL.md), and
> [`imc-experiments`](../../skills/imc-experiments/SKILL.md).

# Worked Example: An IMC-Style Abstract + Introduction (before → after)

This demonstrates the **IMC first-page arc** from `imc-writing-style`:
**a question about the real Internet → why current knowledge is inadequate → the measurement and
its vantage points → what the data show → what it means for operators/the community** — with the
IMC expectations that the contribution is a *measurement* contribution, the evidence comes from
**credible, dated vantage points**, and a **limitations-and-ethics** posture is visible from the
start (not bolted on at the end).

The framing also reflects `imc-topic-selection`: IMC is strongest when the lesson is about **how
the deployed Internet actually behaves** — here, whether a censorship-circumvention protocol is
reliably reachable in the wild — rather than a new system whose evaluation is incidental (which
would route to NSDI or SIGCOMM), and when the study could not simply be re-labeled as a systems
paper without loss.

**Illustrative paper (fictional):** *"Reachable When It Matters? A Multi-Vantage-Point Measurement
of a Circumvention Protocol Under Real Network Conditions."* Fictional artifact: a released dataset
of reachability probes from volunteer and cloud vantage points, plus the measurement tooling.

---

## Before (buries the measurement contribution — typical first-draft abstract + intro)

> **Abstract.** Internet censorship is a growing problem. We build a new circumvention system that
> uses an obfuscated transport and evaluate it, showing it achieves high throughput and low
> latency in our experiments. Our results demonstrate that the system is effective and outperforms
> prior approaches.
>
> **Introduction.** Censorship is bad and circumvention is important. Many systems exist. We built
> a system and ran experiments from our university and a cloud VM, and it works well. Section 2
> covers related work, Section 3 the system, Section 4 the evaluation, Section 5 discussion, and
> Section 6 concludes.

**What's wrong (against `imc-writing-style` / `imc-topic-selection` / `imc-experiments`):**

- **No measurement question about the real Internet on the first page** — it leads with a system
  and a throughput win, not with a question about how the deployed network behaves. IMC wants the
  measurement finding up front.
- **Two vantage points is not a measurement study.** "Our university and a cloud VM" cannot support
  a claim about reachability *in the wild*; the reader cannot tell whether the result generalizes
  across networks, regions, or time.
- **No temporal dimension.** Reachability of a circumvention protocol is a moving target; a single
  snapshot says nothing about stability, and IMC reviewers read for longitudinal awareness.
- **System-as-contribution.** If the framing is "we built a better system," the model-swap analog
  fails: this reads as an NSDI/SIGCOMM systems paper wearing a measurement title
  (`imc-topic-selection` re-route signal).
- **No ethics posture** — active probing that could expose volunteers or trip censorship
  infrastructure is exactly what IMC's mandatory Ethics section governs, and it is absent.
- **No dataset or availability story** — an IMC reviewer looks for the artifact-availability
  declaration immediately.

---

## After (IMC arc — question → inadequacy → measurement + vantage points → findings → meaning)

> **Abstract.** Circumvention protocols are judged in the lab, but what matters to a user is
> whether the protocol is **reachable from their network, at the moment they need it**. It is
> unknown how reachability varies across networks, regions, and time in the deployed Internet. We
> measure the reachability of one widely deployed obfuscated transport from **1,240 vantage points
> across 63 networks in 14 regions over 12 weeks** (a mix of volunteer endpoints and cloud
> probes), using a safety-reviewed active-probing method. We find that reachability is **highly
> bimodal and unstable**: many networks are reliably open while a minority oscillate on a diurnal
> cycle, and a small set of middleboxes accounts for a disproportionate share of failures
> (measurements reported with confidence intervals; per-vantage-point coverage and the probing
> safety design are documented). We release the reachability dataset, the vantage-point metadata,
> and the measurement tooling. *(question → inadequacy → measurement + vantage points → finding →
> release — all on the first page.)*
>
> **Introduction.** *(¶1 — the measurement question, first breath.)* For a user behind a
> filtering network, a circumvention protocol that benchmarks well in a lab is worthless if it is
> **unreachable from their vantage point when they open their laptop**. The engineering question
> is therefore not "how fast is the transport?" but **"how reachable is it across real networks
> and across time, and what explains the failures?"**
>
> *(¶2 — why current knowledge is inadequate.)* Prior evaluations measure throughput and latency
> from a handful of controlled hosts. Those are **properties of a testbed, not of the deployed
> Internet**: they cannot reveal how reachability differs between a mobile carrier and a campus
> network, whether it degrades at peak hours, or which network elements cause blocking. No prior
> study measures reachability at vantage-point and temporal breadth sufficient to answer the
> question a user actually has.
>
> *(¶3 — the measurement, stated as the contribution.)* We contribute a **multi-vantage-point
> reachability measurement** of the protocol: a dated, longitudinal dataset from 63 networks with
> documented probe placement, plus an analysis attributing failures to network conditions and
> specific middlebox behaviors. The tooling and the (privacy-reviewed) dataset are released for
> reuse.
>
> *(¶4 — findings tied to vantage points, each claim paired.)* We tie every claim to evidence:
> reachability rates carry per-network confidence intervals (Table 1); the diurnal oscillation is
> shown across the 12-week window with the vantage points that exhibit it (Fig. 2); and the
> middlebox attribution is supported by controlled follow-up probes whose safety design is stated
> (§4.3). We are explicit about coverage: our volunteer vantage points over-represent some regions,
> a bias we quantify rather than hide.
>
> *(¶5 — limitations, ethics, and what it means.)* We state the central limitations plainly:
> vantage-point sampling is **non-uniform**, and reachability observed by our probes is a proxy for
> what a real user's client would see. Our **Ethics** section (summarized here, detailed in the
> appendix) documents the safety review of active probing, the steps taken to avoid exposing
> volunteers or harming intermediary networks, and the responsible-disclosure path for the
> middlebox findings. The payoff is concrete: circumvention designers can target the networks and
> times where reachability actually fails, and the released dataset lets others track it as the
> Internet changes. Section 2 details the measurement design; findings are discussed alongside
> their vantage-point caveats, not deferred. *(brief roadmap, no over-signposting.)*

---

## Why the "after" meets the IMC bar

Mapped to the skill checklists:

- **Measurement question on the first page** — the abstract and ¶1 pose a question about the
  deployed Internet before any system detail (`imc-writing-style`: "lead with the measurement
  finding").
- **Credible, dated vantage points** — the claim is about reachability in the wild, so the
  evidence is breadth across networks/regions and depth across 12 weeks, with per-vantage-point
  coverage stated (`imc-experiments`: match the evidence to a claim about the real network).
- **Longitudinal awareness** — the diurnal instability is a temporal finding, not a snapshot, and
  the moving-Internet caveat is engaged (`imc-experiments`).
- **Right venue, measurement-first** — the lesson (reachability is bimodal and middlebox-driven)
  survives swapping the specific transport, so it is an IMC contribution, not a systems re-route
  (`imc-topic-selection`).
- **Ethics as a gate, engaged early** — active-probing safety, volunteer protection, and
  responsible disclosure are named in ¶5 and detailed in the mandatory Ethics appendix
  (`imc-submission`, `imc-experiments`).
- **Availability by default** — the dataset, vantage-point metadata, and tooling are released,
  matching the artifact-availability declaration and putting the paper in range of the Community
  Contribution Award (`imc-reproducibility`, `imc-artifact-evaluation`).

> Next: see [`../exemplars/library.md`](../exemplars/library.md) for **real, web-verified IMC
> papers** whose first pages execute this arc, and
> [`../official-source-map.md`](../official-source-map.md) for IMC-specific submission policy and
> the two-deadline cycle model.
