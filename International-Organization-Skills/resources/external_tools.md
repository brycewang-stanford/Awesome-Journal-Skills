# External Tools & Resources for IO-Style International-Relations Research

Data sources, software, and packages useful when preparing an *International Organization* (IO)
submission. IO is an **IR-specialist flagship**: a submission asks an **international or cross-border**
question — international institutions and law, cooperation and conflict, international political economy
(IPE), security, foreign policy, or IR theory — and the international phenomenon must be a **major cause
or effect**, not a backdrop. Work may be **quantitative, formal (game-theoretic), or qualitative**.
Match tools to the level of analysis (state, dyad, IGO, sub-state, transnational) and design. Check
licenses and current access terms before use, and verify any IO-specific policy in
[`official-source-map.md`](official-source-map.md).

## 1. Data sources by IR research area

### Conflict, security & cooperation
| Source | Provider | Typical use |
|--------|----------|-------------|
| Correlates of War (COW) | COW Project | Interstate/intrastate war, MIDs, alliances, national capabilities (CINC) |
| UCDP / PRIO Armed Conflict | Uppsala / PRIO | Conflict onset, fatalities, actor-level dyads |
| ACLED | ACLED | Disaggregated political-violence events |
| ICB (International Crisis Behavior) | Duke/UMD | Foreign-policy crises, escalation |
| Militarized Interstate Disputes (MID) | COW | Dyadic dispute escalation |

### International institutions, law & cooperation
| Source | Provider | Typical use |
|--------|----------|-------------|
| Correlates of War IGO data | COW | State membership in intergovernmental organizations |
| UN General Assembly voting (Voeten) | Harvard Dataverse | Ideal points, state preference alignment |
| DESTA / treaty databases | DESTA | Design of trade agreements; treaty provisions |
| World Bank / IMF / WTO data | IO secretariats | Lending, conditionality, disputes, compliance |
| Treaties & ratification (e.g., human-rights) | Various | Commitment, compliance, depth/flexibility |

### International political economy (IPE)
| Source | Provider | Typical use |
|--------|----------|-------------|
| IMF IFS / World Bank WDI | IMF / World Bank | Trade, capital flows, growth, reserves |
| COMTRADE / CEPII | UN / CEPII | Bilateral trade, gravity-model inputs |
| AidData | William & Mary | Foreign aid and development finance projects |
| KOF Globalisation Index | ETH Zurich | Economic/social/political globalization |
| Penn World Table | UC Davis/Groningen | Cross-country macro comparisons |

### Regimes, preferences & cross-national context
| Source | Provider | Typical use |
|--------|----------|-------------|
| V-Dem | University of Gothenburg | Regime type, democracy indicators (panel) |
| Polity5 | Center for Systemic Peace | Regime authority for IR controls |
| Foreign-policy / elite & mass surveys | Various | Public opinion on war, trade, institutions |

## 2. Software by method

### R
- Causal inference: `fixest`, `did` (Callaway–Sant'Anna), `MatchIt`, `WeightIt`, `rdrobust`, `estimatr`, `sensemakr`
- Dyadic / network IR data: `peacesciencer` (build dyad-year data), `igraph`, `statnet`/`ergm` (alliance/trade networks), `amen` (dyadic/AME models)
- Spatial/gravity & TSCS: `fixest`/`gravity` (PPML gravity models), `plm`, `panelView`
- Survey/experiments: `cregg`/`cjoint` (conjoint), `DeclareDesign`, `ri2` (randomization inference)
- Text-as-data (treaties, speeches, IO documents): `quanteda`, `stm`, `text2vec`; embeddings/LLM pipelines
- Bayesian / measurement: `brms`, `rstan`/`cmdstanr`, `MCMCpack`, `emIRT` (ideal points)
- Reproducibility: `renv` (pin versions), `targets` (pipelines)

### Stata
- `reghdfe`, `ppmlhdfe` (gravity), `csdid`, `did_multiplegt_dyn`, `rdrobust`, `ivreg2`/`ivreghdfe`
- `boottest` (wild-cluster bootstrap), `ritest` (randomization inference), `coefplot`

### Python
- `pandas`, `numpy`, `statsmodels`, `linearmodels` (panel/IV); `networkx` for IGO/alliance networks
- Text-as-data: `spaCy`, `scikit-learn`, `transformers`/`sentence-transformers` for treaty/document corpora
- `matplotlib` / `seaborn` for exhibits; pin with `requirements.txt` / `pip freeze`

### Formal theory
- Game-theoretic modeling (bargaining, signaling, audience-cost, delegation, cooperation games);
  comparative statics and equilibrium derivations. IO **verifies proofs of formal models** before final
  acceptance — keep derivations clean, complete, and reproducible (a proof appendix the editors can check).

### Qualitative & mixed-methods
- CAQDAS: NVivo, ATLAS.ti, Taguette (open source), MAXQDA — coding interviews, archives, IO documents
- Process tracing: explicit hypothesis tests (hoop / smoking-gun / straw-in-the-wind); Bayesian process tracing
- Transparency: **Qualitative Data Repository (QDR)** active citation / Annotation for Transparent Inquiry (ATI)

## 3. Design & transparency
- Preregistration / pre-analysis plans: **OSF Registries**, EGAP, AsPredicted; share **anonymized** for double-blind review
- Power/design: `DeclareDesign` (declare → diagnose → redesign); simulation-based power for dyadic and clustered designs
- Replication package destined for the **IO Dataverse on Harvard Dataverse** at conditional/final
  acceptance (see `io-transparency-and-data-policy`); add a **Data Availability Statement** before the references

## 4. Figures & exhibits
- Coefficient/forest plots (`coefplot`, `ggplot2`/`broom`), event-study and RD plots, marginal-effects
  and predicted-probability plots (`marginaleffects`), conjoint AMCE plots
- Maps for geographic/spatial variation (`sf`, `tmap`); network diagrams for alliance/trade/IGO structure
- Colorblind-safe palettes and figures legible in grayscale; vector output (PDF/EPS) for print

## 5. Writing & references
- Reference managers: Zotero, BibTeX/BibLaTeX, EndNote. Accepted IO manuscripts use **short author-date
  footnotes** rather than parenthetical references; keep one consistent style and convert at acceptance
- Typesetting: LaTeX (TeX Live / MacTeX, Overleaf) or Word; prepare a **double-blind** manuscript
  (no identifying metadata; **third-person self-citation** after the title page) plus a separate title page
- Submit the **abstract, word count, and acknowledgments separately** from the manuscript; an **ORCID** iD
  for the corresponding author

## 6. Process & portal
| Item | Note |
|------|------|
| Submission portal | **Editorial Manager** — confirm current URL on the official page |
| Owner / publisher | **IO Foundation** / **Cambridge University Press** |
| Review model | **Double-blind** — anonymize the manuscript; third-person self-citation |
| Article types | Research Article **≤ 14,000 words** · Research Note **≤ 8,000** · Essay **≤ 10,000** (incl. tables/figures/notes; excl. bibliography) |
| Supplementary material | **Should rarely exceed twenty pages**, especially at initial submission |
| Data policy | Data/code **requested at conditional acceptance**; **IO staff verify quantitative results + formal proofs before final acceptance**; deposit to **IO Dataverse**; **Data Availability Statement** required |
| Submission fee | None stated (verify); any open-access APC handled by Cambridge after acceptance |

## 7. Cautions
1. **Verify volatile specifics** (editors, exact caps, abstract limit, fee/APC, policy wording) on the
   official Cambridge/IO pages — they change; unverified items are marked 待核实.
2. **Center the international level** — IO is an IR-specialist journal; the international or cross-border
   phenomenon must be a **major cause or effect**, not context for a domestic-politics paper.
3. **Anonymize properly** — IO is double-blind; strip metadata and cite your own work in the **third
   person** after the title page.
4. **Engineer the verifiable package from day one** — IO staff **re-run quantitative results and check
   formal proofs before final acceptance**; an unscripted analysis or a hand-waved proof stalls acceptance.
5. **Theory carries the paper** — IO rewards **generalizable theory** about international politics, not a
   data exercise; speak across rationalist/constructivist and IPE/security divides where relevant.
