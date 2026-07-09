---
name: mobicom-related-work
description: Use when building or auditing the related-work of a MobiCom paper — sweeping the SIGMOBILE and networking literature lanes, proving each citation's venue on dblp/ACM DL against the INFOCOM/SIGCOMM/NSDI misattribution traps, positioning against the current rolling-cohort cohort, and self-citing without breaking double-blind.
---

# MobiCom Related Work

Related work at MobiCom does two jobs: it proves you know the wireless/mobile-networking
literature, and it draws the exact line between your mechanism and the nearest prior one.
Because the field's canon is spread across ACM and IEEE venues, half the work is getting the
*venue attribution right* — the most-cited wireless papers are the most-misfiled.

## The literature lanes to sweep

Do not sweep "wireless" as one blob. Cover the lanes that a MobiCom reviewer occupies:

- **MobiCom's own recent editions** — the two most recent programs, including the rolling
  cohort your round competes with; positioning against year-old work reads as stale.
- **Sibling SIGMOBILE venues** — MobiSys, SenSys, IMWUT/UbiComp, HotMobile — where an
  adjacent mechanism may already live.
- **Broad networking** — SIGCOMM, NSDI, INFOCOM — for the protocol/measurement lineage.
- **PHY/communications** — where a coding or modulation primitive you build on originates.
- **The specific mechanism's line** — the direct ancestors of your technique, traced to
  their origin paper, not a recent paper that cites it.

## Prove the venue before you cite

A conference name in a slide deck or a re-hosted PDF is not proof. Verify each load-bearing
citation on dblp and the ACM DL, and watch the traps:

| Trap | Reality | Guard |
|---|---|---|
| RADAR (RF localization) as "MobiCom" | IEEE INFOCOM 2000 | check dblp before attributing |
| "XORs in the Air" as "MobiCom" | ACM SIGCOMM 2006 | wireless topic ≠ MobiCom venue |
| WiSee *demo* as the WiSee paper | demo is SIGCOMM '13; paper is MobiCom '13 | cite the MobiCom DOI |
| ArrayTrack as "MobiCom" | USENIX NSDI 2013 | Test-of-Time mention ≠ MobiCom publication |

The full verified/omitted list and the venue-verification recipe are in
[`../../resources/exemplars/library.md`](../../resources/exemplars/library.md).

```bash
# Sanity-check a citation's venue and year against dblp (read via renderings if 403)
# dblp.org/db/conf/mobicom/  ->  confirm edition number matches the claimed year
# For each load-bearing cite, record: authors | title | venue | year | pages
```

## Position, do not enumerate

A list of summaries is not related work. For each closest prior mechanism, state the
**technical delta** in one sentence: what condition it assumed that you relax, what evidence
it lacked that you provide, what regime it did not reach. MobiCom reviewers — often the
authors of the work you cite — will notice a missing or mischaracterized neighbor
immediately.

- Group by **mechanism**, not by year, so the reader sees the design space and your place in
  it.
- Give the **nearest competitor its strongest form**; beating a weak version of prior work
  is not a contribution (`mobicom-experiments` baselines).
- If a concurrent paper overlaps, address it honestly rather than omitting it.

## Self-citation under double-blind

MobiCom review is double-blind. Cite your own prior work in the **third person** ("Prior
work [12] showed..."), never "our previous paper." Do not drop a needed citation to preserve
anonymity — a conspicuous gap where the obvious reference should be is itself a
de-anonymizing tell. For a concurrent submission of your own, refer to it neutrally without
identifying the authorship (`mobicom-submission`).

## Audit checklist

- [ ] Two most recent MobiCom editions and the rolling cohort covered.
- [ ] Sibling-venue neighbors (MobiSys/SenSys/SIGCOMM/NSDI/INFOCOM) addressed, not ignored.
- [ ] Every load-bearing citation's venue verified on dblp/ACM DL.
- [ ] No misattribution-trap paper credited to MobiCom.
- [ ] Each closest prior mechanism has a one-sentence technical delta.
- [ ] Self-citations in third person; no anonymity-driven omission.

## Output format

```text
[Lane coverage] MobiCom-recent / SIGMOBILE-siblings / broad-net / PHY / mechanism-line — each y/n
[Venue check] citations flagged for dblp/ACM DL verification
[Traps] any misattributed paper found -> corrected venue
[Deltas] closest prior mechanisms missing a stated technical delta
[Blind safety] self-cites / concurrent-sub references audited
```
