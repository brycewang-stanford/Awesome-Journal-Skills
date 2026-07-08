# EuroSys Exemplars Library (topic × era)

> **Verified via web search, access date 2026-07-08.** Every paper below was confirmed to be a
> EuroSys paper through at least two of: the EuroSys Test-of-Time Award page
> (`eurosys.org/awards/test-of-time-award`), dblp's EuroSys index (`dblp.org/db/conf/eurosys/`),
> the ACM DL EuroSys proceedings, or an official EuroSys awards page. Direct fetches of the
> conference domains were blocked in the verification environment, so renderings were
> cross-checked across independent hosts. Papers that could not be pinned to EuroSys were left
> out — a short list that is right beats a long list that guesses.
>
> **Sibling-confusion guard:** the systems canon scatters across SOSP, OSDI, NSDI, ATC, and
> EuroSys, and famous infrastructure papers are routinely mis-shelved. MapReduce and TensorFlow
> are **OSDI** papers; Spark's RDD paper is **NSDI**; ZooKeeper is **ATC**. Conversely, several
> Google cluster-management landmarks that people guess are OSDI — Omega, Borg — are **EuroSys**
> papers. Check dblp before attributing anything.
>
> **Use principle (zero hallucination):** rows carry positioning lessons only. Numbers,
> architectures, and claims must be read from the papers themselves on the ACM DL. Policy facts
> live in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Find the row closest to your project's shape, read how that paper earned its place — almost
always a **retellable mechanism plus an evaluation that explains itself** — and apply the row's
self-check. Pair with
[`../../skills/eurosys-topic-selection/SKILL.md`](../../skills/eurosys-topic-selection/SKILL.md)
for routing and
[`../../skills/eurosys-experiments/SKILL.md`](../../skills/eurosys-experiments/SKILL.md) for the
evidence stack.

---

## Test-of-Time line (award-verified, with award year)

### Dataflow execution — Dryad (EuroSys 2007; Test-of-Time 2017)

- **Isard, Budiu, Yu, Birrell & Fetterly, "Dryad: Distributed Data-Parallel Programs from
  Sequential Building Blocks."**
  - **Lesson:** a general execution abstraction (arbitrary DAGs of sequential programs)
    presented through a buildable engine — the idea outlived the engine and shaped a decade of
    dataflow systems.
  - **Self-check:** does your abstraction subsume the special cases people already run, and can
    you demonstrate that subsumption concretely?

### Program transformation for systems code — Coccinelle (EuroSys 2008; Test-of-Time 2018)

- **Padioleau, Lawall, Hansen & Muller, "Documenting and Automating Collateral Evolutions in
  Linux Device Drivers."**
  - **Lesson:** a EuroSys paper can be a *tool with a thesis* — that driver-API churn is
    systematic enough to automate — validated against the actual Linux tree rather than a toy.
    The award line also explains why EuroSys's artifact prize carries Gilles Muller's name.
  - **Self-check:** is your evidence base the real code ecosystem you claim to serve?

### Cluster scheduling I — Delay Scheduling (EuroSys 2010; Test-of-Time 2020)

- **Zaharia, Borthakur, Sen Sarma, Elmeleegy, Shenker & Stoica, "Delay Scheduling: A Simple
  Technique for Achieving Locality and Fairness in Cluster Scheduling."**
  - **Lesson:** the mechanism fits in its own title. A deliberately small idea, measured on
    production-shaped workloads, beat heavier machinery — EuroSys rewards ideas sized to their
    evidence.
  - **Self-check:** if your mechanism is simple, is the evaluation strong enough to make
    simplicity the headline rather than the apology?

### Cluster scheduling II — Omega (EuroSys 2013; Test-of-Time 2023)

- **Schwarzkopf, Konwinski, Abd-El-Malek & Wilkes, "Omega: flexible, scalable schedulers for
  large compute clusters."**
  - **Lesson:** names a design space (monolithic vs two-level vs shared-state scheduling) and
    argues its corner with simulation driven by real Google workload traces — taxonomy plus
    evidence as a contribution shape.
  - **Self-check:** does your paper give reviewers a vocabulary for the design space, not just
    a point solution in it?

### Production experience — Borg (EuroSys 2015; Test-of-Time 2019)

- **Verma, Pedrosa, Korupolu, Oppenheimer, Tune & Wilkes, "Large-scale cluster management at
  Google with Borg."**
  - **Lesson:** the definitive template for an experience paper: a decade of operation
    distilled into lessons others can act on, with warts documented. EuroSys is a first-class
    home for honest production retrospectives.
  - **Self-check:** if writing an experience paper, do the lessons generalize beyond your
    operator, and do you show the failures alongside the wins?

## Current era (award-verified, 2025 edition)

### LLM serving — CacheBlend (EuroSys 2025; Best Paper)

- **Yao, Li, Liu, Ray, Cheng, Zhang, Du, Lu & Jiang, "CacheBlend: Fast Large Language Model
  Serving for RAG with Cached Knowledge Fusion."** ACM DL: DOI `10.1145/3689031.3696098`,
  pp. 94–109, Proceedings of the Twentieth European Conference on Computer Systems.
  - **Lesson:** the venue's center of gravity now includes ML-serving infrastructure; the
    winning shape is unchanged — a reusable mechanism (selective KV-cache recomputation and
    fusion) with a systems-grade evaluation, not a model-quality result.
  - **Self-check:** is your ML-systems contribution a *systems* mechanism that would interest
    someone who never trains models?

---

## Topic × era grid

| Topic | Exemplar | Edition (award) | Contribution shape |
| --- | --- | --- | --- |
| Dataflow / execution engines | Dryad | 2007 (ToT 2017) | General abstraction + engine |
| Systems tooling on real codebases | Coccinelle collateral evolutions | 2008 (ToT 2018) | Tool with a thesis |
| Scheduling mechanisms | Delay Scheduling | 2010 (ToT 2020) | Small idea, production evidence |
| Scheduler architecture | Omega | 2013 (ToT 2023) | Design-space taxonomy + traces |
| Production experience | Borg | 2015 (ToT 2019) | Operational retrospective |
| ML-serving systems | CacheBlend | 2025 (Best Paper) | Mechanism for LLM inference infra |

The 2007→2025 spread is intentional: it shows the through-line (mechanism + believable
evidence) surviving three technology generations, which is what "EuroSys-shaped" means.

---

## Do-not-misattribute list (checked 2026-07-08)

- **MapReduce** (Dean & Ghemawat) — **OSDI 2004**, not EuroSys.
- **TensorFlow** — **OSDI 2016**, not EuroSys.
- **Resilient Distributed Datasets (Spark)** — **NSDI 2012**, not EuroSys.
- **ZooKeeper** — **USENIX ATC 2010**, not EuroSys.
- **Mesos** — **NSDI 2011**, often confused with the EuroSys scheduling line above.
- **SpInfer** (EuroSys 2025 co-best-paper) is genuinely EuroSys but its full author list was
  only partially verifiable here — confirm on dblp before citing it with authors.

To add a row: locate the paper in `dblp.org/db/conf/eurosys/eurosysYYYY.html`, confirm the DOI
resolves to the ACM DL EuroSys proceedings, record pages and edition, and update the access
date. If either check fails, the row goes under this section as 待核实, never into the grid.
