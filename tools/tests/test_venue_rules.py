"""Unit tests for `venue_rules` — the guard that keeps each machine-readable rules block a
compiled view of its source map's prose rather than a second copy that can drift.

Every test builds its own source-map text; none reads a committed pack.
"""

from __future__ import annotations

import datetime as dt
import json
import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

from venue_rules import find_block, validate

TODAY = dt.date(2026, 11, 23)

PROSE = """# Official Source Map — Example Journal

Submission rules **re-verified 2026-11-23** against the live pages.

| URL | What it verifies |
|---|---|
| https://example.org/authors | Abstract at most 150 words; double-blind review; 3–6 keywords |
"""


def doc(rules: dict, verified="2026-11-23", prose=PROSE) -> str:
    block = {"schema": "ajs-preflight-rules/1", "venue": "Example Journal", "verified": verified, "rules": rules}
    return prose + "\n## Machine-readable submission rules\n\n```json\n" + json.dumps(block) + "\n```\n"


def errors(text: str) -> list[str]:
    block, prose, err = find_block(text)
    assert err is None and block is not None
    return validate("Example-Skills", block, prose, TODAY)


SRC = "https://example.org/authors"


class TestValidate(unittest.TestCase):
    def test_valid_block(self):
        rules = {"abstract_words_max": {"value": 150, "source": SRC},
                 "review_mode": {"value": "double-blind", "source": SRC},
                 "keywords_min": {"value": 3, "source": SRC},
                 "required_statements": {"value": ["data_availability"], "source": SRC},
                 "apc": {"value": None, "note": "not stated"}}
        self.assertEqual(errors(doc(rules)), [])

    def test_number_must_appear_in_prose(self):
        errs = errors(doc({"abstract_words_max": {"value": 250, "source": SRC}}))
        self.assertTrue(any("does not appear in the prose" in e for e in errs), errs)

    def test_source_must_be_cited_in_prose(self):
        errs = errors(doc({"review_mode": {"value": "double-blind", "source": "https://other.org/x"}}))
        self.assertTrue(any("not cited" in e for e in errs), errs)

    def test_bold_url_in_prose_counts_as_cited(self):
        prose = PROSE.replace("| https://example.org/authors |", "| **https://example.org/authors** |")
        self.assertEqual(errors(doc({"review_mode": {"value": "double-blind", "source": SRC}}, prose=prose)), [])

    def test_verified_date_must_match_prose(self):
        errs = errors(doc({"review_mode": {"value": "double-blind", "source": SRC}}, verified="2026-11-30"))
        self.assertTrue(any("'verified'" in e for e in errs), errs)

    def test_unknown_key_and_bad_enum(self):
        errs = errors(doc({"page_max": {"value": 8, "source": SRC},
                           "review_mode": {"value": "blind", "source": SRC}}))
        self.assertTrue(any("unknown key" in e for e in errs))
        self.assertTrue(any("not in" in e for e in errs))

    def test_unknown_statement(self):
        errs = errors(doc({"required_statements": {"value": ["coi"], "source": SRC}}))
        self.assertTrue(any("unknown statement" in e for e in errs), errs)

    def test_soft_only_on_numeric(self):
        ok = errors(doc({"abstract_words_max": {"value": 150, "source": SRC, "soft": True}}))
        bad = errors(doc({"review_mode": {"value": "double-blind", "source": SRC, "soft": True}}))
        self.assertEqual(ok, [])
        self.assertTrue(any("'soft'" in e for e in bad), bad)

    def test_invalid_json_is_reported(self):
        text = PROSE + "\n```json\n{\"schema\": \"ajs-preflight-rules/1\", oops}\n```\n"
        block, _, err = find_block(text)
        self.assertIsNone(block)
        self.assertIn("not valid JSON", err)


if __name__ == "__main__":
    unittest.main()
