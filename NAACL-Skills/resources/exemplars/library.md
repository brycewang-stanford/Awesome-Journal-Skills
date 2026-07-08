# NAACL Exemplars Library (topic × method)

> **Verified via web search, access date 2026-07-08.** Every entry below was
> checked against the **ACL Anthology** — the `N??-` or `20??.naacl-` volume
> identifier, author list, page range, and host city — to confirm it appeared
> at a **NAACL** edition specifically, not at a sibling *ACL venue. Entries
> that could not be cleanly confirmed were moved to the omissions section with
> the reason. Short and verified beats long and guessed.
>
> **Sibling-confusion guard.** The *ACL family shares reviewers, templates,
> and citation styles, so venue misattribution is rampant in secondhand
> sources. An Anthology ID is the arbiter: `N13-…`/`N19-…` and
> `2022.naacl-…`/`2024.naacl-…` are NAACL; `P…`/`20??.acl-…` are ACL;
> `D…`/`20??.emnlp-…` are EMNLP. Check the ID, not the citation you inherited.
>
> **Use principle.** This file positions papers; it does not restate their
> numbers. Read the original on the Anthology before citing any result. For
> policy and calendar facts see [`../official-source-map.md`](../official-source-map.md).

---

## How to use this library

Each exemplar earns its row by illustrating one move the NAACL skills teach —
a first page that scopes its claim, an evaluation designed around a
phenomenon, or an analysis of who produced the data. Find the row nearest
your project's topic × method, read how that paper executes the move, then
run the paired skill against your own draft.

## Verified exemplars

### Pretraining as an NLP contribution (representation learning)

- **Devlin, Chang, Lee & Toutanova, "BERT: Pre-training of Deep Bidirectional
  Transformers for Language Understanding," NAACL 2019, Minneapolis,
  pp. 4171-4186.** Verified: `aclanthology.org/N19-1423/`.
  - **The move to study:** a pretraining-objective idea argued through breadth
    of downstream evidence — the claim's scope (English benchmarks of its
    era) matches the tables exactly. Pair with
    [`naacl-experiments`](../../skills/naacl-experiments/SKILL.md).

### Contextual representations (feature-based transfer)

- **Peters, Neumann, Iyyer, Gardner, Clark, Lee & Zettlemoyer, "Deep
  Contextualized Word Representations," NAACL 2018, New Orleans,
  pp. 2227-2237.** Verified: `aclanthology.org/N18-1202/`.
  - **The move to study:** an analysis section that shows *what* the learned
    layers capture, not just that scores rise — the mechanism probe answered
    in advance. Pair with [`naacl-review-process`](../../skills/naacl-review-process/SKILL.md).

### Distributional semantics (embedding analysis)

- **Mikolov, Yih & Zweig, "Linguistic Regularities in Continuous Space Word
  Representations," NAACL 2013, Atlanta, pp. 746-751.** Verified:
  `aclanthology.org/N13-1090/`.
  - **The move to study:** a short paper doing one thing — the analogy
    regularity — with a clean test and no scope inflation; the model of the
    4-page genre. Pair with [`naacl-writing-style`](../../skills/naacl-writing-style/SKILL.md).

### Document modeling (architecture + attention analysis)

- **Yang, Yang, Dyer, He, Smola & Hovy, "Hierarchical Attention Networks for
  Document Classification," NAACL 2016, San Diego, pp. 1480-1489.**
  Verified: `aclanthology.org/N16-1174/`.
  - **The move to study:** the architecture mirrors a linguistic structure
    (words → sentences → document) and the visualizations argue that the
    structure, not just capacity, drives gains. Pair with
    [`naacl-related-work`](../../skills/naacl-related-work/SKILL.md).

### Annotation and data ethics (human-label analysis)

- **Sap, Swayamdipta, Vianna, Zhou, Choi & Smith, "Annotators with Attitudes:
  How Annotator Beliefs And Identities Bias Toxic Language Detection,"
  NAACL 2022, Seattle, pp. 5884-5906.** Verified:
  `aclanthology.org/2022.naacl-main.431/`.
  - **The move to study:** treats the annotator population as an object of
    study — exactly the who-labeled-this scrutiny the checklist era expects
    every dataset paper to survive. Pair with
    [`naacl-artifact-evaluation`](../../skills/naacl-artifact-evaluation/SKILL.md).

## Topic × method index

| Topic | Exemplar | Anthology ID | Method lane |
| --- | --- | --- | --- |
| Pretraining / transfer | Devlin et al. 2019 | N19-1423 | Masked-LM pretraining |
| Contextual embeddings | Peters et al. 2018 | N18-1202 | BiLSTM features + layer analysis |
| Embedding regularities | Mikolov et al. 2013 | N13-1090 | Vector-offset analogy tests |
| Document classification | Yang et al. 2016 | N16-1174 | Hierarchical attention |
| Annotation bias | Sap et al. 2022 | 2022.naacl-main.431 | Annotator-identity analysis |

## Omitted after checking (do not attribute to NAACL)

- **word2vec** ("Efficient Estimation of Word Representations…", Mikolov et
  al. 2013) — an **ICLR 2013 workshop** paper, not NAACL; only the
  *Linguistic Regularities* paper above is the NAACL one. The two are
  conflated constantly.
- **GloVe** (Pennington et al. 2014) — **EMNLP 2014**, not NAACL.
- **"Attention Is All You Need"** (Vaswani et al. 2017) — **NeurIPS**, cited
  into *ACL papers so often that its venue gets misremembered.
- **AmericasNLI** (Ebrahimi et al.) — despite the Americas theme fit,
  verified as **ACL 2022**, not NAACL; a reminder that topical fit proves
  nothing about venue.
- **"Teaching Language Models to Self-Improve through Interactive
  Demonstrations"** (Yu group) — reported as a **NAACL 2024 best paper** by
  the conference's own channels, but the exact Anthology ID was not pinned
  by the access date: 待核实 before citing volume/pages.

To add a row: confirm the Anthology ID renders under a NAACL volume, record
authors/pages/host city, cite the `aclanthology.org` URL, and update the
access date in the header. Unverifiable candidates go under omissions, never
into the table.
