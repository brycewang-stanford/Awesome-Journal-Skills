---
name: icalp-submission
description: Use when auditing an ICALP (EATCS) Track A or Track B submission for HotCRP readiness, covering the correct-track submission server and (for Track B, since ICALP 2027) the choice of submission round, the no-page-limit full-version format whose first ten pages after the title page must carry the paper, lightweight double-blind anonymity, the AI-use disclosure, the no-simultaneous-submission rule, and the February AoE cutoff.
---

# ICALP Submission

Run this audit before uploading to the ICALP HotCRP site. ICALP — the EATCS International Colloquium
on Automata, Languages, and Programming — is a **pure theory venue** publishing open-access in
**LIPIcs**, with **two tracks** on **separate HotCRP servers**. Track A has one February deadline;
since ICALP 2027, **Track B has two rounds** (a September round and the usual February round; a paper
goes to one only). The paper is judged on its **theorems and proofs**, so this audit is about format,
anonymity, and making the first ten pages carry the result, not about a runnable artifact. The rules
below were read on 2026-11-24 by direct fetch of the ICALP 2027 Track B call
(`https://icalp.uj.edu.pl/track-b/`) and the ICALP 2026 call (see `resources/official-source-map.md`);
the ICALP 2027 Track A call and round-2 dates were not yet posted. Treat them as a one-cycle snapshot
and reopen the live call.

## Pick the right track first

ICALP has two tracks on **two different HotCRP sites** — submitting to the wrong one is a real,
avoidable failure:

- **Track A — Algorithms, Complexity and Games** → `icalp2027-a.hotcrp.com` (ICALP 2026:
  `icalp26-a.hotcrp.com`).
- **Track B — Automata, Logic, Semantics and Theory of Programming** → `icalp2027-b.hotcrp.com`
  (ICALP 2026: `icalp26-b.hotcrp.com`).

If you are unsure, resolve it with `icalp-topic-selection` before touching HotCRP; the tracks have
different program committees, Track B carries a rebuttal (in each round), and in ICALP 2026 Track A
contacted authors only on correctness issues.

## Deadlines and rounds

- **ICALP 2027 Track B, round 1:** submissions **15 September 2026** (AoE), rebuttal 5-9 November
  2026, notification 8 December 2026 — now closed. The decision is final: a round-1 reject cannot be
  resubmitted to round 2, and a paper may go to only one round.
- **ICALP 2027 Track B round 2 and Track A (its only round):** dates **TBA** on 2026-11-24; DMANET
  announced round 2 as "as usual, early-mid February 2027". Deadlines are firm.
- **Abstract registration:** ICALP 2026 had one a few days before the paper (**3 February 2026**,
  paper **6 February 2026**). Whether round 2 of ICALP 2027 has one is not yet posted — check
  HotCRP. If it does, register with the *real* title and abstract; the abstract drives PC bidding.

## Format: no page limit, but the first ten pages decide

- **There is no page limit** (ICALP 2026, both tracks; ICALP 2027 Track B). Authors are encouraged
  to submit the **full version**. The submission starts with a **title page**: title, no author
  information, and an abstract.
- Within the **first ten pages after the title page**, the paper must clearly present its merits,
  main contributions, and the key concepts and technical ideas. Everything beyond the abstract,
  references and those ten pages is read **at the committee's discretion**.
- The submission **must provide proofs** that allow the mathematical claims to be verified.
- Typesetting: readable fonts (e.g. 11-point), single column, ample spacing (e.g. single-spaced
  lines and 1-inch margins); pdflatex or similar is mandatory. The **LIPIcs document class is
  recommended** in the ICALP 2027 Track B call, and the **camera-ready must follow the LIPIcs
  style** — so most authors write in LIPIcs from the start.
- Do not mistake "no page limit" for "no budget": a result whose case only becomes clear on page 25
  has not been made in the pages every reviewer reads (see `icalp-supplementary`). (The 15-page
  extended-abstract cap was the ICALP 2025 rule; do not apply it.)

## Lightweight double-blind sweep

ICALP runs **lightweight double-blind** review: submissions are anonymous and self-references must be
**third person**. This is a *lightweight* regime — the goal is an unbiased first read, not making
authorship undiscoverable — but the mechanical leaks still cost you:

```bash
# Mechanical pass on the submission PDF
pdfinfo paper.pdf | grep -Ei 'author|creator|producer'        # scrub identifying metadata
pdftotext paper.pdf - | grep -nEi 'acknowledg|thanks|this work was supported|grant (no|number)' | head
pdftotext paper.pdf - | grep -nEi 'in our (previous|earlier) (work|paper)|as we showed in' | head
pdftotext paper.pdf - | grep -nEi 'github\.com/[a-z0-9-]+|/home/|/Users/' | head
```

The theory-specific leaks: an acknowledgements block, a grant number, "in our previous work [12]"
(rewrite as "in the work of [12]"), and an arXiv/ECCC identifier that de-anonymizes. It is fine for a
full version to exist on arXiv — just do not point at it in a way that breaks the blind.

## The no-simultaneous-submission rule

ICALP forbids **prior publication** and **simultaneous submission** to any other conference or
journal. A paper concurrently under review at STOC, FOCS, SODA, LICS, or a journal is ineligible.
Posting a **full version on arXiv/ECCC/HAL is allowed and encouraged** — that is not "publication."

## AI-use disclosure (ICALP 2027)

The ICALP 2027 call requires that **use of AI tools for conducting the research be disclosed in the
submitted paper**, with the specific uses described in detail (research design, theories and
algorithms, experiments, data, coding, analysis, testing, assisting with writing, or anything
directly relevant to the conclusions). All named authors are accountable for the content. If AI was
used, add the disclosure to the paper before upload; reviewers are barred from feeding submissions
to external AI tools.

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Merits, contributions and key ideas not clear within the first ten pages after the title page | Weak first read; reviewers need not read further | Restructure so the theorem, its improvement and the proof idea land by page ten |
| Non-standard typesetting (tiny fonts, double column, cramped margins) | Risk of rejection without consideration of merit | Recompile single-column, ~11-point, 1-inch margins (LIPIcs class recommended) |
| AI used in the research but not disclosed | Policy violation (ICALP 2027) | Add the disclosure describing the specific uses |
| Track B paper rejected in round 1 resubmitted to round 2 | Not allowed | Route elsewhere (`icalp-topic-selection`) |
| Submitted to the wrong track | Mis-review / reject | Withdraw and resubmit to the correct HotCRP server before the deadline |
| Author identity leaks (metadata, acks, first-person self-cite) | Anonymity violation | Scrub metadata, remove acks, rewrite self-citations in third person |
| Abstract not registered by the earlier date (where the round has one) | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Headline theorem has no complete proof anywhere | Soundness-fatal | Write the full proof into the submission (there is no page limit) before upload |
| Same result under review at another venue | Dual-submission violation | Withdraw one venue |

## Final-week order of operations

1. Confirm the **track**, the round (Track B), and the correct HotCRP server.
2. Register title/abstract/authors/conflicts before any registration cutoff the round has.
3. Freeze the first ten pages after the title page; make sure every theorem they state is fully
   proved later in the submission.
4. Run the anonymity + format + AI-disclosure sweep on the *final* PDF, not a draft.
5. Flag **student-only authorship** in HotCRP if eligible for the best student paper award.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Both tracks' exact AoE dates, the Track B round structure (new in ICALP 2027), and whether the
  ICALP 2027 Track A call (not yet posted on 2026-11-24) matches the Track B rules.
- The format (no page limit since ICALP 2026; ten-page first-read rule) and the LIPIcs-class
  recommendation.
- The anonymity wording, the no-simultaneous-submission wording, and the AI-disclosure rule — all
  cycle-volatile.

## Automated preflight (run this first)

Before working through this checklist by hand, run the repository's deterministic preflight
on the actual file (`.tex`, `.md`, `.docx` or `.pdf`):

```bash
python3 tools/preflight.py paper.pdf --venue icalp-skills   # from a clone of the AJS repository
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
[ICALP submission status] ready / blocked / needs work
[Track] A (algorithms/complexity/games) / B (automata/logic/semantics; round 1 or 2) — correct server? yes/no
[Registration] title/abstract/authors/conflicts locked by any earlier deadline? yes/no
[Format] title page + abstract; merits clear within the first ten pages; single column ~11pt; LIPIcs class y/n
[AI disclosure] AI used in the research? -> disclosed with specific uses? yes/no/n.a.
[Anonymity] clean / leaks: <where>
[Proofs] every headline theorem fully proved in the submission? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
