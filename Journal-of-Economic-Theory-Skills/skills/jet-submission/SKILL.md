---
name: jet-submission
description: Use when running the final pre-submission preflight for the Journal of Economic Theory (JET) via Elsevier Editorial Manager — editable .tex source (no PDF source), elsarticle formatting, full references in the abstract, generative-AI disclosure, JEL codes and keywords, and the fee-vs-APC distinction. Final checks; it does not draft content.
---

# Submission Preflight (jet-submission)

## When to trigger

- About to press submit on Editorial Manager and want a last pass
- Unsure which files JET expects at initial submission
- Confirming elsarticle formatting, abstract references, and the AI declaration are compliant

## Process facts (verified where reachable; re-confirm on the official page)

- JET is published by **Elsevier (Academic Press / Elsevier Science)**, **print ISSN 0022-0531**,
  electronic **1095-7235**. Submission is via **Elsevier Editorial Manager** through the journal's
  portal (attach-files page).
- **Source must be editable `.tex`** (Elsevier `elsarticle` class). **PDF is not accepted as a
  source file.** Reference styles per template sources are `elsarticle-harv` (name-year) and
  `elsarticle-num` (numbered) — the single required style is **待核实**; confirm in the live guide.
- **References cited in the abstract must be given in full.** Keep **unpublished results / personal
  communications out of the reference list.**
- **Authors must disclose generative-AI use at submission.**
- **Submission fee**: no fee is indicated (third-party tracker lists JET "Free") — but the official
  guide was unreachable (403), so this is **待核实**. Do **not** confuse it with the separate
  **open-access APC of USD 3,130** (hybrid journal; APC applies only if you choose OA after acceptance).
- **Length / abstract caps**: no official limit found — **待核实**.

## Preflight checklist

### Format & source
- [ ] Compiled from **editable `.tex`** in `elsarticle`; no PDF-as-source
- [ ] **Full references inside the abstract**; reference list excludes personal communications
- [ ] JEL classification codes + keywords included (standard Elsevier practice — **待核实** as verbatim rule)
- [ ] Definition/assumption/proposition/theorem/proof structure renders cleanly; cross-refs resolve

### Declarations
- [ ] **Generative-AI use disclosed** (or explicit "none")
- [ ] Conflict-of-interest / funding statements prepared
- [ ] Confirmed not under review elsewhere

### Files for Editorial Manager
- [ ] Main `.tex` + `.bib` + figure sources; cover letter (scope-fit pitch to the matching editor)
- [ ] Suggested / excluded referees (expert, conflict-free)

## Output format

```
【Source】editable .tex (elsarticle), no PDF source? [Y/N]
【Abstract refs】cited in full? [Y/N]
【AI disclosure】declared? [Y/N]
【Fee】no submission fee assumed (待核实); APC ≠ fee acknowledged? [Y/N]
【Next】await editor desk screen → jet-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — elsarticle/LaTeX toolchain
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — official JET URLs behind every fact
