---
name: rss-topic-selection
description: Use when judging whether a robotics project fits RSS (Robotics: Science and Systems), the single-track selective venue whose bar is a scientific claim about robotics, and when routing instead toward ICRA, IROS, CoRL, HRI, WAFR, T-RO, or IJRR based on claim type, evidence shape, and audience.
---

# RSS Topic Selection

Decide whether the project belongs at RSS before any writing starts. RSS is the
deliberately small, single-track robotics conference run under the RSS Foundation:
every accepted paper is presented to the entire audience, so the program committee
selects for work the whole field should hear about. That structure creates the venue's
distinctive question, and this skill applies it.

## The one question RSS asks

**What does this paper claim about robotics — as science — that was not known before?**

- A property proved about a class of planners; a measured bottleneck the community
  misattributed; a representation whose suitability for robot data is argued and then
  tested; a capability shown to transfer for a stated reason — all RSS-shaped.
- "We integrated known components and the system works well" is a legitimate result,
  but it is a *systems demonstration*, and at RSS it must still carry an insight: what
  does the integration reveal that component papers could not?
- The 2026 CFP welcomes both Science and Systems contributions; the shared requirement
  is a contribution statement a skeptic could test, not a capabilities inventory.

## Routing table (from RSS's seat)

| If the project is... | Verdict | Rationale |
|---|---|---|
| One sharp idea + evidence sized to it | RSS core | Single-track audience rewards concentrated novelty |
| A broad integrated platform, many components, no isolable insight | ICRA / IROS | Higher-volume multi-track programs absorb breadth |
| Learning-centric, benchmark-driven, embodiment secondary | CoRL | Robot-learning community is the right jury |
| Human-subject study as the main evidence | HRI | Study-design reviewing lives there |
| Pure algorithmic-foundations result, no experiment planned | WAFR or a theory venue | RSS still expects an empirical anchor |
| Needs 15+ pages of proofs or longitudinal experiments | T-RO / IJRR | Journal length; RSS caps at 8 pages excl. references (2026) |

## Three-part fit probe

Run these in order; failing any one is a re-route signal, not a death sentence:

1. **Claim probe** — write the contribution as a single declarative sentence with no
   system name in it. If the sentence is empty without the system name, the insight is
   not yet separable from the artifact.
2. **Audience probe** — RSS attendees span planning, perception, learning, control,
   and design. Would a session chair from a *different* subfield still care? If the
   result matters only inside one benchmark community, CoRL or a workshop is kinder.
3. **Compression probe** — the 2026 format is 8 pages excluding references, a ceiling
   the CFP explicitly frames as not a target. If the argument cannot be made crisply,
   the project may be a journal paper wearing conference formatting.

## Worked micro-decision

A team has a legged robot climbing unstructured rubble using a new terrain-contact
estimator plus an off-the-shelf controller. As a platform story it routes to ICRA. But
if they can show the estimator's confidence signal *predicts* failures two footsteps
ahead — and that this predictive structure, not raw accuracy, is what enables recovery
— they now own a falsifiable claim about proprioceptive sensing, and RSS becomes the
natural home. Same hardware, different paper.

## Claim taxonomy: what an RSS-shaped assertion looks like

Concrete templates a project can aim to instantiate — each is falsifiable and
system-name-free:

- **Property claim** — "planners of class C converge to suboptimal solutions;
  variant C' restores optimality." (The theorem-first lane.)
- **Bottleneck claim** — "in task family T, failures are dominated by factor F,
  not the factor the literature optimizes."
- **Representation claim** — "encoding the problem as R suits robot data because
  of property P, and evidence across tasks/platforms bears P out."
- **Transfer claim** — "capability K generalizes across E for stated reason R,
  and breaking R breaks the transfer."
- **Measurement claim** — "the community's standard metric M mis-ranks methods
  under condition X; here is the corrected instrument."

If none of these templates fits even loosely, the project is probably a systems
report or an application study — respectable, but routed elsewhere.

## Signals to weigh before committing the January slot

| Signal | Reading |
|---|---|
| The team can state the claim without naming the robot | Strong RSS signal |
| The most exciting artifact is a video, not a finding | Demo gravity — reframe or reroute |
| Reviewers from planning AND learning would both engage | Whole-audience fit confirmed |
| Evidence exists only in simulation, claim mentions the world | Close the gap or scope the claim |
| The natural length is 14 pages | Journal-shaped; consider T-RO/IJRR |
| The idea would still matter if the success rate were 20% lower | Insight-driven, not benchmark-driven |

## Cycle discipline

- Scope emphasis and paper-type wording shift per edition; reread the current CFP
  (roboticsconference.org/information/cfp/) before the final call.
- Deadline geometry matters for routing: RSS 2026 closed in late January for a July
  conference; ICRA and CoRL sit elsewhere in the year — see `rss-workflow` for the
  full calendar argument.
- The Science/Systems paper-type wording was specific to the 2026 CFP; confirm the
  current cycle's categories before framing the contribution statement around them.

## When RSS is the wrong home for excellent work

Fit failure is not quality failure. Recognize these honorable mismatches early:

- A superbly engineered platform whose lessons are in the integration details —
  the field needs it published, at ICRA/IROS length and breadth.
- A benchmark or dataset whose value is adoption, not insight — a track designed
  for artifacts (or a journal) serves it better than a single-track talk slot.
- A result whose proof apparatus dwarfs its empirical story — WAFR or a journal
  gives the proofs room the 8-page ceiling cannot.
- Work whose audience is one application community (agriculture, surgery,
  logistics) — the domain venue's reviewers can evaluate what RSS's generalists
  cannot.

## Output format

```text
[RSS verdict] core fit / fixable framing / re-route
[Scientific claim] <one sentence, no system name>
[Whole-audience hook] <why a distant subfield cares>
[Evidence-to-claim gap] <what is missing>
[If re-route] ICRA / IROS / CoRL / HRI / WAFR / T-RO / IJRR + one-line reason
```
