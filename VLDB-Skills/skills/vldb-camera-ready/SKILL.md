---
name: vldb-camera-ready
description: Use when producing the final PVLDB version of an accepted VLDB paper, covering the volume-specific template, PDF/A compliance and font embedding, figure legibility floors, the availability paragraph and artifact URL, proceedings file naming and copyright steps, and planning presentation at the matching VLDB conference.
---

# VLDB Camera Ready

Use this after a PVLDB acceptance. Publication is journal-style and fast: the
paper enters a monthly PVLDB issue on vldb.org, usually well before the
conference where it is presented. That speed cuts both ways — production errors
go public quickly, and there is no long camera-ready season to catch them.

## Production gates

- **Template**: fetch the *current* template from the volume's formatting page
  (`vldb.org/pvldb/volumes/<N>/formatting`). Templates carry volume-specific
  headers and tags; a stale copy produces wrong running heads that only the
  proceedings chairs will catch, late.
- **PDF/A**: PVLDB has required PDF/A-compliant files (PDF/A-2 or newer in the
  Vol 16 instructions) with **every font embedded**, including fonts inside
  figures exported from plotting tools — the usual offender. Validate with a
  real PDF/A checker, not by eyeballing.
- **Figure floor**: nothing in a figure below LaTeX `scriptsize` (Vol 16 rule).
  Regenerate rather than rescale.
- **Naming and forms**: Vol 16 wanted `p[ID]-[lastname].pdf` plus a signed
  copyright form; the exact Vol 20 mechanics are 待核实 — follow the
  acceptance email over anything here.

## Availability paragraph

Supplying an artifact URL adds a highlighted availability statement to the
published paper and qualifies it for the ACM availability badge. Decide the
permanent home now:

| Artifact home | Badge-worthiness | Risk |
|---|---|---|
| Archival deposit (DOI-backed) | Strong | Least; version-frozen |
| Institutional or lab server | Weak | Link rot within years |
| Git repo, tagged release | Good | Force-push and deletion hazards |
| Git repo, default branch | Poor | Contents drift from the paper |

Tag the exact commit the paper's numbers came from; the Reproducibility
Committee may rerun it long after your cluster allocation expired.

## Final-pass checklist

```text
[ ] Current volume template, unmodified, correct running heads
[ ] Page budget still holds after final author block and acknowledgements
[ ] PDF/A validation passes; all fonts embedded (check figures separately)
[ ] No figure text below scriptsize at print size
[ ] Artifact URL live, tagged, and matching the measured version
[ ] Availability statement present; badge criteria reviewed
[ ] File naming + copyright form per the acceptance email
[ ] Camera-ready numbers identical to accepted-version numbers, or every
    change listed for the editors
```

## Conference leg

Acceptance into the volume earns presentation at the matching conference:
Vol 19 papers accepted by June 15, 2026 present at VLDB 2026 in Boston
(Aug 31 - Sep 4, 2026); Vol 20 feeds VLDB 2027 in Athens (Aug 23-27, 2027);
late acceptances roll to the next conference. Registration and the exact
presentation obligation are cycle-specific — 待核实 against the conference
site, and budget travel early since the conference lands months after
publication.

## What goes wrong here

- Silent renumbering: results edited "for polish" after acceptance without
  telling the editors — a trust violation at a venue that reruns artifacts.
- The artifact URL pointing at a moving branch, so the badge certifies code
  the paper never used.
- PDF/A failures discovered by the proceedings team on issue-assembly week.

## Output format

```text
[Production status] ready / blocked (item)
[PDF/A + fonts] pass / failures listed
[Artifact] <URL, tag, badge intent>
[Issue/volume] <expected placement>
[Conference plan] <who presents, registration state>
[Diffs vs. accepted version] none / listed and disclosed
```
