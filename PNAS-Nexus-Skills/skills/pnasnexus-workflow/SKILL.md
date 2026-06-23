---
name: pnasnexus-workflow
description: Use when deciding which pnasnexus-* sub-skill to invoke next, or when sequencing a manuscript from scope/significance test through reviewer rebuttal for PNAS Nexus (the fully open-access sibling journal of PNAS, published by Oxford University Press for the U.S. National Academy of Sciences). Routes — it does not replace — the specialized skills.
---

# PNAS Nexus Workflow Router (pnasnexus-workflow)

## Overview

This is the router. It does not replace any specialized skill. It tells you **which pnasnexus-* skill to use at the current stage** of a manuscript aimed at *PNAS Nexus*.

**PNAS Nexus is not flagship PNAS.** It is the **gold open-access sibling journal**, published by **Oxford University Press (OUP)** in partnership with the **National Academy of Sciences (NAS)**. Two things reshape the workflow relative to the `pnas-skills` pack and must be settled early: (1) it is **fully open access with an article processing charge (APC)** and a **CC BY / CC BY-NC license choice** (`pnasnexus-openaccess`), and (2) it has **no Direct/Contributed submission track** — every paper goes through standard editor-assigned peer review. PNAS Nexus also has a **transfer route from flagship PNAS** that carries reviews over (`pnasnexus-fit`).

## When to trigger

- "What should I do next with this draft?"
- A draft arrives and you must diagnose the current bottleneck.
- The user just had a paper declined by PNAS and is considering the PNAS Nexus transfer.
- The user is unsure about open-access cost, waivers, or which license to pick.
- Reviews arrive from PNAS Nexus and you need to switch into rebuttal mode.

## The single most important gate

Route to `pnasnexus-fit` first, always. The first question is **"is this high-quality, broadly significant, multidisciplinary research that the PNAS Nexus readership across biological/health/medical, physical sciences & engineering, and social & political sciences would value?"** PNAS Nexus is positioned as a **complementary, broad-scope sibling** to PNAS — including via a **transfer route** for sound work declined at PNAS — so `pnasnexus-fit` also handles the "we were declined at PNAS, is the transfer right?" decision.

> **Settle open access early.** Because every PNAS Nexus article is OA and carries an APC, confirm funding, eligibility for a waiver/discount, and license choice *before* you invest in polishing — run `pnasnexus-openaccess` right after `pnasnexus-fit`.

## Routing table

| Current symptom                                              | Next skill            |
|--------------------------------------------------------------|-----------------------|
| Not sure the result fits PNAS Nexus, or deciding whether to transfer from PNAS | `pnasnexus-fit` |
| Unsure about the APC, waivers/discounts, license (CC BY vs CC BY-NC), or funder compliance | `pnasnexus-openaccess` |
| No Significance Statement, or it is outside 50–120 words / just restates the abstract | `pnasnexus-significance` |
| Abstract too long/narrow, has headings, or conflated with the significance statement | `pnasnexus-abstract` |
| Unsure of article type; structure unclear; Methods misplaced; over the page budget; no classification | `pnasnexus-writing` |
| Figures/tables over the graphical-element budget; sizing/fonts/colors non-compliant | `pnasnexus-figures` |
| Stats under-reported; n/error bars/tests unclear; not reproducible; considering a Registered Report | `pnasnexus-statistics` |
| No data/code deposition plan; raw images not retained; "on request" only | `pnasnexus-data` |
| References messy/inconsistent (note: format-neutral *at submission*) | `pnasnexus-citation` |
| About to submit; need a preflight checklist + cover letter | `pnasnexus-submission` |
| Received reviews / a revision decision | `pnasnexus-rebuttal` |

## Default order

1. `pnasnexus-fit` — clear the broad-significance bar; confirm PNAS Nexus is the venue (incl. the PNAS transfer call)
2. `pnasnexus-openaccess` — APC, waiver/discount eligibility, license choice (do this early; it gates submission)
3. `pnasnexus-writing` — article type, structure, classification, in-text Methods, page budget
4. `pnasnexus-figures` — finalize display items within the graphical-element budget
5. `pnasnexus-statistics` — rigor & reproducibility (and whether a Registered Report fits)
6. `pnasnexus-data` — mandatory data/code deposition + raw-image retention
7. `pnasnexus-significance` — the 50–120-word Significance Statement (high-value; draft early)
8. `pnasnexus-abstract` — ≤250-word single-paragraph abstract (late polish)
9. `pnasnexus-citation` — references (format-neutral at submission; make them clean and consistent)
10. `pnasnexus-submission` — preflight + cover letter
11. `pnasnexus-rebuttal` — after review

> `pnasnexus-significance`, `pnasnexus-abstract`, and `pnasnexus-citation` are **late-stage polish** — but the Significance Statement is high-value and editor-facing, so draft it as soon as the claim is locked.

## Decision shortcuts

- "PNAS declined us — should we accept the PNAS Nexus transfer?" → `pnasnexus-fit`
- "How much will open access cost, and can we get a waiver?" → `pnasnexus-openaccess`
- "Which license — CC BY or CC BY-NC?" → `pnasnexus-openaccess`
- "Is a co-author who is an NAS member able to 'contribute' this paper?" → `pnasnexus-openaccess` / `pnasnexus-fit` (**no** — PNAS Nexus has no Contributed track)
- "What article type is this — Research Report, Brief Report, Perspective, Review?" → `pnasnexus-writing`
- "Where do Materials and Methods go?" → `pnasnexus-writing` (in the **main text**)
- "Do I really have to deposit the data and code?" → `pnasnexus-data` (yes — mandatory, with retraction teeth)

## How PNAS Nexus differs from flagship PNAS (do not transcribe PNAS facts here)

- **Business model:** PNAS Nexus is **fully gold open access with an APC**; flagship PNAS is hybrid. Cost, waivers, and license choice are real workflow steps here (`pnasnexus-openaccess`).
- **No submission tracks:** PNAS Nexus has **no Direct vs Contributed (NAS-member) choice** — all editor-assigned peer review. The `pnas-track` skill has **no equivalent**; its slot is taken by `pnasnexus-openaccess`.
- **Transfer route in:** sound work declined by PNAS can be **transferred** to PNAS Nexus with reviews carried over (`pnasnexus-fit`).
- **Scope & board:** broader, explicitly cross-disciplinary; the editorial board spans the NAS, NAE, and NAM.
- **Length:** **page-based** budgets and named **article types** (Research Report ≈6 pp / 12 max, Brief Report, Perspective, Review, Registered Reports) — `pnasnexus-writing`.
- **References:** **format-neutral at submission** — not the strict numbered-by-appearance PNAS demands up front (`pnasnexus-citation`).
- **Significance Statement:** **50–120 words** (note the **minimum**) (`pnasnexus-significance`).

## Anti-patterns

- **Do not** skip `pnasnexus-fit` and start polishing prose.
- **Do not** defer the open-access/APC/license decision to the final upload — it gates submission (`pnasnexus-openaccess`).
- **Do not** assume a Direct/Contributed track exists — it does not.
- **Do not** copy length, reference-style, or fee facts from the flagship `pnas-skills` pack; PNAS Nexus differs.
- **Do not** generate a rebuttal before the main text is actually revised.
