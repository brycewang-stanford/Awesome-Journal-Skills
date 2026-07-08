# External Tools - EuroSys

Access date: 2026-07-08

Open these surfaces at the start of any EuroSys engagement. EuroSys policy is set per
edition *and per round*, so a URL that was authoritative for the spring round may be
superseded by the fall round's HotCRP instructions.

## Official surfaces

- EuroSys 2027 site and CFP: https://2027.eurosys.org/ and https://2027.eurosys.org/cfp.html
- Round submission portals: https://eurosys27-spring.hotcrp.com/ · https://eurosys27-fall.hotcrp.com/
- EuroSys chapter (ACM SIGOPS Europe), awards and governance: https://www.eurosys.org/
- Artifact evaluation calls (sysartifacts): https://sysartifacts.github.io/ (per-edition
  pages such as `eurosys2026/`)
- Proceedings: https://dl.acm.org/conference/eurosys (ACM DL) · https://dblp.org/db/conf/eurosys/ (index)
- Previous edition for policy diffing: https://2026.eurosys.org/ (CFP, artifact-evaluation,
  shadow-PC pages)

Note: in some environments the `*.eurosys.org` pages refuse automated fetches; the
fallback verification path (search renderings cross-checked against ACM DL, dblp, and
HotCRP) is described in `official-source-map.md`.

## Five author-side passes before an upload

1. **Gate pass** — confirm which round is live, its abstract and paper dates (AoE), and
   that the paper's EuroSys history does not trigger the same-round resubmission ban.
2. **Format pass** — rebuild with `acmart[sigplan,twocolumn,review,anonymous]`, count
   technical pages against the 12-page budget, verify the 178 x 229 mm block and column
   gap, and place the registration paper ID on page one.
3. **Identity pass** — sweep PDF metadata, acknowledgments, grant strings, self-citation
   voice, repository links, and any deployment description that names the operator.
4. **Policy pass** — dual-submission status, topics and conflicts in HotCRP, and the
   round's own instructions for rebuttal, appendices, or supplementary files (these vary;
   never assume from a previous round).
5. **Artifact-readiness pass** — even though AE runs post-acceptance, confirm the
   availability paragraph, the anonymized mirror, and the claims-to-commands map exist,
   so a notification does not start the artifact work from zero.

## Do not infer

- Do not project 2027 dates onto 2028; the two-round calendar is re-announced each edition.
- Do not assume the rebuttal format, revision-condition mechanics, camera-ready page
  allowance, or attendance rules from any prior cycle.
- Do not treat third-party deadline aggregators as authoritative — several disagreed on
  the 2027 conference end date during verification.
- If the CFP and a HotCRP instance disagree, the newer statement from the chairs controls;
  record the conflict and, if material, ask the chairs.
