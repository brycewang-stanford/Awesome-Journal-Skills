# CSCW Exemplars Library (Lasting Impact lineage + PACMHCI era)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked
> against the ACM Digital Library, dblp, or the official CSCW Lasting Impact Award
> page (https://cscw.acm.org/2026/lastingimpact.html) to confirm it is genuinely a
> CSCW paper — not a CHI, GROUP, or DIS sibling. Four of the five carry the
> **CSCW Lasting Impact Award**, the venue's own signal of what work it considers
> foundational; the fifth anchors the modern PACMHCI era.
>
> **Sibling-confusion guard:** CSCW shares authors, topics, and the ACM DL with CHI,
> GROUP, DIS, and ICWSM. Since 2017, CSCW papers are **journal articles in PACMHCI**
> (e.g., "Proc. ACM Hum.-Comput. Interact., Vol. 1, No. CSCW, Article 31"), so a
> citation that says "In Proceedings of CSCW 2019" is already suspect. Before 2017,
> they are conference proceedings papers. Verify era-appropriate citation form on
> dblp before reusing any row.
>
> **Use principle (zero hallucination):** this file gives design positioning only.
> It does not reproduce findings, effect sizes, or participant counts — read the
> original before citing anything. Venue policy lives in
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Match on the **kind of contribution** — organizational analysis, coordination
concept, theoretical lens, activist community study, or large-scale trace analysis —
rather than on topic keywords. Each entry names the move that made the paper durable
and a self-check question. Pair with
[`../../skills/cscw-topic-selection/SKILL.md`](../../skills/cscw-topic-selection/SKILL.md)
for routing and
[`../../skills/cscw-experiments/SKILL.md`](../../skills/cscw-experiments/SKILL.md)
for evidence design.

---

## The exemplars

### 1. The organizational-failure analysis

- **Grudin, "Why CSCW Applications Fail: Problems in the Design and Evaluation of
  Organizational Interfaces," CSCW 1988.** Lasting Impact Award 2014.
  - **The durable move:** explains system failure through the *misalignment between
    who does the work and who gets the benefit* — an organizational mechanism, not a
    usability defect. The unit of analysis is the group, which is the defining CSCW
    posture.
  - **Self-check:** does your paper explain an outcome through group-level
    incentives and structures, or does it quietly collapse back to a single user?

### 2. The coordination-concept paper

- **Dourish & Bellotti, "Awareness and Coordination in Shared Workspaces,"
  CSCW 1992.** Lasting Impact Award 2016.
  - **The durable move:** names and defines a concept — awareness — that the whole
    field could subsequently design with and argue about. The contribution is a
    *vocabulary*, grounded in observed collaborative practice.
  - **Self-check:** if your paper offers a concept, can another researcher apply it
    to a system you never studied and get analytic traction?

### 3. The theoretical-lens paper

- **Harrison & Dourish, "Re-place-ing Space: The Roles of Place and Space in
  Collaborative Systems," CSCW 1996.** Lasting Impact Award 2021.
  - **The durable move:** imports and sharpens a distinction (space vs. place) that
    reframes how designers think about mediated environments. Theory earns its place
    at CSCW by changing what builders do, not by decoration.
  - **Self-check:** does your theoretical framing generate design consequences a
    reviewer could paraphrase in one sentence?

### 4. The social-movement community study

- **Dimond, Dye (Thomas), LaRose & Bruckman, "Hollaback!: The Role of Storytelling
  Online in a Social Movement Organization," CSCW 2013.** Lasting Impact Award
  2025 (dblp: `conf/cscw/DimondDLB13`, DOI 10.1145/2441776.2441831).
  - **The durable move:** qualitative fieldwork with an activist organization,
    treating storytelling as *work* that the platform mediates — and handling a
    sensitive community with visible ethical care. A model for interview-based CSCW
    papers about vulnerable or politically exposed groups.
  - **Self-check:** could a member of the community you studied read your paper
    without feeling exposed or misrepresented?

### 5. The PACMHCI-era trace analysis

- **Chandrasekharan, Pavalanathan, Srinivasan, Glynn, Eisenstein & Gilbert, "You
  Can't Stay Here: The Efficacy of Reddit's 2015 Ban Examined Through Hate Speech,"
  Proc. ACM Hum.-Comput. Interact., Vol. 1, No. CSCW, Article 31 (2017).** Verified:
  `dl.acm.org/doi/10.1145/3134666`.
  - **The durable move:** a platform-governance question answered with large-scale
    trace data and causal-inference methods, published in the journal's first CSCW
    volume — the modern quantitative CSCW template, and the correct citation form
    for the PACMHCI era.
  - **Self-check:** does your trace analysis state its causal identification
    strategy and its construct-validity limits, not just its data volume?

---

## Coverage map

| Contribution kind | Exemplar | Era / citation form | Method family |
| --- | --- | --- | --- |
| Organizational analysis | Grudin 1988 | Proceedings era | Analytic essay from field experience |
| Coordination concept | Dourish & Bellotti 1992 | Proceedings era | Concept development from practice |
| Theoretical lens | Harrison & Dourish 1996 | Proceedings era | Theory for design |
| Sensitive community study | Dimond et al. 2013 | Proceedings era | Qualitative fieldwork / interviews |
| Platform trace analysis | Chandrasekharan et al. 2017 | PACMHCI journal era | Computational + causal inference |

> The five rows deliberately span CSCW's methods pluralism — essayistic, conceptual,
> theoretical, qualitative, and computational work all sit in the venue's own canon.
> A paper that treats only one of these registers as "real research" is arguing with
> the award list.

---

## Verification recipe before adding a row

1. Find the paper on **dblp** under `conf/cscw` (pre-2017) or in **PACMHCI** with a
   `No. CSCW` issue label (2017 onward); record the DOI.
2. Confirm the venue string on the ACM DL landing page names Computer-Supported
   Cooperative Work — CHI Proceedings and PACMHCI's other tracks look nearly
   identical at a glance.
3. For award claims, cite the official award page, not memory or a lab bio.
4. If any step fails, add the row as **待核实 / TO VERIFY** with no attribution, or
   omit it. Update the access-date header whenever a row changes.
