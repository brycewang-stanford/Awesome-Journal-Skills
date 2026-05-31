#!/usr/bin/env python3
"""Install ONE real journal cover into assets/covers/.

Usage:
    python3 assets/install_cover.py <slug> <source_url_or_local_path> <source_label> <license_note> [manifest_name]

`manifest_name` (optional 5th arg) lets concurrent fetch agents each write their OWN provenance
file under assets/covers/ (e.g. REAL-COVERS-chunk3.tsv) to avoid a write race; the orchestrator
merges them. Defaults to REAL-COVERS.tsv.

What it does (idempotent per slug):
  1. Download the image (if a URL) to a temp file; accept an existing local path too.
  2. Validate it is a real raster image and not a tiny/HTML error page (min 6 KB, real JPEG/PNG/GIF/WEBP).
  3. Convert + resize to a cover-shaped PNG (max edge 320 px, preserves aspect) via macOS `sips`.
  4. Write assets/covers/<slug>.png  (this is exactly the path the README galleries reference).
  5. Append a provenance row to assets/covers/REAL-COVERS.tsv so every real cover is traceable
     (slug, source_label, license_note, source_url, px). Re-running a slug replaces its row.

Exit codes: 0 installed · 2 rejected (not a real image / too small) · 3 sips/convert failure.
This NEVER commits or pushes — covers land uncommitted for the user's 验收.
"""
import os, sys, ssl, subprocess, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "covers")
MANIFEST = os.path.join(COVERS, "REAL-COVERS.tsv")  # overridable by optional 5th arg
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
MAGIC = {b"\xff\xd8\xff": "jpg", b"\x89PNG": "png", b"GIF8": "gif", b"RIFF": "webp"}


def fetch(src):
    if os.path.isfile(src):
        return open(src, "rb").read()
    req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0 (cover-fetch)"})
    return urllib.request.urlopen(req, timeout=30, context=CTX).read()


def real_image(data):
    if len(data) < 6000:               # tiny -> almost certainly an error/placeholder
        return None
    for sig, ext in MAGIC.items():
        if data.startswith(sig):
            return ext
    return None


def main():
    if len(sys.argv) < 5:
        print("usage: install_cover.py <slug> <url_or_path> <source_label> <license_note>"); sys.exit(2)
    slug, src, label, lic = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    manifest = os.path.join(COVERS, sys.argv[5]) if len(sys.argv) > 5 else MANIFEST
    try:
        data = fetch(src)
    except Exception as e:
        print(f"REJECT {slug}: fetch failed: {e}"); sys.exit(2)
    ext = real_image(data)
    if not ext:
        print(f"REJECT {slug}: not a real raster image (size={len(data)})"); sys.exit(2)
    with tempfile.NamedTemporaryFile(suffix=f".{ext}", delete=False) as tf:
        tf.write(data); raw = tf.name
    out = os.path.join(COVERS, f"{slug}.png")
    r = subprocess.run(["sips", "-s", "format", "png", "-Z", "320", raw, "--out", out],
                       capture_output=True, text=True)
    os.unlink(raw)
    if r.returncode != 0 or not os.path.isfile(out):
        print(f"REJECT {slug}: sips convert failed: {r.stderr.strip()}"); sys.exit(3)
    dim = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", out],
                         capture_output=True, text=True).stdout
    px = "x".join(w.split(":")[-1].strip() for w in dim.splitlines() if "pixel" in w)
    rows = []
    if os.path.isfile(manifest):
        rows = [ln for ln in open(manifest, encoding="utf-8").read().splitlines()
                if ln and not ln.startswith(slug + "\t")]
    if not rows or not rows[0].startswith("slug\t"):
        rows = ["slug\tsource_label\tlicense\tsource_url\tpx"] + rows
    rows.append(f"{slug}\t{label}\t{lic}\t{src}\t{px}")
    open(manifest, "w", encoding="utf-8").write("\n".join(rows) + "\n")
    print(f"OK {slug}: installed {px} from [{label}/{lic}] {src}")


if __name__ == "__main__":
    main()
