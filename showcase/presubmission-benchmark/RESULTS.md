# Results — pre-submission benchmark (2026-11-23)

Six venue families, 72 planted defects (47 mechanical + 24 substantive + 1 that is both
in effect), six clean controls. See [README.md](README.md) for the design and its limits.

## Headline

| Stage | Measure | Result |
|---|---|---|
| 0 · Preflight (deterministic) | Mechanical defects caught | **45 / 47 (95.7%)**. The 2 misses are documented known limits (below) |
| 0 · Preflight | False alarms on clean controls | **0 FAIL · 0 FLAG** across all 6 (one INFO reminder on ACL), in source, PDF and Word form |
| 0 · Preflight | Verdict separation | **6 / 6** clean copies GO, **6 / 6** seeded copies NO-GO |
| 2 · Referee panel (inline) | Planted substantive flaws kept as a *major* concern | **23 / 24 (95.8%)** |
| 2 · Referee panel | Planted substantive flaws raised at any severity | **24 / 24** |
| 2 · Referee panel | Preflight's two known misses, caught by the panel | **2 / 2** (both as major concerns) |
| 2 · Referee panel | Unplanted major concerns on clean controls | **8 across 6 papers (1.3 per paper)**: 4 genuine errors in the "clean" fixtures, 4 defensible critiques, 0 judged spurious |
| 2 · Referee panel | Decision band, seeded copy vs clean twin of the same paper | Seeded worse in **4 / 6**; in the other 2 the band tied but the seeded copy drew 3× and 2.5× the kept concerns |

## Stage 0: preflight on every fixture

| Fixture | Format | Venue rules | Mechanical caught | Missed | Clean copy | Verdict clean → seeded |
|---|---|---|---|---|---|---|
| `acl-nlp` | .tex | ACL-Skills | 7 / 8 | M7 NUM-MISMATCH (known) | 0 FAIL · 0 FLAG | GO → NO-GO |
| `erj-cn-did` | .md (Chinese) | Economic-Research-Journal-Skills | 7 / 8 | M8 NUM-MISMATCH (known) | 0 FAIL · 0 FLAG | GO → NO-GO |
| `icml-ml-method` | .tex | ICML-Skills | 8 / 8 | — | 0 FAIL · 0 FLAG | GO → NO-GO |
| `jama-rct` | .md | JAMA-Skills | 8 / 8 | — | 0 FAIL · 0 FLAG | GO → NO-GO |
| `jf-corporate-did` | .md | Journal-of-Finance-Skills | 8 / 8 | — | 0 FAIL · 0 FLAG | GO → NO-GO |
| `qje-labor-iv` | .tex | Quarterly-Journal-of-Economics-Skills | 7 / 7 | — | 0 FAIL · 0 FLAG | GO → NO-GO |

**The two known misses** are the same limitation twice. A wrong headline number that
coincides with a real number elsewhere in the paper is invisible to a context-free
traceability check:

- **ACL:** the seeded abstract says 48.9; the correct value is 47.5. But 48.9 is a real
  cell of Table 1, another filter's score on another benchmark.
- **ERJ:** the seeded introduction says 6.4 percentage points; the correct value is 4.6.
  But 0.064 is a real year-3 event-study coefficient, and ×100 is the right conversion
  for a percentage-point claim.

Both are recorded as `"preflight": "known-miss"` in the fixtures' `defects.json`, with
the reason. The panel caught both (ACL R1-M4, ERJ R3-M1). That is the design: the
deterministic stage handles what can be checked deterministically, and stage 2 reads in
context.

**Defects that moved the checker during the week.** These are the bugs found while
building the benchmark, each fixed in the code rather than in the fixture:

- **Invisible JEL line:** `\noindent\textbf{JEL…}` collapsed into one token, so the JEL
  line disappeared.
- **Misread estimator name:** "双重稳健估计量" (doubly robust estimator) was read as a
  description of the standard errors.
- **Name parsing:** Chinese narrative citations captured the preceding verb, and English
  citations inside Chinese full-width punctuation were not parsed.
- **Derived numbers:** an unconditional pool of within-table differences matched almost
  any wrong one-decimal number. It is now gated on explicit comparisons and equal
  precision.
- **Descriptive tables:** a table with an N column was read as a regression table.
- **JF exhibits:** Roman-numeral numbering, as JF uses, was not recognised.

## Stage 0 across file formats (added 2026-11-24)

Authors submit PDFs and Word files, not the Markdown or LaTeX the fixtures are written
in. So every fixture, clean and seeded, was also converted and scored:

- to Word with pandoc;
- to PDF with xelatex (via pandoc) or pdflatex. The ICML and ACL fixtures were compiled
  two-column at 10pt, the layout those venues use.

| Format | Mechanical defects caught | False alarms on clean controls |
|---|---|---|
| Source (.md / .tex) | 45 / 47 | 0 FAIL · 0 FLAG |
| PDF (single- and two-column) | 45 / 47 | 0 FAIL · 0 FLAG |
| Word (.docx, the three Markdown fixtures) | 23 / 24 | 0 FAIL · 0 FLAG |

The misses in every format are the same two known ones. Reaching parity took ten fixes
to the PDF and Word readers:

- **Column order:** pdftotext's reading order interleaves the two columns. Two-column
  layout is now detected from the gutter in `-layout` output and extracted in stream
  order.
- **Structure:** statement headings ("Key Points", "Data Sharing Statement"), Chinese
  section headings (一、 / （一）) and captions that run on into prose were not recognised.
- **References:**
  - AMA/Vancouver and corporate-author entries, and author lines ending "(2019).",
    were split wrongly;
  - a second, cruder re-merge of reference entries was removed;
  - a missing LaTeX citation renders as "(?)", which is now a REF-MISSING.
- **URLs:** links broken across lines are rejoined.
- **Table notes:** a note split by a page break is reconnected.
- **Word:** heading styles in Chinese-locale Word are resolved through `styles.xml`.

The first PDF run, before these fixes, gave 43/47 caught and 165 false alarms on the six
clean papers. Most came from one Chinese PDF in which no section heading was
recognised. The per-format script is not committed, because it needs pandoc and a TeX
installation, and CI is stdlib only. Its result is recorded here.

## Fixture revision v2 (2026-11-24)

The panel's blind read found real errors in three "clean" fixtures (next section). They
were fixed afterwards: ACL language coverage and the quota attribution, the ERJ standard
error of a difference, and the JF sample definition and reference period. Each
`defects.json` now records `"revision": "v2 …"`. **The panel results below were produced
on v1** (commit `d9793503`). The stage-0 results above are on v2, and both versions give
the same mechanical scores.

## Stage 2: referee panel, graded against the manifests

The grading rule: a planted flaw counts as **caught** when a concern the verifier kept
as major names the same mechanism at the same location. It counts as **raised** when it
appears at any severity. The grader read every concern, not only keyword matches.

| Seeded fixture | Band (form) | S1 | S2 | S3 | S4 | Bonus |
|---|---|---|---|---|---|---|
| `jf-corporate-did` | major revision (C) | ✓ TWFE under staggered adoption | ✓ clustering below treatment level | ✓ concurrent state shocks unaddressed | ✓ "first causal" claim vs. Barrot | also listed the 8.6/6.8 mismatch and missing disclosure as carry-overs |
| `qje-labor-iv` | reject (C) | ✓ exclusion broken by bonus + navigator | ✓ weak distance IV, no F | ✓ differential attrition, no Lee bounds | ✓ LATE scaled to all claimants | found that the matched N is inconsistent with the stated rates |
| `icml-ml-method` | reject (A) | ✓ selection on test split | ✓ "significant" gain within 1 SD | ✓ 96-config search vs. untuned baselines | ✓ "general solution" overclaim | budget-confounded ablation |
| `acl-nlp` | resubmit next cycle (B) | ✓ contamination contradiction | ✓ uncorrected per-language tests | ✓ "any language / no human data" overclaim | ◐ ethics removal raised, **downgraded to minor** | caught the 48.9 vs 47.5 known miss as major |
| `jama-rct` | reject (E) | ✓ unmasked outcome assessors | ✓ per-protocol only, no ITT | ✓ primary outcome switched from registry | ✓ CV-event and universal-adoption claims | — |
| `erj-cn-did` | 大修 / major revision (G) | ✓ significant pre-trends waved away | ✓ regional difference without a test | ✓ Baron–Kenny + Sobel as the mechanism | ✓ nationwide-rollout and TFP overreach | caught the 6.4 vs 4.6 known miss as major |

**The one non-catch.** In ACL S4, the seeded copy deletes annotator pay, consent, ethics
review and PII scrubbing. The panel noticed: R3-M2 lists "no pay, consent, IRB". But the
verifier downgraded it to minor as a "reporting gap". Under the ARR form a missing
ethics review can trigger an ethics flag rather than a score change, so the downgrade is
defensible. It is still counted as a miss.

### Clean controls: every unplanted major concern

| Clean fixture | Band | Kept major concerns | Our classification |
|---|---|---|---|
| `qje-labor-iv` | minor revision | none | — |
| `jama-rct` | minor revision | none | — |
| `icml-ml-method` | lean-accept | missing closest group-label-free baselines (CnC, EIIL, GEORGE, AFR) | defensible critique: the fixture does not cite them |
| `jf-corporate-did` | major revision | (1) sample truncated on post-treatment revenue; (2) anticipation window falls in the omitted year | (1) **genuine fixture error**, a real selection problem in the design as written; (2) **genuine fixture error**: the text gives a 6–9-month enactment lag, so the reference-year choice is wrong |
| `acl-nlp` | Findings | (1) Yoruba is in none of the four benchmarks; (2) only Llama 2 models; (3) unverifiable cited source | (1) **genuine fixture error**: the clean paper's coverage claim is false; (2) defensible scope critique; (3) **genuine fixture artefact**: a fictional reference created for a seeded defect |
| `erj-cn-did` | major revision | (1) SE of a between-group difference too small (0.012 vs ≈0.019); (2) contributions are mainly econometric | (1) **genuine fixture error**: the clean paper's arithmetic is wrong; (2) defensible critique |

The fixture-writing agents could not see these errors, but the panel found them in a
blind read. They are fixed in fixture v2 (see above). The panel runs here used v1.

## Multi-agent configuration, two targeted runs (2026-11-24)

The runs above used the cheaper inline configuration. The protocol recommends the
multi-agent one: an AE, three referee subagents that cannot see each other's work, and
a separate verifier. It was tested on the two most informative v2 cases, both blinded
under neutral names ([`panel-runs-multiagent/`](panel-runs-multiagent/)):

| Case | Inline (v1) | Multi-agent (v2) |
|---|---|---|
| `acl-nlp`, seeded | 3 of 4 planted flaws kept as major; S4 (ethics details removed) downgraded | **4 of 4 kept as major**; S4 caught (R3-M3), as was the 48.9 known miss. 23 concerns filed, 18 kept, 5 downgraded |
| `jf-corporate-did`, clean | 2 unplanted major concerns (both genuine v1 fixture errors, since fixed) | **6 unplanted major concerns**: investment pre-trends (breakdown value 0.9), a placebo group that is not clean, buyer-side spillovers, a likely misdescription of Barrot (2016) and Barrot and Nanda (2020), a thin mechanism, and COVID-era timing. Band unchanged (major revision) |

The multi-agent panel is **more thorough in both directions**. It closed the inline
panel's one miss, and it raised three times as many unplanted major concerns on a clean
paper. Read individually, these are defensible referee points for a JF submission, and
the literature one may be a genuine error in the fixture. But they show that "a clean
paper comes back with no major concerns" should not be expected at a top-3 bar. Use
multi-agent when the goal is to surface everything a demanding referee could raise, and
inline for a cheaper first pass. Two runs are not a rate. These are recorded as
observations, not estimates.

## What to take from this

1. **The two stages are complementary.** Preflight is exact on what can be checked
   mechanically and silent about meaning. The panel caught every planted substantive
   flaw and both of preflight's blind spots.
2. **False alarms are low but not zero.** No mechanical false alarms. At the panel stage,
   about one unplanted major concern per clean paper, most of them real.
3. **The real-preprint run mattered more than the synthetic one.** It found five checker
   problems the fixtures had not exercised, including a silent false green. See
   [`../presubmission-real-preprint/REPORT.md`](../presubmission-real-preprint/REPORT.md).
   The next version of this benchmark should add real papers with known post-review
   changes.
