#!/usr/bin/env python3
"""Insert per-bundle cover galleries into README.md and README.en.md.

Each breadth bundle gets an always-expanded gallery (a caption line plus one cover
thumbnail per journal, ordered by discipline so colours cluster). Idempotent:
re-running replaces the content between the HTML-comment markers instead of duplicating.
"""
import importlib.util
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("g", os.path.join(ROOT, "assets", "gen_breadth_covers.py"))
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)

WIDTH = 100

BUNDLES = {
    "cn-soc": ("Chinese-SocialScience-Journal-Skills", g.CN_SOC),
    "en-soc": ("English-SocialScience-Journal-Skills", g.EN_SOC),
    "en-nat": ("English-NaturalScience-Journal-Skills", g.EN_NAT),
}


def label(bdir, slug):
    cn, en = g.read_name(bdir, slug)
    return f"《{cn}》" if cn else en


def gallery(key):
    bdir, dmap = BUNDLES[key]
    out = ['<p align="center">']
    for ckey, slugs in dmap.items():
        for slug in slugs:
            cov = g.COVER_ALIAS.get(slug, slug)
            alt = label(bdir, slug).replace('"', "'")
            out.append(f'  <a href="{bdir}/skills/{slug}/"><img src="assets/covers/{cov}.png" '
                       f'alt="{alt}" width="{WIDTH}"></a>')
    out.append('</p>')
    return "\n".join(out)


def block(key, summary):
    inner = gallery(key)
    return (f"<!-- COVER-GALLERY:{key}:START -->\n"
            f'<p align="center"><sub>{summary}</sub></p>\n\n'
            f"{inner}\n"
            f"<!-- COVER-GALLERY:{key}:END -->")


def upsert(text, key, summary, anchor):
    """Insert/replace the gallery block immediately after the anchor line."""
    blk = block(key, summary)
    start = f"<!-- COVER-GALLERY:{key}:START -->"
    end = f"<!-- COVER-GALLERY:{key}:END -->"
    if start in text:  # replace existing
        return re.sub(re.escape(start) + r".*?" + re.escape(end), blk, text, flags=re.S)
    idx = text.index(anchor)
    line_end = text.index("\n", idx) + 1
    return text[:line_end] + "\n" + blk + "\n" + text[line_end:]


PLANS = {
    "README.en.md": {
        "cn-soc": ("📚 <b>All 102 Chinese social-science journal covers</b> &mdash; grouped by discipline",
                   "| **~100 China econ/management roadmap journals** | [Chinese-SocialScience-Journal-Skills/]"),
        "en-soc": ("📚 <b>All 100 English social-science journal covers</b> &mdash; grouped by discipline",
                   "This bundle covers the full English roadmap below: Economics 50"),
        "en-nat": ("📚 <b>All 100 English natural-science journal covers</b> &mdash; grouped by discipline",
                   "This bundle is the natural-science sibling of the English social-science breadth bundle"),
    },
    "README.md": {
        "cn-soc": ("📚 <b>全部 102 本中文社科期刊封面</b> &mdash; 按学科分组",
                   "| **约 100 本中文经管路线图期刊** | [Chinese-SocialScience-Journal-Skills/]"),
        "en-soc": ("📚 <b>全部 100 本英文社科期刊封面</b> &mdash; 按学科分组",
                   "该合集覆盖下方完整英文路线图：经济学 50"),
        "en-nat": ("📚 <b>全部 100 本英文自然科学期刊封面</b> &mdash; 按学科分组",
                   "这是英文经管广度合集的自然科学姊妹包"),
    },
}

for fname, plan in PLANS.items():
    path = os.path.join(ROOT, fname)
    text = open(path, encoding="utf-8").read()
    for key, (summary, anchor) in plan.items():
        if anchor not in text:
            raise SystemExit(f"ANCHOR NOT FOUND in {fname}: {anchor!r}")
        text = upsert(text, key, summary, anchor)
    open(path, "w", encoding="utf-8").write(text)
    print(f"{fname}: inserted/updated {len(plan)} galleries")
print("done")
