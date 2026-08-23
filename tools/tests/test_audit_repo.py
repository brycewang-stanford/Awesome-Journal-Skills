"""Unit tests for the two `audit_repo` checks that guard the front page.

Both exist because the front page is maintained by hand and nothing was watching it.

**Hero assets.** The two READMEs open with a banner. In August 2026 `assets/banner-en.png` was
overwritten by a screenshot of a bot-check interstitial — captured at exactly the
banner's 2400x860, so every dimension still agreed — and nothing in the repository
noticed: the file existed, the Markdown link resolved, the audit passed. The only
signal was the file size, because a mostly-white error page compresses to a tenth of
what the artwork does.

**README parity.** `README.en.md` exists so a reader without Chinese sees the same
catalogue — the same 1,017 pack entries, the same cover wall. The two files are 2,250
hand-maintained lines each, and a card added to one and not the other is invisible in
review. They are in parity today; the check is what keeps them there.

These tests build PNGs and READMEs from scratch rather than reading the committed ones,
so a test failure means the *rule* changed.
"""

from __future__ import annotations

import struct
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest import mock

from . import context  # noqa: F401  (import for the sys.path side effect)

import audit_repo


def png(width: int, height: int, *, pixel: bytes = b"\x00\x00\x00", pad: int = 0) -> bytes:
    """A real, decodable PNG of the given size — no image library involved."""
    def chunk(kind: bytes, payload: bytes) -> bytes:
        return (struct.pack(">I", len(payload)) + kind + payload
                + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)   # 8-bit truecolour
    raw = b"".join(b"\x00" + pixel * width for _ in range(height))
    parts = [audit_repo.PNG_MAGIC, chunk(b"IHDR", ihdr),
             chunk(b"IDAT", zlib.compress(raw))]
    if pad:
        # A private chunk, so a "make this file bigger" fixture stays a valid PNG.
        parts.append(chunk(b"prVt", b"\x00" * pad))
    parts.append(chunk(b"IEND", b""))
    return b"".join(parts)


class TestPngSize(unittest.TestCase):
    def test_reads_the_dimensions_from_the_header(self):
        self.assertEqual(audit_repo.png_size(png(2400, 860)), (2400, 860))

    def test_a_non_png_is_not_a_png(self):
        self.assertIsNone(audit_repo.png_size(b"\xff\xd8\xff\xe0 JPEG"))
        self.assertIsNone(audit_repo.png_size(b"<!doctype html>"))

    def test_a_truncated_file_is_not_a_png(self):
        self.assertIsNone(audit_repo.png_size(audit_repo.PNG_MAGIC + b"\x00" * 4))


class TestHeroAssets(unittest.TestCase):
    NAME = "assets/banner-en.png"
    WIDTH, HEIGHT, FLOOR = 2400, 860, 250_000

    def run_check(self, data: bytes | None) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            if data is not None:
                (root / "assets").mkdir()
                (root / self.NAME).write_bytes(data)
            errors: list[str] = []
            with mock.patch.object(audit_repo, "ROOT", root), \
                 mock.patch.object(audit_repo, "HERO_ASSETS",
                                   [(self.NAME, self.WIDTH, self.HEIGHT, self.FLOOR)]):
                audit_repo.check_hero_assets(errors)
            return errors

    def test_the_real_artwork_passes(self):
        self.assertEqual(self.run_check(png(self.WIDTH, self.HEIGHT, pad=self.FLOOR)), [])

    def test_a_correctly_sized_but_near_empty_capture_fails(self):
        """The actual incident: right dimensions, a tenth of the bytes."""
        errors = self.run_check(png(self.WIDTH, self.HEIGHT))
        self.assertEqual(len(errors), 1)
        self.assertIn("below the", errors[0])

    def test_a_resized_banner_fails(self):
        errors = self.run_check(png(1200, 430, pad=self.FLOOR))
        self.assertEqual(len(errors), 1)
        self.assertIn("expected 2400x860", errors[0])

    def test_a_file_that_is_not_an_image_fails(self):
        errors = self.run_check(b"<html>Performing security verification</html>")
        self.assertEqual(len(errors), 1)
        self.assertIn("not a PNG", errors[0])

    def test_a_missing_asset_fails(self):
        errors = self.run_check(None)
        self.assertEqual(len(errors), 1)
        self.assertIn("missing", errors[0])

    def test_every_declared_hero_asset_exists_and_passes_today(self):
        # The guard is only worth having if the committed artwork satisfies it, and
        # this is what turns a stale HERO_ASSETS entry into a failing build.
        errors: list[str] = []
        audit_repo.check_hero_assets(errors)
        self.assertEqual(errors, [])


class TestReadmeParity(unittest.TestCase):
    """The English README must present the same catalogue as the Chinese one."""

    ZH = ('<a href="Journal-of-Finance-Skills/"><img src="assets/covers/jof.png"></a>\n'
          '<a href="Econometrica-Skills/"><img src="assets/covers/ecta.png"></a>\n'
          '<img src="assets/banner-zh.png">\n')
    EN = ('<a href="Journal-of-Finance-Skills/"><img src="assets/covers/jof.png"></a>\n'
          '<a href="Econometrica-Skills/"><img src="assets/covers/ecta.png"></a>\n'
          '<img src="assets/banner-en.png">\n')

    def run_check(self, zh: str, en: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text(zh, encoding="utf-8")
            (root / "README.en.md").write_text(en, encoding="utf-8")
            errors: list[str] = []
            with mock.patch.object(audit_repo, "ROOT", root):
                audit_repo.check_readme_parity(errors)
            return errors

    def test_matching_catalogues_pass(self):
        self.assertEqual(self.run_check(self.ZH, self.EN), [])

    def test_the_language_specific_banner_is_not_a_difference(self):
        # The one asset that is *supposed* to differ.
        self.assertNotIn("banner", " ".join(self.run_check(self.ZH, self.EN)))

    def test_a_pack_card_added_to_only_one_readme_fails(self):
        zh = self.ZH + '<a href="Management-Science-Skills/">new</a>\n'
        errors = self.run_check(zh, self.EN)
        self.assertEqual(len(errors), 1)
        self.assertIn("README.en.md is missing", errors[0])
        self.assertIn("Management-Science-Skills", errors[0])

    def test_the_check_is_symmetric(self):
        en = self.EN + '<a href="Management-Science-Skills/">new</a>\n'
        errors = self.run_check(self.ZH, en)
        self.assertEqual(len(errors), 1)
        self.assertIn("README.md is missing", errors[0])

    def test_a_cover_image_added_to_only_one_readme_fails(self):
        zh = self.ZH + '<img src="assets/covers/new.png">\n'
        errors = self.run_check(zh, self.EN)
        self.assertTrue(any("asset" in e for e in errors))

    def test_markdown_style_links_count_too(self):
        # Both link syntaxes appear in these files.
        zh = self.ZH + "[Management Science](Management-Science-Skills/)\n"
        self.assertEqual(len(self.run_check(zh, self.EN)), 1)

    def test_the_committed_readmes_are_in_parity(self):
        errors: list[str] = []
        audit_repo.check_readme_parity(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
