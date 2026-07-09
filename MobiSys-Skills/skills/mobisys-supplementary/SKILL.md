---
name: mobisys-supplementary
description: Use when preparing MobiSys supplementary material — appendices, extra device sweeps, protocol details, demo video and media, and anonymized artifacts under the 12-page-body, double-blind, and reviewer-discretion constraints, including how to split a mobile-systems paper between body, references-and-appendix overflow, and HotCRP fields.
---

# MobiSys Supplementary

Use this when assembling MobiSys supplementary material. The supplement can support the paper,
but the 12-page double-column body must stand on its own — a reviewer may never open it.

## Supplement structure

- Put full protocols, extra device sweeps, additional ablations, and per-device tables in a
  clean appendix after the references (outside the 12-page cap).
- Put a **demo video or media** where the contribution is an interactive service or a
  user-facing behavior a static figure cannot convey; MobiSys work often lives or dies on the
  demo.
- Put executable assets in the artifact package rather than the appendix when the current
  HotCRP form separates them (`mobisys-artifact-evaluation`).
- Keep all supplementary files **double-blind**: no author names, institutions,
  acknowledgements, device serial numbers, account handles in screenshots, internal codenames,
  or repository owners in trace paths.
- Do not use the supplement to hide essential motivation, the core system description, the
  headline device results, or the key design decisions.
- Verify archives and media open on a clean machine, render without your account, and contain
  no credentials, caches, or hidden OS metadata.

## Body / appendix / media split

| Content | Where it goes | Why |
|---|---|---|
| System design, headline latency + energy figures, accuracy-cost table | 12-page body | The paper must be judgeable without the supplement |
| Full workload traces, per-device sweeps, extended ablations | Appendix after references | Supports the body under reviewer discretion |
| Interactive behavior, UI, real-time feel | Demo video/media | A CDF cannot show a user-facing service |
| Runnable code, scripts, model files | Artifact package | Evaluated by the AEC, not read as prose |

## Appendix architecture

- Order appendix sections to mirror the body's experiment order; systems reviewers navigate by
  figure and section number, not by page.
- Restate the setup before each extended result so the appendix reads standalone without
  flipping back to the double-column body.
- Cross-reference every appendix table and figure from the body at least once; orphaned
  supplement material is invisible under reviewer discretion.
- Keep the demo media short and self-explanatory; assume it is watched once, muted, at speed.

## Vignette: splitting an on-device runtime paper

A submission presenting a thermal-aware inference runtime, plus device studies: the body keeps
the design, the latency-under-load curve, the energy-per-frame figure, and the accuracy-cost
table; the appendix holds the four-device sweep and the full workload traces; a 90-second demo
video shows the frame rate holding as the phone heats; the artifact carries the runtime and
the measurement scripts. Nothing decision-critical lives only in the appendix or the video,
because both are discretionary.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Body/appendix/media split] <what sits where, gaps flagged>
[Files] <appendix / demo video / traces / artifact>
[Anonymity checks] <passed / issues incl. screenshots and trace paths>
[Main-paper dependency] <what breaks if the supplement is ignored>
```
