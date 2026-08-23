"""Unit tests for the hero-asset guard in `audit_repo`.

The two READMEs open with a banner. In August 2026 `assets/banner-en.png` was
overwritten by a screenshot of a bot-check interstitial — captured at exactly the
banner's 2400x860, so every dimension still agreed — and nothing in the repository
noticed: the file existed, the Markdown link resolved, the audit passed. The only
signal was the file size, because a mostly-white error page compresses to a tenth of
what the artwork does.

These tests hold the guard that would have caught it. They build PNGs from bytes rather
than reading the committed artwork, so a test failure means the *rule* changed.
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


if __name__ == "__main__":
    unittest.main()
