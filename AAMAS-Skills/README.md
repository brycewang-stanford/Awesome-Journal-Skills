# AAMAS Skills

Twelve agent skills for papers targeting **AAMAS**, the International Conference on Autonomous
Agents and Multiagent Systems - the flagship venue of the International Foundation for
Autonomous Agents and Multiagent Systems (IFAAMAS). The pack focuses on the parts of an AAMAS
submission that reward *interaction* research: venue routing between AAMAS and the AI
conferences, OpenReview submission readiness, the 8-page-plus-references main track, the
double-blind rebuttal, IFAAMAS/open-access camera-ready, multiagent reproducibility, and the
distinctive AAMAS track menu (main, AAAI, JAAMAS, Blue Sky Ideas, Demo, Competitions).

Official basis checked on **2026-07-09**: AAMAS 2026 main-track Call for Papers, submission
instructions, and important-dates page; the AAMAS 2026 and AAMAS 2027 OpenReview conference
groups; the IFAAMAS foundation and proceedings; the JAAMAS journal; and the dblp `conf/atal`
proceedings index. See [`resources/official-source-map.md`](resources/official-source-map.md)
for the exact source map, including the access-method note for host pages that block automated
fetches.

## What makes AAMAS different

AAMAS is not a general AI or single-agent machine-learning venue. Its reviewers ask whether the
contribution is genuinely about **agents interacting**: game-theoretic reasoning, multiagent
reinforcement learning, mechanism design and auctions, negotiation and argumentation,
coordination and teamwork, agent-based simulation, and social choice. A paper where the result
only exists because *multiple* self-interested or cooperating agents are present is a fit; a
strong single-agent method with a multiagent label is the classic re-route. The skills encode
that routing (AAMAS vs AAAI / IJCAI / NeurIPS / ICML) as a first-class decision.

Three structural facts shape everything in this pack, all verified for the 2026 cycle:

- **Format.** Main-track papers are at most **8 pages plus any number of reference pages**, and
  may be submitted as **full papers** or **2-page extended abstracts**. Blue Sky papers are at
  most 4 pages including references.
- **Review.** AAMAS is **double-blind** and runs on **OpenReview** under the `ifaamas.org`
  namespace, with a **rebuttal** window on preliminary reviews. Accepted papers *and their
  reviews* become public on OpenReview, and papers are published **open-access by IFAAMAS**.
- **Tracks.** Beyond the main track, AAMAS runs an **AAAI Track** (fast-track from AAAI with a
  response to the AAAI reviews), a **JAAMAS Track** (oral slots for recently published JAAMAS
  journal articles), **Blue Sky Ideas**, **Demo**, and **Competitions** tracks - each with its
  own deadline and rules.

## Track map (AAMAS 2026, verify each cycle)

| Track | What it is for | Format signal | Verify |
| --- | --- | --- | --- |
| Main Technical Track | Original agents/multiagent research | 8 pp + refs (full) or 2 pp + refs (extended abstract) | CFP + submission instructions |
| AAAI Track | Redirecting strong AAAI submissions | Main-track format + ≤2 pp response to AAAI reviews, changes highlighted | AAAI Track CFP |
| JAAMAS Track | Presenting recent JAAMAS journal papers | 2-page extended abstract of the journal article | JAAMAS Track CFP |
| Blue Sky Ideas | Visionary, agenda-setting positions | ≤4 pp including references | Blue Sky CFP |
| Demo Track | Live/interactive agent systems | Short paper + demo | Demo CFP |
| Competitions Track | Benchmarks and agent contests | Competition proposal | Competitions CFP |

## Skills

- `aamas-topic-selection` - decide whether a project is AAMAS-shaped (agents are the research
  object) or better routed to AAAI, IJCAI, NeurIPS, ICML, EC, or a journal such as JAAMAS.
- `aamas-submission` - audit OpenReview readiness, the 8-page-plus-references limit, full vs
  extended-abstract choice, double-blind anonymity, supplement zip, track fit, and desk-reject
  triggers.
- `aamas-author-response` - draft a focused, anonymous rebuttal to preliminary reviews without
  new results, identity leaks, or a revised-paper upload the process does not allow.
- `aamas-camera-ready` - prepare the IFAAMAS open-access camera-ready, de-anonymization,
  proceedings metadata, registration, and in-person presentation.
- `aamas-artifact-evaluation` - package multiagent code, environments, opponent/population
  sets, seeds, and logs as anonymous supplementary evidence or a public post-acceptance release.
- `aamas-reproducibility` - strengthen the evidence map for interaction claims: proofs,
  opponent sets, seeds, self-play protocols, compute, and uncertainty on strategic outcomes.
- `aamas-supplementary` - organize proofs, extended game definitions, extra multiagent
  experiments, and the anonymized artifact zip within the size cap.
- `aamas-review-process` - reason about OpenReview review, the rebuttal, area-chair
  discussion, public reviews, and the mixed game-theory/MARL/systems reviewer pool.
- `aamas-writing-style` - revise for an interaction-first first page, named solution concepts,
  8-page compression, and double-blind wording.
- `aamas-related-work` - position against multiagent, game-theory, and RL literature across
  AAMAS, AAAI, IJCAI, NeurIPS, ICML, and EC, and handle concurrent and prior versions.
- `aamas-experiments` - audit self-play, population-based, and game-theoretic experiments,
  opponent choice, equilibrium/regret metrics, seeds, ablations, and claim-to-evidence fit.
- `aamas-workflow` - manage the calendar from venue fit through abstract, paper, supplement,
  rebuttal, decision, camera-ready, and presentation, with track-specific deadlines.

## Resources

- [`resources/official-source-map.md`](resources/official-source-map.md) - the verified fact
  anchor, with URLs, access dates, the 403 access-method note, and the 待核实 list.
- [`resources/external_tools.md`](resources/external_tools.md) - official IFAAMAS/AAMAS CFP,
  submission, OpenReview, JAAMAS, and proceedings links.
- [`resources/exemplars/library.md`](resources/exemplars/library.md) - five dblp-verified AAMAS
  papers across MARL, security games, negotiation, and multiagent learning, plus a
  sibling-venue omission list.
- [`resources/worked-examples/01-introduction.md`](resources/worked-examples/01-introduction.md)
  - a fictional before-to-after AAMAS abstract/introduction rewrite.
- [`resources/code/README.md`](resources/code/README.md) - adapter to the shared ML-conference
  reproducibility kit for multiagent experiments.

## How to use

1. **Route first.** Run `aamas-topic-selection` to confirm the interaction claim is real, then
   `aamas-writing-style` to get it onto the first page.
2. **Build the evidence.** Use `aamas-experiments` and `aamas-reproducibility` with the shared
   code kit to make self-play and game-theoretic results defensible.
3. **Submit clean.** Use `aamas-submission` and `aamas-supplementary` against the current CFP,
   then `aamas-review-process` and `aamas-author-response` for the rebuttal window.
4. **Finish.** Use `aamas-camera-ready` for the IFAAMAS open-access version, and
   `aamas-workflow` to keep every track deadline in view.

## Verified fact anchors (checked 2026-07-09)

These are historical anchors from the AAMAS 2026 cycle, not permanent rules. Each is sourced in
[`resources/official-source-map.md`](resources/official-source-map.md); re-verify before any
deadline-sensitive use.

- AAMAS 2026 was the **25th** edition, held **May 25-29, 2026** at the Coral Beach Hotel &
  Resort, **Paphos, Cyprus**, under IFAAMAS.
- Main-track timetable: abstract **October 1, 2025**, paper **October 8, 2025**, rebuttal
  **November 21-25, 2025**, camera-ready **February 11, 2026** (all AoE).
- Track deadlines differed: **AAAI Track November 17, 2025**; **JAAMAS Track January 6, 2026**.
- Main-track papers: **at most 8 pages plus unlimited references**; full paper or 2-page
  extended abstract; Blue Sky at most 4 pages including references.
- Review is **double-blind** on **OpenReview** (`ifaamas.org/AAMAS/2026/Conference`); reviews
  and decisions become public; papers are open-access via IFAAMAS.
- Supplementary material: a single zip, **not exceeding 25 MB**.
- The next cycle, **AAMAS 2027 (26th edition)**, already has an OpenReview group
  (`ifaamas.org/AAMAS/2027/Conference`); its host city, dates, and deadlines were not cleanly
  confirmable on 2026-07-09 (待核实).

## When AAMAS is the wrong home

The most common re-routes the `aamas-topic-selection` skill encodes:

- A strong **single-agent** method benchmarked in a multiagent environment → NeurIPS or ICML.
- Broad **AI reasoning, planning, or knowledge representation** with no interaction at its
  center → AAAI or IJCAI.
- **Market design, auction theory, or equilibrium computation** with economics as the point →
  EC (Economics and Computation).
- Work needing **journal-length archival treatment** → the JAAMAS journal (or its AAMAS
  presentation track).

Apply the frozen-agent test: if the result survives with the other agents replaced by a static
environment, the contribution is single-agent and belongs elsewhere.

## Maintenance notes

- Reopen current-cycle official sources before any deadline-sensitive advice; AAMAS rotates
  hosts every year and the host page may block automated fetches (cross-check IFAAMAS,
  OpenReview, ACM DL, and dblp).
- Treat AAMAS 2026 facts as historical anchors. As of 2026-07-09 the live target is **AAMAS
  2027** (26th edition); its OpenReview group exists but its host city, dates, deadlines, and
  track list were not cleanly confirmable - see the 待核实 list in the source map.
- Page limits, the extended-abstract option, rebuttal mechanics, supplement size caps, track
  deadlines, the proceedings template, registration, and presentation obligations can all
  change by cycle.
