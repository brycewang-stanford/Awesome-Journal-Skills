---
name: pldi-related-work
description: Use when positioning a PLDI paper against the SIGPLAN family and systems neighbors — stating technical deltas per cited line, covering the last few PLDI/POPL/OOPSLA/ICFP cycles, citing PACMPL-era papers in journal form, and verifying every venue attribution on dblp before it ships.
---

# PLDI Related Work

At PLDI, related work is an adversarial exercise: your reviewers are frequently
the authors of your closest baselines. The section must therefore do two things —
prove you know the landscape's *mechanisms* (not just its citations), and state,
line by line, what this paper does that each prior technique cannot.

## The delta discipline

Ban survey sentences ("Much work has studied pointer analysis [3,7,12,19]").
Every citation earns its place with a mechanism and a delta:

> Steensgaard-style unification [7] scales linearly but merges all callees'
> effects; our signatures keep callee effects separate at equal asymptotic cost
> (§4.3).

If you cannot write the delta clause, you have not read the paper closely enough
to cite it at PLDI — where the cited author may be reviewer B.

## Coverage map

| Neighbor | What to check there | Typical relationship to a PLDI paper |
|---|---|---|
| PLDI, last ~4 cycles | The direct competition; reviewers expect these compared, not just cited | Baseline or head-to-head |
| POPL | The semantic foundations your system builds on | "We implement/scale what [x] formalized" |
| OOPSLA | Language design, empirical SE-flavored PL studies | Alternative evidence styles for similar claims |
| ICFP | Functional-language techniques, typed IRs | Technique transfer across paradigms |
| ASPLOS / CGO / PPoPP | Architecture-facing compilation and parallelism | Same optimization, different evidence bar |
| CAV / TACAS | Verification engines and solvers | Your backend or your competitor's |
| ICSE / FSE | Testing and analysis at software-engineering scale | Scale claims to compare honestly |

Since POPL, OOPSLA, ICFP, and PLDI all publish in PACMPL, "recent PACMPL papers"
is a single searchable stream — sweep it by issue name so a POPL 2025 article
does not get labeled PLDI 2025 in your bibliography.

## Cite the PACMPL era correctly

PLDI 2023 and later papers are journal articles, not proceedings entries:

```bibtex
@article{gopinathan2023proofrepair,
  author  = {Gopinathan, Kiran and Keoliya, Mayank and Sergey, Ilya},
  title   = {Mostly Automated Proof Repair for Verified Libraries},
  journal = {Proc. ACM Program. Lang.},
  volume  = {7},
  number  = {PLDI},
  articleno = {107},
  year    = {2023},
  doi     = {10.1145/3591221}
}
```

Pre-2023 PLDI papers keep `@inproceedings` form with page ranges. Mixing the two
conventions — or citing a PACMPL article as "In PLDI '23, pp. ..." — is the most
common bibliography error since the switch, and PL reviewers notice.

## Verification before submission

- Confirm every venue attribution on dblp; the classics are the traps (LLVM is
  CGO 2004, CompCert's certification paper is POPL 2006, RustBelt is PACMPL
  Issue **POPL** — see `resources/exemplars/library.md` for the curated list).
- For arXiv-only concurrent work, cite it as a preprint and position gently;
  it is context, not an archival obligation.
- Double-blind interacts here: your own prior papers appear in third person,
  cited normally — omitting them is itself an identity signal.

## Output format

```text
[Delta audit] citations without a delta clause: <list>
[Coverage] PLDI recent cycles / POPL / OOPSLA / ICFP / systems neighbors — gaps?
[Head-to-head] which cited techniques appear in the evaluation as baselines?
[Bibliography form] PACMPL-era entries in journal form? venues dblp-verified?
[Anonymity] self-citations third person, none omitted?
```
