#!/usr/bin/env python3
"""Per-pack quality scorecard for Awesome Journal Skills.

Objective, dependency-free measurement of every first-party skill pack, so the
maintenance team can SEE where work pays off instead of guessing. Complements
tools/audit_repo.py (pass/fail repository invariants) and tools/clone_audit.py
(similarity).

Two outputs, because they answer different questions
----------------------------------------------------
**Conformance** — does this pack meet the structural requirements every pack is
expected to meet? Both READMEs, a resources README, a source anchor, worked
examples, exemplars, a code library or a stated reason there is none, a skill
count inside its role's band, and every skill description saying *when* to use
it and naming its venue. This is pass/fail and it is the gate.

**Backlog score (0-100)** — of the work that is *not* uniform across packs, how
much of it is done here? Higher means less left to do.

Why they were split
-------------------
The old scorecard folded both into one number, and by August 2026 that number had
stopped measuring anything: five of its six dimensions sat at maximum for 299 of
299 packs, so the score was arithmetically ``94 + freshness(0-6)`` and reported a
mean of 99.2/100. Nothing was wrong with the dimensions — the packs had simply all
met them, which is the success case for a requirement and the failure case for a
metric. A requirement everyone satisfies belongs in a gate; only what still varies
can rank anything.

So the requirements moved to ``conformance`` (still enforced, now as pass/fail),
and the score is computed from the dimensions that still have spread. The tool
reports its own saturation at the bottom of the table, so the next dimension to
retire is visible before it flatlines rather than years after.

Usage:
  python3 tools/quality_scorecard.py                  # full table, worst first
  python3 tools/quality_scorecard.py --top 20         # 20 packs with the most left to do
  python3 tools/quality_scorecard.py --top 5 --show-skills
  python3 tools/quality_scorecard.py --json           # machine-readable
  python3 tools/quality_scorecard.py --require-conformance   # exit 1 on any failure
  python3 tools/quality_scorecard.py --min-score 40   # exit 1 if any pack scores below

The ``unit`` column is a cross-language substance measure: Latin/technical
tokens count as one unit, and two CJK characters count as one unit.
"""

from __future__ import annotations

import argparse
from collections import Counter
import datetime as dt
import json
import re
import sys
from pathlib import Path

from freshness_audit import last_verified

ROOT = Path(__file__).resolve().parents[1]

# External third-party imports are out of scope: we don't own their content.
IMPORTED_ROOTS = {
    "AER-Skills",
    "AER-skills",
    "Nature-Skills",
    "nature-skills",
    "nature-paper-skills",
    "claude-scholar",
    "codex-claude-academic-skills",
}

CONFERENCE_DEPTH_PACKS = {
    "AAAI-Skills",
    "AAMAS-Skills",
    "ACL-Skills",
    "ACM-CCS-Skills",
    "ACM-MM-Skills",
    "AISTATS-Skills",
    "ASE-Skills",
    "ASPLOS-Skills",
    "ATC-Skills",
    "CAV-Skills",
    "CHI-Skills",
    "CIKM-Skills",
    "COLM-Skills",
    "COLT-Skills",
    "CoNEXT-Skills",
    "CoRL-Skills",
    "CSCW-Skills",
    "CVPR-Skills",
    "DAC-Skills",
    "EACL-Skills",
    "ECAI-Skills",
    "ECCV-Skills",
    "EDBT-Skills",
    "EMNLP-Skills",
    "EuroSys-Skills",
    "FAccT-Skills",
    "FAST-Skills",
    "FOCS-Skills",
    "FSE-Skills",
    "HPCA-Skills",
    "HRI-Skills",
    "ICALP-Skills",
    "ICASSP-Skills",
    "ICCV-Skills",
    "ICDE-Skills",
    "ICDM-Skills",
    "ICDT-Skills",
    "ICLR-Skills",
    "ICML-Skills",
    "ICRA-Skills",
    "ICSE-Skills",
    "ICSME-Skills",
    "IEEE-SP-Skills",
    "IJCAI-Skills",
    "IMC-Skills",
    "INFOCOM-Skills",
    "INTERSPEECH-Skills",
    "IPSN-Skills",
    "IROS-Skills",
    "ISCA-Skills",
    "ISSTA-Skills",
    "ITCS-Skills",
    "KDD-Skills",
    "MICRO-Skills",
    "MLSys-Skills",
    "MobiCom-Skills",
    "MobiSys-Skills",
    "NAACL-Skills",
    "NDSS-Skills",
    "NeurIPS-Skills",
    "NSDI-Skills",
    "OOPSLA-Skills",
    "OSDI-Skills",
    "PerCom-Skills",
    "PLDI-Skills",
    "PODC-Skills",
    "PODS-Skills",
    "POPL-Skills",
    "PPoPP-Skills",
    "RecSys-Skills",
    "RSS-Skills",
    "SenSys-Skills",
    "SIGCOMM-Skills",
    "SIGGRAPH-Skills",
    "SIGIR-Skills",
    "SIGMETRICS-Skills",
    "SIGMOD-Skills",
    "SoCC-Skills",
    "SODA-Skills",
    "SOSP-Skills",
    "STOC-Skills",
    "TACAS-Skills",
    "The-Web-Conference-Skills",
    "UAI-Skills",
    "UIST-Skills",
    "USENIX-Security-Skills",
    "VIS-Skills",
    "VLDB-Skills",
    "WACV-Skills",
    "WSDM-Skills",
}

TOOLKIT_PACKS = {
    "Research-Toolkit-Skills",
}

# --- backlog-score weights ---------------------------------------------------------
# Chosen against the observed spread of each signal across the 299 packs, so that the
# ranking separates packs rather than clustering them. They are weights on remaining
# work, not a claim about what fraction of quality each dimension is.
CURRENCY_WEIGHT = 30      # how recently the source map was re-read
VERIFIED_WEIGHT = 25      # how many facts it still flags as unconfirmed
FLOOR_WEIGHT = 25         # how deep the pack's *thinnest* skill is
EVENNESS_WEIGHT = 10      # how far the thinnest skill sits below the pack's own average
WIRING_WEIGHT = 10        # how much of the pack reaches the execution layer

# Publishers change fees, editors and policies on their own schedule. Sixty days is the
# repository's working definition of "recently re-read"; a year is the hard gate in
# tools/freshness_audit.py, and a pack at that edge has no currency credit left.
CURRENCY_BANDS = ((30, 30), (60, 24), (90, 18), (180, 10), (365, 4), (10**6, 0))
# Ten unresolved flags is where the credit runs out. The repository's p90 is 7.
UNRESOLVED_ZERO_AT = 10
# Full wiring credit once a quarter of a pack's skills reach the execution bridge:
# the bridge belongs in the empirical skills, not in every skill of the lifecycle.
WIRING_TARGET_SHARE = 0.25
# Descriptions below this are too thin to route on. Every pack clears it today, which
# is why it is a conformance requirement rather than a scored dimension.
MIN_AVG_DESC_CHARS = 200

FRONTMATTER_DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_+./-]*")
CJK_RE = re.compile(r"[\u3400-\u9fff]")
NO_CODE_MARKERS = (
    "no econometric",
    "why no econometrics code",
    "why no econometric",
    "does not vendor",
    "not vendor",
    "not vendored",
    "no code kit",
    "no `code/`",
    "no vendored econometrics",
    "not an economics venue",
    "not a generic causal-inference",
    "theory venue",
    "multidisciplinary",
    "clinical",
    "humanities",
    "theorem",
    "proof architecture",
)

USE_WHEN_MARKERS = (
    "use when",
    "use this",
    "use after",
    "use before",
    "use if",
    "use for",
    "use as",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def first_party_packs() -> list[Path]:
    packs = []
    for plugin in sorted(ROOT.glob("*/.claude-plugin/plugin.json")):
        pack = plugin.parent.parent
        if pack.name in IMPORTED_ROOTS:
            continue
        if (pack / "skills").is_dir():
            packs.append(pack)
    return packs


def skill_files(pack: Path) -> list[Path]:
    return sorted((pack / "skills").glob("*/SKILL.md"))


def body_after_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :]
    return text


def substance_units(text: str) -> float:
    r"""Approximate body substance across English and CJK prose.

    Whitespace word counts severely undercount Chinese skills, where a dense
    paragraph can be a single ``\S+`` token. Count Latin/technical tokens as
    words and count two CJK characters as roughly one English word-equivalent.
    """
    latin_tokens = len(LATIN_TOKEN_RE.findall(text))
    cjk_units = len(CJK_RE.findall(text)) / 2
    return latin_tokens + cjk_units


def pack_cue_words(pack: Path, skills: list[Path] | None = None) -> set[str]:
    words = [w for w in pack.name.replace("-Skills", "").replace("-", " ").lower().split() if len(w) > 2]
    # >=3 so short-but-real venue tokens count (e.g. "acm" in "ACM MM"): a
    # multi-word acronym name whose glued skill prefix ("acmmm") never appears in
    # the spaced prose form must still get journal-cue credit for naming its venue.
    cue_words = {w for w in words if len(w) >= 3}
    acronym = "".join(w[0] for w in words if w not in {"and", "the", "of"})
    if len(acronym) >= 3:
        cue_words.add(acronym)
    if skills:
        prefixes = [
            sf.parent.name.split("-", 1)[0].lower()
            for sf in skills
            if "-" in sf.parent.name and 3 <= len(sf.parent.name.split("-", 1)[0]) <= 8
        ]
        for prefix, count in Counter(prefixes).items():
            if count >= max(2, len(skills) // 2):
                cue_words.add(prefix)
    return cue_words


def score_pack(pack: Path) -> dict:
    skills = skill_files(pack)
    n = len(skills)
    is_toolkit = pack.name in TOOLKIT_PACKS or pack.name.endswith("Toolkit-Skills")
    # Breadth bundles are venue-fit-card collections (one fit card per venue + a
    # router), so their capability layer is routing, not a depth-pack code library.
    # Two signals mark a breadth bundle, either of which is sufficient:
    #   1. Size: single-venue depth packs top out at ~18 skills, while most breadth
    #      bundles run from the low-30s up to 150+; a threshold of 25 sits cleanly
    #      between the two.
    #   2. A router skill named "*-journal-workflow". This is the canonical breadth
    #      router across all eight breadth bundles and never appears in a depth pack,
    #      so it correctly recognises a small focused breadth bundle (e.g. the
    #      12-journal sport-science bundle) that the size cutoff alone would miss.
    # Either signal avoids penalising a genuine breadth bundle for "missing" a
    # depth-pack code library it is not meant to ship.
    has_breadth_router = any(
        sf.parent.name.endswith("-journal-workflow") for sf in skills
    )
    is_breadth = not is_toolkit and (n >= 25 or has_breadth_router)
    is_conference_depth = pack.name in CONFERENCE_DEPTH_PACKS

    line_counts: list[int] = []
    unit_counts: list[float] = []
    desc_lengths: list[int] = []
    desc_use_when = 0
    desc_has_journal_cue = 0
    code_block_skills = 0
    exec_bridge_skills = 0
    shared_resource_skills = 0
    skill_rows: list[dict] = []

    pack_words = pack_cue_words(pack, skills)
    if is_toolkit:
        pack_words.update(
            {
                "execution",
                "journal",
                "manuscript",
                "readiness",
                "referee",
                "replication",
                "submission",
                "toolkit",
                "venue",
                "workflow",
            }
        )

    for sf in skills:
        text = sf.read_text(encoding="utf-8", errors="replace")
        body = body_after_frontmatter(text)
        line_count = body.count("\n") + 1
        unit_count = substance_units(body)
        line_counts.append(line_count)
        unit_counts.append(unit_count)
        has_code_block = "```" in body
        if "```" in body:
            code_block_skills += 1
        # Execution-bridge signal: does the skill wire guidance to the StatsPAI /
        # Stata MCP execution layer (links the shared execution-with-mcp playbook)?
        # Report-only — tracks the guidance→execution rollout; does not affect score.
        if "execution-with-mcp" in body:
            exec_bridge_skills += 1
        if "shared-resources/" in body:
            shared_resource_skills += 1
        desc = ""
        desc_len = 0
        has_use_when = False
        has_journal_cue = False
        m = FRONTMATTER_DESCRIPTION_RE.search(text)
        if m:
            desc = m.group(1).strip()
            desc_len = len(desc)
            desc_lengths.append(len(desc))
            low = desc.lower()
            if (
                any(marker in low for marker in USE_WHEN_MARKERS)
                or low.startswith("use to ")
                or "用于" in low
                or "当" in low
            ):
                desc_use_when += 1
                has_use_when = True
            # journal-specificity cue: the description names (part of) the venue
            if any(w in low for w in pack_words):
                desc_has_journal_cue += 1
                has_journal_cue = True
        skill_rows.append(
            {
                "path": rel(sf),
                "substance_units": round(unit_count),
                "lines": line_count,
                "desc_chars": desc_len,
                "desc_use_when": has_use_when,
                "desc_journal_cue": has_journal_cue,
                "code_block": has_code_block,
            }
        )

    res = pack / "resources"
    has_code = (res / "code").is_dir()
    has_worked = (res / "worked-examples").is_dir()
    has_exemplars = (res / "exemplars").is_dir()
    has_resources_readme = (res / "README.md").exists()
    has_source_map = (res / "official-source-map.md").exists()
    has_external = (res / "external_tools.md").exists()
    source_map_text = ""
    if has_source_map:
        source_map_text = (res / "official-source-map.md").read_text(
            encoding="utf-8", errors="replace"
        )
    resources_readme_text = ""
    if has_resources_readme:
        resources_readme_text = (res / "README.md").read_text(encoding="utf-8", errors="replace").lower()
        resources_readme_text = re.sub(r"[*_`]", "", resources_readme_text)
    no_code_explained = bool(resources_readme_text) and any(marker in resources_readme_text for marker in NO_CODE_MARKERS)
    has_roster = any((res / name).exists() for name in ("conference-roster.md", "journal-roster.md", "source-basis.md"))
    has_readme = (pack / "README.md").exists()
    has_readme_zh = (pack / "README.zh-CN.md").exists()
    has_router = any("workflow" in sf.parent.name or "router" in sf.parent.name for sf in skills)

    avg_units = sum(unit_counts) / n if n else 0
    avg_desc = sum(desc_lengths) / len(desc_lengths) if desc_lengths else 0

    # ---- composite score (0-100) ----
    # Depth: SKILL bodies that actually carry substance. Journal depth packs are
    # scored against a flagship ~600 unit/skill target. Large breadth bundles,
    # toolkit packs, and compressed AI-conference depth packs have shorter,
    # routing-heavy profiles, so they use smaller targets tied to that role.
    depth_target = 300 if is_toolkit else (350 if is_breadth or is_conference_depth else 600)
    depth = min(35, (avg_units / depth_target) * 35)
    # Trigger precision: descriptions that say WHEN and name the venue.
    trigger = 0.0
    if n:
        trigger += min(8, (avg_desc / 200) * 8)
        trigger += (desc_use_when / n) * 4
        trigger += (desc_has_journal_cue / n) * 8
    # Resources / capability assets. Breadth bundles should not be penalized for
    # lacking a depth-pack code library; their capability layer is routing,
    # roster/source discipline, worked routing examples, and selection patterns.
    if is_toolkit:
        shared_coverage = (shared_resource_skills / n) if n else 0
        resources = (
            (6 if has_resources_readme else 0)
            + min(8, shared_coverage * 8)
            + (5 if has_router else 0)
            + (5 if exec_bridge_skills else 0)
            + (4 if no_code_explained else 0)
        )
    elif is_breadth:
        resources = (
            (6 if has_resources_readme else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (5 if has_source_map else 0)
            + (3 if has_roster else 0)
        )
    else:
        source_anchor = has_source_map or has_external
        resources = (
            (10 if has_code or no_code_explained else 0)
            + (8 if has_worked else 0)
            + (6 if has_exemplars else 0)
            + (3 if source_anchor else 0)
            + (1 if has_resources_readme else 0)
        )
    # Runnable code inside skill bodies (empirical capability signal).
    runnable = min(5, (code_block_skills / n) * 5) if n else 0
    # Structure hygiene. The full-credit bands describe "size fits the pack's
    # role", not an absolute scale: a breadth bundle earns structure credit by
    # shipping its canonical router plus a genuine roster (>= 12 venue cards
    # guards against stubs — the classifier itself accepts small focused
    # bundles, so structure must not re-penalise them for size), and a depth
    # pack earns it by staying within the 8-20 lifecycle band (8 guards
    # against stubs; 20 guards against unfocused sprawl while admitting
    # deliberately deepened flagships such as the 18-skill ERJ pack).
    structure = 0.0
    if is_toolkit:
        # The upper bound is a sprawl guard, not a cap on the lifecycle. It was 10 —
        # the toolkit's size at the time plus one — so the first genuine additions to
        # the loop (ladder pricing, venue verification) read as sprawl. 14 keeps the
        # guard meaningful while leaving room for the loop to grow the way it has.
        structure += 3 if 5 <= n <= 14 and has_router else (1 if n else 0)
    elif is_breadth:
        structure += 3 if n >= 12 and has_router else (1 if n else 0)
    else:
        structure += 3 if 8 <= n <= 20 else (1 if n else 0)
    structure += 1.5 if has_readme else 0
    structure += 1.5 if has_readme_zh else 0

    # Source quality and freshness provide the final six points. The previous
    # formula topped out at 94, causing every conforming pack to receive the same
    # nominal "94/100" and hiding the maintenance backlog.
    unresolved_count = len(re.findall(r"待核实|UNVERIFIED", source_map_text, re.I))
    verified_date, _ = last_verified(source_map_text, dt.date.today()) if source_map_text else (None, "none")
    if is_toolkit:
        evidence = 6.0  # cross-journal toolkit has no venue-specific volatile facts
    elif verified_date:
        age_days = (dt.date.today() - verified_date).days
        freshness_points = 6 if age_days <= 60 else (5 if age_days <= 120 else (3 if age_days <= 365 else 0))
        evidence = max(0.0, freshness_points - min(2.0, unresolved_count * 0.1))
    else:
        evidence = 0.0

    # ---- conformance: the requirements every pack is expected to meet ----
    # These are the dimensions above, re-expressed as pass/fail. They were worth 94 of
    # the old 100 points and every pack earned all 94, which is what a requirement
    # looks like once it has been met — not a differentiator.
    failures: list[str] = []
    if not has_readme:
        failures.append("no README.md")
    if not has_readme_zh:
        failures.append("no README.zh-CN.md")
    if not has_resources_readme:
        failures.append("no resources/README.md")
    if not is_toolkit and not (has_source_map or has_external):
        failures.append("no source anchor (official-source-map.md or external_tools.md)")
    if not is_toolkit:
        if not has_worked:
            failures.append("no resources/worked-examples/")
        if not is_breadth and not has_exemplars:
            failures.append("no resources/exemplars/")
        if not is_breadth and not (has_code or no_code_explained):
            failures.append("no resources/code/ and no stated reason for its absence")
    if is_breadth and not has_roster:
        failures.append("breadth bundle without a roster or source basis")
    if (is_breadth or is_toolkit) and not has_router:
        failures.append("no router skill")
    if is_toolkit:
        if not 5 <= n <= 14:
            failures.append(f"{n} skills, outside the 5-14 toolkit band")
    elif is_breadth:
        if n < 12:
            failures.append(f"{n} venue cards, below the 12-card floor")
    elif not 8 <= n <= 20:
        failures.append(f"{n} skills, outside the 8-20 lifecycle band")
    if n and desc_use_when < n:
        failures.append(f"{n - desc_use_when} description(s) do not say when to use the skill")
    if n and desc_has_journal_cue < n:
        failures.append(f"{n - desc_has_journal_cue} description(s) do not name the venue")
    if n and code_block_skills < n:
        failures.append(f"{n - code_block_skills} skill(s) carry no worked block")
    if avg_desc < MIN_AVG_DESC_CHARS:
        failures.append(f"average description {avg_desc:.0f} chars, below {MIN_AVG_DESC_CHARS}")

    # ---- backlog score (0-100): only dimensions that still vary across packs ----
    min_units = min(unit_counts) if unit_counts else 0
    # The *thinnest* skill, not the average. The average is the statistic that
    # saturated, and it is also the one that hides a soft spot: a pack of eleven
    # 900-unit skills and one 250-unit skill averages comfortably above target.
    floor_points = min(FLOOR_WEIGHT, (min_units / depth_target) * FLOOR_WEIGHT)
    # Evenness asks the same question relatively: is the weakest file weak *for this
    # pack*? The observed range across the repository is 0.50 to 0.95.
    evenness_ratio = (min_units / avg_units) if avg_units else 0.0
    evenness_points = max(0.0, min(EVENNESS_WEIGHT,
                                   (evenness_ratio - 0.5) / 0.45 * EVENNESS_WEIGHT))
    if is_toolkit:
        currency_points = float(CURRENCY_WEIGHT)   # no venue-specific volatile facts
    elif verified_date:
        age_days = (dt.date.today() - verified_date).days
        currency_points = float(next(
            points for limit, points in CURRENCY_BANDS if age_days <= limit))
    else:
        currency_points = 0.0
    # Every 待核实 / UNVERIFIED marker is a fact the pack itself says it could not
    # confirm. Repository-wide this is the largest live backlog, and unlike freshness
    # it does not decay on its own — someone has to go and check.
    verified_points = VERIFIED_WEIGHT * max(0.0, 1 - unresolved_count / UNRESOLVED_ZERO_AT)
    # Execution wiring only applies where there is econometric code to wire.
    wiring_applies = has_code and not is_breadth
    if wiring_applies and n:
        wiring_points = min(WIRING_WEIGHT,
                            (exec_bridge_skills / n) / WIRING_TARGET_SHARE * WIRING_WEIGHT)
    else:
        wiring_points = 0.0

    earned = floor_points + evenness_points + currency_points + verified_points
    available = FLOOR_WEIGHT + EVENNESS_WEIGHT + CURRENCY_WEIGHT + VERIFIED_WEIGHT
    if wiring_applies:
        earned += wiring_points
        available += WIRING_WEIGHT
    # A pack with nothing to wire is not penalised for not having wired it: the
    # dimension leaves the denominator instead of scoring zero.
    total = round(100 * earned / available, 1)
    weak_skills = sorted(
        skill_rows,
        key=lambda row: (
            row["substance_units"],
            0 if row["desc_use_when"] else -1,
            0 if row["desc_journal_cue"] else -1,
            row["path"],
        ),
    )[:5]

    return {
        "pack": pack.name,
        "pack_type": "toolkit"
        if is_toolkit
        else ("breadth" if is_breadth else ("conference" if is_conference_depth else "depth")),
        "skills": n,
        "avg_words": round(avg_units),
        "avg_substance_units": round(avg_units),
        "avg_desc_chars": round(avg_desc),
        "desc_use_when": desc_use_when,
        "desc_journal_cue": desc_has_journal_cue,
        "code_lib": has_code,
        "code_status": "not_applicable"
        if is_breadth or is_toolkit
        else ("present" if has_code else ("not_applicable" if no_code_explained else "missing")),
        "worked_examples": has_worked,
        "exemplars": has_exemplars,
        "source_map": has_source_map,
        "source_last_verified": verified_date.isoformat() if verified_date else None,
        "unresolved_flags": unresolved_count,
        "exec_bridge": exec_bridge_skills > 0,
        "exec_bridge_skills": exec_bridge_skills,
        "score": total,
        "conforms": not failures,
        "conformance_failures": failures,
        "min_substance_units": round(min_units),
        "weak_skills": weak_skills,
        "_breakdown": {
            "currency": round(currency_points, 1),
            "verified": round(verified_points, 1),
            "floor": round(floor_points, 1),
            "evenness": round(evenness_points, 1),
            "wiring": round(wiring_points, 1) if wiring_applies else None,
            "depth_target": depth_target,
        },
        # The retired requirement dimensions, kept so the saturation report at the
        # bottom of the table can show when the next one is ready to be retired too.
        "_conformance_points": {
            "depth": round(depth, 1),
            "trigger": round(trigger, 1),
            "resources": resources,
            "runnable": round(runnable, 1),
            "structure": round(structure, 1),
        },
    }


SATURATION_NOTE = (
    "A dimension every pack maxes out has stopped ranking anything. When one of the "
    "rows below reaches 299/299, move it out of the score and into conformance."
)


def saturation_report(rows: list[dict]) -> list[str]:
    """How close each scored dimension is to measuring nothing.

    The previous scorecard died of this silently: its dimensions saturated one by one
    until the score was a freshness clock in a quality costume, and nothing in the
    output said so. This does.
    """
    lines = []
    ceilings = {
        "currency": CURRENCY_WEIGHT,
        "verified": VERIFIED_WEIGHT,
        "floor": FLOOR_WEIGHT,
        "evenness": EVENNESS_WEIGHT,
        "wiring": WIRING_WEIGHT,
    }
    for name, ceiling in ceilings.items():
        scored = [r["_breakdown"][name] for r in rows if r["_breakdown"][name] is not None]
        if not scored:
            continue
        at_ceiling = sum(1 for value in scored if value >= ceiling - 0.05)
        spread = max(scored) - min(scored)
        lines.append(f"  {name:<9} {at_ceiling:>3}/{len(scored)} at ceiling · "
                     f"spread {spread:.1f} of {ceiling}")
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--top", type=int, default=0,
                    help="show only the N packs with the most work left")
    ap.add_argument(
        "--show-skills",
        action="store_true",
        help="under each displayed pack, show its thinnest SKILL.md files",
    )
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--require-conformance", action="store_true",
                    help="exit 1 if any pack fails a structural requirement")
    ap.add_argument("--min-score", type=float, default=None,
                    help="exit 1 if any pack's backlog score is below this")
    args = ap.parse_args()

    rows = sorted((score_pack(p) for p in first_party_packs()), key=lambda r: r["score"])
    failing = [r for r in rows if not r["conforms"]]

    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        shown = rows[: args.top] if args.top else rows
        scores = [r["score"] for r in rows]
        mean = sum(scores) / len(scores) if scores else 0
        p10 = scores[int((len(scores) - 1) * 0.10)] if scores else 0
        median = scores[len(scores) // 2] if scores else 0
        # Execution-bridge rollout: only packs that ship a code library are candidates
        # for wiring; breadth bundles and theory venues are not.
        empirical = [r for r in rows if r["_breakdown"]["wiring"] is not None]
        wired = [r for r in empirical if r["exec_bridge"]]
        print(f"Quality scorecard — {len(rows)} first-party packs")
        if failing:
            print(f"Conformance: {len(rows) - len(failing)}/{len(rows)} packs meet every "
                  f"structural requirement · {len(failing)} FAIL")
        else:
            print(f"Conformance: {len(rows)}/{len(rows)} packs meet every structural "
                  "requirement")
        print(f"Backlog score: mean {mean:.1f}/100 · min {scores[0]:.1f} · "
              f"p10 {p10:.1f} · median {median:.1f} · max {scores[-1]:.1f}")
        pct = (len(wired) / len(empirical) * 100) if empirical else 0
        print(
            f"Execution bridge (StatsPAI/Stata MCP) wired: {len(wired)}/{len(empirical)} "
            f"packs with a code library ({pct:.0f}%)"
        )
        print(f"(most work left first){' · showing bottom ' + str(args.top) if args.top else ''}\n")
        hdr = (f"{'score':>5}  {'cur':>3} {'ver':>3} {'flr':>3} {'evn':>3} {'wir':>3}  "
               f"{'type':>10} {'skl':>3} {'thin':>5} {'unit':>5} {'flags':>5}  pack")
        print(hdr)
        print("-" * len(hdr))
        for r in shown:
            b = r["_breakdown"]
            wiring = f"{b['wiring']:.0f}" if b["wiring"] is not None else "n/a"
            print(
                f"{r['score']:>5}  {b['currency']:>3.0f} {b['verified']:>3.0f} "
                f"{b['floor']:>3.0f} {b['evenness']:>3.0f} {wiring:>3}  "
                f"{r['pack_type']:>10} {r['skills']:>3} {r['min_substance_units']:>5} "
                f"{r['avg_words']:>5} {r['unresolved_flags']:>5}  {r['pack']}"
            )
            for failure in r["conformance_failures"]:
                print(f"        ! {failure}")
            if args.show_skills:
                for skill in r["weak_skills"]:
                    cue = []
                    if not skill["desc_use_when"]:
                        cue.append("no-use-when")
                    if not skill["desc_journal_cue"]:
                        cue.append("no-journal-cue")
                    cue_text = f" [{', '.join(cue)}]" if cue else ""
                    print(
                        f"        - {skill['substance_units']:>4}u/{skill['desc_chars']:>3}d "
                        f"{skill['path']}{cue_text}"
                    )
        print("\nDimension saturation (cur/ver/flr/evn/wir above):")
        for line in saturation_report(rows):
            print(line)
        print(f"  {SATURATION_NOTE}")

    if args.require_conformance and failing:
        print(f"\n{len(failing)} pack(s) fail a structural requirement", file=sys.stderr)
        return 1
    if args.min_score is not None:
        below = [r for r in rows if r["score"] < args.min_score]
        if below:
            print(f"\n{len(below)} pack(s) below min-score {args.min_score}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
