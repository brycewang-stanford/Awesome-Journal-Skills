---
name: jmcb-internet-appendix
description: Use when deciding what belongs in the online appendix vs. the 40-page main text for a Journal of Money, Credit and Banking (JMCB) manuscript, and how to keep the core self-contained. Organizes the supporting layer and the replication path; it does not generate new analysis or prose.
---

# Online Appendix (jmcb-internet-appendix)

## When to trigger

- The main text is over the recommended 40 pages and material must move out without losing the argument
- Derivations, extra robustness, or data-construction detail are crowding the core narrative
- A referee will want to verify a step (a proof, a series construction) that does not belong in the body
- The replication/data question is unresolved and restricted bank/central-bank data complicate it
- The appendix has grown into a second paper with no map back to the main claims

## The JMCB appendix logic

JMCB explicitly **excludes the online appendix from the recommended 40-page limit** (检索于 2026-06；以官网为准), which makes the appendix the pressure valve for a tight main text — but the journal's replication heritage means the appendix is also where **verifiability lives**. The discipline is twofold: the **main text must remain self-contained** (a reader who never opens the appendix still believes the result), and the **appendix must map cleanly back** (every appendix table answers a question the main text raised). Material that is *load-bearing* for the headline belongs in the body; material that *supports or verifies* belongs in the appendix.

## What goes where

| Material | Main text | Online appendix |
|---|---|---|
| Headline IRF / table / counterfactual | ✓ | |
| The 3–4 load-bearing robustness checks | ✓ | |
| Model derivations, proofs, full FOCs | | ✓ |
| Full robustness battery (alternative orderings, windows, definitions) | summary row | ✓ full set |
| Data construction detail, variable crosswalks, M&A handling | brief note | ✓ full |
| Additional sample splits and heterogeneity cuts | key cut | ✓ rest |
| Estimation diagnostics (convergence, multi-start, Monte Carlo recovery) | one line | ✓ |

## Replication and data path

- **State the data/code plan early.** Given JMCB's archive history, referees expect a clear answer on what will be deposited.
- **Restricted data:** if bank/central-bank/supervisory data cannot be shared, request a **data exemption at submission** (检索于 2026-06；以官网为准) and document the access path (RDC, central-bank data room, register) so a replicator could in principle obtain it.
- **What the package can contain:** code, constructed-variable definitions, crosswalks, and any non-restricted inputs; state explicitly what is withheld and why.
- Keep a table-by-table map from each appendix exhibit to the main-text claim it supports.

## Structuring the appendix so referees use it

A well-organized appendix earns goodwill; a sprawling one frustrates the referee who has to mine it.

- **Mirror the main-text order.** Appendix Section B.3 should support main-text Section 3; a referee checking a claim should find its backup by section number, not by searching.
- **Self-label every exhibit.** Each appendix table/figure repeats the shock, units, sample, and specification — a referee opens the appendix out of order and must not have to flip back to decode it.
- **Lead each appendix section with one sentence** stating which main-text claim it supports and what threat it addresses.
- **Keep proofs complete but signposted** — state the proposition in the body, give the full proof in the appendix, and cross-reference both ways.

## The replication question is a JMCB litmus test

Because JMCB's own archive history is part of the field's collective memory about reproducibility, treat the data/code plan as a first-class deliverable, not an afterthought. Decide, before submission, exactly which inputs are public (Call Reports, Y-9C, FRED/ALFRED vintages) and which are restricted, and write the access path for the restricted ones (RDC, central-bank data room, credit register, with the application route). If a step in the construction is non-obvious — a splice across a regime break, an M&A crosswalk, a winsorization rule — it belongs in the appendix in enough detail to rebuild. A referee who can see exactly how to reproduce the public part and exactly how to request the restricted part is far more likely to trust the result.

## Checklist

- [ ] Main text is self-contained: the result holds for a reader who never opens the appendix
- [ ] Every appendix section maps back to a specific main-text question or claim
- [ ] Load-bearing checks stayed in the body; only supporting/verifying material moved out
- [ ] Proofs/derivations and full robustness batteries are in the appendix, summarized in text
- [ ] Data construction, crosswalks, and M&A handling documented in the appendix
- [ ] Replication plan stated; data-exemption request prepared if data are restricted
- [ ] The appendix has not become a second, unrefereed paper

## Anti-patterns

- The main text leaning on an appendix result the reader must fetch to believe the headline
- An appendix that sprawls with no map back, so referees cannot tell what each table is for
- Hiding a fragile or failed check in the appendix instead of reporting it in the body
- Treating the appendix as unlimited and dumping every specification ever run
- Silence on restricted data — no exemption request, no access path, no statement of what is withheld
- Putting the proof of a *key* result only in the appendix, leaving the body non-self-contained

## The appendix is not a hiding place

Authors sometimes use the appendix to bury a check that did not go their way. JMCB referees read the appendix precisely to find what the body omits, so a failed or weakened result discovered there reads far worse than one reported honestly in the main text. The rule: if a result *qualifies* the headline, it belongs in the body with interpretation; the appendix is for material that *supports or verifies*, never for material that quietly contradicts. Transparency in the body, depth in the appendix.

## Worked vignette (illustrative)

A monetary-transmission paper runs 18 robustness specifications and a 12-page model derivation, blowing past the 40-page recommendation. The fix: keep the headline IRF, the heterogeneity-by-capital cut, and the two checks that defuse the shock-contamination and demand objections in the body (under the page cap), and move the full derivation, the other 16 robustness runs, the RSSD merger crosswalk, and the convergence diagnostics to the online appendix — each section opening with one sentence tying it to a main-text claim. The body is now self-contained at ~38 pages, and a referee can verify any step by appendix section number. The data section states which inputs are public and documents the supervisory-panel access path for the restricted one.

## Output format

```text
【Journal】Journal of Money, Credit and Banking
【Skill】jmcb-internet-appendix
【Self-contained?】main text holds without the appendix? [Y/N]
【Moved to appendix】derivations / full robustness / data construction / extra cuts
【Stayed in body】headline + load-bearing checks
【Appendix→main map】each appendix table tied to a main-text claim? [Y/N]
【Replication plan】code/data deposit; data-exemption + access path if restricted
【Next skill】jmcb-writing-style
```
