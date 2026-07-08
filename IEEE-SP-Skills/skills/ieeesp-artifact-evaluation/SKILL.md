---
name: ieeesp-artifact-evaluation
description: Use when preparing an IEEE S&P (Oakland) artifact-evaluation submission after acceptance, including choosing among the Available, Functional, and Results Reproduced badges, DOI-backed deposits, packaging exploits and malware-adjacent code responsibly, and scoping what evaluators can actually re-run.
---

# IEEE S&P Artifact Evaluation

Use this once a paper is accepted and the team is deciding whether and how to
enter artifact evaluation. At S&P, AE is a **post-acceptance opt-in** run by a
separate committee against three badges (sp2026.ieee-security.org
/cfartifacts.html, checked 2026-07-08); the 2027 schedule and any badge
changes were unpublished at check time — 待核实 on the current AE pages.

## The three badges are three different projects

| Badge | What it certifies | The actual work |
|---|---|---|
| **Available** | Artifact permanently deposited with a DOI (Zenodo, FigShare, Dryad — not a lab webpage or GitHub alone) | Deposit hygiene: license, README, versioned snapshot |
| **Functional** | Evaluators exercised the artifact per your instructions | Environment capture + scripted entry points that run elsewhere |
| **Results Reproduced** | Evaluators regenerated the paper's key results | Claim-to-command map with tolerances and runtimes |

Pick badges by what an outsider can genuinely re-run. A measurement study of
live infrastructure can honestly target Available (data + analysis code) even
when Reproduced is impossible; overclaiming a badge wastes the committee's
goodwill and your response cycles.

## Security artifacts have handling constraints others do not

- **Exploit code**: release what supports the scientific claim; gate or stub
  weaponization details when fixes are not universally deployed, and say so
  in the README. Align with the paper's disclosure timeline — an artifact
  should not out-run the patch.
- **Malware corpora**: ship hashes plus a documented retrieval path rather
  than live binaries; if binaries are necessary, password-protected archives
  with an explicit handling warning are the community norm.
- **Vulnerable targets**: containerize the intentionally-vulnerable service
  so an evaluator cannot accidentally expose it; never require the evaluator
  to scan or attack third-party infrastructure.
- **Datasets with user data**: only what the paper's ethics record covers —
  the AE deposit is public forever.

## Packaging for a stranger with a deadline

Evaluators run many artifacts in a fixed window. Optimize for their first
thirty minutes:

```text
artifact/
├── README.md            # claims table (below), requirements, total runtime
├── LICENSE
├── Dockerfile           # or VM image reference; pin versions incl. kernel
│                        #   if the attack is kernel-sensitive
├── setup.sh             # one command; no sudo surprises undocumented
├── run_minimal.sh       # <30 min smoke path exercising every component
├── run_full.sh          # regenerates paper numbers; prints ETA up front
└── expected/            # reference outputs + tolerance notes

README claims table:
| Paper claim | Command | Expected output | Time |
| Table 3 attack success | ./run_full.sh t3 | success ≥ 0.9 ± noise note | 2 h |
| Fig 5 overhead curve   | ./run_full.sh f5 | CSV within ±5% of expected/ | 40 m |
```

Hardware honesty matters more at S&P than most venues: microarchitectural
attacks, timing channels, and TEE work are CPU-stepping-sensitive. State the
exact tested hardware and what changes off it — "results reproduced on
different silicon may differ in <way>" is a credibility line, not a
weakness.

## Process notes

- Register for AE in the acceptance-notification window; the AE calendar runs
  in parallel with camera-ready and both compete for the same author-weeks.
- Expect an interactive phase where evaluators file issues; respond with
  fixes to the artifact, not prose reassurance.
- The badge outcome is independent of the paper's acceptance — a failed AE
  does not un-accept the paper, but badges print on the published version.
- Keep the deposited DOI version identical to what evaluators approved.

## Failure modes specific to this venue

- A "working" exploit that assumed the lab's exact microcode/patch level —
  pin and document, or downgrade the badge target.
- Disclosure conflict: artifact published before coordinated-disclosure
  clocks expire.
- The AE README assumes security-tool literacy the committee may not have
  (e.g., unstated familiarity with a specific fuzzer's corpus format).
- Zenodo deposit made from the wrong branch after camera-ready edits.

## Output format

```text
[AE decision] opt in: yes/no — badge targets: Available / Functional / Reproduced
[Rerunnability audit] <what an outsider can actually regenerate>
[Handling constraints] exploit gating / malware packaging / user data: <plan>
[Hardware sensitivity] <exact platform + expected drift off-platform>
[Schedule] AE registration <date 待核实> vs camera-ready <date> — conflict?
```
