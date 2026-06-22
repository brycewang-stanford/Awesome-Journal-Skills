# Live-Check Rollout — All Remaining Lanes (2026-07 campaign)

**Mandate:** extend the humanities/social-science live-check method (verify current
Editor[s]-in-Chief + APC/submission fees → backfill source map with fact + source +
access date → de-hedge SKILL bodies → validate gates → commit) to **all 164 remaining
first-party packs** (econ, finance, accounting, management, marketing, ops/IS, poli-sci,
public-admin, psychology, sociology/demography, CS/AI, natural-science/env/ag, law,
humanities/breadth-bundles).

**Method (unchanged from the 19-pack first campaign):** WebSearch is the workhorse
(publisher sites 403 WebFetch); verify each fact against ≥2 authoritative sources
(official journal/society page + society news); never fabricate; keep honest narrowed
hedges where a value genuinely isn't publicly pinnable; correct any stale facts found
(cf. the Sociological Theory "Tavory" correction). Date stamp: **2026-06-22+**.

**Execution:** parallel verification subagents, one per disjoint cluster. Subagents
EDIT files but DO NOT git-commit (avoids `.git/index.lock` races); they report changed
files + per-pack summaries. The orchestrator runs `run_checks` + `source_map_audit` and
commits each wave centrally, with an other-lane guard on every commit.

**Coordination:** Yale-Law-Journal-Skills has an active parallel agent — handled last,
with extra care. Breadth bundles (Chinese-/English-SocialScience/NaturalScience/Humanities,
Social-Sciences-in-China) are multi-journal — no single editor; verify only that their
framing is honest, don't invent a masthead.

## Cluster backlog (≈17 clusters, 164 packs)

- **W1-A Econ-top (8):** Econometrica, Quarterly-Journal-of-Economics, Journal-of-Political-Economy, Review-of-Economic-Studies, Review-of-Economics-and-Statistics, The-Economic-Journal, Journal-of-the-European-Economic-Association, AER-Insights
- **W1-B Finance (8):** Journal-of-Finance, Journal-of-Financial-Economics, Review-of-Financial-Studies, Review-of-Finance, Journal-of-Financial-and-Quantitative-Analysis, Journal-of-Corporate-Finance, Mathematical-Finance, Financial-Management
- **W1-C Accounting (6):** Accounting-Research, Contemporary-Accounting-Research, Journal-of-Accounting-Research, Journal-of-Accounting-and-Economics, Review-of-Accounting-Studies, The-Accounting-Review
- **W1-D Political-Science (8):** American-Journal-of-Political-Science, American-Political-Science-Review, British-Journal-of-Political-Science, Comparative-Political-Studies, International-Organization, Journal-of-Politics, World-Politics, Governance-Journal
- **W2-A Econ-field (9):** AEJ-Applied-Economics, AEJ-Economic-Policy, AEJ-Macroeconomics, AEJ-Microeconomics, European-Economic-Review, International-Economic-Review, Journal-of-Development-Economics, Journal-of-International-Economics, Journal-of-Public-Economics
- **W2-B Econ-field2 (9):** Journal-of-Economic-Behavior-and-Organization, Journal-of-Economic-Geography, Journal-of-Economic-Growth, Journal-of-Environmental-Economics-and-Management, Journal-of-Health-Economics, Journal-of-Human-Resources, Journal-of-Labor-Economics, Journal-of-Monetary-Economics, Journal-of-Urban-Economics
- **W2-C Econ-theory/journals (8):** Journal-of-Economic-Theory, Journal-of-Econometrics, Econometric-Theory, The-Econometrics-Journal, Journal-of-Applied-Econometrics, Journal-of-Business-and-Economic-Statistics, Quantitative-Economics, Games-and-Economic-Behavior
- **W2-D Econ-policy/dev/misc (8):** Journal-of-Money-Credit-and-Banking, Journal-of-International-Money-and-Finance, Review-of-Economic-Dynamics, Economic-Policy, Experimental-Economics, IMF-Economic-Review, World-Bank-Economic-Review, World-Development
- **W3-A Econ-review/China-econ (9):** Annual-Review-of-Economics, RAND-Journal-of-Economics, Journal-of-Risk-and-Uncertainty, Journal-of-Economic-Literature, Journal-of-Economic-Perspectives, China-Economic-Quarterly, China-Industrial-Economics, China-Rural-Economy, Economic-Research-Journal
- **W3-B China-econ2/mgmt-CN (6):** Journal-of-World-Economy, Journal-of-Quantitative-and-Technological-Economics, Journal-of-Finance-and-Economics, Journal-of-Management-World, Journal-of-Management-Sciences-in-China, Nankai-Business-Review
- **W3-C Management/OB/strategy (8):** Academy-of-Management-Annals, Academy-of-Management-Journal, Academy-of-Management-Review, Administrative-Science-Quarterly, Organization-Science, Organization-Studies, Strategic-Management-Journal, Journal-of-Management
- **W3-D Mgmt2/entrep/HR (7):** Entrepreneurship-Theory-and-Practice, Human-Relations, Human-Resource-Management, Journal-of-Business-Venturing, Journal-of-International-Business-Studies, Journal-of-Management-Studies, Journal-of-Banking-and-Finance
- **W4-A Marketing (6):** Journal-of-Consumer-Psychology, Journal-of-Consumer-Research, Journal-of-Marketing, Journal-of-Marketing-Research, Journal-of-the-Academy-of-Marketing-Science, Marketing-Science
- **W4-B Ops/MS/IS (10):** INFORMS-Journal-on-Computing, Information-Systems-Research, Journal-of-Management-Information-Systems, Journal-of-Operations-Management, Journal-of-the-Association-for-Information-Systems, MIS-Quarterly, Management-Science, Manufacturing-and-Service-Operations-Management, Operations-Research, Production-and-Operations-Management
- **W4-C Psychology (11):** Annual-Review-of-Psychology, Cognitive-Psychology, Developmental-Psychology, Journal-of-Applied-Psychology, Journal-of-Personality-and-Social-Psychology, Perspectives-on-Psychological-Science, Psychological-Bulletin, Psychological-Review, Psychological-Science, Social-Psychology-Quarterly, Social-Forces
- **W4-D Socio/demog/comm (7):** Criminology, Demography, Journal-of-Marriage-and-Family, Population-and-Development-Review, Sociological-Studies, New-Media-and-Society, Public-Opinion-Quarterly
- **W5-A Public-admin/policy + law-econ (6):** Chinese-Public-Administration, Journal-of-Policy-Analysis-and-Management, Journal-of-Public-Administration-Research-and-Theory, Public-Administration-Review, Journal-of-Law-Economics-and-Organization, Journal-of-Law-and-Economics
- **W5-B CS/AI (7):** AAAI, AISTATS, Computer-Science-Conference, ICLR, ICML, IJCAI, NeurIPS
- **W5-C NatSci/env/ag (10):** Agricultural-Systems, Agriculture-Environment-Journal, Clinical-Medicine-Journal, Conservation-Biology, Engineering-Technology-Journal, Environmental-Science-and-Technology, Field-Crops-Research, Global-Change-Biology, Global-Environmental-Change, Chinese-Sport-Science-Journal
- **W5-D Humanities/breadth + law (7):** Critical-Inquiry, The-Art-Bulletin, English-Humanities-Journal, Chinese-SocialScience-Journal, English-SocialScience-Journal, English-NaturalScience-Journal, Social-Sciences-in-China
- **LAST (careful, parallel-agent lanes):** Harvard-Law-Review, Yale-Law-Journal (⚠ active parallel agent)

## Progress log
