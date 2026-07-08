---
name: sigmod-writing-style
description: Use when revising a SIGMOD research paper's prose and structure, covering the data-management framing readers expect on page one, running examples and architecture figures, scoping systems claims to measured workloads, third-person anonymity phrasing, and fitting a systems argument into 12 ACM-template pages.
---

# SIGMOD Writing Style

SIGMOD prose is engineering argumentation: a reader who builds database
systems should finish page one knowing what breaks today, what mechanism you
built, and what measurement proves it. The 12-page ACM-template budget
(references excluded) is generous by conference standards, which removes the
usual excuse — at this venue, missing detail reads as concealment rather
than compression.

## Page-one contract

Within the first page, in some order: the workload or application pressure
that makes the problem real *now*; why the incumbent technique fails at that
pressure point (with a number if possible); the mechanism in one concrete
sentence; the headline measured result with its setting attached; and the
contribution list phrased as artifacts a reader can verify — an algorithm, a
system component, a proof, an evaluation.

A first paragraph that opens with "Data volumes are growing exponentially"
has already spent its welcome; open instead inside the specific bottleneck.

## The running example

The single most recognizable SIGMOD stylistic device: one small, concrete
example — a table, a query, a workload snippet — introduced in Section 1 or 2
and threaded through the design sections. Every operator, data structure, or
protocol step is shown acting on it. Papers that explain a join algorithm
purely in symbols, when three rows and two tables would show it, get "hard to
follow" reviews from people fully capable of reading the symbols.

## Claim scoping for systems numbers

| Draft claim | Survives review as |
|---|---|
| "Up to 10x faster than X" | "10x on skewed reads at sf=100; 1.3x on uniform writes (Fig 8)" |
| "Scales linearly" | "Near-linear to 64 cores; contention flattens beyond (Fig 9)" |
| "Negligible overhead" | "3-6% p99 latency overhead across the mixes tested (Tab 4)" |
| "Guarantees consistency" | "Snapshot isolation; serializable with Sec 4.3's lock, at cost Y" |
| "First system to..." | Scoped precisely, or cut — a PC full of builders will find prior art |

The pattern: attach every superlative to a figure, a workload, and a
boundary. Database reviewers respect a stated limitation and hunt an
unstated one.

## Architecture before algebra

- One system-overview figure early, with components named identically in
  figure, prose, and evaluation — nomenclature drift across 12 pages is a
  real and common defect.
- Pseudocode for the core mechanism only; secondary routines are prose plus
  a pointer to the artifact.
- Correctness arguments get a proof sketch in the body and full detail in
  the extended report (`sigmod-supplementary`), but the invariant itself
  must be stated in the body, precisely.
- Design-decision paragraphs ("we chose B over A because...") are not
  filler here; they are what industrial readers cite the paper for.

## Anonymity-safe voice

Write about your own prior systems in the third person, and scrub the tells:
"we extend the engine of [12]" not "we extend our engine [12]"; no
internal codenames that a search engine maps to a company; no "deployed at a
major cloud provider" phrasing that narrows the author set to two teams.
These rules bind for the entire multi-round review, including revised text.

## Budgeting the 12 pages

```text
p1      Problem, failure of incumbents, mechanism, headline number
p2-3    Background + running example; the example does the teaching
p4-7    Design: architecture figure, core algorithm, invariants
p8      Correctness/complexity sketch; report carries the full proof
p9-11   Evaluation: setup table first, then claims in figure order
p12     Related work in contrast form + limitations + conclusion
```

Treat the evaluation-setup half page as immovable: hardware, datasets,
workloads, baselines, tuning provenance. Cutting it to rescue a design
subsection trades a clarity comment for an evidence objection — a bad trade
in this reviewer pool.

## Title and abstract mechanics

- System papers at this venue conventionally lead with the system name and
  a colon-scoped promise ("X: <mechanism> for <setting>"); earn the name by
  making the mechanism clause precise, not grand.
- The abstract must contain at least one number with its setting attached;
  an abstract with zero measurements signals a position paper.
- Avoid "novel," "framework," and "holistic" — three words this reviewer
  pool has learned to read as absence of specifics.
- The abstract's last sentence should say what is released: code, data,
  scripts. PACMMOD's sharing expectation makes silence conspicuous.

## Sentence-level habits

- Present tense for the system's behavior, past tense for what experiments
  did.
- Numbers over intensifiers: "2.1x" not "significantly"; "p99" not "tail".
- Name the enemy precisely: "log-structured merge amplification" beats
  "performance issues of existing approaches".

## Output format

```text
[Page-one audit] pressure / incumbent failure / mechanism / number present?
[Running example] exists and threads through design sections yes/no
[Claim ledger] each superlative -> figure + workload + boundary
[Voice sweep] third-person self-references, codename leaks
[Budget check] section allocation vs. the 12-page plan
[Priority rewrites] ordered list
```
