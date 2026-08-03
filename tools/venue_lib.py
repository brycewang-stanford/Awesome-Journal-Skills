#!/usr/bin/env python3
"""Shared helpers for the journal-selection data layer.

Holds the pack-classification, scope-text extraction, and keyword-derivation logic
used by ``gen_venue_index.py``, ``gen_ladder.py`` and ``eval_journal_match.py`` so
the three stay consistent about *what counts as a venue* and *what text describes it*.

Design rule inherited from the journal-selection capability: everything derived here
is **stable** (discipline / lane / region / scope vocabulary). Volatile facts — fees,
acceptance rates, turnaround, page limits — are never extracted; they stay in each
pack's ``resources/official-source-map.md`` and are read at match time.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

IMPORTED = {
    "AER-Skills", "AER-skills", "Nature-Skills", "nature-skills",
    "nature-paper-skills", "claude-scholar", "codex-claude-academic-skills",
}

# Breadth bundles: one pack, many per-venue profile skills. Each carries a default
# discipline/region/type for the venues it profiles.
BUNDLES = {
    "English-SocialScience-Journal-Skills":
        {"discipline": "social-science", "region": "international", "type": "journal"},
    "English-NaturalScience-Journal-Skills":
        {"discipline": "natural-science", "region": "international", "type": "journal"},
    "English-Humanities-Journal-Skills":
        {"discipline": "humanities", "region": "international", "type": "journal"},
    "Chinese-SocialScience-Journal-Skills":
        {"discipline": "social-science", "region": "china", "type": "journal"},
    "Chinese-Sport-Science-Journal-Skills":
        {"discipline": "sport-science", "region": "china", "type": "journal"},
    "Computer-Science-Conference-Skills":
        {"discipline": "cs-ai", "region": "international", "type": "conference"},
    "Engineering-Technology-Journal-Skills":
        {"discipline": "engineering", "region": "international", "type": "journal"},
    "Agriculture-Environment-Journal-Skills":
        {"discipline": "agriculture-environment", "region": "international", "type": "journal"},
    "Clinical-Medicine-Journal-Skills":
        {"discipline": "clinical-medicine", "region": "international", "type": "journal"},
}

# Chinese-language depth packs.
CHINA = {
    "Economic-Research-Journal-Skills", "Journal-of-Management-World-Skills",
    "China-Industrial-Economics-Skills", "China-Economic-Quarterly-Skills",
    "China-Rural-Economy-Skills", "Chinese-Public-Administration-Skills",
    "Journal-of-Finance-and-Economics-Skills", "Journal-of-Financial-Research-Skills",
    "Journal-of-Management-Sciences-in-China-Skills",
    "Journal-of-Quantitative-and-Technological-Economics-Skills",
    "Journal-of-World-Economy-Skills", "Nankai-Business-Review-Skills",
    "Social-Sciences-in-China-Skills", "Sociological-Studies-Skills",
    "Accounting-Research-Skills",
}

# Indicative tier for well-known flagships (approximate; not a ranking claim).
TIER = {
    "Quarterly-Journal-of-Economics-Skills": "top-5 econ",
    "Journal-of-Political-Economy-Skills": "top-5 econ",
    "Econometrica-Skills": "top-5 econ", "Review-of-Economic-Studies-Skills": "top-5 econ",
    "Journal-of-Finance-Skills": "top-3 finance",
    "Journal-of-Financial-Economics-Skills": "top-3 finance",
    "Review-of-Financial-Studies-Skills": "top-3 finance",
    "Journal-of-Accounting-Research-Skills": "top-3 accounting",
    "Journal-of-Accounting-and-Economics-Skills": "top-3 accounting",
    "The-Accounting-Review-Skills": "top-3 accounting",
    "Management-Science-Skills": "FT50 / UTD24", "Operations-Research-Skills": "FT50 / UTD24",
    "Marketing-Science-Skills": "FT50 / UTD24", "Journal-of-Marketing-Skills": "FT50 / UTD24",
    "Journal-of-Marketing-Research-Skills": "FT50 / UTD24",
    "Journal-of-Consumer-Research-Skills": "FT50 / UTD24",
    "MIS-Quarterly-Skills": "FT50 / UTD24", "Information-Systems-Research-Skills": "FT50 / UTD24",
    "Academy-of-Management-Journal-Skills": "FT50 / UTD24",
    "Academy-of-Management-Review-Skills": "FT50 / UTD24",
    "Administrative-Science-Quarterly-Skills": "FT50 / UTD24",
    "Strategic-Management-Journal-Skills": "FT50 / UTD24",
    "American-Economic-Review-Skills": "top-5 econ",
    "American-Political-Science-Review-Skills": "top-3 polisci",
    "American-Journal-of-Political-Science-Skills": "top-3 polisci",
    "American-Sociological-Review-Skills": "top-3 sociology",
    "American-Journal-of-Sociology-Skills": "top-3 sociology",
    "Journal-of-Personality-and-Social-Psychology-Skills": "flagship psych",
    "Psychological-Bulletin-Skills": "flagship psych (review)",
    "Economic-Research-Journal-Skills": "中文经济学顶刊",
    "Journal-of-Management-World-Skills": "中文管理顶刊",
    "Social-Sciences-in-China-Skills": "中文综合顶刊",
}

# Theory / review / qualitative-leaning venues (lane != empirical).
THEORY = {
    "Econometric-Theory-Skills": "theory", "Journal-of-Economic-Theory-Skills": "theory",
    "Academy-of-Management-Review-Skills": "theory", "Sociological-Theory-Skills": "theory",
    "Psychological-Review-Skills": "theory", "Annals-of-Mathematics-Skills": "theory",
    "Journal-of-Economic-Literature-Skills": "review", "Annual-Review-of-Economics-Skills": "review",
    "Academy-of-Management-Annals-Skills": "review", "Psychological-Bulletin-Skills": "review/meta",
    "Organization-Studies-Skills": "qualitative/mixed", "Sociological-Studies-Skills": "mixed",
    "Social-Sciences-in-China-Skills": "theory/argumentative",
    "Journal-of-Economic-Perspectives-Skills": "review/expository",
}

NON_EMPIRICAL_DISCIPLINES = {
    "philosophy", "history", "art-history", "humanities/literature", "humanities/theory",
    "religion", "anthropology", "mathematics", "economics/theory", "economics/game-theory",
    "humanities",
}

# discipline keyword map (substring match, first match wins; order matters)
DISC: list[tuple[str, str]] = [
    # CS/AI conferences
    ("AAAI", "cs-ai (conference)"), ("AISTATS", "cs-ai (conference)"),
    ("COLT", "cs-ai (conference)"), ("ICLR", "cs-ai (conference)"),
    ("ICML", "cs-ai (conference)"), ("IJCAI", "cs-ai (conference)"),
    ("KDD", "cs-ai (conference)"), ("MLSys", "cs-ai (conference)"),
    ("NeurIPS", "cs-ai (conference)"), ("UAI", "cs-ai (conference)"),
    ("Web-Conference", "cs-ai (conference)"), ("WSDM", "cs-ai (conference)"),
    ("SIGIR", "cs-ai (conference)"), ("CVPR", "cs-ai (conference)"),
    ("ICCV", "cs-ai (conference)"), ("ACL-Skills", "cs-ai (conference)"),
    ("EMNLP", "cs-ai (conference)"), ("ICRA", "cs-ai (conference)"),
    ("CHI-Skills", "cs-ai (conference)"), ("SOSP", "cs-ai (conference)"),
    ("OSDI", "cs-ai (conference)"), ("IEEE-SP", "cs-ai (conference)"),
    ("ACM-CCS", "cs-ai (conference)"), ("ICSE-Skills", "cs-ai (conference)"),
    ("NAACL", "cs-ai (conference)"), ("ECCV", "cs-ai (conference)"),
    ("PLDI", "cs-ai (conference)"), ("SIGMOD", "cs-ai (conference)"),
    ("STOC-Skills", "cs-ai (conference)"), ("NSDI", "cs-ai (conference)"),
    ("USENIX-Security", "cs-ai (conference)"), ("NDSS", "cs-ai (conference)"),
    ("FOCS", "cs-ai (conference)"), ("SODA-Skills", "cs-ai (conference)"),
    ("POPL", "cs-ai (conference)"), ("OOPSLA", "cs-ai (conference)"),
    ("VLDB", "cs-ai (conference)"), ("CIKM", "cs-ai (conference)"),
    ("EuroSys", "cs-ai (conference)"), ("ASPLOS", "cs-ai (conference)"),
    ("UIST", "cs-ai (conference)"), ("CSCW", "cs-ai (conference)"),
    ("ISCA-Skills", "cs-ai (conference)"), ("MICRO-Skills", "cs-ai (conference)"),
    ("RSS-Skills", "cs-ai (conference)"), ("CoRL", "cs-ai (conference)"),
    ("INTERSPEECH", "cs-ai (conference)"), ("COLM", "cs-ai (conference)"),
    ("HPCA", "cs-ai (conference)"), ("IROS", "cs-ai (conference)"),
    ("ICDE", "cs-ai (conference)"), ("ICDM", "cs-ai (conference)"),
    ("RecSys", "cs-ai (conference)"), ("MobiCom", "cs-ai (conference)"),
    ("ACM-MM", "cs-ai (conference)"), ("ICASSP", "cs-ai (conference)"),
    ("SIGCOMM", "cs-ai (conference)"), ("EACL", "cs-ai (conference)"),
    ("AAMAS", "cs-ai (conference)"), ("WACV", "cs-ai (conference)"),
    ("MobiSys", "cs-ai (conference)"), ("SenSys", "cs-ai (conference)"),
    ("ISSTA", "cs-ai (conference)"), ("FSE-Skills", "cs-ai (conference)"),
    ("ASE-Skills", "cs-ai (conference)"), ("PODS-Skills", "cs-ai (conference)"),
    ("CoNEXT-Skills", "cs-ai (conference)"), ("IMC-Skills", "cs-ai (conference)"),
    ("IPSN-Skills", "cs-ai (conference)"), ("VIS-Skills", "cs-ai (conference)"),
    ("ICSME-Skills", "cs-ai (conference)"), ("ECAI-Skills", "cs-ai (conference)"),
    ("ATC-Skills", "cs-ai (conference)"), ("FAST-Skills", "cs-ai (conference)"),
    ("PPoPP-Skills", "cs-ai (conference)"), ("CAV-Skills", "cs-ai (conference)"),
    ("ICALP-Skills", "cs-ai (conference)"), ("PODC-Skills", "cs-ai (conference)"),
    ("SIGMETRICS-Skills", "cs-ai (conference)"), ("PerCom-Skills", "cs-ai (conference)"),
    ("SIGGRAPH-Skills", "cs-ai (conference)"), ("INFOCOM-Skills", "cs-ai (conference)"),
    ("ITCS-Skills", "cs-ai (conference)"), ("HRI-Skills", "cs-ai (conference)"),
    ("SoCC-Skills", "cs-ai (conference)"), ("DAC-Skills", "cs-ai (conference)"),
    ("EDBT-Skills", "cs-ai (conference)"), ("TACAS-Skills", "cs-ai (conference)"),
    ("FAccT-Skills", "cs-ai (conference)"), ("ICDT-Skills", "cs-ai (conference)"),
    # Chinese-language CS/AI journals (CCF-recommended 中文期刊 — journals, not conferences)
    ("Chinese-Journal-of-Computers-Skills", "cs-ai (CN journal)"),
    ("Journal-of-Software-Skills", "cs-ai (CN journal)"),
    ("Journal-of-Computer-Research-and-Development-Skills", "cs-ai (CN journal)"),
    ("Acta-Automatica-Sinica-Skills", "cs-ai (CN journal)"),
    ("Scientia-Sinica-Informationis-Skills", "cs-ai (CN journal)"),
    ("Acta-Electronica-Sinica-Skills", "cs-ai (CN journal)"),
    ("Pattern-Recognition-and-Artificial-Intelligence-Skills", "cs-ai (CN journal)"),
    ("Journal-of-CAD-and-Computer-Graphics-Skills", "cs-ai (CN journal)"),
    ("Journal-on-Communications-Skills", "cs-ai (CN journal)"),
    ("Computer-Science-Journal-Skills", "cs-ai (CN journal)"),
    # specific economics flagships / subfields not caught generically
    ("AEJ-Applied", "economics/applied"), ("AEJ-Macro", "economics/macro"),
    ("AEJ-Micro", "economics/micro"), ("AER-Insights", "economics"),
    ("Quarterly-Journal-of-Economics", "economics"), ("Political-Economy", "economics"),
    ("Review-of-Economic-Studies", "economics"), ("International-Economic-Review", "economics"),
    ("Games-and-Economic-Behavior", "economics/game-theory"),
    ("Economic-Theory", "economics/theory"),
    # humanities / area studies
    ("Anthropolog", "anthropology"), ("Historical-Review", "history"),
    ("Geographers", "geography"), ("Human-Geography", "geography"),
    ("Annual-Review-of-Psychology", "psychology"), ("Critical-Inquiry", "humanities/theory"),
    ("Academy-of-Religion", "religion"), ("Mind-Skills", "philosophy"),
    ("PMLA", "humanities/literature"), ("Art-Bulletin", "art-history"),
    ("Econometric", "econometrics/methods"), ("Econometrics", "econometrics/methods"),
    ("Quantitative-and-Technological", "econometrics/methods"),
    ("Business-and-Economic-Statistics", "econometrics/methods"),
    ("Applied-Econometrics", "econometrics/methods"),
    ("Accounting", "accounting"),
    ("Finance", "finance"), ("Financial", "finance"), ("Banking", "finance"),
    ("Marketing", "marketing"), ("Consumer", "marketing"),
    ("Operations", "operations"), ("Manufacturing-and-Service", "operations"),
    ("INFORMS-Journal-on-Computing", "operations/computing"),
    ("Information-Systems", "information-systems"), ("MIS-Quarterly", "information-systems"),
    ("Management-Information-Systems", "information-systems"),
    ("Association-for-Information-Systems", "information-systems"),
    ("Management-World", "management"), ("Management-Sciences-in-China", "management/OR"),
    ("Management-Review", "management"), ("Management-Studies", "management"),
    ("Management-Annals", "management"), ("Organization", "management"),
    ("Strategic-Management", "management"), ("Human-Resource", "management"),
    ("Human-Relations", "management"), ("Business-Venturing", "entrepreneurship"),
    ("Entrepreneurship", "entrepreneurship"), ("International-Business", "international-business"),
    ("Academy-of-Management", "management"), ("Administrative-Science", "management"),
    ("Nankai-Business", "management"), ("Journal-of-Management", "management"),
    ("Political-Science", "political-science"), ("Journal-of-Politics", "political-science"),
    ("Comparative-Political", "political-science"), ("World-Politics", "political-science"),
    ("International-Organization", "political-science/IR"),
    ("Public-Administration", "public-admin"), ("Governance", "public-admin"),
    ("Public-Policy", "public-policy"), ("Policy-Analysis-and-Management", "public-policy"),
    ("Sociolog", "sociology"), ("Social-Forces", "sociology"),
    ("Social-Psychology-Quarterly", "sociology/social-psych"),
    ("Marriage-and-Family", "sociology/demography"), ("Demography", "demography"),
    ("Population", "demography"), ("Criminolog", "criminology"),
    ("Personality-and-Social-Psychology", "psychology"), ("Psychological", "psychology"),
    ("Cognitive-Psychology", "psychology"), ("Developmental-Psychology", "psychology"),
    ("Educational-Psychology", "psychology/education"),
    ("Applied-Psychology", "psychology/organizational"),
    ("Educational-Research", "education"), ("Education", "education"),
    ("Communication", "communication"), ("Public-Opinion", "communication/polisci"),
    ("New-Media", "communication"),
    ("Health-Economics", "economics/health"), ("Labor-Economics", "economics/labor"),
    ("Human-Resources", "economics/labor"), ("Urban-Economics", "economics/urban"),
    ("Economic-Geography", "economics/geography"),
    ("Environmental-Economics", "economics/environment"),
    ("Public-Economics", "economics/public"), ("Development-Economics", "economics/development"),
    ("International-Economics", "economics/international"),
    ("International-Money", "economics/international-finance"),
    ("Monetary-Economics", "economics/macro"), ("Money-Credit", "economics/macro"),
    ("Economic-Growth", "economics/growth"), ("Economic-Dynamics", "economics/macro"),
    ("Behavior-and-Organization", "economics/behavioral"),
    ("Law-Economics-and-Organization", "law-and-economics"),
    ("Law-and-Economics", "law-and-economics"), ("Law-Review", "law"), ("Law-Journal", "law"),
    ("Experimental-Economics", "economics/experimental"),
    ("Risk-and-Uncertainty", "economics/decision"),
    ("RAND-Journal", "economics/IO"),
    ("World-Development", "development-studies"), ("World-Bank", "economics/development"),
    ("Research-Policy", "innovation/science-policy"),
    ("China-Industrial", "economics"), ("China-Rural", "economics/agricultural"),
    ("Rural-Economy", "economics/agricultural"),
    ("Economic-Quarterly", "economics"), ("Economic-Research", "economics"),
    ("World-Economy", "economics/international"), ("Finance-and-Economics", "economics/finance"),
    ("IMF-Economic", "economics/international"), ("European-Economic", "economics"),
    ("Economic-Policy", "economics/policy"), ("Economic-Journal", "economics"),
    ("European-Economic-Association", "economics"), ("Quantitative-Economics", "economics"),
    ("Economics-and-Statistics", "economics/applied"),
    ("Economic-Literature", "economics"), ("Economic-Perspectives", "economics"),
    ("Annual-Review-of-Economics", "economics"),
    ("Social-Sciences-in-China", "social-science (general)"),
    ("Science-Skills", "natural-science"), ("Cell", "life-sciences"), ("PNAS", "natural-science"),
    ("NEJM", "medicine"), ("Lancet", "medicine"), ("JAMA", "medicine"),
    ("Cancer", "life-sciences"), ("Physical-Review", "physics"),
    ("American-Chemical", "chemistry"), ("Annals-of-Mathematics", "mathematics"),
    ("Conservation-Biology", "environment/ecology"), ("Global-Change-Biology", "environment/ecology"),
    ("Environmental-Science", "environment"), ("Global-Environmental", "environment"),
    ("Agricultural-Systems", "agriculture"), ("Field-Crops", "agriculture"),
    ("Advanced-Materials", "materials-science"), ("Molecular-Cell", "life-sciences"),
    ("Nature-Geoscience", "earth-science"), ("Earth-and-Planetary-Science-Letters", "earth-science"),
    ("Language-Linguistic-Society", "linguistics"),
    ("Chinese-Journal-of-Management-Science", "management/OR"),
    ("Finance-and-Trade-Economics", "economics/public"),
]

# Ranking / indexing labels. Only recorded when the pack's OWN text asserts them —
# this layer never invents a bibliometric claim.
RANKING_PATTERNS: list[tuple[str, str]] = [
    (r"\bFT-?\s?50\b", "FT50"),
    (r"\bUTD-?\s?24\b", "UTD24"),
    (r"\bABS\s*4\*", "ABS 4*"),
    (r"\bAJG\s*4\*", "AJG 4*"),
    (r"\bABS\s*4\b", "ABS 4"),
    (r"\bAJG\s*4\b", "AJG 4"),
    (r"\bABDC\s*A\*", "ABDC A*"),
    (r"\bCCF[-\s]?A\b", "CCF A"),
    (r"\bCCF[-\s]?B\b", "CCF B"),
    (r"\bCSSCI\b", "CSSCI"),
    (r"\bCSCD\b", "CSCD"),
    (r"北大核心|中文核心", "中文核心"),
    (r"中科院一区|一区\s*top|JCR\s*Q1|\bQ1\b", "JCR/CAS Q1-tier"),
    (r"\bSSCI\b", "SSCI"),
    (r"\bSCIE?\b", "SCI/SCIE"),
    (r"top[-\s]?5\b", "top-5"),
]

_WORD = re.compile(r"[a-z][a-z\-]{2,}")
_CJK_RUN = re.compile(r"[一-鿿]{2,}")

# Single-character CJK function words / affixes that make an n-gram meaningless.
CJK_NOISE = set("的了是在和与及或对于把被让使得所之其此该也都很更最就还又再等中前后上下内外")

STOPWORDS = set("""
the and for with that this from are was were has have had not but its it's they them their
you your our his her she who whom which what when where why how all any both each few more
most other some such only own same than too very can will just should now also into over
under about after before between during through against above below out off again further
then once here there while because until unless upon among within without across per via
paper papers article articles journal journals venue venues author authors submission submit
submitted submitting manuscript manuscripts editor editors editorial review reviewer reviewers
referee referees revision revisions accept accepted acceptance reject rejected rejection desk
skill skills pack packs use used using when should must does not need needs read reads
section sections abstract introduction conclusion appendix figure figures table tables
research study studies work works result results finding findings evidence data dataset
method methods methodology approach approaches analysis model models framework
new one two three first second third high higher low lower large small long short
scope fit topic selection positioning house style bar guidance official site live check
before after must-not anti-pattern trigger triggers venue-selection re-check guidelines
""".split())


def read(path: Path, limit: int | None = None) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    return text[:limit] if limit else text


def is_depth_pack(pack: Path) -> bool:
    """A depth pack = one venue, many venue-specific skills."""
    if not (pack / ".claude-plugin" / "plugin.json").exists():
        return False
    if pack.name in IMPORTED or pack.name in BUNDLES:
        return False
    if pack.name.endswith("Toolkit-Skills"):
        return False
    skills = list((pack / "skills").glob("*/SKILL.md")) if (pack / "skills").is_dir() else []
    if not skills:
        return False
    if len(skills) >= 25:
        return False
    if any(s.parent.name.endswith("-journal-workflow") for s in skills):
        return False
    return True


def discipline_of(name: str, default: str = "other") -> str:
    for kw, disc in DISC:
        if kw in name:
            return disc
    return default


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def h1_display_name(skill_md: str, fallback: str) -> str:
    """Pull a human display name out of a breadth-bundle venue profile's H1."""
    m = re.search(r"^#\s+(.+?)\s*$", skill_md, re.M)
    if not m:
        return fallback
    title = m.group(1)
    # strip the trailing slug echo in both ASCII and full-width parentheses
    title = re.sub(r"\s*[(（][^)）]*[)）]\s*$", "", title).strip()
    # Chinese profiles title as 《刊名》投稿 — keep just the journal name
    m2 = re.search(r"《([^》]+)》", title)
    if m2:
        title = m2.group(1).strip()
    title = re.sub(r"(投稿|写作|发表)$", "", title).strip()
    return title or fallback


def frontmatter_description(skill_md: str) -> str:
    m = re.match(r"---\n(.*?)\n---\n", skill_md, re.S)
    if not m:
        return ""
    d = re.search(r"^description:\s*(.+?)\s*$", m.group(1), re.M)
    return d.group(1) if d else ""


def strip_frontmatter(skill_md: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", skill_md, flags=re.S)


_BRACKET_CJK = re.compile(r"《([^》]{2,40})》")
_LONG_NAME_ACRONYM = re.compile(
    r"([A-Z][A-Za-z0-9&'’\-]*(?:\s+[A-Za-z0-9&'’\-]+){2,9})\s*[(（]([A-Za-z][A-Za-z0-9&\-]{1,12})[)）]"
)
_PAREN_NAME = re.compile(r"[(（]([^)）]{2,60})[)）]")


def normalize_identity(text: str) -> str:
    return re.sub(r"[^a-z0-9一-鿿]", "", text.lower())


def acronym_fits(acronym: str, name: str) -> bool:
    """Does `acronym` plausibly abbreviate `name`?

    Parentheses in these packs hold society names as often as venue names —
    "Anesthesiology (ASA)" is the American Society of Anesthesiologists, not an alias
    for the journal. Requiring the acronym's letters to appear in order among the
    initials of the name's words drops those without losing QJE / ICML / AER.
    """
    letters = [c for c in acronym.lower() if c.isalnum()]
    initials = [w[0].lower() for w in re.findall(r"[A-Za-z0-9]+", name) if w]
    if not letters or not initials:
        return False
    i = 0
    for initial in initials:
        if i < len(letters) and initial == letters[i]:
            i += 1
    return i == len(letters)


def identity_keys(title_snippet: str, display_name: str, venue_id: str) -> set[str]:
    """Names by which a venue can be recognised across the depth/breadth tiers.

    The same journal is often a depth pack under its English name and a breadth
    profile under its Chinese name (or an acronym vs. its expansion). Matching on
    slug alone misses those, which would double-count the venue in a shortlist.
    Only the *title area* of a pack is scanned — scanning whole bodies would pull in
    every venue the pack merely discusses.
    """
    keys = {normalize_identity(venue_id), normalize_identity(display_name)}
    long_names = [display_name]
    for name in _BRACKET_CJK.findall(title_snippet):
        keys.add(normalize_identity(name))
        long_names.append(name)
    for long_name, acronym in _LONG_NAME_ACRONYM.findall(title_snippet):
        if not acronym_fits(acronym, long_name):
            continue
        keys.add(normalize_identity(long_name))
        keys.add(normalize_identity(acronym))
        long_names.append(long_name)
    for name in _PAREN_NAME.findall(title_snippet):
        if not re.search(r"[A-Za-z一-鿿]", name) or "," in name:
            continue
        # a bare parenthetical acronym must abbreviate one of the venue's own names
        if len(name) <= 12 and " " not in name:
            if not any(acronym_fits(name, n) for n in long_names):
                continue
        keys.add(normalize_identity(name))
    return {k for k in keys if len(k) >= 3}


def ranking_labels(text: str) -> list[str]:
    """Extract indexing/ranking labels the pack itself asserts. Never inferred."""
    found: list[str] = []
    for pattern, label in RANKING_PATTERNS:
        if re.search(pattern, text) and label not in found:
            found.append(label)
    return found


# --- scope text -------------------------------------------------------------

SCOPE_SKILL_HINTS = ("topic-selection", "positioning", "scope", "fit", "contribution-framing")


def depth_scope_text(pack: Path) -> str:
    """Scope-describing prose for a depth pack: skill descriptions + fit skills + README."""
    parts: list[str] = []
    for skill in sorted((pack / "skills").glob("*/SKILL.md")):
        body = read(skill)
        parts.append(frontmatter_description(body))
        if any(h in skill.parent.name for h in SCOPE_SKILL_HINTS):
            parts.append(strip_frontmatter(body)[:6000])
    readme = pack / "README.md"
    if readme.exists():
        parts.append(read(readme, 3000))
    sm = pack / "resources" / "official-source-map.md"
    if sm.exists():
        # Aims/scope section only — never the volatile-facts sections.
        text = read(sm)
        m = re.search(r"##\s*Aims[^\n]*\n(.*?)(?=\n##\s|\Z)", text, re.S | re.I)
        if m:
            parts.append(m.group(1)[:3000])
    return "\n".join(p for p in parts if p)


def breadth_scope_text(skill_path: Path) -> str:
    body = read(skill_path)
    return frontmatter_description(body) + "\n" + strip_frontmatter(body)[:8000]


# --- keyword derivation -----------------------------------------------------

def cjk_ngrams(text: str) -> list[str]:
    """2- and 3-character n-grams from CJK runs, minus grams built on function words.

    No segmenter is available (and none should be a dependency), so we over-generate
    and let TF-IDF keep only the grams that actually discriminate between venues.
    """
    grams: list[str] = []
    for run in _CJK_RUN.findall(text):
        for size in (2, 3, 4):
            for i in range(len(run) - size + 1):
                gram = run[i:i + size]
                if gram[0] in CJK_NOISE or gram[-1] in CJK_NOISE:
                    continue
                grams.append(gram)
    return grams


def tokenize(text: str) -> list[str]:
    lowered = text.lower()
    words = [w for w in _WORD.findall(lowered) if w not in STOPWORDS and len(w) > 3]
    return words + cjk_ngrams(text)


def candidate_terms(text: str) -> Counter:
    """Unigrams plus adjacent bigrams, so phrases like 'natural experiment' survive."""
    words = tokenize(text)
    counts = Counter(words)
    for a, b in zip(words, words[1:]):
        if _WORD.fullmatch(a) and _WORD.fullmatch(b):
            counts[f"{a} {b}"] += 1
    return counts


def _redundant(term: str, picked: list[str]) -> bool:
    """True when `term` adds nothing over an already-picked term.

    Latin terms overlap by whole word ('natural experiment' subsumes 'experiment');
    CJK n-grams overlap by substring, since the over-generated grams of one phrase
    would otherwise fill the whole keyword slate.
    """
    for other in picked:
        if term == other:
            return True
        if _CJK_RUN.fullmatch(term) and _CJK_RUN.fullmatch(other):
            if term in other or other in term:
                return True
        elif term in other.split() or other in term.split():
            return True
    return False


def derive_keywords(docs: dict[str, str], top_n: int = 40) -> dict[str, list[str]]:
    """TF-IDF over the venue corpus; returns the most venue-distinctive terms.

    Deterministic and dependency-free, so it reruns identically in CI.
    """
    tf = {vid: candidate_terms(text) for vid, text in docs.items()}
    df: Counter = Counter()
    for counts in tf.values():
        df.update(counts.keys())
    n_docs = max(len(docs), 1)
    out: dict[str, list[str]] = {}
    for vid, counts in tf.items():
        total = sum(counts.values()) or 1
        scored = []
        for term, c in counts.items():
            if c < 2 and " " not in term:
                continue
            doc_freq = df[term]
            if doc_freq > n_docs * 0.35:          # too common to discriminate
                continue
            idf = math.log(n_docs / (1 + doc_freq))
            if idf <= 0:
                continue
            score = (c / total) * idf
            if _CJK_RUN.fullmatch(term):
                # over-generated grams: prefer the longer ones, which are far more
                # likely to be a real word than a cross-boundary fragment
                score *= 1 + 0.25 * (len(term) - 2)
            scored.append((score, term))
        scored.sort(key=lambda x: (-x[0], x[1]))
        picked: list[str] = []
        for _, term in scored:
            if _redundant(term, picked):
                continue
            picked.append(term)
            if len(picked) >= top_n:
                break
        out[vid] = picked
    return out
