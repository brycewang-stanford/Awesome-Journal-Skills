---
name: icra-related-work
description: Use when building or auditing the related-work section of an ICRA paper — covering the conference's own recent proceedings plus IROS, RSS, CoRL, RA-L, and T-RO lanes, handling arXiv-only robotics work, citing your own platform papers under ICRA's double-anonymous rules, and positioning against commercial systems.
---

# ICRA Related Work

Related work at ICRA is a positioning argument compressed into roughly half a
page: which line of robotics research the paper extends, which competing
approaches exist, and what precisely is new. Reviewers are drawn from the same
community that wrote the competing papers — coverage gaps are noticed personally.

## The five lanes an ICRA reviewer checks

| Lane | What to cover | Where it lives |
|---|---|---|
| ICRA/IROS proceedings, last 3 years | direct competitors on the same task | IEEE Xplore |
| RSS + CoRL | algorithmic and learning-forward rivals | RSS proceedings site, PMLR |
| RA-L | fast-moving journal siblings — often the *same groups'* newer results | IEEE Xplore |
| Archival journals (T-RO, IJRR, AURO) | the mature line the task descends from | publisher sites |
| Recent arXiv robotics | concurrent work reviewers will have seen tweeted | arXiv cs.RO |

A robotics-specific trap: many results appear twice — an RA-L paper presented at
an ICRA — and are cited inconsistently. Cite the archival journal version
(RA-L/T-RO) when one exists; do not cite the same work twice under both labels.

## Concurrent and arXiv-only work

Robotics moves partly on arXiv now. Practical policy for a September submission:

- Anything on arXiv more than ~2-3 months before the deadline: reviewers may
  treat it as known art; cite it and differentiate technically.
- Preprints appearing within weeks of the deadline: cite as concurrent
  ("developed independently; appeared after our system was built") — reviewers
  reward the honesty and it defuses the "you missed X" review line.
- Never build the novelty claim *solely* against published venues while ignoring
  a widely-known preprint that solves the same task; the review will quote it.

## Self-citation under double-anonymous review

Since the 2026 cycle ICRA reviews are double-anonymous, which changes the
robotics habit of writing "in our prior work [7] we developed this platform":

- Third person, always: "the platform introduced in [7]" — even when [7] is the
  team's own hardware paper and everyone in the subfield knows it.
- Do not cite an unpublished internal report or "anonymous technical report"
  for load-bearing details; if the detail matters, it must be in the paper.
- Platform lineage may still be described factually (sensor suite, DOF, payload)
  without possessives; anonymity is about grammar and links, not omitting specs.
- Verify the anonymity policy each cycle — it is one year old and could be tuned.

## Positioning against commercial and closed systems

Unique to robotics venues: the strongest competitor may be a product (a
commercial gripper, a proprietary planner) with no paper. Handle it explicitly:

- Cite the product documentation or whitepaper with an access date if the
  comparison is quantitative.
- Say what cannot be known ("the vendor controller is closed; we compare
  end-task metrics only") rather than guessing internals.
- Never let "beats a 2019 open-source baseline" stand in for "beats what
  practitioners actually deploy" without acknowledging the gap.

## Building the positioning paragraph

The half-page should end in one paragraph that does the actual work. Template
logic (not template prose):

```text
Prior approaches to <task> fall into <k> families:
  <family A> [refs] achieves <strength-A> but <named failure mode>,
  <family B> [refs] handles <strength-B> yet requires <cost/assumption>.
Closest to this paper, <specific system> [ref] <what it does>;
it differs in <mechanism-level difference, not adjectives>.
This paper is, to the authors' knowledge, the first to <precise claim
narrow enough to be checkable against the five lanes above>.
```

The final claim must be narrow. "First learning-based grasping system" is
falsifiable in seconds; "first to close the loop on slip detection using only
joint-torque sensing on a collaborative arm" is a defensible novelty statement.

## Mechanics: IEEE numeric citations under a 2-page cap

The 2026 geometry gave references their own 2-page allowance at submission but
folded them into the 8-page total at camera-ready — so bibliography discipline
pays twice:

- IEEE numeric style, abbreviated venue strings ("Proc. IEEE Int. Conf. Robot.
  Autom. (ICRA)"), no URLs except for artifacts and standards.
- Cite the DOI-bearing archival version; arXiv IDs only for genuinely
  arXiv-only work.
- Deduplicate conference/journal twins now (one entry, the archival one) —
  it is the cheapest camera-ready page recovery available later.

## Common review complaints this section triggers

- **"Missing comparison to [reviewer's own paper]"** — mitigate by sweeping the
  last three ICRA/IROS proceedings for the task keywords, not just Google
  Scholar's top hits.
- **"Related work is a list, not an argument"** — every cited cluster needs a
  stated failure mode that the present paper fixes.
- **"Novelty over [X] unclear"** — the difference must be mechanism-level
  (different sensing modality, different guarantee, different assumption), not
  "better results."
- **"Cites 40 papers, engages 3"** — at ICRA's length, 20-30 well-chosen
  references engaged honestly beat exhaustive padding.

## Audit sequence

1. Keyword-sweep the last three years of ICRA and IROS proceedings for the task.
2. Check RA-L for newer journal versions of every conference paper cited.
3. Sweep arXiv cs.RO for the last six months; classify hits as prior vs concurrent.
4. Rewrite all self-references into third person; strip possessives and links.
5. Compress into family-structured paragraphs ending in the narrow first-to claim.
6. Ask: which single missing citation would most anger which likely reviewer?

## Output format

```text
[Lane coverage] ICRA/IROS <y/n> RSS/CoRL <y/n> RA-L <y/n> journals <y/n> arXiv <y/n>
[Concurrent work] <list + handling>
[Self-citation anonymity] clean / violations: <lines>
[Duplicate RA-L/ICRA citations] <found or none>
[First-to claim] "<exact sentence>" — falsifiability check: <pass/risk>
[Most dangerous omission] <paper + which reviewer it summons>
```
