---
name: sigir-related-work
description: Use when positioning a paper against the information-retrieval literature for SIGIR — tracing lineage through SIGIR/TOIS/TREC canon, contrasting mechanisms with the nearest recent SIGIR papers, avoiding venue misattribution (DPR is EMNLP, ANCE is ICLR, NCF is WWW), and handling arXiv-era concurrent work in a fast-moving field.
---

# SIGIR Related Work

At SIGIR, related work is a credibility exam graded by reviewers who may have
written the papers you cite. IR is an old field with a living canon: a related-work
section that starts retrieval history at BERT signals a visitor from an adjacent
community, which primes every other judgment. This skill builds positioning that
demonstrates lineage fluency and states the delta mechanically.

## The lineage obligation

An IR paper is expected to know which research line it extends and to cite the
line's origin plus its current SIGIR-era frontier. The canonical lines and their
anchors (all venue-verified — see `../../resources/exemplars/library.md`):

| Line | Origin anchor | What your delta sentence must contrast |
|---|---|---|
| Probabilistic/lexical ranking | Robertson-era BM25 work; Ponte & Croft's language-modeling approach (SIGIR 1998) | Which term-weighting/estimation assumption you change |
| LM smoothing & estimation | Zhai & Lafferty (SIGIR 2001) | Estimation method, prior, or evidence source |
| Graded evaluation | Järvelin & Kekäläinen (SIGIR 2000; nDCG lineage) | Which validity gap your metric/protocol closes |
| Neural re-ranking / late interaction | ColBERT (SIGIR 2020) | Interaction granularity, storage, or supervision |
| Graph collaborative filtering | NGCF (SIGIR 2019), LightGCN (SIGIR 2020) | Propagation structure or training signal |

You do not cite all lines — you identify *yours* and prove you know both ends of it.

## Venue misattribution: the IR-specific trap

Retrieval's most-cited recent papers are scattered across NLP and ML venues, and
misattributing them is a reviewer's one-glance credibility test:

- **DPR** (dense passage retrieval): EMNLP 2020, not SIGIR.
- **ANCE**: ICLR 2021, not SIGIR.
- **Neural Collaborative Filtering**: WWW 2017, not SIGIR (its graph successors
  NGCF/LightGCN *are* SIGIR).
- **RankNet**: ICML 2005. **BERT** itself: NAACL 2019.
- **BM25's** standard citations are TREC/SIGIR-era Robertson et al. papers, not "the
  Anserini paper"; cite the toolkit separately when you mean the implementation.
- Järvelin & Kekäläinen's *"Cumulated gain-based evaluation"* is **TOIS 2002** — the
  SIGIR 2000 paper is the earlier "highly relevant documents" one; the pair is the
  classic conference-then-journal split, and conflating them is common and noticed.

```bash
# Bibliography audit: flag entries whose venue field is suspiciously vague
grep -nE "booktitle.*(arXiv|CoRR|preprint)" refs.bib      # published since?
grep -nE "@misc|howpublished" refs.bib                     # citing repos as papers?
grep -in "sigir" refs.bib | wc -l                          # lineage presence check
```

## The delta sentence, mechanized

For each of the 3-5 nearest neighbors (not the 30 nearest keywords), write one
sentence with three fixed slots: *what it does* (mechanism, not adjective), *what we
do differently* (mechanism again), *what that buys* (measured, or honestly "which we
test in §5"). Neighbors are papers a reviewer would confuse with yours — the correct
list usually includes at least one paper from the last two SIGIR volumes, one from a
sibling venue (ECIR/CIKM/WSDM/WWW/RecSys), and one journal or TREC-track antecedent
that pre-dates the neural era. Missing that third slot is how "novel" claims collide
with 2009.

## Concurrent and arXiv-era work

IR moves at preprint speed while SIGIR reviews at conference speed:

- Sweep arXiv (cs.IR) and the latest SIGIR/ECIR/CIKM accepted-paper lists in the
  final week before submission; add a "concurrent work" note for anything published
  after your experiments froze. Reviewers respect the note and punish the silence.
- Cite preprints as preprints; when a preprint you rely on has since been published,
  cite the published version — mixed-provenance bibliographies age badly in the
  version of record.
- Anonymity interaction: discussing your own preprint must stay third-person and
  must not make the identification trivial (see `sigir-submission`).

## Positioning failures that cost accepts

- **The adjacent-community rewrite**: framing a retrieval problem entirely in LLM/
  agent vocabulary with no IR literature — reviewers read it as "wrong venue."
- **The strawman baseline lineage**: citing only pre-neural or untuned versions of
  the line you claim to beat.
- **The enumeration**: three paragraphs of "X did A. Y did B." with no contrast
  work — spends budget without answering "so what is new?"
- **The self-citation cluster**: heavy self-lineage both risks anonymity and reads
  as insularity; balance against external anchors.
- **TREC blindness**: proposing an evaluation methodology or task without checking
  whether a TREC/NTCIR/CLEF track already operationalized it.

## The reviewer-eye test

Before freezing the section, simulate the three reads it will get:

- **The 30-second AC skim**: do the paragraph topic sentences alone convey "line
  identified, frontier known, delta stated"? If the deltas hide mid-paragraph,
  surface them.
- **The competitor's read**: the author of your nearest neighbor may be R2. Is their
  paper described accurately enough that they nod before you pivot to the
  difference? Misdescribing a rival's mechanism converts a fixable delta dispute
  into hostile review.
- **The veteran's read**: is there any sentence a 20-year IR researcher would mark
  "we knew this in the 2000s"? Pre-neural antecedents cited *by you* defuse what
  they discover *for* you.

## Placement under the 9-page budget

Related work earns ~0.75 page in a full paper. Two structures work: after the intro
(when positioning *is* the motivation) or before the conclusion (when the method
needs no prior-work vocabulary). In short papers, related work compresses into the
introduction as positioning sentences with dense citations — a standalone section is
usually a page-budget error.

## Output format

```text
[Line identified] <which research line, origin + frontier cited y/n>
[Neighbor set] <3-5 papers with mechanism-contrast sentences present y/n>
[Misattribution scan] venues checked against exemplar library: violations <list>
[Era coverage] pre-neural antecedent / recent SIGIR volume / sibling venue: present each
[Concurrent-work note] needed y/n, drafted y/n
[Budget] <fraction of page used> and placement choice
```
