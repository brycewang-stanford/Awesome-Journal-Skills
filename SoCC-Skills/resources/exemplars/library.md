# ACM SoCC Exemplars Library (contribution shape × method)

> **Verified via web search, access date 2026-07-09.** Every paper below was checked against
> **dblp** (`conf/cloud` — the SoCC stream) and the **ACM Digital Library** to confirm it appeared
> at the **ACM Symposium on Cloud Computing (SoCC)** — matching title, author list, year, and
> venue string. Papers that could not be cleanly confirmed as SoCC (as opposed to OSDI, NSDI,
> EuroSys, ATC, SOSP, SIGMOD, or VLDB) were **omitted and documented below**. It is deliberately a
> short, verified list (5 verified > 15 guessed).
>
> **Sibling-confusion guard:** SoCC is **not** OSDI, **not** NSDI, **not** EuroSys, **not** ATC,
> and **not** SIGMOD/VLDB. Several canonical cloud systems (Spark, Mesos, Borg, TensorFlow) were
> introduced at *those* venues, not SoCC; a famous system or author does **not** prove a SoCC
> placement. Each row was checked to be a SoCC edition specifically (see omissions). Also beware
> the unrelated **IEEE SoCC** (System-on-Chip Conference).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, throughput numbers, or table figures — read the original on ACM DL
> before citing anything. For SoCC-specific policy, scope, and the two-round model, see
> [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **contribution shape × method** is closest to yours, then study how that paper
states a **cloud-scale problem an operator or platform team recognizes**, backs it with
**measurement on a real or realistic system**, and reports **cost/throughput/tail behavior**
honestly — the SoCC bar (see
[`../../skills/socc-writing-style/SKILL.md`](../../skills/socc-writing-style/SKILL.md),
[`../../skills/socc-topic-selection/SKILL.md`](../../skills/socc-topic-selection/SKILL.md), and
[`../../skills/socc-experiments/SKILL.md`](../../skills/socc-experiments/SKILL.md)). For each, ask
the self-check question before claiming your paper is "SoCC-shaped."

SoCC's dual SIGMOD+SIGOPS identity is visible in the list: measurement/benchmarking studies,
storage and data-management systems, and resource-management systems all live here, side by side.

---

## By contribution shape

### Measurement + benchmark — cloud data serving

- **Cooper, Silberstein, Tam, Ramakrishnan & Sears, "Benchmarking Cloud Serving Systems with
  YCSB," SoCC 2010, pp. 143-154** (DOI 10.1145/1807128.1807152). Verified: dblp
  `rec/conf/cloud/CooperSTRS10`. Introduced **YCSB**, an open benchmark and workload generator for
  cloud key-value/serving stores.
  - **Why it is an exemplar:** it built a **shared measurement instrument** the whole community
    adopted, framing a data-systems problem (how do we compare serving stores?) and delivering a
    reusable tool plus a comparative study — the SIGMOD side of SoCC's identity in one paper.
  - **Self-check:** does your measurement give the community an instrument or a comparison it
    lacked, on real systems, rather than a one-off number on your own?

### Measurement + trace study — datacenter workloads

- **Reiss, Tumanov, Ganger, Katz & Kozuch, "Heterogeneity and Dynamicity of Clouds at Scale:
  Google Trace Analysis," SoCC 2012** (DOI 10.1145/2391229.2391236). Verified: dblp
  `rec/conf/cloud/ReissTGKK12`; later a SoCC **Test of Time** honoree.
  - **Why it is an exemplar:** it turned a newly released production **cluster trace** into
    durable findings about heterogeneity and dynamicity that reshaped how schedulers are designed
    — measurement whose value is the *insight about real infrastructure*, not a built system.
  - **Self-check:** does your study change what the community believes about how real datacenters
    behave, with a trace or dataset a reviewer could scrutinize and others could reuse?

### Systems-building — storage QoS / multi-tenancy

- **Wang, Venkataraman, Alspaugh, Katz & Stoica, "Cake: Enabling High-level SLOs on Shared Storage
  Systems," SoCC 2012** (DOI 10.1145/2391229.2391249). Verified: dblp `conf/cloud` / author copy
  `cake-socc12.pdf`. A coordinated multi-resource scheduler enforcing latency+throughput SLOs on
  shared distributed storage.
  - **Why it is an exemplar:** it takes a **multi-tenancy** pain point operators feel — mixed
    latency-sensitive and batch workloads contending for one storage tier — and delivers a
    mechanism evaluated on a real system against the consolidation it enables.
  - **Self-check:** does your system solve a resource-sharing problem a cloud operator names
    unprompted, and is it evaluated on a realistic deployment rather than a simulator alone?

### Systems-building — big-data resource management

- **Vavilapalli et al., "Apache Hadoop YARN: Yet Another Resource Negotiator," SoCC 2013**
  (DOI 10.1145/2523616.2523633). Verified: dblp `conf/cloud` / ACM DL. The resource-management
  redesign that decoupled Hadoop's programming model from cluster resource management.
  - **Why it is an exemplar:** an **experience + systems** paper about a widely deployed platform,
    reporting the design decisions and production lessons of running a resource negotiator at
    scale — SoCC's welcome mat for real-world experience papers, not only clean-slate research.
  - **Self-check:** does your paper carry deployment experience or design lessons that only a
    real, operated system could produce, reported honestly including what did not work?

### Systems-building — serverless / stateful cloud (recent)

- **Copik, Calotoiu, Réthy, Böhringer, Bruno & Hoefler, "Process-as-a-Service: Unifying Elastic
  and Stateful Clouds with Serverless Processes," SoCC 2024.** Verified: dblp
  `db/conf/cloud/socc2024`. A serverless abstraction unifying elastic and stateful execution.
  - **Why it is an exemplar:** it shows SoCC's **current** center of gravity — serverless and the
    elastic/stateful tension — with a new abstraction plus a systems evaluation, the modern
    counterpart to the classic resource-management lineage above.
  - **Self-check:** if your contribution is an abstraction, is it evaluated as a *built system*
    with realistic workloads, and does the cloud lesson survive independent of any one runtime?

---

## Contribution-shape ↔ exemplar (verified rows)

| Contribution shape | Verified SoCC exemplar | Edition | Method |
| --- | --- | --- | --- |
| Measurement + benchmark | Cooper et al., "YCSB" | SoCC 2010 | Benchmark + workload generator |
| Measurement + trace study | Reiss et al., "Google Trace Analysis" | SoCC 2012 | Production-trace analysis (Test of Time) |
| Systems-building (storage QoS) | Wang et al., "Cake" | SoCC 2012 | Multi-resource SLO scheduler |
| Systems + experience | Vavilapalli et al., "Apache Hadoop YARN" | SoCC 2013 | Deployed resource negotiator |
| Systems-building (serverless) | Copik et al., "Process-as-a-Service" | SoCC 2024 | Serverless stateful abstraction |

> Five verified papers across five contribution shapes. The two SoCC 2012 rows show the venue's
> twin identities in the same year — a *measurement* study (Google trace) and a *systems* build
> (Cake) — reflecting the joint SIGMOD+SIGOPS sponsorship.

---

## Omitted for lack of clean SoCC verification (do not attribute to SoCC without re-checking)

To keep the list zero-hallucination, the following were **excluded** after checking — several are
exactly the sibling-venue confusions the header warns about:

- **"Mesos: A Platform for Fine-Grained Resource Sharing in the Data Center" (Hindman et al.)** —
  **NSDI 2011**, not SoCC. A classic datacenter-resource paper at a sibling venue; listed as a
  guardrail.
- **"Large-scale cluster management at Google with Borg" (Verma et al.)** — **EuroSys 2015**, not
  SoCC. Omitted.
- **"Resilient Distributed Datasets" (Zaharia et al., Spark)** — **NSDI 2012**, not SoCC. Omitted
  despite being canonical big-data-systems work.
- **"TensorFlow: A System for Large-Scale Machine Learning" (Abadi et al.)** — **OSDI 2016**, not
  SoCC. Omitted.
- **"Spanner: Google's Globally-Distributed Database" (Corbett et al.)** — **OSDI 2012**, not
  SoCC. A data-systems paper, but at a systems flagship; omitted.

Before adding any paper, confirm it on **dblp** (`conf/cloud`) and **ACM DL** by matching the
venue string to a SoCC edition (not OSDI, NSDI, EuroSys, ATC, SOSP, SIGMOD, or VLDB), then record
authors, year, and DOI/pages, and update the access-date header. When in doubt, omit. If web
search is unavailable, add the row as **待核实 / TO VERIFY** with **no attribution**.
