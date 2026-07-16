# External Tools & Resources for PiHG-Style Review Essays

Software and services useful when preparing a *Progress in Human Geography* review article or Progress
Report. PiHG is a **review and theory** journal: your "data" is a **literature**, so the tooling here is
for **finding, managing, mapping, synthesizing, and citing** a corpus — not for collecting or analyzing
primary observations. Match tools to how systematic your review is (narrative, structured, or fully
systematic), and verify any PiHG-specific policy in [`official-source-map.md`](official-source-map.md).

> A caution up front: PiHG essays are **argument-led, not protocol-led**. These tools help you command a
> literature; they do **not** substitute for the critical, synthetic thinking the journal actually
> rewards. A bibliometric map is an input to an argument, never the argument itself.

## 1. Reference management & the corpus

| Tool | What it gives you |
|------|-------------------|
| **Zotero** (open source) | Collect, deduplicate, tag, and annotate the corpus; group libraries for co-authors; SAGE Harvard CSL styles |
| **EndNote / Mendeley** | Alternatives with PDF libraries and cite-while-you-write |
| **BibTeX / BibLaTeX** | Plain-text bibliography if drafting in LaTeX |
| **Connected Papers / ResearchRabbit / Litmaps** | Visual citation neighborhoods to find the works you are missing and trace a debate's lineage |

## 2. Discovery & the search itself

| Source | Use |
|--------|-----|
| **Scopus** / **Web of Science (Core Collection)** | Structured search, citation counts, and export for a defensible, reproducible corpus; the standard bases for a bibliometric map |
| **Google Scholar / Publish or Perish** | Broad recall and forward-citation chasing; weaker precision — triangulate, do not rely on alone |
| **Dimensions / Lens.org** | Open citation data and export |
| **JSTOR / SAGE Journals / Taylor & Francis / Wiley** | Full text for the human-geography canon and its journals |

For a **structured or systematic** review, record the database, date, exact query string, filters, and
counts so the search is reproducible (see PRISMA below).

## 3. Systematic-review protocol & reporting

- **PRISMA 2020** (checklist + flow diagram) — the standard for reporting *how* a systematic corpus was
  assembled (identification → screening → inclusion). Even a narrative PiHG review benefits from stating
  its corpus logic; a fully systematic one should include a PRISMA flow.
- **Registration** (e.g., PROSPERO for protocols, OSF for a pre-registered plan) — where the review is
  systematic enough to warrant it. Optional for a conceptual essay; confirm any PiHG expectation.
- **Rayyan / Covidence** — screening and inclusion/exclusion management for larger structured reviews.

## 4. Bibliometric & science-mapping tools

| Tool | What it maps |
|------|--------------|
| **VOSviewer** | Co-citation, bibliographic-coupling, and keyword co-occurrence networks from Scopus/WoS exports |
| **CiteSpace** | Temporal "burst" detection — emerging fronts and turning points in a field |
| **bibliometrix / biblioshiny** (R) | Scriptable, reproducible bibliometric analysis and figures |
| **Gephi** | General network visualization and layout for citation/keyword graphs |

Use these to **locate** debates and gaps and to make a *conceptual* exhibit — never to let counts stand
in for a critical reading of what the works actually argue.

## 5. Qualitative synthesis & coding

- **CAQDAS**: NVivo, ATLAS.ti, MAXQDA, or Taguette (open source) — code a corpus thematically when the
  synthesis is interpretive; useful for a meta-narrative or thematic-synthesis review.
- **Synthesis methods to name explicitly**: narrative synthesis, thematic synthesis, meta-narrative
  review, critical interpretive synthesis, realist review — state which logic your essay follows.

## 6. Conceptual exhibits (figures do synthesis, not data)
- Diagramming: draw.io/diagrams.net, Excalidraw, Inkscape (vector), TikZ (LaTeX) for typologies and
  framework diagrams; keep them legible in grayscale and free of chartjunk
- Timelines / genealogies of a concept: simple vector figures or tables; label periods and turning points
- Tables: comparison/typology matrices that do the synthesizing work (approach × dimension), not raw data

## 7. Writing, references & submission
| Item | Note |
|------|------|
| Referencing style | **SAGE Harvard** (author–date); keep one consistent style; Zotero/EndNote CSL available |
| Drafting | Word or LaTeX (Overleaf); prepare a **double-anonymous** manuscript + separate title page |
| Abstract & keywords | **Unstructured abstract ~100 words**; **minimum 5 keywords** after the abstract |
| Submission portal | **SAGE Track** (ScholarOne-based), via the SAGE journal page |
| Length | Review article **4,000–8,000 words**, incl. endnotes, **excl. bibliography** (verify) |

## 8. Cautions
1. **Verify volatile specifics** (caps, abstract length, keyword minimum, OA/fee, policy wording) on the
   official SAGE/PiHG pages — they change; unverified items are 待核实.
2. **Tools are inputs, not the contribution** — a VOSviewer map or PRISMA flow supports an argument; PiHG
   publishes the argument, not the map.
3. **PiHG does not publish empirical results** — do not repurpose primary-data tooling (stats packages,
   GIS analysis) as if the essay reported a study.
4. **Make the corpus defensible** — record how it was assembled so a reviewer can trust the coverage.
5. **Cite the debate, not just the citation counts** — bibliometrics locate the conversation; you still
   have to read and adjudicate it.
