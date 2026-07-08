---
name: eurosys-topic-selection
description: Use when deciding whether a systems project belongs at EuroSys — the ACM SIGOPS-Europe flagship spanning OS, distributed systems, storage, cloud, virtualization, security, and ML systems — or routes better to SOSP, OSDI, NSDI, ASPLOS, ATC, FAST, or SoCC, and how the April slot and dual deadlines affect that call.
---

# EuroSys Topic Selection

Use this before serious writing begins. EuroSys is the flagship conference of
the European Chapter of ACM SIGOPS (`eurosys.org`, rendered 2026-07-08),
running annually since 2006 and seeking papers on **all areas of computer
systems** — it is a broad-church systems venue, not a niche. The 2026 edition
(the 21st) met in Edinburgh in April; 2027 meets in Rabat. The right question
is rarely "is this systems?" but "is this *conference-grade* systems, and is
EuroSys the best-positioned jury and calendar slot for it?"

## The substance bar

A EuroSys-ready project typically has all four:

- **A built thing.** An implemented system or substantial modification, not a
  simulation of one (measurement and experience papers are the exception, and
  must be framed as such).
- **A transferable idea.** An abstraction, mechanism, or empirically
  established principle that outlives this codebase.
- **Evidence under realistic conditions.** Workloads and scale that resemble
  the deployment story being told.
- **An articulable insight.** One sentence a reviewer can carry into the PC
  meeting. Strong engineering without a nameable idea routes to ATC-style
  venues or an experience track.

## Routing from the EuroSys seat

| Center of gravity | Stay or route | Why |
|---|---|---|
| OS/kernel, runtimes, virtualization, distributed infra | EuroSys core | The venue's home ground since 2006 |
| ML systems (serving, training infra) | EuroSys core, growing | Recent best papers are LLM-serving systems (e.g., EuroSys '25) |
| Once-a-generation OS-principles result | Consider SOSP/OSDI too | Same-family flagships; route by cycle timing and audience |
| Network protocols, measurement of networks | NSDI / SIGCOMM | EuroSys reads it as out-of-center networking |
| Hardware/software interface, arch mechanisms | ASPLOS | Architecture jury evaluates architecture ideas |
| Storage-stack internals | FAST first | Deepest storage jury; EuroSys viable for broader claims |
| Cloud-native ops, serverless economics | SoCC / Middleware also viable | Match the paper's altitude to the jury |
| Pragmatic engineering, tool papers | USENIX ATC | Idea-density bar differs there |

Two calendar facts sharpen the call: EuroSys's April conference and dual gates
(May and September submissions for 2027) interleave with the SOSP/OSDI and
NSDI cycles, so a systems result can almost always find a flagship gate within
a few months — pick by *fit and readiness*, never by whichever deadline is
nearest. And a EuroSys rejection blocks the same round for a year, which makes
premature submission genuinely expensive.

## Fit self-interrogation

```text
1. Insight test: state the idea in one sentence without naming your system.
2. Jury test: which three published papers would this one sit between?
   If ≥2 are EuroSys/SOSP/OSDI papers, EuroSys is plausible.
3. Evidence test: does the current evaluation reach the four-layer stack
   (end-to-end / decomposition / cost / boundary)? If not, is it reachable
   by the target gate?
4. Regime test: is the claim's deployment story credible to reviewers who
   run real infrastructure?
5. Calendar test: which gate (spring/fall) matches the project's maturity,
   accounting for the one-year ban if it fails?
```

## Contribution shapes EuroSys publishes

The exemplars library (`resources/exemplars/library.md`) documents these
shapes across two decades of the venue's own award line:

| Shape | Award-line instance | What it must bring |
|---|---|---|
| General abstraction + engine | Dryad (2007) | Proof the abstraction subsumes existing practice |
| Tool with a thesis | Coccinelle line (2008) | Validation on the real ecosystem it targets |
| Small mechanism, big evidence | Delay Scheduling (2010) | Production-shaped workloads carrying a simple idea |
| Design-space taxonomy | Omega (2013) | Vocabulary plus trace-driven comparison |
| Production retrospective | Borg (2015) | Transferable lessons including failures |
| ML-infrastructure mechanism | CacheBlend (2025) | A systems idea legible without ML expertise |

If the project matches none of these shapes, that is not disqualifying —
but it should prompt a harder look at what the contribution *type* is
before a EuroSys jury is chosen for it.

## Signals you are forcing it

- The contribution sentence contains "we combine" and three technique names
  but no invariant or tradeoff.
- The evaluation exists only at benchmark scale while the pitch is production
  scale.
- The nearest related work is entirely from another community's venues — the
  jury you are choosing has no vocabulary for the delta.
- The plan is "submit to fall EuroSys because SOSP just closed" — deadline
  proximity masquerading as venue fit.

## When EuroSys is the *strategically* right flagship

Beyond raw fit, three situations tilt toward EuroSys among the systems
flagships:

- The work speaks to infrastructure and communities strongly represented
  on European PCs (e.g., European cloud/telecom operators, EU data-locality
  constraints) and benefits from that jury's context.
- The project's maturity curve matches a EuroSys gate now, and waiting for
  another flagship's next cycle risks being scooped by a fast-moving line
  of work.
- The team wants the artifact culture: sysartifacts badges plus a named
  artifact award make EuroSys a strong home for systems whose artifact *is*
  part of the contribution.

## Output format

```text
[Verdict] EuroSys-ready / EuroSys-plausible after gaps / route elsewhere
[Insight sentence] <the transferable idea, system name omitted>
[Neighbor triangulation] <three papers this would sit between>
[Best-fit gate] spring / fall 2027+ with readiness rationale
[If routing away] <venue + the specific mismatch driving it>
```
