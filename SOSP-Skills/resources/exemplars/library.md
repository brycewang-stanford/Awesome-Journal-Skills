# SOSP Exemplars Library (problem × principle)

> **Verified via web search, access date 2026-07-08.** Every paper below was checked against
> **dblp's SOSP series** (`dblp.org/db/conf/sosp/`) and the ACM Digital Library SOSP proceedings
> to confirm it appeared at the **ACM Symposium on Operating Systems Principles** — matching the
> edition, year, and (where surfaced) page range. Candidates that could not be cleanly pinned to
> SOSP were **omitted and listed below**, because the systems literature's most famous papers are
> scattered across sibling venues and misattribution is the default failure. Short and verified
> beats long and guessed.
>
> **Sibling-confusion guard:** SOSP is **not** OSDI, USENIX ATC, EuroSys, or NSDI, even though the
> same groups publish across all of them and the SIGOPS Hall of Fame draws from both SOSP *and*
> OSDI. "Everyone cites it in systems courses" does not place a paper at SOSP — check the venue
> line on dblp before writing "appeared at SOSP" in a related-work section.
>
> **Use principle (zero hallucination):** this file gives **design positioning only** — it does not
> restate results, numbers, or guarantees from these papers. Read the original in the ACM DL before
> citing content. Venue policy lives in [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Pick the row whose **problem × principle** shape is nearest your project and study how the paper
passes the three-part shape test in
[`../../skills/sosp-topic-selection/SKILL.md`](../../skills/sosp-topic-selection/SKILL.md): an
extractable principle, a built system embodying it, and evidence at the claim's scale. Then apply
the self-check before declaring your own paper "SOSP-shaped." These are also the ancestry
citations [`../../skills/sosp-related-work/SKILL.md`](../../skills/sosp-related-work/SKILL.md)
expects a related-work section to know.

---

## Verified SOSP papers

### Storage at datacenter scale (relaxing POSIX for the workload you actually have)

- **Ghemawat, Gobioff & Leung, "The Google File System," SOSP 2003** (19th SOSP, Bolton
  Landing, NY, Oct 19-22, 2003; verified via dblp SOSP 2003 and the ACM DL).
  - **Why it is an exemplar:** the principle — design the file-system interface and consistency
    around observed workload properties (huge appends, component failure as the common case)
    rather than around POSIX — is stated up front and every design choice traces back to it.
  - **Self-check:** can each of your design decisions be derived from a stated workload
    assumption, and are those assumptions measured rather than asserted?

### Virtualization (an interface chosen for what it makes cheap)

- **Barham, Dragovic, Fraser, Hand, Harris, Ho, Neugebauer, Pratt & Warfield, "Xen and the Art
  of Virtualization," SOSP 2003** (same edition; SIGOPS Hall of Fame 2023, per
  `sigops.org/2023/the-hall-of-fame-award-2023/`).
  - **Why it is an exemplar:** paravirtualization is an interface argument — trade strict
    hardware fidelity for an interface guests can use efficiently — defended with a
    multi-workload evaluation against contemporaries.
  - **Self-check:** if your contribution is an interface, does the paper quantify what the
    interface change buys and name what it gives up?

### Highly available key-value storage (explicit trade-off as the contribution)

- **DeCandia, Hastorun, Jampani, Kakulapati, Lakshman, Pilchin, Sivasubramanian, Vosshall &
  Vogels, "Dynamo: Amazon's Highly Available Key-value Store," SOSP 2007** (21st SOSP,
  Stevenson, WA, Oct 14-17, 2007, pp. 205-220; verified via dblp).
  - **Why it is an exemplar:** a deployed-system paper that earns SOSP by making its trade-off
    (availability over consistency, resolved at read time) the principle, with production
    behavior as evidence — the model for industrial submissions that are more than experience
    reports.
  - **Self-check:** does your deployment paper extract a decision other builders can reuse, or
    only narrate what you built?

### Kernel correctness (proof as a systems artifact)

- **Klein, Elphinstone, Heiser, Andronick, Cock, Derrin, Elkaduwe, Engelhardt, Kolanski,
  Norrish, Sewell, Tuch & Winwood, "seL4: Formal Verification of an OS Kernel," SOSP 2009**
  (22nd SOSP, Big Sky, MT, pp. 207-220; verified via dblp).
  - **Why it is an exemplar:** demonstrates that SOSP's build-and-measure culture admits proof
    as evidence when the claim is correctness — and the paper still treats performance as a
    first-class obligation rather than an externality of verification.
  - **Self-check:** if you claim correctness, is the guarantee's boundary (assumptions,
    unverified layers) stated as carefully as the guarantee?

### Multicore OS architecture (restating the machine model)

- **Baumann, Barham, Dagand, Harris, Isaacs, Peter, Roscoe, Schüpbach & Singhania, "The
  Multikernel: A New OS Architecture for Scalable Multicore Systems," SOSP 2009** (same
  edition; verified via dblp/ACM DL).
  - **Why it is an exemplar:** the principle is a reconceptualization — treat a multicore
    machine as a distributed system, replace shared memory with message passing in the OS —
    carried by a from-scratch system rather than a patch to an existing kernel.
  - **Self-check:** does your architectural claim require the new architecture, or could the
    benefit be retrofitted (a question your evaluation must answer either way)?

---

## Problem × principle grid

| Problem | Verified SOSP exemplar | Edition | Principle shape |
| --- | --- | --- | --- |
| Datacenter storage | Ghemawat et al., "The Google File System" | SOSP 2003 | Interface follows measured workload |
| Machine virtualization | Barham et al., "Xen and the Art of Virtualization" | SOSP 2003 | Trade fidelity for an efficient interface |
| Available key-value stores | DeCandia et al., "Dynamo" | SOSP 2007 | Name the trade-off, move it to read time |
| Kernel correctness | Klein et al., "seL4" | SOSP 2009 | Proof as a measurable artifact |
| Multicore OS structure | Baumann et al., "The Multikernel" | SOSP 2009 | Re-model the machine, rebuild the OS |

The two 2003 rows also show one SOSP program hosting both an industrial-scale storage paper and
a university virtualization paper — evidence for `sosp-topic-selection`'s claim that the shape
test, not the subdomain, is the gate.

---

## Omitted after checking (do not attribute to SOSP without re-verification)

Famous systems papers that are **not** SOSP papers — the exact traps a related-work section
falls into:

- **"MapReduce" (Dean & Ghemawat)** — **OSDI 2004**, not SOSP.
- **"Bigtable" (Chang et al.)** — **OSDI 2006**, not SOSP.
- **"Spanner" (Corbett et al.)** — **OSDI 2012**, not SOSP (SIGOPS HoF 2022, which honors
  SOSP *and* OSDI papers — HoF membership is not SOSP membership).
- **"Onix" (Koponen et al.)** — **OSDI 2010** (HoF 2021); same trap.
- **"ZooKeeper" (Hunt et al.)** — **USENIX ATC 2010**, not SOSP.
- **"In Search of an Understandable Consensus Algorithm" / Raft (Ongaro & Ousterhout)** —
  **USENIX ATC 2014**, not SOSP.
- **"Large-scale cluster management at Google with Borg" (Verma et al.)** — **EuroSys 2015**,
  not SOSP.

Before adding a row, confirm the paper on `dblp.org/db/conf/sosp/` (the entry's venue line must
name SOSP and the edition), record authors, year, and pages, and update the access-date header.
When verification is unavailable, add the candidate as **待核实 / TO VERIFY** with no venue
attribution rather than guessing.
