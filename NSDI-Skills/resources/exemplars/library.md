# NSDI Exemplars Library (system class × evidence style)

> **Verified via search renderings of dblp and USENIX proceedings pages, access date
> 2026-07-08.** Direct fetches of `dblp.org` and `usenix.org` returned HTTP 403 in the
> verification environment, so each row below was confirmed through search-engine
> renderings of the dblp record and/or the USENIX presentation page, matching venue,
> edition, author list, and (where retrievable) page range. Short and verified beats
> long and guessed: five confirmed rows, with the near-misses documented at the bottom.
>
> **Sibling-confusion guard:** the systems canon scatters across NSDI, OSDI, SOSP,
> SIGCOMM, FAST, USENIX ATC, and USENIX Security, and folklore routinely files famous
> papers under the wrong one. "It's a famous networked-systems paper" does **not**
> mean it is an NSDI paper — prove the venue from dblp or the `usenix.org/conference/
> nsdi<yy>/presentation/...` URL before citing it as one.
>
> **Zero-hallucination rule:** this library records positioning only. Numbers, graphs,
> and design details must be read from the open-access PDFs on `usenix.org` — never
> reconstructed from memory.

---

## How to use this library

Each exemplar shows one way to clear NSDI's distinctive bar: a networked or
distributed system whose **design principle survives contact with real traffic** —
traces, testbeds, or production deployment. Pick the row nearest your system class,
study how the paper pairs its abstraction with operational evidence, and answer the
self-check before calling your draft "NSDI-shaped." Cross-reference
[`../../skills/nsdi-topic-selection/SKILL.md`](../../skills/nsdi-topic-selection/SKILL.md)
for the scope test and
[`../../skills/nsdi-experiments/SKILL.md`](../../skills/nsdi-experiments/SKILL.md) for
the evidence ladder.

## The verified five

### Cluster resource sharing — Mesos (NSDI 2011)

- **Hindman, Konwinski, Zaharia, Ghodsi, Joseph, Katz, Shenker, Stoica, "Mesos: A
  Platform for Fine-Grained Resource Sharing in the Data Center," NSDI 2011 (8th
  edition, Boston, MA), pp. 295-308.** Confirmed via the dblp NSDI 2011 volume and the
  USENIX NSDI '11 presentation page.
- **Why it is an exemplar:** one small interface idea — resource offers — carries the
  whole paper; the evaluation shares a real cluster among Hadoop, MPI, and other
  frameworks rather than simulating the point.
- **Self-check:** can you state your system's interface contribution in one sentence,
  and does your evaluation run *competing real workloads* through it?

### Data-processing frameworks as networked systems — Spark RDDs (NSDI 2012)

- **Zaharia, Chowdhury, Das, Dave, Ma, McCauly, Franklin, Shenker, Stoica, "Resilient
  Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing,"
  NSDI 2012 (9th edition, San Jose, CA), pp. 15-28.** Confirmed via the dblp record
  `conf/nsdi/ZahariaCDDMMFSS12`; Best Paper at NSDI '12 as reported by the Apache
  Spark project (reported fact).
- **Why it is an exemplar:** the contribution is an *abstraction with a stated
  restriction* (coarse-grained transformations) whose payoff — lineage-based fault
  recovery without replication — is then measured against the systems it aims to
  replace.
- **Self-check:** does your abstraction name what it gives up, and is the payoff of
  that restriction quantified?

### Cross-layer measurement infrastructure — X-Trace (NSDI 2007)

- **Fonseca, Porter, Katz, Shenker, Stoica, "X-Trace: A Pervasive Network Tracing
  Framework," NSDI 2007 (4th edition, Cambridge, MA).** Confirmed via the ACM DL
  record of the NSDI '07 proceedings and Brown CS's report of its NSDI Test of Time
  award (2017, reported fact). Page range 待核实.
- **Why it is an exemplar:** instrumentation *is* the system — a tracing metadata
  design that crosses layers and administrative domains, validated by deploying it in
  concrete scenarios rather than by microbenchmarks.
- **Self-check:** if your contribution is observability or diagnosis, does the
  evaluation show it finding real cross-layer behavior, not just overhead numbers?

### Measurement with operational consequence — third-party web tracking (NSDI 2012)

- **Roesner, Kohno, Wetherall, "Detecting and Defending Against Third-Party Tracking
  on the Web," NSDI 2012 (9th edition, San Jose, CA), pp. 155-168.** Confirmed via the
  ACM DL record of the NSDI '12 proceedings; NSDI Test of Time honoree at NSDI '23 as
  reported by UW Allen School and USENIX loginonline (reported fact).
- **Why it is an exemplar:** a measurement paper that earned a systems slot by pairing
  a client-side taxonomy of tracker behavior with a deployed defense — evidence of the
  venue's taste for measurement that changes what gets built.
- **Self-check:** does your measurement end in a design consequence (a mechanism, a
  defense, a policy knob), or only in observations?

### Operational deployment evidence — Firecracker (NSDI 2020)

- **Agache, Brooker, Iordache, Liguori, Neugebauer, Piwonka, Popa, "Firecracker:
  Lightweight Virtualization for Serverless Applications," NSDI 2020 (17th edition),
  pp. 419-434.** Confirmed via the USENIX NSDI '20 presentation page.
- **Why it is an exemplar:** the design story (a minimal VMM specialized for
  function-scale workloads) is inseparable from its production context at AWS — the
  archetype of the operational evidence culture the operational-systems track now
  formalizes.
- **Self-check:** if you claim deployment, can the paper state fleet scale, workload
  provenance, and at least one lesson that contradicted the design's assumptions?

## Coverage matrix

| System class | Exemplar | Edition / pages | Evidence style |
| --- | --- | --- | --- |
| Cluster scheduling / resource sharing | Mesos | 2011 / 295-308 | Shared real cluster, competing frameworks |
| Distributed data processing | Spark RDDs | 2012 / 15-28 | Head-to-head vs incumbent systems |
| Tracing / diagnosis infrastructure | X-Trace | 2007 / 待核实 | Multi-scenario deployment |
| Web measurement + defense | Third-party tracking | 2012 / 155-168 | Large-scale client measurement + built defense |
| Production virtualization | Firecracker | 2020 / 419-434 | Operational deployment at provider scale |

## Do not attribute to NSDI without re-checking

Common misfilings caught during verification — each of these is a *different* venue:

- **Raft ("In Search of an Understandable Consensus Algorithm")** — USENIX **ATC
  2014**, not NSDI.
- **B4 (Google's WAN)** — **SIGCOMM 2013**, not NSDI.
- **Chord** — **SIGCOMM 2001**, not NSDI.
- **Spanner** — **OSDI 2012**, not NSDI.
- **Tor ("The Second-Generation Onion Router")** — **USENIX Security 2004**, not NSDI.

## Adding a row

Confirm the paper on the dblp NSDI stream (`dblp.org/db/conf/nsdi/`) or the USENIX
presentation URL, matching edition number, city, authors, and pages; record which
rendering you used and the access date; label award claims sourced from author
institutions or project sites as **reported**. If the venue cannot be pinned, add the
candidate as 待核实 with no attribution — or leave it out.
