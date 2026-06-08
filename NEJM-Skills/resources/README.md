# NEJM Resources

Action-oriented resources for the *New England Journal of Medicine* (NEJM) skill pack. The `skills/` give
advice; this directory lets an agent **act** — model an NEJM-style abstract and introduction, and benchmark
against verified NEJM exemplars. Pair these with the relevant `skills/nejm-*/SKILL.md`.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a clinical-trial **structured abstract** (Background/Methods/Results/Conclusions) and a terse IMRAD **introduction** in NEJM house style — CONSORT-aligned, registration and funding stated, effect size + 95% CI led. Illustrative **fictional** trial; invents no clinical fact. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified NEJM papers** organized by topic × design (RCT superiority / non-inferiority / vaccine / platform, plus a review article). Design positioning only — no fabricated numbers. Includes a sibling-confusion guard (NEJM ≠ Lancet / JAMA / BMJ / Annals). |
| [`official-source-map.md`](external_tools.md) | **NEJM-specific policy & facts:** Author Center submission, structured-abstract and length/reference caps, ICMJE/CONSORT enforcement, data-sharing policy, editors/scope, and a do-not-misattribute list. The authoritative pack source. *(Planned index target — add this file to complete the map; not yet present in this pack.)* |
| [`external_tools.md`](external_tools.md) | External registries, reporting-standard checklists (EQUATOR/CONSORT/STROBE/PRISMA), statistics software, and references used when preparing an NEJM manuscript. |

## No econometric code kit here — this is a clinical venue

NEJM is a **clinical-medicine** journal. The repo's vendored **econometric / causal-inference code kit**
(Stata + Python DID / IV / RDD / DML pipeline used by the economics packs) is **deliberately not vendored
into this pack** — it is the wrong toolchain for clinical-trial reporting. Instead, this pack follows the
clinical-research standards, and an agent should reach for those rather than an econometrics pipeline:

- **CONSORT** (with the participant flow diagram) for randomized trials, **STROBE** for observational
  studies, **PRISMA** for systematic reviews — see [`../skills/nejm-reporting/SKILL.md`](../skills/nejm-reporting/SKILL.md)
  and the EQUATOR links in [`external_tools.md`](external_tools.md).
- **ICMJE** recommendations for registration, authorship, disclosures, and the data-sharing statement — see
  [`../skills/nejm-study-design/SKILL.md`](../skills/nejm-study-design/SKILL.md) and
  [`../skills/nejm-ethics/SKILL.md`](../skills/nejm-ethics/SKILL.md).
- **NEJM clinical statistical reporting** (confidence intervals over bare P values, ITT primary analysis,
  multiplicity control, absolute risk + NNT) — see [`../skills/nejm-statistics/SKILL.md`](../skills/nejm-statistics/SKILL.md).

## Suggested workflow

1. Confirm design rigor and **prospective registration / protocol / SAP** with
   [`../skills/nejm-study-design/SKILL.md`](../skills/nejm-study-design/SKILL.md); clear ethics, disclosures,
   and the data-sharing statement with [`../skills/nejm-ethics/SKILL.md`](../skills/nejm-ethics/SKILL.md).
2. Pick and build the reporting checklist + flow diagram with
   [`../skills/nejm-reporting/SKILL.md`](../skills/nejm-reporting/SKILL.md) (CONSORT for RCTs).
3. Write terse IMRAD with [`../skills/nejm-writing/SKILL.md`](../skills/nejm-writing/SKILL.md) and enforce the
   statistical reporting with [`../skills/nejm-statistics/SKILL.md`](../skills/nejm-statistics/SKILL.md);
   model the abstract and introduction on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md).
4. Polish the **structured abstract** with [`../skills/nejm-abstract/SKILL.md`](../skills/nejm-abstract/SKILL.md).
5. Benchmark against verified NEJM papers in [`exemplars/library.md`](exemplars/library.md); confirm
   submission and policy details in [`official-source-map.md`](external_tools.md) (when present) and the
   [NEJM Author Center](https://www.nejm.org/author-center).
