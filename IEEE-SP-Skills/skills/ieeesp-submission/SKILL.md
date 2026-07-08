---
name: ieeesp-submission
description: Use when auditing an IEEE S&P (Oakland) submission for HotCRP readiness, including the registration freeze with ORCID matching, the 13-page/18-page compsoc format, anonymization, the Ethics Considerations field, SoK checkbox, conflict declarations, and the desk-reject triggers specific to S&P cycles.
---

# IEEE S&P Submission

Use this as the final audit before a paper enters an S&P cycle on HotCRP.
S&P's desk-reject rules are unusually mechanical — page counts, ORCID
matching, and registration completeness are enforced without review — so
most preventable losses happen in the upload week, not in review.

## The two-deadline structure

An S&P cycle has a **registration deadline** and a **paper deadline** about a
week apart, and the registration is binding: title, full abstract, complete
author list, ORCIDs, and conflicts are frozen when registration closes
(cycle1.sp2027.ieee-security.org/deadlines, checked 2026-07-08). Audit
registration as its own deliverable:

- Every author has an ORCID whose **email and name match the HotCRP record**
  — the 2027 CFP desk-rejects papers that violate this.
- The abstract entered at registration is the real abstract, not a
  placeholder; it routes reviewers and cannot be swapped later.
- Conflicts are declared per the current CFP's conflict definition; both
  missing and fabricated conflicts are chair-level problems.
- The **Ethics Considerations** field is filled with substance at
  registration time (see `ieeesp-review-process` for how the REC uses it).
- SoK papers have the `SoK:` title prefix **and** the SoK checkbox — one
  without the other misroutes reviewing.

## Format gate

| Rule (2027 CFP, checked 2026-07-08) | Enforcement |
|---|---|
| ≤ 13 pages of body text | Over-length ⇒ rejected without review |
| ≤ 5 further pages, references + appendices only | Same |
| Hard ceiling 18 pages total | Same |
| Everything past page 13 clearly marked as appendix | Reviewer-visible violation |
| IEEE "compsoc" conference-proceedings LaTeX template | Tampering ⇒ desk-level flag |
| Anonymized submission | Identity leak ⇒ desk reject |

Two S&P-specific implications. Reviewers are **not required to read
appendices**, so a proof, an ablation, or the adaptive-attack evaluation that
the acceptance case depends on must live in the first 13 pages. And the
compsoc template's two-column layout eats wide tables and long listings —
compress artifacts early, not on deadline night.

## Anonymization with security-paper edges

Security submissions leak identity in ways generic checklists miss:

- **Disclosure trails** — "we reported this to Vendor X in March" plus a CVE
  number can uniquely identify the reporting group; write disclosure evidence
  in venue-neutral terms ("the affected vendors were notified on <date>;
  identifiers omitted for anonymity") unless the current CFP says otherwise.
- **Artifact hostnames and scan origins** — measurement infrastructure IPs,
  institutional network names in traces, and cloud project IDs in scripts.
- Self-citations go in the **third person**, per the CFP.
- PDF metadata, embedded fonts from institutional templates, and figure
  source paths (`/home/<user>/...`) all deanonymize.

```bash
# Mechanical pass before upload
pdfinfo paper.pdf | grep -iE 'author|creator'        # metadata
pdftotext paper.pdf - | grep -inE 'our (prior|previous) work|we reported|CVE-20'
grep -rniE '(\.edu|\.ac\.|corp)/|/home/[a-z]' figures/ scripts/ || true
```

## Upload-week order of operations

1. Freeze the threat model and claims; no new results after this point.
2. Run the anonymization sweep above on the PDF **and** any linked artifact.
3. Verify page arithmetic: body ends on or before p.13, total ≤ 18, appendix
   pages labeled.
4. Complete registration: authors, ORCIDs, conflicts, abstract, Ethics
   Considerations, SoK checkbox if applicable.
5. Upload the paper; re-download from HotCRP and re-check the rendered PDF —
   font substitution has broken compsoc submissions before.
6. Confirm the HotCRP abstract matches the PDF abstract.

## Desk-reject triage

| Trigger | Repairable after deadline? |
|---|---|
| Missing/mismatched ORCID for any author | No — desk reject |
| Body text past page 13 or total > 18 | No — rejected without review |
| Author list change after registration | No — frozen |
| Identity leak in PDF or artifact | No |
| Weak Ethics Considerations entry | No new entry; damage lands in review/REC |
| Thin adaptive-attack evaluation | Review-stage damage; fix before, not after |

## Output format

```text
[S&P upload readiness] Ready / Needs fixes / Not ready
[Registration] authors+ORCIDs ✓/✗ · abstract ✓/✗ · conflicts ✓/✗ · ethics field ✓/✗
[Format] body ≤13 ✓/✗ · total ≤18 ✓/✗ · compsoc ✓/✗ · appendix marked ✓/✗
[Anonymity] pdf metadata / disclosure trail / artifact origins: <findings>
[Highest desk-reject risk] <one item>
[Fix order] <ordered list before the registration deadline>
```
