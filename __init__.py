"""hermes-the-firm plugin entry point.

Opt-in by design: plugin skills cost zero tokens until
skill_view("hermes-the-firm:<name>") is called, so nothing loads at
session start. /hermes-the-firm is the front door (roster), and the
/firm-* command family registers every drill target as its own slash
command so the areas are selectable from the composer's menu. No
lifecycle hooks; there is no process gate to enforce here, only
domain knowledge and a practice-profile config to read.
"""
import logging
from pathlib import Path

try:
    from . import commands  # Hermes package loading
    from .commands import PRACTICE_AREAS
except ImportError:
    import commands  # flat imports (pytest from repo root)
    from commands import PRACTICE_AREAS

_HERE = Path(__file__).parent


def _safe(fn, *args, **kwargs):
    """One malformed skill directory must not take down the plugin."""
    try:
        fn(*args, **kwargs)
    except Exception:
        logging.getLogger("hermes-the-firm").warning(
            "skill registration failed", exc_info=True)


def register(ctx):
    # The one user-facing entry point. Kept deliberately hook-free:
    # registration itself costs nothing per-session.
    ctx.register_command(
        "hermes-the-firm", commands.handle_entry,
        description="Load a legal practice area (roster or <area>)",
        args_hint="[<area>]",
    )
    # The /firm-* family: one command per drill target. Plugin commands
    # are listed in the slash popover with their descriptions, so this
    # makes the departments/states selectable from the command menu —
    # no typed argument needed.
    for name, handler, description in commands.drill_commands():
        _safe(lambda n=name, h=handler, d=description:
              ctx.register_command(n, h, description=d))

    skills_dir = _HERE / "skills"
    if skills_dir.is_dir():
        for d in sorted(skills_dir.iterdir()):
            md = d / "SKILL.md"
            if md.is_file():
                _safe(lambda d=d, md=md: ctx.register_skill(
                    d.name, md,
                    description=f"legal practice skill: {d.name}"))
