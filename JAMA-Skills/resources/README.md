# JAMA Resources

Action-oriented resources for the *JAMA* (Journal of the American Medical Association)
skill pack. The `skills/` give advice; this directory lets an agent **act** — model a
JAMA-style structured abstract and Introduction, and benchmark against verified exemplars.
Pair these with the relevant [`../skills/jama-*/SKILL.md`](../skills/).

## What's here

| Resource | Use it to... |
| --- | --- |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of a JAMA clinical-research **structured abstract + Key Points box + Introduction** in JAMA house style (Importance / Objective / Design, Setting, and Participants / … ; CONSORT for trials, STROBE for observational; spin removed). Illustrative **fictional** study; derived only from this pack's own skills. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified JAMA papers** organized by topic × design. Design positioning only — no fabricated numbers. Verified access date 2026-06-08. |
| [`external_tools.md`](external_tools.md) | Reporting guidelines (EQUATOR: CONSORT/STROBE/PRISMA/STARD), trial/protocol registries, statistical software, AMA-style reference tools, and figure/integrity utilities referenced by the pack. |

## Scope note: clinical-medicine venue, no econometric code kit

JAMA is a **clinical-medicine** journal. Accordingly, this pack deliberately **does not
vendor** the econometrics / causal-inference code kit (Stata + Python DID/IV/RDD/DML
pipeline) that the economics packs carry — it is the wrong methodology for this venue.
The clinical-research toolchain (EQUATOR reporting guidelines, registries, survival /
meta-analysis / multiple-imputation software, AMA style) lives in
[`external_tools.md`](external_tools.md) instead. There is **no `code/` directory** here by
design.

## JAMA-specific policy source

A venue-specific **`official-source-map.md`** (authoritative JAMA submission, data-sharing,
and editorial-policy facts, plus a do-not-misattribute list) is the intended home for
JAMA-specific policy. **It is not yet present in this directory** — until it is added, do
**not** cite JAMA-specific limits, fees, editors, or policy from memory; verify everything
against JAMA's official **Instructions for Authors** and the ICMJE Recommendations (see the
notes in [`external_tools.md`](external_tools.md)). When `official-source-map.md` is added,
link it from the table above.

## Suggested workflow

1. **Scope & design.** Lock the design and a single pre-specified primary outcome with
   [`../skills/jama-scope-fit`](../skills/jama-scope-fit/SKILL.md) and
   [`../skills/jama-study-design`](../skills/jama-study-design/SKILL.md).
2. **Reporting standard.** Map the design to its EQUATOR checklist and flow diagram with
   [`../skills/jama-reporting-standards`](../skills/jama-reporting-standards/SKILL.md); see
   the guideline table in [`external_tools.md`](external_tools.md).
3. **Write the front matter.** Model the structured abstract, Key Points box, and
   Introduction on [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md),
   guided by [`../skills/jama-structured-abstract`](../skills/jama-structured-abstract/SKILL.md).
4. **Polish & de-spin.** Tighten prose and remove spin with
   [`../skills/jama-writing-style`](../skills/jama-writing-style/SKILL.md).
5. **Benchmark.** Compare your design against the verified papers in
   [`exemplars/library.md`](exemplars/library.md) — confirming, as that file does, that each
   target is *JAMA* itself and not a sibling venue (NEJM, The Lancet, BMJ, or a JAMA Network
   specialty journal).
