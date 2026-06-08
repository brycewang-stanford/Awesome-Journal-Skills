#!/usr/bin/env python3
"""Generate uniform cover cards for the humanities / broader-social-science and
environment / agriculture depth packs.

Reuses the exact 240x320 card template from gen_covers.py (same look as the
natural-science depth cards and English flagship cards) so the new packs blend
into the existing cover walls. Run explicitly; it never touches the breadth or
flagship covers that other galleries depend on.

  python3 assets/gen_new_pack_covers.py            # render the new-pack cards
  python3 assets/gen_new_pack_covers.py --emit-md  # also print README gallery HTML

ES&T already ships a cover via the natural-science breadth bundle, so it is not
re-rendered here (the env gallery reuses that existing asset).
"""
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("gc", os.path.join(ROOT, "assets", "gen_covers.py"))
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)

# Discipline-cluster palette (dark enough for white header text + pill).
PALETTE = {
    "socio":  "#6a2c70",  # sociology / criminology / demography / family — plum
    "polsci": "#11507a",  # political science / IR / public opinion — steel blue
    "psych":  "#2a7a8c",  # psychology — teal
    "commedu": "#8a5a17",  # communication / education — amber
    "human":  "#6e1423",  # history / art / philosophy / literature / religion — burgundy
    "env":    "#2f6b3a",  # environment / ecology / agriculture — forest green
}

# slug, color-key, banner, [name lines], big font-size, subtitle (abbr), pill
HUMANITIES = [
    ("american-sociological-review",        "socio",  "SOCIOLOGY",        ["American", "Sociological Review"], 19, "ASR", "12 skills"),
    ("american-journal-of-sociology",       "socio",  "SOCIOLOGY",        ["American Journal", "of Sociology"], 19, "AJS", "12 skills"),
    ("social-forces",                       "socio",  "SOCIOLOGY",        ["Social Forces"],                  26, "Soc. Forces", "12 skills"),
    ("social-psychology-quarterly",         "socio",  "SOCIAL PSYCHOLOGY", ["Social Psychology", "Quarterly"], 18, "SPQ", "12 skills"),
    ("journal-of-marriage-and-family",      "socio",  "FAMILY STUDIES",   ["Journal of Marriage", "and Family"], 16, "JMF", "12 skills"),
    ("criminology",                         "socio",  "CRIMINOLOGY",      ["Criminology"],                    24, "Criminology", "12 skills"),
    ("demography",                          "socio",  "DEMOGRAPHY",       ["Demography"],                     26, "Demography", "12 skills"),
    ("american-political-science-review",   "polsci", "POLITICAL SCIENCE", ["American Political", "Science Review"], 17, "APSR", "12 skills"),
    ("american-journal-of-political-science","polsci","POLITICAL SCIENCE", ["American J. of", "Political Science"], 18, "AJPS", "12 skills"),
    ("journal-of-politics",                 "polsci", "POLITICAL SCIENCE", ["The Journal", "of Politics"],     22, "JOP", "12 skills"),
    ("world-politics",                      "polsci", "INTL RELATIONS",   ["World Politics"],                 24, "World Pol.", "12 skills"),
    ("international-organization",          "polsci", "INTL RELATIONS",   ["International", "Organization"],   21, "IO", "12 skills"),
    ("journal-of-personality-and-social-psychology", "psych", "PSYCHOLOGY", ["J. Personality &", "Social Psychology"], 17, "JPSP", "12 skills"),
    ("psychological-bulletin",              "psych",  "PSYCHOLOGY",       ["Psychological", "Bulletin"],       21, "Psych Bull.", "12 skills"),
    ("psychological-science",               "psych",  "PSYCHOLOGY",       ["Psychological", "Science"],        21, "Psych Sci.", "12 skills"),
    ("journal-of-communication",            "commedu", "COMMUNICATION",   ["Journal of", "Communication"],     21, "J. Comm.", "12 skills"),
    ("public-opinion-quarterly",            "polsci", "PUBLIC OPINION",   ["Public Opinion", "Quarterly"],     20, "POQ", "12 skills"),
    ("american-educational-research-journal","commedu","EDUCATION",       ["American Educ.", "Research Journal"], 18, "AERJ", "12 skills"),
    ("american-historical-review",          "human",  "HISTORY",          ["The American", "Historical Review"], 18, "AHR", "12 skills"),
    ("the-art-bulletin",                    "human",  "ART HISTORY",      ["The Art", "Bulletin"],             26, "Art Bull.", "12 skills"),
    ("mind",                                "human",  "PHILOSOPHY",       ["Mind"],                           46, "Founded 1876", "12 skills"),
    ("pmla",                                "human",  "LITERATURE",       ["PMLA"],                           44, "MLA", "12 skills"),
    ("critical-inquiry",                    "human",  "CRITICAL THEORY",  ["Critical", "Inquiry"],             26, "Crit. Inq.", "12 skills"),
    ("journal-of-the-american-academy-of-religion", "human", "RELIGION",  ["J. Am. Academy", "of Religion"],   17, "JAAR", "12 skills"),
]

# ES&T omitted on purpose (already covered by the natural-science breadth bundle).
ENVIRONMENT = [
    ("conservation-biology",        "env", "CONSERVATION",  ["Conservation", "Biology"],       21, "Cons. Biol.", "12 skills"),
    ("global-change-biology",       "env", "GLOBAL CHANGE", ["Global Change", "Biology"],      20, "GCB", "12 skills"),
    ("global-environmental-change", "env", "ENVIRONMENT",   ["Global Environ.", "Change"],     19, "GEC", "12 skills"),
    ("agricultural-systems",        "env", "AGRICULTURE",   ["Agricultural", "Systems"],       21, "Agric. Syst.", "12 skills"),
    ("field-crops-research",        "env", "AGRICULTURE",   ["Field Crops", "Research"],        21, "Field Crops", "12 skills"),
]

ALL = HUMANITIES + ENVIRONMENT


def render():
    for slug, ckey, banner, lines, bigsize, subtitle, pill in ALL:
        svg = gc.build_card_svg(PALETTE[ckey], banner, lines, bigsize, subtitle, pill)
        gc.write_card(slug, svg)
        print(f"  {slug}: {banner} ({subtitle})")


if __name__ == "__main__":
    print("New depth-pack cover cards:")
    render()
    print(f"done — {len(ALL)} cards")
