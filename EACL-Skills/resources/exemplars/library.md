# EACL Exemplars Library (topic × contribution)

> **Verified via web search against the ACL Anthology, access date 2026-07-09.** Every paper below was
> checked on `aclanthology.org` to confirm it appeared at an **EACL edition specifically** — matching the
> Anthology venue line ("Conference of the European Chapter of the Association for Computational
> Linguistics" or "Findings of the Association for Computational Linguistics: EACL") to the edition, plus
> author list, year, and page range. Papers that could not be cleanly confirmed as **EACL** (as opposed to
> a sibling *ACL venue) were **omitted**. It is deliberately a short, verified list (5 verified > 15
> guessed).
>
> **Sibling-confusion guard:** EACL is **not** ACL, EMNLP, NAACL, AACL, TACL, or LREC-COLING. The ACL
> Anthology hosts all of them, and the shared identifiers are a trap: the legacy prefix **`E`** (e.g.
> `E17-`) *is* EACL, but the modern `YYYY.eacl-*` / `YYYY.findings-eacl-*` slugs sit right next to
> `YYYY.acl-*`, `YYYY.emnlp-*`, and `YYYY.naacl-*`. A paper's Anthology ID must literally say `eacl`.
> **Edition ↔ identifier (verified rows below):** `E17-` = EACL 2017 (15th, Valencia); `2021.eacl-main` =
> EACL 2021 (16th, online); `2024.eacl-long` = EACL 2024 (18th, St. Julian's, Malta).
>
> **Use principle (zero hallucination):** this file gives **design positioning only**. It does not
> reproduce or invent results, metrics, or table numbers — read the original in the Anthology before
> citing anything. For EACL-specific policy and the routing rules, see
> [`../official-source-map.md`](../official-source-map.md) and
> [`../../skills/eacl-topic-selection/SKILL.md`](../../skills/eacl-topic-selection/SKILL.md).

---

## How to use this library

Pick the row whose **topic × contribution** is closest to yours, then study how that paper earns an EACL
slot: a **task-first framing on the first page**, a **claim that is measured rather than asserted**, and
**scope stated honestly** — the EACL bar (see
[`../../skills/eacl-writing-style/SKILL.md`](../../skills/eacl-writing-style/SKILL.md) and
[`../../skills/eacl-experiments/SKILL.md`](../../skills/eacl-experiments/SKILL.md)). For each, ask the
self-check question before claiming your paper is "EACL-shaped."

---

## By contribution type

### Efficient method / strong baseline (text classification)

- **Joulin, Grave, Bojanowski & Mikolov, "Bag of Tricks for Efficient Text Classification," EACL 2017,
  Short Papers.** Verified: `aclanthology.org/E17-2068/` (Proceedings of the *15th* Conference of the
  European Chapter of the ACL, Volume 2: Short Papers).
  - **Why it is an exemplar:** a **four-page short paper** whose contribution is a *simple, fast baseline*
    that holds its own against heavier models — the archetypal EACL short paper (one clean claim, decisive
    efficiency evidence, no padding). A model for the "short paper is a genre, not a truncated long paper"
    rule in `eacl-submission`.
  - **Self-check:** can your idea be stated and defended in four pages, with the efficiency/accuracy
    trade-off measured, rather than stretched to eight?

### Analysis / probing of pretrained models (does X still help?)

- **Glavaš & Vulić, "Is Supervised Syntactic Parsing Beneficial for Language Understanding Tasks? An
  Empirical Investigation," EACL 2021, Main Volume (Best Long Paper).** Verified:
  `aclanthology.org/2021.eacl-main.270/` (16th Conference of the European Chapter of the ACL), pp.
  3090-3104.
  - **Why it is an exemplar:** a **negative/empirical result** — asking whether an old inductive bias
    still pays off in the pretrained-model era — carried by careful controls across tasks. EACL rewards a
    well-scoped empirical question answered cleanly over a flashy system claim (`eacl-experiments`).
  - **Self-check:** is your research question falsifiable and answered with matched controls, so a null
    result would be as publishable as a positive one?

### Dataset/evaluation critique (contamination & overlap)

- **Lewis, Stenetorp & Riedel, "Question and Answer Test-Train Overlap in Open-Domain Question Answering
  Datasets," EACL 2021, Main Volume (Best Short Paper).** Verified: `aclanthology.org/2021.eacl-main.86/`
  (16th Conference of the European Chapter of the ACL), pp. 1000-1008.
  - **Why it is an exemplar:** turns a **measurement of a widely used benchmark** into the contribution —
    quantifying test-train overlap and re-reading model results through it. Pairs with the contamination
    discipline in `eacl-reproducibility` and `eacl-experiments`.
  - **Self-check:** does your critique *measure* the flaw and show its consequence for reported numbers,
    rather than merely asserting a benchmark is imperfect?

### Multilingual / lower-resource analysis (morphology across many languages)

- **Bollmann & Søgaard, "Error Analysis and the Role of Morphology," EACL 2021, Main Volume (Best
  Paper).** Verified: `aclanthology.org/2021.eacl-main.162/` (16th Conference of the European Chapter of
  the ACL).
  - **Why it is an exemplar:** tests two folk conjectures about morphology **across up to 57 languages and
    four tasks**, confirming one and refuting the other — the multilingual, cross-linguistic breadth that
    plays to EACL's community. A model for `eacl-experiments`' "breadth matched to the claim."
  - **Self-check:** is your multilingual claim backed by enough languages to separate a real pattern from
    a few convenient cases, with the negative half reported honestly?

### LLM-era evaluation integrity (data contamination in closed models)

- **Balloccu, Schmidtová, Lango & Dušek, "Leak, Cheat, Repeat: Data Contamination and Evaluation
  Malpractices in Closed-Source LLMs," EACL 2024, Long Papers.** Verified:
  `aclanthology.org/2024.eacl-long.5/` (18th Conference of the European Chapter of the ACL, Volume 1: Long
  Papers), pp. 67-93, St. Julian's, Malta.
  - **Why it is an exemplar:** a **systematic review** of how closed LLMs get indirectly exposed to
    benchmarks, quantifying leakage across hundreds of papers — an evidence-and-methodology contribution,
    not a model. Shows EACL's appetite for rigorous, honest evaluation critique in the LLM era
    (`eacl-writing-style`'s "scope the LLM-era claim").
  - **Self-check:** if your contribution is a critique or a protocol, is it backed by a reproducible
    survey/measurement whose scope and method are stated, rather than anecdote?

---

## Topic × contribution grid (each cell is a verified EACL paper above)

| Contribution type | Verified EACL exemplar | Edition / Anthology ID |
| --- | --- | --- |
| Efficient method / short paper | Joulin et al., "Bag of Tricks for Efficient Text Classification" | 2017 / `E17-2068` |
| Probing / does-X-still-help | Glavaš & Vulić, "Is Supervised Syntactic Parsing Beneficial...?" | 2021 / `2021.eacl-main.270` |
| Dataset/eval critique | Lewis, Stenetorp & Riedel, "Question and Answer Test-Train Overlap..." | 2021 / `2021.eacl-main.86` |
| Multilingual analysis | Bollmann & Søgaard, "Error Analysis and the Role of Morphology" | 2021 / `2021.eacl-main.162` |
| LLM evaluation integrity | Balloccu et al., "Leak, Cheat, Repeat..." | 2024 / `2024.eacl-long.5` |

> Five verified papers across five contribution cells. The three EACL 2021 Main-Volume rows also show that
> **best-paper recognition at EACL routinely goes to analysis, critique, and multilingual breadth**, not
> only to state-of-the-art systems — a useful calibration signal for `eacl-topic-selection`.

---

## Omitted for lack of clean EACL verification (do not attribute to EACL without re-checking)

To keep the list zero-hallucination, candidates that could not be pinned to an EACL edition at build time
were excluded. Common traps to guard against:

- **`E`-prefix vs `2021.eacl` confusion.** The legacy `E##-` identifiers are EACL, but any paper whose
  Anthology ID is `YYYY.acl-*`, `YYYY.emnlp-*`, `YYYY.naacl-*`, or `YYYY.findings-emnlp-*` is a sibling
  venue, not EACL — several famous NLP papers with "European" author lists live at ACL or EMNLP.
- **LREC / COLING confusion.** European resources and multilingual papers frequently appear at
  LREC-COLING, which is *not* an EACL edition even though the community overlaps.
- **TACL papers presented at EACL.** TACL articles can be *presented* at an EACL meeting but are published
  in the TACL journal track — cite them as TACL, not as EACL proceedings.

Before adding any new paper, confirm it on `aclanthology.org` by matching the **venue line to a specific
EACL edition** (the volume landing page names the numbered Conference of the European Chapter of the ACL,
or "Findings ... EACL"), then record author list, year, and pages, and update the access-date header. When
in doubt, omit. If web search is unavailable, add the row as **待核实 / TO VERIFY** with **no
attribution**.
