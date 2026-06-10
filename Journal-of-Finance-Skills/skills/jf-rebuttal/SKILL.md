---
name: jf-rebuttal
description: Use when drafting the response to a The Journal of Finance (JF) revise-and-resubmit (or addressing a reject-with-comments). Structures the response letter and revision plan after the manuscript is revised.
---

# Rebuttal & Response Letter (jf-rebuttal)

## When to trigger

- A JF **revise-and-resubmit (R&R)** has arrived and you must respond
- You are deciding whether/how to answer a reject-with-encouragement
- The revision is drafted and you need to map every editor/referee point to a change

## A JF R&R is rare — treat it accordingly

With **~5% acceptance** and **~33–45% desk rejection** (afajof.org editor reports, accessed 2026-05-30), an R&R from JF is precious. The path to acceptance runs through the **handling editor** (currently the team led by **Antoinette Schoar (MIT)** — verify the masthead): the **editor's letter, not any single referee, defines what acceptance requires**. Address the editor's framing first and most fully.

## Structure

- **To the editor**: summarize the main changes and how you met the editor's synthesis of the decision.
- **Per-referee, per-point**: restate each point, then state exactly what changed and **where** (section/table/Internet Appendix), quoting revised text where useful.
- **Disagreements**: handle respectfully with evidence; never ignore a point — explain if you chose not to change something.

## JF-specific moves

- Route substantial new robustness to the **Internet Appendix** (bundled at the end of the same PDF; does not count toward 60 pages; see `jf-internet-appendix`) and say so explicitly — this matches JF norms and keeps the body lean.
- Keep the body within the **60-page limit** after revisions.
- Update **disclosure** and ensure **replication code** is ready for the Data Editor under JF's Data and Code Sharing Policy (see `jf-submission`); near acceptance the code is verified before publication.
- Use the cover-letter channel only for specifics (e.g., a code-exemption request) — JF does not want a generic letter.

## Triaging the decision letter

A JF R&R bundles the editor's letter with two or three referee reports of unequal weight. Sort every point before drafting:

| Point type                                   | Weight                  | Response discipline                                  |
|----------------------------------------------|-------------------------|------------------------------------------------------|
| Editor's synthesis / central concern         | Highest — defines acceptance | Answer first, most fully, in the body            |
| Referee point the editor echoed              | High                    | Treat as a near-condition; change, don't argue        |
| Referee point on identification/robustness   | High                    | New tests, mostly routed to the Internet Appendix     |
| Referee suggestion the editor did not endorse | Medium                  | Address respectfully; disagree with evidence if warranted |
| Minor / stylistic                            | Low                     | Fix quietly; note in the per-point table              |

The recurring JF failure mode: optimizing for the most vocal referee while underweighting the editor — who, not any referee, decides.

## Worked vignette — answering an R&R on a DID paper

*Illustrative.* The editor writes: "I am convinced the effect is real, but the staggered-DID estimator is the open question; please satisfy Referee 2." The disciplined response opens **to the editor**: "Following your central concern, we re-estimate with Callaway–Sant'Anna; the leverage effect moves from 4.2 to 3.1 pp (illustrative) and holds; Internet Appendix Table IA.VII holds the full comparison." Then a **per-referee table** logs every point with its change and location. New tables go to the IA so the body stays under 60 pages; code is staged for the Data Editor.

### Referee-pushback patterns and the JF-specific fix
| Residual pushback on resubmission                  | JF-specific fix                                                 |
|----------------------------------------------------|------------------------------------------------------------------|
| "You answered R1 but not my main point" (editor)   | Open the letter with the editor's concern, resolved in the body  |
| "The new robustness bloated the paper"             | Route it to the Internet Appendix; cite, don't inline            |
| "Where exactly did this change?"                   | Give section/table/IA location and quote the revised text        |

## Calibration anchors
- A JF R&R is **scarce** given the flagship's selectivity; treat it as the project's most valuable asset and over-invest in the editor's framing. How many rounds and what "conditional acceptance" requires vary; confirm from the editor's letter.

## Checklist

- [ ] Editor's points ranked and addressed first
- [ ] Every referee point tabulated with response + location of change
- [ ] New robustness placed in the Internet Appendix and cross-referenced
- [ ] Body still ≤60 pages after revision
- [ ] Disagreements handled with evidence, none ignored
- [ ] Replication code / disclosure updated for the Data Editor

## Anti-patterns

- Optimizing for one referee while missing the editor's central concern
- Burying or ignoring a referee point
- Adding robustness without telling referees it lives in the Internet Appendix
- Letting the revision push the body past 60 pages
- Forgetting the code-sharing obligation surfaces at acceptance

## Output format

```
【Editor's central concern + how met】...
【All referee points tabulated?】yes / no
【New robustness → Internet Appendix + cited?】yes / no
【Body ≤60 pp?】yes / no
【Code/disclosure ready for Data Editor?】yes / no
【Next step】resubmit via the AFA portal
```
