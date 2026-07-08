# ISCA Exemplars Library (award-anchored contribution shapes)

> **Verified 2026-07-08.** Every paper below is a winner of the **ACM SIGARCH /
> IEEE-CS TCCA Influential ISCA Paper Award**, taken from the SIGARCH award page
> (https://www.sigarch.org/benefit/awards/acm-sigarchieee-cs-tcca-influential-isca-paper-award/,
> read via search rendering — the gateway blocked direct fetches; see the
> access-method note in [`../official-source-map.md`](../official-source-map.md)).
> The award is presented annually at ISCA to a paper from a past ISCA judged to
> have had the greatest impact in the intervening years — which makes the winner
> list the venue's own longitudinal statement of what an ISCA paper should be.
>
> **Zero-hallucination rule:** rows state title, authors, original edition, and
> award year as recorded on the award page, plus *shape analysis only*. No result
> numbers, no mechanism details beyond what titles state, no quotes. Read the
> papers (via dblp → publisher) before citing content from them.
>
> **Attribution guard:** ISCA proceedings alternate between ACM DL and IEEE
> Xplore by edition. Verify venue attribution through dblp
> (https://dblp.org/db/conf/isca/), never through a publisher search alone — a
> paper's absence from one publisher's library proves nothing at this venue.

---

## How to use this library

These are calibration objects, not citation padding. Find the shape nearest your
project, then ask the paired self-check question with the fit test from
[`../../skills/isca-topic-selection/SKILL.md`](../../skills/isca-topic-selection/SKILL.md)
in hand. Note what the six shapes jointly demonstrate: ISCA's long-run taste
spans *mechanism*, *architecture*, *technology adoption*, *measurement*, and
*design-space cartography* — the venue is broader than "new structure, +N%".

## The verified rows

### Shape 1 — security concern met with an architectural mechanism

- **"New Cache Designs for Thwarting Software Cache-based Side Channel Attacks"**
  — Zhenghong Wang and Ruby B. Lee, ISCA 2007. *Influential ISCA Paper Award
  2025.*
- **Shape:** a threat originating outside classical architecture (side
  channels) answered *inside* the cache organization — the paper's staying
  power came from making security a first-class cache-design constraint.
- **Self-check:** if your paper imports a problem from another community, does
  the solution live in machine organization, and would the other community's
  venue reject it as "too architectural"? That inversion is the ISCA fit.

### Shape 2 — a rethinking of the core's contract with parallelism

- **"Exploiting ILP, TLP, and DLP with the polymorphous TRIPS architecture"** —
  Karthikeyan Sankaralingam, Ramadass Nagarajan, Haiming Liu, Changkyu Kim,
  Jaehyuk Huh, Doug Burger, Stephen W. Keckler, and Charles R. Moore, ISCA 2003.
  *Award 2024.*
- **Shape:** an aggressive full-architecture proposal — one substrate
  reconfiguring across parallelism types — influential for the design space it
  named even where industry took other paths.
- **Self-check:** if your proposal is radical, is the *taxonomy or principle* it
  introduces valuable to readers who will never build it?

### Shape 3 — technology transition turned into architecture

- **"3D-Stacked Memory Architectures for Multi-core Processors"** — Gabriel H.
  Loh, ISCA 2008. *Award 2023.*
- **Shape:** takes an emerging integration technology and works out what it
  means for memory-system organization — the architecture paper that ages best
  when its technology bet lands.
- **Self-check:** does your technology-driven paper contribute organization
  (what to build with it), or only feasibility (that it can be built)? ISCA
  wants the former.

### Shape 4 — measurement that reframed a design space

- **"Power provisioning for a warehouse-sized computer"** — Xiaobo Fan,
  Wolf-Dietrich Weber, and Luiz André Barroso, ISCA 2007. *Award 2022.*
- **Shape:** an industrial measurement study — no new mechanism — whose data
  changed how the field reasoned about datacenter power. Proof that
  characterization can be a flagship-grade ISCA contribution
  (and a natural fit for today's industry track, per
  [`../../skills/isca-topic-selection/SKILL.md`](../../skills/isca-topic-selection/SKILL.md)).
- **Self-check:** if your paper is a measurement study, does it overturn or
  sharpen a design assumption, or only report numbers?

### Shape 5 — mapping and classifying a mechanism space

- **"Techniques for Multicore Thermal Management: Classification and New
  Exploration"** — James Donald and Margaret Martonosi, ISCA 2006. *Award 2021.*
- **Shape:** organizes a crowded technique space into a classification, then
  explores gaps the classification exposes — cartography plus contribution.
- **Self-check:** does your taxonomy *generate* the new design points you
  evaluate, or is it decoration around an unrelated mechanism?

### Shape 6 — quantifying an overlooked cost before it bites

- **"Interconnections in Multi-Core Architectures: Understanding Mechanisms,
  Overheads and Scaling"** — Rakesh Kumar, Victor V. Zyuban, and Dean M.
  Tullsen, ISCA 2005. *Award 2020.*
- **Shape:** rigorous accounting of a cost (on-chip interconnect) the field was
  under-modeling, ahead of the era when it dominated — influence through
  methodology and warning, not through a proposed design.
- **Self-check:** if your contribution is "everyone is modeling X wrong," do you
  show the misestimate changes *conclusions*, not just error bars?

---

## Shape index

| Award year | Original edition | Shape | Modern lane it calibrates |
| --- | --- | --- | --- |
| 2025 | ISCA 2007 | Security constraint → cache mechanism | Side channels, speculation safety, confidential computing |
| 2024 | ISCA 2003 | Polymorphous core architecture | Reconfigurable/spatial architectures, dataflow revivals |
| 2023 | ISCA 2008 | Technology transition → memory organization | CXL-era memory, stacked DRAM, near-memory compute |
| 2022 | ISCA 2007 | Warehouse-scale measurement | Datacenter/AI-fleet characterization, industry track |
| 2021 | ISCA 2006 | Classification + exploration | DVFS/thermal/power-management spaces |
| 2020 | ISCA 2005 | Overhead accounting at scale | NoC, chiplet interconnect, communication-dominated designs |

## Adding rows without hallucinating

1. Take candidates only from the SIGARCH/TCCA award pages or the edition's own
   awards announcements — "famous" is not a criterion; "award-verified" is.
2. Confirm title/author/edition via the dblp entry for that ISCA year before
   writing the row.
3. State shape, not content: nothing the title and award page do not support,
   until you have read the paper itself.
4. Record the award-page URL and access date in
   [`../official-source-map.md`](../official-source-map.md); if verification
   fails, the row is 待核实 and carries no author names.
