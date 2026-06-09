---
name: journal-of-the-acm
description: Use when targeting the Journal of the ACM (JACM) or deciding whether a theoretical computer science manuscript fits this most-prestigious broad CS-theory venue. Encodes the journal's fit, framing, proof-and-rigor bar, house style, official-submission re-check, and desk-reject heuristics.
---

# Journal of the ACM (journal-of-the-acm)

## Journal positioning

The Journal of the ACM, published by the Association for Computing Machinery, is the most prestigious general journal in theoretical computer science. Its defining character is depth and definitiveness across the breadth of CS theory: algorithms, computational complexity, logic, data structures, distributed and parallel computation, cryptography, theory of databases and programming languages, and the theoretical foundations of systems. JACM publishes results that are not merely correct and novel but central — papers that define or settle a question, introduce a foundational model or technique, or deliver the definitive treatment of a problem. Many JACM papers are the full, complete journal versions of breakthrough conference results, with complete proofs that the conference format could not accommodate.

This skill is a **fit / venue-selection / re-framing** tool. It does not replace the journal's current official submission guidelines. Before submitting, re-check the live author instructions on the JACM site and confirm submission procedures.

## When to trigger

- The author is considering JACM for a deep, definitive theoretical computer science result.
- A breakthrough conference paper (STOC/FOCS/SODA/LICS/CRYPTO and similar) is being prepared as a complete journal version and the author wants the most prestigious general venue.
- A result is foundational or settles a central question across an area of CS theory rather than a narrow sub-problem.
- The author needs JACM's significance and rigor bar, plus common rejection reasons, before submission.

## Scope & topic fit

- Algorithms and data structures: new algorithms with strong guarantees, lower bounds, and definitive analyses.
- Computational complexity: separations, completeness results, hardness, fine-grained complexity, and structural complexity theory.
- Logic and computation: proof complexity, finite model theory, verification foundations, type theory and programming-language theory.
- Cryptography and security theory with rigorous definitions and proofs.
- Distributed, parallel, and online computation; theory of databases; foundations of machine learning when treated as theory.
- Results must be foundational or definitive and of broad interest across CS theory — narrow or incremental results, however correct, are not in scope.

## Method & evidence bar

- The primary standard is correctness and completeness: every claim must be fully and rigorously proved; conference-style proof sketches must be expanded to complete, verifiable arguments for the journal version.
- Significance is judged on centrality and definitiveness: JACM favors results that settle or fundamentally advance a question, not incremental improvements.
- Novelty of technique or model is highly valued; a new method or framework of lasting use can be as important as the headline theorem.
- Exposition must let expert referees verify correctness across potentially long and intricate arguments: precise definitions, complete proofs, and clear delineation of new versus prior contributions.
- ACM Computing Classification System (CCS) concepts should be assigned to signal scope; relationship to any prior conference version must be stated explicitly.
- arXiv (or ECCC/IACR ePrint) posting is standard practice; most submissions are publicly available before or contemporaneously with submission.

## Structure & house style

- Structure follows TCS convention: introduction (context, precise statement of results, technical overview), preliminaries and definitions, core technical sections with complete proofs, and discussion of open problems.
- The introduction must state results precisely, position them against the literature and any conference version, and give a technical overview of the key ideas accessible to a broad theory audience.
- LaTeX with the current ACM article style is standard — re-check the formatting and template requirements on the submission site.
- References must be complete and current; cite the conference version and relevant preprints with stable identifiers (arXiv/ECCC/ePrint).
- Length is set by the mathematics: complete proofs are expected even when long; unnecessary verbosity is discouraged but completeness is non-negotiable.

## Official-submission checklist

- Before giving submission-ready advice, read `../../resources/source-basis.md` and `../../resources/official-source-map.md`; start from the official source anchors for this journal family, then cite the current journal-specific page you checked.
- Check the current JACM submission instructions on the ACM site and re-verify the submission system and procedure.
- Assign ACM CCS concepts and state explicitly the relationship to any prior conference publication.
- Post to arXiv/ECCC/IACR ePrint (or confirm prior posting) with the identifier ready for correspondence.
- Prepare a cover letter stating the main result, its centrality to CS theory, the conference lineage, and suggested/excluded referees with conflicts noted.
- Confirm all co-authors have approved the submission and re-check current ACM open-access/APC options.
- If the live official instructions conflict with this skill, the official instructions win.

## Pre-submission self-check

- [ ] One sentence stating the main result and why it is central or definitive for CS theory broadly.
- [ ] Every claim is fully and rigorously proved; all conference-version sketches are expanded to complete proofs.
- [ ] The contribution is foundational or definitive, not an incremental improvement.
- [ ] The introduction states results precisely, positions them against prior work and any conference version, and overviews the techniques.
- [ ] The paper is posted on arXiv/ECCC/ePrint with CCS concepts assigned and the conference relationship stated.
- [ ] An honest assessment: is this JACM-level, or is a strong specialized theory journal or a conference venue a better fit?

## Common desk-reject triggers

- A correct but incremental result that improves a constant or extends a known technique without central significance.
- A conference paper resubmitted with proof sketches rather than complete, expanded proofs.
- A narrow result of interest only to a small sub-community, lacking broad CS-theory significance.
- An identifiable gap or unverified claim in the proofs.
- Failure to disclose or properly position a prior conference version, or an out-of-date positioning against the literature.

## Re-routing decision

Primary machine-learning research with a theory component → `journal-of-machine-learning-research`. Fast-moving CS results where conference publication is the field norm → the appropriate top conference (STOC, FOCS, SODA, LICS, CRYPTO, etc.). Strong but specialized theory results → an area-specific theory journal (SICOMP, ACM Transactions, etc.). Deep mathematical content beyond CS theory → `advances-in-mathematics`.

## Output format

```text
[Fit] High / Medium / Low (one-line reason)
[Target] Journal of the ACM
[Topic tags] <2–3 CS-theory areas (CCS)>
[Method/evidence] <are all results fully proved (complete, not conference sketches), central/definitive, and broadly significant?>
[Top risk] <the single most likely reason for rejection — usually significance or incomplete proofs>
[Official items to re-check] <submission procedure / CCS concepts / preprint posting / conference-version disclosure / ACM style>
[Re-route suggestion] <if not a fit, a better-matched venue>
```
