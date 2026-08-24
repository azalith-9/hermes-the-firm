"""hermes-the-firm — the single front door.

/hermes-the-firm                    -> roster: departments + admin + library
/hermes-the-firm <area>             -> one practice department's skills
/hermes-the-firm firm-admin         -> firm AI administration layer
/hermes-the-firm louis              -> Louis library overview (47 categories)
/hermes-the-firm louis <category>   -> one Louis category's skills

Pure string handling: reads skills/ + references/owner-map.json off
disk, never mutates state, never raises past a caught error (a broken
listing must not break the session). Skill names are registered
plugin-skill bare names; every mention resolves via
skill_view("hermes-the-firm:<skill>").

Skills live FLAT under skills/ (Hermes registers one flat namespace).
Which area owns which flat skill is decided at port time and written to
references/owner-map.json — one source of truth, no guessing here. Owner values:
  - "<area>"            one of the twelve practice departments
  - "firm-admin"        HAQQ master pack (AI policy, governance)
  - "louis/<category>"  HAQQ mini library, per category
"""
import json
from pathlib import Path

# Practice departments = the upstream first-party plugins, roster order.
PRACTICE_AREAS = [
    "commercial-legal",
    "privacy-legal",
    "product-legal",
    "corporate-legal",
    "employment-legal",
    "litigation-legal",
    "regulatory-legal",
    "ai-governance-legal",
    "ip-legal",
    "law-student",
    "legal-clinic",
    "legal-builder-hub",
]

_HERE = Path(__file__).parent
_SKILLS_DIR = _HERE / "skills"
_OWNER_MAP_PATH = _HERE / "references" / "owner-map.json"


def _owner_map() -> dict:
    """flat skill name -> owner ("<area>", "firm-admin", or
    "louis/<category>"). Empty on missing/corrupt file — a broken map
    degrades the roster, never the session."""
    try:
        return json.loads(_OWNER_MAP_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _all_skills() -> list[str]:
    if not _SKILLS_DIR.is_dir():
        return []
    return sorted(d.name for d in _SKILLS_DIR.iterdir()
                  if (d / "SKILL.md").is_file())


def _skills_for(owner_prefix: str, owners: dict) -> list[str]:
    """Flat names whose owner is exactly owner_prefix (for departments/
    firm-admin) or starts with it (louis/<cat> drill-downs use exact)."""
    return sorted(n for n in _all_skills() if owners.get(n) == owner_prefix)


def _louis_categories(owners: dict) -> dict[str, int]:
    cats: dict[str, int] = {}
    for n, owner in owners.items():
        if owner.startswith("louis/"):
            cat = owner.split("/", 1)[1]
            cats[cat] = cats.get(cat, 0) + 1
    return dict(sorted(cats.items()))


def _short(area: str) -> str:
    # kept in sync with the port toolchain by test
    specials = {
        "ai-governance-legal": "aigov",
        "law-student": "lawstudent",
        "legal-clinic": "clinic",
        "legal-builder-hub": "builderhub",
    }
    return specials.get(area, area.replace("-legal", ""))


def _roster(owners: dict) -> str:
    total = len(_all_skills())
    lines = [
        "hermes-the-firm — a complete legal practice on Hermes.",
        "",
        f"  {total} skills across three layers:",
        "",
        "DEPARTMENTS (practice law; each has a cold-start interview)",
    ]
    for area in PRACTICE_AREAS:
        n = len(_skills_for(area, owners))
        lines.append(f"  {area:<24} {n:>3} skills")
    lines += [
        f"  firm-admin               {len(_skills_for('firm-admin', owners)):>3} skills"
        "   <- how the firm runs AI (policy, privilege, vendors)",
        "",
        "THE LOUIS LIBRARY (982 deep-knowledge skills, MENA-first lens)",
    ]
    cats = _louis_categories(owners)
    row = []
    for cat, n in cats.items():
        row.append(f"{cat}({n})")
        if len(row) == 6:
            lines.append("  " + "  ".join(f"{r:<14}" for r in row))
            row = []
    if row:
        lines.append("  " + "  ".join(f"{r:<14}" for r in row))
    lines += [
        "",
        "Drill in: /hermes-the-firm <area> | firm-admin | louis [category]",
        'Or load directly: skill_view("hermes-the-firm:<skill>").',
        "New to a department? Run its cold-start interview first — every",
        "skill there reads the practice profile it writes.",
    ]
    return "\n".join(lines)


def _louis_listing(owners: dict, category: str | None) -> str:
    cats = _louis_categories(owners)
    if not category:
        lines = [f"Louis library — {sum(cats.values())} skills, "
                 f"{len(cats)} categories:", ""]
        row = []
        for cat, n in cats.items():
            row.append(f"{cat}({n})")
            if len(row) == 6:
                lines.append("  " + "  ".join(f"{r:<16}" for r in row))
                row = []
        if row:
            lines.append("  " + "  ".join(f"{r:<16}" for r in row))
        lines += ["", "Drill in: /hermes-the-firm louis <category>"]
        return "\n".join(lines)

    prefix = f"louis/{category}"
    if category not in cats:
        known = ", ".join(cats)
        return f"unknown louis category {category!r}. categories:\n{known}"
    skills = _skills_for(prefix, owners)
    lines = [f"louis/{category} — {len(skills)} skills:", ""]
    for s in skills:
        lines.append(f'  skill_view("hermes-the-firm:{s}")')
    return "\n".join(lines)


def handle_entry(raw: str) -> str:
    try:
        arg = (raw or "").strip().lower().replace(" ", "-")
        owners = _owner_map()

        if not arg:
            return _roster(owners)

        # "louis" / "louis-<category>"
        if arg == "louis":
            return _louis_listing(owners, None)
        if arg.startswith("louis-"):
            return _louis_listing(owners, arg[len("louis-"):])

        if arg == "firm-admin":
            skills = _skills_for("firm-admin", owners)
            if not skills:
                return ("firm-admin is empty (master-claude-for-legal "
                        "not present at port time — see UPSTREAM.md)")
            lines = [
                "firm-admin — how the firm itself runs AI.", "",
                "Skills:",
            ]
            for s in skills:
                lines.append(f'  skill_view("hermes-the-firm:{s}")')
            lines += [
                "",
                "Reference library: references/firm-admin/*.md "
                "(privilege layers, MCP hardening, anti-patterns, ...)",
                "Governance templates: templates/firm-admin-*.md "
                "(firm AI policy, client data explainer, vendor security)",
            ]
            return "\n".join(lines)

        if arg in PRACTICE_AREAS:
            skills = _skills_for(arg, owners)
            if not skills:
                return (f"{arg} has no skills installed "
                        f"(conversion gap — see UPSTREAM.md)")
            interview = f"{_short(arg)}-cold-start-interview"
            lines = [f"{arg} — {len(skills)} skills:", ""]
            for s in skills:
                marker = "   <- START HERE" if s == interview else ""
                lines.append(
                    f'  skill_view("hermes-the-firm:{s}"){marker}')
            lines += [
                "",
                "Run the interview first if this department is new —",
                "every other skill reads the practice profile it writes.",
            ]
            return "\n".join(lines)

        known = ", ".join(PRACTICE_AREAS + ["firm-admin", "louis"])
        return (f"unknown area {raw.strip()!r}. areas:\n{known}\n"
                f"(or: louis <category>)")
    except Exception as e:  # never break the session over a listing
        return f"hermes-the-firm error: {e}"
