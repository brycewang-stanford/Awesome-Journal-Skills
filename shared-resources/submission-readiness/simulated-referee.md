# Simulated Referee — a calibrated AE + referee panel before you submit

After the [`readiness-checklist`](readiness-checklist.md) clears the mechanical bar, this
runs the *substantive* gauntlet: a simulated **Associate Editor desk-screen** plus **2–3
distinct-lens referees calibrated to the venue**, adversarially verified and synthesized
into a referee report, a recommendation, and a prioritized, skill-mapped fix list. The
goal is to surface the decisive objection *before* a real referee does — the single
biggest lever on time-to-publication.

> **A rehearsal, not a verdict.** It predicts the attack surface and the likely decision
> band; it does not replace peer review and never asserts a paper "will" be accepted.

## Calibration (do this first — it is what makes the panel realistic)

Pull the venue's bar from the pack, not from generic intuition:

- **Acceptance/desk-reject reality + mechanics** — `resources/official-source-map.md`.
- **What this venue's referees actually attack** — pack `*-referee-strategy` + the shared
  [`reviewer-objection-checklist`](../empirical-methods/reviewer-objection-checklist.md).
- **The bar for fit / contribution / identification / robustness / exhibits** — the
  pack's corresponding skills.
- **Selectivity setting** — a ~5% top-3 venue desk-screens hard and expects general
  interest; a field journal weighs correctness and incremental contribution. Set the
  panel's strictness accordingly.

## Roles (give each a distinct lens — do not run identical referees)

| Role | Mandate |
|---|---|
| **Associate Editor (desk-screen)** | Fit & general interest, fatal-flaw scan, contribution vs. closest work; decides desk-reject vs. send-out, then synthesizes the reports |
| **Referee 1 — identification / method skeptic** | Attack the design: selection, exclusion, parallel trends, weak instruments, manipulation, structural assumptions. "Why is this causal?" |
| **Referee 2 — contribution / fit / literature** | Is the delta real and general-interest? Closest papers cited and correctly attributed? "So what, and what's new?" |
| **Referee 3 (optional) — robustness / inference / reproducibility** | Multiple testing, SE/clustering, subsample fragility, data-and-code feasibility. "Does it survive, and can I reproduce it?" |

## Protocol

1. **AE desk-screen.** Against the venue bar: in scope? general-interest enough? any
   fatal flaw? → **desk-reject risk** (low/med/high) with the deciding reason. If a clear
   desk reject, say so and stop before spending referee effort.
2. **Independent referee reports.** Each referee, in its lens, writes a structured report
   (template below) — independently, so concerns aren't anchored on each other.
3. **Adversarial verification.** Every *major* concern must pass three filters or be
   downgraded/dropped: **real** (not a misreading), **specific** (names the section/table
   and the mechanism), **addressable** (the author can act on it). This kills the
   plausible-but-unfair objections that waste revision cycles.
4. **AE synthesis.** Combine into one decision: **reject / major revision / minor
   revision / lean-accept**, naming the 1–3 *decisive* issues (the ones that actually move
   the decision), separated from the long tail of minors.
5. **Prioritized fix list, skill-mapped.** Each decisive issue → the exact pack skill (and
   its execution bridge) that fixes it, e.g. *"R1: TWFE under staggered adoption →
   `*-identification` execution bridge → run `callaway_santanna` + `bacon_decomposition`;
   move pre-trends to the appendix."*

## Referee report template (per referee)

```
【Lens】identification / contribution / robustness
【One-line summary of the paper as I read it】…
【Recommendation】reject / major / minor / accept
【Major concerns】(verified: real + specific + addressable)
   M1 — concern · where (§/table) · why it matters · what would fix it
   M2 — …
【Minor concerns】…
【What would move me to accept】…
```

## AE synthesis output

```
【Venue】… (calibrated from pack + source-map)
【Desk-screen】send out / desk reject — deciding reason; desk-reject risk: low/med/high
【Decision band】reject / major / minor / lean-accept
【Decisive issues (1–3)】each with the owning pack skill + concrete fix
【Secondary issues】…
【Author action plan】ordered: fix decisive issues first; tie each to a skill + tool
【Calibration caveats】where the simulation is uncertain (it is a rehearsal)
```

## Orchestration

- **Inline** (1 agent): play the AE then each referee in turn — fine for a quick read.
- **Multi-agent** (recommended for a real gauntlet): spawn one subagent per role with the
  *same manuscript* + the *calibrated venue bar*, collect the independent reports, then a
  final AE-synthesis agent. Distinct lenses + independence are what make it catch more
  than a single read. (Use the Agent tool per role; for a larger panel with verification
  rounds, a workflow that fans out referees → adversarially verifies each concern →
  synthesizes is the natural shape.)

## Anti-patterns

- **Identical referees.** Three clones of the same skeptic miss the contribution and
  reproducibility failure modes — diversify the lenses.
- **Unfiltered objections.** Passing through vague or unfair concerns wastes revision
  cycles; verify real + specific + addressable first.
- **Generic, venue-blind review.** A top-3 desk-screen and a field-journal review are
  different bars; calibrate from the pack or the report is noise.
- **Verdict theater.** Don't output a fake accept/reject probability; output the decision
  *band* and the decisive issues.

## Hard rules

1. **Calibrate from the pack + source-map**, never from generic memory.
2. **Verify before reporting** — real, specific, addressable.
3. **Map every decisive issue to a skill + (where empirical) its execution bridge**, so
   the author can act immediately.
4. **It's a rehearsal.** State that plainly; never claim acceptance.
