# Depth-pack polishing methodology (quality bar)

**Problem (verified):** the standalone depth packs are find-replace clones of one master template.
`qje-identification` ≡ `jpe-identification` after name-normalization (empty diff). They give generic
top-5 advice with zero venue-specific facts. Each pack must become genuinely venue-specific.

## Per-skill rubric — every SKILL.md must add real, checkable facts
1. **Numbers**: word/figure/reference limits, abstract format, acceptance rate, typical timelines, fees.
2. **Named systems**: actual submission portal (e.g. QJE = Editorial Express), reporting/replication
   checklists, required statements, reference style, the venue's own jargon.
3. **Desk-reject triggers** specific to this venue.
4. **Editorial culture**: blinding policy, format-free option, transfer cascade, referee norms, R&R style,
   named current editors/co-editors (with date), data-editor / replication policy.
5. **Exemplars**: >=1 named landmark/representative paper to anchor framing.
6. **No cross-contamination / no clone twins**: a sibling-journal reader must NOT be able to swap the
   journal name and have it read correctly. Each pack distinct from siblings.

## Process per pack
1. Claim in CLAIMS.md; `git status <pack>` first (skip if the other agent has pending edits there).
2. Research the venue (web): official author guidelines + scope + editorial board + recent issues.
3. Rewrite each SKILL.md keeping folder names + frontmatter keys; replace generic prose with specifics.
   Bump plugin.json version 0.1.0 -> 0.2.0; fix clone-generic descriptions.
4. Add `resources/official-source-map.md` listing the official URLs used (verified).
5. Leave edits **uncommitted** for the user's final 验收 (do not push). Log in PROGRESS.md.

## Invariants (do not break)
- Keep skill **count** and folder **names** stable (README claims 844 skills; counts must not drift).
- Keep YAML frontmatter keys (`name`, `description`).
- Keep `## Related skills` cross-links valid.
- Never invent editor names, fees, or limits — flag UNVERIFIED instead.
