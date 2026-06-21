---
name: hlr-footnotes-and-cite-check
description: Use when building and stress-testing the heavy footnote apparatus of a Harvard Law Review (HLR) piece so it survives the student-editor cite-check / source-pull. Builds and audits the apparatus for pull-readiness; it does not set Bluebook form per citation (hlr-sources-and-bluebook) or manage the editor relationship (hlr-student-editor-review).
---

# Footnotes and Cite-Check (hlr-footnotes-and-cite-check)

Legal scholarship runs on a **dense footnote apparatus**, and HLR editors run a **full cite-check /
source-pull**: they obtain every cited source and confirm that each footnote actually supports its
proposition, that quotations are exact, and that pincites are right. The author who is **pull-ready
before submission** sails through; the one who is not faces painful rounds. This skill builds the
apparatus and audits it for that scrutiny.

## When to trigger

- Building footnotes as you draft, or auditing them before submission
- Preparing for the source-pull after an offer
- A footnote carries a proposition you are not sure the source supports
- Quotations, pincites, or short forms feel shaky after editing moved footnotes

## What the apparatus must do

1. **Support every proposition.** Each assertion of law or fact in the text has a footnote whose source
   actually states (or, with the right signal, supports) it — at the **exact page** cited.
2. **Carry the qualifications.** Caveats, contrary authority, and side disputes live in footnotes so the
   text reads as a clean argument (see the text/footnote division in `hlr-writing-style`).
3. **Be verifiable by a stranger.** A student editor with no prior knowledge must be able to pull each
   source and confirm the footnote — that is the whole test.

## Pull-readiness: the author's source file

Before submission, assemble a **source file**: a copy (or precise locator) of **every** cited source with
the **cited page marked** and the supported proposition noted. This is the single best predictor of an
easy cite-check.

| Source type | What to keep | Pull-check |
|-------------|--------------|------------|
| Cases | Reporter cite + the pincited page | Does that page state/support the proposition? |
| Statutes / regs | Exact section, current version | Is the language current and on point? |
| Articles / books | Copy with cited page flagged | Quote exact? Pincite to the right page? |
| Web sources | Archived/dated copy (link rot is real) | Captured with an access date? |

## Self-running cite-check (do this before editors do)

- **Proposition ↔ source match.** Read each footnote against the page it cites. If the page does not
  support the claim, fix the cite or soften the claim — never leave the gap.
- **Quotation accuracy.** Check every quotation character-for-character against the source; verify the pincite.
- **Signal accuracy.** Confirm the signal matches the relationship (see `hlr-sources-and-bluebook`).
- **Short-form integrity.** After any footnote reordering, re-verify every *Id.* and *supra* — these break
  silently when notes move.
- **No orphan or dead cites.** Every footnote resolves; no broken cross-references or rotted URLs.

## Checklist

- [ ] Every text proposition has a supporting footnote, pincited to the exact page
- [ ] Source file assembled: every source kept with the cited page marked
- [ ] Each footnote re-read against its source page (proposition actually supported)
- [ ] Every quotation verified character-for-character and pinned
- [ ] Signals match relationships; short forms (Id./supra) re-verified after moves
- [ ] Web sources archived with access dates (link rot)
- [ ] No orphan footnotes, dead cross-references, or unsupportable claims

## Anti-patterns

- Footnotes that gesture at a source which does not actually support the proposition
- Quotations not checked against the original (a cite-check failure that erodes trust fast)
- Dangling *Id.*/*supra* after footnotes were reordered in drafting or editing
- Citing web sources without an archived, dated capture (link rot at proof time)
- Leaving the source-gathering until editors ask — assemble the source file before submission

## Output format

```
【Apparatus】every proposition footnoted + pincited? [Y/N]
【Source file】all sources kept with cited pages marked? [Y/N]
【Self cite-check】propositions match sources; quotations exact? [Y/N]
【Short forms】Id./supra re-verified after moves? [Y/N]
【Pull-ready】a stranger could verify every footnote? [Y/N]
【Next】hlr-writing-style (text/footnote balance) → hlr-submission
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — citators (Shepard's/KeyCite), archiving (Perma.cc), reference managers
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — HLR's Bluebook role and editorial cite-check practice
