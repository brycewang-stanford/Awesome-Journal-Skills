# SOSP Resources

Action-oriented companions to the `skills/`. The skills carry the advice; this
directory carries the reference material an agent needs to model a SOSP-shaped
paper, mine verified exemplars, confirm official rules, and stage a systems artifact
for post-acceptance evaluation.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every SOSP fact in this pack to its official URL and 2026-07-08 access date, see what is 待核实, and learn the gateway-blocked verification method. |
| [`external_tools.md`](external_tools.md) | Open the live venue systems — CFP, HotCRP, sysartifacts, ACM DL, SIGOPS Hall of Fame — with author-side checklists attached. |
| [`exemplars/library.md`](exemplars/library.md) | Position against verified real SOSP papers and dodge the OSDI/ATC misattribution traps that embarrass related-work sections. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | Watch a fictional systems paper's first page rebuilt into the SOSP problem-to-principle arc. No real-paper facts, no invented policy. |
| [`code/README.md`](code/README.md) | Adapt the repo-level ML-conference reproducibility kit to OS-level artifacts: environment pinning below userspace, claims maps, and sysartifacts badge staging. |

## Scope note

This is an ACM systems-conference pack. Its center of gravity is built-and-measured
operating-systems research: HotCRP mechanics, a PC-meeting review culture, shepherded
camera-readies, and sysartifacts badges. Do not import the econometrics kits from the
journal packs in this repository, and do not treat the shared ML kit's accuracy-table
assumptions as sufficient for kernel-level artifacts — the adaptations in
[`code/README.md`](code/README.md) exist precisely because a systems claim pins the
platform, not just the Python environment.

## Suggested workflow

1. Route the project with [`../skills/sosp-topic-selection`](../skills/sosp-topic-selection/SKILL.md)
   and place it on the annual calendar with [`../skills/sosp-workflow`](../skills/sosp-workflow/SKILL.md).
2. Design evidence early via [`../skills/sosp-experiments`](../skills/sosp-experiments/SKILL.md)
   and [`../skills/sosp-reproducibility`](../skills/sosp-reproducibility/SKILL.md),
   staging artifacts with [`code/README.md`](code/README.md).
3. Shape the paper against [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md),
   [`../skills/sosp-writing-style`](../skills/sosp-writing-style/SKILL.md), and the
   verified neighbors in [`exemplars/library.md`](exemplars/library.md).
4. Before anything deadline-sensitive, reopen the current cycle through
   [`official-source-map.md`](official-source-map.md) and
   [`external_tools.md`](external_tools.md) — every date in this pack is a
   2026-cycle anchor, not a law.
