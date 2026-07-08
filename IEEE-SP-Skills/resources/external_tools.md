# External Tools - IEEE S&P

Access date: 2026-07-08

Use these after reopening the current S&P cycle pages. S&P re-issues its CFP
every year and runs multiple cycles per symposium; dates, caps, HotCRP URLs,
and policy wording change every cycle.

**Access-method note:** direct fetches of `sp<year>.ieee-security.org` and the
per-cycle sites returned HTTP 403 in the verification environment. Read the
official pages through search-engine renderings of the exact URLs and
cross-check against dblp (`conf/sp`), IEEE Xplore, and the IEEE TC on Security
and Privacy index. Open the primary URL yourself before acting on any
deadline, cap, or policy.

## Official workflow surfaces

- S&P 2027 Call for Papers: https://sp2027.ieee-security.org/cfpapers.html
- S&P 2027 home / identity: https://sp2027.ieee-security.org/
- S&P 2027 Cycle 1 deadlines: https://cycle1.sp2027.ieee-security.org/deadlines
- S&P 2026 CFP (decision set, ethics wording, compsoc): https://sp2026.ieee-security.org/cfpapers.html
- S&P 2026 artifact evaluation: https://sp2026.ieee-security.org/cfartifacts.html
  and https://sp2026.ieee-security.org/artifact_instructions.html
- IEEE TC on Security and Privacy index: https://www.ieee-security.org/TC/SP-Index.html
- Awards / Test of Time lineage: https://www.ieee-security.org/TC/Awards.html
- Series history ("Oakland" origin): https://www.ieee-security.org/TC/sp-people-history.html
- Proceedings stream (venue authority): https://dblp.org/db/conf/sp/index.html
- Published papers: IEEE Xplore proceedings for S&P
- Submission system: HotCRP (per-cycle URL from the current CFP)

## Author-side verification passes (run before each milestone)

**Registration week**
- Every author has an ORCID; ORCID email and name match the HotCRP record
  (mismatch ⇒ desk reject).
- Title, full abstract, complete author list, and conflicts finalized — all
  freeze at registration.
- Ethics Considerations field completed with substance (what you *did*).
- SoK papers: `SoK:` title prefix **and** the SoK checkbox both set.

**Format gate before upload**
- Body ≤ 13 pages; references + appendices ≤ 5; total ≤ 18; content past
  page 13 clearly marked as appendix.
- IEEE compsoc conference-proceedings template, unmodified.
- Anonymized PDF: no author names, third-person self-citation, no
  identifying metadata.

**Security-specific anonymity sweep**
- Disclosure narrative venue-neutral (no vendor names + CVE that fingerprint
  the group).
- Artifact scripts, traces, and figures free of institutional hostnames, IPs,
  cloud project IDs, and `/home/<user>` paths.
- PDF metadata and embedded font/producer strings scrubbed.

**Ethics record (assemble months earlier)**
- Responsible-disclosure timeline: who notified, when, responses, fix status.
- IRB approval or waiver ID where human subjects / user data are involved.
- Harm-mitigation and data-minimization notes for any PII.

**Post-acceptance**
- Shepherd concern ledger from the draft meta-review.
- Dedicated ethics section (does not count against page limits at
  camera-ready).
- Artifact-evaluation registration if opting in — its calendar runs off the
  acceptance date, parallel to camera-ready.

## Do not infer

- Do not infer a later cycle's dates or a future symposium's caps from this
  snapshot.
- Do not assume the decision set, rebuttal length, ethics/REC process, page
  limits, template version, HotCRP URL, artifact badges, or generative-AI
  policy carry over unchanged — reopen the current CFP.
- If official pages disagree, the newest CFP, per-cycle deadline page, or
  direct chair communication controls; record the conflict.
