#!/usr/bin/env python3
"""Resolve Wikipedia lead images (journal covers) in batch and install them.

Usage:
    python3 assets/wiki_cover.py <slug> "<Wikipedia Article Title>"      # single
    python3 assets/wiki_cover.py --batch pairs.tsv                        # many

`pairs.tsv` lines are  <slug>\t<Wikipedia Title>  (blank lines / # comments ignored).

Method: MediaWiki `pageimages` API with **pilicense=any** (so fair-use journal covers
hosted on en.wikipedia are NOT excluded), then hand the resolved thumbnail URL to
install_cover.py (validate -> sips resize 320 -> write assets/covers/<slug>.png -> log).

Respects Wikimedia etiquette: descriptive User-Agent + a delay between API calls.
Always visually verify installed PNGs (a few journal articles use a logo, not a cover).
"""
import json, os, ssl, subprocess, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
UA = "awesome-journal-skills-cover-fetch/1.0 (https://github.com/brycewang-stanford; brycewang2018@gmail.com)"
DELAY = 1.6  # seconds between API calls to avoid HTTP 429


def resolve(title):
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "pageimages",
        "piprop": "thumbnail", "pithumbsize": "500", "pilicense": "any",
        "redirects": "1", "titles": title})
    url = "https://en.wikipedia.org/w/api.php?" + q
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    data = json.load(urllib.request.urlopen(req, timeout=30, context=CTX))
    for _, p in data.get("query", {}).get("pages", {}).items():
        src = p.get("thumbnail", {}).get("source")
        if src:
            return src
    return None


def install(slug, title):
    try:
        url = resolve(title)
    except Exception as e:
        print(f"NOURL {slug}: api error: {e}"); return 2
    if not url:
        print(f"NOURL {slug}: no pageimage for '{title}'"); return 2
    print(f"RESOLVED {slug}: {url}")
    r = subprocess.run([sys.executable, os.path.join(ROOT, "assets", "install_cover.py"),
                        slug, url, "Wikipedia (en)", "fair-use thumbnail"])
    return r.returncode


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--batch":
        pairs = []
        for ln in open(sys.argv[2], encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            slug, _, title = ln.partition("\t")
            pairs.append((slug.strip(), title.strip()))
        ok = 0
        for i, (slug, title) in enumerate(pairs):
            if i:
                time.sleep(DELAY)
            if install(slug, title) == 0:
                ok += 1
        print(f"\nBATCH DONE: {ok}/{len(pairs)} installed")
        return
    if len(sys.argv) < 3:
        print("usage: wiki_cover.py <slug> \"<Title>\"  |  --batch pairs.tsv"); sys.exit(2)
    sys.exit(install(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
