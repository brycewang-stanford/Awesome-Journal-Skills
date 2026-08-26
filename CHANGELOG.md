# Changelog

All notable changes to this repository. Versions apply to the plugin packs, which are
released together — every first-party pack carries the same version so that
`/plugin install` never leaves a user with a mixed-vintage set.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this
project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Two of the repository's own instruments had stopped working, and neither said so. The
quality scorecard reported a mean of 99.2/100 while measuring almost nothing; the
abstract harvester recorded "no such paper" for papers an API had merely refused to
answer about. Both are fixed here, both now have tests, and the retrieval index turns
out to have been running at a third of a depth nobody had measured.

A third instrument was missing rather than broken. For a conference, "when was this
re-read?" and "is it still true?" are different questions, and only the first was being
asked — so a pack could be a month old, accurate, and entirely about a cycle that closed
before the reader arrived. That is what issue #3 reported, and `cycle_audit.py` now asks
the second question for all 90 conference packs.

The largest change here is not a fix. The matcher had only ever searched one vocabulary
per venue, derived from each pack's own prose — and a pack's prose is about a *process*
while a paper's title is about a *subject*. Asked to connect "Deep Contextualized Word
Representations" to ACL through a vocabulary in which ACL is largely a set of anonymity
rules, it could not, and neither could it for one gold paper in seven. Venues now carry
a second vocabulary built from the titles of the articles they actually published, and
the headline recall moves further in one step than everything else in this release
combined.

### Added

- **A subject vocabulary for every venue the free registries can identify**
  (`tools/fetch_venue_topics.py`, `topic-postings.tsv`, `venue-sources.tsv`). Journals
  resolve through Crossref, conference series through DBLP, and each venue's ranked
  TF-IDF vocabulary is derived from the titles of its own recent articles. `match_lib`
  loads it beside the scope index and merges the two; document frequency is computed per
  file, because a term's rarity among published titles is a different measurement from
  its rarity among editorial prose. **Held-out `test` half: R@10 46.7% → 65.3%,
  R@1 18.1% → 24.4%, MRR 0.269 → 0.374, and any-rank 85.0% → 96.2%** —
  the last number is the one that matters, because it is coverage rather than ranking:
  a seventh of the gold set had been unreachable at any depth. `wrong-lane@10` falls
  6.7% → 4.2% at the same time, which is the direction a *subject* vocabulary
  should move it. `eval/RESULTS.md` now prints the scope-only configuration beside the
  headline so the contribution stays visible rather than being absorbed into it.
- **`audit_repo.check_documented_counts`** — pins every count written into the
  capability docs to the generated file it describes. It was added because all five had
  drifted: a 743-venue index that holds 744, 289 depth packs that are 290, a scope
  vocabulary "300 terms deep" that has been 900 since the depth was measured, and two
  files claiming 1,725 and 1,507 ladder edges against each other and against the 1,511
  rows in `ladder.tsv`. Every occurrence is checked, and a sentence that stops stating
  its count fails rather than passing quietly.
- **`tools/tests/`** — 359 offline unit tests, stdlib `unittest`, under a second, run
  first in `run_checks.py`. `py_compile` was the entire test suite for 200 KB of Python
  that every gate depends on, and the generators' `--check` runs are not a substitute:
  they compare a fresh build against a committed build produced by the same code, so a
  wrong rule reproduces itself and passes. The tests build their own fixtures rather
  than reading the committed index, so a failure means the rule changed.
- **Hero-asset integrity check** (`audit_repo.check_hero_assets`) — pins the five
  images at the top of the READMEs by dimensions and a byte floor.
- **Two more abstract sources** — Europe PMC (near-complete for medicine and the life
  sciences) and arXiv (the CS and physics preprints Crossref misses), asked after
  Crossref and before the opt-in, now-billed OpenAlex. The miss cache records *which*
  source said no, so adding a source re-opens every paper the previous one could not
  find. The harvest completed at **729 term bags, 42% of the gold set** (Crossref 393,
  Europe PMC 91, arXiv 85, plus the 160 rows OpenAlex had produced before it started
  billing), with zero declines recorded as misses.
- **The realistic eval configuration is reported for the first time.**
  `title+abstract` had been withheld at 5% coverage since the eval was built; it now
  covers 381 of the 861 test papers (44%) and scores **R@10 54.9%, MRR 0.339** against
  the bare title's 46.7%. Two things a reader should take from it: an abstract is worth
  about as much as knowing the discipline (55.7%), and its `any-rank` of 100% is a
  query-length artefact — 130 median terms against a 900-deep index reach *something*
  in the true venue almost always — not a solved coverage problem. Coverage is uneven by
  discipline and `RESULTS.md` now says by how much.
- **Dimension-saturation reporting** in the scorecard, so the next dimension to stop
  measuring anything is visible before it flatlines rather than years after.
- **Discipline routing for the abstract sources**, so a biomedical index is not asked
  about a marketing paper and a preprint server is not asked about a 1985 accounting
  paper. Cut the harvest from ~14s per paper to a fraction of that, and stopped
  spending other people's free quota on requests that could only return "no result".
- **`tools/cycle_audit.py` + `.maintenance/CYCLE-CURRENCY.md`** — which *edition* each
  conference pack's source map describes. A journal has a standing masthead; a
  conference's page caps, chairs, tracks and review phases belong to one edition and are
  replaced wholesale by the next call, so freshness and currency come apart for the 90
  conference packs in a way `freshness_audit.py` structurally cannot see. Four states:
  `current`, `due` (this year's edition with no stated date still ahead — a live check,
  not an error), `stale` (a past edition; `--max-stale 0` is a hard gate in
  `run_checks.py`), and `retired` (the map says the venue stopped running, so a last
  edition in the past is correct — `IPSN-Skills` folded into SenSys after its 23rd).
  Edition labels are parsed from each pack's own prose, anchored to the venue's acronym,
  because a second stored copy of a fact is a fact free to drift. Two guards took real
  false positives out: a retirement claim must follow the venue's own name closely — in
  this corpus `OOPSLA-Skills` says two *review outcomes* "were merged into" one and
  `USENIX-Security-Skills` cites a page confirming USENIX **ATC** was discontinued — and
  years inside URLs and inline code spans are ignored, or a note recording that
  `aistats.org/aistats2027/` **404s** would be read as announcing a 2027 edition. That
  last one took two attempts: stripping the URL scheme was not enough, because the
  schemeless path still matches. Prose asserts; a quoted literal does not.
- **`.maintenance/DEAD-LINKS.md`**, generated by `external_link_audit.py --write` —
  the actionable half of the link audit as a queue with the citing files named, so a
  dead `Official` link is visible work rather than a line in a log nobody reruns.

### Changed

- **Retrieval depth 300 → 900.** `KEYWORD_DEPTH` had a comment explaining why the index
  wants a long tail and no measurement of how long. On the `dev` half, R@10 runs
  41.0 / 45.5 / 46.9 / 47.7 / 48.5 at depths 300 / 600 / 900 / 1200 / 2000; 900 is the
  knee. On the held-out `test` half, **R@10 41.5% → 46.5%**, MRR 0.245 → 0.267, and
  **any-rank 72.7% → 85.0%** — a quarter of the corpus had been unreachable at any
  depth. No weighting constant changed; they sit on the same plateau at the new depth.
  The CI recall floor moves 0.36 → 0.42. `scope-postings.tsv` grows 3.3 MB → 7.8 MB.
- **The quality scorecard is now two measurements.** Conformance (pass/fail, the gate)
  and a backlog score (0-100, the ranking). They were one number, and five of its six
  dimensions sat at maximum for 299 of 299 packs, making the score arithmetically
  `94 + freshness(0-6)` and `--min-score 94` a gate that could not fire. The backlog
  score uses only signals that still vary — source-map currency, unresolved-fact load,
  the depth of the pack's *thinnest* skill, its distance below the pack's own average,
  and execution-bridge wiring where a code library exists. Mean 77.6, min 51.5, max
  97.9, and the bottom of the table is a real work queue.
- **`--min-score 94` → `--require-conformance --min-score 40`** in `run_checks.py`.
- **The execution-bridge dimension was scoring the wrong 102 packs.** Wiring credit asks
  how much of a pack reaches `shared-resources/empirical-methods/execution-with-mcp.md`,
  and a pack entered that denominator by shipping *any* code library. But the bridge is
  StatsPAI and Stata — DiD, IV, RDD, DML, synthetic control — so the rule was asking 90
  AI conferences and 10 Chinese CS journals why they had not wired an econometrics stack
  to their PyTorch and EDA work, and docking them up to ten points for the answer. They
  were, between them, every unwired pack in the repository, which is what gave it away:
  all 139 packs that *had* wired it were economics, finance, management, marketing,
  accounting, political science, sociology and psychology. The denominator now also asks
  whether the discipline uses that stack (`venue_lib.uses_econometric_execution`), and
  the two genuinely-eligible packs left unwired — `Chinese-Journal-of-Management-Science`
  and `Language-Linguistic-Society` — were wired rather than excused. Wiring reads
  140/140; the backlog-score mean moves 77.7 → 80.3 because a hundred packs stopped being
  charged for work that was never theirs.
- **`CONFERENCE_DEPTH_PACKS` moved to `venue_lib`**, where the rest of the venue
  classification lives, now that two tools read it.
- **`tools/match_venues.py` marks a candidate it searched over less evidence.** Not every
  venue has a subject vocabulary — Chinese-language journals that neither Crossref nor
  DBLP indexes have none, by design rather than by oversight — and those venues compete
  on prose alone against neighbours that have both. A shortlist that hides that is
  comparing two things it measured differently, so such candidates print with a `°` and
  the tool warns when they make up a third of the list. On the gold set the asymmetry
  does not cost the Chinese venues anything measurable (R@10 unchanged at 70.0%), which
  is a reason to state it plainly rather than a reason to stop stating it.

### Verified

- **The Prop 99 showcase case re-runs to the digit.** Seven weeks after it was
  written, classic SCM returns −18.1934 against a recorded −18.19, ASCM −18.0774
  against −18.08, SDID −17.8985 against −17.90, placebo p 0.02564 against ≈0.026.
  Stated tolerance is ±0.5; observed deviation is zero. One new obstacle recorded in
  the case's own defect section: calling `sdid` the way the recipe specifies now
  raises a type error, and `synth(method="sdid")` is the working path.

### Fixed

- **`cycle_audit` matched a venue's acronym as a suffix.** `edition_years` anchored a
  pack on any occurrence of its venue's name followed by a year, with no left boundary,
  so "EACL 2027" contained "ACL 2027" and `ACL-Skills` was reported as anchored to an
  edition it holds no fact about — by the one check whose purpose is to notice that a
  conference pack describes a closed cycle. `VLDB` read "PVLDB 2018" the same way. A
  preceding letter or digit now disqualifies; a hyphen does not, because "IJCAI-ECAI
  2026" is genuinely an ECAI edition and "-27" is how AAAI writes its own.
- **The venue resolver matched Chinese journals on their translated names.** Six
  resolved on name equality alone and at least three were the wrong journal: 《金融研究》
  (ISSN 1002-7246) matched the Southern Finance Association's *Journal of Financial
  Research* (0270-2592), 《世界经济》 (1002-9621) matched an unrelated *Journal of World
  Economy* (2709-3999), 《中国社会科学》 (1002-4921) matched its own English translation
  edition (0252-9203) — a different serial. A wrong resolution does not rank a venue
  badly; it puts a different venue's subjects in its place. Where a pack states an ISSN
  the candidate must now carry it, an ISSN the pack states is looked up directly before
  any name search, and a Chinese-language venue with nothing to corroborate a name is
  refused outright. `M&SOM` and 《软件学报》 both resolve correctly through the direct ISSN
  lookup the same rule introduced.
- **Two harvest bugs that presented as venues with no articles.** DBLP answers a page
  size above 100 with a closed connection rather than an error, and `urllib.parse.quote`
  leaves "/" alone, so `q=stream:conf/aies:` was refused the same way — between them,
  every conference in the corpus harvested zero titles while its resolution row said it
  was correctly mapped. Crossref's `/journals/{issn}/works` answers only for the ISSN the
  publisher deposited under, so *Nature Plants* resolved on a print ISSN whose journal
  record reports 2,968 DOIs and whose works endpoint returns none. Both failures looked
  from the inside like a venue that simply publishes nothing, which is why `--harvest`
  now ends by naming how many resolved venues came back empty.
- **`assets/banner-en.png` was a bot-check screenshot.** The English README opened with
  a Cloudflare "Performing security verification" page, captured at exactly the
  banner's 2400x860 so every dimension still agreed. Nothing in the repository noticed:
  the file existed, the link resolved, the audit passed. Restored, and guarded.
- **A declining API is no longer recorded as a paper without an abstract.**
  `fetch_abstracts.py` returned `{}` for every 4xx that was not exactly 429 and the
  caller read that as "no such paper" — so when OpenAlex began billing per request and
  answering 403, one run cached 50 false misses, which are skipped forever. Answers are
  now typed `found` / `absent` / `declined`, `retryAfter` is honoured, and a source that
  declines is dropped from the run instead of being asked (and charged for) 1,600 more
  times.
- **Seven discipline rules could never fire.** `venue_lib.DISC` is a substring map,
  first match wins, so a specific key placed after a generic one it contains is dead
  code that hands its venues to the generic rule in silence.
  `International-Organization` never beat `Organization`, so the IR journal was filed
  under management — as were the Journal of Human Resources, the Journal of Economic
  Behavior and Organization, and the Journal of Law, Economics and Organization.
  Separately, `Science-Skills` was a whole-name rule written as a substring one, which
  is how INFORMS' Management Science came to share a discipline with PNAS. Eight depth
  venues reclassified; a test now fails if any rule becomes unreachable again.
- **Nine dead external citations repaired**, each verified against the page that
  replaced it rather than against a URL that merely returns 200 (EATCS Gödel Prize,
  AMA JPP&M, CIKM 2026 policies, SIGCOMM Test of Time, CoNEXT Best Paper, CoRL
  reviewer guide, two INFOCOM author pages, RSS review process). The rest are listed
  in `.maintenance/DEAD-LINKS.md` rather than guessed at.
- **Two "official" venue links pointed at squatters.** `coling.org` and
  `frontiersinai.com` had lapsed and been re-registered; both answered 200, so the
  audit filed them as ordinary redirects and nobody opened them. COLING's official
  anchor was serving an Indonesian online-poker site and ECAI's FAIA proceedings index
  a gambling landing page — repointed to the ACL Anthology COLING venue record and the
  IOS Press FAIA series page, each opened and confirmed to carry the cited fact. The
  redirect table now says out loud that a host change is also what a hijacked
  conference domain looks like.
- **Three live citations were catalogued as dead pages.** SciEngine and CNKI's magazine
  portal answer an unrecognised agent with 404 rather than 403, and the audit believed
  the first answer — sending a maintainer to hunt replacements for
  `sciengine.com/SCIS/home`, `sciengine.com/SSI/home` and CNKI's 《中国社会科学》 page,
  none of which had moved. A 404 is now re-asked once as a browser before it counts; a
  403 still is not, because that is a refusal, not an ambiguous answer.
- **Three of the audit's own "dead links" were its parser.** `URL_RE` matched
  printable ASCII only, truncating every citation with a non-Latin path — three live
  百度百科 citations were reported dead — and elided template URLs
  (`https://arxiv.org/abs/...`) lost their ellipsis to trailing-punctuation stripping.
- **Seven more dead citations repaired, and two of them were hiding a wrong fact.** The
  backlog goes 18 → 11. Chasing `sscp.cssn.cn/gywm/wsld/jmq/` found not a moved page but a
  **change of leadership**: 《中国社会科学》's editor-in-chief is now **李洪雷**, and 金民卿,
  recorded here since June, is no longer on the masthead. The pack had also fused "总编辑"
  with "第七届编委会主任"; after a handover that inference does not carry, so the second role
  is now 待核实 rather than reassigned. Chasing the VIS 2026 review-changes blog post found
  the pack claiming approved reviews are "archived as supplemental material in IEEE Xplore"
  — the live guidelines say publication is **opt-in to an OSF repository** and needs the
  consent of the authors *and every reviewer*, any one of whom can veto it. Also repointed:
  JOM's editorial team (`/editorial-team` → `/team`), JPAM's editor-in-chief and editorial
  board (APPAM restructured `/news/` to `/news-publications/` and now hands the board to
  Wiley), and EuroSys artifact evaluation (moved to the shared `sysartifacts` site). Two
  citations were **narrowed instead of repointed**, because the replacement page does not
  carry the whole claim: EuroSys' AE chair names are 待核实, and COLM's dblp cross-check was
  dropped outright — dblp has no COLM entry, so the link was never going to resolve. The
  remaining 11 are past-event pages, a closed HotCRP instance and a login-gated EasyChair
  URL; they stay in `.maintenance/DEAD-LINKS.md` rather than being repointed at something
  that merely returns 200.
- **`AAAI-Skills` re-anchored to AAAI-27**, the case issue #3 reported. The pack was 65
  days old, accurate, and entirely about AAAI-26 while the AAAI-27 cycle had opened, run
  and closed its 2026-07-28 paper deadline. Every fact re-read from the AAAI-27 pages,
  and three of them had changed rather than moved: the reproducibility checklist is now
  **uploaded separately** from the paper instead of sitting after the references; the
  page rule is stated as a 9-page maximum whose pages 8-9 are references only, with any
  ethics statement inside the 7 content pages; and **all qualified authors are now
  expected to join the reviewer pool** at a light load. The multiple-submission policy
  also grew teeth it did not have — "thin slicing" and "alternative universe" duplicates
  are named. Two AAAI-26 sources are kept deliberately, each labelled on its own row:
  AAAI-27 has published no rebuttal FAQ, and the AI-review pilot FAQ is not re-issued per
  cycle. No AAAI-27 program chairs are recorded — that page still redirects to AAAI-25's
  roster, so the names are 待核实 rather than carried forward.
- **`ICLR-Skills` re-anchored to ICLR 2027 — the one live deadline in the set.** Abstracts
  are due 2026-09-18 and papers 2026-09-25, three weeks after this pass, and ICLR's own
  CFP flags three policies as new. All three desk-reject: a **co-authorship quota** (no
  more than 20 papers, and at most one paper per author where nobody qualifies as a
  reciprocal reviewer — excess submissions are desk-rejected *at random*), a **reciprocal
  reviewing requirement** (authors on 3+ papers review 6; every paper needs an author
  registered to review 3, qualified by an accepted primary-conference paper at a listed
  venue **as of the abstract deadline**, so an accepted NeurIPS 2026 paper does not
  count), and a **mandatory AI use statement** in the paper with a required/recommended
  disclosure task list. Also recorded: OpenReview profiles created without an
  institutional email sit in moderation for up to two weeks, which makes profile creation
  a task for the weeks before the deadline rather than the day of it.
- **Six more conference packs record their edition status**, checked live rather than
  inferred. `CAV-Skills` gains the edition its previous pass could not reach — CAV has
  moved host, and CAV 2027 is the 39th edition, in the Netherlands, with a fixed calendar
  and rules still unannounced. `DAC-Skills` records that DAC 2026 has met and DAC 2027 is
  a save-the-date. `COLT-Skills` records COLT 2027 in Tokyo with every date still "TBD".
  In each case the procedural facts stay the previous edition's **deliberately** — they
  are the most recent rules the venue has actually stated, and replacing them with
  guesses would trade a dated fact for an invented one. `AISTATS`, `ICML` and `PODC` were
  probed and their current anchors are the newest edition pages those venues have
  published; `NeurIPS-Skills` is the open cycle and meets in December.
- Published recall figures in `README.md`, `README.en.md` and `journal-match.md`
  refreshed to the new held-out numbers, including `title+abstract` at **R@10 55.1%**
  over 383 test papers after the harvest was re-run against the free sources.

## [1.1.0] — 2026-08-08

Journal selection stops being a method an agent improvises over a TSV and becomes a
command with a measured error rate. Recall@10 for the true venue, from a bare title,
goes from **27.7% to 41.5%** on a newly held-out half of the gold set.

### Added

- **`tools/match_venues.py`** — step 2 of the journal-match method, executable.
  Ranks all 743 venues against a paper's title and abstract, prints where to read each
  candidate and which terms it matched, and takes `--discipline` (a **prior**, not a
  filter), `--only-discipline`, `--lane` / `--region` / `--venue-type` / `--coverage`,
  `--exclude` for venues that already rejected the paper, and `--json`.
- **`tools/match_lib.py`** — the shared retrieval layer. `match_venues.py` and
  `eval_journal_match.py` both go through it, so the published number now describes the
  code an author actually runs. Previously the harness re-implemented its own keyword
  overlap that nothing else used.
- **`scope-postings.tsv`** — a 300-term-deep inverted index behind the matcher. The
  human-readable `venue-index.tsv` keeps its 40 terms per venue; the term a given paper
  shares with its venue is usually not in the top forty, which was the single largest
  cause of misses.
- **`discipline-adjacency.tsv`** — which disciplines routinely stand in for one another,
  collapsed from the venue graph. A labour paper now reaches general economics and
  public economics automatically instead of relying on the agent to remember to widen.
- **`rt-ladder-ev` + `tools/ladder_ev.py`** — cost a submission *sequence*, not a venue:
  expected months, P(placed), P(ladder exhausted), with a sensitivity band, because
  `p_accept` is a judgement and not a measurement. The sequence is what spends a year.
- **`rt-venue-integrity`** — the escape hatch for the coverage-honesty rule. When the
  right venue is outside the index, a source-by-source verification protocol (indexing,
  publisher, editorial board, fees, retractions) with each finding attributed to a
  primary source. It ships no predatory list and applies no label; it reports checks.
- **`paper-profile.md`** — the five signals of step 1, written once and read by every
  downstream skill instead of each re-deriving them from the manuscript and quietly
  disagreeing.
- **`worked-example.md`** — one paper through all six steps with the tool output pasted
  verbatim (and checked against a fresh run). It shows the parts that matter and are
  easy to leave out of a demo: a plausible-looking candidate that is wrong on inspection
  of its matched terms, and a ladder comparison whose headline probability difference
  does not survive its own sensitivity band.
- **A dev/test split on the gold set**, assigned by a hash of each paper's title. The
  matcher's four weighting constants are tuned on `dev`; every figure in
  `eval/RESULTS.md` is computed on `test`, and both halves are printed side by side.
- **`tools/fetch_abstracts.py`** — resolves gold papers against OpenAlex and commits a
  sorted, stopword-filtered **term bag** per abstract (not the abstract), for the
  realistic `title+abstract` configuration. Network-dependent and therefore never run by
  CI; resumable, and it refuses to record a rate-limit response as "no abstract found".
- **A wrong-lane precision metric** — the share of top-10 slots given to a venue that
  publishes no empirical work, for a paper whose true venue does. Recall alone said
  nothing about the obviously wrong suggestions an author notices first.
- **Weak-evidence and coverage-gap warnings** on the matcher's output. When the leading
  candidates each rest on one or two shared words, or when nothing in the discipline you
  named scored at all, the tool says so instead of presenting a confident-looking
  ranking. The failure it names is real and visible: a paper on a cytosolic DNA *sensor*
  is otherwise offered SenSys, IPSN and PerCom.
- **A discipline-spread discount.** Inverse document frequency asks how many *venues*
  use a term; this asks how many different *subjects* do, and discounts the ones that
  are everywhere. "electrolyte" means something; "sensor", "generation" and "network"
  are words the language reuses. Worth +1.0 R@10 and −0.5 wrong-lane on the held-out
  half, and it is why "Hallmarks of Cancer: The Next Generation" stopped being routed
  by the word *generation*.

### Changed

- **Scope text now covers every skill in a pack**, not only the four "fit" skills. A
  methods skill names the designs a venue accepts and a review-process skill names what
  its referees ask about; both were being discarded. The exemplar library remains
  excluded, since it is the label source for the eval.
- **Chinese scope terms are filtered through a vocabulary discovered from the corpus**
  (recurrence + internal cohesion + boundary entropy) instead of storing every generated
  n-gram. TF-IDF ranks terms; it cannot tell a word from a fragment, and fragments
  scored *well* precisely because they were rare — `融学院主`, sliced out of `金融学院主办`,
  was indexed as though it were a term.
- **Skill slugs, URLs and submission-process boilerplate no longer reach the index.**
  `qje-identification` and `neurips-submission` are the most TF-IDF-distinctive strings
  in a pack and are worthless for matching; they were taking roughly half of every
  English pack's keyword budget. Publisher-format vocabulary (`etoc`, `blurb`, `rrid`,
  `accession`, `star methods`) went with them — neutral on recall, but it was never
  scope vocabulary, and it was most of what the Cell pack had.
- **The retrieval floor in CI rises from 22% to 36%**, measured on the held-out half.
- **The quality scorecard's toolkit size band** widens from 5–10 to 5–14 skills. The
  upper bound had been set to the toolkit's size at the time plus one, so the first
  genuine additions to the lifecycle registered as sprawl.

### Verified

- **The Prop 99 showcase case re-runs to the digit.** Seven weeks after it was
  written, classic SCM returns −18.1934 against a recorded −18.19, ASCM −18.0774
  against −18.08, SDID −17.8985 against −17.90, placebo p 0.02564 against ≈0.026.
  Stated tolerance is ±0.5; observed deviation is zero. One new obstacle recorded in
  the case's own defect section: calling `sdid` the way the recipe specifies now
  raises a type error, and `synth(method="sdid")` is the working path.

### Fixed

- **Two alias-collision bugs in the resubmission-ladder graph.** Venue aliases were
  counted with a plain substring search, so *TAR* matched inside **STAR**D and every
  radiology pack looked adjacent to The Accounting Review, while *ISS* matched inside
  **ISS**N and half the economics packs looked adjacent to ACM ISS. Latin aliases now
  require non-alphanumeric boundaries: **218 spurious edges removed** (1,725 → 1,507),
  and the share of same-discipline edges rose from 51% to 59%.
- **A configuration that covers too little of the eval split is now withheld** rather
  than published beside one that covers all of it.

### Corrections to 1.0.0

- 1.0.0 stated that "CJK keyword extraction no longer emits cross-boundary fragments in
  place of words." That was an overclaim. The change it referred to was a scoring bonus
  for longer n-grams, which makes fragments *rarer* in the ranking but cannot exclude
  them — `融学院主` was still in the shipped index. The vocabulary filter described above
  is what actually excludes them.

## [1.0.0] — 2026-08-03

First stable release. The catalogue, the audits and the cross-journal capability layer
are considered stable enough to depend on; all 299 first-party packs move from `0.1.0`
(and assorted `0.2.0` / `0.3.0`) to a single `1.0.0`.

### Added

- **Venue index covering the whole repository.** `venue-index.tsv` grew from 289 rows
  (depth packs only) to **743 venues** by indexing the discipline bundles' per-venue
  profiles, which previously existed only as prose and so could not be shortlisted or
  ranked. Cross-tier duplicates are resolved by name/acronym identity, not by slug.
- **Richer, retrieval-ready index columns.** `scope_keywords` (TF-IDF over each venue's
  own scope prose), `coverage`, `venue_type`, `profile_path`, and `ranking_labels` —
  the last recorded only where the pack's own text asserts a label, never inferred.
- **`ladder.tsv`** — a 1,725-edge venue-adjacency graph built from the venues each
  pack names as siblings or alternatives, so the resubmission ladder starts from
  evidence rather than improvisation.
- **A measurable floor under journal matching.**
  `shared-resources/journal-selection/eval/` ships a 1,738-paper gold set harvested
  from the packs' own verified exemplar libraries, plus a deterministic harness that
  scores the candidate-generation step (recall@k, MRR, per-discipline breakdown). CI
  enforces a recall floor, so an index regression fails the build.
- **`rt-venue-reframe`** — turns a manuscript framed for one venue into one framed for
  another, diffing contribution claim, introduction arc, evidence bar, house style and
  policy across both venues' packs.
- **`rt-desk-reject-risk`** — scores a draft against the target venue's *own*
  documented desk-reject triggers (456 of 743 venues publish them) and returns a
  cost-ranked fix list.
- **`CATALOG.md` + `catalog.json`** — a browsable and a machine-readable index of every
  venue with its install target, generated from the same index the matcher reads.
- **`.maintenance/FRESHNESS.md` + `tools/freshness_audit.py`** — makes the
  "grounded in official sources" claim auditable by deriving each pack's
  `last_verified` date from its own source-map prose, with age gates available in CI.

### Changed

- All first-party pack versions normalised to `1.0.0` across `plugin.json`, each pack's
  `marketplace.json`, and the root marketplace, via the new `tools/set_version.py`.
- `rt-journal-match` and `rt-workflow` updated for the wider index, the ladder, and the
  two new steps in the lifecycle.
- `tools/gen_venue_index.py` rewritten; shared classification and text-extraction logic
  factored into `tools/venue_lib.py`.

### Verified

- **The Prop 99 showcase case re-runs to the digit.** Seven weeks after it was
  written, classic SCM returns −18.1934 against a recorded −18.19, ASCM −18.0774
  against −18.08, SDID −17.8985 against −17.90, placebo p 0.02564 against ≈0.026.
  Stated tolerance is ±0.5; observed deviation is zero. One new obstacle recorded in
  the case's own defect section: calling `sdid` the way the recipe specifies now
  raises a type error, and `synth(method="sdid")` is the working path.

### Fixed

- Chinese venue display names no longer carry the `《刊名》投稿（slug）` boilerplate.
- CJK keyword extraction no longer emits cross-boundary fragments in place of words.
- Parenthetical acronyms are matched against the venue's own name before being treated
  as an alias — previously "Anesthesiology (ASA)" made every venue mentioning the
  American Sociological Association look adjacent to it.

### Notes

- The venue index still holds **no volatile facts** by design. Fees, acceptance rates,
  turnaround and page limits live in each pack's `resources/official-source-map.md` and
  are read at match time.
- `tier` remains an indicative bucket, not a ranking or a bibliometric claim.

## [0.1.0] — 2026-05 to 2026-07

Initial public development: 299 packs and 4,152 skills across 522 journals and 155+
CS/AI conferences, the nine discipline breadth bundles, the cross-journal
`Research-Toolkit-Skills`, the `shared-resources/` capability layer, and the repository
audit suite (`tools/run_checks.py`) wired into CI.
