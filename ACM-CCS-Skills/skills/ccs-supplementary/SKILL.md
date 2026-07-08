---
name: ccs-supplementary
description: Use when preparing ACM CCS appendices and supplementary material, including the ethics considerations appendix, protocol transcripts, formal proofs, measurement tables, and anonymized supporting material under the 12-page body limit, anonymity, and reviewer-discretion constraints for a security paper.
---

# CCS Supplementary

Use this when assembling CCS appendices and supplementary material. At CCS the main 12-page
body must let reviewers judge novelty and soundness on its own; appendices support it but the
committee is not obligated to read them.

## Supplement structure

- Put formal proofs, full protocol transcripts, extra measurements, and additional evaluation
  tables in well-marked appendices after the bibliography.
- Place the ethics considerations content where the CFP directs it. CCS 2026 required a
  dedicated ethics section as an appendix after the 12-page body and the bibliography for work
  touching human subjects, user data, or real-world vulnerabilities.
- Keep every supplementary file double-blind: no authors, institutions, acknowledgements,
  private paths, repository owners, or identifying metadata, including in code and datasets.
- Do not hide the core threat model, the main attack description, the headline defense, or the
  primary evidence in an appendix; a paper whose contribution is only legible with the
  appendix reads as unreviewable within the page limit.
- Verify archives open on a clean machine and carry no credentials, cache directories, or OS
  metadata that leaks identity.

## Appendix architecture for a security paper

- Order appendix sections to mirror the body: threat model details, then proofs, then extended
  attack variants, then measurement tables, then the ethics section where required.
- Restate each theorem or protocol step before its full derivation so the appendix reads
  standalone without flipping back to the two-column body.
- Cross-reference every appendix table and proof from the body at least once; orphaned
  material is invisible under reviewer discretion.
- Keep the ethics section self-contained: disclosure timeline, harm-minimization steps, IRB or
  ERB status, and the reasoning, so the ethics reviewer can grade it without hunting.

## What gets opened first

| Supplement item | Inspection likelihood | Practical implication |
|---|---|---|
| Ethics considerations section | High for sensitive work | Write it to stand alone and answer the obvious concern |
| Proof of the headline security guarantee | High for crypto/formal papers | Polish it to main-text standard |
| Extended attack variants and measurements | Medium | Reference each one from the body |
| Code and data archive | Variable, reviewer discretion | The README must orient a reader in one minute |

## Vignette: splitting a protocol-security paper

A submission proving a key-exchange protocol secure, plus an implementation and overhead
plots: the body keeps the threat model, the protocol, the main security theorem with a
sketch, and the overhead figure; the appendix holds the full proof, the message-level
transcript, and the ethics note on the disclosed implementation bug; the archive carries the
reference implementation and test vectors. Nothing decision-critical lives only in the
archive, because archive inspection is discretionary.

## Output format

```text
[Supplement status] Ready / Needs fixes / Not ready
[Files] <appendix / proofs / ethics section / code / data>
[Ethics section] present / required-and-missing / not-applicable
[Anonymity checks] passed / issues
[Main-paper dependency] <what breaks if the appendix is ignored>
```
