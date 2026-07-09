---
name: mobisys-topic-selection
description: Use when deciding whether a project belongs at MobiSys — testing whether the core contribution is a mobile or embedded system, application, or service whose on-device behavior is the result, and routing wireless, sensor-network, distributed-systems, ubicomp, or early-idea misfits to MobiCom, SenSys, NSDI/OSDI, IMWUT, or HotMobile.
---

# MobiSys Topic Selection

MobiSys is the ACM SIGMOBILE venue for **mobile systems, applications, and services** — the
system that runs *on* the device, not the radio underneath it. The fastest way to waste a
year-long cycle is to submit a paper whose real contribution belongs one venue over. This
skill is a **fit and routing** tool, not a substitute for the current CFP scope list.

## The fit test

A MobiSys-shaped paper answers all four:

1. **Is the contribution a mobile or embedded *system*?** A runtime, an OS/platform mechanism,
   an on-device inference engine, a sensing pipeline, an offload scheduler, a mobile
   application or service — something built and run on the device, not an algorithm evaluated
   in the abstract.
2. **Does the device constraint shape the result?** If compute, energy, latency, memory, or
   thermal budget could be idealized away with no loss, the contribution is probably not
   MobiSys's.
3. **Is there on-device evidence, or a credible plan for it?** MobiSys expects real phones,
   wearables, or embedded boards; a simulation-only story is a fit risk
   (`mobisys-experiments`).
4. **Would MobiSys's systems-and-services reviewers be the right audience?** Say why in one
   sentence using the venue's vocabulary, not "it is a top conference."

## Routing map

Route by **contribution type**, not prestige. The nearest siblings and what pulls a paper to
each:

| Signal in the contribution | Better-fit venue |
|---|---|
| Wireless/PHY-MAC mechanism, protocol, or RF sensing as the core | ACM MobiCom |
| Sensor-network / embedded-sensing infrastructure at large | ACM SenSys |
| Data-center, cloud, or distributed-systems design and implementation | USENIX NSDI / OSDI |
| Operating-system generality beyond mobile | USENIX OSDI / ACM SOSP |
| Ubiquitous-computing / on-body inference as the *finding* | ACM IMWUT (UbiComp) |
| Security or privacy of mobile as the central claim | a security venue |
| Early idea without a full on-device evaluation | HotMobile or a workshop |

The **MobiSys↔MobiCom line** is the one authors get wrong most: a **wireless mechanism** is
MobiCom; an **end-to-end mobile system whose device behavior is the point** is MobiSys. The
**MobiSys↔SenSys line** is the second: a **sensing infrastructure** is SenSys; a **mobile
platform, app, or service** built on sensing is MobiSys. When two are present, decide which
is the *contribution* and which is the vehicle.

## Contribution-type honesty

Name the contribution before choosing the venue:

```text
[Contribution type] mobile runtime / OS-platform mechanism / on-device ML system /
                    sensing service / offload scheduler / mobile app-service / other
[Device dependence] does the result change if compute/energy/latency is idealized? y/n
[Evidence form] real-device measurement / deployment / user study / trace / simulation-only
[Primary audience] the MobiSys sub-community that should review it
```

If the type is "on-device ML system," MobiSys rewards a **resource-management or runtime**
contribution (scheduling, approximation, placement, thermal control), not a better model — a
new architecture with mobile motivation routes to a machine-learning venue. If it is "sensing
service," the mobile system and its on-device budget must be the contribution, not just the
sensor.

## Common misfit patterns

- **The better-model paper.** A more accurate network that happens to run on a phone; the
  system is incidental → a machine-learning venue, unless the runtime is the contribution.
- **The wireless paper wearing a systems hat.** A link/PHY result with a phone demo → MobiCom.
- **The sensor-network paper.** A multi-node embedded-sensing infrastructure → SenSys.
- **The simulation-only system.** A scheduler or runtime evaluated only in a simulator; strong
  ones still need on-device measurement to clear the bar.
- **The distributed-systems paper with a mobile example.** A cloud/back-end contribution with
  a mobile motivating scenario → NSDI/OSDI.

## Re-routing decision

If the paper misses MobiSys's bar, do not force it into the December deadline — re-route by
type and record why. A wireless mechanism goes to MobiCom, a sensing infrastructure to SenSys,
a distributed-systems design to NSDI/OSDI, a ubicomp finding to IMWUT, an early idea to
HotMobile. Because MobiSys runs one deadline a year, a misfit costs a full cycle, and the
two-round review often surfaces it as an early reject after round 1 rather than a rescue —
re-routing early is by far the cheaper move.

## Output format

```text
[Fit] High / Medium / Low (one-line reason in MobiSys's vocabulary)
[Contribution type] <named>
[Device dependence] result depends on compute/energy/latency/memory? y/n
[Evidence form] real-device / deployment / user study / trace / simulation-only
[Main gap] the single most important missing system mechanism or measurement
[Re-route] <sibling venue if not a fit, with the signal that sends it there>
```
