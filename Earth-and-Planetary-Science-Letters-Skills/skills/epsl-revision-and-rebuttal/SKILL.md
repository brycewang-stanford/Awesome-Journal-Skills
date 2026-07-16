---
name: epsl-revision-and-rebuttal
description: Use when responding to an Earth and Planetary Science Letters (EPSL) revision decision. EPSL decisions are made by a subject editor on the advice of referees who often span two sub-fields, so the response must satisfy each specialist with evidence while keeping the Letter concise. It structures the revision and response letter; it does not fabricate new results.
---

# Revision & Rebuttal (epsl-revision-and-rebuttal)

An EPSL revision has a specific tension: referees ask for additions — more standards data, another
sensitivity case, an alternative-hypothesis discussion — while the letters format refuses to grow.
The craft is to satisfy every technical demand *in the supplement and deposit* while the main text
stays near the cap, and to remember that the subject editor, not the referees, makes the call.

## When to trigger

- A major/minor revision decision arrived and you are planning the response
- Referees from different sub-fields pull in different directions
- A requested addition would blow the word cap
- Drafting the summary-of-changes note to the editor

## Strategy

1. **Mine the editor's letter first.** The handling editor is a specialist and usually signals which
   referee points are decisive; resolve those with new evidence, not prose.
2. **Answer every point, point-by-point.** Quote each comment, respond beneath it, and cite the exact
   location of the change (section, figure, table, supplement item, repository DOI). Unanswered
   comments read as evasion.
3. **Route additions to the supplement.** New robustness tests, standards tables, and sensitivity
   cases go to the supplementary material and repositories; the main text absorbs only conclusions.
   State this routing openly — EPSL editors know the format's constraint and respect it.
4. **Rebut with data, concede with grace.** A disagreement backed by a new calculation or a cited
   constraint is persuasive; a disagreement backed by adjectives is not. Where the referee is right,
   fix it and say so plainly.
5. **Reconcile cross-field conflicts explicitly.** When the geochemist wants more caveats and the
   geodynamicist wants a bolder claim, choose a principled position and explain the trade-off to the
   editor — the adjudicator — rather than splitting the difference incoherently.
6. **Keep numbers synchronized.** Any re-reduction or added analysis updates the manuscript, the
   supplement, and the deposited tables together; a mismatch discovered in round two is fatal to trust.

## Triaging EPSL referee asks

| Referee ask | Default mode | What to show |
|-------------|--------------|--------------|
| "Report full standards/blank data" | concede → supplement | the per-session traceability table |
| "The feature may be a resolution artifact" | test, then rebut or scope | the recovery test at that node |
| "Consider alternative hypothesis H" | engage seriously | a discriminating calculation, or an honest scope limit |
| "Harmonize with published ages" | concede | recalculated comparison, constants stated |
| "Expand the regional context" | resist politely | letters format; one sentence + citations |
| "Tone down the global claim" | negotiate | keep the portable claim, bound its domain |

## Response-letter format

```
> [Quoted referee comment]

Response: [what changed / why we respectfully disagree, with evidence].
Change: [Section X / Fig. Y / Table S3 / EarthChem DOI updated].
```

Open with a one-paragraph summary of the major changes for the editor; group by referee; keep the
tone even toward a hostile review — the editor reads your temperament as a proxy for your rigor.

## Worked micro-example (illustrative — answering a resolution objection)

Referee 2 (seismologist, illustrative): *"The low-velocity conduit lies near the edge of ray
coverage; I suspect vertical smearing."*

```
> The low-velocity conduit lies near the edge of ray coverage; I suspect
> vertical smearing.

Response: We agree coverage thins there and have tested the concern directly.
A synthetic conduit restricted to <80 km depth, run through the identical
inversion, does not reproduce the observed anomaly at 120 km; recovery at the
key node is 78% (illustrative). The feature therefore cannot be explained as
smearing of shallow structure. New Supplementary Fig. S7 shows the full test;
the main text now states the recovery value where the conduit is first named.
Change: Section 4.2 (one sentence); Fig. S7; inversion configs updated at
Zenodo (DOI: illustrative).
```

The pattern: reproduce the referee's alternative inside your own machinery, show it fails, and spend
one main-text sentence on it — the rest lives in the supplement.

## Anti-patterns

- Growing the main text past the cap to appease referees instead of routing to the supplement
- Answering a technical objection with rhetoric or seniority
- Silently dropping a comment, or merging two comments to avoid one
- Capitulating on the portable claim, leaving a Letter with no letter-worthy result
- Updated figures whose underlying deposited tables were never refreshed

## Output format

```
【Editor's decisive points】listed + resolved with evidence
【Coverage】every comment quoted and answered? [Y/N]
【Routing】additions → supplement/deposit; main text within cap? [Y/N]
【Rebuttals】each backed by a calculation/citation? [Y/N]
【Cross-field conflicts】reconciled for the editor? [Y/N or N/A]
【Sync】manuscript = supplement = deposit? [Y/N]
【Next】resubmit via Editorial Manager
```

## Supplementary resources

- [`../../resources/external_tools.md`](../../resources/external_tools.md) — tooling for referee-requested tests
- [`../../resources/official-source-map.md`](../../resources/official-source-map.md) — decision flow and policy links
