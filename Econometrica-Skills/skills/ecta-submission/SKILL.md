---
name: ecta-submission
description: Use when running the final pre-submission preflight for an Econometrica manuscript via Editorial Express — manuscript assembly, Supplemental Material, the 45-page limit, anonymization, references, the ES-member submission fee, and Data and Code Availability Policy compliance.
---

# Submission Preflight (ecta-submission)

## When to trigger

- "Submitting tomorrow"; final check before clicking submit on Editorial Express
- Unsure how to split the body (≤45 pages) vs. the Supplemental Material
- Unsure which files and declarations the portal needs

> Verify all volatile specifics — portal URL, submission fee, the current Data and Code
> Availability Policy, the editorial board, and formatting rules — on the official journal
> site before submitting. The figures below were re-checked on 2026-11-23 but change.

## Econometrica specifics (verify; re-checked 2026-11-23)

- **Membership + fee:** at least one author must be a member of the **Econometric Society**.
  Submission fee (from Jan 1, 2025): **US$125 regular member, US$50 student member**,
  non-refundable even on rejection without review. Invited resubmissions require only membership;
  authors residing in World Bank **low-income** countries are exempt (every coauthor must qualify
  for a discount/exemption to use it). Papers *transferred from* Econometrica to QE or TE pay no
  extra fee there. Accepted papers pay a **publication page fee** of 50% of production cost
  (currently US$12/page), waived for low- and lower-middle-income-country authors.
- **Length:** main text **≤45 pages including references and appendices**; font ≥12pt, line
  spacing ≥1.5, margins ≥1.25in. **Supplemental Appendix ≤25 pages**, same formatting;
  additional online Supplemental Material (proofs, Monte Carlo detail) is uploaded with the
  submission and does **not** count toward the limit.
- **Front matter:** abstract **≤150 words**, keywords required, **JEL codes optional**.
- **Portal:** **Editorial Express** (editorialexpress.com, `dbase=econometrica`).
- **Replication:** governed by the **Econometric Society** Data and Code Availability Policy;
  the **Data Editor** runs a reproducibility check at conditional acceptance; deposit at the
  ES Journals' Community on **Zenodo** (see `ecta-replication-package`).
- **Anonymization: not required.** The official submission instructions (re-checked
  2026-11-23) say the title page carries the abstract, keywords, and **full author
  affiliations**; Econometrica is single-anonymous (referees know the author).

## Pre-submission checklist

### Manuscript assembly

- [ ] Main text states the contribution / informal main theorem early
- [ ] Main text fits **≤45 pages incl. references and appendices**; font ≥12pt / spacing ≥1.5 / margins ≥1.25in
- [ ] Definitions and assumptions are numbered, displayed objects
- [ ] Theorems numbered consistently; cross-references by number
- [ ] Proof sketches in the body; **full proofs in the Supplemental Material** if long
- [ ] Supplemental Appendix **≤25 pages**; further Supplemental Material carries full proofs, Monte Carlo detail, additional results
- [ ] Every number in the text matches the tables
- [ ] Abstract **≤150 words**; keywords present; JEL codes (optional) included if used

### Supplemental Material

- [ ] Full, complete proofs of every result not proven in full in the body
- [ ] Complete Monte Carlo design and any additional simulations
- [ ] Additional theorems / extensions referenced from the body
- [ ] Supplemental Appendix within ≤25 pages; further material in unrestricted Supplemental Material
- [ ] Self-contained and cross-referenced from the main text

### Title page and author identity (single-anonymous — do not de-identify)

- [ ] Title page carries the abstract (≤150 words), keywords, and full author affiliations
- [ ] Optional footnote explaining how author order was determined, if non-alphabetical
- [ ] Self-citation phrased in the third person ("X (2020) shows") as a matter of style
- [ ] Re-check the Instructions page in case the blinding policy changes

### References

- [ ] Every in-text citation appears in the reference list and vice versa
- [ ] Theorem-level results cited precisely (which theorem, not just the paper) where the proof relies on them
- [ ] Reference style matches the journal's current requirement
- [ ] Foundational and contemporaneous work cited fairly

### Data and Code Availability Policy (Econometric Society)

- [ ] Replication package built and reproduces from a clean checkout (see `ecta-replication-package`)
- [ ] Monte Carlo / simulation tables reproduce bit-for-bit (seeds recorded) — simulations are in-scope
- [ ] Data provenance / access documented; restricted-data procedures handled
- [ ] README in **PDF** (Social Science Data Editors' template); Zenodo deposit planned (ES Journals' Community)
- [ ] If pure theory (no empirical/experimental/simulation results): exemption noted **at initial submission**
- [ ] Verified against the **current** ES Data Editor policy and deposit location

### Fee and member status

- [ ] Submission fee handled (US$125 regular / US$50 student member, from 2025 — verify current amounts)
- [ ] At least one author is a current Econometric Society member
- [ ] Fee-exemption checked (invited resubmission; all authors in World Bank low-income countries)

## Editorial Express operation

- Submit via **Editorial Express** (editorialexpress.com, `dbase=econometrica`; verify the
  current URL via the journal site).
- Upload the main manuscript and the Supplemental Material as the portal specifies.
- Enter abstract (≤150 words), keywords, and JEL codes (optional) accurately.
- Provide qualified, conflict-free referee suggestions (see `ecta-referee-strategy`).
- Choose the correct classification / field for routing to an appropriate co-editor.
- At **conditional acceptance**, final files (and the replication package) go to a separate
  Editorial Express account for the **Data Editor**'s reproducibility check.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue econometrica-skills   # from a clone of the AJS repository
```

It reports, with a location for each finding:

- this venue's machine-readable limits, review mode and required statements, when the venue has a
  rules block (`--list-venues`);
- citations ↔ references;
- table and figure numbering, cross-references and standard-error notes;
- abstract numbers traced to the tables;
- placeholders and tracked changes.

With the Research Toolkit pack installed, `rt-submission-readiness` runs the same check as stage 0
of the full pre-submission pipeline (scorecard → referee panel → polish → cover letter). Anything
it lists as *not checked* still needs the manual items below.

## Anti-patterns

- Submitting with proofs only in the body and the Supplemental Material not assembled
- A body over **45 pages** (incl. references and appendices) with no prior editor exception
- Submitting without an Econometric Society member among the authors, or unpaid fee
- Asymptotics in, Monte Carlo left for "the revision" — often a fast rejection
- A replication package that does not actually reproduce (the Data Editor will run it)
- An off-the-shelf applied paper with no methodological contribution (eligibility desk-reject)
- Citing a survey where the proof depends on a specific theorem
- Trusting a stale fee / board / policy figure instead of verifying on the journal site

## Output format

```
【Body ≤45pp + split】within limit + proofs split correctly: yes/no
【Supplemental Material assembled】yes/no — missing: [...]
【Title page】abstract ≤150 words + keywords + full affiliations: pass / fix: [...]
【References】in/out consistent: yes/no
【ES Data & Code Policy】reproduces + Zenodo plan / theory-exempt: yes/no
【Fee + ES membership】handled: yes/no (US$125/US$50 — verify)
【Next step】await decision / R&R / conditional acceptance → ecta-rebuttal
```

## Related resources

- [`templates/checklist.md`](templates/checklist.md) — full pre-submission self-check (manuscript, appendix, anonymization, proofs, simulations, references, replication, portal)
- [`templates/manuscript_template.md`](templates/manuscript_template.md) — standard theory/methods manuscript skeleton (assumptions, theorems, proof sketches, Supplemental Material)
- [`../../resources/external_tools.md`](../../resources/external_tools.md) — typesetting, symbolic/computation, and reproducibility toolchain
