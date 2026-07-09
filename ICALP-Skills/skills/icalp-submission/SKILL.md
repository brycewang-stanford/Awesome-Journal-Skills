---
name: icalp-submission
description: Use when auditing an ICALP (EATCS) Track A or Track B submission for HotCRP readiness, covering the correct-track submission server, abstract registration before the full-paper deadline, the 15-page extended-abstract page budget with a clearly labelled appendix / full version, lightweight double-blind anonymity, the no-simultaneous-submission rule, and the single annual February AoE cutoff.
---

# ICALP Submission

Run this audit before uploading to the ICALP HotCRP site. ICALP — the EATCS International Colloquium
on Automata, Languages, and Programming — is a **pure theory venue** publishing open-access in
**LIPIcs**, with a **single annual deadline** and **two tracks** on **separate HotCRP servers**. The
paper is judged on its **theorems and proofs**, so this audit is about format, anonymity, and the
body/appendix split, not about a runnable artifact. Every number below was read from the ICALP 2026
(53rd, Royal Holloway) call on 2026-07-09 via search renderings of the CFP (see
`resources/official-source-map.md`); treat them as a one-cycle snapshot and reopen the live call.

## Pick the right track first

ICALP has two tracks on **two different HotCRP sites** — submitting to the wrong one is a real,
avoidable failure:

- **Track A — Algorithms, Complexity and Games** → `icalp2026-a.hotcrp.com`.
- **Track B — Automata, Logic, Semantics and Theory of Programming** → `icalp2026-b.hotcrp.com`.

If you are unsure, resolve it with `icalp-topic-selection` before touching HotCRP; the tracks have
different program committees, and Track B carries a rebuttal while Track A does not.

## The two-step deadline

ICALP separates **abstract registration** from **full submission**, both AoE:

- **Abstract registration** (ICALP 2026: **3 February 2026**) locks title, abstract, authors, and
  conflicts a few days early. Miss it and the system will not take the PDF later.
- **Full submission** (ICALP 2026: **6 February 2026**, AoE) uploads the anonymized PDF.

Register with the *real* title and abstract — the abstract drives PC bidding, and a placeholder
quietly worsens your reviewer match.

## Format and page budget

- **Extended abstract of at most 15 pages**, **excluding** the bibliography and a **clearly labelled
  appendix**. The appendix may hold omitted proofs or a **full version**, read at the PC's discretion.
- **LIPIcs `lipics-v2021` document class** is an option but not required *at submission* in recent
  cycles (confirm per cycle); the **camera-ready must be LIPIcs** — so many authors write in LIPIcs
  from the start.
- The 15-page limit is on the **main body**; do not pad the body to 15 and dump every proof into an
  unread appendix (see `icalp-supplementary`). Reviewers judge on the body.

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
Posting a **full version on arXiv/ECCC/HAL is allowed and normal** — that is not "publication."

## Desk-risk triage

| Finding at audit time | Severity | Real fix |
|---|---|---|
| Body over 15 pages (excluding refs + appendix) | Format-reject-grade | Compress the body; move detail to the appendix, not into the body count |
| Submitted to the wrong track | Mis-review / reject | Withdraw and resubmit to the correct HotCRP server before the deadline |
| Author identity leaks (metadata, acks, first-person self-cite) | Anonymity violation | Scrub metadata, remove acks, rewrite self-citations in third person |
| Abstract not registered by the earlier date | No submission slot exists | Nothing fixes this post-AoE — calendar it now |
| Headline theorem has no complete proof anywhere | Soundness-fatal | Write the full proof into the appendix / full version before upload |
| Same result under review at another venue | Dual-submission violation | Withdraw one venue |

## Final-week order of operations

1. Confirm the **track** and the correct HotCRP server.
2. Register title/abstract/authors/conflicts before the earlier registration cutoff.
3. Freeze the 15-page body; make sure every theorem it states is fully proved in the appendix / full
   version.
4. Run the anonymity + page-budget sweep on the *final* PDF, not a draft.
5. Flag **student-only authorship** in HotCRP if eligible for the best student paper award.
6. Re-download the uploaded PDF and read it cold to confirm it is the file you meant.

## Reverify each cycle

- Both tracks' exact AoE dates and whether they share one deadline.
- The page budget and whether the LIPIcs class is mandatory at submission this cycle.
- The anonymity wording, the no-simultaneous-submission wording, and any AI-disclosure rule — all
  cycle-volatile.

## Output format

```text
[ICALP submission status] ready / blocked / needs work
[Track] A (algorithms/complexity/games) / B (automata/logic/semantics) — correct server? yes/no
[Registration] title/abstract/authors/conflicts locked by the earlier deadline? yes/no
[Format] body pages (<=15 excl. refs + appendix), LIPIcs class y/n
[Anonymity] clean / leaks: <where>
[Proofs] every headline theorem fully proved in appendix / full version? yes/no
[Fix queue] <ordered, with owners and dates before the AoE cutoff>
```
