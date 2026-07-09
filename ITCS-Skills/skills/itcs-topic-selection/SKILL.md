---
name: itcs-topic-selection
description: Use when deciding whether a theoretical-computer-science result belongs at ITCS or should be routed to STOC, FOCS, SODA, CCC, ICALP, TCC, or a journal, and when distinguishing ITCS from its depth-first siblings by the conceptual-novelty test — is this a new question, model, or connection worth asking, rather than the deepest theorem of the year.
---

# ITCS Topic Selection

Decide the venue before drafting, and decide it on the axis ITCS actually selects on. ITCS — the
**Innovations in Theoretical Computer Science** conference — was founded (as *Innovations in
Computer Science*, 2010) to reward **conceptual novelty**: a new model, a new question, a
surprising connection, a direction the field had not thought to take. Its sibling flagships STOC
and FOCS reward the **deepest, most polished** result on questions the field already agrees are
hard. A technically strong paper whose real virtue is that it *finally proves a known hard
theorem* is respected and then, often, routed away from ITCS as "not innovative enough" — while a
bold, imperfect, genuinely new idea can be accepted here that STOC/FOCS would reject for want of
depth.

## The routing question that matters most

For most theory papers the decisive question is not "is this good theory?" but **"does this paper
give the community a new *idea*, or a stronger *result* on an existing idea?"**

- If a reader's main takeaway is *"I hadn't thought to ask that / model it that way / connect
  those two areas"* — that is an ITCS signal.
- If the main takeaway is *"they finally proved / improved / tightened X"* — that is a
  STOC/FOCS/SODA signal, however elegant.

Both are valuable; ITCS is simply the venue whose PC is briefed to weight the first over the
second. When your paper has both a new idea *and* deep technical results, you have a genuine
choice, and the calendar and community fit break the tie.

## Sibling-venue routing table

| Signal in your project | Better home | Why |
|---|---|---|
| A **new model, definition, question, or connection** with a first result showing it is alive | **ITCS** | The conceptual-novelty venue; "innovation" is the selection criterion, not a bonus |
| The **deepest/tightest theorem of the year** on an established question | **STOC / FOCS** | Depth-first general theory flagships; polish and difficulty are rewarded |
| A **new or improved algorithm / data structure**, discrete-algorithms flavor | **SODA** | Algorithms-centered; the ACM-SIAM discrete-algorithms community |
| A **complexity** result centered on classes, lower bounds, circuit/proof complexity | **CCC** | Computational Complexity Conference; specialist depth |
| A broad EATCS-scope algorithms/automata/logic result, single September-ish cycle | **ICALP** | Track A/B breadth; European TCS flagship |
| A **cryptography** result with a formal model and reductions | **TCC / CRYPTO / Eurocrypt** | Crypto-specialist venues; TCC especially for foundational crypto |
| A result too long, too incremental-over-your-own-prior, or needing full journal treatment | **A journal (JACM/SICOMP/ToC/...)** | No conference deadline or page pressure; simultaneous journal submission is even allowed alongside ITCS |

## Conceptual shapes ITCS rewards

- **A new model or definition** — you hand the community an object it did not have (the
  non-malleable-codes lineage). The definition *is* the contribution.
- **A new algorithmic or complexity notion** — a fresh way to say what "solving" means (the
  pseudodeterministic lineage), reorganizing questions people already cared about.
- **A surprising connection** — tools from area X attack a problem in area Y that neither had
  linked (the "quantum money from knots" lineage).
- **A new question at a seam** — a problem two mature areas could have posed together but never
  did (interactive proofs meet learning; verification meets distributed networks).
- **A conceptual reframing or "manifesto-with-teeth"** — a position that changes what questions
  look worth asking, *backed by at least one theorem* so it is not a mere opinion.

## The three ITCS acceptance tests

Sharpen a borderline verdict with three quick tests the PC will apply:

- **New-question test:** after the abstract, does a reader think *"I want to work on that"* about
  a question they had not previously posed? If the reaction is instead *"impressive that they
  proved it,"* the paper is depth-shaped -> STOC/FOCS.
- **Not-empty-not-everything test:** a new model is only interesting if it is neither trivial nor
  all-powerful. Do you have at least one crisp result (a separation, a surprising possibility, an
  impossibility) proving the model is alive? Without it, ITCS reads the paper as a definition in
  search of a result.
- **Survives-the-improvement test:** if someone later proves a *far* stronger theorem inside your
  model, does your *framing* still get credit? If yes, the idea is the contribution (ITCS). If
  your paper's whole value is the current bound, route to a depth venue where the bound is the
  point.

## Evidence maturity, ITCS-style

Fit is necessary but not sufficient — but note ITCS's maturity ladder runs *opposite* to an
empirical venue's. A **preliminary, incomplete, bold** exploration of a genuinely new model is
*more* ITCS-appropriate than a fully mopped-up version whose novelty has worn off. What ITCS will
not accept is a new-model paper with **no result at all** (a definition with nothing proved) or a
"new" question that is actually a known question in disguise. The failure mode here is not "too
early" (as at STOC) but "not actually new" — do the related-work delta honestly first (see
[`itcs-related-work`](../itcs-related-work/SKILL.md)).

## Cheap reconnaissance before committing

```text
[Novelty]  can you state your contribution as a NEW noun (a model, a notion, a connection)?
           -> yes, and it's checkably new in the literature = ITCS-shaped
           -> it's a better bound/algorithm on an existing noun = STOC/FOCS/SODA
[Scope]    scan the last 2-3 ITCS programs (dblp conf/innovations, LIPIcs) for kindred papers
           -> a cluster of "new model" papers in your area = a reviewer pool exists
[Calendar] ITCS has ONE deadline, early September, notification November, conference January.
           Missed it? the next depth-venue deadline may beat waiting a year for ITCS.
```

## Decision procedure

```text
[Takeaway] is the reader's takeaway a new IDEA or a stronger RESULT?
[Shape]    model / notion / connection / seam-question / reframing -> ITCS lane
[Alive]    do you have >=1 crisp result showing the model is not empty and not everything?
[Sibling]  depth on a known question -> STOC/FOCS; algorithms -> SODA; complexity -> CCC;
           crypto model -> TCC; too long/incremental -> journal (journal submission is
           even allowed simultaneously with ITCS)
[Verdict]  ITCS / sibling venue / journal, with a one-line reason naming the new noun
```

Run this before the writing skills; a wrong venue decision wastes every later step. When the
verdict is ITCS, continue with [`itcs-workflow`](../itcs-workflow/SKILL.md) for the single-cycle
calendar and [`itcs-writing-style`](../itcs-writing-style/SKILL.md) for the innovation-first
paper shape.
