---
name: osdi-submission
description: Use when running the final pre-upload audit of an OSDI submission on HotCRP — the December 1 / December 8, 2026 registration and full-paper deadlines at 5:59 pm EST (2:59 pm PST), the 12-page/no-appendix check and optional separate supplementary files, institution-level double-blind rules, the renamed-system requirement, track choice, the eight-submission author cap, the Volunteer Candidate Senior Reviewer, and the AI and resubmission rules.
---

# OSDI Submission

Run this audit before touching the HotCRP upload form. Every rule below is the OSDI
'27 cycle as re-verified on 2026-11-24 (`osdi27.usenix.hotcrp.com` plus the CFP and its
September/October 2026 updates); treat the numbers as one year's snapshot and reopen the
current CFP before acting — the CFP itself says process details may still be added.

## The two December gates, in US clock time

OSDI '27 splits the deadline in two, both at **5:59 pm EST (10:59 pm UTC)** — shown on
HotCRP as 2:59:59 PM PST, USENIX's local-afternoon convention, not AoE midnight. Both
are hard deadlines with no extensions:

- **Abstract registration (Tuesday, December 1, 2026):** title, a real abstract,
  authors, conflicts, the **track** (Research or Operational Systems), and the
  **Volunteer Candidate Senior Reviewer** (or exemption) created in HotCRP. Empty,
  placeholder or trivial abstracts are desk-rejected, which precludes submission;
  unregistered papers cannot be submitted a week later, full stop.
- **Complete paper (Tuesday, December 8, 2026):** the final anonymized PDF uploaded and
  marked complete, plus any supplementary files. HotCRP "complete" status is the state
  that counts — a draft sitting in the form is not a submission.

Convert 5:59 pm EST to every coauthor's time zone in writing. It is 10:59 pm in
London, 6:59 am *the next day* in Beijing — the single most common OSDI logistics
error is an AoE reflex from ML venues.

## Format gate (rejection-grade)

| Check | OSDI '27 rule |
|---|---|
| Body length | ≤ 12 single-spaced 8.5"×11" pages, **including figures and tables**; pages numbered |
| References | Unlimited extra pages |
| Appendices | **None in the submitted PDF** |
| Supplementary material | Optional, in **separate files**; PC members need not read it (`osdi-supplementary`) |
| Type/layout | 10-pt Times-like on 12-pt leading, two columns, 7"×9" text block; legible in black and white |
| Operational track | Title ends with "(Operational Systems)"; track marked on the title page and form |
| Per-author load | At most **eight submissions** per author; surplus desk-rejected |

Papers not meeting the format criteria are desk-rejected without review, with no
extension for reformatting. If volume requires an **early review round**, reviewers
read at least the first **two** pages and vote on advancing — so scope, readability and
the contribution must be clear by page 2.

The 12-page count including figures is stricter than it sounds: a figure-heavy systems
paper loses two pages to its own graphs. Compress via `osdi-writing-style`'s passes,
never via geometry or font tampering.

## Anonymity gate: OSDI's two distinctive rules

Beyond standard double-blind hygiene, OSDI '27 (continuing '26) imposes two
requirements authors from other venues miss:

1. **Institutions are anonymized too** (mandatory for the Research track, encouraged
   for Operational Systems). Not only names — the paper must not identify
   the authors' institutions explicitly or by implication. "Our datacenter fleet" plus
   a trace only one company could own is an implication; describe the deployment in
   neutral scale terms.
2. **The renamed-system rule.** Prior non-peer-reviewed exposure (arXiv, tech reports,
   talks, social posts) is permitted **only if the submission uses a different,
   anonymized project/system name** than any of those venues. Rename before the
   deadline, then sweep for the old name everywhere — body, figures, config listings,
   embedded paths.

```bash
# Mechanical sweep on the exact PDF you will upload
pdftotext paper.pdf - | grep -nEi 'OLDNAME|github\.com|gitlab|acknowledg|grant' | head
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'      # metadata identity
pdffonts paper.pdf | head                                    # embedded, expected fonts
# figures often embed usernames in paths: check figure sources too
grep -rnEi 'home/|Users/|OLDNAME' figures/ *.tex | head
```

Self-citations stay, in third person, treated as someone else's work
(`osdi-related-work` has the full protocol). Program co-chair conflicts are handled
by recusal on the PC side — your job is accurate conflict declaration in HotCRP, not
creative omission.

## Policy gate

- **Dual submission:** not under review elsewhere; concurrent arXiv is fine (renamed),
  concurrent conference review is not. **NSDI '27 Fall submissions** (notified the same
  day as the OSDI '27 deadline) count as simultaneous and are desk-rejected.
- **Resubmissions:** a paper previously rejected by another conference or journal must
  upload the prior-submission information and a summary of how it improved (shared with
  reviewers after reviews, before decisions); a related workshop paper is uploaded with
  an explanation of what is new.
- **AI:** a paper whose text was wholly or largely generated by AI is fraud; AI editing
  tools are fine; if **coding agents** helped build the system, disclose it in the paper
  (e.g., the Implementation section). The USENIX Authorship Policy applies.
- **Senior reviewer:** name one author (PhD or equivalent, significant OSDI/SOSP-class
  record, not on the PC) as the **Volunteer Candidate Senior Reviewer**, who may review up
  to four papers — or mark the paper exempt.
- **Track sanity:** an experience paper registered as Research (or vice versa) is
  reviewed against the wrong bar — re-check the registration before the December 1 gate
  closes (`osdi-topic-selection`).
- **Ethics:** authors must abide by the **ACM Code of Ethics** (Requirements for Authors);
  no out-of-band contact with PC members. If measurements involved production users,
  disclosed vulnerabilities, or third-party infrastructure, address the ethics posture
  in the paper.

## HotCRP field hygiene

The form is read before the PDF and drives assignment; draft it before deadline day:

- **Title and abstract** must match the PDF verbatim — reviewers bid on the form,
  and drift between form and paper reads as carelessness.
- **Topics/keywords** route the paper to reviewers: pick for the reviewer you want
  (storage vs ML-systems vs distributed) rather than checking everything plausible.
- **Author list complete at registration**, even though anonymized in the PDF —
  HotCRP uses it for conflict computation, and a coauthor added after review
  assignment is a chairs-level problem.
- **Conflicts**: declared per the CFP's definitions (institution, advisor, collaboration
  from December 2024 through December 2026, close family), accurately and no wider — conflict inflation to dodge feared
  reviewers is detectable and sanctionable.
- The eight-per-author cap counts *submissions on the form*, so groups running
  multiple December papers should reconcile author lists before registration week.

## Why this audit is terminal at OSDI

OSDI '26 removed the **author-response period** and the OSDI '27 CFP describes none. There is no later moment to explain that
the missing baseline exists, that the leak was an oversight, or that page 13 was an
accident. The submission as uploaded is the entire conversation until notification —
which is also why the last step is non-negotiable: **re-download the PDF from HotCRP
and read it cold**, checking that what reviewers will open is what you think you sent.

## Final sequence

1. T-7 days: register title/abstract/track/senior reviewer (December 1 gate).
2. T-3 days: freeze content; run the format gate table top to bottom.
3. T-2 days: anonymity sweep (mechanical checks above + a human pass over figures).
4. T-1 day: coauthor sign-off on the exact PDF; HotCRP fields match the PDF verbatim.
5. T-0: upload, mark complete, re-download, cold-read, archive the receipt.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue osdi-skills   # from a clone of the AJS repository
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

## Output format

```text
[Gate status] registration / format / anonymity / policy — each pass/fail
[Clock] local-time equivalent of the 5:59 pm EST deadline; hours remaining
[Form] senior reviewer or exemption / resubmission summary / workshop upload / supplement
[Anonymity findings] <leak list or clean> incl. institution-implication check
[Renamed system] old name absent from body/figures/metadata? yes/no
[Terminal risks] items that cannot be explained later (no response period)
[Fix order] <ordered blockers before upload>
```
