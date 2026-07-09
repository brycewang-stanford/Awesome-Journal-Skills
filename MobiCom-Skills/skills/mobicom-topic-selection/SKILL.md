---
name: mobicom-topic-selection
description: Use when deciding whether a project belongs at MobiCom or a sibling venue — testing whether the core contribution is a mobile/wireless-networking mechanism the SIGMOBILE flagship rewards, and routing platform, sensing, broad-networking, security, or ubicomp misfits to MobiSys, SenSys, SIGCOMM/NSDI, WiSec, or IMWUT before a cycle is committed.
---

# MobiCom Topic Selection

MobiCom is the ACM SIGMOBILE flagship for **mobile computing and wireless networking** —
the radio, protocol, and mobility side of mobile. The fastest way to waste a rolling
deadline is to submit a paper whose real contribution belongs one venue over. This skill is
a **fit and routing** tool, not a substitute for the current CFP scope list.

## The fit test

A MobiCom-shaped paper answers all four:

1. **Is the contribution a wireless or mobile-networking mechanism?** A protocol, a
   link/PHY-MAC technique, a routing or scheduling method, an RF-sensing capability, a
   measurement finding about mobile networks — something in the networking stack, not an
   application that merely runs on a phone.
2. **Does the wireless/mobility condition matter to the result?** If the channel, spectrum,
   interference, or mobility could be abstracted away with no loss, the contribution is
   probably not MobiCom's.
3. **Is there over-the-air evidence, or a credible plan for it?** MobiCom expects real
   radios and testbeds; a simulation-only story is a fit risk (`mobicom-experiments`).
4. **Would MobiCom's reviewers be the right audience?** Say why in one sentence using the
   venue's own vocabulary, not "it is a top conference."

## Routing map

Route by **contribution type**, not prestige. The nearest siblings and what pulls a paper
to each:

| Signal in the contribution | Better-fit venue |
|---|---|
| End-to-end mobile/embedded platform, wearable, or mobile app system | ACM MobiSys |
| Sensing pipeline, ubiquitous/embedded sensing infrastructure | ACM SenSys |
| Broad Internet/measurement/data-center networking, congestion control | ACM SIGCOMM |
| Networked/distributed systems design and implementation at large | USENIX NSDI |
| Security or privacy of wireless/mobile as the central claim | ACM WiSec |
| Ubiquitous-computing / on-body inference as the finding | ACM IMWUT (UbiComp) |
| Early idea without full evaluation | HotMobile or a workshop |

The MobiCom↔MobiSys line is the one authors get wrong most: a **wireless/networking
mechanism** is MobiCom; an **end-to-end platform whose artifact behavior is the point** is
MobiSys. When both are present, decide which is the *contribution* and which is the vehicle.

## Contribution-type honesty

Name the contribution before choosing the venue:

```text
[Contribution type] protocol / PHY-MAC technique / routing / RF sensing /
                    measurement study / mobile-networking system / other
[Wireless dependence] does the result change if the channel/mobility is idealized? y/n
[Evidence form] testbed / SDR prototype / deployment / trace / simulation-only
[Primary audience] the MobiCom sub-community that should review it
```

If the type is "measurement study," MobiCom rewards a study that changes how the community
models a mobile network — not a dashboard of numbers. If it is "RF sensing," the wireless
mechanism must be the contribution, not just the medium (see WiSee in
[`../../resources/exemplars/library.md`](../../resources/exemplars/library.md)).

## Common misfit patterns

- **The phone-app paper.** Runs on mobile hardware but the novelty is an application or an
  ML model; the wireless stack is incidental → MobiSys, IMWUT, or a domain venue.
- **The pure-PHY paper.** A modulation or coding result with no networking or systems
  payoff → an information-theory or communications venue unless it changes a networked
  mechanism.
- **The simulation-only protocol.** A routing or scheduling idea evaluated only in a
  simulator; strong ones still need over-the-air or testbed evidence to clear the bar.
- **The broad-systems paper wearing a wireless hat.** A distributed-systems contribution
  with a mobile motivating example → NSDI/OSDI.

## Re-routing decision

If the paper misses MobiCom's bar, do not force it — re-route by type and record why. A
theory result goes to a theory venue, a platform to MobiSys, a measurement-heavy networking
study to SIGCOMM, an early idea to HotMobile. Re-routing early is cheaper than a rolling
deadline spent on a mismatch, and MobiCom's two-round review means a misfit often surfaces
as an early reject after round 1 rather than a rescue.

## Output format

```text
[Fit] High / Medium / Low (one-line reason in MobiCom's vocabulary)
[Contribution type] <named>
[Wireless dependence] result depends on channel/mobility? y/n
[Evidence form] testbed / SDR / deployment / trace / simulation-only
[Main gap] the single most important missing mechanism or measurement
[Re-route] <sibling venue if not a fit, with the signal that sends it there>
```
