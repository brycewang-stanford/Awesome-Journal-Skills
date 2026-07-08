---
name: uist-topic-selection
description: Use when deciding whether a project belongs at UIST — testing it against the interface-systems contribution bar (novel technique, toolkit, or hardware that works), making the CHI-vs-UIST routing call explicitly, and re-routing to CSCW, IMWUT, TEI, ISMAR, IUI, or TOCHI when the artifact is not the contribution.
---

# UIST Topic Selection

UIST publishes papers whose contribution **is an interface artifact**: a new
interaction technique, an enabling piece of hardware, a toolkit or authoring system,
or an algorithm that makes a previously impossible interaction possible. The venue
grew out of demo culture and still reviews like it — the implicit first question is
"what did you build, and can I imagine holding it?" Use this skill before any UIST
plan is made; the March deadline punishes late routing discoveries.

## The artifact-subtraction test

Delete the system from the paper and see what survives:

- If what survives is a **finding about people** (how users behave, adopt, trust,
  collaborate), the system was an instrument, not a contribution — that is a CHI or
  CSCW paper.
- If what survives is **nothing**, because every claim is about what the artifact
  enables and how it is engineered, you are holding a UIST candidate.
- If what survives is a **model or algorithm evaluated offline** with no interactive
  loop, consider IUI, an ML venue, or a domain venue instead.

## CHI vs UIST: make the call, don't drift into it

Both are SIGCHI venues, both use PCS, and many projects could be dressed for either.
Decide on contribution shape, not on which deadline is closer:

| Question | Points to UIST | Points to CHI |
|---|---|---|
| What is novel? | The technique, device, toolkit, or enabling pipeline | The empirical insight, theory, or design knowledge |
| What is the evidence spine? | It runs: technical evaluation, demo, video figure | Study rigor: participants, methods, analysis |
| Who must be convinced? | Systems builders who will reuse or extend the artifact | A mixed jury weighing study quality and framing |
| Weakest section right now? | A thin user study is survivable if the engineering is deep | A thin study is usually fatal |
| Natural conference moment? | A demo people queue for | A talk people argue about |

An honest tie-breaker: if your video figure would be boring — nothing moves, nothing
is manipulated, nothing responds — UIST reviewers will feel the same way about the
system.

## Fit ledger

Score each row 0-2 and be suspicious of any total under 8:

```text
[ ] Enabling novelty: the artifact does something no published system does (not "does it better on a benchmark")
[ ] Technical depth: there is a mechanism, algorithm, or fabrication method worth two pages of implementation
[ ] Demonstrability: the contribution is visible in under three minutes of video
[ ] Evaluation match: the planned evidence measures what the artifact claims (see uist-experiments)
[ ] Community reuse: a builder could take the technique/toolkit and make something you didn't anticipate
[ ] Timing: buildable and evaluable before the late-March abstract/paper deadlines
```

## Where UIST-adjacent work actually belongs

- **Deployment and appropriation studies** of an interactive system → CSCW or CHI;
  UIST wants the system's construction, not its month-three usage patterns.
- **Sensing without an interactive application** (activity recognition, physiological
  pipelines) → IMWUT/UbiComp.
- **Tangibles and fabrication where the argument is design-theoretic** → TEI or DIS;
  keep fabrication at UIST when the contribution is the enabling process or machine.
- **AR/VR perception or display optics without an interface contribution** → ISMAR or
  IEEE VR.
- **Intelligent interfaces where the model is the contribution** and the interface is
  a wrapper → IUI, or an ML venue with a demo track.
- **Mature systems with longitudinal evaluation** that outgrew a 10-page conference
  paper → TOCHI.

The Lasting Impact lineage is a useful calibration set: mobile sensing hardware
(Hinckley et al., UIST 2000), multi-user touch hardware (DiamondTouch, UIST 2001),
gesture text entry (SHARK2, UIST 2004) — every one is an artifact a reader can
picture operating. Benchmark your idea against that lineage in
[`../../resources/exemplars/library.md`](../../resources/exemplars/library.md).

## Three routing vignettes

Concrete cases, because the boundary is learned by example:

1. **"We built a VR classroom and studied 40 students learning in it."** Subtract
   the artifact: a finding about learning in VR survives. Unless the classroom
   required new rendering, tracking, or authoring machinery worth two implementation
   pages, this is CHI (Learning subcommunity) or a learning-technology venue. The
   UIST version of this project would contribute the authoring system that let a
   teacher build such classrooms without programmers.
2. **"We invented a way to print stretchable circuits on fabric with a consumer
   printer, and made four demo garments."** Nothing survives subtraction — the
   process is the paper. The four garments are the evaluation breadth, and the
   technical characterization (resistance under strain, wash cycles) is the
   evidence. Textbook UIST; TEI only if the argument shifts to design theory.
3. **"Our LLM agent completes GUI tasks from natural-language instructions; we
   benchmarked it on 500 tasks."** The judgment call of the current era. If the
   contribution is benchmark accuracy, it drifts toward an ML/agents venue. It
   becomes UIST-shaped when the paper contributes the *interactive* machinery:
   mixed-initiative repair when the agent stalls, user-visible plans, an
   architecture others can build interfaces on — and evaluates those interactions,
   not just task completion.

## Timing the decision

Routing is cheapest at conception and expensive after a rejection. Three checkpoints:

- **At project pitch**: run the subtraction test on the *planned* paper, not the
  planned system — labs routinely build UIST systems and then write CHI papers
  about them by accident.
- **At feature freeze** (see `uist-workflow`): re-run the fit ledger; if technical
  depth scored 0-1, the short-paper category or an adjunct track is the honest
  landing zone.
- **After reviews**: rejections phrased as "the evaluation doesn't support the
  claims" are often routing errors in disguise — reviewers asked for the evidence
  the *other* venue's version of the paper would have carried.

## Scope notes for the 2026 cycle

- The 2026 CFP was verified via search renderings on 2026-07-08 (direct fetches were
  blocked); the Papers deadline (March 31, 2026) has passed, so a routing decision
  made today targets the adjunct tracks of UIST 2026 — Demos and Posters welcome work
  already shown elsewhere — or the UIST 2027 Papers cycle.
- Short papers (5 pages) exist for smaller-but-complete contributions; routing a
  half-built system to a short paper is legitimate, padding it to 10 pages is not.
- Scope vocabulary drifts with the field (2026 chairs span video accessibility,
  human-AI systems, fabrication, and programming tools — a hint about breadth);
  reread the current topics list rather than assuming last decade's hardware focus.

## Output format

```text
[UIST fit] strong / plausible / re-route
[Artifact-subtraction result] <what survives without the system>
[CHI-vs-UIST call] UIST / CHI / genuinely either — with the deciding row
[Fit ledger] <score>/12 with weakest two rows
[Re-route candidate] <venue + why its reviewers are the right jury>
[Next skill] uist-experiments (evidence plan) or uist-workflow (calendar)
```
