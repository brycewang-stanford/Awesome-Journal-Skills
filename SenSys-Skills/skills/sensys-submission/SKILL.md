---
name: sensys-submission
description: Use when running the final pre-upload audit of a SenSys submission — confirming the right per-edition HotCRP site and which of the two deadlines is open, the AoE cutoff in local time, the 12/6-page double-column cap, the double-blind sweep including hardware and deployment leaks, and the resubmission-with-revision contract at the second deadline.
---

# SenSys Submission

Order the checks by how permanent the mistake is. A paper aimed at the wrong deadline, or a
first-deadline reject re-entered without its required revision, is bounced before a reviewer ever
opens it — nothing recovers that. Formatting and anonymity slips, by contrast, are fixable right
up to upload. So the audit below front-loads the irreversible gates and leaves the mechanical
sweeps for last. Treat every number as the 2026/2027 snapshot; the live HotCRP `/deadlines` page
overrides it.

## Gate 1 — the deadline is real and yours

SenSys submits through a **per-edition HotCRP instance** (e.g. `sensys27.hotcrp.com`) and offers
**two deadlines per cycle**, each fully reviewed on its own. Confirm on the deadlines page:

- Whether the **open deadline is the first or the second**, and **which edition it feeds** — a
  mid-cycle submission competes for that edition's program, not one already decided.
- Whether this edition requires **abstract registration** ahead of the paper, and its date.
- That the cutoff is **AoE**, then convert it to each coauthor's wall clock — a Paris or New York
  time printed on the page is nobody's local midnight.

The resubmission gate is the one authors miss: if you are re-entering a first-deadline reject at
the second deadline, the submission is **invalid without a substantive revision and a "Response
to Reviewers"** tying each prior concern to a concrete change (`sensys-author-response`). A
repackaged reject is a desk reject.

## Gate 2 — the geometry is legal

| Item | Rule (2027 cycle) | How to check |
|---|---|---|
| Full paper | ≤ 12 pages including figures and tables | Count the compiled PDF |
| Short paper | ≤ 6 pages (vision/experience track) | Confirm which track you entered |
| References | unlimited, beyond the cap | Nothing load-bearing tucked among them |
| Appendices | optional, after references, beyond the cap | Nothing a reviewer must read to believe the claim |
| Template | ACM double-column, geometry from the class file | Diff against the template; never resize by hand |

At SenSys the cap pressure is *figures* — power traces, latency CDFs, and testbed schematics eat
the body. Relieve it by cutting content, not by `\vspace` tricks or shrinking a measurement plot
past legibility; production and reviewers both notice. The exact template version and font floor
are 待核实 for the cycle — read the CFP.

## Gate 3 — nobody can tell whose paper it is

Beyond the standard anonymization (no names, affiliations, funding lines, or acknowledgments;
third-person self-citation; references intact), SenSys papers leak identity through their
*hardware and deployments*. Sweep the exact upload candidate:

```bash
# 1. text + metadata identity
pdftotext final.pdf - | grep -niE 'acknowledg|funded by|grant no|@[a-z]+\.(edu|com)'
pdfinfo final.pdf | grep -iE 'author|creator|producer'
# 2. paths and un-blinded artifact hosts
grep -rniE 'github\.com/[a-z0-9_-]+|zenodo\.org|/home/[a-z]+|/Users/[a-z]+' *.tex figures/
# 3. the SenSys-specific tell: a nameable site, testbed, or deployment
pdftotext final.pdf - | grep -niE 'our (lab|building|campus|deployment|testbed)|[A-Z][a-z]+ Hall|room [0-9]+|IRB'
```

Strings are the easy part. A "30-node testbed across our engineering building" beside a photo of
a distinctive atrium narrows to one group; soften identifying specifics to scale-descriptive
language. And every artifact URL must resolve to a **blinded** repo or an author-stripped Zenodo
deposit. A machine finds the strings; only a human reading for *implication* catches the rest —
hand the PDF to a non-author and ask what lab they'd guess.

## Gate 4 — the form and the policies

The HotCRP record is read before the PDF: title and abstract must match the paper word for word;
topic tags steer the paper toward the sensing / embedded / IoT / on-device-AI reviewers you want
bidding, so pick for reviewer fit rather than breadth; and the full author list is registered for
conflict computation even while the PDF stays blind — a late author addition after assignment is a
chairs-level problem. Declare conflicts exactly as the site defines them. Then clear the policy
gates: no concurrent submission elsewhere; a stated delta for any overlapping workshop or poster;
human-subjects and third-party-infrastructure handling addressed (wording 待核实); and the cycle's
AI-use rule read live rather than assumed.

## Run-of-show

```text
T-8d  account on the right instance + deadline; form fields drafted; conflicts entered
T-7d  abstract registered if required; topic tags chosen for reviewer fit
T-2d  content freeze; Gates 2-3 run on the near-final PDF; resubmission packet attached
T-1d  coauthors sign off; HotCRP title/abstract match the PDF verbatim
T-0   upload → status ready; then re-download the stored file and open it — only server bytes count
```

## Report back

```text
[Gate1] instance + first/second deadline + edition fed + AoE cutoff in local time
[Gate2] full/short track + page/column/template verdict
[Gate3] mechanical hits + human-read verdict (deployment + artifact-link giveaways)
[Resub] revision + Response-to-Reviewers attached? (second-deadline re-entry only)
[Gate4] form verbatim-match + conflicts + dual-sub/ethics/AI each cleared or flagged
[Open]  live blockers, most-permanent first, each with an owner and hours-to-fix
```
