---
name: ieeesp-supplementary
description: Use when deciding what goes in an IEEE S&P (Oakland) paper's appendix versus the 13-page body, including the 5-page references-and-appendices allowance, the rule that reviewers need not read appendices, marking requirements past page 13, and what must never be relegated out of the reviewed body.
---

# IEEE S&P Supplementary Material

Use this when splitting content between the body and the appendix. S&P's
model is stricter than most: there is **no separate supplement upload** in
the verified CFPs — everything is one PDF of at most 13 body pages plus at
most 5 pages of references and appendices, 18 total, with all content past
page 13 clearly marked as appendix and **reviewers explicitly not required
to read appendices** (sp2027.ieee-security.org/cfpapers.html, checked
2026-07-08).

## The rule that decides every split

If the acceptance case needs it, it lives on pages 1–13. The appendix is
for material a *convinced* reviewer might verify, never for material that
does the convincing.

| Content | Placement | Why |
|---|---|---|
| Threat model, all of it | Body | The claim is undefined without it |
| Adaptive-attack evaluation summary | Body | The defense's acceptance case |
| End-to-end exploit walkthrough (one target) | Body | Existence proof of the attack |
| Per-target breakdown across 30 targets | Appendix | Verification depth, not persuasion |
| Full protocol/proof details | Appendix, with theorem statements in body | Statements are claims; derivations are checks |
| Ethics considerations | Body (submission); dedicated section added at camera-ready doesn't count against limits | Reviewed substance |
| Extended related work | Appendix | Positioning core stays in body (`ieeesp-related-work`) |
| Measurement instrument details (query lists, scan configs) | Appendix | Reproducibility depth |

## The 5-page arithmetic

References and appendices *share* the 5-page allowance. A security paper's
bibliography routinely runs 2.5–3 pages in compsoc format, leaving perhaps
two pages of real appendix. Consequences:

- Budget references first; the appendix gets the remainder.
- Long tables (per-CVE results, device lists) may need an artifact-repository
  home instead — but then nothing argumentative may depend on them.
- "Deferred to the extended version" is acceptable for proofs *only if* the
  paper states the theorem and its assumptions fully in the body; check the
  current CFP's stance on citing anonymous tech reports (待核实).

## Marking and mechanics

- Everything after page 13 must be **clearly labeled as appendix** — a
  running "Appendix" heading structure, not a continuation of numbered
  sections that silently crosses the boundary.
- Appendix references from the body should be load-bearing pointers
  ("full derivation in App. B"), and the body sentence must still stand if
  the pointer is never followed.
- The appendix is inside the anonymous PDF: the same anonymization sweep
  applies (`ieeesp-submission`), including figure paths and dataset names
  that identify a lab.

```text
Split audit — run over the section list:
for each body section:    would a first-round reviewer cut the paper
                          without this? if no → appendix candidate
for each appendix item:   does any *claim* in the body rely on it as
                          evidence? if yes → PROMOTE to body or weaken
                          the claim
page check:               body ≤ 13 · refs+appendix ≤ 5 · total ≤ 18
                          · post-13 content labeled
```

## Interplay with the Revise pathway

A Revise expectations summary often asks for material authors originally
appendixed ("bring the adaptive evaluation into the main text"). Cheapest
prevention: at first submission, put the *summary statistics* of every
appendix experiment in the body with a pointer down — reviewers who can see
the number rarely demand the relocation.

## Anti-patterns from this venue's review piles

- The 13th page ends mid-evaluation and the "results continue" in Appendix A
  — reads as a page-limit dodge and draws the over-length flag.
- Proof-by-appendix: a body theorem whose stated assumptions differ from the
  appendix proof's actual assumptions.
- An appendix ethics discussion — at S&P ethics is reviewed substance and
  the registration form asks for it directly.
- Appendix-only artifacts descriptions when the availability statement in
  the body promises more than the appendix delivers.

## Output format

```text
[Page arithmetic] body <n>/13 · refs <n> + appendix <n> ≤ 5 · total <n>/18
[Marking] post-p13 labeled ✓/✗
[Promotion list] <appendix items the acceptance case secretly depends on>
[Demotion list] <body items a first-round reviewer would not miss>
[Anonymity] appendix swept ✓/✗
```
