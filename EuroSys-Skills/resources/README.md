# EuroSys Resources

Working material behind the EuroSys skill pack. The `skills/` directory carries the advice;
this directory carries what the advice points at — verified sources, verified exemplar
papers, a style demonstration, and tooling adapters.

## Contents

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | Trace every cycle fact in the pack to an official URL with an access date, see the access-method workaround used during verification, and read the explicit 待核实 list. |
| [`external_tools.md`](external_tools.md) | Open the live official surfaces (CFP, HotCRP rounds, sysartifacts, eurosys.org, ACM DL, dblp) and run the five author-side passes before an upload. |
| [`exemplars/library.md`](exemplars/library.md) | Study award-verified EuroSys papers from Dryad (2007) to CacheBlend (2025), with self-checks and a do-not-misattribute list for the systems canon. |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a fictional systems abstract/introduction rebuilt into the EuroSys arc: pain → structural gap → insight → system → scoped numbers. |
| [`code/README.md`](code/README.md) | Adapt the shared reproducibility kit to EuroSys artifacts, plus the four venue-specific checks no generic tool covers. |

## Scope note

This is a systems-conference pack: the deliverables are a HotCRP submission, possibly a
one-shot revision, an ACM camera-ready, and a sysartifacts artifact. Do not import the
econometrics or journal-submission kits from elsewhere in the repository; the only shared
dependency is the generic experiment/artifact scaffolding referenced from `code/README.md`.

## Suggested route through the pack

1. Route the project with
   [`../skills/eurosys-topic-selection`](../skills/eurosys-topic-selection/SKILL.md), then
   time it with [`../skills/eurosys-workflow`](../skills/eurosys-workflow/SKILL.md).
2. Build evidence against
   [`../skills/eurosys-experiments`](../skills/eurosys-experiments/SKILL.md) and
   [`../skills/eurosys-reproducibility`](../skills/eurosys-reproducibility/SKILL.md),
   keeping the evaluation matrix under version control.
3. Draft with [`../skills/eurosys-writing-style`](../skills/eurosys-writing-style/SKILL.md)
   against the [worked example](worked-examples/01-introduction.md), and position with
   [`../skills/eurosys-related-work`](../skills/eurosys-related-work/SKILL.md).
4. Before upload, run [`../skills/eurosys-submission`](../skills/eurosys-submission/SKILL.md)
   and the passes in [`external_tools.md`](external_tools.md); confirm any date against
   [`official-source-map.md`](official-source-map.md).
5. After notification, branch per
   [`../skills/eurosys-review-process`](../skills/eurosys-review-process/SKILL.md) into
   response, camera-ready, and artifact work.
