---
name: itcs-submission
description: Use when auditing an ITCS submission for HotCRP readiness — the early-September abstract-then-paper deadlines, single-column >= 11pt format with no hard page limit, the first-10-pages merits window, complete proofs of all central claims, the lightweight double-blind sweep, and the archival-prior-publication check.
---

# ITCS Submission

Run this audit before uploading to the ITCS HotCRP site. ITCS papers publish **open access in
LIPIcs** and are reviewed **lightweight double-blind with no rebuttal**, so the submitted PDF has
to be complete, self-defending, and correctly anonymized on the first and only try. Every rule
below was read from the ITCS 2026/2025 calls on 2026-07-09 via search renderings of the
`itcs2026.hotcrp.com` and `itcs-conf.org` URLs (see
[`../../resources/official-source-map.md`](../../resources/official-source-map.md)); treat them as
a one-cycle snapshot and reopen the live call first.

## The two-step deadline

ITCS separates the **abstract/registration** from the **full-paper submission**, and the abstract
cutoff is *earlier*:

- **Abstract / registration** locks title, abstract, authors, and conflicts (ITCS 2026:
  **4 September 2025**, 7:59:59 PM EDT). The abstract drives PC bidding — register the *real*
  title and abstract, not a placeholder.
- **Full-paper submission** uploads the anonymized PDF with complete proofs (ITCS 2026:
  **6 September 2025**, 7:59:59 PM EDT). Miss the registration and no submission slot exists.

## Format and page policy

- **Single column, font size at least 11 point.** Beyond that, the submission call imposes **no
  hard formatting template** and **no hard page limit** (the LIPIcs `lipics-v2021` class is a
  *camera-ready* requirement, not a submission one — see
  [`itcs-camera-ready`](../itcs-camera-ready/SKILL.md)).
- **First-10-pages merits window.** It is strongly recommended that the first ~10 pages give a
  clear presentation of the paper's merits, significance, innovations, and place in the
  literature. Reviewers judge the idea from this window; do not bury it (see
  [`itcs-writing-style`](../itcs-writing-style/SKILL.md)).
- **Complete proofs of all central claims** must be included, in an appendix if needed. "Proof
  omitted" or "see the full version" for a load-bearing claim is a substantive defect, not a
  formatting one (see [`itcs-supplementary`](../itcs-supplementary/SKILL.md)).

## Lightweight double-blind sweep

ITCS anonymity is **lightweight**: hide the authors *in the PDF*, but keep the references honest
and allow a public full version. The leak surface is narrower than an empirical venue's (no code,
no data), but real:

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'     # scrub metadata identity
pdftotext paper.pdf - | grep -nEi 'thank|acknowledg|grant|supported by|our (previous|prior|earlier) (work|paper)' | head
pdftotext paper.pdf - | grep -nEi '\\bwe (previously|earlier) (showed|proved)\\b' | head
```

- **Remove** author names, affiliations, emails, and acknowledgements/funding lines from the PDF.
- **Neutralize first-person self-reference:** rewrite "in our prior work [12]" as a third-person
  "[Author, YEAR] showed." Do **not** anonymize or remove the reference itself — the reference
  list stays intact (see [`itcs-related-work`](../itcs-related-work/SKILL.md)).
- **A public arXiv/ECCC/ePrint full version is allowed** and encouraged; you need not delay it for
  anonymity. Just keep the *submitted* PDF blinded.

## Prior-publication and dual-submission check

- The result must **not** be published, presented, or under submission at another **archival**
  conference. Papers accepted to ITCS should not then go to another archival conference.
- **Simultaneous submission to a journal is allowed** — a distinctive ITCS latitude; a journal
  version in parallel is fine.
- Confirm the exact current wording each cycle; the archival/non-archival boundary and any
  workshop carve-outs are cycle-volatile.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Central claim lacks a complete proof | Substantive reject-grade | Add the full proof (appendix); do not defer to the preprint |
| Merits not legible within ~10 pages | High | Restructure so model+motivation+results come first |
| Author identity in PDF metadata/acknowledgements | Anonymity violation | Scrub metadata; remove acknowledgements/funding |
| First-person self-citation ("our prior [12]") | Anonymity leak | Rewrite in third person; keep the reference |
| References anonymized/removed | Breaks the lightweight rule; reads evasive | Restore normal citations |
| Abstract/authors not registered by the earlier cutoff | No submission slot | Nothing fixes this post-deadline — calendar it now |
| Result already at another archival venue | Dual-submission violation | Withdraw or reroute; journal parallel is OK |
| Font < 11pt or multi-column | Formatting non-compliance | Recompile single-column, >= 11pt |

## Final-week order of operations

1. Freeze the model and definitions early; proofs can be polished, the framing cannot churn.
2. Register title/abstract/authors/conflicts before the earlier registration cutoff.
3. Run the proof-completeness pass: every central claim fully proved *in the PDF*.
4. Run the mechanical anonymity checks on the **final** PDF (metadata + self-reference).
5. Post the full version to arXiv/ECCC/ePrint if desired (allowed); keep the submission blinded.
6. Fill every HotCRP field — topics, conflicts for every coauthor's institution and recent
   collaborators — a day early; late conflicts are the classic midnight failure.
7. Re-download the uploaded PDF and read the first 10 pages cold to confirm the idea lands.

## Reverify each cycle

- The two cutoff dates and their timezone (EDT/AoE).
- Whether the current call still runs **no rebuttal** and lightweight double-blind.
- The exact prior-publication/dual-submission wording and any generative-AI-disclosure rule.
- That there is still no hard page limit and the 11pt/single-column format holds.

## Output format

```text
[ITCS submission status] ready / blocked / needs work
[Registration] title/abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] single-column, >= 11pt? merits legible within ~10 pages? yes/no
[Proofs] every central claim fully proved IN the PDF (not only the preprint)? yes/no
[Anonymity] metadata clean, self-cites neutralized, references intact? yes/no
[Prior publication] not at another archival venue (journal parallel OK)? yes/no
[Fix queue] <ordered, with owners and dates before the early-September cutoff>
```
