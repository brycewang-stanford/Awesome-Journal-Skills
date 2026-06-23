# PNAS Nexus Resources

Action-oriented resources for the *PNAS Nexus* skill pack. The `skills/` give advice; this directory
lets an agent **model** PNAS-Nexus-specific front matter and **ground** every venue fact in a verified
source-of-record. Pair these with the relevant `skills/pnasnexus-*/SKILL.md`.

> **PNAS Nexus is the gold open-access sibling of PNAS** (OUP, on behalf of the NAS) — a *different*
> journal from flagship *PNAS*, with its own editors, business model (gold OA + APC), submission process
> (no Direct/Contributed track), length rules, and reference policy. Do not transcribe facts from the
> `PNAS-Skills` pack into this one.

PNAS Nexus is **multidisciplinary** — spanning Biological/Health/Medical, Physical Sciences & Engineering,
and Social & Political Sciences. As with the PNAS pack, there is therefore **no single discipline-specific
code kit** that fits the whole readership, so **no econometrics / causal-inference code kit is vendored
here**. The venue-specific value lives in the source map, the tools list, the verified exemplar library,
and the worked front-matter example.

## What's here

| Resource | Use it to... |
| --- | --- |
| [`official-source-map.md`](official-source-map.md) | **The authoritative pack source-of-record.** Every PNAS-Nexus-specific name, number, fee, or policy in the skills traces back here, with access dates, confidence labels, and 待核实 flags for volatile items (APC figure, sitting editors, final reference style). Read this first. |
| [`external_tools.md`](external_tools.md) | Find the OA/APC pages and CC-license chooser, the mandatory data/code deposition repositories, reporting standards, figure/stats tooling, the Word/LaTeX templates, and the official PNAS Nexus author pages. |
| [`exemplars/library.md`](exemplars/library.md) | Benchmark against **real, web-verified PNAS Nexus articles** (every one a `10.1093/pnasnexus/…` DOI) across the three divisions — design/positioning only, no fabricated findings — plus a sibling-confusion guard (PNAS Nexus ≠ flagship PNAS ≠ *Science*/*Nature*). |
| [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md) | See a before→after rewrite of the two PNAS Nexus front-matter artifacts — the **50–120-word Significance Statement** *and* the ≤250-word **abstract** — kept genuinely distinct, in house style. Illustrative **fictional** paper; no invented policy. |

## Suggested workflow

1. **Decide PNAS Nexus is right** with [`../skills/pnasnexus-fit`](../skills/pnasnexus-fit/SKILL.md)
   (cross-division significance test; the PNAS-transfer call).
2. **Settle open access** with [`../skills/pnasnexus-openaccess`](../skills/pnasnexus-openaccess/SKILL.md)
   — APC (confirm live), waiver/discount eligibility, CC BY vs CC BY-NC.
3. **Pick the article type and structure** with
   [`../skills/pnasnexus-writing`](../skills/pnasnexus-writing/SKILL.md) (page-based budget; in-text Methods).
4. **Draft the Significance Statement early** with
   [`../skills/pnasnexus-significance`](../skills/pnasnexus-significance/SKILL.md), then the abstract with
   [`../skills/pnasnexus-abstract`](../skills/pnasnexus-abstract/SKILL.md) — model both on
   [`worked-examples/01-introduction.md`](worked-examples/01-introduction.md), keeping the two distinct.
5. **Benchmark** your field × method against verified PNAS Nexus articles in
   [`exemplars/library.md`](exemplars/library.md); confirm every venue fact in
   [`official-source-map.md`](official-source-map.md) and the deposition/OA policy in
   [`external_tools.md`](external_tools.md).

## On the source map

Unlike some economics packs that fold policy into `external_tools.md`, this pack keeps a dedicated
[`official-source-map.md`](official-source-map.md) as the single fact-of-record — because PNAS Nexus's
volatile facts (the APC figure, the sitting editor-in-chief, the final reference style) **must** be
re-verified live before submission, and the source map is where those 待核实 flags live.
