---
name: ndss-reproducibility
description: Use when making an NDSS paper's results reconstructible — snapshotting live-network observations, pinning testbeds and toolchains, scrubbing traces that carry identities, and writing honest availability statements when ethics or vendor embargoes limit release.
---

# NDSS Reproducibility

Network-security results decay: targets patch, providers change behavior, botnets die, and
the population you measured in August is not the population of next March. Reproducibility
at NDSS therefore means two different promises, and conflating them is the classic mistake:

1. **Reconstruction** — anyone can re-derive your numbers from what you recorded.
2. **Re-execution** — anyone can re-run your pipeline against the world and get *their*
   numbers, understanding why they differ from yours.

Promise (1) unconditionally. Promise (2) only where the world cooperates.

## Freezing the measured world

| Volatile thing | What to freeze at experiment time |
| --- | --- |
| Scanned population | Input list + source + retrieval date; per-target response snapshots |
| Target software | Exact versions, build hashes, config files; patch level on the test date |
| Network path | Vantage descriptions, traceroute-level context where relevant, ASN of probes |
| Testbed | Topology file, firmware images (or their hashes), kernel/NIC settings |
| Toolchain | Container image or lockfile for every analysis script; seeds for anything sampled |
| Third-party feeds | Copies (or hashes + dates) of blocklists, zone files, certificate logs used |

The snapshot habit converts "trust us, it was exploitable in July 2026" into an auditable
record — which is also what the rebuttal will need when a reviewer asks whether the fix
released in September invalidates the paper.

## Traces are radioactive

Packet captures, flow logs, DNS transcripts, and crawl outputs embed user identities,
internal hostnames, and your institution's fingerprints — an anonymity leak against
double-blind review *and* a privacy harm on release. Rules that hold up:

- Scrub at capture time, not release time; a raw pcap on a laptop is a liability, not an
  asset.
- Prefix-preserving IP anonymization where analysis needs structure; deletion where it
  does not. Document which was applied — reviewers of measurement work will check.
- Replace real victim traffic with regenerated synthetic equivalents whenever the result
  tolerates it, and say so.
- Grep every release candidate for institutional domains, usernames, and cloud-account
  identifiers before it leaves the repo.

## The claims ledger

Maintain, from the first experiment, a machine-checkable mapping between paper claims and
regeneration paths:

```yaml
# claims.yml — one entry per number/figure the paper depends on
fig4_takeover_success:
  claim: "takeover succeeds against configs A-C"
  inputs: [snapshots/2026-07-scan/, configs/targets.yml]
  command: "make fig4"          # runs inside container ndss-artifact:v3
  runtime: "35 min, no network" # replays recorded traces
  status: verified 2026-07-05
prevalence_table2:
  claim: "condition present in N/M sampled domains"
  inputs: [snapshots/2026-06-population.csv.gz]
  command: "make table2"
  status: verified 2026-07-02
```

If a claim has no entry, either add the pipeline or soften the claim. The ledger later
becomes the artifact-evaluation appendix almost verbatim (see `ndss-artifact-evaluation`).

## Honest availability statements

Some NDSS work legitimately cannot release everything: unpatched-exploit details under
embargo, traces that cannot be de-identified, vendor NDAs. The venue's culture accepts
limits that are *named and mitigated*, not gestured at:

- State precisely what is withheld, why, and until when (e.g., "exploit module released
  after the coordinated-disclosure window closes").
- Ship the largest safe substitute: redacted configs, synthetic traces with matched
  statistics, the analysis code even when the data stays private.
- Never write "code available upon request" as the entire plan — at this venue it reads as
  "not available".

Because NDSS proceedings are open access (Internet Society model, no paywall), your
artifact link and the paper will be read together by the whole community; the availability
statement is a public commitment, not review-stage decoration.

## Cheap habits that pay at rebuttal time

- Date-stamp every scan directory; the timeline question always comes.
- Re-run the full pipeline from clean checkout monthly during the project — drift found
  early is drift fixed cheaply.
- Keep one `LIMITS.md` recording every known non-determinism (timing-sensitive exploits,
  load-dependent measurements) and how the paper's statistics absorb it.

## Output format

```text
[Reconstruction status] claims with regeneration paths: N/M; missing listed
[World snapshot] frozen / partial / absent per volatile category
[Trace hygiene] scrub method, leak grep result, synthetic substitutions
[Availability statement] withheld items + reason + mitigation + release date
[Drift check] last clean-checkout rerun date and result
```
