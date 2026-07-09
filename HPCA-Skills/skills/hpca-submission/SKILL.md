---
name: hpca-submission
description: Use when auditing an HPCA submission for the two-step July gate on HotCRP, the 11-page main-body limit, the IEEE template, double-blind anonymity plus the all-authors reference rule, the AI-use disclosure, artifact-link scrubbing, and final-week sequencing before the paper deadline.
---

# HPCA Submission

Use this for an HPCA paper submission audit. Reopen the current
`20XX.hpca-conf.org` call for papers, the HotCRP portal, and the IEEE template
before giving deadline-ready advice — every cap and date below is a cycle snapshot.

## The two-step July gate

HPCA collects an **abstract-and-conflict registration** roughly a week before the
full paper, both on HotCRP (`hpca<year>.hotcrp.com`). The registration step is not a
placeholder: it finalizes the conflict list and seeds reviewer assignment, so a
missed registration can forfeit the paper slot even if the PDF is ready. For HPCA
2027 the paper deadline is **July 24, 2026 (AoE)**, with registration about a week
earlier.

- Register the real title, abstract, authors, topics, and complete per-author
  conflicts by the registration cutoff — not placeholders you plan to fix.
- Treat the paper step as a second hard deadline, not an extension of the first.

## Format and anonymity audit

- Apply the current IEEE template without margin, font, or spacing hacks. Recent
  cycles cap the main body at **11 pages excluding references**, with a minimum
  **10pt font and 12pt leading**.
- References are **unlimited and uncounted** — but **each reference must list all of
  its authors**, or the paper can be rejected. Never abbreviate an author list with
  "et al." in the bibliography to save space.
- Enforce double-blind: no author names anywhere outside the HotCRP form, scrubbed
  PDF metadata, and fully anonymized artifact links (repositories, dataset hosts).
- Keep references **de-anonymized**: cite your own prior work in the third person,
  but do not remove or blind citations for anonymity.
- Disclose any AI-generated content in the **acknowledgments** per recent CFP
  wording; the acknowledgments themselves stay anonymous until camera-ready.

## Blocking risks

- Missed abstract-and-conflict registration, or an incomplete conflict list.
- Overlength main text or a modified template.
- A reference that omits authors (a stated reject trigger), or a bibliography blinded
  for anonymity.
- Author identity leaking through PDF metadata or a non-anonymized artifact link.
- Headline numbers with no named instrument (simulator/fidelity or machine/state).

## Desk-reject and triage table

| Trigger | Severity at HPCA | Repair window |
|---|---|---|
| Missed registration step | Lost paper slot | None after the cutoff |
| Overlength main text | Desk reject | None after the deadline |
| Template tampering | Desk reject or chair flag | None |
| Reference omits authors | Reject per CFP | Only before the deadline |
| Identity leak in PDF or artifact link | Desk reject | None |
| Missing AI-use disclosure | Policy flag | Fixable before the deadline |

## Final-week sequence for a simulation-plus-silicon paper

1. Freeze the mechanism description and figure set; renumber so reviewers can
   cross-reference.
2. Regenerate every figure from a scripted pipeline so PDF and artifact cannot
   diverge.
3. Verify each bibliography entry lists all authors, then scrub PDF metadata and
   anonymize every artifact URL.
4. Confirm the HotCRP abstract matches the PDF abstract, all fields are filled, and
   status reads **submitted** (not saved).
5. Re-run the registration-vs-paper check: the conflict list from step one still
   matches the author list.

## Output format

```text
[HPCA readiness] Ready / Needs fixes / Not ready
[Gate step] registration / paper
[Blocking checks] <registration/page/template/anonymity/references/AI-disclosure>
[Instrument risk] <one un-anchored number, or none>
[Desk-reject risk] <one issue>
[Fix order] <ordered fixes before the deadline>
```

Recheck the current CFP before trusting any number here: the 11-page cap, the
registration-to-paper gap, and the AI-disclosure wording are all per-edition.
