---
name: eacl-supplementary
description: Use when organizing an EACL paper's body, mandatory Limitations section, appendices, and anonymized supplementary archive so that no decision-critical content hides where ACL Rolling Review reviewers are not obliged to read, and so the content-page budget carries the whole argument on its own.
---

# EACL Supplementary Material

Use this to decide **what goes where** across an EACL submission: the content pages, the
Limitations section, the appendices, and the anonymized supplementary archive. The governing
rule in ARR is that **reviewers must read the content pages but are not obliged to read
appendices or the archive** — so anything decision-critical that lives outside the body is a
self-inflicted risk. Reopen the current ARR CFP before finalizing structure.

## The placement hierarchy

| Location | Reviewer obligation | Put here |
|---|---|---|
| Content pages (8 long / 4 short) | Must read | The claim, method, key results, the argument |
| Limitations (after conclusion, uncounted) | Must read | Honest scope, failure modes, threats to validity |
| References (unlimited) | As needed | Citations |
| Appendices (in-PDF, after refs) | May skip | Proof detail, extra tables, full hyperparameters |
| Anonymized archive (OpenReview) | May skip | Code, data, prompts, model outputs |

## The self-containedness test

- Read only the content pages and the Limitations section. Can a reviewer **accept or reject on
  that alone**? If a core mechanism, the main baseline, or the headline result lives only in an
  appendix, move it into the body.
- "See Appendix X" is fine for *detail*, never for the *argument*.

## Limitations is body, not backmatter

- The Limitations section is **mandatory and read**; treat it as part of the argument, not a
  disclaimer. Name the languages you did not cover, the settings you did not test, and the
  claims you cannot support — reviewers reward this and it is explicitly protected.
- Do not smuggle results into Limitations to dodge the page limit; that is transparent and
  counterproductive.

## Appendix organization

```text
Appendix A: full hyperparameters + search spaces
Appendix B: additional / per-language results tables
Appendix C: annotation guidelines + agreement
Appendix D: prompt templates + decoding settings (verbatim)
Appendix E: additional error analysis / examples
```

Label appendices so the body can point precisely, and keep each reproducible from the archive.

## Anonymized archive hygiene

- The OpenReview supplement must be **fully de-identified** (see `eacl-artifact-evaluation`): no
  names in paths, headers, or git history.
- Keep the archive **self-contained** — a reviewer who does open it should be able to reproduce a
  reported table without hunting for external files.

## Common misplacements to catch

- **Core baseline hidden in an appendix** — reviewers may never see it; the comparison then reads
  as missing.
- **Key multilingual result only in the archive** — an EACL reviewer will not go digging;
  surface at least a summary table in the body.
- **Ethics/data-governance detail buried** — for sensitive or lower-resource data, keep the
  intended-use and provenance statement visible.

## Output format

```text
[Placement audit] Pass / Needs moves
[Decision-critical content outside body] <list, with where it should go>
[Limitations quality] <substantive / ritual>
[Appendix map] <A-E contents>
[Archive hygiene] <anonymized + self-contained: pass/fail>
```
