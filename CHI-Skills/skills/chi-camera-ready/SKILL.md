---
name: chi-camera-ready
description: Use when preparing an accepted ACM CHI paper for publication — the TAPS source upload, the PCS publication-ready package, mandatory accessibility work (alt text, screen-reader-friendly PDFs, table headers), video previews, ACM's open-access model, e-rights, and registration deadlines.
---

# CHI Camera-Ready

Acceptance at CHI starts a production pipeline with more moving parts than most
venues: ACM TAPS renders your paper from source, an accessibility pass is mandatory
rather than aspirational, and the video preview and registration have their own
deadlines. CHI 2027 dates (chi2027.acm.org, read 2026-07-08): TAPS source upload
**January 14, 2027**; publication-ready package on PCS **February 18, 2027**;
registration and presentation video **March 4, 2027**.

## TAPS is a compiler, not a dropbox

The ACM Publishing System ingests your LaTeX or Word *source* and generates the
final double-column PDF plus HTML for the Digital Library. You reviewed in
single-column; TAPS produces the publication look. Consequences:

- Hand-tuned spacing, hacked floats, and non-standard packages that survived your
  local build can fail in TAPS. Compile with the current `acmart` class settings
  early, and budget a round trip for TAPS errors before January 14.
- The HTML edition means your content must survive reflow: content buried in
  absolutely-positioned figures or images-of-text will degrade or vanish.
- De-anonymize deliberately: restore authors, affiliations, ORCIDs (get every
  coauthor's ORCID before January), acknowledgements, grant numbers, and re-link
  repositories and OSF projects under real identities.

## The accessibility pass is required work

SIGCHI's accessibility guidance and the CHI publication-ready instructions make the
author responsible for a paper that works with screen readers. The posted division of
labor: an external provider tags the TAPS-produced PDF, **but authors must supply
meaningful alt text for every figure in the source and in PCS** — tagging cannot
invent descriptions you never wrote.

| Item | Requirement | Where it lives |
|---|---|---|
| Figure alt text | Describes the information content, not the pixels; complements rather than repeats the caption | `\Description{}` in source + PCS field |
| Tables | Real table markup with marked header rows — never a screenshot of a table | Source |
| Color | No claim readable only through color; check contrast | Figures |
| Math | Real math markup, not inline images | Source |
| Links | Meaningful link text, not raw URLs mid-sentence | Source |
| Video captions | Closed captions (SRT/SBV/VTT) on every video file | PCS upload |

```latex
% Every figure needs a Description; acmart warns, TAPS and PCS expect it.
\begin{figure}
  \includegraphics[width=\linewidth]{study-setup.pdf}
  \Description{Participant seated at a desk wearing the haptic glove, with the
    stimulus screen 60 cm away showing a 3-by-3 target grid.}
  \caption{Study apparatus.}
\end{figure}
```

```bash
# Find figures still missing descriptions before the TAPS upload
grep -L '\\Description' $(grep -rl 'includegraphics' sections/) 2>/dev/null
grep -c '\\Description' main.tex sections/*.tex
```

Write alt text as if explaining the figure over the phone to a colleague who will act
on it. "Bar chart of results" fails; "Bar chart: error rate halves from 12% with the
baseline to 6% with our technique, consistent across all three tasks" succeeds.

## Open access and rights

ACM's publication model changed decisively for this generation of CHI: **from
January 1, 2026 all ACM publications are open access** in the Digital Library. Costs
are covered either by your institution's ACM Open agreement (over 2,600 institutions;
the majority of ACM conference papers) or by an APC; ACM posted discounted transitional
APC rates ($250 member / $350 non-member) for conferences during 2026 — the exact
arrangements applying to CHI 2027 authors are cycle-specific (待核实 via the e-rights
form and acm.org/publications/openaccess). Complete the ACM e-rights form as soon as
it arrives; TAPS will not finalize without it. Fill CCS concepts and keywords
thoughtfully — they drive DL discovery permanently.

## The February and March deliverables

The **publication-ready deadline (2027-02-18)** is when PCS wants the TAPS-approved
paper plus final supplementary materials: the video figure with captions, any
datasets/appendix files, and the optional **30-second video preview** that appears
beside the DL record and in conference programs. The **March 4** deadline pairs
registration with the presentation video. Practical notes:

- The video preview is optional but cheap leverage: it is often the only part of the
  paper a conference attendee sees before choosing sessions. One idea, one
  visual, spoken captions-checked audio — not a compressed talk.
- Registration rules for publication (who must register, at what rate, in-person
  versus remote presentation) are posted per cycle and were 待核实 at check time;
  confirm before assuming a remote option exists.

## Sequence for a calm January–March

1. Week of acceptance: e-rights form, ORCID collection, owner per deliverable.
2. Early January: TAPS compile attempt #1; fix class errors; alt-text sweep done.
3. Jan 14: TAPS source in. Respond to TAPS validation quickly — the queue slows near
   the deadline.
4. Early February: proof the TAPS PDF *and* HTML rendering; check every figure,
   table, and math block survived.
5. Feb 18: PCS publication-ready package: final PDF sign-off, supplements, captions,
   video preview.
6. Mar 4: registration confirmed, presentation video uploaded.

## Output format

```text
[Pipeline] e-rights ✓/✗ · TAPS compiled ✓/✗ · alt text <n>/<n figures> ·
           supplements ✓/✗ · preview ✓/✗ · registered ✓/✗
[Next deadline] <date> — <deliverable> — owner: <name>
[Accessibility gaps] <figures/tables/math still failing>
[OA route] ACM Open institution / APC (rate 待核实 for the cycle)
```
