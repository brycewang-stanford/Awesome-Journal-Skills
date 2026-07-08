---
name: pldi-camera-ready
description: Use when turning an accepted PLDI paper into its PACMPL Issue PLDI article — de-anonymization, acmsmall journal formatting, ACM rights and open-access handling, delivering every author-response commitment, and coordinating the Zenodo artifact and June conference presentation.
---

# PLDI Camera-Ready

Since 2023, "camera-ready" at PLDI means producing a **journal article**: accepted
papers appear as PACMPL (Proceedings of the ACM on Programming Languages),
Issue PLDI — Vol 7 for 2023, Vol 8 for 2024, Vol 9 for 2025 (SIGPLAN blog
2022-08-08 and ACM DL, read 2026-07-08). The conference talk in June is downstream
of the article, not the other way around: the 2025 wording invited PACMPL Issue
PLDI authors to present, without requiring it. Recheck the current instructions —
the 2026 camera-ready deadline itself was not visible in accessible renderings
(待核实).

## What changes at acceptance

| Submission state | Camera-ready state |
|---|---|
| Anonymous, third-person self-citations | Real authors, ORCIDs, affiliations, acknowledgements, grants restored |
| "We will..." sentences in the response | Delivered text, tables, and proofs — reviewers may verify |
| acmsmall draft with review margins | acmsmall with ACM rights block, CCS concepts, and final metadata |
| Code on an anonymous mirror | Artifact heading to Zenodo with a DOI (see `pldi-artifact-evaluation`) |
| No fee questions | Open-access handling under ACM's model |

## Open access, concretely

PACMPL is Gold Open Access. As of the check date: the discounted author-side APC
was 400 USD, SIGPLAN covers it for authors who cannot pay, ACM Open institutions
owe nothing, and ACM became a fully open-access publisher on January 1, 2026
(dl.acm.org/journal/pacmpl, read 2026-07-08). Verify which regime applies to your
institution during the rights workflow rather than budgeting from hearsay, and
never route the fee question to a student author alone.

## The de-anonymization pass

Do this as a diff, not a rewrite:

```bash
git diff submission..camera-ready -- paper/ | grep -E '^\+' | \
  grep -viE 'author|orcid|acknowledg|grant|funding|\\cite' && \
  echo "WARNING: content drift beyond identity restoration"
```

Legitimate additions: author block, acknowledgements, funding, restored
first-person self-citations, and the revisions promised in the author response.
Anything else — a new claim, a quietly changed number — needs your shepherd's or
the chairs' sign-off. Fix any self-citations that were blinded into vagueness:
"prior work [12]" may now become "our earlier analysis [12] which this paper
extends," with the delta stated plainly.

## PACMPL metadata checklist

- Title and author order exactly as approved; changes after acceptance go through
  the chairs, not the production form.
- ORCID for every author; ACM's workflow expects them.
- CCS concepts and keywords chosen by where compiler and PL readers will search,
  not copied from the template sample.
- Citations to post-2023 SIGPLAN papers in journal form: *Proc. ACM Program.
  Lang.* volume, issue (PLDI/POPL/OOPSLA/ICFP), article number — see
  `pldi-related-work` for the bibliography discipline.
- Every axis label and table caption re-read at final size; the single-column
  layout is unforgiving of figure text scaled for two columns.

## Coordinate the three deliverables

The article, the artifact, and the talk ship on different clocks: the article on
the production deadline, the artifact on the AE timetable (Zenodo versioning
means no artifact camera-ready deadline), and the talk in June — registration for
PLDI 2026 opened March 16, 2026. Name one owner for each clock; the classic
failure is a perfect article whose artifact DOI still points at a stale
pre-response version.

## Output format

```text
[Camera-ready status] on track / blocked
[Response commitments] delivered: n/n, with section pointers
[Identity restoration] author block / ORCID / acknowledgements / self-citations
[Open access] ACM Open covered / APC path / SIGPLAN waiver (verify current terms)
[Clocks] article: <date 待核实> | artifact: <AE timetable> | talk: <June program>
```
