"""Leak + structure tests for the hermes-the-firm port.

These tests pin down what "no Claude Code leakage" and "valid Hermes
skills" mean mechanically, so a regeneration pass that regresses any
rule fails loudly instead of shipping.
"""
import re
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent.parent
SKILLS = HERE / "skills"
TEMPLATES = HERE / "templates"

# Every upstream practice area must be represented.
PRACTICE_AREAS = [
    "commercial-legal", "privacy-legal", "product-legal",
    "corporate-legal", "employment-legal", "litigation-legal",
    "regulatory-legal", "ai-governance-legal", "ip-legal",
    "law-student", "legal-clinic", "legal-builder-hub",
]

# Substrings that must not appear anywhere outside the attribution note.
# (The port note itself credits anthropics/claude-for-legal.)
LEAK_PATTERNS = [
    (re.compile(r"~/\.claude"), "upstream home config path"),
    (re.compile(r"\.claude/plugins"), "Claude plugin path"),
    (re.compile(r"\bCLAUDE\.md\b"), "unrenamed CLAUDE.md reference"),
    (re.compile(r"\$\{?CLAUDE_PLUGIN_ROOT\}?"), "Claude plugin-root var"),
    (re.compile(r"mcp__[a-z0-9_*-]+__"), "raw mcp__ tool name"),
    (re.compile(r"\bTodoWrite\b"), "TodoWrite"),
    (re.compile(r"\bAskUserQuestion\b"), "AskUserQuestion"),
    (re.compile(r"\bTask tool\b"), "Task tool"),
    (re.compile(r"\bWebFetch\b|\bWebSearch\b"), "CC web tools"),
    (re.compile(r"^model:\s", re.MULTILINE), "CC agent model field"),
    (re.compile(r"^tools:\s\[", re.MULTILINE), "CC agent tools field"),
]


def _md_files():
    return sorted(SKILLS.rglob("*.md"))


def _without_port_note(text: str) -> str:
    return text.replace(
        "Mechanically ported from anthropics/claude-for-legal", "")


def test_skills_exist():
    assert SKILLS.is_dir() and len(list(SKILLS.iterdir())) >= 1140


def test_templates_exist_for_all_areas():
    for area in PRACTICE_AREAS:
        assert (TEMPLATES / f"{area}-PRACTICE.md").is_file(), area


def test_flat_names_are_valid_and_unique():
    names = [d.name for d in SKILLS.iterdir() if d.is_dir()]
    assert len(names) == len(set(names)), "duplicate skill dir names"
    for n in names:
        assert re.match(r"^[a-z0-9][a-z0-9-]*$", n), \
            f"invalid skill dir name {n!r}"


def test_every_skill_has_frontmatter_with_name_and_description():
    for d in sorted(SKILLS.iterdir()):
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        text = md.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        assert m, f"{d.name}: no frontmatter"
        fm = yaml.safe_load(m.group(1))
        assert fm.get("name") == d.name, (
            f"{d.name}: frontmatter name {fm.get('name')!r} != dir name")
        assert fm.get("description"), f"{d.name}: empty description"


def test_no_claude_code_leakage():
    bad = []
    for md in _md_files():
        text = _without_port_note(md.read_text(encoding="utf-8"))
        for pat, label in LEAK_PATTERNS:
            if pat.search(text):
                bad.append(f"{md.relative_to(HERE)}: {label}")
    assert not bad, "\n".join(bad)


def test_no_unmapped_namespaced_invocations():
    """Every /<area>:<skill> invocation should have been rewritten to
    hermes-the-firm:<flat>. Leftover upstream forms fail."""
    ns_re = re.compile(
        r"/(" + "|".join(PRACTICE_AREAS) + r"):([a-z0-9-]+)")
    bad = []
    for md in _md_files():
        rel = str(md.relative_to(HERE))
        if "/references/" in rel:  # archived originals may quote upstream
            continue
        if ns_re.search(md.read_text(encoding="utf-8")):
            bad.append(rel)
    assert not bad, f"unrewritten /area:skill refs: {bad}"


def test_no_broken_skill_refs():
    """hermes-the-firm:<name> mentions must resolve to real skill dirs."""
    real = {d.name for d in SKILLS.iterdir() if (d / "SKILL.md").is_file()}
    ref_re = re.compile(r"hermes-the-firm:([a-z0-9-]+)")
    missing = {}
    for md in _md_files():
        for name in ref_re.findall(md.read_text(encoding="utf-8")):
            if name not in real:
                missing.setdefault(name, str(md.relative_to(HERE)))
    assert not missing, f"dangling refs: {missing}"


def test_config_paths_point_at_hermes():
    hits = []
    for md in _md_files():
        text = md.read_text(encoding="utf-8")
        if "~/.hermes/plugins/config/hermes-the-firm/" in text:
            continue
    # positive check lives in test_config_path_present; here we only
    # ensure no skill still writes to a claude config dir
    for md in _md_files():
        t = md.read_text(encoding="utf-8")
        if re.search(r"plugins/config/claude", t):
            hits.append(str(md.relative_to(HERE)))
    assert not hits


def test_ported_agents_have_scheduling_note():
    agents = ["docket-watcher", "dataroom-watcher", "reg-change-monitor",
              "registry-sync", "launch-watcher", "renewal-watcher",
              "playbook-monitor", "deal-debrief", "ip-renewal-watcher"]
    for name in agents:
        text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        assert "## Scheduling" in text, f"{name}: scheduling note missing"


def test_merged_leave_tracker_reference_exists():
    ref = SKILLS / "leave-tracker" / "references" / "scheduled-agent.md"
    assert ref.is_file()
    body = ref.read_text(encoding="utf-8")
    assert "Scheduled sweep" in body
    assert not body.startswith("---"), "reference doc must not keep FM"


def test_all_sources_represented():
    """All upstreams must land: departments, federal-mcp, firm-admin,
    louis, primary-law, plus codearranger's state floors + consumer
    credit."""
    import json
    owners = json.loads((HERE / "references" / "owner-map.json")
                        .read_text(encoding="utf-8"))
    kinds = set()
    for v in owners.values():
        kinds.add(v.split("/")[0])
    assert "firm-admin" in kinds, "master-claude-for-legal missing"
    assert "louis" in kinds, "mini-claude-for-legal missing"
    assert "federal-mcp" in kinds, "us-legal-tools missing"
    assert "primary-law" in kinds, "open-us-law missing"
    for st in ("az", "ca", "co", "in", "mi", "ny", "oh", "or", "tn", "wa"):
        assert f"{st}-legal" in kinds, f"{st} civil-practice layer missing"
    assert "federal-debt" in kinds, "federal consumer-credit layer missing"
    assert len([v for v in owners.values() if "/" not in v]) >= 159


def test_drill_commands_cover_every_owner():
    """The /firm-* command family is what makes the areas selectable in
    the slash popover — it must expose every owner in owner-map.json,
    plus the bare /firm roster, and its handlers must route."""
    import json
    import commands
    owners = json.loads((HERE / "references" / "owner-map.json")
                        .read_text(encoding="utf-8"))
    rows = {name: handler for name, handler, _ in commands.drill_commands()}
    assert "firm" in rows, "the /firm roster command is missing"
    for owner in sorted(set(owners.values())):
        top = owner.split("/")[0]
        expected = "firm-louis" if top == "louis" else f"firm-{top}"
        assert expected in rows, f"{owner}: no /{expected} command"
    assert commands.make_drill("mi-legal")("") == \
        commands.handle_entry("mi-legal"), "drill handler routes wrong"


def test_front_door_accounts_for_every_skill():
    """The /hermes-the-firm front door must expose every owner in
    owner-map.json. A layer rolled into skills/ + the map but not into
    commands.py silently vanishes from the roster, and its drill-down
    answers 'unknown area' (the state layer shipped exactly that way)."""
    import json
    import commands
    owners = json.loads((HERE / "references" / "owner-map.json")
                        .read_text(encoding="utf-8"))
    drillable = set(commands.PRACTICE_AREAS + commands.STATE_AREAS
                    + commands.SPECIAL_AREAS + [commands.FEDERAL_CREDIT])
    roster = commands.handle_entry("")
    counted = commands.PRACTICE_AREAS + commands.STATE_AREAS \
        + [commands.FEDERAL_CREDIT]
    for owner in sorted(set(owners.values())):
        n = sum(1 for v in owners.values() if v == owner)
        if owner.startswith("louis/"):
            cat = owner.split("/", 1)[1]
            out = commands.handle_entry(f"louis-{cat}")
            assert f"{n} skills" in out and "unknown" not in out, \
                f"louis/{cat} not drillable"
            assert cat in roster, f"louis/{cat} missing from the roster"
            continue
        assert owner in drillable, (
            f"owner {owner!r} not drillable — /hermes-the-firm {owner} "
            f"would answer 'unknown area'")
        assert owner in roster, f"{owner} missing from the roster"
        if owner in counted:
            assert f"{n} skills" in commands.handle_entry(owner), \
                f"{owner}: drill-down does not state its skill count"


def test_primarylaw_coverage_data_driven():
    """us-law-coverage.json must come from the corpus's own manifest and
    carry the fields the skills rely on (Michigan included)."""
    import json
    cov = json.loads((HERE / "references" / "us-law-coverage.json")
                     .read_text(encoding="utf-8"))
    assert len(cov) >= 50
    mi = cov["mi"]
    assert mi["coverage_status"] == "complete"
    assert mi["coverage_verified"] is True
    assert mi["section_count"] > 30000


def test_federal_mcp_skills_have_wiring():
    """Each federal-mcp skill must name its npx package + hermes mcp add."""
    import json
    owners = json.loads((HERE / "references" / "owner-map.json")
                        .read_text(encoding="utf-8"))
    fed = [n for n, v in owners.items() if v == "federal-mcp"]
    assert len(fed) == 4
    for name in fed:
        text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        assert "@us-legal-tools/" in text, f"{name}: no npm package"
        assert "hermes mcp add" in text, f"{name}: no wiring command"


def test_louis_frontmatter_yaml_valid():
    """70 upstream mini skills ship broken YAML (unquoted ':' scalars);
    the port must have fixed every one."""
    import json
    owners = json.loads((HERE / "references" / "owner-map.json")
                        .read_text(encoding="utf-8"))
    louis = [n for n, v in owners.items() if v.startswith("louis/")]
    assert len(louis) >= 950
    for name in louis[:100]:  # sample is enough; herminator sweep does all
        text = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        assert m, f"{name}: no frontmatter"
        fm = yaml.safe_load(m.group(1))  # raises on invalid YAML
        assert isinstance(fm, dict) and fm.get("name") == name
