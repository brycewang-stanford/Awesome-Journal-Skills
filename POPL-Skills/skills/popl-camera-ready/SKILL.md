---
name: popl-camera-ready
description: Use when a POPL paper is conditionally accepted — planning the mandatory revision the Review Committee must approve, de-anonymizing for PACMPL Issue POPL, handling ORCID/open-access/APC steps on the ACM side, syncing the paper with its proof artifact, and preparing the January talk.
---

# POPL Camera-Ready and Conditional-Acceptance Revision

POPL does not accept papers; it *conditionally* accepts them. Per the POPL 2027 call
(read 2026-07-08), authors "must submit a satisfactory revision to the Review
Committee by the requested deadline or risk rejection." The camera-ready is therefore
two gates, not one: first satisfy the committee's revision requirements, then produce
the PACMPL Issue POPL journal article. The 2027 revision deadline was not rendered at
check time — 待核实; take it from your notification email, which controls.

## Gate 1: the committee revision

- Extract every mandatory item from the meta-review and reviews into a ledger; the
  committee re-checks against its own list, not your memory.
- Anything promised in the author response is now owed. A response that said "we will
  state the well-formedness premise" has created a checkable obligation.
- Keep changes conservative. New theorems or a reworked calculus in revision invites
  re-review skepticism; strengthen statements only where reviewers demanded it.
- Where a fix touches a mechanized proof, re-run the full build and update the
  paper-to-proof correspondence table (`popl-reproducibility`) in the same commit.

## Gate 2: the PACMPL article

Identities unblind only for conditionally accepted papers, so de-anonymization
happens now and should be reviewed as a diff, not retyped:

```bash
git diff submitted..camera-ready -- '*.tex' | grep -E '^\+' | \
  grep -viE 'author|orcid|acknowledg|grant|thanks|email' && \
  echo "WARNING: content drifted beyond identity changes — justify each hunk"
```

| Item | Why POPL-specific care is needed |
|---|---|
| Author block, ORCIDs, affiliations | PACMPL is a journal; metadata errors persist in the ACM DL record forever |
| Acknowledgements and grants | Were deleted for full double-blind; restore from the pre-anonymization commit, not memory |
| Third-person self-citations | Rewrite to first person where it reads naturally, and unmask anonymized citations |
| Rights and open access | PACMPL is Gold OA; the APC was 400 USD with SIGPLAN support for authors who cannot pay and ACM Open coverage (verified 2026-07-08 — recheck amounts) |
| Artifact badge placement | Badges from artifact evaluation print on the published article; coordinate timing with `popl-artifact-evaluation` |
| Citation form | Your own paper is now PACMPL vol(POPL), article N — teach your BibTeX file before others copy it wrong |

## The January clock

Notification lands in early October (October 5, 2026 for POPL 2027) and the
conference runs mid-January (January 10-16, 2027, Mexico City). That quarter must
absorb: the committee revision, artifact evaluation, PACMPL production, visa and
travel arrangements for a January international trip, and the talk. Book the visa
appointment the week of notification; for many nationalities it is the longest pole.

## Output format

```text
[Conditional-acceptance ledger] <n mandatory items, m done>
[Response debts] <promises from the author response, each with its landing site>
[De-anonymization diff] clean / flagged hunks
[PACMPL metadata] ORCID / affiliations / rights / OA status
[January logistics] visa / registration / talk owner
```
