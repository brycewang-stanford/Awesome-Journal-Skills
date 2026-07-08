---
name: focs-experiments
description: Use when deciding whether and how computation appears in a FOCS (IEEE Symposium on Foundations of Computer Science) paper — a venue that accepts on theorems with no evaluation section expected — covering machine-verified case analyses, computer-discovered constructions, and honest illustrative plots.
---

# FOCS Experiments

FOCS solicits research on the theory of computation; nothing in the 2026 CFP
asks for an evaluation, a benchmark, or an artifact (checked 2026-07-08).
Most accepted papers contain no computation at all, and a submission that
*needs* an empirical section to be persuasive is signaling that it belongs at
an algorithms-engineering venue. Yet computation does appear in strong FOCS
papers — inside proofs, behind constructions, and occasionally as a figure.
This skill scopes each mode so it helps rather than hurts.

## Referee questions, by computational mode

The useful frame is not "may I include code?" but "what will a theory referee
ask about this computation?" — because each mode triggers a different
interrogation:

| Mode | Referee's question | Your obligation |
|---|---|---|
| Case analysis inside a proof (finitely many configurations checked by program) | "If this program is wrong, is the theorem false?" | Yes → full rigor: deterministic run, published certificate, an independent checker a reader can audit |
| Search that found an object (a gadget, a code, a hard instance) later verified by hand | "Is the object's correctness independent of how it was found?" | Verify the found object analytically or by a trivially-auditable checker; describe the search in one honest sentence |
| Numerical exploration that motivated a conjecture-turned-theorem | "Does the paper claim anything based on the numerics?" | No claims may rest on it; at most a remark crediting the exploration |
| Illustrative plot of the algorithm's behavior | "Is this decoration or evidence?" | Label as illustration, disclose instance generation and seeds, make no comparative-performance claim |

The forbidden mode is the missing row: runtime comparisons against prior
implementations. That evidence form has real homes — SODA's experimental
track culture, ALENEX, ESA — and importing it into a FOCS submission invites
the committee to judge the theorems as insufficient on their own.

## Rigor pattern for a proof-bearing computation

When a lemma's truth rests on a machine check, engineer it like a proof step,
because it is one. The pattern that satisfies skeptical referees:

```makefile
# Lemma 4.7: no 3-colorable configuration of size <= 11 exists.
# The enumerator is complex; the checker is small enough to audit.
verify: configs.enum
	python3 check_lemma47.py configs.enum   # 40 lines, stdlib only
	sha256sum -c configs.enum.sha256        # pin the enumerated set
configs.enum:
	./enumerate --exhaustive --size 11 > configs.enum
```

Three properties matter: the *checker* is short and transcribes a definition
from the paper verbatim; the enumerated evidence is content-addressed so a
re-run is comparable; and the paper's proof text says precisely what the
computation certifies ("the program verifies that each of the 2,146
configurations fails condition (ii) of Definition 4.5") rather than gesturing
at "extensive computer verification". Deposit the checker and the certificate
with the public full version (`focs-artifact-evaluation`).

## Discovered objects, honestly credited

A construction found by simulated annealing, SAT solving, or an LLM-guided
search is fully legitimate at FOCS — the community judges the object, not the
finder. Honesty norms:

- Report the finder's nature truthfully; do not dress a heuristic search as
  exhaustive, and do not claim exhaustiveness you cannot certify (a
  nonexistence claim silently upgrades the computation to proof-bearing).
- If the object is small, print it in the paper; an explicit 40-entry table
  beats "available in our repository" for a reviewer deciding correctness.
- The interesting open question "why does this object exist?" can be posed as
  such — FOCS tolerates, even likes, a proof that works for reasons not yet
  structurally understood, provided the paper says so.

## Where the computation is described

Placement follows proof weight. A proof-bearing computation is described in
the proof itself — search space, what the output certifies, where the
certificate lives — because a proof with an undocumented machine step is
incomplete inside the ten-page window's promises (`focs-writing-style`). A
discovery gets one sentence at the construction's first appearance. An
illustration lives in a figure whose caption is self-sufficient. What never
works is a trailing "Implementation" section: it signals to a breadth
reviewer that the paper wants evaluation credit, and it buries proof-relevant
information where depth reviewers will not look for it.

## Plots without performance theater

An illustration is admissible when it teaches, not when it argues. A figure
showing the recursion depth of your algorithm on random instances can make an
amortization argument vivid; the guardrails are a caption that names the
instance distribution and seed, axes that start at zero or say why not, and
no baseline curves — the presence of a competitor curve converts illustration
into benchmark and triggers the missing-row problem above.

## Disclosure when the finder is an AI system

Search by LLM-guided methods is entering theory workflows, and the norms
above extend cleanly: the found object is still judged on its own
verification, and the finder is still reported honestly ("the candidate
inequality was proposed by an LLM-assisted search and verified in Lemma
5.2"). Two cautions specific to the current moment: check the live CFP for
any AI-use disclosure policy before submission (none appeared in the FOCS
2026 CFP at the 2026-07-08 check; future cycles 待核实), and never let
generated text stand in for a proof step — the verification obligations in
the table above attach to the *claim*, not to the tool that produced it.

## Decision rule

If deleting every computational element leaves the paper's claims intact, the
elements are decoration: keep only those that teach. If deleting one makes a
theorem unproved, that element is a proof step: give it proof-grade rigor. If
deleting them makes the paper unconvincing, the paper is at the wrong venue —
return to `focs-topic-selection` and route toward the algorithms-engineering
ecosystem before investing in FOCS formatting.
