# MISQ Exemplars Library (tradition × method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against MIS
> Quarterly's own article pages (`misq.umn.edu/misq/...`) and/or the AIS Electronic Library MISQ
> collection (`aisel.aisnet.org/misq/...`) to confirm it actually appeared in **MIS Quarterly** — with
> year, volume/issue, and pages. Papers that could not be fully verified as **MISQ** were **omitted** and
> documented below; this is deliberately a short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** MIS Quarterly is **not** *Information Systems Research* (ISR), the *Journal
> of Management Information Systems* (JMIS), the *Journal of the AIS* (JAIS), or *Management Science*.
> Several famous IS papers live in those siblings, not in MISQ; the omissions section names the specific
> traps caught during verification. When in doubt, omit.
>
> **Use principle (zero hallucination):** this file gives **design and positioning guidance only**. It
> does not reproduce or invent coefficients, scale loadings, or specific findings — read the original on
> `misq.umn.edu` / `aisel.aisnet.org/misq` before citing any number. For MISQ-specific scope, limits, and
> a "do-not-misattribute" list, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

MISQ is pluralistic across **four IS traditions** (behavioral, design science, economics of IS,
organizational). Pick the row whose **tradition × method × question** is closest to yours, then study how
that paper makes the **IT artifact load-bearing** and states its contribution in **the currency of its
tradition** — the MISQ bar (see
[`../../skills/misq-topic-selection/SKILL.md`](../../skills/misq-topic-selection/SKILL.md),
[`../../skills/misq-theory-development/SKILL.md`](../../skills/misq-theory-development/SKILL.md), and
[`../../skills/misq-contribution-framing/SKILL.md`](../../skills/misq-contribution-framing/SKILL.md)).
For each, ask the self-check question before claiming your paper is "MISQ-shaped."

> Note: the econometric [`code/`](../code/) kit applies primarily to the **economics-of-IS** row below;
> the behavioral, design-science, and organizational rows are evaluated with SEM, artifact evaluation, and
> qualitative trustworthiness respectively (`misq-data-analysis`).

---

## By tradition × method

### Behavioral — instrument development / measurement (scale validation)

- **Davis, "Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology," MIS Quarterly 1989, 13(3):319–340.**
  Verified: `misq.umn.edu/misq/article-abstract/13/3/319/191/...`; `aisel.aisnet.org/misq/vol13/iss3/6/`.
  - **Why it is an exemplar:** the canonical Technology Acceptance Model (TAM) paper — it develops and
    validates two constructs central to IT use and shows the *artifact-perception → use* link, the
    template for behavioral measurement work in IS.
  - **Self-check:** are your constructs about *IT use/impact specifically*, with reliability and validity
    earned before any structural claim (`misq-data-analysis`)?

### Behavioral — theory integration / unified model (survey, model comparison)

- **Venkatesh, Morris, Davis & Davis, "User Acceptance of Information Technology: Toward a Unified View," MIS Quarterly 2003, 27(3):425–478.**
  Verified: `misq.umn.edu/misq/article/27/3/425/1340/...`; `aisel.aisnet.org/misq/vol27/iss3/5/`.
  - **Why it is an exemplar:** UTAUT — synthesizes eight competing acceptance models into one and tests it,
    showing how MISQ rewards a *consolidating* behavioral contribution, not just one more model.
  - **Self-check:** does your model *adjudicate* among accounts the field already argues over, rather than
    add an n-th untested variant?

### Design science — design-knowledge framework (build-and-evaluate paradigm)

- **Hevner, March, Park & Ram, "Design Science in Information Systems Research," MIS Quarterly 2004, 28(1):75–105.**
  Verified: `misq.umn.edu/misq/article/28/1/75/261/...`; `aisel.aisnet.org/misq/vol28/iss1/6/`.
  - **Why it is an exemplar:** the field-defining statement of the design-science paradigm and its seven
    guidelines — the reference point for "build *and rigorously evaluate* a purposeful IT artifact" and
    for stating transferable **design knowledge**, not one instantiation
    (`misq-theory-development`, `misq-methods`).
  - **Self-check:** does your design-science paper yield generalizable design principles + a real-problem
    evaluation, not "we built it and it ran"?

### Behavioral / IS security — rationality-based survey model (PLS/CB-SEM)

- **Bulgurcu, Cavusoglu & Benbasat, "Information Security Policy Compliance: An Empirical Study of Rationality-Based Beliefs and Information Security Awareness," MIS Quarterly 2010, 34(3):523–548.**
  Verified: `misq.umn.edu/misq/article-abstract/34/3/523/1436/...`.
  - **Why it is an exemplar:** anchors the IS-security-compliance conversation — a behavioral model of why
    employees comply with security policy, with the IT/IS-policy artifact central to the theory, not
    incidental.
  - **Self-check:** is the security/IS artifact load-bearing, and is the measurement model (reliability,
    AVE, discriminant validity, CMB beyond a single-factor test) defended before structure?

### Economics of IS — randomized field experiment (causal identification)

- **Luo, Zhang, Zeng & Qu, "Complementarity and Cannibalization of Offline-to-Online Targeting: A Field Experiment on Omnichannel Commerce," MIS Quarterly 2020, 44(2):957–982.**
  Verified: `misq.umn.edu/misq/article/44/2/957/449/...`; `aisel.aisnet.org/misq/vol44/iss2/17/`.
  - **Why it is an exemplar:** a randomized field experiment delivering *causal* evidence on how a digital
    targeting channel complements vs. cannibalizes offline sales — the model for an economics-of-IS claim
    earning its keep through a credible identification strategy. Pairs naturally with this pack's
    [`code/`](../code/) causal-inference chain (the DiD/IV/RDD/DML skeleton as evidentiary backbone).
  - **Self-check:** does your design isolate quasi-random or experimental variation in the *IT artifact's*
    use that rules out the selection story a referee raises first (`misq-methods`)?

### Organizational — qualitative field study (practice/process theory)

- **Levina & Vaast, "The Emergence of Boundary Spanning Competence in Practice: Implications for Implementation and Use of Information Systems," MIS Quarterly 2005, 29(2):335–363.**
  Verified: `misq.umn.edu/misq/article-abstract/29/2/335/1362/...`; `aisel.aisnet.org/misq/vol29/iss2/8/`.
  - **Why it is an exemplar:** two qualitative field studies build a *process theory* of how
    boundary-spanning competence emerges around IS implementation — the model for a transparent path from
    rich field data to constructs (boundary objects-in-use), with the IT artifact theorized in context.
  - **Self-check:** is the path from raw data → codes → constructs traceable and trustworthy, with the IT
    artifact theorized rather than a backdrop (`misq-data-analysis`)?

---

## By topic (each cell is a verified MISQ paper above)

| Topic | Verified MISQ exemplar | Year / vol(issue):pp | Tradition / method |
| --- | --- | --- | --- |
| Technology acceptance & use | Davis, "Perceived Usefulness, Perceived Ease of Use" | 1989, 13(3):319–340 | Behavioral / scale development |
| Acceptance models, unified | Venkatesh, Morris, Davis & Davis, "Toward a Unified View" (UTAUT) | 2003, 27(3):425–478 | Behavioral / model integration |
| Design-science methodology | Hevner, March, Park & Ram, "Design Science in IS Research" | 2004, 28(1):75–105 | Design science / framework |
| IS security & policy compliance | Bulgurcu, Cavusoglu & Benbasat, "Information Security Policy Compliance" | 2010, 34(3):523–548 | Behavioral–security / SEM |
| Digital platforms & omnichannel commerce | Luo, Zhang, Zeng & Qu, "Complementarity and Cannibalization" | 2020, 44(2):957–982 | Economics of IS / field experiment |
| IS implementation & the future of work | Levina & Vaast, "Boundary Spanning Competence in Practice" | 2005, 29(2):335–363 | Organizational / qualitative |

---

## Omitted for lack of MISQ verification (do not attribute to MISQ without re-checking)

To keep the list zero-hallucination, the following well-known IS papers were **excluded** after web
verification placed them in a **sibling venue**, not MIS Quarterly. They are listed only as guardrails:

- **Brynjolfsson & Hitt, "Paradox Lost? Firm-Level Evidence on the Returns to Information Systems
  Spending" (1996)** — verified to be in ***Management Science*** 42(4):541–558, **not MISQ**. A natural
  economics-of-IS candidate, but the wrong venue.
- **Orlikowski, "Improvising Organizational Transformation Over Time: A Situated Change Perspective"
  (1996)** — verified to be in ***Information Systems Research (ISR)*** 7(1):63–92, **not MISQ**. A
  flagship organizational/qualitative IS paper, but ISR, MISQ's sibling.
- **Pavlou & Gefen, "Building Effective Online Marketplaces with Institution-Based Trust" (2004)** —
  verified to be in ***Information Systems Research (ISR)*** 15(1):37–59, **not MISQ**.
- **Goh, Heng & Lin, "Social Media Brand Community and Consumer Behavior" (2013)** — verified to be in
  ***Information Systems Research (ISR)*** 24(1):88–107, **not MISQ**.
- **Burtch, Ghose & Wattal, "An Empirical Examination of the Antecedents and Consequences of Contribution
  Patterns in Crowd-Funded Markets" (2013)** — verified to be in ***Information Systems Research (ISR)***
  24(3):499–519, **not MISQ**.

Before adding any new paper to this library, confirm it on `misq.umn.edu/misq` or `aisel.aisnet.org/misq`
(article page with volume/issue/pages) and update the access-date header. When a famous IS paper "feels"
like MISQ, check the masthead — it is often ISR, JMIS, JAIS, or *Management Science*. When in doubt, omit.
