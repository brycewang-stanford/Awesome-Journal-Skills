# MobiCom Exemplars Library (sub-area × contribution)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked
> against **dblp** (`dblp.org/db/conf/mobicom/`) and the **ACM Digital Library** proceedings
> landing to confirm it actually appeared at the **ACM International Conference on Mobile
> Computing and Networking (MobiCom)** — matching the edition number, proceedings title,
> author list, year, and page range. Papers that could not be cleanly confirmed as MobiCom
> (as opposed to INFOCOM, SIGCOMM, NSDI, or a co-located workshop) were **omitted and
> documented below**. This is deliberately a short, verified list (5 verified > 20 guessed).
>
> **Sibling-confusion guard:** MobiCom is **not** INFOCOM, SIGCOMM, or NSDI. Several famous
> wireless papers live in those venues, and one canonical result even has a **same-title
> demo** at a sibling venue. A conference name in a slide deck or a re-hosted PDF is not
> proof — each row below was checked to be a MobiCom edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It
> does not reproduce or invent results, constants, or table numbers — read the original on
> the ACM DL before citing anything. For MobiCom-specific policy, scope, and the
> do-not-misattribute list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **sub-area × contribution** is closest to yours, then study how that
paper states a **wireless or mobile-networking mechanism** up front and then earns it with
**measurement on real hardware** — the MobiCom bar (see
[`../../skills/mobicom-writing-style/SKILL.md`](../../skills/mobicom-writing-style/SKILL.md),
[`../../skills/mobicom-topic-selection/SKILL.md`](../../skills/mobicom-topic-selection/SKILL.md),
and [`../../skills/mobicom-experiments/SKILL.md`](../../skills/mobicom-experiments/SKILL.md)).
For each, ask the self-check question before claiming your paper is "MobiCom-shaped."

**MobiCom edition ↔ year (verified rows below):** 6th = MobiCom 2000; 9th = MobiCom 2003;
11th = MobiCom 2005; 19th = MobiCom 2013.

---

## By sub-area

### Geographic routing (mobile ad-hoc networking / algorithms)

- **Karp & Kung, "GPSR: Greedy Perimeter Stateless Routing for Wireless Networks,"
  MobiCom 2000, pp. 243-254.** Verified: dblp MobiCom 2000; ACM DL
  `10.1145/345910.345953` (6th Annual International Conference on Mobile Computing and
  Networking, Boston, MA).
  - **Why it is an exemplar:** replaces per-destination routing state with **position-based
    greedy forwarding plus a perimeter-mode fallback**, so the contribution is a scaling
    property of the *protocol*, not one topology. A model of the MobiCom "mechanism with a
    stated property" abstract.
  - **Self-check:** is your contribution a networking mechanism with a named property
    (statelessness, a bound, a scaling law), rather than a tuned configuration?

### Sensor-network communication paradigm (data-centric networking)

- **Intanagonwiwat, Govindan & Estrin, "Directed Diffusion: A Scalable and Robust
  Communication Paradigm for Sensor Networks," MobiCom 2000, pp. 56-67.** Verified: dblp
  MobiCom 2000; ACM DL `10.1145/345910.345920`.
  - **Why it is an exemplar:** frames sensor-network communication as **data-centric,
    named-data diffusion with in-network aggregation** — the contribution is an
    *abstraction* that reorganizes a whole design space, exactly the kind of framing move
    MobiCom rewards over an incremental protocol tweak.
  - **Self-check:** does your work name a new abstraction others can build on, and show the
    payoff of adopting it, rather than optimizing inside an existing one?

### Link-quality metric for multi-hop wireless (mesh routing / measurement)

- **De Couto, Aguayo, Bicket & Morris, "A High-Throughput Path Metric for Multi-Hop
  Wireless Routing" (ETX), MobiCom 2003, San Diego, CA.** Verified: dblp MobiCom 2003; the
  MIT PDOS `grid:mobicom03` record. SIGMOBILE Test-of-Time lineage.
  - **Why it is an exemplar:** shows that minimum-hop-count routing loses throughput on
    lossy 802.11 links and replaces it with **expected transmission count**, validated on a
    **29-node testbed** — a mechanism justified by over-the-air measurement, not simulation.
  - **Self-check:** is your metric or mechanism validated on a **real multi-node testbed**
    with the link behavior (loss, asymmetry, interference) that motivates it?

### Unplanned mesh deployment (systems measurement / deployment)

- **Bicket, Aguayo, Biswas & Morris, "Architecture and Evaluation of an Unplanned 802.11b
  Mesh Network" (Roofnet), MobiCom 2005, pp. 31-42.** Verified: dblp MobiCom 2005; ACM DL
  `10.1145/1080829.1080833` (11th edition, Cologne).
  - **Why it is an exemplar:** evaluates a **37-node rooftop mesh spread over an urban
    area** to test whether high performance survives *without* deployment planning —
    the contribution is a measured architectural finding at deployment scale, the strongest
    kind of MobiCom systems evidence.
  - **Self-check:** does your evaluation reach a **real deployment** (or a testbed at
    honest scale), and does it report what the deployment revealed that a lab run would not?

### RF sensing (wireless as a sensor / signal processing)

- **Pu, Gupta, Gollakota & Patel, "Whole-Home Gesture Recognition Using Wireless Signals"
  (WiSee), MobiCom 2013, 19th edition.** Verified: dblp MobiCom 2013; ACM DL
  `10.1145/2500423.2500436`; MobiCom '13 Best Paper. **Note the trap:** a same-title *demo*
  appears at SIGCOMM 2013 — the full paper is the MobiCom one.
  - **Why it is an exemplar:** turns the wireless channel itself into a **whole-home gesture
    sensor** using Doppler shifts, prototyped on **USRP software radios** — a new capability
    from radios, measured over the air, that defines the MobiCom-flavored sensing paper.
  - **Self-check:** is the wireless/RF mechanism the *contribution* (not just the medium),
    and is it demonstrated on real radio hardware under realistic conditions?

---

## By contribution type (each cell is a verified MobiCom paper above)

| Contribution | Verified MobiCom exemplar | Edition / year : pages | Evidence form |
| --- | --- | --- | --- |
| Position-based protocol with a scaling property | Karp & Kung, "GPSR" | 6th / 2000 : 243-254 | Analysis + simulation of the mechanism |
| New communication abstraction | Intanagonwiwat et al., "Directed Diffusion" | 6th / 2000 : 56-67 | Paradigm + evaluation |
| Link-quality metric | De Couto et al., "ETX" | 9th / 2003 | 29-node 802.11b testbed |
| Unplanned mesh architecture | Bicket et al., "Roofnet" | 11th / 2005 : 31-42 | 37-node urban deployment |
| RF sensing capability | Pu et al., "WiSee" | 19th / 2013 | USRP software-radio prototype |

> Five verified papers across five sub-areas. GPSR and Directed Diffusion also show that a
> single edition (MobiCom 2000) can host both an **algorithmic-property** paper and an
> **abstraction** paper — two distinct routes to a MobiCom contribution.

---

## Omitted for lack of clean MobiCom verification (do not attribute to MobiCom without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking —
several are exactly the sibling-venue confusions the header warns about:

- **Bahl & Padmanabhan, "RADAR: An In-Building RF-Based User Location and Tracking System"
  (2000)** — verified to be **IEEE INFOCOM 2000** (Tel Aviv, pp. 775-784), **not MobiCom**.
  A canonical wireless-localization paper frequently misfiled as MobiCom. Listed here only
  as a guardrail.
- **Katti, Rahul, Hu, Katabi, Médard & Crowcroft, "XORs in the Air: Practical Wireless
  Network Coding" (2006)** — verified to be **ACM SIGCOMM 2006** (Pisa, pp. 497-510), **not
  MobiCom**. Wireless topic, wrong venue. Omitted.
- **The WiSee "demo" (2013)** — a **same-title demo** sits in **SIGCOMM 2013**
  (`10.1145/2486001.2491687`); only the **full paper** is MobiCom '13. Cite the MobiCom
  DOI, not the demo, when you mean the paper.
- **ArrayTrack, "A Fine-Grained Indoor Location System"** — commonly co-mentioned with
  MobiCom Test-of-Time presentations, but the paper itself was published at **USENIX NSDI
  2013**, not MobiCom. Do not attribute it to MobiCom; verify on dblp before citing.

Before adding any new paper, confirm it on `dblp.org/db/conf/mobicom/` and the ACM DL by
matching the **edition number to the year** (the proceedings landing names the "Annual
International Conference on Mobile Computing and Networking"), then record author list,
year, and pages, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
