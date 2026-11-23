"""Unit tests for `preflight` — the deterministic stage 0 of submission readiness.

Two layers:

* Small inline manuscripts, one per input format, each with a known set of planted
  defects. These pin the parser for every format and every check ID, and they build
  their own fixtures so they cannot pass by agreeing with a wrong committed file.
* The seeded-defect benchmark under ``fixtures/manuscripts/``: realistic synthetic
  manuscripts plus a manifest of find/replace edits. The contract is the one the
  benchmark reports (``showcase/presubmission-benchmark/RESULTS.md``): the clean copy
  raises no FAIL, and every planted *mechanical* defect is caught in the seeded copy
  by a finding that the clean copy did not already have. Substantive defects are for
  the referee panel and are not asserted here.
"""

from __future__ import annotations

import io
import json
import shutil
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout
from pathlib import Path

from . import context  # noqa: F401  (import for the sys.path side effect)

import preflight
from preflight import Checker, load, resolve_venue, verdict

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "manuscripts"

RULES = {
    "abstract_words_max": {"value": 30},
    "review_mode": {"value": "double-blind"},
    "required_statements": {"value": ["data_availability", "jel_codes", "keywords"]},
    "keywords_max": {"value": 5},
}

CLEAN_MD = """# Credit Shocks and Firm Leverage

Anonymous Authors

## Abstract

We study a staggered regulatory shock and find that leverage falls by 4.2 percentage points, about 12% of the sample mean.

**Keywords:** leverage; regulation; banks

**JEL Codes:** G32, G21

## 1. Introduction

Prior work (Smith and Jones, 2019; Lee et al., 2021) studies credit supply. Rajan (2005) argues otherwise. We find an effect of 4.2 percentage points (Table 1). Figure 1 shows the event study, and Table 2 shows robustness.

## 2. Results

**Table 1: Main results**

| | (1) |
|---|---|
| Treated | -0.042 |
| Observations | 12,000 |

*Notes:* Standard errors clustered by state in parentheses.

**Table 2: Robustness**

| | (1) |
|---|---|
| Treated | -0.040 |

*Notes:* Placebo cohorts only.

Mean leverage is 0.35, so the effect is 12% of the mean. Code is available at https://anonymous.4open.science/r/credit-1234.

**Figure 1: Event study**

## Data Availability Statement

All data come from public filings.

## References

Lee, A., B. Kim, and C. Park (2021). Credit and firms. Journal of Examples 1, 1-20.

Rajan, R. (2005). Has financial development made the world riskier? Example Review 9, 1-2.

Smith, J. and K. Jones (2019). Banks. Example Review 2, 3-4.
"""

SEEDS = [
    ("Anonymous Authors", "Jane Doe, Example University, jane@example.edu", "ANON-AUTHOR"),
    ("about 12% of the sample mean.", "about 12% of the sample mean, a large effect that survives every robustness check we could think of in this setting.", "LEN-ABSTRACT"),
    ("Rajan (2005) argues otherwise.", "Rajan (2005) argues otherwise, and Zingales (2015) disagrees.", "REF-MISSING"),
    ("Smith, J. and K. Jones (2019). Banks. Example Review 2, 3-4.",
     "Smith, J. and K. Jones (2019). Banks. Example Review 2, 3-4.\n\nZed, Q. (2018). Uncited. Journal of Nothing 1, 1.", "REF-UNCITED"),
    ("**Table 2: Robustness**", "**Table 3: Robustness**", "EXH-NUMBERING"),
    ("Figure 1 shows the event study, and", "The event study is informative, and", "EXH-UNREFERENCED"),
    ("*Notes:* Standard errors clustered by state in parentheses.", "*Notes:* Fixed effects included.", "EXH-SE-NOTE"),
    ("We find an effect of 4.2 percentage points", "We find an effect of 5.1 percentage points", "NUM-MISMATCH"),
    ("studies credit supply.", "studies credit supply. TODO: add the 2024 papers.", "LEFTOVER-MARKER"),
    ("## Data Availability Statement\n\nAll data come from public filings.\n\n", "", "STMT-MISSING"),
    ("**JEL Codes:** G32, G21\n\n", "", "STMT-MISSING"),
    ("Code is available at https://anonymous.4open.science/r/credit-1234.",
     "Our code is available at https://github.com/janedoe/credit.", "ANON-URL"),
    ("Rajan (2005) argues otherwise.", "Rajan (2005) argues otherwise. In our previous work (Doe, 2023) we built this panel.",
     "ANON-SELFCITE"),
    ("## References", "## Acknowledgments\n\nWe thank seminar participants. Grant No. NSF-12345.\n\n## References", "ANON-ACK"),
]


def run(path: Path, rules: dict, blind=None) -> Checker:
    doc = load(path, None)
    ck = Checker(doc, rules, "test", blind, online=False)
    ck.run()
    return ck


def checks(ck: Checker, severities=("FAIL", "FLAG")) -> list[str]:
    return [f.check for f in ck.findings if f.severity in severities]


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def write(self, text: str, name="paper.md") -> Path:
        p = self.tmp / name
        p.write_text(text, encoding="utf-8")
        return p

    def test_clean_manuscript_is_go(self):
        ck = run(self.write(CLEAN_MD), RULES)
        self.assertEqual(checks(ck), [], [f.message for f in ck.findings])
        self.assertEqual(verdict(ck.findings), "GO")

    def test_each_seed_is_caught_alone(self):
        for find, replace, check in SEEDS:
            with self.subTest(check=check, find=find[:30]):
                self.assertEqual(CLEAN_MD.count(find), 1)
                ck = run(self.write(CLEAN_MD.replace(find, replace)), RULES)
                self.assertIn(check, checks(ck), [f.message for f in ck.findings])

    def test_missing_statement_names_the_statement(self):
        text = CLEAN_MD.replace("**JEL Codes:** G32, G21\n\n", "")
        ck = run(self.write(text), RULES)
        self.assertEqual([f.statement for f in ck.findings if f.check == "STMT-MISSING"], ["jel_codes"])

    def test_single_blind_skips_anonymity(self):
        text = CLEAN_MD.replace("Anonymous Authors", "Jane Doe, Example University")
        rules = dict(RULES, review_mode={"value": "single-blind"})
        self.assertNotIn("ANON-AUTHOR", checks(run(self.write(text), rules)))

    def test_unknown_review_mode_is_reported_not_passed(self):
        rules = {k: v for k, v in RULES.items() if k != "review_mode"}
        ck = run(self.write(CLEAN_MD), rules)
        self.assertTrue(any("anonymization" in n for n in ck.not_checked))

    def test_derived_numbers_are_not_mismatches(self):
        # 3.4 = 71.2 - 67.8, a difference no table prints.
        text = CLEAN_MD.replace("We find an effect of 4.2 percentage points (Table 1).",
                                "We find an effect of 4.2 percentage points (Table 1), 3.4 points above ERM.")
        text = text.replace("| Treated | -0.040 |", "| Ours | 71.2 |\n| ERM | 67.8 |")
        self.assertNotIn("NUM-MISMATCH", checks(run(self.write(text), RULES)))

    def test_numbers_attributed_to_other_papers_are_skipped(self):
        text = CLEAN_MD.replace("Rajan (2005) argues otherwise.", "Rajan (2005) finds 7.7 percent.")
        self.assertNotIn("NUM-MISMATCH", checks(run(self.write(text), RULES)))

    def test_chinese_author_year_citations(self):
        text = """# 数字金融与融资约束

匿名作者

## 摘要

本文发现融资约束下降了3.5个百分点。

**关键词：** 数字金融；融资约束；中小企业

## 一、引言

已有研究（张三和李四，2019；王五等，2021）讨论了这一问题，赵六（2020）持不同观点。

## 参考文献

张三，李四. 2019. 数字金融研究. 经济研究, 1: 1-10.

王五，钱七，孙八. 2021. 融资约束. 管理世界, 2: 3-4.
"""
        ck = run(self.write(text), {"review_mode": {"value": "double-blind"}})
        missing = [f.message for f in ck.findings if f.check == "REF-MISSING"]
        self.assertEqual(len(missing), 1)
        self.assertIn("赵六", missing[0])


class TestVenueSpecificRules(unittest.TestCase):
    """Rules that came out of running the pipeline on a real preprint (arXiv:2611.21070)."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.path = self.tmp / "paper.md"
        self.path.write_text(CLEAN_MD, encoding="utf-8")

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_per_exhibit_word_deduction_and_cap(self):
        # 2 tables + 1 figure = 3 exhibits; cap 60 - 3 x 10 = 30 words, the body is longer.
        ck = run(self.path, {"main_text_words_max": {"value": 60}, "words_per_exhibit": {"value": 10},
                             "exhibits_max": {"value": 2}})
        self.assertEqual(ck.stats["main_exhibits"], 3)
        self.assertEqual(ck.stats["word_cap_after_exhibits"], 30)
        self.assertIn("LEN-EXHIBITS", checks(ck))
        self.assertIn("LEN-WORDS", checks(ck))

    def test_significance_stars(self):
        self.path.write_text(CLEAN_MD.replace("| Treated | -0.042 |", "| Treated | -0.042*** |"), encoding="utf-8")
        self.assertIn("EXH-STARS", checks(run(self.path, {"significance_stars": {"value": "prohibited"}})))
        self.assertNotIn("EXH-STARS", checks(run(self.path, {})))

    def test_separate_upload_is_a_reminder_not_a_fail(self):
        ck = run(self.path, {"required_statements": {"value": []},
                             "separate_upload_statements": {"value": ["disclosure_statement"]}})
        self.assertNotIn("STMT-MISSING", checks(ck))
        self.assertTrue(any("separate upload" in r for r in ck.reminders))

    def test_untested_rule_is_reported_not_passed(self):
        ck = run(self.path, {"references_max": {"value": 40}})
        self.assertTrue(any("references_max" in n for n in ck.not_checked))

    def test_grey_literature_is_not_a_crossref_miss(self):
        ck = run(self.path, {})
        ck.findings.clear()
        text = CLEAN_MD.replace("Example Review 9, 1-2.", "NBER Working Paper 11728.")
        self.path.write_text(text, encoding="utf-8")
        doc = load(self.path, None)
        grey = [r for r in preflight.reference_entries(doc, preflight.sections(doc)) if "Working Paper" in r.text]
        self.assertEqual(len(grey), 1)


class TestOtherFormats(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_tex(self):
        tex = r"""\documentclass{article}
\title{Robust Training}
\author{John Roe \\ \texttt{roe@example.edu}}
\begin{document}
\begin{abstract}
We improve accuracy by 3.4 points.
\end{abstract}
\section{Introduction}
Shift is common \citep{koh2021}. We gain 3.4 points (Table~\ref{tab:main}); see Figure~\ref{fig:none}.
\todo{more}
\begin{table}\caption{Main}\label{tab:main}
\begin{tabular}{lc} Ours & 71.2 \\ ERM & 67.8 \\ \end{tabular}\end{table}
\begin{table}\caption{Ablation}\label{tab:abl}
\begin{tabular}{lc} A & 70.0 \\ \end{tabular}\end{table}
\begin{thebibliography}{9}
\bibitem{koh2021} Koh et al. 2021.
\bibitem{unused} Unused 2020.
\end{thebibliography}
\end{document}
"""
        p = self.tmp / "p.tex"
        p.write_text(tex, encoding="utf-8")
        got = checks(run(p, {}, blind=True))
        for want in ("ANON-AUTHOR", "LEFTOVER-MARKER", "REF-UNCITED", "EXH-UNREFERENCED"):
            self.assertIn(want, got)
        self.assertNotIn("NUM-MISMATCH", got)
        self.assertNotIn("REF-MISSING", got)

    def test_docx_tracked_changes_comments_and_metadata(self):
        W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

        def para(text, style=""):
            ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
            return f"<w:p>{ppr}<w:r><w:t>{text}</w:t></w:r></w:p>"
        body = "".join([
            para("A Paper", "Title"), para("Jane Doe"), para("Abstract", "Heading1"),
            para("We find 2.5 percent."), para("Results", "Heading1"),
            para("The effect is 2.5 percent."),
            '<w:p><w:ins w:id="1" w:author="x"><w:r><w:t>added</w:t></w:r></w:ins></w:p>',
        ])
        p = self.tmp / "p.docx"
        with zipfile.ZipFile(p, "w") as z:
            z.writestr("word/document.xml", f'<w:document {W}><w:body>{body}</w:body></w:document>')
            z.writestr("word/comments.xml", f'<w:comments {W}><w:comment w:id="0"><w:p><w:r><w:t>fix this</w:t>'
                                            '</w:r></w:p></w:comment></w:comments>')
            z.writestr("docProps/core.xml", '<cp:coreProperties xmlns:cp="x" xmlns:dc="y"><dc:creator>Jane Doe'
                                            '</dc:creator></cp:coreProperties>')
        ck = run(p, {}, blind=True)
        got = checks(ck)
        self.assertIn("LEFTOVER-TRACKED", got)
        self.assertIn("ANON-META", got)
        self.assertIn("ANON-AUTHOR", got)
        self.assertNotIn("NUM-MISMATCH", got)

    def test_plain_text_rebuilds_wrapped_paragraphs(self):
        txt = ("A Title\nAnonymous\n\nAbstract\nWe find 1.5 percent.\n\n1 Introduction\n"
               "As argued by Rajan\n(2005), this matters.\n\nReferences\n"
               "Smith, J. (2019). A paper.\n")
        p = self.tmp / "p.txt"
        p.write_text(txt, encoding="utf-8")
        ck = run(p, {})
        msgs = [f.message for f in ck.findings if f.check == "REF-MISSING"]
        self.assertTrue(any("Rajan" in m for m in msgs), msgs)


class TestVenueResolution(unittest.TestCase):
    DB = {"Journal-of-Finance-Skills": {"venue": "The Journal of Finance",
                                        "aliases": ["The Journal of Finance", "Journal-of-Finance-Skills", "jf-skills",
                                                    "journal-of-finance"]}}

    def test_aliases(self):
        for name in ("Journal of Finance", "the journal of finance", "jf-skills", "Journal-of-Finance-Skills"):
            with self.subTest(name=name):
                self.assertEqual(resolve_venue(self.DB, name)[0], "Journal-of-Finance-Skills")

    def test_unknown(self):
        self.assertIsNone(resolve_venue(self.DB, "Nonexistent Review"))

    def test_cli_exit_codes(self):
        tmp = Path(tempfile.mkdtemp())
        try:
            p = tmp / "p.md"
            p.write_text(CLEAN_MD.replace("studies credit supply.", "studies credit supply. TODO"), encoding="utf-8")
            block = tmp / "rules.json"
            block.write_text(json.dumps({"schema": "ajs-preflight-rules/1", "venue": "T", "verified": "2026-01-01",
                                         "rules": RULES}), encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(preflight.main([str(p), "--rules-block", str(block)]), 1)
                self.assertEqual(preflight.main([str(tmp / "missing.md")]), 2)
        finally:
            shutil.rmtree(tmp)


def apply_manifest(clean: str, manifest: dict) -> str:
    text = clean
    for d in manifest["defects"]:
        if text.count(d["find"]) != 1:
            raise AssertionError(f"{manifest['id']} {d['id']}: find occurs {text.count(d['find'])} times")
        text = text.replace(d["find"], d["replace"])
    return text


class TestBenchmarkFixtures(unittest.TestCase):
    """Clean copy: no FAIL. Seeded copy: every mechanical defect caught."""

    def fixtures(self):
        return sorted(p for p in FIXTURES.iterdir() if (p / "defects.json").exists()) if FIXTURES.exists() else []

    def test_fixtures_present(self):
        self.assertGreaterEqual(len(self.fixtures()), 6)

    def test_clean_and_seeded(self):
        db = preflight.load_rules_db(None)
        for fx in self.fixtures():
            manifest = json.loads((fx / "defects.json").read_text(encoding="utf-8"))
            src = next(p for p in fx.iterdir() if p.name.startswith("manuscript."))
            hit = resolve_venue(db, manifest["pack"]) or resolve_venue(db, manifest["venue"])
            rules = hit[1]["rules"] if hit else {}
            with self.subTest(fixture=fx.name):
                self.assertIsNotNone(hit, f"{fx.name}: no compiled rules for {manifest['pack']}")
                clean = run(src, rules)
                fails = [f"{f.check}: {f.message}" for f in clean.findings if f.severity == "FAIL"]
                self.assertEqual(fails, [], f"{fx.name}: clean copy raises FAIL")
                tmp = Path(tempfile.mkdtemp())
                try:
                    seeded_path = tmp / src.name
                    seeded_path.write_text(apply_manifest(src.read_text(encoding="utf-8"), manifest), encoding="utf-8")
                    seeded = run(seeded_path, rules)
                finally:
                    shutil.rmtree(tmp)
                base = {(f.check, f.statement, f.message) for f in clean.findings}
                new = [f for f in seeded.findings if (f.check, f.statement, f.message) not in base
                       and f.severity in {"FAIL", "FLAG"}]
                for d in manifest["defects"]:
                    if d["kind"] != "mechanical" or d.get("preflight") == "known-miss":
                        continue  # known misses are reported in the benchmark RESULTS, not hidden
                    caught = [f for f in new if f.check == d["check"]
                              and (not d.get("statement") or f.statement == d["statement"])]
                    self.assertTrue(caught, f"{fx.name} {d['id']} {d['check']} not caught: {d['description']}")


if __name__ == "__main__":
    unittest.main()
