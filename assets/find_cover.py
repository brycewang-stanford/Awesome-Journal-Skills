#!/usr/bin/env python3
"""Find the *cover* image on a Wikipedia article (not the logo / a random photo).

Strategy that beats `pageimages` (which returns whatever the lead image is — often a logo):
  1. List every file used on the page via prop=images.
  2. Score each filename: strongly prefer ones containing 'cover'; accept journal-name
     matches; HARD-REJECT logos, wordmarks, building photos, portraits, icons, commons
     decorations (Commons-logo, Wikidata, Edit-icon, ambox, question_book ...).
  3. Resolve the winning file's real thumbnail URL via prop=imageinfo (iiurlwidth=500).
  4. Print 'URL <slug> <url>' on success, or 'MISS <slug> <reason>' — caller installs.

Usage:
    python3 assets/find_cover.py --batch pairs.tsv        # prints candidate URLs
    python3 assets/find_cover.py <slug> "<Wikipedia Title>"
"""
import json, re, ssl, sys, time, urllib.parse, urllib.request

CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
UA = "awesome-journal-skills-cover-fetch/1.1 (https://github.com/brycewang-stanford; brycewang2018@gmail.com)"
API = "https://en.wikipedia.org/w/api.php?"
DELAY = 2.5

REJECT = re.compile(r"(logo|wordmark|commons-logo|wikidata|edit-icon|ambox|question_book|"
                    r"padlock|symbol|icon|\.svg$|building|headquarters|portrait|seal|"
                    r"flag|map|red_pog|location|barnstar|crystal|nuvola|folder)", re.I)
PREFER = re.compile(r"cover", re.I)


def api(params):
    url = API + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=30, context=CTX))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(4 + attempt * 3); continue
            raise
    raise RuntimeError("429 after retries")


def page_images(title):
    d = api({"action": "query", "format": "json", "prop": "images",
             "imlimit": "200", "redirects": "1", "titles": title})
    pages = d.get("query", {}).get("pages", {})
    files = []
    for _, p in pages.items():
        for im in p.get("images", []):
            files.append(im["title"])  # 'File:...'
    return files


def imageinfo_url(filetitle, width=500):
    d = api({"action": "query", "format": "json", "prop": "imageinfo",
             "iiprop": "url", "iiurlwidth": str(width), "titles": filetitle})
    for _, p in d.get("query", {}).get("pages", {}).items():
        ii = p.get("imageinfo")
        if ii:
            return ii[0].get("thumburl") or ii[0].get("url")
    return None


def pick(files, title):
    """Return best cover-file title or None."""
    name_tokens = [t.lower() for t in re.findall(r"[A-Za-z]+", title) if len(t) > 3]
    scored = []
    for f in files:
        base = f.split(":", 1)[-1]
        if REJECT.search(base):
            continue
        if not re.search(r"\.(jpe?g|gif|png|webp)$", base, re.I):
            continue
        score = 0
        if PREFER.search(base):
            score += 100
        low = base.lower()
        score += sum(5 for tok in name_tokens if tok in low)
        if score > 0:
            scored.append((score, f))
    if not scored:
        return None
    scored.sort(reverse=True)
    return scored[0][1]


def resolve(slug, title):
    try:
        files = page_images(title)
    except Exception as e:
        return None, f"api error: {e}"
    f = pick(files, title)
    if not f:
        return None, "no cover-like file among %d images" % len(files)
    url = imageinfo_url(f)
    if not url:
        return None, f"could not resolve url for {f}"
    return url, f


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--batch":
        pairs = []
        for ln in open(sys.argv[2], encoding="utf-8"):
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.lstrip().startswith("#"):
                continue
            slug, _, title = ln.partition("\t")
            pairs.append((slug.strip(), title.strip()))
        for i, (slug, title) in enumerate(pairs):
            if i:
                time.sleep(DELAY)
            url, info = resolve(slug, title)
            if url:
                print(f"URL\t{slug}\t{url}\t# {info}")
            else:
                print(f"MISS\t{slug}\t{info}")
        return
    if len(sys.argv) < 3:
        print("usage: find_cover.py <slug> \"<Title>\"  |  --batch pairs.tsv"); sys.exit(2)
    url, info = resolve(sys.argv[1], sys.argv[2])
    print(f"{'URL' if url else 'MISS'}\t{sys.argv[1]}\t{url or info}\t# {info if url else ''}")


if __name__ == "__main__":
    main()
