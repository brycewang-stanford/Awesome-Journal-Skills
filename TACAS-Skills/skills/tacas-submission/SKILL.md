---
name: tacas-submission
description: Use when auditing a TACAS (ETAPS) submission for EasyChair readiness, covering the choice among the four paper categories (research, case-study, regular tool, tool-demonstration), the correct LNCS page limit and llncs.cls format, the per-category blind mode (double-blind research vs single-blind tool/case-study), the mandatory tool-paper artifact deadline, and desk-reject triage before the firm ETAPS deadline.
---

# TACAS Submission

Run this audit before uploading to the TACAS **EasyChair** site. TACAS is a main conference of
**ETAPS**, publishing in **Springer LNCS** (gold open access), and — unlike a single-track venue —
it has **four paper categories** whose rules differ in page limit, anonymity, and artifact
obligation. Every number below was read from the TACAS 2026 / ETAPS 2026 joint call on 2026-07-09
via search renderings of the `etaps.org` pages (see `resources/official-source-map.md`); treat them
as a one-cycle snapshot and reopen the live call first. ETAPS deadlines are advertised as **firm
and not extended**.

## Step 0 — pick the category (it sets every other rule)

| Category | Page limit (llncs.cls) | Blind mode | Artifact |
|---|---|---|---|
| Regular research paper | ≤16 pages | **Double-blind** | Voluntary, post-acceptance |
| Case-study paper | ≤16 pages | Single-blind | Voluntary, post-acceptance |
| Regular tool paper | ≤16 pages | Single-blind | **Mandatory**, submitted after the paper, gates acceptance |
| Tool-demonstration paper | ≤6 pages | Single-blind | **Mandatory**, submitted after the paper, gates acceptance |

Page limits **exclude the bibliography and a clearly marked appendix**. Choosing the wrong category
is a substantive error, not a label: a research paper submitted as a tool paper will be held to a
tool paper's artifact bar, and vice versa. If unsure, run `tacas-topic-selection` first.

## Format and page budget

- **Springer LNCS `llncs.cls`**, unmodified. This is the LNCS path, not ACM `acmart` or IEEE
  `IEEEtran` — do not carry a template habit from a sibling venue.
- **Page limit for your category** (16 or 6), counting all text and figures but **not** references
  or an end appendix. Material that does not fit may go in the appendix and/or a supplementary
  website, with access enabled and license clear.
- Margins, font, and spacing are fixed by `llncs.cls`; recover space by editing, never by shrinking
  the template.

## The blind sweep — but only where it applies

Anonymity at TACAS is **per category**. A **regular research paper is double-blind**; a case-study,
regular tool, or tool-demonstration paper is **single-blind** and names its authors and tool.

For a **regular research** paper, run the mechanical anonymity pass:

```bash
# Research-paper (double-blind) anonymity check on the final PDF and any review artifact
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|gitlab|zenodo\.org/record|acknowledg|grant|thanks' | head
grep -rniE 'our (tool|group|lab)|university of|@[a-z0-9.]+\.edu' artifact/ --include='*.md' | head
```

Omit author names and institutions, cite your own prior work **in the third person**, drop
identifying acknowledgements, and route any supplementary link through an anonymizing host. For a
**tool or case-study** paper, do the opposite: name the tool clearly and make authorship and
provenance unambiguous — anonymizing a single-blind tool paper is itself a mistake.

## The mandatory-artifact reality (tool and tool-demo papers)

For a **regular tool** or **tool-demonstration** paper the artifact is **not optional and not
post-acceptance**: it is submitted shortly after the paper (TACAS 2026: paper 16 Oct 2025,
mandatory artifact 30 Oct 2025), evaluated **in parallel with the PC**, and its outcome **feeds the
acceptance decision**. Plan the packaging before the paper deadline, not after. See
`tacas-artifact-evaluation`.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Wrong category for the contribution | Held to the wrong bar | Re-scope to research / case-study / tool / tool-demo before submitting |
| Over the category page limit | Desk-reject-grade | Cut or move to appendix/website; references and appendix do not absorb body text |
| `llncs.cls` altered (margins, font) | Format violation | Recompile clean, recover space editorially |
| Research paper not anonymized | Double-blind violation | Strip names, third-person self-cites, scrub PDF metadata, re-anonymize artifact |
| Tool/tool-demo paper with no artifact ready | Cannot meet the mandatory deadline | Build and stage the artifact now; it gates acceptance |
| Same work under review / published elsewhere | Dual-submission | Withdraw one venue; confirm the current concurrent-submission wording |

## Final-week order of operations

1. Confirm the **category** and its page limit; freeze the body early.
2. For a research paper, run the anonymity sweep on the **final** PDF and any review artifact; for a
   tool/case-study paper, confirm the tool and authorship are clearly named.
3. For a tool / tool-demo paper, stage the **mandatory artifact** and its VM packaging on the
   post-paper deadline.
4. Fill every EasyChair field — category, topics, co-authors, conflicts — a day early.
5. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Page limits per category and the current `llncs.cls` revision.
- The per-category blind wording and which categories carry a mandatory artifact.
- Exact ETAPS dates, the abstract/full-paper gap, and dual-submission and AI-disclosure rules — all
  cycle-volatile.

## Output format

```text
[TACAS submission status] ready / blocked / needs work
[Category] research / case-study / regular tool / tool-demonstration
[Format] pages used (limit 16/6), llncs.cls compliance
[Blind mode] double-blind (research): clean / leaks: <where>  |  single-blind (other): named correctly? yes/no
[Artifact] mandatory (tool/tool-demo) staged? / voluntary (research/case-study) planned?
[Fix queue] <ordered, with owners and dates before the firm ETAPS cutoff>
```
