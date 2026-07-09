# IEEE PerCom Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** and the **IEEE Xplore / IEEE Computer Society Digital Library** to confirm it appeared
> at the **IEEE International Conference on Pervasive Computing and Communications (PerCom)** —
> matching title, author list, year, and venue string — and, where noted, that it received the
> **Mark Weiser Best Paper Award** or the **PerCom Test of Time Award**. Papers that could not be
> cleanly confirmed as PerCom (as opposed to ACM UbiComp/IMWUT, MobiCom, SenSys, IPSN, or a
> journal) were **omitted and documented below**. It is deliberately a short, verified list
> (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** PerCom is **not** ACM UbiComp/IMWUT, **not** MobiCom, **not**
> SenSys, and **not** IPSN. Much canonical ubicomp work appears at those venues instead; a famous
> author or a familiar system name does **not** prove PerCom. Each row was checked to be a PerCom
> edition specifically (see omissions).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, F1 numbers, or table values — read the original on IEEE Xplore
> before citing anything. For PerCom-specific policy, scope, and the review model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **pervasive-computing problem grounded in real human use**, backs it with **evidence
proportional to the claim** (real subjects, cross-subject evaluation, deployment realism), and
names its **limitations** — the PerCom bar (see
[`../../skills/percom-writing-style/SKILL.md`](../../skills/percom-writing-style/SKILL.md),
[`../../skills/percom-topic-selection/SKILL.md`](../../skills/percom-topic-selection/SKILL.md),
and [`../../skills/percom-experiments/SKILL.md`](../../skills/percom-experiments/SKILL.md)). For
each, ask the self-check question before claiming your paper is "PerCom-shaped."

Several rows are **Mark Weiser Best Paper** or **Test of Time** honorees, so they also model what
influence looks like at this venue.

---

## By contribution shape

### Foundational infrastructure — indoor localization (Test of Time)

- **Ni, Liu, Lau & Patil, "LANDMARC: Indoor Location Sensing Using Active RFID," PerCom 2003.**
  Verified: dblp `db/conf/percom`; IEEE Xplore; **PerCom 2026 Test of Time Award** (inaugural).
  Introduced reference-tag ("landmark") calibration for active-RFID indoor location.
  - **Why it is an exemplar:** it takes a concrete pervasive-computing need — knowing *where*
    things and people are indoors — and delivers a deployable sensing method whose idea (reference
    landmarks to absorb environmental variation) outlived the specific hardware. The problem is
    legible to any ubicomp practitioner and the contribution travels beyond one testbed.
  - **Self-check:** does your system solve a pervasive-computing problem a real deployment would
    hit, with a method whose insight survives a hardware generation?

### Human activity recognition + self-supervision (Mark Weiser Best Paper)

- **"EMGSense: A Low-Effort Self-Supervised Domain Adaptation Framework for EMG Sensing,"
  PerCom 2023.** Verified: IEEE Xplore; PerCom 2023 **Mark Weiser Best Paper Award**. A
  self-supervised domain-adaptation framework reducing labeling effort for EMG-based sensing.
  - **Why it is an exemplar:** it targets the defining pain of wearable HAR — labels are scarce and
    subjects differ — and shows a cross-subject adaptation gain on real EMG signals rather than a
    single-subject accuracy headline. The lesson is about *sensing under distribution shift*, the
    heart of PerCom.
  - **Self-check:** does your evaluation report cross-subject / low-label performance on real
    physiological or motion signals, not just within-subject accuracy?

### System + smart-space simulation (Mark Weiser Best Paper)

- **Chio, Jiang, Gupta, Bouloukakis, Yus, Mehrotra & Venkatasubramanian, "SmartSPEC: Customizable
  Smart Space Datasets via Event-Driven Simulations," PerCom 2022.** Verified: IEEE Xplore;
  PerCom 2022 **Mark Weiser Best Paper Award**. A generator for realistic smart-space datasets via
  event-driven simulation.
  - **Why it is an exemplar:** it answers a reproducibility problem the community feels — real
    smart-space data is scarce and privacy-encumbered — with a tool others can reuse to generate
    and share datasets. A contribution that improves how everyone else evaluates.
  - **Self-check:** does your artifact unblock a data or evaluation bottleneck for other ubicomp
    researchers, not just your own paper?

### Mobile sensing side-channel (Mark Weiser Best Paper)

- **Ning, Wang, Xin, Li & Wu, "DeepMag: Sniffing Mobile Apps in Magnetic Field through Deep
  Convolutional Neural Networks," PerCom 2018.** Verified: IEEE Xplore; PerCom 2018 **Mark Weiser
  Best Paper Award**. Inferring running mobile apps from magnetometer signals via a CNN.
  - **Why it is an exemplar:** it exposes a pervasive-sensing *privacy* consequence — an ordinary
    phone sensor leaks app activity — and quantifies it on real devices. PerCom prizes work that
    surfaces what ubiquitous sensing makes possible, for good or ill.
  - **Self-check:** does your finding change what practitioners believe a commodity sensor can
    reveal, backed by measurements on real hardware?

### Context sharing / device-to-device systems (Mark Weiser Best Paper)

- **Cho & Julien, "CHITCHAT: Navigating Tradeoffs in Device-to-Device Context Sharing,"
  PerCom 2016.** Verified: IEEE Xplore; PerCom 2016 **Mark Weiser Best Paper Award**. A framework
  navigating the tradeoffs of sharing context directly between nearby devices.
  - **Why it is an exemplar:** it treats **context** — the C-word at the center of pervasive
    computing — as a first-class systems problem with explicit tradeoffs, not a modeling
    afterthought. The contribution is a reusable way of reasoning, not a one-off result.
  - **Self-check:** is context modeling / sharing the actual contribution, framed with the
    tradeoffs a real deployment faces?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified PerCom exemplar | Edition | Method |
| --- | --- | --- | --- |
| Foundational infrastructure | Ni et al., "LANDMARC" | PerCom 2003 | Active-RFID landmark localization |
| HAR + self-supervision | "EMGSense" | PerCom 2023 | Self-supervised domain adaptation |
| System + dataset tooling | Chio et al., "SmartSPEC" | PerCom 2022 | Event-driven smart-space simulation |
| Mobile-sensing side-channel | Ning et al., "DeepMag" | PerCom 2018 | CNN on magnetometer signals |
| Context sharing / D2D | Cho & Julien, "CHITCHAT" | PerCom 2016 | Context-sharing tradeoff framework |

> Five verified papers across five contribution shapes, four of them Mark Weiser Best Paper
> honorees and one an inaugural Test of Time honoree — spanning the PerCom range from foundational
> sensing infrastructure to human activity recognition, smart-space tooling, and context systems.

---

## Omitted for lack of clean PerCom verification (do not attribute to PerCom without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **Canonical wearable-HAR deep-learning papers (e.g. DeepConvLSTM lineage)** — several landmark
  HAR papers appear at **ACM UbiComp/IMWUT, ISWC, or in Sensors**, *not* PerCom; do not attribute
  them here without matching the venue string.
- **RF-based sensing landmarks (e.g. RF human sensing)** — much of that lineage is **MobiCom or
  NSDI**, not PerCom. Omitted.
- **Low-power sensor-platform / networked-sensing systems papers** — typically **SenSys or IPSN**,
  the networked-sensor-systems venues, not PerCom's human-centric center. Omitted.
- **UbiComp/IMWUT activity-recognition datasets** — published in the ACM IMWUT journal, a
  different venue and model; cite them to IMWUT, not PerCom.

Before adding any paper, confirm it on **dblp** and **IEEE Xplore** by matching the venue string to
a PerCom edition (not UbiComp/IMWUT, MobiCom, SenSys, IPSN, or a journal), then record authors,
year, and DOI/pages, and update the access-date header. When in doubt, omit. If web search is
unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
