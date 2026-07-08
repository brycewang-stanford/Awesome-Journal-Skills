# UIST Exemplars Library (contribution type × era)

> **Verified via web search against ACM Digital Library and dblp records, access date
> 2026-07-08.** Every paper below was confirmed to have appeared in the **ACM Symposium on
> User Interface Software and Technology (UIST) main proceedings** — not CHI, not the UIST
> adjunct proceedings, not a sibling venue. Where an award is noted, its source is given;
> one award claim rests on secondary sources and is flagged. Six verified entries beat a
> longer guessed list.
>
> **Sibling-confusion guard:** the HCI publication circuit (CHI, UIST, CSCW, TEI, IMWUT,
> ISMAR) shares authors, topics, and even system names, and many famous interface papers
> live at CHI or SIGGRAPH rather than UIST. An `uist.acm.org` mention or a demo appearance
> does not prove main-proceedings publication — only the ACM DL / dblp record does.
>
> **Use principle (zero hallucination):** this file gives design positioning only. It does
> not reproduce results, latency figures, or study numbers — read the original in the ACM
> DL before citing anything. Policy and cycle facts live in
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Four of the six entries carry the **UIST Lasting Impact Award** or a reported best-paper
distinction — the community's own signal of what the venue's contribution bar looks like
when it pays off over decades. Pick the row nearest your contribution type, then study how
that paper (a) names an artifact on page one, (b) spends real pages on mechanism, and
(c) matches its evaluation to its claim — the triad taught in
[`../../skills/uist-writing-style/SKILL.md`](../../skills/uist-writing-style/SKILL.md),
[`../../skills/uist-topic-selection/SKILL.md`](../../skills/uist-topic-selection/SKILL.md),
and [`../../skills/uist-experiments/SKILL.md`](../../skills/uist-experiments/SKILL.md).

---

## The exemplars

### Sensor-augmented mobile input (hardware + technique)

- **Hinckley, Pierce, Sinclair & Horvitz, "Sensing Techniques for Mobile Interaction,"
  UIST 2000.** Verified: UIST 2000 proceedings (ACM DL, `dl.acm.org/doi/proceedings/10.1145/354401`);
  **UIST 2011 Lasting Impact Award** (UIST archive pages).
  - **Why it is an exemplar:** instruments a handheld with tilt, touch, and proximity
    sensors and derives a vocabulary of interactions from them — the archetype of the UIST
    move where new sensing hardware plus interaction design yields capabilities, a decade
    before smartphones shipped the same ideas.
  - **Self-check:** does your hardware addition produce *interactions*, or only readings?

### Multi-user touch hardware (enabling technology)

- **Dietz & Leigh, "DiamondTouch: A Multi-User Touch Technology," UIST 2001.** Verified:
  UIST 2001 main proceedings via dblp/ACM DL; **UIST 2012 Lasting Impact Award** (UIST
  archive pages).
  - **Why it is an exemplar:** a table that knows *which* user is touching — a genuinely
    new device capability, presented with the physical mechanism at the center. The paper
    is the clean case of "the artifact is the contribution."
  - **Self-check:** can you state, in one sentence, the capability no prior device had?

### Gesture text entry (interaction technique + algorithm)

- **Kristensson & Zhai, "SHARK2: A Large Vocabulary Shorthand Writing System for Pen-Based
  Computers," UIST 2004.** Verified: `dl.acm.org/doi/10.1145/1029632.1029640` (17th
  symposium, Santa Fe); **UIST 2014 Lasting Impact Award** (UIST archive pages).
  - **Why it is an exemplar:** technique plus recognition architecture plus a
    transfer-of-skill story (tracing that becomes recall-based gesturing), the pattern that
    later shipped in commercial gesture keyboards. Shows how an input technique paper pairs
    algorithmic depth with human performance evidence.
  - **Self-check:** does your technique paper explain the *skill trajectory*, not just the
    novice snapshot?

### Pixel-level UI automation (software system)

- **Yeh, Chang & Miller, "Sikuli: Using GUI Screenshots for Search and Automation,"
  UIST 2009, pp. 183-192.** Verified: `dl.acm.org/doi/10.1145/1622176.1622213`. Best
  Student Paper Award **reported** on an author's CV — treat the award (not the paper) as
  待核实.
  - **Why it is an exemplar:** treats the screen's pixels as a universally available API,
    turning screenshots into a scripting primitive — a systems idea that spawned a tool
    ecosystem. A model for "make the impossible scriptable" toolkit framing.
  - **Self-check:** could someone build something you did not anticipate with your system
    within a week of the release?

### Shape-changing tangible interface (actuated hardware)

- **Follmer, Leithinger, Olwal, Hogge & Ishii, "inFORM: Dynamic Physical Affordances and
  Constraints through Shape and Object Actuation," UIST 2013.** Verified: UIST 2013
  proceedings, St Andrews (`dl.acm.org/doi/proceedings/10.1145/2501988`).
  - **Why it is an exemplar:** a 2.5D actuated pin display plus a design vocabulary
    (affordances and constraints rendered physically) plus application breadth — the
    fabrication-era UIST pattern of hardware, concept, and demo portfolio in one paper,
    with one of the most-watched video figures in the venue's history.
  - **Self-check:** does your hardware paper contribute a *vocabulary* others can design
    with, or only a build log?

### LLM-driven interactive system (the current frontier)

- **Park, O'Brien, Cai, Ringel Morris, Liang & Bernstein, "Generative Agents: Interactive
  Simulacra of Human Behavior," UIST 2023.** Verified:
  `dl.acm.org/doi/10.1145/3586183.3606763` (36th symposium, San Francisco).
  - **Why it is an exemplar:** an architecture (memory stream, reflection, planning) that
    turns LLMs into believable interactive agents, evaluated through the system's emergent
    behavior — evidence that UIST's artifact bar extends to AI-infrastructure work when the
    contribution is the *interactive system architecture*, not the model.
  - **Self-check:** if the underlying model is swapped, does your contribution survive?

---

## By contribution type

| Contribution type | Exemplar | Edition | Recognition |
| --- | --- | --- | --- |
| Sensing hardware → technique vocabulary | Sensing Techniques for Mobile Interaction | UIST 2000 | Lasting Impact 2011 |
| Enabling device capability | DiamondTouch | UIST 2001 | Lasting Impact 2012 |
| Input technique + recognizer | SHARK2 | UIST 2004 | Lasting Impact 2014 |
| Software toolkit / automation | Sikuli | UIST 2009 | Best Student Paper (reported, 待核实) |
| Actuated tangible hardware | inFORM | UIST 2013 | — |
| LLM-based interactive architecture | Generative Agents | UIST 2023 | — |

> The 2000→2023 spread is deliberate: it shows the artifact bar holding constant while the
> substrate moves from accelerometers to LLMs — useful when arguing that an AI-era system
> is "UIST-shaped" (see `uist-topic-selection`).

## Verification recipe before adding a row

1. Find the paper's ACM DL page and confirm the proceedings title says *ACM Symposium on
   User Interface Software and Technology* — and note **main vs adjunct** proceedings
   (posters and demos live in adjunct volumes such as `10.1145/3746058`).
2. Cross-check the edition, year, and authors on `dblp.org/db/conf/uist/`.
3. For award claims, require a `uist.acm.org` awards or archive page; author homepages and
   CVs are secondary sources — include the claim only with a 待核实 flag.
4. Record the DOI and the access date; when in doubt, omit the row.
