"""Unit tests for URL extraction in the external-link audit.

The audit is report-only, which means its whole value is its signal-to-noise ratio:
a list of "dead links" that is partly the tool's own parsing is a list nobody acts on.
Three of its 34 DEAD findings were artefacts — a Chinese-language citation truncated
at the first non-ASCII byte, and two LaTeX template URLs whose elided variable part
was stripped as trailing punctuation.

Extraction is pure and offline; the network half of the tool is not exercised here.
"""

from __future__ import annotations

import unittest

from . import context  # noqa: F401  (import for the sys.path side effect)

import external_link_audit as ela


def extract(text: str) -> list[str]:
    """The extraction half of `collect_urls`, without the filesystem walk."""
    out = []
    for match in ela.URL_RE.finditer(text):
        raw = match.group(0)
        if ela.is_elided(raw, text[match.end():match.end() + 12]):
            continue
        url = ela.normalize(raw)
        if url:
            out.append(url)
    return out


class TestNonAsciiPaths(unittest.TestCase):
    def test_a_chinese_path_survives_intact(self):
        # Cited as-is in several source maps. Truncated at `item/`, it 404s, and the
        # audit reports a live citation as dead.
        self.assertEqual(
            extract("百度百科 https://baike.baidu.com/item/中国科学：信息科学 （二手佐证）"),
            ["https://baike.baidu.com/item/中国科学：信息科学"])

    def test_a_percent_encoded_path_is_unaffected(self):
        url = "https://baike.baidu.com/item/%E7%BB%8F%E6%B5%8E%E5%AD%A6/7007846"
        self.assertEqual(extract(f"see {url} for details"), [url])

    def test_chinese_punctuation_after_a_url_is_not_part_of_it(self):
        self.assertEqual(extract("参见 https://example.org/页面，以及别处"),
                         ["https://example.org/页面"])


class TestElidedTemplates(unittest.TestCase):
    def test_an_ellipsis_url_is_not_a_citation(self):
        # `\relatedversion{Full version: https://arxiv.org/abs/...}` tells an author
        # where their own arXiv id goes.
        self.assertEqual(extract(r"\relatedversion{Full version: https://arxiv.org/abs/...}"),
                         [])

    def test_a_unicode_ellipsis_is_also_elided(self):
        self.assertEqual(extract("url = {https://www.usenix.org/presentation/…}"), [])

    def test_a_braced_placeholder_is_not_a_citation(self):
        self.assertEqual(extract("https://example.org/paper/{paper_id}"), [])

    def test_a_real_url_that_merely_ends_a_sentence_still_counts(self):
        self.assertEqual(extract("See https://example.org/page."),
                         ["https://example.org/page"])


class TestMarkdownWrappers(unittest.TestCase):
    def test_an_angle_bracketed_url_is_unwrapped(self):
        self.assertEqual(extract("<https://example.org/a>"), ["https://example.org/a"])

    def test_a_markdown_link_target_is_extracted_without_its_paren(self):
        self.assertEqual(extract("[label](https://example.org/a)"),
                         ["https://example.org/a"])

    def test_balanced_parentheses_inside_a_url_are_kept(self):
        self.assertEqual(extract("https://en.wikipedia.org/wiki/Mercury_(planet)"),
                         ["https://en.wikipedia.org/wiki/Mercury_(planet)"])

    def test_adjacent_markdown_links_do_not_bleed_into_each_other(self):
        self.assertEqual(
            extract("[a](https://example.org/a)/[b](https://example.org/b)"),
            ["https://example.org/a", "https://example.org/b"])

    def test_a_backticked_url_is_extracted_cleanly(self):
        self.assertEqual(extract("`https://example.org/a`"), ["https://example.org/a"])


class TestHostOf(unittest.TestCase):
    def test_reads_the_host(self):
        self.assertEqual(ela.host_of("https://Example.ORG/a/b"), "example.org")

    def test_a_non_url_has_no_host(self):
        self.assertEqual(ela.host_of("not a url"), "")


if __name__ == "__main__":
    unittest.main()
