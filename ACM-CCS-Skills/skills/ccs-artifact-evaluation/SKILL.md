---
name: ccs-artifact-evaluation
description: Use when packaging ACM CCS artifacts for the artifact-evaluation committee and the ACM badges — Artifacts Available, Artifacts Evaluated Functional, Artifacts Evaluated Reusable, and Results Reproduced — covering what security evaluators inspect, how to make attacks and defenses turnkey, and how to justify withheld artifacts.
---

# CCS Artifact Evaluation

Use this for artifact packaging around CCS. CCS runs an optional artifact-evaluation process
after acceptance; passing artifacts earn ACM badges that appear on the paper's first page.
Reopen the current call for artifacts for the exact badge set, submission form, and deadlines.

## The ACM badge ladder

| Badge | What it certifies | What the committee does |
|---|---|---|
| Artifacts Available | The artifact is publicly archived with a stable identifier | Confirms the artifact is retrievable and permanent |
| Artifacts Evaluated - Functional | The artifact runs and does what the paper says | Executes it against the documented steps |
| Artifacts Evaluated - Reusable | It exceeds functional quality and others can reuse it | Judges structure, documentation, and reusability |
| Results Reproduced | The main paper results are independently reproduced | Reruns experiments and checks they support the claims |

Available is about archival permanence; Functional and Reusable are about quality; Results
Reproduced is the highest bar and requires the committee to regenerate your headline numbers.

## Artifact plan

- Decide which claims the artifact must support: the exploit, the defense overhead, the
  measurement pipeline, or the protocol implementation.
- Make the security claim turnkey: one documented command per headline result, with expected
  output, runtime, and the hardware assumed.
- Anonymize nothing at this stage — artifact evaluation is post-acceptance and single-blind or
  open — but do pin versions, dependencies, and a container so it runs on a clean machine.
- For dangerous artifacts (working exploits, malware, live attack tooling), gate access,
  document safe-handling, and follow the responsible-disclosure posture from the paper.
- Justify anything withheld: licensing, disclosure embargo, subject safety, or premature-release
  risk, and offer partial, synthetic, or redacted substitutes that still let evaluators check
  the method.

## What security evaluators open first

| Claim type | First artifact inspected | Common failure caught |
|---|---|---|
| Exploit against real software | The PoC and its target build instructions | Target version unspecified; PoC fails to build |
| Defense with overhead numbers | The benchmark runner and instrumented build | Overhead cannot be reproduced; workload undocumented |
| Measurement study | The collection and classification scripts | Classification rule differs from the paper's prose |
| Cryptographic implementation | Test vectors and the reference build | No test vectors; outputs cannot be checked |

## Worked vignette: packaging a fuzzing-tool artifact

A hypothetical accepted paper presents a new fuzzer that found N bugs. For Reusable and
Results Reproduced: ship a container pinning the fuzzer, the target corpus, and the seed set;
document one command to reproduce a representative crash and one to rerun a bounded campaign;
provide the bug list with disclosure status; and note which crashes are embargoed pending
vendor patches, offering redacted reproducers for those.

## Output format

```text
[Target badges] available / functional / reusable / results-reproduced
[Contents] <code / data / container / test vectors / logs>
[Turnkey level] one-command / scripted / descriptive / weak
[Safe-handling] <gating and disclosure posture for dangerous artifacts>
[Withheld-and-justified] <what and why, with substitute offered>
[Fixes before submission] <ordered list>
```
