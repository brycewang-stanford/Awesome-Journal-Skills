---
name: ndss-experiments
description: Use when designing or auditing the evaluation of an NDSS paper — attack demonstrations, defense evaluations under adaptive adversaries, and Internet measurements — choosing between testbed, emulation, and live experiments and meeting NDSS's deployment-realism evidence bar.
---

# NDSS Experiments

Evidence at NDSS answers one question: *would this hold on the real network?* Every design
choice in the evaluation — target selection, vantage, scale, baseline — either supports
that answer or advertises that you avoided it.

## Evidence by contribution type

| You claim... | Reviewers require... | Weak substitute they will flag |
| --- | --- | --- |
| A new attack | End-to-end demonstration on real implementations, named versions, measured preconditions and cost | PoC against a config you weakened |
| A prevalent condition | Defined population, sampling method, validated vulnerability test, false-positive analysis | Extrapolation from anecdotes |
| A defense | Security *and* utility: adaptive-adversary evaluation + overhead on realistic workloads | Blocking only the published attack |
| A detection system | Base-rate honest metrics on traffic resembling deployment, drift discussion | Accuracy on one stale benchmark |
| A protocol change | Interop and incremental-deployment story, behavior under partial adoption | "Assume everyone upgrades" |

## Choosing the experimental substrate

Match the substrate to the claim, and say why in the paper:

- **Live Internet** — the only substrate for prevalence claims. Requires the ethics
  machinery (below) and a recorded snapshot: measurement results are time-indexed facts, so
  log the observation window, vantage points, and population source.
- **Testbed / physical devices** — for exploit reliability and defense overhead, where you
  need ground truth and repeatability. Pin firmware, kernel, and topology; a testbed nobody
  can reconstruct is an anecdote with racks.
- **Emulation / simulation** — legitimate for scale sweeps and what-if topologies *after*
  the mechanism is shown real elsewhere. A paper whose only evidence is simulated packets
  is, at this venue, a proposal.

Mixed designs are the norm: demonstrate on real systems, generalize on the testbed, sweep
in emulation, and keep the chain of custody between the three explicit.

## The adaptive-adversary requirement

For defenses, the reviewer's first move is to play attacker against your design. Do it
first, in print:

1. Restate the defense as the constraint it imposes on the adversary.
2. Enumerate strategies that respect capabilities from the threat model but target the
   mechanism itself — evasion, mimicry, resource exhaustion, downgrade, oracle abuse.
3. Implement the strongest of these, not the most convenient, and report where the defense
   bends. Cost asymmetry (defender cents vs. attacker weeks) is a legitimate result;
   silence about adaptation is not.

## Measurement hygiene

- One vantage point is a case study; state how many you used and what each can and cannot
  see (anycast, geo-blocking, and CDN behavior all bite here).
- Validate the classifier or vulnerability test against labeled ground truth and report
  both error directions — a scanner's false positives *are* the headline number's error bar.
- Repeat over time before claiming stability; the Internet's diurnal and patch-cycle
  rhythms confound single-shot scans.

## Ethics as an experimental parameter

Live experiments are bounded by harm, and the CFP backs this with an Ethics Review Board.
Design limits in from the start: rate caps and opt-out honoring for scans, no serving of
real user traffic during interception experiments, synthetic victims wherever the
demonstration allows, notification pipelines for anything you confirm exploitable, and IRB
engagement where humans are observed — while remembering NDSS treats IRB sign-off as
necessary context, not sufficient mitigation. Every one of these choices belongs in the
paper's method text, not only in the ethics section.

## Reporting discipline

```text
For every headline number, the text or appendix must pin:
  target set + versions + selection method
  vantage(s) and observation window
  trials, variance, and the aggregation rule
  hardware/software of the measurement or attack host
  configuration deltas from defaults (ideally: none, or justified)
  the command or procedure that regenerates the number (→ artifact)
```

Numbers that move between runs get intervals; comparisons against baselines get identical
conditions or an explanation of why identity was impossible.

## Failure modes this venue punishes

- Evaluating on the environment you developed on, and nowhere else.
- Baselines run with defaults while your system got tuning.
- Success rates without denominators; "up to X" as a summary statistic.
- Prevalence claims from a population chosen because it was scannable, described as if it
  were representative.

## Output format

```text
[Claim → evidence map] each headline claim + substrate + status
[Adaptive evaluation] strategies enumerated / strongest implemented / result
[Measurement validity] population, vantage, validation, error directions
[Ethics parameters] rate caps, synthetic victims, notification, IRB state
[Repro pinning] items from the reporting block still missing
```
