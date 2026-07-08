---
name: kdd-camera-ready
description: Use when preparing an accepted KDD paper for ACM proceedings, covering the 12-page proceedings budget with 9 content pages, the extra content page over the submission, the 3-page cap on references plus appendix, ACM e-rights and TAPS source processing, ACM Open APC status, de-anonymization, and Digital Library metadata for SIGKDD.
---

# KDD Camera Ready

Use this after acceptance. KDD publishes through ACM, which means the final version is
not "the PDF you upload" — it is the output of ACM's production pipeline (e-rights,
then TAPS) applied to your **source files**. Papers that compile locally but violate
acmart conventions stall in TAPS, so start this process the week the decision arrives,
not the week the proceedings deadline arrives.

## The page arithmetic (2026 anchor — reverify per cycle)

Accepted KDD 2026 papers all received the same proceedings budget: **12 pages total,
of which 9 are content pages**. Since submissions were 8 content pages, acceptance
buys exactly **one extra content page**, while references and appendix together must
fit in the remaining **3 pages**.

- Spend the ninth page deliberately: reviewer-requested ablations, the scoping
  sentences promised in rebuttal, and de-anonymized acknowledgements all compete for it.
- The 3-page references+appendix cap is the trap: submissions with long optional
  appendices must **cut appendix material**, not just add a page. Decide early what
  migrates into the body, what moves to the public repository, and what dies.
- Keep section, table, and algorithm numbering aligned with the reviewed version where
  possible, so the AC's conditional-acceptance notes remain checkable.

## ACM production pipeline

The standard ACM sequence KDD rides on:

1. **e-rights form** — the contact author receives the rights email; the paper's final
   title/author list must be frozen before completing it, because the form stamps the
   copyright block and DOI metadata.
2. **TAPS upload** — a zip of LaTeX source (or Word), named per instruction, which TAPS
   compiles into both the PDF and the HTML5 Digital Library version.
3. **Proof review** — check the generated proofs; HTML rendering surfaces errors the
   PDF hides.

```bash
# Typical TAPS package hygiene before zipping (KDD-specific naming: see the
# acceptance email; the zip name encodes proceedings acronym + paper id)
grep -rn "anonymous" main.tex sections/*.tex   # leftover anonymity flags
grep -rn "\\\\vspace\|\\\\baselineskip" *.tex  # spacing hacks TAPS rejects
grep -rn "includegraphics" *.tex | wc -l       # every figure file must ship in the zip
biber --tool --validate-datamodel refs.bib     # broken .bib entries stall TAPS builds
```

Switch the document class options from `[sigconf,anonymous,review]` to `[sigconf]`,
add the rights commands TAPS emails you (`\setcopyright`, conference metadata), and
never hand-edit the copyright block.

## De-anonymization sweep

| Item | Submission state | Camera-ready state |
|---|---|---|
| Author block + affiliations | Stripped by `anonymous` | Restored, order frozen pre-e-rights |
| Acknowledgements, grants | Absent | Restored (costs body space) |
| Repository reference | Anonymized mirror | Public, licensed, DOI/URL stable |
| Self-citations | Third person | Natural first person where clearer |
| ADS deployment context | Possibly genericized | Name the system/org to the extent employer policy allows |
| CCS concepts + keywords | Often placeholder | Final — they drive DL indexing |

Test the public repository logged out; a camera-ready pointing at a still-private repo
is the most common post-publication complaint at ACM venues.

## Money and access

- KDD proceedings live in the ACM Digital Library under the **ACM Open** model: authors
  from institutions not participating in ACM Open face an article-processing charge
  unless they qualify for a waiver; ACM announced a temporary 65% subsidy for 2026.
  Check your institution's ACM Open status before budgeting — this surprises industrial
  and non-Western labs most.
- Exact APC amounts, waiver mechanics, registration pricing, and presentation
  obligations were not verifiable at pack-build time (待核实): confirm all four against
  the acceptance email and the current conference pages.

## Worked example: spending the ninth page

An accepted Research Track paper has three claims on the extra content page: the AC's
conditional note asked for a scoped limitations paragraph; R3 requested the
sensitivity analysis currently in Appendix C; and the authors want a new "extensions"
subsection. Allocation logic:

1. The AC's conditional item is non-negotiable — it lands first (≈0.25 page).
2. The reviewer-requested sensitivity table migrates from appendix to body — this
   also relieves the 3-page refs+appendix cap, solving two constraints at once
   (≈0.5 page).
3. The new extensions subsection loses: content never reviewed should not enter the
   version of record beyond clarification. It belongs in the repository README or the
   next paper.

The heuristic: the ninth page pays review debts before it buys new real estate.

## Proceedings metadata checklist

- Title and abstract in TAPS metadata match the PDF exactly — the DL indexes the
  metadata, not the PDF.
- CCS concepts and keywords chosen deliberately; they drive Digital Library search
  and recommendation for the paper's whole life.
- Author name forms consistent with each author's prior DL records (initials vs full
  names split citation counts).
- ORCIDs attached; funding acknowledgements in the format your grants require.
- The repository/dataset DOI cited in the final text is the archival one, not a
  branch URL that will rot.
- If the conference collects presentation or poster assets separately, that pipeline
  is distinct from TAPS — track both.

## Timeline discipline

- Camera-ready deadlines for the current cycle were not verifiable at pack-build
  time (待核实) — take them from the acceptance email, and assume the window is
  short: dual-cycle venues compress production schedules.
- Do the TAPS dry run in week one: compile the de-anonymized source with the rights
  commands stubbed in, and fix acmart violations before the real upload window.
- Author-order changes after e-rights are painful to impossible; settle order
  disputes before anyone touches the form.

## Output format

```text
[Camera-ready status] on-track / blocked-at-TAPS / blocked-at-rights / not started
[Page budget] content: <n>/9, refs+appendix: <n>/3, total: <n>/12
[Pipeline stage] e-rights / TAPS upload / proofs / done
[De-anonymization] <items restored, repo publicly reachable yes-no>
[ACM Open status] covered / APC due (amount 待核实) / waiver requested
[Conditional-acceptance items] <AC-required change -> where it landed>
```
