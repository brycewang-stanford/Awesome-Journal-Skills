> **Illustrative teaching example.** The study, community, platform, and every number
> below are **fictional**, invented only to demonstrate how a CSCW abstract and
> introduction should be built. No real-world findings are stated and no venue policy
> is invented. Corresponding skills:
> [`cscw-writing-style`](../../skills/cscw-writing-style/SKILL.md),
> [`cscw-experiments`](../../skills/cscw-experiments/SKILL.md), and
> [`cscw-topic-selection`](../../skills/cscw-topic-selection/SKILL.md).

# Worked Example: A CSCW-Style Abstract + Introduction (before → after)

The rewrite below demonstrates the moves CSCW reviewers look for: the **group or
community as the unit of analysis**, an empirical setting described concretely, a
**concept the field can reuse**, methods and ethics visible on the first page, and
claims calibrated to what interviews plus trace data can actually support. It also
demonstrates the routing logic from `cscw-topic-selection`: this paper is about how
*collaborative moderation work is organized*, not about a novel interface — which is
why it belongs at CSCW rather than a UI venue.

**Fictional paper:** *"Holding the Queue: How Volunteer Moderation Teams Distribute
Emotional Labor in Crisis-Support Communities."* Fictional study: interviews with
moderators of peer-support communities, combined with twelve months of moderation-log
traces.

---

## Before (a system-and-users draft that buries the CSCW contribution)

> **Abstract.** Online communities are increasingly important. Moderation is a
> challenging task, and moderators often experience burnout. We interviewed
> moderators and analyzed log data from several communities. We find that moderation
> is difficult and emotionally demanding, and we propose design implications for
> better moderation tools that could reduce burnout and improve efficiency.
>
> **Introduction.** Content moderation has received much attention in recent years.
> Prior work has studied moderation on Reddit, Twitch, and Facebook. However, less is
> known about moderation in support communities. We conducted a study to fill this
> gap. Our contributions are: (1) an interview study; (2) a log analysis; (3) design
> implications. The rest of this paper is organized as follows...

**Why this fails the CSCW read:**

- **The group is missing.** Everything is phrased at the individual-moderator level
  (burnout, workload); nothing describes how the *team* divides, hands off, or
  coordinates the work — the venue's core question.
- **"Fill the gap" positioning.** The gap is defined by absence ("less is known"),
  not by a stake: what breaks, for whom, if we keep misunderstanding this work?
- **No reusable concept.** "Moderation is difficult" gives the field nothing to
  think with next time.
- **Methods and ethics invisible.** "Several communities," no participant counts, no
  consent posture, no statement of how sensitive crisis-support content was handled
  — a reviewer's first ethical question left open.
- **Contributions-as-deliverables.** Listing "an interview study" as a contribution
  confuses the activity with the finding.
- **Tool framing.** "Better tools for efficiency" pitches an intervention paper the
  study cannot support, and drifts toward a different venue's evidence bar.

---

## After (the group-level rewrite)

> **Abstract.** Volunteer moderators of online crisis-support communities absorb the
> emotional weight of other people's worst moments — yet how *teams* organize that
> absorption is poorly understood, and tools built for individual efficiency may cut
> against the collective practices that keep moderators whole. Drawing on interviews
> with 24 moderators across six peer-support communities and twelve months of
> moderation-log traces from three of them, we identify **queue-holding**: a set of
> team practices — rotating who faces the rawest reports, informal debriefs after
> hard cases, and deliberately slow hand-offs — through which teams convert
> individual emotional labor into a shared, schedulable resource. Trace data show
> the rotation rhythm in action; interviews show why teams defend it even at the
> cost of response speed. We discuss how moderation tooling that optimizes
> throughput can erode queue-holding, and what designing *for* it would require.
> All participants consented to research use; quoted material is paraphrased and
> community identifiers are removed by agreement with the communities.
>
> **Introduction.** *(¶1 — the collaborative work, concretely.)* When a report
> arrives in a crisis-support community at 3 a.m., someone must decide, quickly,
> whether a stranger is in danger. That someone is a volunteer — but they are not
> alone. Behind each decision sits a team that decides who takes the night shift,
> who is "too close" to a case, and who needs a week away from the queue. This
> paper is about that team-level machinery.
>
> *(¶2 — the stake, not the gap.)* Research and platform tooling largely treat
> moderation as an individual classification task to be accelerated. If moderation
> in these settings is instead a *collectively managed emotional practice*, then
> throughput-oriented tools do not merely miss the point — they may dismantle the
> practices teams use to protect their members. Understanding those practices is a
> precondition for building tools that help.
>
> *(¶3 — setting, methods, ethics, in one honest breath.)* We interviewed 24
> moderators across six crisis-support communities and analyzed twelve months of
> moderation logs from the three communities that granted trace access. Communities
> and participants consented to research use; given the sensitivity of the setting,
> we paraphrase rather than quote verbatim and withhold community names under a
> data-use agreement. Our analysis is interpretive, with the trace data used to
> ground and bound — not to statistically confirm — the interview findings.
>
> *(¶4 — the concept and the claims, calibrated.)* We contribute the concept of
> **queue-holding** to name how teams schedule, rotate, and decompress emotional
> labor, and we show its signature in the traces: rotation rhythms and hand-off
> pauses that a throughput lens would read as inefficiency. We do not claim these
> practices are universal or optimal; we claim they are load-bearing in the teams
> we studied, and that design which ignores them carries a describable risk.
>
> *(¶5 — why CSCW.)* The contribution is an account of cooperative work — how a
> team turns individual exposure into shared capacity — with consequences for the
> design of collaborative systems. It extends CSCW's long conversation about
> articulation work and awareness into settings where what must be coordinated is
> emotional load itself.

---

## What changed, mapped to the skills

| Before-symptom | After-fix | Skill |
| --- | --- | --- |
| Individual burnout framing | Team-level machinery (rotation, hand-offs, debriefs) | `cscw-topic-selection` |
| "Less is known" gap | A stake: efficiency tools may dismantle protective practices | `cscw-writing-style` |
| No reusable idea | Named concept: queue-holding | `cscw-writing-style` |
| Invisible methods/ethics | Counts, consent, paraphrasing policy on page one | `cscw-experiments` |
| Overclaimed generality | "Load-bearing in the teams we studied," limits stated | `cscw-experiments` |
| Trace data as decoration | Traces ground and bound the interpretive claims | `cscw-experiments` |

> Next: study the real canon in [`../exemplars/library.md`](../exemplars/library.md)
> — especially the Dimond et al. entry for sensitive-community ethics and the
> Dourish & Bellotti entry for what a durable concept contribution looks like —
> then check current submission mechanics in
> [`../official-source-map.md`](../official-source-map.md).
