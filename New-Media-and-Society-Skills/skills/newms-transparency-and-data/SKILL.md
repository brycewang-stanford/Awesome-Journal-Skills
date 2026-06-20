---
name: newms-transparency-and-data
description: Use when handling research ethics, transparency, and data sharing for a New Media & Society (NM&S) manuscript — consent and anonymization, the ethics of scraping and platform ToS, qualitative analytic transparency, and any quantitative data/code sharing. Prepares ethics and documentation; it does not over-state requirements.
---

# Research Ethics, Transparency & Data (newms-transparency-and-data)

NM&S studies people through digital media, so **research ethics for online and platform data** is
central, and **transparency** is calibrated to the method, not to a one-size mandate. NM&S follows
SAGE/COPE publishing ethics; it is not (as at some quantitative journals) a mandatory editor-verified
replication deposit. The posture: clear ethics, anonymization that actually protects people, and
documentation that lets a stranger judge your claims. **Confirm the current data-availability and
ethics policy on the live guidelines** — this skill does not assert a step the policy doesn't state.

## When to trigger

- Planning or reporting consent, anonymization, IRB/ethics approval
- Scraping or using platform data and unsure about ToS, public/private, and consent
- Documenting qualitative or computational work so the claims are credible
- A reviewer asked how others could verify or build on your analysis, or flagged an ethics concern

## Research ethics for online/platform data (the NM&S core)

- **Consent and the public/private blur.** "Publicly available" is not the same as "consented." Posts in
  a semi-private group, identifiable users, or vulnerable communities need a defensible ethics rationale,
  not just "it was online." State your IRB/ethics-board position.
- **Anonymization that protects.** Remove handles, paraphrase searchable quotes (verbatim posts can be
  reverse-searched to a user), blur faces and identifying detail in screenshots, and consider aggregation.
- **Scraping and platform ToS.** Be transparent about how data were collected (API vs. scraping), and
  acknowledge ToS and legal/ethical constraints; do not over-claim that data are freely redistributable.
- **Vulnerable users and harm.** Extra care for minors, marginalized groups, or sensitive topics;
  minimize harm in what you collect, report, and republish.

## Transparency by method (NM&S / SAGE-COPE norm)

| Data type | Typically shareable | Restricted | Credibility documentation |
|-----------|---------------------|------------|----------------------------|
| Interviews | coding scheme, anonymized excerpts | identifiable transcripts | memo trail, excerpt-to-claim table |
| Digital ethnography | analytic memos | informant identities, raw fieldnotes | positionality + IRB conditions note |
| Content / discourse corpus | codebook, sample | ToS-restricted raw posts | coding reliability + sampling frame |
| Computational / scraped | code + seeds, derived measures | raw API/ToS-restricted data | collection log, validation, model versions |
| Any quantitative survey | data + code where ethical | identifiable records | codebook + master script + pinned versions |

## Good practice (do this even though NM&S doesn't pre-verify)

- **Document provenance and construction**: a README/codebook describing sources, collection window,
  sampling, variable/category definitions, and analysis steps — so the work is checkable.
- **Quantitative/computational**: keep a master script + pinned versions + seeds; share code even when
  raw platform data cannot be redistributed (give a documented access path).
- **Qualitative**: protect informants first; share coding schemes and anonymized excerpts that support
  the claims without exposing participants.
- **Confidentiality outranks sharing**: state clearly when and why data cannot be shared, and what *can*.

## Worked micro-example (illustrative)

```
Study: digital ethnography of a courier forum + interviews + scraped public posts.
Ethics: IRB-approved; forum posts paraphrased (not verbatim) to defeat reverse-search; interview
  informants pseudonymized; minors excluded; employer unnamed.
ToS: posts collected via the platform's API within ToS; raw corpus not redistributed; codebook + derived
  counts shared instead, with an access path on request.
Transparency statement: "Coding scheme, anonymized excerpts, and analysis code are available;
  identifiable data are withheld to protect participants and per platform terms."
```

## Referee pushback → NM&S-specific fix

- *"You quote identifiable users verbatim."* → Paraphrase searchable quotes, strip handles, justify consent.
- *"'It was public' isn't an ethics argument."* → State IRB position, public/private rationale, and harm minimization.
- *"How could anyone verify the qualitative claims?"* → Provide a coding scheme and excerpt-to-claim table.

## Calibration anchors

- **Public ≠ consented.** The ethics question is harm and reasonable expectations, not mere availability.
- **Anonymize against reverse-search.** Verbatim posts and visible handles can re-identify users — paraphrase.
- **Transparency, not a replication gate.** NM&S follows SAGE/COPE ethics and data-availability norms; do
  not assert a mandatory editor-run replication check the policy doesn't state — confirm current wording.

## Anti-patterns

- Treating "publicly available" as automatic consent
- Verbatim, searchable quotes that re-identify users; unredacted screenshots
- Silence on scraping method, API/ToS constraints, or IRB/ethics review
- Promising open data that consent/ToS/confidentiality forbid
- Over-stating NM&S's policy as a mandatory verified replication deposit

## Output format

```
【Ethics】consent, IRB/ethics approval, public/private rationale handled? [Y/N]
【Anonymization】reverse-search-resistant; screenshots redacted? [Y/N]
【Data collection】API/scraping + ToS disclosed? [Y/N]
【Sharing posture】what can be shared (code/codebook/excerpts) and what cannot, and why
【Policy check】current NM&S ethics/data-availability policy confirmed? [Y/N/待核实]
【Next】newms-review-process
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — reproducibility tooling and controlled-access options
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — SAGE/COPE ethics and data-availability policy
