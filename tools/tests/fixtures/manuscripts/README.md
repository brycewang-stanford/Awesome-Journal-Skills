# Seeded-defect manuscript fixtures

The benchmark for the pre-submission pipeline. Each directory holds one **clean,
submission-ready synthetic manuscript** for a real venue and a manifest of **planted
defects**. Everything is fictional — papers, data, authors (first line of every
manuscript says so) — and written to the standard a strong author would submit.

| Fixture | Venue (pack) | Format | Family |
|---|---|---|---|
| `jf-corporate-did` | The Journal of Finance (`Journal-of-Finance-Skills`) | Markdown | economics/finance, staggered DiD |
| `qje-labor-iv` | The Quarterly Journal of Economics (`Quarterly-Journal-of-Economics-Skills`) | LaTeX | economics, lottery IV |
| `icml-ml-method` | ICML (`ICML-Skills`) | LaTeX | ML conference, double-blind |
| `acl-nlp` | ACL via ARR (`ACL-Skills`) | LaTeX | NLP conference, double-blind |
| `jama-rct` | JAMA (`JAMA-Skills`) | Markdown | clinical RCT |
| `erj-cn-did` | 《经济研究》 (`Economic-Research-Journal-Skills`) | Markdown, Chinese | Chinese economics, staggered DiD |

## `defects.json`

```json
{
  "id": "…", "pack": "…", "venue": "…", "format": "md|tex", "synthetic": true,
  "defects": [
    {"id": "M1", "kind": "mechanical", "check": "REF-MISSING", "find": "…", "replace": "…",
     "description": "…", "rule_basis": "…"},
    {"id": "S1", "kind": "substantive", "lens": "identification", "severity": "major",
     "find": "…", "replace": "…", "description": "…", "match_terms": ["…"]}
  ]
}
```

The edits are applied in order to the clean text to produce the seeded copy; each `find`
occurs exactly once at the moment it is applied. `kind: mechanical` defects name the
`preflight.py` check that must catch them. `kind: substantive` defects are for the referee
panel. A mechanical defect marked `"preflight": "known-miss"` carries a `miss_reason`: it is
a documented limit of the deterministic check, reported as a miss in the results and
expected to be caught by the panel instead. It is never silently dropped.

## What is asserted, and where

- `tools/tests/test_preflight.py` (CI): the clean copy raises **no FAIL**, and every
  mechanical defect that is not a known miss is caught in the seeded copy by a new finding.
- `showcase/presubmission-benchmark/` (by hand, not CI): catch rates for both stages,
  false alarms on the clean controls, and the committed panel outputs.

## Adding a fixture

Write the clean manuscript first and make `python3 tools/preflight.py <file> --venue <pack>`
report GO. Then plant defects one at a time and confirm each is caught. When a defect
cannot be caught, fix the checker if the miss is a bug. If the miss is a real limit of a
context-free check, mark it `known-miss` with the reason. Never weaken the defect to make
the test pass.
