---
name: conext-related-work
description: Use when writing the related-work and positioning of an ACM CoNEXT paper — covering the networking literature lanes (SIGCOMM, NSDI, IMC, SIGMETRICS, MobiCom, CCR), delta-first positioning against the venue's own recent programs, and keeping self-citations double-anonymous.
---

# CoNEXT Related Work

Position the paper for a networking reviewer who knows the field's flagships cold. At CoNEXT, related
work is not a literature dump; it is the **delta argument** — what your contribution adds over the
closest prior systems and measurements — written so a double-anonymous reviewer can locate your
paper in the networking landscape in one read.

## Cover the lanes a networking reviewer expects

A CoNEXT reviewer will mentally check whether you engage the right bodies of work:

- **The flagship conferences:** SIGCOMM, NSDI, and CoNEXT itself for systems and architecture.
- **Measurement:** IMC (and PAM) for internet/system measurement methodology and findings.
- **Performance/modeling:** SIGMETRICS for analysis and evaluation methodology.
- **Wireless/mobile:** MobiCom, MobiSys, and related venues when relevant.
- **The journal and letters record:** IEEE/ACM ToN, CCR (SIGCOMM Computer Communication Review), and
  now **PACMNET** itself.

Missing the lane your paper lives in — e.g., a measurement paper that ignores IMC methodology, or a
data-plane paper that ignores the recent SIGCOMM/NSDI switch-hardware line — reads as unfamiliarity
and invites a change-list item in a one-shot revision.

## Delta-first positioning

Write each comparison as a **delta sentence**, not a summary:

```text
Prior work X [SIGCOMM'YY] measures/builds <what> but <the gap on the real target>;
we <the specific advance> and show it on <the real platform/trace>.
```

- Lead with the **closest** prior work, not the oldest or most famous.
- Make the delta concrete and testable: a new mechanism, a measured phenomenon prior work missed, a
  platform prior work did not evaluate on, a scale prior work did not reach.
- Avoid "to the best of our knowledge, we are the first" unless it is literally true and checkable;
  a measurement reviewer will know a counterexample.

## Keep self-citation anonymous

CoNEXT is double-anonymous, so your own prior work is a leak surface:

- Cite your prior papers in the **third person** ("Prior work [12] proposed..."), never "our
  previous system."
- Do not reveal a system lineage that identifies the group (e.g., "the successor to OurSys").
- If a comparison genuinely requires your non-anonymous artifact, use the anonymized location and
  describe it without owner-identifying detail.

## Positioning against CoNEXT's own recent programs

Because CoNEXT runs two cycles a year and publishes in PACMNET, the venue's own recent output moves
fast:

- Scan the **last two CoNEXT programs** and recent **PACMNET issues** for work in your subarea; a
  paper that ignores a directly relevant CoNEXT/PACMNET paper from last cycle looks careless.
- If your work extends a CoNEXT paper, state the delta precisely — reviewers may include that
  paper's authors.

## Structure and length

- Related work can be its own section or woven into the introduction and design sections; CoNEXT
  tolerates both, but the **delta must be visible early** regardless.
- Under the acmart budget, references are unlimited — so cite generously, but keep the *prose* tight;
  a wall of one-line summaries wastes body pages you need for evidence.

## Failure modes

| Failure | Why it hurts at CoNEXT | Fix |
|---|---|---|
| Literature list with no delta | Reviewer cannot place your contribution | Rewrite each entry as a delta sentence |
| Missing the closest prior system/measurement | Reads as unfamiliarity; revision risk | Lead with the nearest work and its gap |
| First-person self-citation | Breaks double-anonymity | Third-person, no lineage reveal |
| Ignoring the right lane (IMC/NSDI/SIGMETRICS) | Signals you are a visitor | Engage the venue where your method lives |
| Over-claiming "first" | A reviewer knows a counterexample | Scope the novelty to the checkable delta |

## Output format

```text
[Lanes covered] SIGCOMM / NSDI / IMC / SIGMETRICS / MobiCom / ToN-CCR-PACMNET as relevant
[Closest prior work] <papers + the specific gap each leaves on the real target>
[Delta sentences] <one per closest work>
[Anonymity] third-person self-citation; no system-lineage leak
[Recency] last two CoNEXT programs + recent PACMNET issues checked? yes/no
```
