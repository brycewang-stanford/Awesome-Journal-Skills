# ACM MM Exemplars Library (topic × contribution)

> **Verified via web search against the ACM Digital Library and dblp, access date 2026-07-09.**
> Every paper below was checked to have actually appeared in the **ACM International Conference
> on Multimedia (ACM MM)** — matching the dblp `conf/mm` edition record and the ACM DL entry
> (title, authors where confirmable, year, DOI or page range). Papers that could not be cleanly
> confirmed as **ACM MM main-conference** (as opposed to a sibling venue) were **omitted and
> documented below**. It is deliberately a short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** ACM MM is **not** ICMR (ACM International Conference on Multimedia
> *Retrieval*), **not** MMSys, **not** ACM Multimedia *Asia*, and **not** the *ACM TOMM* journal —
> all SIGMM-adjacent, all different acceptance bars and citation strings. It is also **not** CVPR
> or ICCV: a famous vision paper is usually *not* an ACM MM paper. A "MM" abbreviation or a SIGMM
> connection alone does **not** prove ACM MM — verify the dblp edition line ("ACM International
> Conference on Multimedia").
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, metrics, or table numbers — read the original on the ACM DL before
> citing anything. Where an author list was not fully confirmed at check time, it is marked
> *(confirm full author list on ACM DL)*. For ACM MM-specific policy and the do-not-misattribute
> list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **topic × contribution type** is closest to yours, then study how that paper
makes a *multimedia* point — a tool the community reuses, a cross-modal method, or an
affective/perceptual result — rather than a single-modality benchmark win (the ACM MM bar; see
[`../../skills/acmmm-writing-style/SKILL.md`](../../skills/acmmm-writing-style/SKILL.md),
[`../../skills/acmmm-topic-selection/SKILL.md`](../../skills/acmmm-topic-selection/SKILL.md), and
[`../../skills/acmmm-experiments/SKILL.md`](../../skills/acmmm-experiments/SKILL.md)). For each,
ask the self-check before claiming your paper is "ACM MM-shaped."

**ACM MM edition ↔ year (verified rows below):** 18th = MM '10 (2010); 22nd = MM '14 (2014);
25th = MM '17 (2017).

---

## By contribution type

### Open-source system / framework (tool the community reuses)

- **Jia, Shelhamer, Donahue, Karayev, Long, Girshick, Guadarrama & Darrell, "Caffe:
  Convolutional Architecture for Fast Feature Embedding," ACM MM 2014 (22nd), Orlando.**
  Verified: ACM DL `10.1145/2647868.2654889`; a SIGMM Test-of-Time honoree.
  - **Why it is an exemplar:** the contribution is a *reusable, well-engineered framework* with
    reference models — the kind of artifact ACM MM's Open Source Software Competition exists to
    reward, valued for adoption rather than a single leaderboard number.
  - **Self-check:** is your system usable by others as infrastructure, with a clear license and
    reproducible reference models, not just a research prototype?

### Open-source library (reproducible-research infrastructure)

- **Vedaldi & Fulkerson, "VLFeat: An Open and Portable Library of Computer Vision Algorithms,"
  ACM MM 2010 (18th), pp. 1469–1472.**
  Verified: ACM DL `10.1145/1873951.1874249`; a SIGMM Test-of-Time honoree.
  - **Why it is an exemplar:** packages common building blocks as a portable library so others can
    prototype and *reproduce* — the paper's value is enabling multimedia research, not a new score.
  - **Self-check:** does your release lower the cost of the community's next paper, and is that the
    contribution you are actually claiming?

### Affective / perceptual multimedia (human-centric content analysis)

- **Machajdik & Hanbury, "Affective Image Classification Using Features Inspired by Psychology and
  Art Theory," ACM MM 2010 (18th), pp. 83–92.** *(confirm full author list on ACM DL.)*
  Verified: ACM MM 2010 proceedings, pages 83–92; named on the SIGMM Test-of-Time page.
  - **Why it is an exemplar:** it fuses *psychology and art-theory* features with classification —
    an emotion/aesthetics contribution that is multimedia precisely because it crosses content and
    human perception, a natural fit for the Emotional/Social-Signals and Art-and-Culture areas.
  - **Self-check:** does your paper connect media content to human response with domain-grounded
    features, rather than treating the image as a generic vision benchmark?

### Cross-modal retrieval via adversarial learning (multimodal representation)

- **Wang et al., "Adversarial Cross-Modal Retrieval," ACM MM 2017 (25th).** *(confirm full author
  list on ACM DL.)*
  Verified: ACM DL `10.1145/3123266.3123326` (Proceedings of the 25th ACM international conference
  on Multimedia).
  - **Why it is an exemplar:** learns a *modality-invariant* representation with an adversarial
    objective so text and image live in one space — the contribution is the cross-modal bridge
    itself, the Multimodal-Fusion / Search-and-Recommendation heartland of ACM MM.
  - **Self-check:** is the fusion mechanism the contribution (and ablated as such), rather than a
    single-modality encoder swap?

### Cross-modal retrieval via correspondence autoencoders (representation learning)

- **Feng, Wang & Li, "Cross-modal Retrieval with Correspondence Autoencoder," ACM MM 2014 (22nd),
  pp. 7–16.**
  Verified: ACM MM 2014 proceedings, pages 7–16.
  - **Why it is an exemplar:** couples per-modality autoencoders through a correspondence objective
    to align image and text — an early, clean statement of the "learn a shared space" idea that
    ACM MM retrieval work builds on; pairs with the adversarial row as a *research line*.
  - **Self-check:** does your method state and test the alignment assumption between modalities,
    not just report retrieval numbers?

---

## By topic (each cell is a verified ACM MM paper above)

| Topic | Verified ACM MM exemplar | Edition / year : locator | Contribution type |
| --- | --- | --- | --- |
| Deep-learning framework | Jia et al., "Caffe" | 2014 / 22nd : `10.1145/2647868.2654889` | Open-source system |
| CV library / reproducibility | Vedaldi & Fulkerson, "VLFeat" | 2010 / 18th : pp. 1469–1472 | Open-source library |
| Emotion / aesthetics | Machajdik & Hanbury, "Affective Image Classification" | 2010 / 18th : pp. 83–92 | Human-centric analysis |
| Cross-modal retrieval | Wang et al., "Adversarial Cross-Modal Retrieval" | 2017 / 25th : `10.1145/3123266.3123326` | Adversarial multimodal representation |
| Cross-modal retrieval | Feng, Wang & Li, "Correspondence Autoencoder" | 2014 / 22nd : pp. 7–16 | Shared-space representation |

> Five verified papers across five topic × contribution cells. The Caffe/VLFeat pair shows the
> **open-source lane** ACM MM rewards for adoption; the two retrieval rows show a **research line**
> (correspondence autoencoders → adversarial alignment) useful for positioning an incremental but
> principled cross-modal contribution.

---

## Omitted for lack of clean ACM MM verification (do not attribute to ACM MM without re-checking)

To keep the list zero-hallucination, the following classes were **excluded** after checking —
several are exactly the sibling-venue confusions the header warns about:

- **Cross-modal retrieval / hashing papers indexed under ICMR or SIGIR** (e.g., latent-semantic
  sparse hashing at SIGIR '14; semantics-preserving hashing at CVPR '15) — these are **not ACM MM
  main-conference** papers even though they share the retrieval topic. Omitted.
- **Papers in the ACM TOMM journal or ACM Multimedia *Asia*** — SIGMM-adjacent but a different
  citation string and acceptance process. Omitted unless the dblp `conf/mm` edition line confirms
  the main conference.
- **Famous computer-vision papers** whose canonical placement is CVPR/ICCV/ECCV — a MM-adjacent
  topic does not make them ACM MM papers. Omitted.

Before adding any new paper, confirm it on the ACM DL and dblp by matching the **edition line
("ACM International Conference on Multimedia") to the year**, then record authors, DOI, and pages,
and update the access-date header. When in doubt, omit. If web search is unavailable, add the row
as **待核实 / TO VERIFY** with **no attribution**.
