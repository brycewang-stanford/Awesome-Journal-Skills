# ISR Exemplars Library (method × topic)

> **Verified via web search, access date 2026-06-08.** Every paper below was checked against the
> INFORMS PubsOnline article page (`pubsonline.informs.org/doi/10.1287/isre.*`) to confirm it actually
> appeared in *Information Systems Research* (the INFORMS journal, internal code `isre`), with author(s),
> year, and volume/issue where recoverable. Papers outside ISR were **omitted** — this is deliberately a
> short, clean list rather than a long, uncertain one.
>
> **Sibling-confusion guard.** ISR is **not** *MIS Quarterly* (MISQ), *Journal of MIS* (JMIS),
> *Journal of the AIS* (JAIS), or *Management Science* (MS). A paper with an `isre.*` DOI on PubsOnline
> is ISR; an `mnsc.*` DOI is Management Science; MISQ/JMIS/JAIS are not on INFORMS PubsOnline at all.
> Confirmed sibling cases are listed at the bottom as guardrails.
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent coefficients, effect sizes, or specific findings — read the original on PubsOnline
> before citing any number. For ISR-specific scope, length, contribution-statement, and review-model
> facts, see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

ISR is **sociotechnical and intradisciplinary** and houses behavioral, analytical-economic, and
design-science genres as co-equals (see
[`../../skills/isr-topic-selection/SKILL.md`](../../skills/isr-topic-selection/SKILL.md) and
[`../../skills/isr-methods/SKILL.md`](../../skills/isr-methods/SKILL.md)). Pick the row whose
**genre × method × question** is closest to yours, then study how that paper makes the **IT artifact do
load-bearing theoretical work** rather than supply mere context. For each, ask the self-check question
before claiming your paper is "ISR-shaped." The shared empirical-methods hub
([reviewer-objection-checklist](../../../shared-resources/empirical-methods/reviewer-objection-checklist.md),
[reporting-standards](../../../shared-resources/empirical-methods/reporting-standards.md)) covers the
identification and inference table stakes referenced below.

---

## By method

### Archival econometrics on an e-market — endogeneity + welfare (empirical, archival)

- **Ghose, Smith & Telang, "Internet Exchanges for Used Books: An Empirical Analysis of Product Cannibalization and Welfare Impact," ISR 2006, 17(1):3–19.**
  Verified: `pubsonline.informs.org/doi/10.1287/isre.1050.0072`.
  - **Why it is an exemplar:** a digital secondary-market artifact (the used-book exchange) is the
    mechanism, not the backdrop — it changes the structure of the market and lets the authors quantify
    cannibalization *and* consumer-welfare effects from observational data. A model of turning archival
    e-commerce data into a credible economic claim. Pairs with the IV / panel-FE chain in
    [`../code/stata/04_iv.do`](../code/stata/04_iv.do).
  - **Self-check:** would your result change if the IT artifact (the platform/market design) were
    different? If not, the story is IT-as-wallpaper, not an ISR contribution.

### Electronic-markets econometrics — reviews, identity, and sales (empirical, archival)

- **Forman, Ghose & Wiesenfeld, "Examining the Relationship Between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets," ISR 2008, 19(3):291–313.**
  Verified: `pubsonline.informs.org/doi/10.1287/isre.1080.0193`.
  - **Why it is an exemplar:** a platform design feature — whether reviewers disclose identity — is theorized
    to shift how community-generated content moves sales, a genuinely sociotechnical claim (social
    disclosure × a technical affordance). The IT artifact (the review system's identity field) is the locus
    of the mechanism.
  - **Self-check:** is the social and the technical *co-determining* your outcome, or is it a generic
    social-science effect that merely uses platform data?

### Online field experiment — causal effect of a platform intervention (empirical, experimental)

- **Chen & Horton, "Research Note—Are Online Labor Markets Spot Markets for Tasks? A Field Experiment on the Behavioral Response to Wage Cuts," ISR 2016, 27(2).**
  Verified: `pubsonline.informs.org/doi/10.1287/isre.2016.0633`.
  - **Why it is an exemplar:** randomized manipulation of a wage on a real digital-labor platform delivers
    clean causal identification of a behavioral response that the platform's market design makes possible.
    Demonstrates ISR's appetite for field experiments where the platform is the instrument of variation.
  - **Self-check:** does your design isolate quasi-random or randomized variation in an *IT-enabled*
    treatment, rather than estimate a correlation a referee will read as selection?

### Randomized field experiment on an algorithmic artifact (empirical, experimental)

- **Lee & Hosanagar, "How Do Recommender Systems Affect Sales Diversity? A Cross-Category Investigation via Randomized Field Experiment," ISR 2019, 30(1):239–259.**
  Verified: `pubsonline.informs.org/doi/abs/10.1287/isre.2018.0800`.
  - **Why it is an exemplar:** the recommender algorithm *is* the IT artifact under study; randomizing its
    exposure separates individual-level from aggregate-level consumption diversity — a result that only
    exists because the algorithm is the treatment. Exemplary IT-artifact centrality.
  - **Self-check:** is the algorithm/system the thing you manipulate and theorize, or just the data source?

### Analytical game-theoretic model of a platform market (analytical-economic)

- **Zhang, Cheng, Yu & Tan, "To Partner or Not to Partner? The Partnership Between Platforms and Data Brokers in Two-Sided Markets," ISR 2024, 36(3):1437–1460.**
  Verified: `pubsonline.informs.org/doi/10.1287/isre.2022.0470`.
  - **Why it is an exemplar:** a transparent game-theoretic model where agents, payoffs, and the information
    structure (the data broker's role) are the theory; the comparative statics — e.g., that rising privacy
    concern can *encourage* partnering — are the propositions. Shows the analytical-economic genre ISR houses
    co-equally. See [`../../skills/isr-theory-development/SKILL.md`](../../skills/isr-theory-development/SKILL.md)
    on "assumptions are the theory."
  - **Self-check:** do your assumptions map to an IT-enabled decision (platform pricing, data sharing,
    contracting) and deliver one memorable qualitative insight, not just algebra?

### Design-science / design theory for an IS artifact (design science)

- **Walls, Widmeyer & El Sawy, "Building an Information System Design Theory for Vigilant EIS," ISR 1992, 3(1):36–59.**
  Verified: `pubsonline.informs.org/doi/10.1287/isre.3.1.36`.
  - **Why it is an exemplar:** the foundational articulation of an **information system design theory (ISDT)** —
    integrating kernel (descriptive) theory with prescriptive design paths — and the reference point ISR's
    design-science genre still cites. The contribution is an evaluable design artifact and its design
    principles, not an empirical estimate.
  - **Self-check:** does your design-science paper specify the artifact, its design objectives, *and* a
    rigorous evaluation — or is it a build without evaluation (which ISR does not treat as a DSR contribution)?

---

## By topic (each cell is a verified ISR paper above)

| Topic | Verified ISR exemplar | Year / vol(issue) | Genre / method |
| --- | --- | --- | --- |
| Digital markets / cannibalization & welfare | Ghose, Smith & Telang, "Internet Exchanges for Used Books" | 2006, 17(1) | Archival econometrics |
| Online reviews / user-generated content | Forman, Ghose & Wiesenfeld, "Reviewer Identity Disclosure" | 2008, 19(3) | Archival econometrics |
| Digital / gig labor markets | Chen & Horton, "Are Online Labor Markets Spot Markets for Tasks?" | 2016, 27(2) | Online field experiment |
| Recommender systems / algorithmic curation | Lee & Hosanagar, "How Do Recommender Systems Affect Sales Diversity?" | 2019, 30(1) | Randomized field experiment |
| Platform economics / privacy & data brokers | Zhang, Cheng, Yu & Tan, "To Partner or Not to Partner?" | 2024, 36(3) | Analytical game theory |
| IS design theory / decision-support artifacts | Walls, Widmeyer & El Sawy, "Design Theory for Vigilant EIS" | 1992, 3(1) | Design science |

---

## Omitted / sibling-journal guardrails (do **not** attribute to ISR without re-checking)

To keep the list zero-hallucination, the following near-neighbors were **excluded** after checking; several
are classic IS papers that live in ISR's *sibling* journals and are routinely misremembered as ISR:

- **Bharadwaj, "A Resource-Based Perspective on Information Technology Capability and Firm Performance" (2000)** —
  appeared in ***MIS Quarterly***, **not ISR**. Listed only as a guardrail.
- **Bharadwaj, Bharadwaj & Konsynski, "Information Technology Effects on Firm Performance as Measured by Tobin's q" (1999)** —
  appeared in ***Management Science*** (`mnsc.*` DOI), **not ISR**.
- **Fleder & Hosanagar, "Blockbuster Culture's Next Rise or Fall: The Impact of Recommender Systems on Sales Diversity" (2009)** —
  appeared in ***Management Science*** (`mnsc.1080.0974`), **not ISR**. It is the analytical sibling of the
  Lee & Hosanagar ISR field experiment above; do not conflate the two.
- Any paper recalled as "ISR" but found only with an `mnsc.*` DOI, or on a MISQ / JMIS / JAIS page, was
  dropped — these journals are not on INFORMS PubsOnline.

Before adding any new paper to this library, confirm it on `pubsonline.informs.org/doi/10.1287/isre.*`
(article page with volume/issue) and update the access-date header. When in doubt, omit.
