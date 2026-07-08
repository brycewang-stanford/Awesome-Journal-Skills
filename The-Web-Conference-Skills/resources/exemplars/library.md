# Web Conference Exemplars Library (topic × contribution type)

> **Verified via web search on 2026-07-08.** Each paper below was confirmed against
> ACM Digital Library records, dblp, or the WWW proceedings themselves as having
> appeared at an **International World Wide Web Conference / The Web Conference**
> edition — matching title, authors, edition, and (where retrievable) DOI or page
> range. The list is deliberately short and verified rather than long and guessed.
>
> **Sibling-confusion guard:** the WWW reviewer pool overlaps with WSDM, SIGIR,
> KDD, CIKM, and ICWSM, and many "web" classics live at those venues, not here.
> A famous recommendation or graph paper is *not* a WWW paper until its proceedings
> entry says so. See the omissions section for the traps checked and avoided.
>
> **Zero-hallucination rule:** rows give *positioning* only — why the paper is
> shaped like a Web Conference paper. No result numbers, no table values. Read the
> original in the ACM DL before citing anything quantitative.

---

## How to use this library

Find the row nearest your topic × contribution type, then study how that paper
passes the two tests this pack drills: the **web-native mechanism on page one**
(`../../skills/webconf-writing-style/SKILL.md`) and **evidence scaled to the claim**
(`../../skills/webconf-experiments/SKILL.md`). Each row ends with the self-check
question to ask of your own draft.

## Verified exemplars

### Network embedding for web-scale graphs (algorithm)

- **Tang, Qu, Wang, Zhang, Yan & Mei, "LINE: Large-scale Information Network
  Embedding," WWW 2015 (24th, Florence), pp. 1067-1077.**
  - **Why it exemplifies the venue:** the contribution is explicitly scoped to
    *information networks as they occur on the web* — directed, weighted, and at
    sizes where prior embedding objectives were infeasible — so scale is a design
    constraint, not an evaluation garnish.
  - **Self-check:** is your method's web-scale claim built into the objective and
    complexity analysis, or only into the size of one test graph?

### Neural recommendation (algorithm, user modeling track lineage)

- **He, Liao, Zhang, Nie, Hu & Chua, "Neural Collaborative Filtering," WWW 2017
  (26th, Perth), pp. 173-182, DOI 10.1145/3038912.3052569.**
  - **Why it exemplifies the venue:** replaces a specific mechanism (the inner
    product in matrix factorization) with a learned interaction function and argues
    the change where web platforms feel it — implicit feedback at scale. A model of
    the mechanism-first framing `webconf-writing-style` teaches.
  - **Self-check:** can you name the single mechanism you replace and show the
    ablation row that isolates it?

### Probabilistic models for implicit feedback (algorithm + analysis)

- **Liang, Krishnan, Hoffman & Jebara, "Variational Autoencoders for Collaborative
  Filtering," WWW 2018 (Lyon), DOI 10.1145/3178876.3186150.**
  - **Why it exemplifies the venue:** imports a general ML tool (VAEs) but earns
    the web venue by adapting the likelihood (multinomial) to the actual shape of
    web interaction data and analyzing why that choice matters — adaptation with
    reasons, not decoration.
  - **Self-check:** if your paper imports an ML method, what about *web data
    specifically* forced a nontrivial adaptation?

### Heterogeneous graph learning (algorithm)

- **Wang, Ji, Shi, Wang, Ye, Cui & Yu, "Heterogeneous Graph Attention Network,"
  WWW 2019 (San Francisco), pp. 2022-2032.**
  - **Why it exemplifies the venue:** the heterogeneity it models (typed nodes and
    meta-paths) is the defining property of real web graphs; node-level and
    semantic-level attention map one-to-one onto claims, giving reviewers a clean
    claim→ablation contract.
  - **Self-check:** does each architectural component correspond to a stated
    property of web data, with an ablation per component?

### Platform-scale social measurement (measurement/empirical)

- **Kwak, Lee, Park & Moon, "What is Twitter, a Social Network or a News Media?,"
  WWW 2010 (Raleigh), pp. 591-600.**
  - **Why it exemplifies the venue:** a census-scale crawl (the entire platform at
    the time) put to a *conceptual* question, with the sampling frame stated and
    the construct ("social network vs. news media") operationalized in measurable
    graph and diffusion terms — the measurement-track template.
  - **Self-check:** is your sampling frame explicit, and is the headline concept
    operationalized so a skeptic could re-measure it?

## By topic × contribution type

| Topic | Exemplar | Edition / location | Type |
| --- | --- | --- | --- |
| Web-scale graph embedding | Tang et al., LINE | 2015 / Florence | Algorithm |
| Neural recommendation | He et al., NCF | 2017 / Perth | Algorithm |
| Implicit-feedback modeling | Liang et al., VAE-CF | 2018 / Lyon | Algorithm + analysis |
| Heterogeneous web graphs | Wang et al., HAN | 2019 / San Francisco | Algorithm |
| Social-platform measurement | Kwak et al., Twitter | 2010 / Raleigh | Measurement |

> The 2015→2017→2018→2019 sequence also traces a *lineage* (embeddings → neural
> interaction functions → probabilistic deep models → heterogeneous attention)
> usable verbatim as a related-work waypoint chain
> (`../../skills/webconf-related-work/SKILL.md`).

## Heritage note (cite with care)

The search-engine paper by **Brin & Page** was presented at **WWW7 (1998,
Brisbane)** and published in the conference's journal-format proceedings
(*Computer Networks and ISDN Systems* 30(1-7):107-117) — cite the journal issue,
not "Proceedings of WWW" in the modern ACM style. Early-edition citations
generally predate the ACM-proceedings era; check dblp for the correct container.

## Omitted after checking (misattribution guard)

- **node2vec (Grover & Leskovec)** — KDD 2016, not WWW, despite constant
  co-citation with LINE. Do not attribute here.
- **DeepWalk (Perozzi et al.)** — KDD 2014, not WWW.
- **BPR (Rendle et al.)** — UAI 2009, not WWW, though it is the standard implicit
  -feedback baseline in WWW recommendation papers.
- **LightGCN (He et al.)** — SIGIR 2020, not WWW; frequent confusion with NCF's
  lineage.
- **"The PageRank Citation Ranking" (Page et al.)** — a 1999 Stanford technical
  report, never a WWW proceedings paper; see the heritage note for the related
  WWW7 citation that *is* valid.

Before adding a row, confirm the proceedings entry on dl.acm.org or dblp (title,
authors, edition, pages), record the access date, and when verification fails,
either omit or add as 待核实 with no attribution.
