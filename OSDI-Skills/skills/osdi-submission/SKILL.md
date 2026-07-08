---
name: osdi-submission
description: Use when running the final pre-upload audit of an OSDI submission on HotCRP — the December registration and full-paper deadlines at 2:59 pm PST, the 12-page/no-appendix check, institution-level double-blind rules, the renamed-system requirement, track choice, and the eight-submission author cap.
---

# OSDI Submission

Run this audit before touching the HotCRP upload form. Every rule below is the OSDI
'26 cycle as read on 2026-07-08 (`osdi26.usenix.hotcrp.com` plus the CFP); treat the
numbers as one year's snapshot and reopen the current CFP before acting.

## The two December gates, in Pacific time

OSDI '26 split the deadline in two, and both were **2:59 pm PST** — USENIX's local
afternoon convention, not AoE midnight:

- **Registration (Dec 4, 2025):** title, abstract, authors, and **track** (Research or
  Operational Systems) created in HotCRP. Unregistered papers cannot be submitted a
  week later, full stop.
- **Full submission (Dec 11, 2025):** the final anonymized PDF uploaded and marked
  complete. HotCRP "complete" status is the state that counts — a draft sitting in
  the form is not a submission.

Convert 2:59 pm PST to every coauthor's time zone in writing. It is 10:59 pm in
London, 6:59 am *the next day* in Beijing — the single most common OSDI logistics
error is an AoE reflex from ML venues.

## Format gate (rejection-grade)

| Check | OSDI '26 rule |
|---|---|
| Body length | ≤ 12 pages, single-spaced, **including figures and tables** |
| References | Unlimited extra pages |
| Appendices | **Forbidden in the submission** — no supplementary material |
| Type/layout | 10-pt Times-like on 12-pt leading, two columns, 7"×9" text block |
| Length norm | "The right length" — reviewers told to down-rank padded papers |
| Per-author load | At most **eight submissions** per author across the PC's pile |

The 12-page count including figures is stricter than it sounds: a figure-heavy systems
paper loses two pages to its own graphs. Compress via `osdi-writing-style`'s passes,
never via geometry or font tampering.

## Anonymity gate: OSDI's two distinctive rules

Beyond standard double-blind hygiene, OSDI '26 imposed two requirements authors from
other venues miss:

1. **Institutions are anonymized too.** Not only names — the paper must not identify
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
  concurrent conference review is not.
- **Track sanity:** an experience paper registered as Research (or vice versa) is
  reviewed against the wrong bar — re-check the registration before the Dec 4 gate
  closes (`osdi-topic-selection`).
- **Ethics:** if measurements involved production users, disclosed vulnerabilities, or
  third-party infrastructure, address the ethics posture in the paper; check the
  current CFP's exact ethics wording (marked 待核实 in the source map) rather than
  assuming any specific code applies.

## HotCRP field hygiene

The form is read before the PDF and drives assignment; draft it before deadline day:

- **Title and abstract** must match the PDF verbatim — reviewers bid on the form,
  and drift between form and paper reads as carelessness.
- **Topics/keywords** route the paper to reviewers: pick for the reviewer you want
  (storage vs ML-systems vs distributed) rather than checking everything plausible.
- **Author list complete at registration**, even though anonymized in the PDF —
  HotCRP uses it for conflict computation, and a coauthor added after review
  assignment is a chairs-level problem.
- **Conflicts**: declared per HotCRP's definitions (advisors, recent coauthors,
  same institution), accurately and no wider — conflict inflation to dodge feared
  reviewers is detectable and sanctionable.
- The eight-per-author cap counts *submissions on the form*, so groups running
  multiple December papers should reconcile author lists before registration week.

## Why this audit is terminal at OSDI

OSDI '26 had **no author-response period**. There is no later moment to explain that
the missing baseline exists, that the leak was an oversight, or that page 13 was an
accident. The submission as uploaded is the entire conversation until notification —
which is also why the last step is non-negotiable: **re-download the PDF from HotCRP
and read it cold**, checking that what reviewers will open is what you think you sent.

## Final sequence

1. T-7 days: register title/abstract/track (Dec 4 gate).
2. T-3 days: freeze content; run the format gate table top to bottom.
3. T-2 days: anonymity sweep (mechanical checks above + a human pass over figures).
4. T-1 day: coauthor sign-off on the exact PDF; HotCRP fields match the PDF verbatim.
5. T-0: upload, mark complete, re-download, cold-read, archive the receipt.

## Output format

```text
[Gate status] registration / format / anonymity / policy — each pass/fail
[Clock] local-time equivalent of the Pacific deadline; hours remaining
[Anonymity findings] <leak list or clean> incl. institution-implication check
[Renamed system] old name absent from body/figures/metadata? yes/no
[Terminal risks] items that cannot be explained later (no response period)
[Fix order] <ordered blockers before upload>
```
