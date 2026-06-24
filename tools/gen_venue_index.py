#!/usr/bin/env python3
"""Generate a STABLE venue index for the journal-match capability.
Stable fields only (discipline / tier / lane / region / source-map pointer) — NO
volatile fees/acceptance (those stay in each pack's official-source-map.md, kept
current by the live-check campaign). Covers first-party DEPTH packs; breadth
bundles are added as pointer rows for the long tail of profile-only venues.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTED = {"AER-Skills", "AER-skills", "Nature-Skills", "nature-skills",
            "nature-paper-skills", "claude-scholar", "codex-claude-academic-skills"}

# Chinese-language depth packs (from the Tier-4 inventory)
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

# discipline keyword map (substring on pack dir, first match wins; order matters)
DISC = [
    # CS/AI conferences
    ("AAAI", "cs-ai (conference)"), ("AISTATS", "cs-ai (conference)"),
    ("ICLR", "cs-ai (conference)"), ("ICML", "cs-ai (conference)"),
    ("IJCAI", "cs-ai (conference)"), ("NeurIPS", "cs-ai (conference)"),
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
]


def is_depth_pack(p: Path) -> bool:
    if not (p / ".claude-plugin" / "plugin.json").exists():
        return False
    if p.name in IMPORTED:
        return False
    skills = list((p / "skills").glob("*/SKILL.md")) if (p / "skills").is_dir() else []
    if not skills:
        return False
    # breadth bundles: >=25 skills or a *-journal-workflow router
    if len(skills) >= 25:
        return False
    if any(s.parent.name.endswith("-journal-workflow") for s in skills):
        return False
    return True


def discipline_of(name: str) -> str:
    for kw, d in DISC:
        if kw in name:
            return d
    return "other"


rows = []
for plugin in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
    pack = plugin.parent.parent
    if not is_depth_pack(pack):
        continue
    name = pack.name
    display = name.replace("-Skills", "").replace("-", " ")
    disc = discipline_of(name)
    tier = TIER.get(name, "field")
    NON_EMPIRICAL = {"philosophy", "history", "art-history", "humanities/literature",
                     "humanities/theory", "religion", "anthropology", "mathematics",
                     "economics/theory", "economics/game-theory"}
    lane = THEORY.get(name) or ("interpretive/theory" if disc in NON_EMPIRICAL else "empirical")
    region = "china" if name in CHINA else "international"
    sm = f"{name}/resources/official-source-map.md"
    sm_exists = (ROOT / sm).exists()
    rows.append((name, display, disc, tier, lane, region, sm if sm_exists else ""))

rows.sort(key=lambda r: (r[2], r[0]))
out = ROOT / "shared-resources/journal-selection/venue-index.tsv"
out.parent.mkdir(parents=True, exist_ok=True)
with out.open("w", encoding="utf-8") as f:
    f.write("pack_dir\tdisplay_name\tdiscipline\ttier\tlane\tregion\tsource_map\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
print(f"wrote {len(rows)} depth-pack rows -> {out}")
# distribution sanity
from collections import Counter
print("disciplines:", dict(Counter(r[2] for r in rows)))
print("other (need review):", [r[0] for r in rows if r[2] == "other"])
