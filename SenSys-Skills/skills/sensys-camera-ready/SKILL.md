---
name: sensys-camera-ready
description: Use when preparing an accepted SenSys camera-ready — de-anonymizing the double-column ACM final, completing ACM rights and metadata, restoring acknowledgments, landing the awarded ACM artifact badges onto the paper, releasing traces and firmware within their constraints, and planning the in-person talk and demo for the merged audience.
---

# SenSys Camera-Ready

Acceptance flips the paper from anonymous-under-review to a permanent ACM DL record. The
camera-ready is a checklist of irreversible steps: de-anonymize completely, get the ACM rights and
metadata exactly right, land any artifact badges onto the printed paper, and prepare to present to
a room that now spans the merged SenSys/IPSN/IoTDI communities. A metadata or rights slip here is
corrected only by a painful post-publication erratum.

## De-anonymize completely

Everything double-blind suppressed now goes back — and nothing may be missed:

```text
[ ] Author names, affiliations, and emails restored on the paper.
[ ] Acknowledgments and funding/grant numbers added back.
[ ] Self-citations returned to first person where natural.
[ ] Artifact links de-blinded to their permanent public homes (with DOIs).
[ ] PDF metadata now correctly names authors (was scrubbed for review).
```

Run the inverse of the submission blindness sweep: the risk now is an *un*-restored acknowledgment
or a still-anonymized repo link, not a leak.

## ACM rights and metadata

The ACM e-rights process gates the final. Complete it precisely:

| Item | Action | Failure cost |
|---|---|---|
| e-rights form | Choose the license/transfer the process offers; get the exact **rights text + DOI** | Wrong rights block on the PDF |
| Rights stamp | Paste ACM's rights text and conference string verbatim into the template | Reprint / erratum |
| Author metadata | Names, affiliations, ORCIDs match the form and the PDF | ACM DL record errors |
| Title/abstract | Match the accepted paper exactly | Indexing mismatch |
| Template version | Use the ACM double-column version the CFP names (待核实 per cycle) | Production rejection |

Extra camera-ready pages are sometimes granted for reviewer-requested additions; confirm the exact
allowance for the cycle before spending them.

## Coordinate the artifact badges onto the paper

If you pursued badges (`sensys-artifact-evaluation`), the camera-ready is where awarded badges are
attached to the printed paper and the ACM DL metadata. Confirm:

```text
[ ] Each awarded badge (Available / Functional / Reproduced) appears on the final PDF.
[ ] The permanent artifact DOI in the paper matches the archived deposit.
[ ] Released traces/firmware honor their consent/NDA/location constraints (sensys-reproducibility).
[ ] The public repo README maps claims → the script/trace that reproduces each figure.
```

Do not release sensor data, firmware, or deployment locations you have not cleared — the public
release is permanent.

## Plan the talk and demo

SenSys is in-person; presenting to the merged audience means a room with sensor-networks, embedded,
IoT, and on-device-AI expertise all present:

- **Lead with the physical problem**, not the architecture — the same first-page arc as the paper
  (`sensys-writing-style`), compressed to a few minutes.
- **Show the measurement**, not just the claim: a power trace or a latency CDF lands harder than a
  bullet saying "efficient."
- **A live or recorded demo** of the node/deployment is unusually persuasive at SenSys; if you
  demo, rehearse the failure modes (a dead battery on stage is avoidable).
- **Anticipate the merged audience's questions**: an IPSN-rooted reviewer asks about the protocol;
  an IoTDI-rooted one about deployment; an embedded-AI one about footprint. Have all three ready.

## Final camera-ready sequence

```text
1. De-anonymize fully; inverse blindness sweep passes.
2. ACM e-rights complete; rights text + DOI stamped verbatim in the template.
3. Metadata (authors, ORCIDs, title, abstract) matches the form and PDF.
4. Awarded badges + artifact DOI on the final PDF; public release cleared.
5. Compile in the correct template version; re-read the produced PDF.
6. Talk + demo built from the measured-behavior arc; merged-audience Q&A prepared.
```

## Output format

```text
[Deanon]   de-anonymization complete? un-restored items listed
[Rights]   ACM e-rights done; rights text + DOI stamped — pass/gap
[Metadata] authors/ORCIDs/title/abstract consistent across form and PDF
[Badges]   awarded badges + artifact DOI on the final; release cleared
[Talk]     talk/demo built from the measured-behavior arc; Q&A ready
[Open]     the one irreversible item still unconfirmed before the deadline
```
