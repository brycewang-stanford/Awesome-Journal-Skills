---
name: uist-related-work
description: Use when positioning a UIST submission against prior art — organizing by capability delta rather than paper lists, covering the technique lineage, toolkit ancestry, and commercial systems reviewers know, citing your own work in the third person, and verifying venue attribution through the ACM DL and dblp.
---

# UIST Related Work

At UIST, related work is a **novelty proof**, not a literature survey. The section
exists to establish that no prior system delivers your capability, and its jury
includes people who built the prior systems. Precision about what neighbors can and
cannot do is therefore worth more than coverage breadth — and misdescribing a
reviewer's own system is the fastest way to earn a hostile expert review.

## Organize by capability, not by paper

Structure subsections around the dimensions on which your artifact differs, and end
each with an explicit delta sentence:

```text
WEAK:  "Several systems have explored on-skin input [4,9,12]. Others used
       acoustic sensing [7,15]. We also use acoustic sensing."
STRONG: "Prior on-skin input systems localize touches on the forearm [4,9] or
       hand [12], but all require instrumentation of the touching finger.
       Acoustic approaches remove finger instrumentation [7,15] yet resolve
       only 4-6 discrete locations. Our contribution is continuous 2D
       localization with no finger instrumentation."
```

A comparison table (rows: closest systems; columns: the 3-5 capability dimensions)
is often the strongest half-page in the paper — but every cell about someone else's
system must be defensible from their paper's text.

## The three lineages to cover

| Lineage | What reviewers check | Where authors slip |
|---|---|---|
| Technique lineage | The chain of prior techniques for the same user intent, across decades | Citing only the last 5 years; UIST's canon runs to the early 1990s |
| Toolkit/platform ancestry | Which abstractions you inherit vs invent | Claiming novelty for what a mature toolkit already provides |
| Commercial and open-source practice | Shipping products that already do a version of it | Ignoring the product every reviewer owns |

Commercial systems lack papers but not existence: cite documentation or teardowns and
state the capability difference plainly. "No academic paper describes X" is not a
novelty claim when X ships on a phone.

## Where to search, and how to verify

- Sweep the **UIST main proceedings** first, then the **adjunct proceedings** —
  demos and posters establish prior art too, and a 2-page poster that showed your
  idea must be cited and differentiated, not hidden.
- Continue through the sibling venues in both directions: CHI, TEI, IMWUT, ISMAR,
  IUI, SUI, CSCW — UIST reviewers move through the same circuit.
- Verify every venue attribution against the ACM DL record or dblp before the
  camera-ready; "CHI 2019" citations that were actually UIST 2019 (or an adjunct
  demo, or an arXiv preprint) are noticed at this venue in particular.
- For canonical anchors, the Lasting Impact lineage in
  [`../../resources/exemplars/library.md`](../../resources/exemplars/library.md)
  is verified against DL/dblp records; follow the same recipe for anything you add.

## Building the comparison table without libel

The capability-comparison table is high-value and high-risk. A defensible build
procedure:

1. Choose dimensions from **your claims**, not from your strengths — a table whose
   columns are exactly where you win reads as rigged, and reviewers discount it.
2. Fill each competitor cell **from their paper's own text**, with the section
   number kept in your notes; "not reported" is a legitimate cell value and more
   honest than an inferred "no."
3. Include at least one dimension where a **prior system beats yours** (maturity,
   cost, resolution); the table gains credibility exactly there.
4. Re-check cells against later versions — a 2019 system may have gained the
   capability in its authors' 2023 follow-up, and those authors review at UIST.

```text
Table skeleton (rows = closest systems, cols = capability dimensions):
            | finger-free | continuous 2D | on unmodified skin | latency reported
SystemA '19 |     no      |  4 sites      |       yes          |  not reported
SystemB '22 |     yes     |  1D slider    |       no (sleeve)  |  23 ms
Ours        |     yes     |  yes ±2.1 mm  |       yes          |  11 ms median
```

## Anonymization interacts with self-citation

UIST's 2026 rules (verified 2026-07-08) are specific and unusual in one respect:

- Cite your own prior work **in the third person with a full, non-redacted
  reference** — do not write "[anonymized for review]", which both leaks that the
  cited work is yours and breaks the reviewer's ability to check the delta.
- If a prior submission of yours **overlaps heavily** with this one, attach an
  anonymized copy of it as supplementary material so reviewers can judge the overlap
  themselves.
- The delta over your own prior system gets the same explicit treatment as anyone
  else's — self-succession without a stated capability difference reads as
  salami-slicing.

## Timing note for the live cycle

Reviews for UIST 2026 papers are in (notification June 27, 2026). If you are
repositioning after rejection, mine the reviews for missed prior art before choosing
the next venue: an expert pointing at a system you did not cite is the cheapest
related-work audit you will ever get. For camera-ready papers, the +10% page
allowance is often best spent making the comparison table honest about points the
rebuttal conceded (see `uist-camera-ready`).

## Output format

```text
[Novelty frame] <the capability delta in one sentence>
[Nearest neighbors] <3-5 systems + the dimension separating each>
[Lineage gaps] technique / toolkit / commercial — which is thin
[Attribution check] verified via DL-dblp / pending
[Self-citation risk] third-person compliant / overlap attachment needed / clean
```
