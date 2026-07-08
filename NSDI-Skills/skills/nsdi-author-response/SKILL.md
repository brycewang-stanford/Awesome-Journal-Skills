---
name: nsdi-author-response
description: Use when answering NSDI reviewers through the channel the venue actually provides — executing a one-shot revision against the required-issues list, writing the change memo and highlighted diff for the same reviewers, and pre-empting objections inside the submission when no response phase exists.
---

# NSDI Author Response

At NSDI the author's voice reaches reviewers at two moments only: inside the original
submission, and — if granted — inside a one-shot revision packet read by the same
people who wrote the demands. There is no rendered rebuttal phase in the '27 CFP
(absence 待核实; verify each cycle). This skill covers both moments; the second is
the venue's signature mechanism and the reason this skill is not a rebuttal-writing
guide.

## Moment one: the response you embed in advance

Without a mid-review channel, anticipated objections must be answered in the PDF:

- Run the objection drill: each coauthor writes the three most likely reviewer
  complaints; any complaint appearing twice gets a paragraph in the paper —
  typically a "why not X?" design-alternatives note or a limits paragraph
  (`nsdi-writing-style`).
- Pre-empt the baseline attack by documenting baseline tuning in-body
  (`nsdi-experiments`).
- Pre-empt the scope attack with an explicit sentence locating the contribution in
  the networking stack or distributed design (`nsdi-topic-selection`).

## Moment two: the one-shot revision, treated as a contract

The decision letter's required-issues list is an offer with exact terms: fix these,
same reviewers check, one attempt. Respond like a contractor, not a debater.

**Triage the issues within days of notification:**

| Issue type | Typical cost | Response posture |
|---|---|---|
| New experiment / baseline | machine-weeks + testbed access | reserve infrastructure immediately (`nsdi-workflow`) |
| Analysis or clarity | days | do fully; these are free credibility |
| Claim recalibration | hours, plus ego | almost always concede — narrow the claim to the evidence |
| Genuinely infeasible demand | — | contact the program co-chairs early; silence then surprise is the worst path |

**Execution rules:**

1. **Address every listed issue, visibly.** Coverage is binary at NSDI: revisions
   that fail to address the required issues are rejected with no further revision
   option. Partial credit does not exist.
2. **Do not renovate beyond the list.** The same reviewers approved everything they
   did not flag; gratuitous rewrites reopen settled sections and can introduce new
   objections that the one-shot format gives you no chance to answer.
3. **If an experiment's result contradicts the reviewer's expectation, report it
   straight.** The issue said "evaluate under churn," not "show churn is fine." An
   honest unfavorable result plus a scoped claim is a fulfilled requirement; a
   massaged favorable one is a rejection when the reviewer probes.

## The packet: memo + highlighted diff

Both components are mandatory auxiliary material (`nsdi-supplementary`). Their shared
purpose: let a reviewer verify their own issue in under a minute.

```text
Change memo skeleton (one block per required issue, in the letter's order):

R-1  Compare against <deployed system>.
     DONE — §6.2 now includes tuned <system> (config: App. C).
     Result: our gains drop from 3.4x to 2.6x at p99.9; text and
     abstract recalibrated. [diff pages 8-9, 1]

R-2  Clarify lease-expiry semantics.
     DONE — new §4.3 (state machine, Fig. 5); two corner cases we
     had not specified are now explicit. [diff pages 5-6]

Also changed (minimal): fixed two typos flagged in reviews; updated
citation [31] to its published version. No other content changes.
```

The "Also changed" section builds the trust the format depends on — it certifies the
diff is complete. Generate the highlighted version mechanically (latexdiff or
equivalent) from the true submitted baseline, not from a reconstructed one.

**Tone:** the readers already invested in this paper — a one-shot revision means
they voted to see it again. Write as a colleague closing out a punch list:
no re-argument of the original decision, no flattery, no hedging about what was
and wasn't done.

## Timeline for a typical revision window

A spring '27 one-shot revision (notified July 23, 2026) targeting the fall gate
(September 17, 2026) has roughly eight weeks:

1. **Week 1:** issue ledger built; infeasibility flags raised with co-chairs if any;
   testbed time reserved.
2. **Weeks 2-5:** demanded experiments run with full provenance
   (`nsdi-reproducibility`); text changes drafted in parallel.
3. **Week 6:** memo and diff assembled from the running drafts; internal reviewer
   plays the original R2 against the packet.
4. **Week 7:** freeze; verify the resubmission enters the correct HotCRP site with
   the packet attached (`nsdi-submission`).
5. **Week 8:** buffer — the revision that arrives calm beats the one that arrives
   complete-but-chaotic at 11:58 pm.

A fall-issued revision aiming at the next edition's spring gate has more calendar
but the same structure; do not let the longer runway defer the testbed reservation.

## When the letter says plain reject

There is no response channel and no appeal-by-email; the ban clock runs
(`nsdi-review-process`). The productive move is extraction: convert each review
point into either a fix, a re-route signal, or a documented disagreement to handle
in the next version's pre-emption layer. The reviews were written by this
community; the next PC will resemble them.

## Output format

```text
[Channel] pre-emption (drafting) / one-shot revision (letter in hand)
[Issue ledger] R-# -> action -> cost -> owner -> status
[Feasibility] any issue needing co-chair contact? deadline realistic?
[Packet status] memo issue-complete? diff from true baseline? extras declared?
[Risk] unfavorable-result handling; renovation creep check
[Ship date] resubmission gate targeted, freeze date set
```
