---
name: asplos-supplementary
description: Use when deciding what goes into an ASPLOS submission's appendices versus the 11 self-contained pages — applying the rule that reviewers are neither required nor encouraged to read supplemental material, using anonymized supplements for unciteable own work, and staging content for the revision and artifact phases.
---

# ASPLOS Supplementary Material

ASPLOS 2027 lets appendices and supplemental material ride in the submission file
with **no page limit** — under two conditions that define this entire skill: the
11-page body must be **self-contained**, and reviewers are **neither required nor
encouraged** to read anything past it (CFP, checked 2026-07-08). Supplementary
material is therefore not extra space; it is a different medium with a different
reader contract.

## The reader-contract test

For every block of content, ask: *what happens if no reviewer ever reads this?*

| If unread, the paper... | Verdict | Destination |
|---|---|---|
| ...loses a claim's only support | Body — the claim is otherwise unsupported | Compress into the 11 pages or cut the claim |
| ...still stands; the block deepens confidence | Legitimate appendix | Appendix, with a forward pointer from the body |
| ...still stands; the block enables re-implementation | Appendix or artifact | Appendix now; artifact package later |
| ...still stands; nobody would miss it | Cut | Nowhere |

The self-containment rule has teeth: the CFP frames appendices explicitly as not a
way to circumvent the page limit. A proof sketch, key config table, or summary
sensitivity plot that a claim *depends on* belongs inside the 11 pages, however
tight that makes them.

## What ASPLOS appendices are actually good for

- **Full configuration dumps** — simulator configs, kernel settings, tuning values
  whose *summary* appears in the evaluation section.
- **Extended result grids** — every workload × platform cell, where the body shows
  the representative subset and states the selection rule.
- **Interface specifications** — the full ISA-extension encoding or API surface the
  body describes functionally.
- **Proof details** for any formal claims, with theorem statements kept in-body.
- **Reproduction detail** that previews the Artifact Appendix (`asplos-artifact-evaluation`)
  without depending on it.

## The anonymized-supplement mechanism (ASPLOS-specific)

The 2027 double-blind rules include a mechanism siblings lack: when your own prior
or concurrent work cannot be cited in the third person without breaking anonymity —
a workshop paper being extended, a related manuscript under review elsewhere — it is
**uploaded and cited as anonymized supplemental material**. Checklist for using it:

1. Strip the supplement itself: author block, acknowledgments, PDF metadata,
   repository URLs, venue headers/footers.
2. Cite it in the body as anonymous supplemental material, not with a placeholder
   like "removed for review" (the placeholder wording is disallowed).
3. Include enough of the prior work that a reviewer can judge the delta — the point
   of the mechanism is to make "how much is new here?" answerable.

## Pointer discipline

Every appendix section earns a one-line, promise-shaped pointer in the body:

```text
Good: "Appendix B lists the full gem5 configuration; §6.1 states the
       parameters that materially affect the results."
Bad:  "Due to space constraints, details are in the appendix."
       (names no content, admits the body is incomplete)
Bad:  "See Appendix C for why this is safe."
       (a safety argument is claim-support; it must live in the body)
```

## Staging across the cycle

- **Submission:** appendices frozen with the body; they share the PDF and the
  deadline (September 9, 2026 for the live gate).
- **Response window:** you may point reviewers to specific appendix content that
  answers their question — this is the one moment unread appendices get read, and
  precise pointers (`asplos-author-response`) are what make it happen.
- **Major Revision:** appendix deltas count as part of the revision; log them in
  the change note like body changes.
- **Camera-ready/AE:** decide what migrates from appendix to the archived artifact,
  where it gains versioning and badges instead of page count.

## Appendix architecture

Unlimited length is not license for a junk drawer. Conventions that keep the
appendix navigable for the two audiences who might read it (a response-window
reviewer following your pointer, and a future artifact evaluator):

- One appendix per purpose, lettered and titled by content ("Appendix B: Full
  gem5 configurations"), never "Additional results."
- Order by likelihood of being pointed to during the response window: extended
  results and configurations first, proofs and encodings later.
- Each appendix opens with a two-line scope note: what it contains and which
  body section it backs — orphan appendices with no body pointer get cut.
- Keep appendix figures compilable from the same scripts as body figures; a
  supplement that contradicts the body (stale plot, different config) is worse
  than no supplement, because it is the kind of inconsistency that surfaces
  during revision re-review.

## What never belongs in any supplement

- Content that breaks anonymity (author-identifying configs, lab hostnames,
  grant boilerplate) — appendices are swept by the same double-blind rules as
  the body.
- The only statement of a limitation. Burying a known weakness in an appendix
  reads as concealment when a reviewer finds it — and one usually does.
- Results that contradict the body's claims without discussion; if the extended
  grid shows losing cases, the body's claim must already be scoped to survive
  them.
- Anything you are not prepared to defend in the response window — appendices
  are in the reviewed record even when unread by default.

## Interaction with the 11-page budget

The appendix is the pressure-relief valve that makes the figure-inclusive
11-page limit workable — but only content that passes the reader-contract test
may flow through it. When `asplos-writing-style`'s compression pass moves a
result grid out of the body, the body must retain the summary statistic and the
selection rule, so the claim remains supported by in-limit content alone. The
test after every move: re-read the body claim and ask whether a reviewer who
stops at page 11 still has grounds to believe it.

## Output format

```text
[Self-containment] claims supported only by appendix content: none / list
[Contract test] blocks re-classified body/appendix/artifact/cut: N moved
[Anonymized supplements] needed for: <own-work items> · stripped + cited correctly: Y/N
[Pointers] promise-shaped, content-naming: Y/N per appendix
[Staging] response-window pointer list drafted · artifact-migration list drafted
```
