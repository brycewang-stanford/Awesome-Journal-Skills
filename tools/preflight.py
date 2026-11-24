#!/usr/bin/env python3
"""Pre-submission preflight: deterministic mechanical checks on a real manuscript.

Stage 0 of the submission-readiness pipeline
(``shared-resources/submission-readiness/README.md``). It reads the *author's* manuscript
— ``.tex``, ``.md``, ``.docx``, ``.pdf`` or ``.txt`` — and checks it against the target
venue's hard rules, compiled from each pack's ``official-source-map.md`` into
``venue-rules.json`` by ``tools/venue_rules.py``. Every finding carries a location and
the pack skill that owns the fix.

What it checks (check IDs are stable; the benchmark and the skills cite them):

    LEN-ABSTRACT  LEN-WORDS  LEN-PAGES  LEN-TITLE  KW-COUNT  ABS-STRUCTURE
    ANON-AUTHOR  ANON-SELFCITE  ANON-ACK  ANON-URL  ANON-META      (blind review only)
    STMT-MISSING                                                   (venue-required statements)
    REF-MISSING  REF-UNCITED  REF-UNRESOLVED (--online)
    EXH-UNREFERENCED  EXH-NUMBERING  EXH-SE-NOTE
    NUM-MISMATCH  LEFTOVER-MARKER  LEFTOVER-TRACKED

What it does NOT do: judge contribution, identification, or prose. Those are stages 1-3
(the readiness scorecard and the simulated referee panel), which read this report first.
It never reports PASS for a rule it could not test: unknown venue rules are listed under
"not checked", never silently passed.

    python3 tools/preflight.py paper.tex --venue "Journal of Finance"
    python3 tools/preflight.py paper.pdf --venue icml --json > preflight.json
    python3 tools/preflight.py paper.md --venue jama --online   # + Crossref reference check
    python3 tools/preflight.py --list-venues

Exit status: 0 = GO or CONDITIONAL GO (no FAIL), 1 = NO-GO (at least one FAIL),
2 = usage or input error. Stdlib only; ``pdftotext``/``pdfinfo`` (poppler) are used for
PDFs when present.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
RULES_CANDIDATES = (
    HERE / "venue-rules.json",                                                  # vendored copy
    HERE.parent / "shared-resources" / "submission-readiness" / "venue-rules.json",  # repo
)

# ----------------------------------------------------------------------------- model


@dataclass
class Line:
    no: int            # 1-based line (tex/md/txt), paragraph (docx) or page (pdf)
    text: str          # plain text
    heading: int = 0   # heading level, 0 for body text
    kind: str = "text"  # text | table | caption | ref | front


@dataclass
class Doc:
    path: Path
    fmt: str
    title: str = ""
    front: str = ""            # author/affiliation block
    lines: list[Line] = field(default_factory=list)
    cite_keys: list[tuple[str, int]] = field(default_factory=list)   # tex \cite keys
    bib_keys: dict[str, int] = field(default_factory=dict)           # tex \bibitem / .bib
    labels: dict[str, int] = field(default_factory=dict)             # tex \label
    refs: list[tuple[str, int]] = field(default_factory=list)        # tex \ref targets
    tex_tables: list[dict] = field(default_factory=list)             # {label, text, line, kind}
    comments: list[tuple[str, int]] = field(default_factory=list)    # tex comments / docx comments
    tracked: int = 0
    pages: int | None = None
    ref_start_page: int | None = None
    metadata: dict = field(default_factory=dict)
    loc_unit: str = "line"
    nocite_all: bool = False


@dataclass
class Finding:
    check: str
    severity: str       # FAIL | FLAG | INFO
    message: str
    where: str = ""
    owner: str = ""
    statement: str = ""


OWNER = {
    "LEN": "*-submission (move material to the appendix/supplement per *-internet-appendix or *-supplementary)",
    "KW": "*-submission",
    "ABS": "*-writing-style + *-submission",
    "ANON": "*-submission (anonymization)",
    "STMT": "*-submission (required statements)",
    "REF": "*-literature-positioning + *-submission",
    "EXH": "*-tables-figures",
    "NUM": "*-writing-style + *-tables-figures",
    "LEFTOVER": "*-submission",
}


def owner_of(check: str) -> str:
    return OWNER.get(check.split("-")[0], "*-submission")


# ----------------------------------------------------------------------------- text utils

CJK = re.compile(r"[\u3400-\u9fff\uf900-\ufaff]")
WORD = re.compile(r"[A-Za-z0-9]+(?:[-'’.][A-Za-z0-9]+)*")


def is_cjk(text: str) -> bool:
    cjk = len(CJK.findall(text))
    return cjk > 0.3 * max(1, cjk + len(WORD.findall(text)))


def count_words(text: str) -> int:
    return len(WORD.findall(text))


def count_chars(text: str) -> int:
    """Chinese venues state length in 字: count CJK characters plus Latin words."""
    return len(CJK.findall(text)) + len(WORD.findall(text))


def norm_name(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z\u3400-\u9fff]", "", s.lower())


def heading_core(text: str) -> str:
    t = text.strip().strip("*#").strip()
    t = re.sub(r"^(?:\d+(?:\.\d+)*\.?|[IVXLC]+\.|[A-Z]\.|[一二三四五六七八九十]+、|（[一二三四五六七八九十]+）)\s*", "", t)
    return t.strip().rstrip(":：").strip()


def is_abstract_h(h: str) -> bool:
    return bool(re.fullmatch(r"(abstract|summary|摘\s*要|内容提要|提要)", heading_core(h), re.I))


def is_refs_h(h: str) -> bool:
    return bool(re.fullmatch(r"(references?|bibliography|works cited|literature cited|参考文献|主要参考文献)",
                             heading_core(h), re.I))


def is_appendix_h(h: str) -> bool:
    return bool(re.search(r"appendix|appendices|附录|supplementa|online appendix|internet appendix",
                          heading_core(h), re.I))


def is_intro_h(h: str) -> bool:
    return bool(re.search(r"introduction|引言|导论|问题的提出|^绪论", heading_core(h), re.I))


# ----------------------------------------------------------------------------- loaders

def load(path: Path, bib: Path | None) -> Doc:
    suffix = path.suffix.lower()
    if suffix == ".tex":
        return load_tex(path, bib)
    if suffix in {".md", ".markdown"}:
        return load_md(path)
    if suffix == ".docx":
        return load_docx(path)
    if suffix == ".pdf":
        return load_pdf(path)
    if suffix in {".txt", ".text"}:
        return load_plain(path, path.read_text(encoding="utf-8", errors="replace"), "txt")
    raise SystemExit(f"preflight: unsupported format {suffix} (use .tex .md .docx .pdf .txt)")


def _md_inline(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 \2", text)
    text = re.sub(r"<!--.*?-->", " ", text)
    text = re.sub(r"[*_`]{1,3}", "", text)
    return text


def load_md(path: Path) -> Doc:
    raw = unicodedata.normalize("NFC", path.read_text(encoding="utf-8", errors="replace"))
    doc = Doc(path=path, fmt="md")
    doc.tracked = len(re.findall(r"\{\+\+.*?\+\+\}|\{--.*?--\}|\{~~.*?~~\}", raw, re.S))
    doc.comments = [(m.group(0)[:80], raw[: m.start()].count("\n") + 1)
                    for m in re.finditer(r"\{>>.*?<<\}", raw, re.S)]
    in_code = False
    seen_title = False
    front: list[str] = []
    in_front = False
    for i, line in enumerate(raw.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if re.match(r"^\s*<!--.*-->\s*$", line):
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level, text = len(m.group(1)), _md_inline(m.group(2)).strip()
            if level == 1 and not seen_title:
                doc.title, seen_title, in_front = text, True, True
                continue
            in_front = False
            doc.lines.append(Line(i, text, heading=level))
            continue
        text = _md_inline(line).strip()
        if not text:
            continue
        if in_front:
            front.append(text)
            doc.lines.append(Line(i, text, kind="front"))
            continue
        kind = "table" if line.lstrip().startswith("|") else "text"
        if kind == "table" and re.fullmatch(r"[\s|:\-]+", line):
            continue
        if kind == "table":
            text = " ".join(c.strip() for c in line.strip().strip("|").split("|"))
        doc.lines.append(Line(i, text, kind=kind))
    doc.front = "\n".join(front)
    return doc


TEX_KEEP = r"textbf|textit|emph|underline|textsc|textrm|texttt|mbox|text|mathrm|mathbf|footnote|thanks|url|hl"


def _tex_plain(s: str) -> str:
    s = re.sub(r"\\(?:no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{[^}]*\}", " ⟨cite⟩ ", s)
    s = re.sub(r"\\(?:auto|c|C|eq|page|name)?ref\*?\{[^}]*\}", " 1 ", s)
    s = re.sub(r"\\label\{[^}]*\}", " ", s)
    s = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", r"\2 \1", s)
    for _ in range(3):
        # \x01 marks the seam so "\noindent\textbf{JEL}" cannot collapse into "\noindentJEL"
        s = re.sub(r"\\(?:%s)\*?\{([^{}]*)\}" % TEX_KEEP, "\x01\\1", s)
    s = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\{[^}]*\}|\[[^\]]*\])*", " ", s)
    s = re.sub(r"\\[a-zA-Z@]+\*?(?:\[[^\]]*\])?", " ", s)
    s = s.replace("\x01", "")
    s = s.replace("\\%", "%").replace("\\&", "&").replace("\\$", "$").replace("\\_", "_")
    s = s.replace("~", " ").replace("&", " ").replace("\\\\", " ")
    s = re.sub(r"[{}$]", "", s)
    s = s.replace("``", '"').replace("''", '"')
    return re.sub(r"\s+", " ", s).strip()


def _tex_arg(src: str, cmd: str) -> tuple[str, int] | None:
    m = re.search(r"\\%s\*?(?:\[[^\]]*\])?\{" % cmd, src)
    if not m:
        return None
    depth, i = 1, m.end()
    while i < len(src) and depth:
        depth += {"{": 1, "}": -1}.get(src[i], 0)
        i += 1
    return src[m.end(): i - 1], src[: m.start()].count("\n") + 1


def _expand_inputs(path: Path, depth: int = 0) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if depth > 4:
        return text

    def sub(m: re.Match) -> str:
        name = m.group(1).strip()
        cand = (path.parent / name)
        if cand.suffix != ".tex":
            cand = cand.with_suffix(".tex") if not cand.exists() else cand
        return _expand_inputs(cand, depth + 1) if cand.exists() else m.group(0)

    return re.sub(r"\\(?:input|include)\{([^}]+)\}", sub, text)


def load_tex(path: Path, bib: Path | None) -> Doc:
    raw = _expand_inputs(path)
    doc = Doc(path=path, fmt="tex")
    # comments: keep them for the leftover scan, drop them from the text
    src_lines = []
    for i, line in enumerate(raw.splitlines(), 1):
        m = re.search(r"(?<!\\)%(.*)$", line)
        if m:
            if m.group(1).strip():
                doc.comments.append((m.group(1).strip(), i))
            line = line[: m.start()]
        src_lines.append(line)
    src = "\n".join(src_lines)
    doc.tracked = len(re.findall(r"\\DIF(?:add|del)(?:begin|end)?\b", src))
    t = _tex_arg(src, "title")
    doc.title = _tex_plain(t[0]) if t else ""
    fronts = []
    for cmd in ("author", "affiliation", "icmlauthor", "icmlaffiliation", "icmlcorrespondingauthor",
                "address", "email", "institute"):
        for m in re.finditer(r"\\%s\*?(?:\[[^\]]*\])?\{" % cmd, src):
            a = _tex_arg(src[m.start():], cmd)
            if a:
                fronts.append(a[0])
    doc.front = _tex_plain(" \n ".join(fronts))
    doc.nocite_all = bool(re.search(r"\\nocite\{\*\}", src))

    for m in re.finditer(r"\\(?:no)?cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", src):
        line = src[: m.start()].count("\n") + 1
        if m.group(0).startswith("\\nocite"):
            continue
        for key in m.group(1).split(","):
            if key.strip():
                doc.cite_keys.append((key.strip(), line))
    for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", src):
        doc.bib_keys[m.group(1).strip()] = src[: m.start()].count("\n") + 1
    bibs = []
    if bib:
        bibs.append(bib)
    for m in re.finditer(r"\\(?:bibliography|addbibresource)\{([^}]+)\}", src):
        for name in m.group(1).split(","):
            p = path.parent / name.strip()
            bibs.append(p if p.suffix == ".bib" else p.with_suffix(".bib"))
    # arXiv sources usually ship the compiled .bbl instead of the .bib
    bbl = path.with_suffix(".bbl")
    if bbl.exists():
        for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bbl.read_text(encoding="utf-8", errors="replace")):
            doc.bib_keys.setdefault(m.group(1).strip(), 0)
        doc.metadata["bib_files"] = doc.metadata.get("bib_files", []) + [str(bbl)]
    for b in bibs:
        if b.exists():
            btxt = b.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", btxt):
                if not m.group(0).lower().startswith(("@comment", "@string", "@preamble")):
                    doc.bib_keys.setdefault(m.group(1), 0)
            doc.metadata["bib_files"] = doc.metadata.get("bib_files", []) + [str(b)]
    for m in re.finditer(r"\\label\{([^}]+)\}", src):
        doc.labels[m.group(1)] = src[: m.start()].count("\n") + 1
    for m in re.finditer(r"\\(?:auto|c|C|eq|page|name)?ref\*?\{([^}]+)\}", src):
        for key in m.group(1).split(","):
            doc.refs.append((key.strip(), src[: m.start()].count("\n") + 1))
    for m in re.finditer(r"\\begin\{(table|figure)\*?\}(.*?)\\end\{\1\*?\}", src, re.S):
        body = m.group(2)
        lab = re.search(r"\\label\{([^}]+)\}", body)
        doc.tex_tables.append({
            "kind": m.group(1),
            "label": lab.group(1) if lab else "",
            "text": _tex_plain(body) + "\n" + "\n".join(_tex_plain(r) for r in re.split(r"\\\\", body)),
            "line": src[: m.start()].count("\n") + 1,
        })

    # body lines with headings
    body_start = src.find("\\begin{document}")
    in_abstract = in_bib = in_float = False
    heading_re = re.compile(r"\\(part|chapter|section|subsection|subsubsection|paragraph)\*?(?:\[[^\]]*\])?\{")
    lines = src.splitlines()
    first = src[:body_start].count("\n") + 1 if body_start >= 0 else 1
    i = first - 1
    while i < len(lines):
        no, line = i + 1, lines[i]
        i += 1
        if "\\begin{abstract}" in line:
            in_abstract = True
            doc.lines.append(Line(no, "Abstract", heading=1))
            line = line.split("\\begin{abstract}", 1)[1]
        if "\\end{abstract}" in line:
            line = line.split("\\end{abstract}", 1)[0]
            if line.strip():
                doc.lines.append(Line(no, _tex_plain(line)))
            in_abstract = False
            doc.lines.append(Line(no, "", heading=9))  # sentinel: abstract ended
            continue
        if "\\begin{thebibliography}" in line:
            in_bib = True
            doc.lines.append(Line(no, "References", heading=1))
            continue
        if "\\end{thebibliography}" in line:
            in_bib = False
            continue
        if re.search(r"\\(bibliography|printbibliography)\b", line) and not in_bib:
            doc.lines.append(Line(no, "References", heading=1))
            continue
        if re.search(r"\\appendix\b", line):
            doc.lines.append(Line(no, "Appendix", heading=1))
            continue
        hm = heading_re.search(line)
        if hm:
            a = _tex_arg(line[hm.start():] + "\n" + "\n".join(lines[i:i + 3]), hm.group(1))
            level = {"part": 1, "chapter": 1, "section": 1, "subsection": 2,
                     "subsubsection": 3, "paragraph": 4}[hm.group(1)]
            htext = _tex_plain(a[0]) if a else ""
            doc.lines.append(Line(no, htext, heading=level))
            rest = line[hm.end():]
            rest = rest.split("}", 1)[1] if "}" in rest else ""
            if rest.strip():
                doc.lines.append(Line(no, _tex_plain(rest)))
            continue
        if in_bib and "\\bibitem" in line:
            doc.lines.append(Line(no, _tex_plain(re.sub(r"\\bibitem(?:\[[^\]]*\])?\{[^}]*\}", "", line)), kind="ref"))
            continue
        if re.search(r"\\begin\{(table|figure|threeparttable)\*?\}", line):
            in_float = True
        kind = "table" if "&" in line and "\\\\" in line else ("float" if in_float else "text")
        if re.search(r"\\end\{(table|figure)\*?\}", line):
            in_float = False
        plain = _tex_plain(line)
        if plain:
            if re.search(r"\\caption", line):
                kind = "caption"
            doc.lines.append(Line(no, plain, kind=kind))
    return doc


W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def load_docx(path: Path) -> Doc:
    doc = Doc(path=path, fmt="docx", loc_unit="paragraph")
    style_names: dict[str, str] = {}
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
        names = set(z.namelist())
        if "word/styles.xml" in names:
            # styleIds are locale-dependent ("Heading1", or "1"/"2" in Chinese Word); the
            # w:name ("heading 1", "Title") is not.
            for st in ET.fromstring(z.read("word/styles.xml")).iter(W + "style"):
                nm = st.find(W + "name")
                if nm is not None and st.get(W + "styleId"):
                    style_names[st.get(W + "styleId")] = (nm.get(W + "val") or "").lower()
        if "word/comments.xml" in names:
            croot = ET.fromstring(z.read("word/comments.xml"))
            for c in croot.iter(W + "comment"):
                txt = "".join(t.text or "" for t in c.iter(W + "t"))
                doc.comments.append((txt[:80], 0))
        if "docProps/core.xml" in names:
            core = z.read("docProps/core.xml").decode("utf-8", "replace")
            for tag in ("creator", "lastModifiedBy"):
                m = re.search(r"<(?:dc|cp):%s>([^<]*)</" % tag, core)
                if m and m.group(1).strip():
                    doc.metadata[tag] = m.group(1).strip()
    root = ET.fromstring(xml)
    doc.tracked = sum(1 for _ in root.iter(W + "ins")) + sum(1 for _ in root.iter(W + "del"))
    body = root.find(W + "body")
    n = 0
    seen_title = False
    in_front = False
    for el in list(body) if body is not None else []:
        if el.tag == W + "tbl":
            for row in el.iter(W + "tr"):
                cells = [" ".join("".join(t.text or "" for t in p.iter(W + "t")) for p in c.iter(W + "p"))
                         for c in row.iter(W + "tc")]
                n += 1
                txt = " ".join(c.strip() for c in cells if c.strip())
                if txt:
                    doc.lines.append(Line(n, txt, kind="table"))
            continue
        if el.tag != W + "p":
            continue
        n += 1
        style = el.find(f"{W}pPr/{W}pStyle")
        sid = (style.get(W + "val") if style is not None else "") or ""
        sname = style_names.get(sid, sid)
        txt = "".join(t.text or "" for t in el.iter(W + "t")).strip()  # deletions live in w:delText
        if not txt:
            continue
        if sname.lower() == "title" and not seen_title:
            doc.title, seen_title, in_front = txt, True, True
            continue
        hm = re.match(r"(?:heading|标题)\s*(\d)", sname, re.I) or (re.match(r"(\d)$", sname) if not style_names else None)
        level = int(hm.group(1)) if hm else 0
        if not level and (is_abstract_h(txt) or is_refs_h(txt)) and len(txt) < 40:
            level = 1
        if level:
            in_front = False
            doc.lines.append(Line(n, txt, heading=level))
            continue
        if in_front:
            doc.front += txt + "\n"
            doc.lines.append(Line(n, txt, kind="front"))
            continue
        kind = "caption" if caption_match(txt) else "text"
        doc.lines.append(Line(n, txt, kind=kind))
    if not seen_title and doc.lines:
        _guess_front(doc)
    return doc


def load_pdf(path: Path) -> Doc:
    if not shutil.which("pdftotext"):
        raise SystemExit("preflight: PDF input needs pdftotext (poppler). Install it, or pass the .tex/.docx source.")
    text = subprocess.run(["pdftotext", "-enc", "UTF-8", str(path), "-"], capture_output=True,
                          text=True, check=False).stdout
    if _two_column(path):
        # pdftotext's reading-order heuristic interleaves the columns of a two-column paper;
        # the content-stream order (-raw) of LaTeX/Word output reads column by column.
        text = subprocess.run(["pdftotext", "-raw", "-enc", "UTF-8", str(path), "-"], capture_output=True,
                              text=True, check=False).stdout
    doc = load_plain(path, text, "pdf")
    if shutil.which("pdfinfo"):
        info = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True, check=False).stdout
        m = re.search(r"^Pages:\s+(\d+)", info, re.M)
        doc.pages = int(m.group(1)) if m else None
        for key in ("Author", "Creator", "Title"):
            m = re.search(rf"^{key}:\s+(.+)$", info, re.M)
            if m and m.group(1).strip():
                doc.metadata[key.lower()] = m.group(1).strip()
    else:
        doc.pages = text.count("\f") + 1
    return doc


def _two_column(path: Path) -> bool:
    """Two-column layout? In pdftotext -layout output the right column of a two-column page
    starts at the same x on line after line, after a gap of 2+ spaces. Single-column pages
    (justified prose) have almost no such gaps. Measured on the benchmark PDFs: two-column
    papers put 44-51% of their full lines in one 9-character band, single-column ones at
    most 7%; the threshold sits between."""
    lay = subprocess.run(["pdftotext", "-layout", "-l", "4", "-enc", "UTF-8", str(path), "-"],
                         capture_output=True, text=True, check=False).stdout
    lines = [ln.rstrip() for ln in lay.splitlines() if len(ln.strip()) > 50]
    if len(lines) < 30:
        return False
    hits: Counter = Counter()
    for ln in lines:
        hits.update({m.end() // 3 for m in re.finditer(r"(?<=\S) {2,}(?=\S)", ln) if m.end() >= 25})
    if not hits:
        return False
    mode = hits.most_common(1)[0][0]
    band = sum(1 for ln in lines if any(abs(m.end() // 3 - mode) <= 1
                                         for m in re.finditer(r"(?<=\S) {2,}(?=\S)", ln)))
    return band / len(lines) > 0.25


KNOWN_HEADINGS = re.compile(
    r"^(abstract|introduction|related work|background|method(s|ology)?|data|results|discussion|"
    r"conclusions?|references|bibliography|acknowledg(e)?ments?|limitations|appendix.*|"
    r"(?:supplementary|online|internet|supplemental) (?:appendix|material).*|"
    r"impact statement|broader impacts?|ethics statement|data availability.*|funding.*|"
    r"conflicts? of interest.*|disclosure.*|摘\s*要|引言|参考文献|附录|结论|致谢|英文(?:梗概|摘要).*|"
    r"key points|trial registration|data sharing statement)$", re.I)


CAPTION_EN = re.compile(r"^\s*(Table|Figure|Fig\.|Exhibit)\s*([A-Z]?)(\d+|[IVXL]+\b)\s*(?:[.:：|—–]|-\s|$)")
ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50}


def exhibit_number(tok: str) -> int:
    """'4' -> 4, 'IV' -> 4 (journals such as JF number exhibits in Roman numerals)."""
    if tok.isdigit():
        return int(tok)
    total = 0
    for a, b in zip(tok, tok[1:] + " "):
        v = ROMAN.get(a, 0)
        total += -v if ROMAN.get(b, 0) > v else v
    return total
# "表1：…" / "表 1 描述性统计" — but not prose that starts with a reference ("表 4 Panel A 显示，…")
CAPTION_CN = re.compile(r"^\s*(表|图)\s*([A-Z]?)(\d+)\s*(?:[.:：]|\s+[^，。,；]{1,40}$)")


def caption_match(text: str):
    m = CAPTION_EN.match(text)
    if m:
        return m
    m = CAPTION_CN.match(text)
    if m and "。" not in text and len(text) < 60:
        return m
    return None


def load_plain(path: Path, text: str, fmt: str) -> Doc:
    """PDF/plain text: rebuild paragraphs, since pdftotext breaks every visual line."""
    doc = Doc(path=path, fmt=fmt, loc_unit="page" if fmt == "pdf" else "line")
    # pdftotext emits decomposed accents ("Gonza\u0301lez"), which break name matching.
    text = unicodedata.normalize("NFC", text)
    text = _join_split_headings(text)
    page = 1
    buf: list[str] = []
    buf_no = 0

    def flush() -> None:
        nonlocal buf
        if buf:
            joined = ""
            for part in buf:
                if re.search(r"(https?:|https?://\S*[/._-])$", joined):
                    joined += part  # a URL broken across lines
                elif joined.endswith("-") and part[:1].islower():
                    joined = joined[:-1] + part
                elif joined and CJK.match(joined[-1:] or " ") and CJK.match(part[:1] or " "):
                    joined += part
                else:
                    joined = (joined + " " + part).strip()
            kind = "caption" if caption_match(joined) else "text"
            doc.lines.append(Line(buf_no, joined, kind=kind))
        buf = []

    for i, line in enumerate(text.split("\n"), 1):  # not splitlines(): it eats the \f page breaks
        if "\f" in line:
            page += line.count("\f")
            line = line.replace("\f", "")
        s = line.strip()
        no = page if fmt == "pdf" else i
        if not s:
            flush()
            continue
        if fmt == "pdf" and re.fullmatch(r"\d{1,3}|page \d+( of \d+)?", s, re.I):
            continue  # running page numbers
        core = heading_core(s)
        numbered = (re.match(r"^((?:1?\d)(\.\d+)*\.?|[IVX]+\.|[A-H](\.\d+)*\.?)\s+[A-Z][^.!?,]{2,60}$", s)
                    and not re.match(r"^0", s))
        fragment = re.search(r"[,;)]\.?$", s) or s[:1].islower()  # "Appendix Section IA.C)." is prose
        stmt_head = (len(s) < 50 and not re.search(r"[.,;:]$", s)
                     and any(re.fullmatch(f"(?:{p})(?:\\s+statement|\\s+disclosures?)?", core, re.I)
                             for k, p in STATEMENT_PATTERNS.items()
                             if k not in {"jel_codes", "keywords", "reporting_guideline", "trial_registration"}))
        cn_head = re.fullmatch(r"(?:[一二三四五六七八九十]+、|（[一二三四五六七八九十]+）)[^。，；]{1,28}", s)
        if cn_head or (not fragment and ((KNOWN_HEADINGS.match(core) and len(s) < 60) or stmt_head
                             or re.fullmatch(r"(key points|trial registration|data sharing statement)", core, re.I)
                             or (numbered and len(s) < 70))):
            flush()
            level = 2 if re.match(r"^(\d+|[A-H])\.\d+|^（", s) else 1
            doc.lines.append(Line(no, s, heading=level))
            if is_refs_h(s) and fmt == "pdf" and doc.ref_start_page is None:
                doc.ref_start_page = page
            continue
        if not any(ln.heading for ln in doc.lines) or KW_LINE.match(s) or JEL_LINE.match(s):
            flush()  # front matter and keyword/JEL lines stay one line each
            buf_no = no
            buf.append(s)
            flush()
            continue
        if caption_match(s) and len(s) < 160:
            flush()  # a caption is its own line; the description that follows is not part of it
            buf_no = no
            buf.append(s)
            flush()
            continue
        if _starts_reference(doc, buf, s):
            flush()
        if not buf:
            buf_no = no
        buf.append(s)
    flush()
    _guess_front(doc)
    return doc


def _join_split_headings(text: str) -> str:
    """pdftotext often puts a section number on its own line: "1\n\nIntroduction",
    "A\n\nTourism Data". Re-join them, so the heading (and the end of the previous
    section) is not lost. Never across a page break."""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        if re.fullmatch(r"\s*(\d{1,2}(\.\d{1,2})*|[A-H](\.\d{1,2})*)\s*", cur) and "\f" not in cur:
            j = i + 1
            while j < len(lines) and not lines[j].strip() and "\f" not in lines[j]:
                j += 1
            nxt = lines[j] if j < len(lines) else ""
            if (nxt and "\f" not in nxt and len(nxt.strip()) < 60 and re.match(r"\s*[A-Z]", nxt)
                    and not re.search(r"[.,;:]\s*$", nxt)):
                out.append(f"{cur.strip()} {nxt.strip()}")
                i = j + 1
                continue
        out.append(cur)
        i += 1
    return "\n".join(out)


def _starts_reference(doc: Doc, buf: list[str], s: str) -> bool:
    """In a PDF reference list, does line ``s`` begin a new entry? The buffered entry must
    already carry a year. A new entry starts with an author ("Surname, I." / "Surname, Given"
    / AMA "Surname IK," / a Chinese name / a number), or follows a line that closed an entry
    with a period (corporate authors such as "SPRINT Research Group.")."""
    if not (doc.lines and buf and is_refs_h_current(doc) and re.search(r"(19|20)\d{2}", " ".join(buf))):
        return False
    if re.match(rf"^(\[\d+\]|\d+\.\s|{SURNAME},\s+(?:[A-ZÀ-Þ]\.|[A-ZÀ-Þ][a-zà-ÿ]+)|"
                rf"{SURNAME}\s+[A-Z]{{1,3}}[,.]\s|[一-鿿]{{2,4}}[，,.、（(])", s):
        return True
    # "Borkan, D., … (2019)." then the title on the next line: the entry is not finished yet
    if re.search(r"\((19|20)\d{2}[a-z]?\)\.?$", buf[-1].rstrip()):
        return False
    return bool(re.match(r"[A-Z]", s) and buf[-1].rstrip().endswith("."))


def is_refs_h_current(doc: Doc) -> bool:
    last = next((ln for ln in reversed(doc.lines) if ln.heading), None)
    return bool(last and is_refs_h(last.text))


def _guess_front(doc: Doc) -> None:
    """For formats without explicit structure: title = first line; front = up to Abstract."""
    idx = next((k for k, ln in enumerate(doc.lines) if ln.heading and is_abstract_h(ln.text)), None)
    if idx is None:
        idx = next((k for k, ln in enumerate(doc.lines) if ln.heading), min(len(doc.lines), 8))
    head = doc.lines[:idx]
    if head and not doc.title:
        doc.title = head[0].text
        head = head[1:]
    for ln in head:
        ln.kind = "front"
    doc.front = "\n".join(ln.text for ln in head)
    if doc.lines and doc.title and doc.lines[0].text == doc.title:
        doc.lines = doc.lines[1:]  # the title is not body text


# ----------------------------------------------------------------------------- structure

@dataclass
class Section:
    heading: str
    level: int
    lines: list[Line]

    @property
    def text(self) -> str:
        return "\n".join(ln.text for ln in self.lines)

    @property
    def where(self) -> str:
        return self.heading or "(front matter)"


def sections(doc: Doc) -> list[Section]:
    out = [Section("", 0, [])]
    for ln in doc.lines:
        if ln.heading == 9:
            out.append(Section("(after abstract)", 1, []))
            continue
        if ln.heading:
            out.append(Section(ln.text, ln.heading, []))
        else:
            out[-1].lines.append(ln)
    return out


NOTE_LINE = re.compile(r"^\s*(notes?|sources?|注|说明|资料来源|数据来源)\s*[:：.]", re.I)
# First-page footnotes (thanks, affiliations) that pdftotext places before the Introduction.
FOOTNOTE_LEAD = re.compile(r"^\s*[∗†‡§¶*]")
KW_LINE = re.compile(r"^\s*(key\s?words?|index terms|关\s*键\s*词)\s*[:：.]?", re.I)
JEL_LINE = re.compile(r"^\s*(JEL\b[^:：]{0,25}|JEL\s*分类号)\s*[:：]?", re.I)


def abstract_text(doc: Doc, secs: list[Section]) -> tuple[str, str]:
    for s in secs:
        if is_abstract_h(s.heading):
            body = [ln.text for ln in s.lines if not KW_LINE.match(ln.text) and not JEL_LINE.match(ln.text)
                    and ln.kind != "front" and not FOOTNOTE_LEAD.match(ln.text)]
            return "\n".join(body).strip(), s.where
    return "", ""


def main_body(secs: list[Section]) -> list[Section]:
    """Sections that count as main text: after the abstract, before references/appendix."""
    out, started, stopped = [], False, False
    has_abstract = any(is_abstract_h(s.heading) for s in secs)
    for s in secs:
        if is_abstract_h(s.heading):
            started = True
            continue
        if not started and has_abstract:
            continue
        if not s.heading and not s.lines:
            continue
        if is_refs_h(s.heading) or is_appendix_h(s.heading):
            stopped = True
        if stopped:
            # statements after the references are still not main text
            continue
        if s.heading == "" and has_abstract:
            continue
        out.append(s)
    return out


# ----------------------------------------------------------------------------- statements

STATEMENT_PATTERNS = {
    "data_availability": r"data (availability|access|sharing)|availability of data|data and (code|materials) availability|replication (package|files|materials)|数据(可得性|获取|可用性|共享)|数据与代码",
    "code_availability": r"code availability|code (and data )?(is |are )?available|software availability|replication (package|code)|代码(获取|可得|共享|公开)|数据与代码",
    "conflict_of_interest": r"conflicts? of interest|competing interests?|declaration of interests?|conflict of interest disclosures?|financial disclosures?|disclosure statement|利益冲突",
    "funding": r"funding|financial support|grant support|基金项目|资助",
    "ethics_approval": r"ethic(s|al) (approval|statement|review|considerations)|institutional review board|\bIRB\b|伦理(审查|批准)",
    "informed_consent": r"informed consent|知情同意",
    "ai_use_disclosure": r"(use of|statement on|disclosure of) (generative )?(ai|artificial intelligence|large language models?)|\bai (use |usage )?(disclosure|statement)|ai[- ]assisted|llm (use|usage)|generative ai|人工智能(工具)?使用",
    "author_contributions": r"author contributions?|credit authorship|作者贡献",
    "trial_registration": r"trial registration|clinicaltrials\.gov|\bNCT\d{8}\b|ISRCTN|ChiCTR",
    "reporting_guideline": r"\b(CONSORT|STROBE|PRISMA|STARD|TRIPOD|ARRIVE|SPIRIT|CHEERS|SQUIRE)\b",
    "limitations": r"^limitations?\b|局限",
    "broader_impact": r"(broader|societal) impacts?|impact statement",
    "reproducibility_checklist": r"reproducibility checklist|paper checklist|responsible nlp checklist",
    "significance_statement": r"significance( statement)?$",
    "acknowledgments": r"acknowledg(e)?ments?|致\s*谢",
    "disclosure_statement": r"disclosure statement|disclosures?$|conflicts? of interest|competing interests?|利益冲突",
    "jel_codes": r"\bJEL\b",
    "keywords": r"key\s?words?|index terms|关\s*键\s*词",
    "highlights": r"^highlights",
    "key_points": r"^key points",
    "lay_summary": r"lay summary|plain language summary",
    "graphical_abstract": r"graphical abstract",
}
STATEMENT_LABEL = {
    "data_availability": "Data availability statement",
    "code_availability": "Code availability statement",
    "conflict_of_interest": "Conflict-of-interest / competing-interests statement",
    "funding": "Funding statement",
    "ethics_approval": "Ethics / IRB approval statement",
    "informed_consent": "Informed-consent statement",
    "ai_use_disclosure": "Generative-AI use disclosure",
    "author_contributions": "Author-contributions statement",
    "trial_registration": "Trial registration",
    "reporting_guideline": "Reporting-guideline statement (CONSORT/STROBE/PRISMA…)",
    "limitations": "Limitations section",
    "broader_impact": "Impact / broader-impact statement",
    "reproducibility_checklist": "Reproducibility / paper checklist",
    "significance_statement": "Significance statement",
    "acknowledgments": "Acknowledgments",
    "disclosure_statement": "Disclosure statement",
    "jel_codes": "JEL codes",
    "keywords": "Keywords",
    "highlights": "Highlights",
    "key_points": "Key Points box",
    "lay_summary": "Lay / plain-language summary",
    "graphical_abstract": "Graphical abstract",
}
# Statements whose presence is judged anywhere in the text, not only in a heading or lead.
ANYWHERE = {"trial_registration", "reporting_guideline", "jel_codes"}


def has_statement(doc: Doc, name: str) -> bool:
    if name == "structured_abstract":
        return True  # tested by ABS-STRUCTURE
    pat = re.compile(STATEMENT_PATTERNS.get(name, re.escape(name)), re.I | re.M)
    for ln in doc.lines:
        if ln.heading and pat.search(heading_core(ln.text)):
            return True
        lead = re.split(r"[:：.。]", ln.text, maxsplit=1)[0] if ln.text else ""
        if len(lead) <= 80 and pat.search(lead) and (":" in ln.text[:90] or "：" in ln.text[:90]):
            return True
        if name in ANYWHERE and pat.search(ln.text):
            return True
    if name in ANYWHERE and pat.search(doc.front):
        return True
    return False


# ----------------------------------------------------------------------------- citations

_L = r"[^\W\d_\u3400-\u9fff\uf900-\ufaff]"  # any non-CJK letter, so D'Haultfœuille and Pérez are surnames
SURNAME = rf"(?:(?:van|von|de|der|den|da|di|du|le|la|del|Mc|O')\s?)?[A-ZÀ-ÖØ-Þ](?:{_L}|['’\-])+"
NARRATIVE = re.compile(
    rf"({SURNAME})(?:\s+et\s+al\.?|\s+(?:and|&)\s+{SURNAME}|,\s+{SURNAME},?\s+(?:and|&)\s+{SURNAME})?"
    r"(?:’s|'s)?\s+\(((?:19|20)\d{2}[a-z]?)(?:[,;][^)]*)?\)")
PAREN_ITEM = re.compile(
    rf"({SURNAME})(?:\s+et\s+al\.?|\s+(?:and|&)\s+{SURNAME}|,\s+{SURNAME},?\s+(?:and|&)\s+{SURNAME})?,?\s+((?:19|20)\d{{2}}[a-z]?)")
CN_NARRATIVE = re.compile(r"([\u4e00-\u9fff]{2,4}?)(?:等|和[\u4e00-\u9fff]{2,4}|与[\u4e00-\u9fff]{2,4})?（((?:19|20)\d{2}[a-z]?)）")
CN_PAREN_ITEM = re.compile(r"([\u4e00-\u9fff]{2,4}?)(?:等|和[\u4e00-\u9fff]{2,4}|与[\u4e00-\u9fff]{2,4})?[，,]\s*((?:19|20)\d{2}[a-z]?)")
NOT_NAMES = {
    "january", "february", "march", "april", "may", "june", "july", "august", "september",
    "october", "november", "december", "table", "figure", "section", "appendix", "in", "since",
    "during", "by", "from", "until", "after", "before", "as", "of", "the", "and", "see", "eg", "ie",
    "e.g", "i.e", "cf", "fall", "spring", "summer", "winter", "fy", "q", "wave", "cohort",
    "year", "years", "through", "to", "between", "census", "survey", "act", "law", "panel",
}
CN_NOT_NAMES = {"本文", "我们", "截至", "自从", "年份", "样本", "数据", "研究", "以及"}


@dataclass
class Cite:
    name: str
    year: str
    line: int


def text_citations(doc: Doc, secs: list[Section]) -> list[Cite]:
    out: list[Cite] = []
    for s in secs:
        if is_refs_h(s.heading):
            continue
        for ln in s.lines:
            if ln.kind in {"front", "ref"}:
                continue
            t = ln.text
            # English citations inside Chinese text use full-width punctuation: "（Beck et al.，2018）"
            t_latin = (t.replace("（", " (").replace("）", ")").replace("，", ", ").replace("；", "; "))
            for m in NARRATIVE.finditer(t_latin):
                if m.group(1).lower().strip(".") not in NOT_NAMES:
                    out.append(Cite(m.group(1), m.group(2), ln.no))
            for pm in re.finditer(r"\(([^()]*?(?:19|20)\d{2}[a-z]?[^()]*)\)", t_latin):
                inner = pm.group(1)
                for part in re.split(r";", inner):
                    im = PAREN_ITEM.search(part)
                    if im and im.group(1).lower().strip(".") not in NOT_NAMES:
                        out.append(Cite(im.group(1), im.group(2), ln.no))
            for m in CN_NARRATIVE.finditer(t):
                if m.group(1) not in CN_NOT_NAMES:
                    out.append(Cite(m.group(1), m.group(2), ln.no))
            for pm in re.finditer(r"（([^（）]*?(?:19|20)\d{2}[^（）]*)）", t):
                for part in re.split(r"[；;]", pm.group(1)):
                    im = CN_PAREN_ITEM.search(part)
                    if im and im.group(1) not in CN_NOT_NAMES:
                        out.append(Cite(im.group(1), im.group(2), ln.no))
                    else:
                        em = PAREN_ITEM.search(part)
                        if em and em.group(1).lower() not in NOT_NAMES:
                            out.append(Cite(em.group(1), em.group(2), ln.no))
    # dedupe identical (name, year, line)
    seen, uniq = set(), []
    for c in out:
        k = (norm_name(c.name), c.year, c.line)
        if k not in seen:
            seen.add(k)
            uniq.append(c)
    return uniq


@dataclass
class Ref:
    text: str
    line: int
    name: str
    year: str


def reference_entries(doc: Doc, secs: list[Section]) -> list[Ref]:
    """One entry per reference line. Markdown/LaTeX/Word already give one paragraph per
    entry, and the PDF/text loader splits the wrapped list into entries itself
    (``_starts_reference``), so no second, cruder split happens here."""
    entries: list[Ref] = []
    for s in secs:
        if is_refs_h(s.heading):
            entries.extend(_mk_ref([ln]) for ln in s.lines)
    return [e for e in entries if e.year]


def _mk_ref(buf: list[Line]) -> Ref:
    text = " ".join(b.text for b in buf).strip()
    text = re.sub(r"^\s*(\[\d+\]|\d+\.)\s*", "", text)
    text = re.sub(r"^\s*[-*]\s+", "", text)
    ym = re.search(r"\b((?:19|20)\d{2})[a-z]?\b", text)
    if CJK.match(text):
        nm = re.match(r"([\u4e00-\u9fff]{2,4})", text)
        name = nm.group(1) if nm else ""
    else:
        nm = re.match(rf"((?:(?:van|von|de|der|den|da|di|du|le|la|del)\s)?[A-ZÀ-ÖØ-Þ](?:{_L}|['’\-])+)", text)
        name = nm.group(1) if nm else ""
    return Ref(text, buf[0].no, name, ym.group(1) if ym else "")


def numeric_citations(doc: Doc, secs: list[Section]) -> list[tuple[int, int]]:
    out = []
    for s in secs:
        if is_refs_h(s.heading):
            continue
        for ln in s.lines:
            for m in re.finditer(r"\[(\d+(?:\s*[-–,]\s*\d+)*)\]", ln.text):
                for part in m.group(1).split(","):
                    if re.search(r"[-–]", part):
                        a, b = re.split(r"\s*[-–]\s*", part.strip())[:2]
                        out.extend((k, ln.no) for k in range(int(a), int(b) + 1) if int(b) - int(a) < 50)
                    elif part.strip().isdigit():
                        out.append((int(part.strip()), ln.no))
    return out


# ----------------------------------------------------------------------------- checks

class Checker:
    def __init__(self, doc: Doc, rules: dict, venue: str, blind: bool | None, online: bool):
        self.doc, self.rules, self.venue, self.online = doc, rules, venue, online
        mode = (rules.get("review_mode") or {}).get("value")
        self.blind = blind if blind is not None else (mode in {"double-blind", "triple-blind"})
        self.blind_known = blind is not None or mode is not None
        self.secs = sections(doc)
        self.findings: list[Finding] = []
        self.reminders: list[str] = []
        self.checked: list[str] = []
        self.not_checked: list[str] = []
        self.stats: dict = {}

    # helpers
    def add(self, check: str, severity: str, message: str, where: str = "", statement: str = "") -> None:
        self.findings.append(Finding(check, severity, message, where, owner_of(check), statement))

    def loc(self, no: int) -> str:
        return f"{self.doc.loc_unit} {no}" if no else ""

    def rule(self, key: str):
        r = self.rules.get(key)
        return r.get("value") if isinstance(r, dict) else None

    def sev(self, key: str) -> str:
        """FAIL for a hard limit; FLAG when the venue words it as a guideline ("about",
        "preferably no more than") and the rules block marks it ``"soft": true``."""
        r = self.rules.get(key)
        return "FLAG" if isinstance(r, dict) and r.get("soft") else "FAIL"

    def soft_note(self, key: str) -> str:
        return " (a guideline, not a hard cap)" if self.sev(key) == "FLAG" else ""

    def run(self) -> None:
        for fn in (self.lengths, self.abstract_structure, self.keywords, self.anonymity,
                   self.statements, self.references, self.exhibits, self.numbers, self.leftovers):
            fn()
        if self.online:
            self.online_refs()
        self.reference_count()
        self.stars()
        self.venue_reminders()
        self.unimplemented()

    # Rules preflight tests. Anything else with a value is either a portal reminder or is
    # listed as not checked — a rule in the block must never pass silently.
    TESTED = {
        "main_text_pages_max", "main_text_words_max", "total_words_max", "abstract_words_max",
        "abstract_chars_max", "main_text_chars_max", "keywords_min", "keywords_max", "title_words_max",
        "title_chars_max", "words_per_exhibit", "exhibits_max", "review_mode", "abstract_format",
        "jel_codes_required", "keywords_required", "page_limit_includes_references", "required_statements",
        "separate_upload_statements", "conditional_statements", "significance_stars", "references_max",
    }
    REMINDER = {
        "cover_letter": "Cover letter", "llm_policy": "AI/LLM policy", "data_code_policy": "Data & code policy",
        "file_format": "File format", "supplement_policy": "Supplement", "anonymized_supplement_required":
        "Anonymized supplement required", "preprint_policy": "Preprints", "submission_fee": "Submission fee",
        "apc": "APC", "portal": "Portal", "template": "Template", "reference_style": "Reference style",
        "language": "Language",
    }

    def venue_reminders(self) -> None:
        for key, label in self.REMINDER.items():
            val = self.rule(key)
            if val is None or val is False:
                continue
            self.reminders.append(f"{label}: {'yes' if val is True else val}")
        has_refs = any(ln.heading and is_refs_h(ln.text) for ln in self.doc.lines)
        app = next((ln for ln in self.doc.lines if ln.heading and is_appendix_h(ln.text)), None)
        if app and has_refs and any(self.rule(k) for k in ("main_text_words_max", "main_text_pages_max", "total_words_max")):
            self.add("LEN-APPENDIX", "INFO", f"An appendix ('{app.text[:40]}') is bound into this file. It was excluded from "
                     "the counts above; check whether the venue counts in-file appendices or wants them uploaded "
                     "separately.", self.loc(app.no))

    def unimplemented(self) -> None:
        for key, rule in self.rules.items():
            if key in self.TESTED or key in self.REMINDER or not isinstance(rule, dict):
                continue
            if rule.get("value") is not None:
                self.not_checked.append(f"venue rule {key} = {rule['value']} (preflight does not test it yet)")

    def reference_count(self) -> None:
        cap = self.rule("references_max")
        if not cap:
            return
        if self.doc.fmt == "tex" and self.doc.bib_keys:
            # a .bib may hold more entries than the paper uses; count what is cited then
            n = (len(self.doc.bib_keys) if not self.doc.metadata.get("bib_files")
                 else len({k for k, _ in self.doc.cite_keys if k in self.doc.bib_keys}))
        else:
            n = len(reference_entries(self.doc, self.secs))
        if not n:
            self.not_checked.append(f"reference count ≤ {cap} (no reference list found)")
            return
        self.stats["references_counted"] = n
        self.checked.append(f"≤ {cap} references")
        if n > cap:
            self.add("LEN-REFS", self.sev("references_max"), f"{n} references; the venue allows {cap}"
                     f"{self.soft_note('references_max')}.")

    def stars(self) -> None:
        policy = self.rule("significance_stars")
        if policy not in {"prohibited", "discouraged"}:
            return
        self.checked.append("no significance asterisks")
        if self.doc.fmt in {"md", "tex", "txt"}:
            raw = (_expand_inputs(self.doc.path) if self.doc.fmt == "tex"
                   else self.doc.path.read_text(encoding="utf-8", errors="replace")).replace("\\*", "*")
            rows = [(i, l) for i, l in enumerate(raw.splitlines(), 1)
                    if l.lstrip().startswith("|") or "&" in l or self.doc.fmt == "txt"]
        else:
            rows = [(ln.no, ln.text) for ln in self.doc.lines]
        pat = re.compile(r"[-−]?\d*\.\d+\)?\s*(?:\$?\^\{?\s*)?(?:[*∗]{1,3}|\\ast)")
        hits = [(i, l) for i, l in rows if pat.search(l)]
        if hits:
            self.add("EXH-STARS", "FLAG" if policy == "prohibited" else "INFO",
                     f"Significance asterisks in {len(hits)} table row(s) (first: '{hits[0][1].strip()[:70]}'); the venue "
                     f"{'does not allow' if policy == 'prohibited' else 'discourages'} them — report standard errors or "
                     "confidence intervals instead.",
                     (f"line {hits[0][0]} of the source with \\input files expanded" if self.doc.fmt == "tex"
                      else self.loc(hits[0][0])))

    # ---- lengths
    def lengths(self) -> None:
        abstract, where = abstract_text(self.doc, self.secs)
        cjk = is_cjk(abstract or self.doc.title)
        self.stats["abstract_words"] = count_words(abstract)
        self.stats["abstract_chars"] = count_chars(abstract)
        lim_w, lim_c = self.rule("abstract_words_max"), self.rule("abstract_chars_max")
        if not abstract:
            self.add("LEN-ABSTRACT", "FLAG", "No abstract found (looked for an 'Abstract' / '摘要' heading or environment).")
        elif lim_c and cjk:
            n = count_chars(abstract)
            self.checked.append(f"abstract ≤ {lim_c} 字")
            if n > lim_c:
                self.add("LEN-ABSTRACT", self.sev("abstract_chars_max"), f"Abstract is {n} 字; the venue limit is {lim_c}{self.soft_note('abstract_chars_max')}.", where)
        elif lim_w:
            n = count_words(abstract)
            self.checked.append(f"abstract ≤ {lim_w} words")
            if n > lim_w:
                self.add("LEN-ABSTRACT", self.sev("abstract_words_max"), f"Abstract is {n} words; the venue limit is {lim_w}{self.soft_note('abstract_words_max')}.", where)
        else:
            self.not_checked.append("abstract length (no limit in the venue rules)")

        body = main_body(self.secs)
        body_text = "\n".join(ln.text for s in body for ln in s.lines if ln.kind in {"text"}
                              and not NOTE_LINE.match(ln.text) and not self._is_statement_heading(s.heading))
        words = count_words(body_text)
        chars = count_chars(body_text)
        self.stats.update(main_text_words=words, main_text_chars=chars)
        lim = self.rule("main_text_words_max")
        n_ex = self._main_exhibits()
        self.stats["main_exhibits"] = n_ex
        wpe = self.rule("words_per_exhibit")
        if lim and wpe:
            # e.g. AER: Insights — 7,000 words with no exhibits, 200 fewer for each one.
            lim = lim - wpe * n_ex
            self.stats["word_cap_after_exhibits"] = lim
        exmax = self.rule("exhibits_max")
        if exmax:
            self.checked.append(f"≤ {exmax} main-text exhibits")
            if n_ex > exmax:
                self.add("LEN-EXHIBITS", "FAIL", f"{n_ex} tables/figures in the main text; the venue allows at most {exmax}. "
                         "Move the rest to the appendix or supplement.")
        if lim:
            self.checked.append(f"main text ≤ {lim} words" + (f" ({self.rule('main_text_words_max')} − {wpe} × {n_ex} exhibits)"
                                                             if wpe else ""))
            if words > lim:
                self.add("LEN-WORDS", self.sev("main_text_words_max"), f"Main text is ~{words} words (abstract, tables, captions, "
                         f"references, appendix and statements excluded); the venue limit is {lim}.")
            elif words > 0.95 * lim:
                self.add("LEN-WORDS", "FLAG", f"Main text is ~{words} words, within 5% of the {lim}-word limit; "
                         "the venue's own counting rule may differ.")
        limc = self.rule("main_text_chars_max")
        if limc:
            self.checked.append(f"main text ≤ {limc} 字")
            if chars > limc:
                self.add("LEN-WORDS", self.sev("main_text_chars_max"), f"Main text is ~{chars} 字; the venue limit is {limc}{self.soft_note('main_text_chars_max')}.")
        total = self.rule("total_words_max")
        if total:
            all_words = count_words("\n".join(ln.text for ln in self.doc.lines))
            self.checked.append(f"total ≤ {total} words")
            if all_words > total:
                self.add("LEN-WORDS", "FAIL", f"Manuscript is ~{all_words} words in total; the venue limit is {total}.")

        pages = self.rule("main_text_pages_max")
        if pages:
            incl_refs = bool(self.rule("page_limit_includes_references"))
            if self.doc.pages:
                main_pages = self.doc.pages
                if not incl_refs and self.doc.ref_start_page:
                    main_pages = self.doc.ref_start_page
                self.stats["pages"] = self.doc.pages
                self.stats["main_text_pages"] = main_pages
                self.checked.append(f"main text ≤ {pages} pages")
                if main_pages > pages:
                    self.add("LEN-PAGES", "FAIL", f"Main text runs to page {main_pages} "
                             f"({'including' if incl_refs else 'before'} references); the venue limit is {pages} pages.")
            else:
                wpp = 850 if self._two_column() else 400
                est = round(words / wpp, 1)
                self.stats["estimated_pages"] = est
                self.not_checked.append(f"exact page count (source format; estimated ~{est} pages at ~{wpp} words/page — "
                                        "compile to PDF and rerun on the PDF)")
                if est > 1.25 * pages:
                    self.add("LEN-PAGES", "FLAG", f"Estimated ~{est} pages of main text against a {pages}-page limit. "
                             "Compile to PDF and rerun for an exact count.")
        tw = self.rule("title_words_max")
        if tw and count_words(self.doc.title) > tw:
            self.add("LEN-TITLE", self.sev("title_words_max"), f"Title is {count_words(self.doc.title)} words; the limit is {tw}{self.soft_note('title_words_max')}.")
        tc = self.rule("title_chars_max")
        if tc and len(self.doc.title) > tc:
            self.add("LEN-TITLE", self.sev("title_chars_max"), f"Title is {len(self.doc.title)} characters; the limit is {tc}{self.soft_note('title_chars_max')}.")

    def _main_exhibits(self) -> int:
        """Distinct tables + figures before the references/appendix (appendix series excluded)."""
        stop = next((ln.no for ln in self.doc.lines if ln.heading and (is_refs_h(ln.text) or is_appendix_h(ln.text))),
                    None)
        if self.doc.fmt == "tex":
            return sum(1 for t in self.doc.tex_tables if stop is None or t["line"] < stop)
        seen = set()
        for s in main_body(self.secs):
            for ln in s.lines:
                m = caption_match(ln.text)
                if m and not m.group(2):
                    series = {"Fig.": "Figure", "表": "Table", "图": "Figure"}.get(m.group(1), m.group(1))
                    seen.add((series, exhibit_number(m.group(3))))
        return len(seen)

    def _two_column(self) -> bool:
        if self.doc.fmt != "tex":
            return False
        head = self.doc.path.read_text(encoding="utf-8", errors="replace")[:4000]
        return bool(re.search(r"twocolumn|\{icml|\{acl|\{neurips|\{iclr|cvpr|aaai|ieeeconf|IEEEtran|sigconf|acmart", head))

    def _is_statement_heading(self, h: str) -> bool:
        core = heading_core(h)
        return any(re.search(p, core, re.I) for k, p in STATEMENT_PATTERNS.items()
                   if k not in {"keywords", "jel_codes", "reporting_guideline"}) and len(core) < 60

    # ---- abstract structure
    def abstract_structure(self) -> None:
        fmt = self.rule("abstract_format")
        required = "structured_abstract" in (self.rule("required_statements") or [])
        if fmt != "structured" and not required:
            return
        abstract, where = abstract_text(self.doc, self.secs)
        heads = re.findall(r"(?:^|\n|\.\s)\s*(importance|objectives?|background|purpose|aims?|design|setting|participants|"
                           r"interventions?|exposures?|methods?|main outcomes?(?: and measures)?|results|findings|"
                           r"conclusions?(?: and relevance)?|interpretation|trial registration|funding)\s*[:：]",
                           abstract, re.I)
        self.checked.append("structured abstract")
        first = abstract.strip()[:80]
        opens_labelled = re.match(r"(importance|objectives?|background|purpose|aims?|context|introduction|design|"
                                  r"rationale|question)\s*[:：]", first, re.I)
        if len(set(h.lower() for h in heads)) >= 3 and not opens_labelled:
            self.add("ABS-STRUCTURE", "FLAG", "The structured abstract opens with unlabelled text "
                     f"('{first[:50]}…'); the venue's headings (e.g. Importance/Objective/Design…) should start it.", where)
        if len(set(h.lower() for h in heads)) < 3:
            self.add("ABS-STRUCTURE", "FAIL", "The venue requires a structured abstract, but fewer than three labelled "
                     "parts (e.g. Objective: / Methods: / Results: / Conclusions:) were found.", where)

    # ---- keywords
    def keywords(self) -> None:
        kmin, kmax = self.rule("keywords_min"), self.rule("keywords_max")
        line = next((ln for ln in self.doc.lines if KW_LINE.match(ln.text)), None)
        if line is None and self.doc.front:
            m = next((x for x in self.doc.front.splitlines() if KW_LINE.match(x)), None)
            line = Line(0, m) if m else None
        if line is None:
            return  # absence is STMT-MISSING's job when the venue requires keywords
        kw_text = re.split(r"\bJEL\b|JEL\s*分类号", KW_LINE.sub("", line.text))[0]
        items = [x for x in re.split(r"[;,，；、]", kw_text) if x.strip(" .。")]
        self.stats["keywords"] = len(items)
        if kmin and len(items) < kmin:
            self.add("KW-COUNT", "FLAG", f"{len(items)} keywords; the venue asks for at least {kmin}.", self.loc(line.no))
        if kmax and len(items) > kmax:
            self.add("KW-COUNT", "FLAG", f"{len(items)} keywords; the venue allows at most {kmax}.", self.loc(line.no))
        if kmin or kmax:
            self.checked.append("keyword count")

    # ---- anonymity
    def anonymity(self) -> None:
        if not self.blind:
            mode = self.rule("review_mode")
            if mode in {"single-blind", "open"} and re.search(r"anonym|匿名", self.doc.front or "", re.I):
                self.add("ANON-AUTHOR", "INFO", f"The venue reviews {mode}; an anonymized author block is allowed by "
                         "some single-blind journals but others require names, affiliations and contact details on "
                         "the title page — check the pack's *-submission skill.", "front matter")
            if not self.blind_known:
                self.not_checked.append("anonymization (review mode unknown — pass --blind if the venue is double-blind)")
            return
        self.checked.append("anonymization (double-blind)")
        front = self.doc.front.strip()
        if front and not re.search(r"anonymous|anonymized|匿名|blind", front, re.I):
            lines = [x.strip() for x in front.splitlines() if x.strip()]
            who = (next((x for x in lines if re.search(r"@|universit|institut|college|school|department|大学|研究院|学院", x, re.I)), None)
                   or next((x for x in lines if re.fullmatch(r"[A-Z][a-zà-ÿ'’\-]+(?:\s+[A-Z]\.?)*(?:\s+[A-Z][a-zà-ÿ'’\-]+)+[∗*†‡§¶\d,\s]*", x)), None)
                   or (lines[-1] if lines else front))
            self.add("ANON-AUTHOR", "FAIL", f"Author block is not anonymized: '{who[:90]}'. Double-blind review requires "
                     "removing names, affiliations and emails.", "front matter")
        emails = [(m.group(0), ln.no) for ln in self.doc.lines
                  for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.-]+", ln.text)
                  if not re.search(r"anonymous|example\.(com|org)", m.group(0), re.I)]
        if emails and not (front and not re.search(r"anonymous", front, re.I)):
            e, no = emails[0]
            self.add("ANON-AUTHOR", "FAIL", f"Email address '{e}' identifies an author.", self.loc(no))
        selfcite = re.compile(
            r"\b(?:in|as in|see|following|extends?|extending|building on|builds on)?\s*our\s+(?:own\s+)?"
            r"(?:previous|prior|earlier|recent|past|companion)\s+(?:work|paper|study|studies|results?|analysis|findings)"
            r"|\bwe\s+(?:previously|earlier)\s+(?:showed|proposed|introduced|developed|found|reported)"
            r"|本文作者(?:此前|先前)|我们(?:在)?(?:此前|先前|之前|前期|以往|早期)(?:的)?(?:研究|工作|论文)", re.I)
        for ln in self.doc.lines:
            if ln.kind == "front":
                continue
            m = selfcite.search(ln.text)
            if m:
                self.add("ANON-SELFCITE", "FAIL", f"Self-revealing citation: '…{ln.text[max(0, m.start() - 20): m.end() + 40]}…'. "
                         "Cite your own work in the third person.", self.loc(ln.no))
                break
        ack_head = next((ln for ln in self.doc.lines if ln.heading
                         and re.search(STATEMENT_PATTERNS["acknowledgments"], heading_core(ln.text), re.I)), None)
        ack_text = next((ln for ln in self.doc.lines if ln.kind != "front" and re.search(
            r"\bwe (?:thank|are grateful|gratefully acknowledge)|\bgrateful to\b|\bthanks? (?:are due )?to\b.*\bfor\b|"
            r"\b(?:grant|award)\s+(?:no\.?|number|#)\s*[A-Z0-9-]{3,}|国家自然科学基金|感谢", ln.text, re.I)), None)
        thanks = self.doc.fmt == "tex" and re.search(r"\\thanks\{", self.doc.path.read_text(encoding="utf-8", errors="replace"))
        hit = ack_head or ack_text
        if hit or thanks:
            where = self.loc(hit.no) if hit else "\\thanks{}"
            self.add("ANON-ACK", "FAIL", "Acknowledgments / funding / thanks present in a double-blind submission; "
                     "remove them until the camera-ready version.", where)
        for ln in self.doc.lines:
            for m in re.finditer(r"https?://(?:www\.)?(github\.com|gitlab\.com|bitbucket\.org|huggingface\.co|osf\.io|"
                                 r"sites\.google\.com|[\w.-]+\.(?:edu|ac\.[a-z]{2})/~?[\w.-]+)/?([\w.-]*)[^\s)]*", ln.text):
                url = m.group(0).rstrip(".,;:")
                if re.search(r"anonym", url, re.I):
                    continue
                ours = re.search(r"\b(our|we release|we provide|we make|code (?:is|will be) (?:available|released)|"
                                 r"available at|implementation is|本文代码)", ln.text, re.I)
                self.add("ANON-URL", "FAIL" if ours else "FLAG",
                         f"Non-anonymous link {url}" + (" presented as the authors' own code/data; use an anonymized "
                         "mirror (e.g. anonymous.4open.science)." if ours else " — confirm it is not your own repository."),
                         self.loc(ln.no))
        for key in ("author", "creator", "lastModifiedBy"):
            val = self.doc.metadata.get(key)
            if val and not re.search(r"anonym|latex|tex|word|pdf|acrobat|microsoft|quartz|skia|cairo|chrome|overleaf",
                                     val, re.I):
                self.add("ANON-META", "FAIL", f"File metadata field '{key}' = '{val}' identifies an author; "
                         "clear document properties before upload.", "file metadata")
                break

    # ---- required statements
    def statements(self) -> None:
        for name in self.rule("separate_upload_statements") or []:
            self.reminders.append(f"{STATEMENT_LABEL.get(name, name)}: required as a separate upload or form field, "
                                  "not inside the manuscript" + (" (keep it out of the anonymized file)" if self.blind else ""))
        for name in self.rule("conditional_statements") or []:
            if not has_statement(self.doc, name):
                note = (self.rules.get("conditional_statements") or {}).get("note", "")
                self.reminders.append(f"{STATEMENT_LABEL.get(name, name)}: required only in some cases — {note[:160]}")
        req = list(self.rule("required_statements") or [])
        if self.rule("jel_codes_required") and "jel_codes" not in req:
            req.append("jel_codes")
        if self.rule("keywords_required") and "keywords" not in req:
            req.append("keywords")
        if not req:
            if self.rule("separate_upload_statements") or self.rule("conditional_statements"):
                self.checked.append("in-manuscript statements (the venue requires none; uploads listed in the portal checklist)")
            else:
                self.not_checked.append("required statements (none listed in the venue rules)")
            return
        for name in req:
            if name == "structured_abstract":
                continue
            if name in {"acknowledgments"} and self.blind:
                continue  # never demand acknowledgments in a blind submission
            if name == "reproducibility_checklist" and not has_statement(self.doc, name):
                # Usually filed on the submission form (ARR, NeurIPS-style OpenReview forms),
                # so its absence from the PDF is not evidence it is missing.
                self.add("STMT-MISSING", "INFO", "No reproducibility/paper checklist in this file — confirm it is "
                         "completed on the submission form or appended after the references.", statement=name)
                continue
            if not has_statement(self.doc, name):
                self.add("STMT-MISSING", "FAIL", f"{STATEMENT_LABEL.get(name, name)} is required by the venue but was not "
                         "found (looked for a heading or a labelled paragraph).", statement=name)
        self.checked.append(f"required statements: {', '.join(req)}")

    # ---- references
    def references(self) -> None:
        doc = self.doc
        if doc.fmt in {"pdf", "txt"}:
            # LaTeX renders an undefined \cite as "(?)" or "[?]"
            for ln in doc.lines:
                if ln.kind != "front" and re.search(r"\((?:\?\s*[,;]?\s*)+\)|\[\?\]", ln.text):
                    m = re.search(r".{0,40}(?:\((?:\?\s*[,;]?\s*)+\)|\[\?\]).{0,20}", ln.text)
                    self.add("REF-MISSING", "FAIL", f"Unresolved citation rendered as '?': '…{m.group(0)}…' — a cited "
                             "key has no bibliography entry.", self.loc(ln.no))
        if doc.fmt == "tex" and (doc.cite_keys or doc.bib_keys):
            if not doc.bib_keys:
                self.not_checked.append("citation ↔ bibliography (no \\bibitem and no readable .bib — pass --bib refs.bib)")
                return
            cited = {k for k, _ in doc.cite_keys}
            missing = [(k, ln) for k, ln in doc.cite_keys if k not in doc.bib_keys]
            seen = set()
            for k, ln in missing:
                if k in seen:
                    continue
                seen.add(k)
                self.add("REF-MISSING", "FAIL", f"\\cite{{{k}}} has no bibliography entry (renders as [?]).", self.loc(ln))
            if not doc.nocite_all and not doc.metadata.get("bib_files"):
                for k, ln in doc.bib_keys.items():
                    if k not in cited:
                        self.add("REF-UNCITED", "FLAG", f"Bibliography entry '{k}' is never cited.", self.loc(ln))
            self.checked.append("citations ↔ bibliography")
            return
        refs = reference_entries(doc, self.secs)
        if not refs:
            self.not_checked.append("citations ↔ reference list (no reference list found)")
            return
        nums = numeric_citations(doc, self.secs)
        if nums and len(nums) >= 3 and not text_citations(doc, self.secs):
            n = len(refs)
            for k, ln in nums:
                if k > n:
                    self.add("REF-MISSING", "FAIL", f"Citation [{k}] but the reference list has {n} entries.", self.loc(ln))
            used = {k for k, _ in nums}
            for i, r in enumerate(refs, 1):
                if i not in used:
                    self.add("REF-UNCITED", "FLAG", f"Reference [{i}] is never cited: {r.text[:80]}", self.loc(r.line))
            self.checked.append("numbered citations ↔ reference list")
            return
        cites = text_citations(doc, self.secs)
        index = {}
        for r in refs:
            index.setdefault((norm_name(r.name), r.year), r)
        names_by_year = {}
        for r in refs:
            names_by_year.setdefault(r.year, set()).add(norm_name(r.name))
        # A CJK narrative cite can capture leading characters ("遵循江艇（2022）"): resolve it
        # to a same-year reference whose author name it ends with.
        for c in cites:
            if CJK.match(c.name) and (norm_name(c.name), c.year[:4]) not in index:
                for r in refs:
                    if r.year == c.year[:4] and r.name and CJK.match(r.name) and c.name.endswith(r.name):
                        c.name = r.name
                        break
        seen = set()
        for c in cites:
            key = (norm_name(c.name), c.year[:4])
            if key in index or key in seen:
                continue
            # tolerate a cite whose surname appears anywhere in a same-year entry (co-author first)
            if any(c.name.lower() in r.text.lower()[:120] and r.year == c.year[:4] for r in refs):
                continue
            seen.add(key)
            self.add("REF-MISSING", "FAIL", f"'{c.name} ({c.year})' is cited but has no reference-list entry.", self.loc(c.line))
        cited = {(norm_name(c.name), c.year[:4]) for c in cites}
        cited_names = {norm_name(c.name) for c in cites}
        for r in refs:
            k = (norm_name(r.name), r.year)
            if k in cited:
                continue
            if any(norm_name(c.name) in norm_name(r.text[:150]) and c.year[:4] == r.year for c in cites):
                continue
            if not r.name or norm_name(r.name) not in cited_names and not any(
                    norm_name(c.name) and norm_name(c.name) in norm_name(r.text[:150]) for c in cites):
                self.add("REF-UNCITED", "FLAG", f"Reference never cited in the text: {r.text[:90]}", self.loc(r.line))
            elif r.name:
                self.add("REF-UNCITED", "FLAG", f"Reference never cited with this year: {r.text[:90]}", self.loc(r.line))
        self.stats["references"] = len(refs)
        self.stats["in_text_citations"] = len(cites)
        self.checked.append("author-year citations ↔ reference list")

    def online_refs(self) -> None:
        refs = reference_entries(self.doc, self.secs)
        if self.doc.fmt == "tex" and not refs:
            self.not_checked.append("online reference check (tex .bib entries are not parsed into text; run on the PDF)")
            return
        ua = {"User-Agent": "AJS-preflight/1.0 (+https://github.com/brycewang-stanford/Awesome-Journal-Skills)"}
        checked = declined = 0
        grey = re.compile(r"working paper|discussion paper|arxiv|ssrn|nber|mimeo|preprint|unpublished|"
                          r"dissertation|thesis|工作论文|讨论稿", re.I)
        for r in refs[:80]:
            if grey.search(r.text) and not re.search(r"\b10\.\d{4,9}/", r.text):
                self.add("REF-UNRESOLVED", "INFO", f"Grey literature, not Crossref-indexed — check by hand: {r.text[:90]}",
                         self.loc(r.line))
                continue
            doi = re.search(r"\b10\.\d{4,9}/[^\s\"<>]+", r.text)
            try:
                if doi:
                    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi.group(0).rstrip(".,;"))
                    req = urllib.request.Request(url, headers=ua)
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        ok = resp.status == 200
                else:
                    q = urllib.parse.urlencode({"query.bibliographic": r.text[:300], "rows": 1})
                    req = urllib.request.Request("https://api.crossref.org/works?" + q, headers=ua)
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        items = json.load(resp)["message"]["items"]
                    title = (items[0].get("title") or [""])[0] if items else ""
                    a = set(WORD.findall(title.lower()))
                    b = set(WORD.findall(r.text.lower()))
                    ok = bool(a) and len(a & b) / len(a) >= 0.6
                checked += 1
                if not ok:
                    self.add("REF-UNRESOLVED", "FLAG", f"Could not match this reference on Crossref — confirm it exists "
                             f"and the details are right: {r.text[:100]}", self.loc(r.line))
            except urllib.error.HTTPError as e:
                if e.code == 404 and doi:
                    checked += 1
                    self.add("REF-UNRESOLVED", "FAIL", f"DOI {doi.group(0)} does not resolve on Crossref.", self.loc(r.line))
                else:
                    declined += 1  # 401/403/429/5xx say nothing about the reference
            except Exception:
                declined += 1
        self.checked.append(f"online reference existence (Crossref; {checked} checked, {declined} not answered)")

    # ---- exhibits
    def exhibits(self) -> None:
        doc = self.doc
        if doc.fmt == "tex":
            refd = {k for k, _ in doc.refs}
            for t in doc.tex_tables:
                if t["label"] and t["label"] not in refd:
                    self.add("EXH-UNREFERENCED", "FLAG", f"{t['kind'].title()} '{t['label']}' is never referenced in the text.",
                             self.loc(t["line"]))
                if t["kind"] == "table":
                    self._se_note(t["text"], self.loc(t["line"]), t["label"] or "table")
            src = doc.path.read_text(encoding="utf-8", errors="replace")
            # \setcounter{table}{0} restarts numbering for an appendix series (A1, A2, …) —
            # standard practice. Only a manual offset breaks consecutive numbering.
            for m in re.finditer(r"\\(?:addtocounter\{(table|figure)\}\{[^}]*\}|setcounter\{(table|figure)\}\{\s*[1-9][^}]*\})", src):
                kind = m.group(1) or m.group(2)
                self.add("EXH-NUMBERING", "FLAG", f"\\{m.group(0)[1:]} changes the {kind} counter by hand, so "
                         f"{kind}s will not be numbered consecutively.", self.loc(src[: m.start()].count("\n") + 1))
            for k, ln in doc.refs:
                if k not in doc.labels:
                    self.add("LEFTOVER-MARKER", "FAIL", f"\\ref{{{k}}} points to an undefined label (renders as ??).", self.loc(ln))
            self.checked.append("exhibits referenced; table notes")
            return
        ref = re.compile(r"\b(Tables?|Figures?|Figs?\.|Exhibits?)\s+((?:[IVXL]+\b|[A-Z]?\d+[a-z]?)(?:\s*(?:,|and|&|–|-|to)\s*(?:[IVXL]+\b|[A-Z]?\d+[a-z]?))*)"
                         r"|(表|图)\s*([A-Z]?\d+)(?:\s*[-–至和、]\s*([A-Z]?\d+))?")
        defs: dict[tuple[str, str], list[tuple[int, int]]] = {}
        cap_lines = set()
        for idx, ln in enumerate(doc.lines):
            m = caption_match(ln.text)
            if m and (ln.kind == "caption" or len(ln.text) < 220):
                series = {"Fig.": "Figure", "表": "Table", "图": "Figure"}.get(m.group(1), m.group(1))
                defs.setdefault((series, m.group(2)), []).append((exhibit_number(m.group(3)), ln.no))
                cap_lines.add(idx)
        if not defs:
            self.not_checked.append("table/figure numbering (no captions found)")
            return
        used: set[tuple[str, str, int]] = set()
        for idx, ln in enumerate(doc.lines):
            if idx in cap_lines:
                continue
            for m in ref.finditer(ln.text):
                if m.group(1):
                    series = "Figure" if m.group(1).lower().startswith("fig") else ("Exhibit" if m.group(1).lower().startswith("exh") else "Table")
                    nums = re.findall(r"([A-Z]?)(\d+)", m.group(2))
                    nums += [("", str(exhibit_number(r))) for r in re.findall(r"\b([IVXL]+)\b", m.group(2))]
                    span = re.search(r"([A-Z]?)(\d+)\s*(?:–|-|to)\s*([A-Z]?)(\d+)", m.group(2))
                    if span and int(span.group(4)) - int(span.group(2)) < 30:
                        nums += [(span.group(1), str(k)) for k in range(int(span.group(2)), int(span.group(4)) + 1)]
                else:
                    series = "Table" if m.group(3) == "表" else "Figure"
                    nums = [re.match(r"([A-Z]?)(\d+)", m.group(4)).groups()]
                    if m.group(5):
                        a, b = int(re.sub(r"\D", "", m.group(4))), int(re.sub(r"\D", "", m.group(5)))
                        nums += [("", str(k)) for k in range(a, b + 1)]
                for prefix, n in nums:
                    used.add((series, prefix, int(n)))
        for (series, prefix), items in sorted(defs.items()):
            nums = [n for n, _ in items]
            expected = list(range(1, len(nums) + 1))
            if sorted(set(nums)) != expected:
                gap = sorted(set(expected) - set(nums)) or sorted(set(nums) - set(expected))
                self.add("EXH-NUMBERING", "FLAG", f"{series}s {prefix}{', '.join(str(n) for n in nums)} are not numbered "
                         f"consecutively (check {series.lower()} {prefix}{gap[0]}).", self.loc(items[0][1]))
            elif nums != sorted(nums):
                self.add("EXH-NUMBERING", "FLAG", f"{series}s {prefix}* appear out of order: {nums}.", self.loc(items[0][1]))
            for n, line in items:
                if (series, prefix, n) not in used:
                    self.add("EXH-UNREFERENCED", "FLAG", f"{series} {prefix}{n} is never referenced in the text.", self.loc(line))
        # table notes (md/docx/pdf): the block from a Table caption to the next caption/heading
        lines = doc.lines
        for idx in sorted(cap_lines):
            m = caption_match(lines[idx].text)
            if not m or m.group(1) not in {"Table", "表", "Exhibit"}:
                continue
            block = []
            k = idx
            for k in range(idx, min(len(lines), idx + 400)):  # PDF tables come out one cell per line
                ln = lines[k]
                if k != idx and (ln.heading or caption_match(ln.text)):
                    break
                block.append(ln.text)
                if ln.kind == "text" and k != idx and re.match(r"^\s*(notes?|注|说明)\s*[:：.]", ln.text, re.I):
                    # a note broken by a PDF page break continues in lowercase
                    for nxt in lines[k + 1: k + 3]:
                        if nxt.heading or caption_match(nxt.text) or not nxt.text[:1].islower():
                            break
                        block.append(nxt.text)
                    break
            self._se_note("\n".join(block), self.loc(lines[idx].no), f"Table {m.group(2)}{m.group(3)}")
        self.checked.append("exhibit numbering and cross-references; table notes")

    @staticmethod
    def _se_row(row: str) -> bool:
        """A row of only parenthesized numbers — the (SE) line under a row of estimates.
        'Mean (SD)' rows in descriptive tables mix bare and parenthesized numbers."""
        paren = re.findall(r"[(（\[]\s*[-−–]?\d*\.\d+\s*[)）\]]", row)
        bare = re.findall(r"(?<![(（\[\d.,])[-−–]?\d[\d,]*(?:\.\d+)?(?![\d.,]*[)）\]])", row)
        return len(paren) >= 2 and not bare

    def _se_note(self, text: str, where: str, name: str) -> None:
        # A row count alone does not make a regression table (descriptive tables have N too):
        # require estimation vocabulary, or the standard layout of estimates over (SEs).
        regression = (re.search(r"\b(R-?squared|R\s?\^?2|adj(?:usted)?\.? R|fixed effects|controls|"
                                r"denote (?:statistical )?significance|significant at the|2SLS|OLS|regressions?)\b|"
                                r"\bp\s*<\s*0?\.\d|"
                                r"固定效应|控制变量|显著性水平|水平上显著", text, re.I)
                      or any(self._se_row(row) for row in re.split(r"\n|\\\\", text)))
        if not regression:
            return
        # "robust"/"稳健" alone is not enough: "doubly robust estimator" / "双重稳健估计量" names
        # an estimator, not the standard errors.
        if not re.search(r"standard errors?|std\.? err|\bs\.e\.|robust (?:standard|s\.?e)|cluster|t-stat|z-stat|"
                         r"bootstrap|heteroskedastic|Newey|confidence intervals?|标准误|聚类|自助法|t\s*值|t\s*统计量|"
                         r"standard deviations?|\bstd\b|±\s*(?:std|sd|s\.d\.)|over \d+ (?:random )?seeds|标准差",
                         text, re.I):
            self.add("EXH-SE-NOTE", "FLAG", f"{name} looks like a regression table but its note does not say what the "
                     "standard errors are (type, clustering level) or what the parentheses contain.", where)

    # ---- numbers
    def numbers(self) -> None:
        abstract, _ = abstract_text(self.doc, self.secs)
        claim_lines = [("abstract", ln) for s in self.secs if is_abstract_h(s.heading) for ln in s.lines
                       if not KW_LINE.match(ln.text) and not JEL_LINE.match(ln.text)]
        # The introduction includes its own sub-headings (\paragraph{Related literature.},
        # "1.1 Contribution") up to the next heading at the same or a higher level.
        start = next((k for k, s in enumerate(self.secs) if is_intro_h(s.heading)), None)
        if start is not None:
            level = self.secs[start].level
            for s in self.secs[start:]:
                if s is not self.secs[start] and s.level <= level:
                    break
                claim_lines += [("introduction", ln) for ln in s.lines]
        if not claim_lines:
            return
        claim_ids = {id(ln) for _, ln in claim_lines}
        rest = " ".join(ln.text for ln in self.doc.lines if id(ln) not in claim_ids)
        rest += " " + " ".join(t["text"] for t in self.doc.tex_tables)
        pool = set(self._nums(rest))
        # Headline claims are often a difference between two cells ("+3.4 points over
        # ERM") or a relative change, which no table prints. Both are computed per table,
        # but only consulted when the sentence makes a comparison (and relative changes only
        # for percentages): an unconditional pool of every pairwise difference covers so
        # many one-decimal values that a wrong headline number almost always "matches".
        # (value, decimals) of every derived quantity; operands must share the claim's
        # precision, which keeps "3.4 = 71.2 − 67.8" while refusing "6.4 = 312.9 − 306.5".
        diffs, rels = set(), set()
        for block in self._table_blocks():
            vals = self._nums_d(block)[:150]
            for a, da in vals:
                for b, db in vals:
                    if a != b and da == db:
                        diffs.add((round(abs(a - b), da), da))
                        if b:
                            rels.add(abs(a - b) / abs(b) * 100)
        # Only an explicit comparison with another number licenses a difference. Effect-size
        # verbs ("increases by", "提高") describe a coefficient that should be in a table as is.
        comparative = re.compile(r"\b(over|above|below|than|versus|vs\.?|gains?|improv\w*|outperform\w*|"
                                 r"relative to|compared (?:with|to))\b|高于|低于|相比|相较", re.I)
        num_re = re.compile(r"(?<![\w.\-/])(\d{1,3}(?:,\d{3})+|\d+)?(\.\d+)?\s*(%|percentage points?|percent|pp\b|个百分点)?")
        flagged = 0
        for zone, ln in claim_lines:
            sentences = re.split(r"(?<=[。；！？])|(?<=[.!?;])\s+", ln.text)
            for si, sent in enumerate(sentences):
                if re.search(r"⟨cite⟩|\b(?:19|20)\d{2}[a-z]?\)|（(?:19|20)\d{2}）|et al\.", sent):
                    continue  # numbers attributed to other papers
                for m in num_re.finditer(sent):
                    whole, frac, unit = m.group(1), m.group(2), m.group(3)
                    if not frac and not unit:
                        continue
                    if re.search(r"[<>≤≥=]\s*$", sent[: m.start()]):
                        continue  # thresholds such as "P < .001" or "n = 1,240" are not results
                    if not whole and not frac:
                        continue
                    s = (whole or "0").replace(",", "") + (frac or "")
                    try:
                        v = float(s)
                    except ValueError:
                        continue
                    if v == 0 or (not frac and v.is_integer() and v >= 1900 and v <= 2100):
                        continue
                    d = len(frac) - 1 if frac else 0
                    if self._in_pool(v, d, pool):
                        continue
                    if comparative.search(sent):
                        if (round(v, d), d) in diffs:
                            continue
                        if unit and unit.strip() in {"%", "percent"} and self._in_pool(v, d, rels, scale=False):
                            continue
                    flagged += 1
                    # "Figure 1 plots monthly visitors. Visits fell by 51.7 percent" — the number is
                    # likely printed in the figure. Only when the figure is cited in this or the
                    # previous sentence and no table is.
                    window = " ".join(sentences[max(0, si - 1): si + 1])
                    in_fig = (re.search(r"\b(Figure|Fig\.)\s*[A-Z]?\d|图\s*\d", window)
                              and not re.search(r"\bTables?\s*[A-Z]?\d|表\s*\d", window))
                    self.add("NUM-MISMATCH", "INFO" if in_fig else "FLAG", f"'{m.group(0).strip()}' in the {zone} does not appear in any table "
                             f"or in the body text (also tried ×100, ÷100, rounding, and — for comparisons — differences within a table)"
                             + (" — the paragraph cites a figure, so it may be printed in the image" if in_fig else "")
                             + f". Sentence: '{sent[:120]}'",
                             self.loc(ln.no))
        self.checked.append("abstract/introduction numbers traceable to the body or tables")

    @staticmethod
    def _nums(text: str) -> list[float]:
        out = []
        for m in re.finditer(r"(?<![\w.])[-−–]?(?:\d[\d,]*\.?\d*|\.\d+)", text):
            tok = m.group(0).replace(",", "").replace("−", "-").replace("–", "-").lstrip("-").rstrip(".")
            try:
                out.append(float(tok))
            except ValueError:
                pass
        return out

    @staticmethod
    def _nums_d(text: str) -> list[tuple[float, int]]:
        out = []
        for m in re.finditer(r"(?<![\w.])[-−–]?(\d[\d,]*)(?:\.(\d+))?", text):
            try:
                out.append((float(m.group(1).replace(",", "") + ("." + m.group(2) if m.group(2) else "")),
                            len(m.group(2) or "")))
            except ValueError:
                pass
        return out

    def _table_blocks(self) -> list[str]:
        blocks = [t["text"] for t in self.doc.tex_tables if t["kind"] == "table"]
        cur: list[str] = []
        for ln in self.doc.lines:
            if ln.kind == "table":
                cur.append(ln.text)
            elif cur:
                blocks.append(" ".join(cur))
                cur = []
        if cur:
            blocks.append(" ".join(cur))
        return blocks

    @staticmethod
    def _in_pool(v: float, d: int, pool: set[float], scale: bool = True) -> bool:
        for t in pool:
            for c in ((t, t * 100, t / 100) if scale else (t,)):
                if abs(round(c, d) - v) < 10 ** (-d) / 2 + 1e-9:
                    return True
        return False

    # ---- leftovers
    def leftovers(self) -> None:
        pat = re.compile(r"\bTODO\b|\bFIXME\b|\bTBD\b|\bXX+\b|\?\?|\[citation needed\]|\[(?:CITATION|REF|CITE)\]|"
                         r"\\todo\b|Error! Reference source not found|\[\?\]|lorem ipsum|\bINSERT (?:HERE|CITATION|REF)|"
                         r"待补充|待定|此处补充", re.I)
        for ln in self.doc.lines:
            m = pat.search(ln.text)
            if m:
                self.add("LEFTOVER-MARKER", "FAIL", f"Placeholder left in the text: '…{ln.text[max(0, m.start() - 30): m.end() + 30]}…'",
                         self.loc(ln.no))
        if self.doc.fmt == "tex":
            src = self.doc.path.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"\\todo(?:\[[^\]]*\])?\{", src):
                self.add("LEFTOVER-MARKER", "FAIL", "\\todo{} command left in the source.", self.loc(src[: m.start()].count("\n") + 1))
            stmt = [(c, ln) for c, ln in self.doc.comments if re.search(
                r"\\section\*?\{[^}]*(declaration|competing|interest|disclosure|\bAI\b|funding|acknowledg|data avail|ethic)",
                c, re.I)]
            if stmt:
                self.add("STMT-MISSING", "INFO", f"Commented-out statement section(s) in the source, e.g. '{stmt[0][0][:60]}' — "
                         "if the venue needs it, restore it; if not, delete it before uploading source.", self.loc(stmt[0][1]))
            bad = [(c, ln) for c, ln in self.doc.comments if re.search(r"TODO|FIXME|XXX|reviewer|referee|hack", c, re.I)]
            if bad:
                self.add("LEFTOVER-MARKER", "INFO", f"{len(bad)} LaTeX comment(s) contain notes such as '{bad[0][0][:50]}'. "
                         "They do not render, but they ship in an arXiv/source upload.", self.loc(bad[0][1]))
        if self.doc.tracked:
            self.add("LEFTOVER-TRACKED", "FAIL", f"{self.doc.tracked} tracked change(s) remain — accept or reject all changes.")
        if self.doc.fmt in {"docx", "md"} and self.doc.comments:
            self.add("LEFTOVER-TRACKED", "FAIL", f"{len(self.doc.comments)} reviewer comment(s) remain in the file "
                     f"(first: '{self.doc.comments[0][0][:60]}').")
        self.checked.append("placeholders, tracked changes, comments")


# ----------------------------------------------------------------------------- venue rules

def load_rules_db(path: Path | None) -> dict:
    for cand in ([path] if path else []) + list(RULES_CANDIDATES):
        if cand and cand.exists():
            return json.loads(cand.read_text(encoding="utf-8")).get("venues", {})
    return {}


def _key(s: str) -> str:
    s = re.sub(r"^the\s+", "", s.lower().strip())
    return re.sub(r"[^a-z0-9\u3400-\u9fff]", "", s.replace("&", "and").replace("-skills", ""))


def resolve_venue(db: dict, name: str) -> tuple[str, dict] | None:
    want = _key(name)
    for pack, entry in db.items():
        if any(_key(a) == want for a in entry.get("aliases", [])):
            return pack, entry
    hits = [(pack, e) for pack, e in db.items() if any(want and want in _key(a) for a in e.get("aliases", []))]
    return hits[0] if len(hits) == 1 else None


# ----------------------------------------------------------------------------- report

def _finding_key(f: dict) -> tuple:
    """Identity of a finding across two runs: check + statement + message with numbers and
    quoted excerpts blanked, since a revision moves line numbers and changes counts."""
    msg = re.sub(r"'[^']*'|\[[^\]]*\]|\d[\d,.]*", "#", f.get("message", ""))
    return (f.get("check"), f.get("statement", ""), msg)


def compare(prev: dict, findings: list[Finding]) -> dict:
    """Stage 5 of the pipeline: what the revision resolved, left open, or introduced."""
    old = [f for f in prev.get("findings", []) if f.get("severity") in {"FAIL", "FLAG"}]
    new = [asdict(f) for f in findings if f.severity in {"FAIL", "FLAG"}]
    old_keys = {_finding_key(f) for f in old}
    new_keys = {_finding_key(f) for f in new}
    return {
        "previous_verdict": prev.get("verdict"),
        "resolved": [f for f in old if _finding_key(f) not in new_keys],
        "still_open": [f for f in new if _finding_key(f) in old_keys],
        "new": [f for f in new if _finding_key(f) not in old_keys],
    }


def render_diff(d: dict, now: str) -> str:
    out = [f"\n【Re-run diff】{d['previous_verdict']} → {now}: {len(d['resolved'])} resolved · "
           f"{len(d['still_open'])} still open · {len(d['new'])} new"]
    for label, key in (("Resolved", "resolved"), ("Still open", "still_open"), ("New since last run", "new")):
        for f in d[key]:
            out.append(f"  {label:<18} {f['check']:<16} {f['message'][:110]}")
    return "\n".join(out)


def verdict(findings: list[Finding]) -> str:
    if any(f.severity == "FAIL" for f in findings):
        return "NO-GO"
    if any(f.severity == "FLAG" for f in findings):
        return "CONDITIONAL GO"
    return "GO"


def render(doc: Doc, venue: str, entry: dict | None, ck: Checker) -> str:
    out = []
    v = verdict(ck.findings)
    out.append(f"【Preflight】{doc.path.name} ({doc.fmt}) → {venue or 'no venue given'}")
    if entry:
        out.append(f"【Venue rules】{entry['venue']} — verified {entry['verified']} ({entry['source_map']})")
    else:
        out.append("【Venue rules】none loaded — only universal checks ran; venue limits, review mode and required "
                   "statements were NOT checked")
    out.append(f"【Mechanical verdict】{v}  ({sum(f.severity == 'FAIL' for f in ck.findings)} FAIL · "
               f"{sum(f.severity == 'FLAG' for f in ck.findings)} FLAG · {sum(f.severity == 'INFO' for f in ck.findings)} INFO)")
    stats = ", ".join(f"{k}={v}" for k, v in ck.stats.items())
    if stats:
        out.append(f"【Counts】{stats}")
    for sev in ("FAIL", "FLAG", "INFO"):
        items = [f for f in ck.findings if f.severity == sev]
        if not items:
            continue
        out.append(f"\n{sev}")
        for f in items:
            where = f" [{f.where}]" if f.where else ""
            out.append(f"  {f.check:<17}{where} {f.message}")
            if sev != "INFO":
                out.append(f"  {'':<17} → owner: {f.owner}")
    if ck.reminders:
        out.append("\n【Portal checklist — from the venue rules, not testable in the file】")
        out.extend(f"  · {r}" for r in ck.reminders)
    out.append("\n【Checked】" + ("; ".join(ck.checked) if ck.checked else "—"))
    if ck.not_checked:
        out.append("【NOT checked — do not read as PASS】" + "; ".join(ck.not_checked))
    out.append("【Next】This is stage 0 (mechanics). Fix every FAIL, then run the readiness scorecard and the "
               "simulated referee panel (rt-submission-readiness → rt-simulated-referee).")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manuscript", nargs="?", help=".tex .md .docx .pdf or .txt")
    ap.add_argument("--venue", help="venue name, acronym, pack dir or plugin name (e.g. 'JF', 'icml', 'JAMA-Skills')")
    ap.add_argument("--rules", help="path to a venue-rules.json (default: the repo/vendored copy)")
    ap.add_argument("--rules-block", help="path to a JSON file holding one ajs-preflight-rules/1 block, for a venue "
                                          "without a pack")
    ap.add_argument("--bib", help=".bib file for a .tex manuscript, if not found via \\bibliography")
    blind = ap.add_mutually_exclusive_group()
    blind.add_argument("--blind", dest="blind", action="store_true", default=None, help="force double-blind checks")
    blind.add_argument("--no-blind", dest="blind", action="store_false", help="skip anonymization checks")
    ap.add_argument("--online", action="store_true", help="also check references exist on Crossref (network)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--compare", metavar="PREVIOUS.json",
                    help="a previous --json report for this manuscript: show what was resolved, is still "
                         "open, or is new (stage 5 of the pipeline)")
    ap.add_argument("--list-venues", action="store_true", help="list venues with machine-readable rules")
    args = ap.parse_args(argv)

    db = load_rules_db(Path(args.rules) if args.rules else None)
    if args.list_venues:
        for pack, e in sorted(db.items(), key=lambda kv: kv[1]["venue"].lower()):
            print(f"{e['venue']:<55} {pack:<50} verified {e['verified']}  ({len(e['rules'])} rules)")
        print(f"\n{len(db)} venues. Others: pass --rules-block, or --blind for anonymization-only checks.")
        return 0
    if not args.manuscript:
        ap.error("a manuscript path is required")
    path = Path(args.manuscript)
    if not path.exists():
        print(f"preflight: {path} not found", file=sys.stderr)
        return 2
    entry, pack = None, ""
    if args.rules_block:
        block = json.loads(Path(args.rules_block).read_text(encoding="utf-8"))
        entry = {"venue": block.get("venue", "custom"), "verified": block.get("verified", "?"),
                 "source_map": args.rules_block, "rules": block.get("rules", {})}
    elif args.venue:
        hit = resolve_venue(db, args.venue)
        if hit:
            pack, entry = hit
        else:
            print(f"preflight: no machine-readable rules for '{args.venue}' — universal checks only "
                  "(see --list-venues)", file=sys.stderr)
    try:
        doc = load(path, Path(args.bib) if args.bib else None)
    except (zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"preflight: could not read {path}: {exc}", file=sys.stderr)
        return 2
    ck = Checker(doc, (entry or {}).get("rules", {}), args.venue or "", args.blind, args.online)
    ck.run()
    diff = None
    if args.compare:
        try:
            diff = compare(json.loads(Path(args.compare).read_text(encoding="utf-8")), ck.findings)
        except (OSError, json.JSONDecodeError) as exc:
            print(f"preflight: could not read --compare file: {exc}", file=sys.stderr)
            return 2
    if args.json:
        print(json.dumps({
            "manuscript": str(path), "format": doc.fmt, "venue": entry["venue"] if entry else args.venue,
            "pack": pack, "rules_verified": entry["verified"] if entry else None,
            "verdict": verdict(ck.findings), "stats": ck.stats,
            "findings": [asdict(f) for f in ck.findings],
            "checked": ck.checked, "not_checked": ck.not_checked, "portal_checklist": ck.reminders,
            **({"diff": diff} if diff else {}),
        }, ensure_ascii=False, indent=2))
    else:
        print(render(doc, args.venue or "", entry, ck))
        if diff:
            print(render_diff(diff, verdict(ck.findings)))
    return 1 if verdict(ck.findings) == "NO-GO" else 0


if __name__ == "__main__":
    sys.exit(main())
