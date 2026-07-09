# Official Source Map - SenSys

Access date: 2026-07-09

This map records the official sources behind every SenSys-specific fact in this pack and,
just as important, how they were read. SenSys rewrites its Call for Papers each edition and,
starting with the 2026 edition, is a **newly merged conference**, so reopen the current CFP,
the edition HotCRP `/deadlines` page, and the artifact-evaluation page before giving any
deadline-sensitive or format-sensitive advice.

## Access-method note (read this first)

Direct programmatic fetches of `sensys.acm.org`, `*.hotcrp.com`, and `dblp.org` returned
**HTTP 403 Forbidden** from the verification environment on 2026-07-09. Every fact below was
therefore read through **search-engine renderings of the exact official URLs** and
cross-checked across independent renderings and the ACM Digital Library proceedings pages.
Where a single rendering carried a fact that a second could not confirm, the fact is marked
**待核实** and phrased as a question, not stated as settled. Treat the URL as the address to
reopen live, not as bytes this pack has verified byte-for-byte.

## Primary official sources

| # | Source URL | What it anchors | Access date |
|---|---|---|---|
| 1 | https://sensys.acm.org/ | SenSys identity as the ACM/IEEE International Conference on **Embedded Artificial Intelligence and Sensing Systems**, and the landing point for the current edition. | 2026-07-09 |
| 2 | https://sensys.acm.org/2026/cfp.html | SenSys 2026 (Second) Call for Papers: the merger of SenSys/IPSN/IoTDI, the two-deadline self-contained review model, and resubmission-with-revision rule. | 2026-07-09 |
| 3 | https://sensys.acm.org/2027/cfp.html | SenSys 2027 CFP: page limits (12-page full / 6-page short, unlimited references and appendices), double-blind anonymity policy, and anonymous-artifact-link rule. | 2026-07-09 |
| 4 | https://sensys27.hotcrp.com/ | SenSys 2027 HotCRP submission site (per-edition instance). | 2026-07-09 |
| 5 | https://sensys26nov.hotcrp.com/deadlines | SenSys 2026 edition HotCRP deadlines surface (per-round cutoffs printed as AoE). | 2026-07-09 |
| 6 | https://sensys.acm.org/tot/ | SenSys Test-of-Time award roll, used only to source venue-verified exemplars. | 2026-07-09 |
| 7 | https://sensys.acm.org/2024/art/ | SenSys artifact-evaluation submission system and the three independent ACM badges (Available / Functional / Reproduced) as run in a recent edition. | 2026-07-09 |
| 8 | https://dblp.org/db/conf/sensys/index.html | dblp SenSys index, used to confirm edition numbers, authorship, and year for every exemplar. | 2026-07-09 |
| 9 | https://dl.acm.org/doi/proceedings/10.1145/3774906 | ACM DL proceedings of the 2026 merged edition ("Embedded Artificial Intelligence and Sensing Systems"). | 2026-07-09 |

## Verified facts used in the skills

- **SenSys 2026 is a merger.** Beginning with the 2026 edition, SenSys, IPSN (Information
  Processing in Sensor Networks), and IoTDI (Internet-of-Things Design and Implementation)
  merged into a **single flagship** conference styled the ACM/IEEE International Conference
  on **Embedded Artificial Intelligence and Sensing Systems** (source 1, 2). The historical
  name — ACM Conference on Embedded Networked Sensor Systems — persists as the `SenSys` brand
  and the dblp key `conf/sensys` (source 8).
- **SenSys 2026 already happened.** It was held **May 11-14, 2026 in Saint-Malo, France**;
  its proceedings are published in the ACM DL (source 9). As of 2026-07-09 the 2026 program
  is complete — the pack treats 2026 as a historical anchor and points live advice at 2027.
- **The open gate is SenSys 2027.** SenSys 2027 is scheduled **May 10-13, 2027 in New York
  City, NY, USA**, submitting through `sensys27.hotcrp.com` (source 3, 4).
- **Two-deadline, self-contained review model.** SenSys runs **two submission deadlines per
  cycle**; each deadline is a **self-contained review round**. A paper rejected at the first
  deadline may enter the second **only with a substantive revision plus a "Response to
  Reviewers" statement mapping each concern to a specific change** (source 2). The SenSys 2027
  **first-round deadline is June 6, AoE** (source 3).
- **Page format (2027).** Full papers are **≤ 12 pages**; short papers (vision/experience,
  etc.) are **≤ 6 pages**; **references and optional appendices are unlimited** and sit
  outside the cap (source 3). The ACM double-column proceedings template applies (待核实 for
  the exact template version/geometry each cycle).
- **Double-blind.** Submissions are fully anonymized: no author names, affiliations, emails,
  or identifying PDF metadata; no acknowledgments during review; self-citations in the third
  person; and **artifact links anonymized** (blinded GitHub/GitLab, Zenodo with anonymized
  authors — no personal/lab/department/company URLs) (source 3).
- **Artifact evaluation via three independent ACM badges.** An Artifact Evaluation Committee
  awards **Artifacts Available**, **Artifacts Evaluated — Functional**, and **Results
  Reproduced**; the badges are independent, authors may seek one/two/all three, and awarded
  badges are printed on the paper and recorded in the ACM DL (source 7). The AEC may request
  iterative artifact revisions.

## Verified exemplar anchors (see exemplars/library.md)

- Maróti, Kusy, Simon & Lédeczi, "The Flooding Time Synchronization Protocol," SenSys 2004
  (2nd) — `dl.acm.org/doi/10.1145/1031495.1031501`; SenSys Test-of-Time award (source 6, 8).
- Gnawali, Fonseca, Jamieson, Moss & Levis, "Collection Tree Protocol," SenSys 2009 (7th) —
  `dl.acm.org/doi/10.1145/1644038.1644040`; SenSys Test-of-Time award (source 6, 8).
- Polastre, Hill & Culler, "Versatile Low Power Media Access for Wireless Sensor Networks"
  (B-MAC), SenSys 2004 (2nd) — SenSys Test-of-Time award (source 6, 8).
- Dunkels, Schmidt, Voigt & Ali, "Protothreads: Simplifying Event-Driven Programming of
  Memory-Constrained Embedded Systems," SenSys 2006 (4th) — SenSys Test-of-Time award
  (source 6, 8).
- Hemminki, Nurmi & Tarkoma, "Accelerometer-Based Transportation Mode Detection on
  Smartphones," SenSys 2013 (11th) — SenSys Test-of-Time award (source 6, 8).

## 待核实 register (do not present as settled)

- The **exact SenSys 2027 second-round deadline**, abstract-registration dates, rebuttal
  window, and notification dates — reopen source 3 and 4 live.
- Whether SenSys 2027 offers an **explicit major-revision channel** at notification (distinct
  from the first→second deadline resubmission-with-revision rule) — 待核实 against source 3.
- The **2026 and 2027 organizing/program chairs and AEC chairs** — not cleanly retrievable on
  2026-07-09; check the current committee page before naming anyone.
- The exact **ACM template version, column geometry, and font floor** for the 2027 cycle.
- The **ethics/human-subjects and AI-use policy wording** for 2027 — reopen the CFP section.
- Whether short papers and full papers share one deadline or are staged — 待核实 on source 3.

## Still cycle-volatile

Future dates, HotCRP instance IDs, page limits, the two-deadline calendar, resubmission
rules, anonymity mechanics, artifact-badge deadlines, ethics/AI-use wording, camera-ready
forms, registration, and presentation obligations. When official pages disagree, the newest
CFP or a direct chair communication controls; record the conflict.
