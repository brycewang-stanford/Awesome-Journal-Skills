#!/usr/bin/env python3
"""Generate uniform cover cards for EVERY breadth-bundle journal.

This is the companion to gen_covers.py (which renders the natural-science depth
packs, the 22 English-flagship cards, and the bundle hero). That script left the
non-flagship breadth journals without per-journal art. This script closes that
gap: it renders one 240x320 card for each of the ~263 remaining journals across
the three breadth bundles, using the same card system so the galleries stay
visually consistent.

  * English-SocialScience-Journal-Skills  (100 journals; 22 already had cards)
  * English-NaturalScience-Journal-Skills (100 journals;  5 already had cards)
  * Chinese-SocialScience-Journal-Skills  (102 journals; 12 already had cards)

Journal display names are read from each skill's SKILL.md heading (the single
source of truth), so the cards never drift from the packs. Discipline -> colour
is assigned by explicit, reviewable maps below. Cards that already exist in
assets/covers/ are skipped, so existing approved art is never churned.

Usage:
  python3 gen_breadth_covers.py            # render all missing cards
  python3 gen_breadth_covers.py --force    # re-render even if the png exists
  python3 gen_breadth_covers.py --list     # print the plan, render nothing

Requires rsvg-convert (librsvg); falls back to cairosvg, then macOS sips.
"""
import math
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "covers")

# ---------------------------------------------------------------------------
# Discipline palette. All colours are dark enough for white text on the header
# band and pill. Social-science keys match gen_covers.py; the rest are new.
# ---------------------------------------------------------------------------
PALETTE = {
    # social science (shared with gen_covers.py)
    "econ":     "#7a1322",  # economics — deep crimson
    "finance":  "#15406b",  # finance — deep navy
    "mgmt":     "#14635a",  # management / strategy / org — teal
    "mktg":     "#9a4a06",  # marketing — burnt orange
    "acct":     "#3f3d73",  # accounting / audit — indigo
    "opsis":    "#2f5a34",  # operations & information systems — forest
    # social science (new, for the Chinese bundle)
    "pubadmin": "#2f4858",  # public administration / governance — deep slate
    "scimgmt":  "#1f5b52",  # science studies / S&T management — dark teal-green
    "socio":    "#8a4a2a",  # sociology / social security — terracotta
    # natural science (new)
    "gen":      "#1f3a5f",  # general & multidisciplinary — deep blue
    "bio":      "#157a5b",  # cell / molecular / genome biology — emerald
    "eco":      "#5b6b1f",  # ecology / evolution / plant — olive
    "immuno":   "#8a2d6b",  # immunology / microbiology — plum
    "neuro":    "#5b2a86",  # neuroscience & behaviour — violet
    "med":      "#a01f2e",  # clinical medicine — medical red
    "onco":     "#6e1f3a",  # oncology / translational — wine
    "phys":     "#1b2f7a",  # physics — royal blue
    "astro":    "#2e2a6e",  # astronomy — cosmic indigo
    "chem":     "#8a5a14",  # chemistry — dark amber
    "matsci":   "#7a3b1a",  # materials & energy — copper
    "earth":    "#146b6b",  # earth / environment / climate — deep cyan
    "cs":       "#37474f",  # CS / AI / engineering — steel
    "math":     "#46327a",  # mathematics — deep purple
}

BANNER = {
    "econ": "ECONOMICS", "finance": "FINANCE", "mgmt": "MANAGEMENT",
    "mktg": "MARKETING", "acct": "ACCOUNTING", "opsis": "OPERATIONS · IS",
    "pubadmin": "公共管理", "scimgmt": "科学学 · 科技管理",
    "socio": "社会学",
    "gen": "MULTIDISCIPLINARY", "bio": "LIFE SCIENCES", "eco": "ECOLOGY · EVOLUTION",
    "immuno": "IMMUNOLOGY", "neuro": "NEUROSCIENCE", "med": "CLINICAL MEDICINE",
    "onco": "ONCOLOGY", "phys": "PHYSICS", "astro": "ASTRONOMY", "chem": "CHEMISTRY",
    "matsci": "MATERIALS · ENERGY", "earth": "EARTH · ENVIRONMENT",
    "cs": "COMPUTING · AI", "math": "MATHEMATICS",
}
# Chinese banners get their discipline word in Chinese (set per-key above for the
# CN-only keys). Econ/finance/etc are reused for Chinese journals with a CN word:
CN_BANNER = {
    "econ": "经济学", "finance": "金融", "mgmt": "管理学",
    "acct": "会计 · 审计", "pubadmin": "公共管理",
    "scimgmt": "科学学 · 科技管理", "socio": "社会学",
}

# ---------------------------------------------------------------------------
# Discipline assignment by slug. Social-science maps follow the README roadmap;
# the natural-science map is grouped by the README's category counts.
# ---------------------------------------------------------------------------
EN_SOC = {
    "econ": [
        "american-economic-review", "quarterly-journal-of-economics",
        "journal-of-political-economy", "econometrica", "review-of-economic-studies",
        "aer-insights", "aej-applied-economics", "aej-macroeconomics",
        "aej-microeconomics", "aej-economic-policy", "journal-of-economic-literature",
        "journal-of-economic-perspectives", "review-of-economics-and-statistics",
        "journal-of-econometrics", "journal-of-monetary-economics",
        "journal-of-economic-growth", "journal-of-labor-economics",
        "journal-of-the-european-economic-association", "the-economic-journal",
        "rand-journal-of-economics", "journal-of-international-economics",
        "journal-of-public-economics", "journal-of-development-economics",
        "journal-of-economic-theory", "journal-of-money-credit-and-banking",
        "review-of-economic-dynamics", "european-economic-review",
        "journal-of-human-resources", "international-economic-review",
        "experimental-economics", "journal-of-applied-econometrics",
        "journal-of-business-and-economic-statistics", "journal-of-health-economics",
        "journal-of-environmental-economics-and-management", "journal-of-urban-economics",
        "games-and-economic-behavior", "journal-of-law-and-economics",
        "journal-of-law-economics-and-organization", "world-development",
        "world-bank-economic-review", "imf-economic-review", "annual-review-of-economics",
        "brookings-papers-on-economic-activity", "economic-policy",
        "journal-of-risk-and-uncertainty", "quantitative-economics",
        "the-econometrics-journal", "econometric-theory",
        "journal-of-economic-behavior-and-organization", "journal-of-economic-geography",
    ],
    "finance": [
        "journal-of-finance", "journal-of-financial-economics", "review-of-financial-studies",
        "review-of-finance", "journal-of-financial-and-quantitative-analysis",
        "journal-of-financial-intermediation", "journal-of-financial-markets",
        "journal-of-banking-and-finance", "journal-of-corporate-finance",
        "journal-of-international-money-and-finance", "mathematical-finance",
        "journal-of-empirical-finance", "financial-management",
    ],
    "mgmt": [
        "academy-of-management-journal", "academy-of-management-review",
        "academy-of-management-annals", "administrative-science-quarterly",
        "strategic-management-journal", "organization-science", "journal-of-management-en",
        "journal-of-management-studies", "organization-studies", "human-relations",
        "human-resource-management", "journal-of-international-business-studies",
        "research-policy", "journal-of-business-venturing",
        "entrepreneurship-theory-and-practice",
    ],
    "mktg": [
        "journal-of-marketing", "journal-of-marketing-research", "marketing-science",
        "journal-of-consumer-research", "journal-of-consumer-psychology",
        "journal-of-the-academy-of-marketing-science",
    ],
    "acct": [
        "the-accounting-review", "journal-of-accounting-research",
        "journal-of-accounting-and-economics", "review-of-accounting-studies",
        "contemporary-accounting-research", "accounting-organizations-and-society",
    ],
    "opsis": [
        "management-science", "operations-research",
        "manufacturing-and-service-operations-management",
        "journal-of-operations-management", "production-and-operations-management",
        "mis-quarterly", "information-systems-research",
        "journal-of-management-information-systems",
        "journal-of-the-association-for-information-systems",
        "informs-journal-on-computing",
    ],
}

EN_NAT = {
    "gen": [
        "nature", "science", "pnas", "science-advances", "nature-communications",
        "national-science-review", "the-innovation",
        "science-signaling", "nature-reviews-methods-primers",
    ],
    "bio": [
        "cell", "molecular-cell", "developmental-cell", "cell-stem-cell",
        "current-biology", "nature-cell-biology", "nature-genetics", "nature-methods",
        "nature-biotechnology", "nature-structural-and-molecular-biology",
        "the-embo-journal", "genome-biology", "nucleic-acids-research", "the-plant-cell",
        "plos-biology", "elife", "cell-metabolism",
    ],
    "eco": [
        "ecology-letters", "nature-ecology-and-evolution", "molecular-biology-and-evolution",
        "trends-in-ecology-and-evolution", "global-ecology-and-biogeography",
        "the-isme-journal",
        "annual-review-of-ecology-evolution-and-systematics", "molecular-ecology",
        "journal-of-ecology", "functional-ecology",
    ],
    "immuno": [
        "immunity", "nature-immunology", "nature-microbiology", "cell-host-and-microbe",
        "journal-of-experimental-medicine", "science-immunology",
    ],
    "neuro": [
        "neuron", "nature-neuroscience", "trends-in-cognitive-sciences",
        "molecular-psychiatry", "nature-human-behaviour",
    ],
    "med": [
        "nejm", "the-lancet", "jama", "the-bmj", "annals-of-internal-medicine",
        "plos-medicine", "nature-medicine", "science-translational-medicine",
        "circulation", "european-heart-journal",
        "journal-of-the-american-college-of-cardiology", "gastroenterology", "gut",
        "blood", "diabetes-care", "the-lancet-infectious-diseases", "the-lancet-neurology",
        "journal-of-clinical-investigation", "cell-reports-medicine",
        "nature-reviews-drug-discovery", "the-lancet-digital-health",
    ],
    "onco": [
        "cancer-cell", "cancer-discovery", "journal-of-clinical-oncology",
        "ca-a-cancer-journal-for-clinicians", "the-lancet-oncology",
    ],
    "phys": [
        "physical-review-letters", "physical-review-b", "physical-review-d",
        "physical-review-x", "reviews-of-modern-physics", "reports-on-progress-in-physics",
        "nature-physics", "nature-photonics", "prx-quantum",
        "journal-of-high-energy-physics", "new-journal-of-physics",
        "physical-review-e", "physical-review-applied", "nature-reviews-physics",
        "physics-reports", "classical-and-quantum-gravity", "living-reviews-in-relativity",
    ],
    "astro": [
        "the-astrophysical-journal", "monthly-notices-of-the-royal-astronomical-society",
        "nature-astronomy",
        "astronomy-and-astrophysics", "the-astronomical-journal",
        "astrophysical-journal-letters", "annual-review-of-astronomy-and-astrophysics",
    ],
    "chem": [
        "journal-of-the-american-chemical-society",
        "angewandte-chemie-international-edition", "chemical-reviews",
        "chemical-society-reviews", "accounts-of-chemical-research", "nature-chemistry",
        "nature-catalysis", "chem", "acs-nano",
        "nature-reviews-chemistry", "acs-catalysis",
        "nature-synthesis", "jacs-au", "acs-central-science",
        "coordination-chemistry-reviews",
    ],
    "matsci": [
        "advanced-materials", "nature-materials", "nature-nanotechnology",
        "energy-and-environmental-science", "joule", "nature-energy",
        "nature-reviews-materials", "matter",
        "advanced-energy-materials", "advanced-functional-materials",
        "acs-energy-letters", "npj-computational-materials",
    ],
    "earth": [
        "nature-geoscience", "nature-climate-change", "nature-sustainability",
        "one-earth", "environmental-science-and-technology",
        "geophysical-research-letters", "reviews-of-geophysics", "nature-water",
        "water-research", "atmospheric-chemistry-and-physics",
        "journal-of-geophysical-research-atmospheres", "nature-reviews-earth-and-environment",
        "earths-future", "the-cryosphere",
    ],
    "cs": [
        "ieee-transactions-on-pattern-analysis-and-machine-intelligence",
        "journal-of-machine-learning-research", "nature-machine-intelligence",
        "science-robotics", "journal-of-the-acm",
        "siam-journal-on-computing",
    ],
    "math": [
        "annals-of-mathematics", "inventiones-mathematicae",
        "journal-of-the-american-mathematical-society",
        "communications-on-pure-and-applied-mathematics", "advances-in-mathematics",
        "duke-mathematical-journal", "siam-review",
        "acta-mathematica", "geometry-and-topology",
        "foundations-of-computational-mathematics",
    ],
}

CN_SOC = {
    "econ": [
        "economic-research", "china-industrial-economics", "journal-of-world-economy",
        "china-economic-quarterly", "asia-pacific-economic-review", "china-economic-studies",
        "china-rural-economy", "china-rural-survey", "comparative-economic-and-social-systems",
        "contemporary-economy-of-japan", "contemporary-finance-and-economics",
        "east-china-economic-management", "economic-aspects", "economic-perspectives",
        "economic-problems", "economic-review-cn", "economic-science",
        "economic-theory-and-business-management", "economist-cn", "finance-and-economics",
        "finance-and-trade-economics", "industrial-economics-research",
        "inquiry-into-economic-issues", "international-economic-review-cn",
        "international-economics-and-trade-research", "issues-in-agricultural-economy",
        "journal-of-agrotechnical-economics", "journal-of-business-economics",
        "journal-of-central-university-of-finance-and-economics",
        "journal-of-finance-and-economics",
        "journal-of-guangdong-university-of-finance-and-economics",
        "journal-of-international-trade",
        "journal-of-jiangxi-university-of-finance-and-economics",
        "journal-of-macro-quality-research",
        "journal-of-shanghai-university-of-finance-and-economics",
        "journal-of-shanxi-university-of-finance-and-economics",
        "journal-of-zhongnan-university-of-economics-and-law", "macroeconomics",
        "modern-economic-research", "modern-economic-science", "modern-finance-and-economics",
        "nankai-economic-studies", "public-finance-research", "reform",
        "reform-of-economic-system", "research-on-economics-and-management",
        "research-on-financial-and-economic-issues", "review-of-political-economy",
        "rural-economy", "shanghai-journal-of-economics", "south-china-journal-of-economics",
        "studies-in-labor-economics", "world-economic-papers", "world-economic-studies",
    ],
    "finance": [
        "journal-of-financial-research", "chinese-review-of-financial-studies",
        "financial-regulation-research", "modern-financial-research",
        "securities-market-herald", "studies-of-financial-economics",
        "studies-of-international-finance",
    ],
    "mgmt": [
        "management-world", "nankai-business-review", "journal-of-management-sciences-china",
        "business-management-journal", "chinese-journal-of-management",
        "chinese-journal-of-management-science", "foreign-economics-and-management",
        "frontiers-of-engineering-management-science-and-technology",
        "journal-of-industrial-engineering-and-engineering-management",
        "journal-of-management", "management-review", "management-science-cn",
        "organization-and-management",
    ],
    "acct": [
        "accounting-research", "accounting-and-economics-research",
        "auditing-and-economics-research", "auditing-research", "china-accounting-review",
        "tax-research",
    ],
    "scimgmt": [
        "journal-of-quantitative-technological-economics",
        "bulletin-of-chinese-academy-of-sciences", "china-soft-science",
        "forum-on-science-and-technology-in-china", "research-and-development-management",
        "science-and-technology-progress-and-policy",
        "science-of-science-and-management-of-st", "science-research-management",
        "scientific-decision-making", "scientific-management-research", "soft-science",
        "studies-in-science-of-science", "systems-engineering-theory-and-practice",
    ],
    "pubadmin": [
        "china-public-administration-review", "chinese-public-administration",
        "e-government", "governance-studies", "journal-of-public-management",
        "public-administration-and-policy-review",
    ],
    "socio": [
        "social-sciences-in-china", "sociological-studies", "social-security-studies",
    ],
}

# ---------------------------------------------------------------------------
# Curated abbreviations. Used as the subtitle for English cards, and promoted to
# the hero text when the full name would otherwise render too small.
# ---------------------------------------------------------------------------
ABBREV = {
    "american-economic-review": "AER", "quarterly-journal-of-economics": "QJE",
    "journal-of-political-economy": "JPE", "review-of-economic-studies": "REStud",
    "aer-insights": "AER: Insights", "aej-applied-economics": "AEJ: Applied",
    "aej-macroeconomics": "AEJ: Macro", "aej-microeconomics": "AEJ: Micro",
    "aej-economic-policy": "AEJ: Policy", "journal-of-economic-literature": "JEL",
    "journal-of-economic-perspectives": "JEP", "review-of-economics-and-statistics": "REStat",
    "journal-of-econometrics": "JoE", "journal-of-monetary-economics": "JME",
    "journal-of-economic-growth": "JEG", "journal-of-labor-economics": "JOLE",
    "journal-of-the-european-economic-association": "JEEA", "the-economic-journal": "EJ",
    "rand-journal-of-economics": "RAND JE", "journal-of-international-economics": "JIE",
    "journal-of-public-economics": "JPubE", "journal-of-development-economics": "JDE",
    "journal-of-economic-theory": "JET", "journal-of-money-credit-and-banking": "JMCB",
    "review-of-economic-dynamics": "RED", "european-economic-review": "EER",
    "journal-of-human-resources": "JHR", "international-economic-review": "IER",
    "journal-of-applied-econometrics": "JAE-Econ",
    "journal-of-business-and-economic-statistics": "JBES",
    "journal-of-health-economics": "JHE",
    "journal-of-environmental-economics-and-management": "JEEM",
    "journal-of-urban-economics": "JUE", "games-and-economic-behavior": "GEB",
    "journal-of-law-and-economics": "JLE", "journal-of-law-economics-and-organization": "JLEO",
    "world-bank-economic-review": "WBER", "imf-economic-review": "IMF ER",
    "brookings-papers-on-economic-activity": "BPEA",
    "journal-of-risk-and-uncertainty": "JRU", "quantitative-economics": "QE",
    "the-econometrics-journal": "EctJ", "econometric-theory": "ET",
    "journal-of-economic-behavior-and-organization": "JEBO",
    "journal-of-economic-geography": "JEG-Geo", "annual-review-of-economics": "Ann. Rev. Econ.",
    "journal-of-finance": "JF", "journal-of-financial-economics": "JFE",
    "review-of-financial-studies": "RFS", "review-of-finance": "RoF",
    "journal-of-financial-and-quantitative-analysis": "JFQA",
    "journal-of-financial-intermediation": "JFI", "journal-of-financial-markets": "JFM",
    "journal-of-banking-and-finance": "JBF", "journal-of-corporate-finance": "JCF",
    "journal-of-international-money-and-finance": "JIMF", "mathematical-finance": "Math. Fin.",
    "journal-of-empirical-finance": "JEmpF", "financial-management": "FM",
    "academy-of-management-journal": "AMJ", "academy-of-management-review": "AMR",
    "academy-of-management-annals": "AMA", "administrative-science-quarterly": "ASQ",
    "strategic-management-journal": "SMJ", "organization-science": "Org. Sci.",
    "journal-of-management-en": "JOM", "journal-of-management-studies": "JMS",
    "organization-studies": "Org. Studies", "human-relations": "Human Relations",
    "human-resource-management": "HRM", "journal-of-international-business-studies": "JIBS",
    "research-policy": "Res. Policy", "journal-of-business-venturing": "JBV",
    "entrepreneurship-theory-and-practice": "ETP", "journal-of-marketing": "JM",
    "journal-of-marketing-research": "JMR", "marketing-science": "Mktg. Sci.",
    "journal-of-consumer-research": "JCR", "journal-of-consumer-psychology": "JCP",
    "journal-of-the-academy-of-marketing-science": "JAMS", "the-accounting-review": "TAR",
    "journal-of-accounting-research": "JAR", "journal-of-accounting-and-economics": "JAE",
    "review-of-accounting-studies": "RAST", "contemporary-accounting-research": "CAR",
    "accounting-organizations-and-society": "AOS", "management-science": "Mgmt. Sci.",
    "operations-research": "Oper. Res.", "manufacturing-and-service-operations-management": "M&SOM",
    "journal-of-operations-management": "JOM-Ops", "production-and-operations-management": "POM",
    "mis-quarterly": "MISQ", "information-systems-research": "ISR",
    "journal-of-management-information-systems": "JMIS",
    "journal-of-the-association-for-information-systems": "JAIS",
    "informs-journal-on-computing": "IJOC",
    # natural science
    "pnas": "PNAS", "nejm": "NEJM", "science-advances": "Sci. Adv.",
    "national-science-review": "NSR", "nature-communications": "Nat. Commun.",
    "the-embo-journal": "EMBO J.", "genome-biology": "Genome Biol.",
    "nucleic-acids-research": "NAR", "plos-biology": "PLOS Biol.",
    "molecular-biology-and-evolution": "MBE", "nature-cell-biology": "Nat. Cell Biol.",
    "nature-structural-and-molecular-biology": "NSMB",
    "journal-of-experimental-medicine": "JEM", "science-immunology": "Sci. Immunol.",
    "trends-in-cognitive-sciences": "TiCS", "annals-of-internal-medicine": "Ann. Intern. Med.",
    "plos-medicine": "PLOS Med.", "science-translational-medicine": "Sci. Transl. Med.",
    "european-heart-journal": "EHJ", "journal-of-the-american-college-of-cardiology": "JACC",
    "the-lancet-infectious-diseases": "Lancet ID", "the-lancet-neurology": "Lancet Neurol.",
    "the-lancet-oncology": "Lancet Oncol.", "journal-of-clinical-investigation": "JCI",
    "journal-of-clinical-oncology": "JCO", "cancer-discovery": "Cancer Discov.",
    "ca-a-cancer-journal-for-clinicians": "CA Cancer J. Clin.",
    "physical-review-letters": "PRL", "physical-review-b": "PRB", "physical-review-d": "PRD",
    "physical-review-x": "PRX", "reviews-of-modern-physics": "RMP",
    "reports-on-progress-in-physics": "RoPP", "the-astrophysical-journal": "ApJ",
    "monthly-notices-of-the-royal-astronomical-society": "MNRAS",
    "journal-of-the-american-chemical-society": "JACS",
    "angewandte-chemie-international-edition": "Angew. Chem.",
    "chemical-reviews": "Chem. Rev.", "chemical-society-reviews": "Chem. Soc. Rev.",
    "accounts-of-chemical-research": "Acc. Chem. Res.",
    "energy-and-environmental-science": "EES",
    "environmental-science-and-technology": "ES&T", "advanced-materials": "Adv. Mater.",
    "ieee-transactions-on-pattern-analysis-and-machine-intelligence": "IEEE TPAMI",
    "journal-of-machine-learning-research": "JMLR",
    "annals-of-mathematics": "Ann. of Math.", "inventiones-mathematicae": "Invent. Math.",
    "journal-of-the-american-mathematical-society": "JAMS-Math",
    # --- breadth STEM expansion (2026-06) ---
    "journal-of-high-energy-physics": "JHEP", "new-journal-of-physics": "NJP",
    "astronomy-and-astrophysics": "A&A", "the-astronomical-journal": "AJ",
    "nature-reviews-chemistry": "Nat. Rev. Chem.", "acs-catalysis": "ACS Catal.",
    "nature-reviews-materials": "Nat. Rev. Mater.", "matter": "Matter",
    "trends-in-ecology-and-evolution": "TREE",
    "global-ecology-and-biogeography": "GEB", "the-isme-journal": "ISME J.",
    "geophysical-research-letters": "GRL", "reviews-of-geophysics": "Rev. Geophys.",
    "nature-water": "Nat. Water", "water-research": "Water Res.",
    "atmospheric-chemistry-and-physics": "ACP",
    "communications-on-pure-and-applied-mathematics": "CPAM",
    "advances-in-mathematics": "Adv. Math.", "duke-mathematical-journal": "Duke Math. J.",
    "siam-review": "SIAM Rev.", "journal-of-the-acm": "JACM",
    "science-signaling": "Sci. Signal.",
    "nature-reviews-methods-primers": "Nat. Rev. Methods Primers",
    "cell-reports-medicine": "Cell Rep. Med.",
    # --- breadth STEM expansion wave 2 (2026-06) ---
    "physical-review-e": "PRE", "physical-review-applied": "PR Applied",
    "nature-reviews-physics": "Nat. Rev. Phys.", "physics-reports": "Phys. Rep.",
    "classical-and-quantum-gravity": "CQG", "living-reviews-in-relativity": "LRR",
    "astrophysical-journal-letters": "ApJL",
    "annual-review-of-astronomy-and-astrophysics": "ARA&A",
    "nature-synthesis": "Nat. Synth.", "jacs-au": "JACS Au",
    "acs-central-science": "ACS Cent. Sci.", "coordination-chemistry-reviews": "Coord. Chem. Rev.",
    "advanced-energy-materials": "Adv. Energy Mater.",
    "advanced-functional-materials": "Adv. Funct. Mater.",
    "acs-energy-letters": "ACS Energy Lett.", "npj-computational-materials": "npj Comput. Mater.",
    "annual-review-of-ecology-evolution-and-systematics": "AREES",
    "molecular-ecology": "Mol. Ecol.", "journal-of-ecology": "J. Ecol.",
    "functional-ecology": "Funct. Ecol.",
    "journal-of-geophysical-research-atmospheres": "JGR-Atmos.",
    "nature-reviews-earth-and-environment": "Nat. Rev. Earth Environ.",
    "earths-future": "Earth's Future", "the-cryosphere": "TC",
    "acta-mathematica": "Acta Math.", "geometry-and-topology": "Geom. Topol.",
    "foundations-of-computational-mathematics": "FoCM", "siam-journal-on-computing": "SICOMP",
    "nature-reviews-drug-discovery": "Nat. Rev. Drug Discov.",
    "the-lancet-digital-health": "Lancet Digit. Health",
}

# Names that should render with the abbreviation as the hero (full name too long
# even at 3 lines, or simply far more recognisable as an acronym).
HERO_ABBREV = {
    "ieee-transactions-on-pattern-analysis-and-machine-intelligence",
    "monthly-notices-of-the-royal-astronomical-society",
    "journal-of-the-american-college-of-cardiology",
    "ca-a-cancer-journal-for-clinicians",
}

# ---------------------------------------------------------------------------
# SVG card (matches gen_covers.py geometry; supports 1-3 hero lines).
# ---------------------------------------------------------------------------
FONT_LATIN = "Helvetica Neue, Helvetica, Arial, sans-serif"
FONT_CJK = "PingFang SC, Hiragino Sans GB, Noto Sans CJK SC, STHeiti, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def balance_words(words, nlines):
    """Greedily split words into nlines roughly-equal-length lines."""
    if nlines == 1:
        return [" ".join(words)]
    total = sum(len(w) for w in words) + len(words) - 1
    target = total / nlines
    lines, cur, curlen = [], [], 0
    for i, w in enumerate(words):
        add = len(w) + (1 if cur else 0)
        remaining_lines = nlines - len(lines)
        if cur and curlen + add > target and remaining_lines > 1 and \
                (len(words) - i) >= remaining_lines - 1:
            lines.append(" ".join(cur))
            cur, curlen = [w], len(w)
        else:
            cur.append(w)
            curlen += add
    if cur:
        lines.append(" ".join(cur))
    while len(lines) < nlines:
        lines.append("")
    return lines[:nlines]


def layout_latin(name, abbrev):
    """Return (lines, font_size, is_hero_abbrev) for a Latin-script name."""
    words = name.split()
    caps = {1: 30, 2: 24, 3: 18}
    best = None  # (font, lines, nlines)
    for nlines in (1, 2, 3):
        if nlines > len(words):
            break
        lines = balance_words(words, nlines)
        maxlen = max(len(l) for l in lines) or 1
        f = min(int(205 / (0.55 * maxlen)), caps[nlines])
        if best is None or f > best[0]:
            best = (f, lines, nlines)
    f, lines, _ = best
    if (f < 14 or name in ()) and abbrev:
        return [abbrev], 30, True
    return lines, max(f, 12), False


def split_cjk(name):
    """Strip a trailing parenthetical (kept out of the hero) -> main text."""
    m = re.match(r"^(.*?)[（(].*", name)
    return m.group(1) if m else name


def layout_cjk(name):
    """Return (lines, font_size) for a CJK hero name."""
    main = split_cjk(name)
    n = len(main)
    if n <= 5:
        return [main], min(44, int(205 / max(n, 1)))
    if n <= 10:
        half = math.ceil(n / 2)
        per = max(half, n - half)
        return [main[:half], main[half:]], min(40, int(200 / per))
    third = math.ceil(n / 3)
    return [main[:third], main[third:2 * third], main[2 * third:]], min(26, int(200 / third))


def hero_svg(lines, font, cjk):
    n = len(lines)
    gap = font * 1.2
    center = 162.0
    family = FONT_CJK if cjk else FONT_LATIN
    out = []
    for i, line in enumerate(lines):
        if not line:
            continue
        y = center + (i - (n - 1) / 2.0) * gap + font * 0.34
        out.append(
            f'<text x="120" y="{y:.1f}" text-anchor="middle" font-family="{family}" '
            f'font-size="{font}" font-weight="700" fill="#1a1a1a">{esc(line)}</text>'
        )
    return "\n".join(out)


def build_svg(color, banner, hero_lines, hero_font, cjk_hero, subtitle, pill, cjk_banner=False):
    bw = min(max(len(banner) * (10 if cjk_banner else 5), 46), 170)
    ux = round(120 - bw / 2, 1)
    bfam = FONT_CJK if cjk_banner else FONT_LATIN
    sub = ""
    if subtitle:
        sfam = FONT_CJK if any(ord(c) > 0x2e80 for c in subtitle) else FONT_LATIN
        # shrink very long subtitles so they stay on one line
        sf = 11 if len(subtitle) <= 30 else (10 if len(subtitle) <= 36 else 9)
        sub = (f'<text x="120" y="238" text-anchor="middle" font-family="{sfam}" '
               f'font-size="{sf}" fill="#6a6a6a">{esc(subtitle)}</text>')
    pfam = FONT_CJK if any(ord(c) > 0x2e80 for c in pill) else FONT_LATIN
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 320" width="240" height="320">
<rect width="240" height="320" fill="#ffffff"/>
<rect x="5" y="5" width="230" height="310" rx="13" fill="#ffffff" stroke="{color}" stroke-width="2"/>
<path d="M5,18 a13,13 0 0 1 13,-13 h204 a13,13 0 0 1 13,13 v60 h-230 z" fill="{color}"/>
<text x="120" y="35" text-anchor="middle" font-family="{bfam}" font-size="{8.5 if cjk_banner else 10.5}" letter-spacing="{1.5 if cjk_banner else 2.5}" font-weight="700" fill="#ffffff">{esc(banner)}</text>
<rect x="{ux}" y="45" width="{bw}" height="2" rx="1" fill="#ffffff" opacity="0.7"/>
<text x="120" y="63" text-anchor="middle" font-family="{FONT_LATIN}" font-size="8.5" letter-spacing="1.5" fill="#ffffff" opacity="0.8">JOURNAL · AGENT SKILLS</text>
{hero_svg(hero_lines, hero_font, cjk_hero)}
{sub}
<line x1="42" y1="276" x2="198" y2="276" stroke="{color}" stroke-width="1" opacity="0.3"/>
<rect x="78" y="285" width="84" height="22" rx="11" fill="{color}"/>
<text x="120" y="300" text-anchor="middle" font-family="{pfam}" font-size="11" font-weight="700" fill="#ffffff">{esc(pill)}</text>
</svg>
'''


def render_png(svg_path, png_path):
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "480", "-h", "640", "-o", png_path, svg_path], check=True)
    elif shutil.which("cairosvg"):
        subprocess.run(["cairosvg", svg_path, "-W", "480", "-H", "640", "-o", png_path], check=True)
    elif shutil.which("sips"):
        subprocess.run(["sips", "-s", "format", "png", "-z", "640", "480", svg_path, "--out", png_path],
                       check=True, stdout=subprocess.DEVNULL)
    else:
        raise SystemExit("Install rsvg-convert (librsvg), cairosvg, or run on macOS with sips.")


def read_name(bundle_dir, slug):
    p = os.path.join(ROOT, bundle_dir, "skills", slug, "SKILL.md")
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"^#\s+(.+)$", txt, re.M)
    head = m.group(1).strip()
    cn = re.search(r"《([^》]+)》", head)
    if cn:
        en = re.search(r"《[^》]+》\s*[（(]([A-Za-z][^)）]+)[)）]", txt)
        return cn.group(1), (en.group(1).strip() if en else None)
    return re.sub(r"\s*\([^)]*\)\s*$", "", head).strip(), None


# slug alias: a few existing covers use a shorter slug than the skill folder.
COVER_ALIAS = {
    "the-lancet": "lancet",
    "nejm": "nejm", "pnas": "pnas",
}

PLAN = [
    ("English-SocialScience-Journal-Skills", EN_SOC, "en", False),
    ("English-NaturalScience-Journal-Skills", EN_NAT, "en", False),
    ("Chinese-SocialScience-Journal-Skills", CN_SOC, "cn", True),
]


def main():
    force = "--force" in sys.argv
    list_only = "--list" in sys.argv
    os.makedirs(COVERS, exist_ok=True)
    existing = {f[:-4] for f in os.listdir(COVERS) if f.endswith(".png")}
    made = skipped = 0
    for bundle_dir, disc_map, lang, cjk in PLAN:
        print(f"\n== {bundle_dir} ==")
        for ckey, slugs in disc_map.items():
            for slug in slugs:
                cover_slug = COVER_ALIAS.get(slug, slug)
                if not force and cover_slug in existing:
                    skipped += 1
                    continue
                color = PALETTE[ckey]
                if lang == "cn":
                    cn_name, en_name = read_name(bundle_dir, slug)
                    banner = CN_BANNER.get(ckey, BANNER[ckey])
                    lines, font = layout_cjk(cn_name)
                    subtitle = en_name or ""
                    svg = build_svg(color, banner, lines, font, True, subtitle,
                                    "fit skill", cjk_banner=True)
                else:
                    en_name, _ = read_name(bundle_dir, slug)
                    banner = BANNER[ckey]
                    abbrev = ABBREV.get(slug)
                    if slug in HERO_ABBREV and abbrev:
                        lines, font, is_hero = [abbrev], 28, True
                    else:
                        lines, font, is_hero = layout_latin(en_name, abbrev)
                    subtitle = en_name if is_hero else (abbrev or "")
                    svg = build_svg(color, banner, lines, font, False, subtitle, "fit skill")
                if list_only:
                    print(f"  {cover_slug:52s} {ckey:8s} f{font}")
                    made += 1
                    continue
                svg_path = os.path.join(COVERS, f"{cover_slug}.svg")
                with open(svg_path, "w", encoding="utf-8") as fh:
                    fh.write(svg)
                render_png(svg_path, os.path.join(COVERS, f"{cover_slug}.png"))
                made += 1
        print(f"   running total: made={made} skipped={skipped}")
    print(f"\nDONE: {'planned' if list_only else 'rendered'} {made}, skipped {skipped} existing")


if __name__ == "__main__":
    main()
