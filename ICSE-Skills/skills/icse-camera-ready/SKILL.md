---
name: icse-camera-ready
description: Use when converting an accepted ICSE research-track paper into its final published form, covering the extra camera-ready page, de-anonymization order, finalizing the Data Availability section with archival DOIs, IEEE-template production checks, and conference-presentation obligations to verify.
---

# ICSE Camera-Ready

Acceptance converts the paper from an argument into a permanent record —
ICSE proceedings live in the ACM Digital Library and IEEE Xplore, and the
camera-ready is the version every future reader, replicator, and artifact
evaluator holds against your claims. The window is short and lands amid
artifact-evaluation prep, so run it as a checklist, not a rewrite.

## What actually changes

The 2027 call (read 2026-07-08) grants accepted papers **one extra page of
main text** for the camera-ready — 11 + 2 instead of 10 + 2. Spend it where
review friction was, in this order of value:

1. Changes promised in the author response or Major Revision ledger that were
   squeezed by space — reviewers who see their request honored in the final
   version include your artifact evaluators and future citers.
2. The threats-to-validity or study-design detail that reviews called thin.
3. Restored per-subject detail that summarize-and-point compression removed.

Do not spend it on a new contribution: the paper was accepted for what it
evidenced, and content that never faced review is a correctness risk with
your name permanently on it.

## De-anonymization order

Reverse the double-anonymous transformations *systematically* — grep, don't
recall:

```bash
# Residual-anonymity sweep on the camera-ready sources
grep -rn "anonym\|blinded\|double-blind\|under review" *.tex        # stale phrases
grep -rn "anonymous.4open\|anonymized-link\|REDACTED" *.tex         # placeholder URLs
grep -n "our prior work\|the authors of \[" *.tex                   # third-person self-cites to naturalize
pdfinfo camera-ready.pdf | grep -Ei 'author|title'                  # metadata now SHOULD carry authors
```

Restore: the author block with affiliations, emails, and ORCIDs;
acknowledgments and funding with grant numbers; self-citations rephrased into
natural first person where it improves clarity; and — most consequentially —
**the availability statement's links**, from anonymized mirrors to the
permanent DOI-issuing archive (`icse-artifact-evaluation` covers minting it).
A camera-ready that still points at a review-time anonymous mirror will
outlive the mirror.

## Production-quality gate

| Check | Detail |
|---|---|
| Template | Current IEEE conference class, unmodified; production vendors reject tampering the PC tolerated |
| Metadata block | Copyright/DOI stamps per the acceptance instructions; correct year and conference string |
| Author records | Name spellings, affiliations, ORCIDs consistent with the submission system — indexing errors are near-impossible to fix post-publication |
| Fonts and figures | Fonts embedded, figures vector where possible, colorblind-legible; print-grayscale still distinguishable |
| References | Every entry re-verified against dblp/DL records; camera-ready is the last chance to fix a wrong venue or year |
| Availability statement | DOI links live; artifact contents match final table/figure numbering |
| Title/abstract sync | Final title and abstract match the submission system's metadata fields exactly |

## Consistency with the accepted version

Chairs expect the camera-ready to be the accepted paper plus the required
changes — not a quiet second revision. Keep a change log from accepted PDF to
camera-ready; if a real error surfaced after acceptance (a bug in an analysis
script, a corrected number), fix it *and* flag it to the track chairs rather
than hoping nobody diffs. Silent number changes discovered later are an
integrity problem; disclosed corrections are routine science.

## Obligations around the paper — verify, don't assume

Several items were not published for the 2027 cycle at check time and are
待核实 on the live pages once acceptance emails go out:

- Camera-ready deadline and the exact submission system/vendor instructions.
- Registration requirements tied to publication (one author registering at a
  qualifying rate is the common conference pattern — confirm ICSE 2027's
  wording before budgeting).
- Presentation format and whether remote presentation exists; plan for
  in-person in Dublin (Apr 25 – May 1, 2027; core days Apr 28–30).
- Page-purchase options beyond the granted extra page.
- Video, poster, or preprint requirements attached to the final submission.

Book Dublin logistics early regardless: late-April conference housing in a
capital city is its own deadline.

## The December–January squeeze

For Major-Revision papers the final decision (December 18 in the 2027
cycle) lands directly against the artifact-evaluation window (early January
in recent cycles) and, soon after, camera-ready production. Sequence
deliberately: freeze the artifact container first (it feeds the badge
deadline), then finalize the availability statement's DOI (the camera-ready
needs it), then spend the extra page — because page-11 content that cites
package paths must cite the *final* package. Groups that treat these as
three independent deadlines do the DOI work twice.

## Publication-week hygiene

Post the accepted-version preprint per the copyright terms you signed (arXiv
or institutional repository — the open-science culture expects it), update
the artifact's citation file with the final DOI, and make the paper's page,
package, and preprint agree on one canonical title and author order. Future
citation graphs are built from whichever version spreads first.

## Output format

```text
[Extra page] spent on: <review-friction items>; new-contribution check: none added
[De-anonymization] sweep results; availability links now DOI-permanent
[Production gate] table above -> pass/fail per row
[Change log] accepted -> camera-ready diffs; disclosed items
[Obligations] deadline / registration / presentation — verified or 待核实 with owner
```
