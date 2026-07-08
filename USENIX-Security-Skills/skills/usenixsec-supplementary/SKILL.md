---
name: usenixsec-supplementary
description: Use when deciding what goes where in a USENIX Security Symposium paper — the 13-page body, the two mandatory one-page appendices (Ethical Considerations, Open Science), optional appendices after the references, and external artifacts — so nothing decision-critical lands where reviewers won't look.
---

# USENIX Security Supplementary Material

USENIX Security does not collect a separate supplement upload; everything textual
travels in one PDF with a fixed geography, and everything executable lives at the
locations named in the Open Science appendix. Placement is therefore a reviewing
decision: material outside the 13-page body has no guarantee of being read. The
layout below is the '26 rule set (checked 2026-07-08); confirm against the current
CFP before restructuring a draft.

## The four tiers and their reading guarantees

| Tier | Cap ('26) | Who reads it |
|---|---|---|
| Main body | 13 pages | Reviewers, fully — the only tier with a guarantee |
| Ethical Considerations appendix | ~1 page, mandatory | Reviewers and (when flagged) ethics scrutiny — read carefully |
| Open Science appendix | ~1 page, mandatory | Reviewers + AEC after acceptance — enforced, not just read |
| References + optional appendices | uncapped | Discretionary; assume skimmed at best |

The two named appendices sit **between the body and the references** — an ordering
unique enough that template mistakes are common. They are not overflow space: their
job is compliance content (see `usenixsec-reproducibility` and the ethics coverage
in `usenixsec-topic-selection` / `usenixsec-experiments`), and stuffing evaluation
material into them reads as a page-limit dodge.

## What must stay inside the 13 pages

Anything a reviewer needs to judge the contribution:

- Threat model and assumptions — never appendix material at a security venue.
- The core mechanism or attack technique, end to end.
- Headline evaluation: main tables/figures, the adaptive-attacker experiment for
  defenses, the false-positive analysis for detection systems.
- Enough dataset description to assess validity (full construction detail can
  overflow to an optional appendix).
- Limitations. Hiding limitations in an appendix is a known reviewer irritant and
  reads as bad faith at a venue that prizes calibrated claims.

## What earns its place in optional appendices

- Extended proofs or protocol-analysis detail supporting a body-level statement.
- Full per-target or per-CVE result tables where the body shows aggregates.
- Additional case studies repeating a body-demonstrated pattern.
- Survey instruments, codebooks, disclosure-email templates.
- Configuration minutiae an artifact user needs but a reviewer does not.

For each candidate block, apply the demotion test: *if a reviewer never reads
this, does any claim in the body lose its support?* If yes, it stays in the body
or the claim gets weakened. If no, demote it and leave a one-line pointer.

## Overflow triage when the body runs long

Cutting to 13 pages is a routing exercise, in priority order:

1. **Compress prose, not evidence** — security drafts habitually re-narrate tables.
2. Merge figures that make one point; move third-and-later examples out.
3. Demote per-item tables to an appendix, keeping the aggregate + the worst case.
4. Only then consider dropping an experiment — and if it was load-bearing, the
   paper may actually be two papers (see `usenixsec-topic-selection`).

Never solve overflow with template surgery; the CFP forbids whitespace tampering
and desk-level format checks are mechanical.

```latex
% Correct skeleton ('26 geometry) — verify against the current template
\end{document-body}            % ≤ 13 pages ends here
\section*{Ethical Considerations}   % mandatory, ≤ ~1 page
...
\section*{Open Science}             % mandatory, ≤ ~1 page
...
\bibliographystyle{plain}
\bibliography{refs}                 % uncapped
\appendix
\section{Extended Results}          % optional, uncapped, no reading guarantee
\section{Survey Instrument}
```

## External material: the artifact is the real supplement

Code, data, VM images, and long-form documentation live at the Open Science
locations, not in the PDF. Two placement rules connect the tiers:

- The PDF should contain everything needed to **evaluate** the paper; the artifact
  contains everything needed to **redo** it. Reviewers are not obliged to open
  artifact links during review, so no reviewing-critical fact may exist only there.
- Anonymization at submission applies to all tiers at once: optional appendices
  and artifact READMEs leak identity exactly as effectively as page 1 does.

## Reverify each cycle

- Page caps and the mandatory-appendix allowances in the current CFP ('27 待核实).
- Appendix ordering relative to references (this changed style between recent
  cycles at peer venues; don't assume).
- Whether any separate supplemental upload channel has been introduced.

## Output format

```text
[Geometry] body pages / named appendices present in order / optional appendix count
[Demotion audit] items moved out + demotion-test result for each
[Body integrity] claims fully supported inside 13 pages: yes / gaps
[External] artifact-only material list — nothing reviewing-critical: confirmed
```
